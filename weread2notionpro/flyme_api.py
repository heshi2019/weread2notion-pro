import hashlib
import json
import re
import os
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry


Flyme_URL = "https://cloud.flyme.cn/"
# 分类请求，post，无载荷
Flyme_Classification_URL = "https://notes.flyme.cn/c/browser/note/gettags"

# 数据请求，post，载荷start=0&length=1000&groupUuid=-1
Flyme_data_URL = "https://notes.flyme.cn/c/browser/note/getnotegroups"



class FlymeApi:
    def __init__(self):
        self.cookie = self.get_cookie()

        self.session = requests.Session()
        self.session.cookies = self.parse_cookie_string()
        self.session.verify = False  # 禁用SSL验证
        requests.packages.urllib3.disable_warnings()  # 禁用SSL警告

    def get_cookie(self):
        cookie = os.getenv("FLYME_COOKIE")
        cookie = "lang=zh_CN; _uid=114155673; _keyLogin=86a80de50f5f1a0b88d091a784f204; _rmtk=e44242fb8e83ae40314485c3635351; DSESSIONID=8cf1c527-5873-4b29-aa66-9adb936628d5; _islogin=true; _uticket=sz_a5e464085a1f3c73bd2cf7343ac1febd; _ckk=sz_3982b332c02e72d6f26fa0b86e32d3b3; _cct=313734bfdb239eeab916d9a07b; JSESSIONID=node01ek3ne3wi4zug5lo3b8xgxq31615857.node0"
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
        self.session.post(Flyme_URL)

        r = self.session.post(Flyme_Classification_URL)
        print(f"这是返回的分类API数据{r.json()}")
        print(f"这是返回的分类API数据1{r.json().get("returnValue",{}).get("data")}")
        if r.ok:
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Flyme_Classification.json")

            with open(output_path, "w", encoding='utf-8') as f:
                # 这个post请求返回的数据，如果经过json格式化再写入文件，会导致文件出现莫名其妙的\
                # f.write(r.json().get("text"))
                # f.write(r.json().get("returnValue",{}).get("data"))
                f.write(json.dumps(r.json().get("returnValue",{}).get("data"), indent=4, ensure_ascii=False))

        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取章节信息错误，错误如下： {r.text}")
        return r.json().get("returnValue",{}).get("data")


    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_Flyme_data(self):
        self.session.post(Flyme_URL)

        params = {"start": 0, "length": 1000, "groupUuid": -1}

        headers = {
            "sec-ch-ua-platform": "Windows",
            "x-requested-with":"XMLHttpRequest",
            "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "accept-encoding":"gzip, deflate, br, zstd",
            "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Accept":"application/json, text/plain, */*"
        }

        r = self.session.post(Flyme_data_URL,headers=headers, params=params)
        print(f"这是返回的数据API数据{r.json()}")
        print(f"这是返回的数据API数据1{r.json().get("returnValue",{}).get("content")}")
        if r.ok:
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Flyme_data.json")

            with open(output_path, "w", encoding='utf-8') as f:
                # 这个post请求返回的数据，如果经过json格式化再写入文件，会导致文件出现莫名其妙的\
                # f.write(r.json().get("returnValue",{}).get("content"))
                f.write(json.dumps(r.json().get("returnValue",{}).get("content"), indent=4, ensure_ascii=False))

        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取章节信息错误，错误如下： {r.text}")

        return r.json().get("returnValue",{}).get("content")