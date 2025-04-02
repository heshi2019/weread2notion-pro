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
DU_Chapter = "https://p.du.163.com/batch"

class DUApi:
    def __init__(self):
        self.cookie = self.get_cookie()

        self.session = requests.Session()
        self.session.cookies = self.parse_cookie_string()
        # self.session.verify = False  # 禁用SSL验证
        # requests.packages.urllib3.disable_warnings()  # 禁用SSL警告

    def get_cookie(self):
        cookie = os.getenv("DU_COOKIE")
        cookie = "nts_mail_user=xieke6379@163.com:-1:1; NTES_P_UTID=UrJkEbo6qaCix8CzvKLDv9RYUfQ6jpBl|1740655265; P_INFO=xieke6379@163.com|1740655265|1|mail163|00&99|gas&1737599886&mail163#CN&null#10#0#0|&0||xieke6379@163.com; _ntes_nnid=5c0dfee99346d1da44005ae81bccea4a,1742883365014; _ntes_nuid=5c0dfee99346d1da44005ae81bccea4a; _cid=4c1c2f54-d51f-4762-bbcd-7aa96f5f7b41; _xsrf=da8bd23c-16d0-4a34-a06b-30f05b047401; JSESSIONID-WNYD-WEB=1743405976786-C94CF398A3F961E50D7DA4.hzabj-fehtml2img2; hb_MA-9691-1BA279D56416_source=cn.bing.com; X-Auth-Token=e16d7812d9a74dd8a6d132cb1afcc92e"

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

    # 获取笔记列表
    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_book_list(self):
        self.session.get(DU_URL)
        # 这个请求很奇怪，他有一个page参数，但不加也可以，如果加了，按每页100条来请求，后续请求的如第十页的数据，
        # 他会重复返回之前的数据,并不会返回空序列，可使用remove_duplicate_books函数去重

        # params = dict(
        #     time=0,
        #     pageSize=1000,
        #     page=1
        # )

        # for i in range(1, 40):
        #     params = dict(
        #         time=0,
        #         pageSize=100,
        #         page=i,
        #     )
        #
        #     r = self.session.get(DU_BOOKLIST, params=params)
        #     if r.json().get("bookWrappers") == []:
        #         break
        #     else:
        #         if r.ok:
        #             if i == 1:
        #                 book_dataAnnotations.update(r.json())
        #             else:
        #
        #                 book_dataAnnotations["bookWrappers"] = book_dataAnnotations.get("bookWrappers") + r.json().get(
        #                     "bookWrappers")
        #         else:
        #             errcode = r.json().get("errcode", 0)
        #             self.handle_errcode(errcode)
        #             raise Exception(f"获取笔记划线列表错误，错误如下： {r.text}")

        params = dict(
            time=0,
            pageSize=1000,
        )

        r = self.session.get(DU_BOOKLIST, params=params)

        if r.ok:
            r.json()
        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取笔记划线列表错误，错误如下： {r.text}")

        os.makedirs("Data_Star", exist_ok=True)
        output_path = os.path.join("Data_Star", "Du_bookList.json")

        with open(output_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(r.json(), indent=4, ensure_ascii=False))

        return r.json()

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

    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_Chapter(self, bookIdStr):
        self.session.get(DU_URL)

        body = [
            {
                "url": "/book/catalogs.json?bookIds="+bookIdStr,
                "method": "GET"
            }
        ]

        r = self.session.post(DU_Chapter,json=body)
        if r.ok:
            os.makedirs("Data_Star", exist_ok=True)
            output_path = os.path.join("Data_Star", "Du_Chapter.json")

            with open(output_path, "w", encoding='utf-8') as f:
                # 这个post请求返回的数据，如果经过json格式化再写入文件，会导致文件出现莫名其妙的\
                f.write(r.json()[0].get("body"))
        else:
            errcode = r.json().get("errcode", 0)
            self.handle_errcode(errcode)
            raise Exception(f"获取章节信息错误，错误如下： {r.text}")

        return json.loads(r.json()[0].get("body"))


# list中dict去重
def remove_duplicate_books(data):
    unique_book_ids = set()
    new_book_wrappers = []
    for book_wrapper in data.get('bookWrappers', []):
        book_id = book_wrapper['book']['bookId']
        if book_id not in unique_book_ids:
            unique_book_ids.add(book_id)
            new_book_wrappers.append(book_wrapper)
    data['bookWrappers'] = new_book_wrappers
    return data