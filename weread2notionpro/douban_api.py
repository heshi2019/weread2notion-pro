import hashlib
import json
import re
import os
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry

DOUBAN_API_HOST = os.getenv("DOUBAN_API_HOST", "frodo.douban.com")
DOUBAN_API_KEY = os.getenv("DOUBAN_API_KEY", "0ac44ae016490db2204ce0a042db2916")

AUTH_TOKEN = os.getenv("AUTH_TOKEN")




class DouBanApi:
    def __init__(self):
        pass

    # def __init__(self):
    #     self.cookie = self.get_cookie()
    #     self.session = requests.Session()
    #     self.session.cookies = self.parse_cookie_string()
    #     self.session.verify = False  # 禁用SSL验证
    #     requests.packages.urllib3.disable_warnings()  # 禁用SSL警告
    #
    # def get_cookie(self):
    #     cookie = os.getenv("DOUBAN_COOKIE")
    #
    #     cookie = ""
    #
    #     if not cookie or not cookie.strip():
    #         raise Exception("没有找到cookie，请按照文档填写cookie")
    #     return cookie
    #
    # def parse_cookie_string(self):
    #     cookies_dict = {}
    #
    #     # 使用正则表达式解析 cookie 字符串,不知道这个解析对网易蜗牛能不能生效
    #     pattern = re.compile(r'([^=]+)=([^;]+);?\s*')
    #     matches = pattern.findall(self.cookie)
    #
    #     for key, value in matches:
    #         cookies_dict[key] = value.encode('unicode_escape').decode('ascii')
    #     # 直接使用 cookies_dict 创建 cookiejar
    #     cookiejar = cookiejar_from_dict(cookies_dict)
    #
    #     return cookiejar
    #
    # def handle_errcode(self, errcode):
    #     if (errcode == -2012 or errcode == -2010):
    #         print(f"::error::Cookie过期了。")
    #
    #


    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def fetch_subjects(self,user,status):


        headers = {
            "host": DOUBAN_API_HOST,
            "authorization": f"Bearer {AUTH_TOKEN}" if AUTH_TOKEN else "",
            "user-agent": "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001023) NetType/WIFI Language/zh_CN",
            "referer": "https://servicewechat.com/wx2f9b06c1de1ccfca/84/page-frame.html",
        }

        offset = 0
        page = 0

        url = f"https://{DOUBAN_API_HOST}/api/v2/user/{user}/interests"
        total = 0
        results = []

        while True:
            params = {
                "type": "movie",
                "count": 50,
                "status": status,
                "start": offset,
                "apiKey": DOUBAN_API_KEY,
            }
            response = requests.get(url, headers=headers, params=params)

            if response.ok:
                response = response.json()
                interests = response.get("interests")
                if len(interests) == 0:
                    break
                results.extend(interests)
                print(f"total = {total}")
                print(f"size = {len(results)}")
                page += 1
                offset = page * 50

        # 将笔记文字部分输出到json文件
        os.makedirs("Data_Star", exist_ok=True)
        output_path = os.path.join("Data_Star", "douban_"+status+".json")

        with open(output_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(results, indent=4, ensure_ascii=False))

        return results


    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def getErr_id(self,id):
        headers = {
            # "content-type":"text/html; charset=utf-8",
            "referer":"https://m.douban.com/",
            "user-agent": "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001023) NetType/WIFI Language/zh_CN",
        }

        url = f"https://movie.douban.com/subject/"+id+"/"

        response = requests.get(url, headers=headers)

        if response.ok:
            # 保存数据
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "douban_"+id+".json")

            with open(output_path, "w", encoding='utf-8') as f:
                f.write(response.text.strip())


            return response.text.strip()





