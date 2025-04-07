import hashlib
import json
import re
import os
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry



Flomo_URL = "https://v.flomoapp.com/mine"
Flomo_URL_V1 = "https://h5.udrig.com/app/v1"


class FlomoApi:
    def __init__(self):
        self.cookie = self.get_cookie()
        self.session = requests.Session()
        self.session.cookies = self.parse_cookie_string()
        self.session.verify = False  # 禁用SSL验证
        requests.packages.urllib3.disable_warnings()  # 禁用SSL警告

    def get_cookie(self):
        cookie = os.getenv("FLOMO_COOKIE")
        cookie =""


        if not cookie or not cookie.strip():
            raise Exception("没有找到cookie")
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

    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_flomo_data(self):

        print("正在请求数据")
        headers = {
            # 移除冒号开头的非标准请求头
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Sec-Ch-Ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",  # 修正平台标识格式
            "Upgrade-Insecure-Requests": "1",
            "Referer": "https://flomoapp.com/"
        }

        r = self.session.get(Flomo_URL,headers=headers)

        if r.ok:

            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Flomo_Data.json")

            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(r.json(), indent=4, ensure_ascii=False))

        else:
            raise Exception(f"获取flomo数据错误： {r}")
        return r.json()
    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_flomo_data1(self):

        print("正在请求数据")
        headers = {
            # 移除所有冒号开头的伪头字段
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://flomoapp.com/",
            "Sec-Ch-Ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",  # 移除转义引号
            "X-Requested-With": "XMLHttpRequest"  # 新增常用头字段
        }

        params = {"deviceId":"C4AJIDWQ95G4PKEX","appkey":"BCD64148B62C444EB9E37DE24F7912C2","appProfile":{"versionName":"4.0.0","versionCode":"20240710103954","initTime":1744049531732,"sdkVersion":"H5+APP+v1.0.6","partner":""},"deviceProfile":{"pixel":"1707*1067*1.5","language":"zh-CN","timezone":8},"msgs":[{"type":2,"data":{"id":"C4AJIDWQ95G4PKEX1744049531734000","start":1744049531734,"status":2,"duration":0,"pages":[{"name":"https://v.flomoapp.com/mine","start":1744049945032,"duration":19,"refer":"https://v.flomoapp.com/mine"},{"name":"https://v.flomoapp.com/mine","start":1744049964112,"duration":0,"refer":"https://v.flomoapp.com/mine"}],"events":[{"count":1,"start":1744049963178,"id":"页面访问_随机漫步","label":"","params":{"普通用户":True,"关闭":"关闭","browser":"Chrome"}},{"count":1,"start":1744049963180,"id":"页面访问_历史版本","label":"","params":{"普通用户":True,"关闭":"关闭","browser":"Chrome"}}]}}]}
        r = self.session.post(Flomo_URL_V1,headers=headers,params=params)

        if r.ok:

            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Flomo_Data_V1.json")

            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(r.json(), indent=4, ensure_ascii=False))

        else:
            raise Exception(f"获取flomo数据错误： {r}")
        return r.json()
