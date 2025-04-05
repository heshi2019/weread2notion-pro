import hashlib
import json
import re
import os
from urllib.parse import urlencode
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry

#掌阅的API探索已放弃，无论是抓包还是浏览器调试，都无法获取到笔记的内容

ZhangYue_data_list = "https://ah2.zhangyue.com/zyuc/api/space/interact"
ZhangYue_URL = "https://ah2.zhangyue.com"

#
# 获取一本书的章节，get请求
# https://api-pc.zhangyue.com/bookstore/open/book/chapter/web/list?book_id=10867543&page=1&size=50&usr=i361520555&zysid=83340d05611f5c280f3f511414787529&p29=zye5b814&p2=104583&p3=101010010&p4=501603&p33=com.chaozh.iReaderFree
#
# 一本书的详细信息，目前知道的是有书籍分类
# https://ah2.zhangyue.com/webintf/ClientApi_Book.BookResourceDetail
#
# 日志请求API
# https://log.ireader.com/log-agent/rlog
#
# 笔记API可能是这个，但是返回内容被加密了
# https://icloud.zhangyue.com/cloud/storage2/safe/downloadDataV2
#
# 疑似DRM密钥
# https://romsdk-mobile.uu.163.com/v4/game
#
# https://dispatcher-mobile.uu.163.com/v4/host
#
# http://fp-it.fengkongcloud.com/v3/cloudconf


class ZhangYueApi:
    def __init__(self):
        self.cookie = self.get_cookie()
        self.session = requests.Session()
        self.session.cookies = self.parse_cookie_string()
        self.session.verify = False  # 禁用SSL验证
        requests.packages.urllib3.disable_warnings()  # 禁用SSL警告

    def get_cookie(self):
        cookie = os.getenv("ZHANGYUE_COOKIE")

        if not cookie or not cookie.strip():
            raise Exception("没有找到cookie，请按照文档填写cookie")
        return cookie

    def parse_cookie_string(self):
        cookies_dict = {}

        # 使用正则表达式解析 cookie 字符串
        pattern = re.compile(r'([^=]+)=([^;]+);?\s*')
        matches = pattern.findall(self.cookie)

        for key, value in matches:
            cookies_dict[key] = value.encode('unicode_escape').decode('ascii')
        # 直接使用 cookies_dict 创建 cookiejar
        cookiejar = cookiejar_from_dict(cookies_dict)

        return cookiejar

    def handle_errcode(self, errcode):
        if (errcode == -2012 or errcode == -2010):
            print(f"::error::Cookie过期了。")

    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_Classification(self):
        self.session.post(ZhangYue_URL)

        for i in range(1, 40):

            params = {"plug": 72,
                      "pluginVersion": 72,
                      "act": "note",
                      "hasTab": 0,
                      # 这个page值需要从1开始，如果超过了最大页数，会返回[]
                      "page": i,
                      "pageSize": 10,
                      "zysid":"",
                      "usr": "",
                      "rgt": "7",
                      "p1": "",
                      "pc": "",
                      "p3": "",
                      "p4": "501603",
                      "p5": "19",
                      "p7": "",
                      "p16": "",
                      "p25": "",
                      "p28": "",
                      "p29": "",
                      "p30": "",
                      "p31": "com.chaozh.iReaderFree",
                      "p32": "",
                      "p33": "",
                      "p34": "",
                      }

            query_params = urlencode(params)

            headers = {
                ":authority": "ah2.zhangyue.com",
                ":method": "GET",
                ":path": "/zyuc/api/space/interact?"+str(query_params),
                ":scheme": "https",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.11.0"
            }

            r = self.session.get(ZhangYue_data_list,headers=headers,params = params)

            if r.ok and r.json().get("data",{}) != {}:
                os.makedirs("Data_Star", exist_ok=True)
                output_path = os.path.join("Data_Star", "ZhangYue_Data_List.json")

                with open(output_path, "w", encoding='utf-8') as f:
                    f.write(json.dumps(r.json().get("data",{}), indent=4, ensure_ascii=False))

            else:
                errcode = r.json().get("errcode", 0)
                self.handle_errcode(errcode)
                raise Exception(f"获取掌阅批注数据信息错误，错误如下： {r.text}")
            return r.json().get("data",{})

