import hashlib
import json
import re
import os
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry

# 播客
Gcores_Radios_URL = "https://www.gcores.com/gapi/v1/latest-radios"

# 首页
Gcores_URL = "https://www.gcores.com"

# 用户id
# Gcores_USER_URL = "https://www.gcores.com/gapi/v1/users/"+userId

# 某个类型的电台
# # https://www.gcores.com/gapi/v1/categories/45/originals

# Gcores_Subject_URL = "https://www.gcores.com/gapi/v1/collections"
# page[limit]=18&page[offset]=0&sort=-updated-at&meta[collections]=%2C

# 获取连载博客
# Gcores_Albums_URL = "https://www.gcores.com/gapi/v1/albums/152/published-audiobooks"


radiosList = []
categoriesList = {}
usersList = {}
albumsList = {}

class GcoresApi:
    def __init__(self):
        self.cookie = self.get_cookie()
        self.session = requests.Session()
        self.session.cookies = self.parse_cookie_string()
        self.session.verify = False  # 禁用SSL验证
        requests.packages.urllib3.disable_warnings()  # 禁用SSL警告

    def get_cookie(self):
        cookie = os.getenv("Gcores_COOKIE")
        cookie = "navAppDownload=2; navJizuFlag=1; navDiscussionFlag=5; navGfusionFlag=5; navBooom2024Flag=5; p_h5_u=733EF180-4BCE-487C-A9E0-ACA552155DC2; acw_tc=0bdd344e17439250001023874e8ecb3d8fcbcddb4fcf2a780b25d050010821; wechatTicket=kgt8ON7yVITDhtdwci0qeVh-oVHCGueploMGrzaCyq87pBNJf7LpDz5vK90E0VmCz1voJbZYIVOZV8zr4tcC1Q; sensorable=true; __snaker__id=Y5P5rCZPWWdq3d1h; gdxidpyhxdE=DyNx9HDU5tTOie1LRrg%2FqbWld2MCMxArkis9GfQy2jUzzf3wTEnIbAXg6P6vf%2Bg7%2FaCtvSmXXnCvpV994qhZTBkJD%5CjzsjJlCW9%5CozwCb5kAsTkOit1JZA6mt0sizBiXEKz3%2FRKZJR3wz9O75rCVWU0XpDxr7dypvwnxHOCG4xaUx08c%3A1743925905823; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193263a1135581-0796947914ffee4-26011951-1821369-193263a11362921%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.gcores.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzMjYzYTExMzU1ODEtMDc5Njk0NzkxNGZmZWU0LTI2MDExOTUxLTE4MjEzNjktMTkzMjYzYTExMzYyOTIxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193263a1135581-0796947914ffee4-26011951-1821369-193263a11362921%22%7D"

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
    def get_HomePage(self):

        headers = {
            "Host": "www.gcores.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            # "Cookie": "navAppDownload=2; navJizuFlag=1; navDiscussionFlag=5; navGfusionFlag=5; navBooom2024Flag=5; p_h5_u=733EF180-4BCE-487C-A9E0-ACA552155DC2; acw_tc=0bdd344e17439250001023874e8ecb3d8fcbcddb4fcf2a780b25d050010821; wechatTicket=kgt8ON7yVITDhtdwci0qeVh-oVHCGueploMGrzaCyq87pBNJf7LpDz5vK90E0VmCz1voJbZYIVOZV8zr4tcC1Q; sensorable=true; __snaker__id=Y5P5rCZPWWdq3d1h; gdxidpyhxdE=DyNx9HDU5tTOie1LRrg%2FqbWld2MCMxArkis9GfQy2jUzzf3wTEnIbAXg6P6vf%2Bg7%2FaCtvSmXXnCvpV994qhZTBkJD%5CjzsjJlCW9%5CozwCb5kAsTkOit1JZA6mt0sizBiXEKz3%2FRKZJR3wz9O75rCVWU0XpDxr7dypvwnxHOCG4xaUx08c%3A1743925905823; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193263a1135581-0796947914ffee4-26011951-1821369-193263a11362921%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.gcores.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzMjYzYTExMzU1ODEtMDc5Njk0NzkxNGZmZWU0LTI2MDExOTUxLTE4MjEzNjktMTkzMjYzYTExMzYyOTIxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193263a1135581-0796947914ffee4-26011951-1821369-193263a11362921%22%7D",

        }
        params = {
            "start": 0,
            "length": 1000,
            "groupUuid": -1
        }
        self.session.get(Gcores_URL, headers=headers, params=params)

    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_Radios(self):
        """获取博客列表"""
        self.get_HomePage()
        for i in range(20, 10000, 20):
            params = {
                "page[limit]": "20",
                "page[offset]": i,
                "include": "radio.category,radio.djs,album",
                "fields[radios]": "title,duration,cover,thumb,published-at,is-published,is-verified,likes-count,comments-count,category,albums,djs",
                "fields[categories]": "name,logo,subscriptions-count",
                "fields[albums]": "title,cover,is-require-privilege,content-type,is-free,owner-type",
                "fields[users]": "nickname,thumb",
                "meta[radios]": ",",
                "meta[categories]": ",",
                "meta[albums]": ",",
                "meta[users]": ",",
                # "Cookie": "navAppDownload=2; navJizuFlag=1; navDiscussionFlag=5; navGfusionFlag=5; navBooom2024Flag=5; p_h5_u=733EF180-4BCE-487C-A9E0-ACA552155DC2; acw_tc=0bdd344e17439250001023874e8ecb3d8fcbcddb4fcf2a780b25d050010821; wechatTicket=kgt8ON7yVITDhtdwci0qeVh-oVHCGueploMGrzaCyq87pBNJf7LpDz5vK90E0VmCz1voJbZYIVOZV8zr4tcC1Q; sensorable=true; __snaker__id=Y5P5rCZPWWdq3d1h; gdxidpyhxdE=DyNx9HDU5tTOie1LRrg%2FqbWld2MCMxArkis9GfQy2jUzzf3wTEnIbAXg6P6vf%2Bg7%2FaCtvSmXXnCvpV994qhZTBkJD%5CjzsjJlCW9%5CozwCb5kAsTkOit1JZA6mt0sizBiXEKz3%2FRKZJR3wz9O75rCVWU0XpDxr7dypvwnxHOCG4xaUx08c%3A1743925905823; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193263a1135581-0796947914ffee4-26011951-1821369-193263a11362921%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.gcores.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzMjYzYTExMzU1ODEtMDc5Njk0NzkxNGZmZWU0LTI2MDExOTUxLTE4MjEzNjktMTkzMjYzYTExMzYyOTIxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193263a1135581-0796947914ffee4-26011951-1821369-193263a11362921%22%7D",
            }

            headers = {
                "Host": "www.gcores.com",
                "Connection": "keep-alive",
                "sec-ch-ua-platform": "Windows",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                "Content-Type": "application/vnd.api+json",
                "sec-ch-ua-mobile": "?0",
                "Accept": "*/*",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.gcores.com/radios",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            }
            print(f"正在同步第{i/20}页，已同步{i}条数据")
            r = self.session.get(Gcores_Radios_URL, headers=headers, params=params)
            if r.json().get("data",[]) == []:
                break
            if r.ok:
                data = r.json().get("included")
                # 筛选数据
                self.get_saveRadiosData(data)
            else:
                errcode = r.json().get("errcode",0)
                self.handle_errcode(errcode)
                raise Exception(f"获取机核博客失败： {r}")

            os.makedirs("Data_End", exist_ok=True)
            output_path = os.path.join("Data_End", "Gcores_Radios.json")
            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(radiosList, indent=4, ensure_ascii=False))

            os.makedirs("Data_End", exist_ok=True)
            output_path = os.path.join("Data_End", "Gcores_Categories.json")
            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(categoriesList, indent=4, ensure_ascii=False))

            os.makedirs("Data_End", exist_ok=True)
            output_path = os.path.join("Data_End", "Gcores_User.json")
            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(usersList, indent=4, ensure_ascii=False))

            os.makedirs("Data_End", exist_ok=True)
            output_path = os.path.join("Data_End", "Gcores_albums.json")
            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(albumsList, indent=4, ensure_ascii=False))

    # 数据筛选
    def get_saveRadiosData(self,radios):

        global categoriesList
        global radiosList
        global usersList

        global albumsList

        for item in radios:
            # 博客
            if item.get("type") == "radios":

                id = item.get("id", "0")

                title = item.get("attributes", {}).get("title", "")
                # 博客时长，秒
                duration = item.get("attributes", {}).get("duration", "")
                # 节目封面图，只是图片名称
                cover = item.get("attributes", {}).get("cover", "")
                # 发布时间
                published_at = item.get("attributes", {}).get("published-at", "")
                # 点赞数
                likes_count = item.get("attributes", {}).get("likes-count", "")
                # 评论数
                comments_count = item.get("attributes", {}).get("comments-count", "")
                # 节目分类，字典
                category = item.get("relationships", {}).get("category", {}).get("data", {})
                # 参与节目的用户，列表
                userList = []
                user = item.get("relationships", {}).get("djs", {}).get("data", [])
                for value in user:
                    userList.append(value.get("id"))
                radiosList.append({"id": id, "title": title, "duration": duration, "cover": cover,
                                   "published_at": published_at, "likes_count": likes_count,
                                   "comments_count": comments_count, "category": category,
                                   "userList": userList})
            # 分类
            elif item.get("type") == "categories":
                if categoriesList.get("id", None) is None:
                    # 分类id
                    id = item.get("id", "0")
                    # 专题名称
                    name = item.get("attributes", {}).get("name", "")
                    # 专题图片
                    categorieImages = item.get("attributes", {}).get("logo", "")
                    # 订阅数
                    subscriptions_count = item.get("attributes", {}).get("subscriptions-count", 0)

                    categoriesList[id] = {"name": name, "images": categorieImages, "subscriptions_count": subscriptions_count}
            # 参与节目用户
            elif item.get("type") == "users":
                if usersList.get("id", None) is None:
                    # 用户id
                    id = item.get("id", "0")
                    # 用户昵称
                    nickname = item.get("attributes", {}).get("nickname", "")
                    # 用户头像
                    nicknameImages = item.get("attributes", {}).get("thumb", "")

                    usersList[id] = {"nickname": nickname, "images": nicknameImages}
            # 连载专题
            elif item.get("type") == "albums":
                if albumsList.get("id", None) is None:
                    id = item.get("id")
                    title = item.get("attributes",{}).get("title","")
                    # 封面
                    cover = item.get("attributes",{}).get("cover","")
                    # 是否需要会员
                    is_require_privilege = item.get("attributes",{}).get("is-require-privilege","")
                    # 是否免费，单独付费内容
                    is_free = item.get("attributes",{}).get("is-free","")

                    albumsList[id] = {"title":title,"cover":cover,"is_require_privilege":is_require_privilege,"is_free":is_free}

            else:
                print(f"未分类数据：{item}")


    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def get_Albums(self,albumsIds):
        global albumsList
        albumsList = [{
            "id": "87",
            "type": "albums",

            "title": "有声书《紫与黑：K.J.帕克短篇小说集》 ",

        }, {
            "id": "152",
            "type": "albums",
            "title": "机核跑团：世界尽头的酒馆",

        }]

        for value in albumsIds:

            Gcores_Albums_URL = "https://www.gcores.com/gapi/v1/albums/"+str(value.get("id"))+"/published-audiobooks"

            for i in range(20, 200, 20):
                params = {
                    "page[limit]": "20",
                    "page[offset]": i,
                    "include": "media,category,albums",
                    "fields[categories]": "name",
                    "fields[radios]": "title,is-free,is-require-privilege,is-limited-free,published-at,duration,comments-count,cover,media,category,albums"
                }

                headers = {
                    "Host": "www.gcores.com",
                    "Connection": "keep-alive",
                    "sec-ch-ua-platform": "Windows",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "Content-Type": "application/vnd.api+json",
                    "sec-ch-ua-mobile": "?0",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.gcores.com/radios",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
                print(f"正在同步连载播客，第{i/20}页，已同步{i}条数据")
                r = self.session.get(Gcores_Albums_URL,params=params)
                if r.json().get("data",[]) == []:
                    break
                if r.ok:
                    data = r.json()
                    # 筛选数据
                    self.get_saveAlbumsData(data)
                else:
                    errcode = r.json().get("errcode",0)
                    self.handle_errcode(errcode)
                    raise Exception(f"获取机核博客失败： {r}")

            os.makedirs("Data_End", exist_ok=True)
            output_path = os.path.join("Data_End", "Gcores_albums_test_1.json")
            with open(output_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(albumsList, indent=4, ensure_ascii=False))


    def get_saveAlbumsData(self,albums):
        temp = []
        for item in albums.get("data",[]):
            temp.append(item.get("id"))

        # albumsList是一个列表，列表中的字典才是要新增数据的地方

        # 专题节目列表
        if albumsList.get("RadiosList",None) is None:
            albumsList["RadiosList"] = temp
        else:
            albumsList["RadiosList"].append(temp)

        # 增加专题介绍
        included = albums.get("included", [])
        if albumsList.get("description",None) is None:
            description = included(len(included)-1).get("attributes",{}).get("description","")
            albumsList["description"] = description

