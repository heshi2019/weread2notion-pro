import json
import os
import pendulum
from weread2notionpro.gcores_api import GcoresApi


def main():

    gcores_api = GcoresApi()

    print("开始获取机核电台信息")

    # gcores_api.get_Radios()

    temp =[{
        "id": "87",
        "type": "albums",
        "title": "有声书《紫与黑：K.J.帕克短篇小说集》 ",

    },{
        "id": "152",
        "type": "albums",
        "title": "机核跑团：世界尽头的酒馆",

    }]

    gcores_api.get_Albums(temp)




if __name__ == "__main__":
    main()
