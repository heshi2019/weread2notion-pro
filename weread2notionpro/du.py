import json
import os

import pendulum

from weread2notionpro.du_api import DUApi

# 所有数据信息，全局变量
book_message = None

def main():
    # 清空
    global book_message
    book_message = {}

    du_api = DUApi()

    #微信读书API，获取基本数据
    Books = du_api.get_book_list()

    BookAnnotations = du_api.get_Annotations()

    print(Books)
    print(BookAnnotations)


    os.makedirs("Data_End", exist_ok=True)
    output_path = os.path.join("Data_End", "du.json")

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(json.dumps(book_message, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
