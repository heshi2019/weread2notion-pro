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

        # 使用正则表达式解析 cookie 字符串,不知道这个解析对网易蜗牛能不能生效
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
                      "zysid":"83340d05611f5c280f3f511414787529",
                      "usr": "i361520555",
                      "rgt": "7",
                      "p1": "ffffffffffffffffffffffffff",
                      "pc": "108032",
                      "p3": "18010103",
                      "p4": "501603",
                      "p5": "19",
                      "p7": "__7cd34834c5e81760",
                      "p16": "24031",
                      "p25": "__7cd34834c5e81760",
                      "p28": "__7cd34834c5e81760",
                      "p29": "__7cd34834c5e81760",
                      "p30": "__7cd34834c5e81760",
                      "p31": "com.chaozh.iReaderFree",
                      "p32": "__7cd34834c5e81760",
                      "p33": "Xiaomi",
                      "p34": "__7cd34834c5e81760",
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

