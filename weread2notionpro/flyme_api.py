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
        cookie =""

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

        headers = {
            "sec-ch-ua-platform": "Windows",
            "x-requested-with":"XMLHttpRequest",
            "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "accept-encoding":"gzip, deflate, br, zstd",
            "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Accept":"application/json, text/plain, */*"
        }
        r = self.session.post(Flyme_Classification_URL,headers=headers)

        if r.ok and r.json().get("returnValue",{}).get("data",None) is not None:
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Flyme_Classification.json")

            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(r.json().get("returnValue",{}).get("data"), indent=4, ensure_ascii=False))

        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取分类信息错误，错误如下： {r.text}")
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

        if r.ok and r.json().get("returnValue",{}).get("content",None) is not None:
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Flyme_data.json")

            with open(output_path, "w", encoding='utf-8') as f:
                # 这个post请求返回的数据，如果经过json格式化再写入文件，会导致文件出现莫名其妙的\
                # f.write(r.json().get("returnValue",{}).get("content"))
                f.write(json.dumps(r.json().get("returnValue",{}).get("content"), indent=4, ensure_ascii=False))

        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取笔记信息错误，错误如下： {r.text}")

        return r.json().get("returnValue",{}).get("content")

    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_FirstImg(self,imgUrl):
        self.session.post(Flyme_URL)

        headers = {
            "sec-ch-ua-platform": "Windows",
            "x-requested-with": "XMLHttpRequest",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
        }

        r = self.session.get(imgUrl, headers=headers)

        if r.status_code == 200:
            # 使用更精确的文件名提取方式
            from urllib.parse import urlparse
            parsed_url = urlparse(imgUrl)
            path_parts = parsed_url.path.split('/')

            # 提取倒数第二个路径段作为文件名（示例URL结构：.../filename/uuid）
            filename = path_parts[-2] if len(path_parts) >= 2 else "unknown"

            save_path = os.path.join("FlymeImages", filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, 'wb') as f:
                f.write(r.content)
            print(f"{filename}_图片下载成功")
        else:
            print(f"{imgUrl}_图片下载失败")
