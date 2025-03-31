import hashlib
import json
import re
import os
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry

#网易蜗牛读书的这个API很神奇，只有在第一次下载并登录时，会将所有的笔记和阅读数据发送过来
# 并且没有根据书名id来获取具体笔记的API，会一次性将所有的笔记和阅读数据发送过来，所以只能通过这个API来获取笔记和阅读数据
DU_URL = "https://du.163.com/"
DU_BOOKLIST = "https://p.du.163.com/bookshelf/book/history.json"
DU_Annotations = "https://p.du.163.com/booknote/sync.json"

#context.json请求获取cook

class DUApi:
    def __init__(self):
        self.cookie = self.get_cookie()

        self.session = requests.Session()
        self.session.cookies = self.parse_cookie_string()
        # self.session.verify = False  # 禁用SSL验证
        # requests.packages.urllib3.disable_warnings()  # 禁用SSL警告
    def get_cookie(self):
        cookie = os.getenv("DU_COOKIE")


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
            print(f"::error::Cookie过期了，请参考文档重新设置。https://mp.weixin.qq.com/s/B_mqLUZv7M1rmXRsMlBf7A")

    # 获取笔记列表
    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_book_list(self):
        self.session.get(DU_URL)

        params = dict(
            limit=3000,
        )


        # r = self.session.get(DU_BOOKLIST, headers=headers, params=params)
        r = self.session.get(DU_BOOKLIST, params=params)
        if r.ok:
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Du_bookList.json")

            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(r.json(), indent=4, ensure_ascii=False))

            return r.json()
        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取笔记列表错误，错误如下： {r.text}")


    # 获取某本书的笔记
    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_Annotations(self):
        self.session.get(DU_URL)
        book_dataAnnotations = {}

        for i in range(1, 40):
            params = dict(
                time=0,
                pageSize=100,
                page=i,
            )

            r = self.session.get(DU_Annotations, params=params)
            if r.json().get("updated") == [] :
                break
            else:
                if r.ok:
                    if i == 1:
                        book_dataAnnotations.update(r.json())
                    else:

                        book_dataAnnotations["updated"] = book_dataAnnotations.get("updated")+r.json().get("updated")
                else:
                    errcode = r.json().get("errcode", 0)
                    self.handle_errcode(errcode)
                    raise Exception(f"获取笔记划线列表错误，错误如下： {r.text}")

        os.makedirs("Data_Star", exist_ok=True)
        output_path = os.path.join("Data_Star", "Du_Annotations.json")

        with open(output_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(book_dataAnnotations, indent=4, ensure_ascii=False))

        return book_dataAnnotations