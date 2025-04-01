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

    books = Books.get("bookWrappers")

    bookIdStr = ""
    BookList = {}
    if books!= None:

        for index, book in enumerate(books):

            # 书名
            title = book.get("book").get("title")



            # 书籍id
            bookId = book.get("book").get("bookId")
            bookIdStr = bookIdStr + str(bookId) + ","


            print(f"正在同步《{title}》,一共{len(books)}本，当前是第{index + 1}本。")


            # 简介
            description = book.get("book").get("description")
            # 封面连接
            imageUrl = book.get("book").get("imageUrl")
            # 阅读状态，-1为读完
            ReadStatus = book.get("book").get("status")
            # 字数
            wordCount = book.get("book").get("wordCount")
            # isbn
            isbn = book.get("book").get("isbn")
            # 出版时间 unix时间戳 毫秒
            publishTime = book.get("book").get("publishTime")
            # 出版社
            publisher = book.get("book").get("publisher")
            # 最后阅读时间 unix时间戳 毫秒
            LastReadTime = book.get("book").get("updateTime")
            # 分类
            category = book.get("category").get("name")
            # 作者,列表
            authors = []
            for author in book.get("authors"):
                authors.append(author.get("name"))

            # 书籍信息整合
            BookInformation = {"bookId":bookId,"title":str(title),"description":description,"imageUrl":imageUrl,
                               "ReadStatus":ReadStatus,"wordCount":wordCount,"isbn":isbn,"publishTime":publishTime,
                               "publisher":publisher,"LastReadTime":LastReadTime,"category":category,"authors":authors
                               }
            BookList[title] = BookInformation



    Chapter = du_api.get_Chapter(bookIdStr)

    BookAnnotations = du_api.get_Annotations()

    MyExtend(BookList,BookAnnotations, Chapter)
    # 遍历书籍


    # os.makedirs("Data_End", exist_ok=True)
    # output_path = os.path.join("Data_End", "du.json")
    #
    # with open(output_path, "w", encoding='utf-8') as f:
    #     f.write(json.dumps(book_message, indent=4, ensure_ascii=False))

def MyExtend(BookList,BookAnnotations, Chapter):
    for title, BookInformation in BookList.items():
        # 章节信息
        pass
    # print(f"这是章节信息{Chapter}")
    # print(f"这是数据信息{BookList}")
    # print(f"这是划线信息{BookAnnotations}")

    BookListAll = {}
    for mes in Chapter.get("catalogs"):
        idNUmer = 1
        for mes_1 in mes.get("catalog"):
            if mes.get("children") == []:
                BookListAll[mes.get("bookId")][mes_1.get("articleId")]={"articleId":mes_1.get("articleId"),"title":mes_1.get("title")}
                BookListAll[mes.get("bookId")]["1000000"].append({idNUmer:mes_1.get("title")})
                idNUmer = idNUmer + 1
            elif mes.get("children") != []:
                idNUmerF = 0.1
                BookListAll[mes.get("bookId")]["1000000"].append({idNUmer: mes_1.get("title")})
                for mes_2 in mes.get("children"):
                    BookListAll[mes.get("bookId")][mes_2.get("articleId")]={"articleId":mes_2.get("articleId"),"title":mes_2.get("title")}
                    BookListAll[mes.get("bookId")]["1000000"].append({idNUmer+idNUmerF: mes_2.get("title")})
                    idNUmerF = idNUmerF + 0.1
    print(BookListAll)





def assemble_BookMessage(MyExtendList,BookInformation):

    BookInformation['chapter'] = MyExtendList
    title = BookInformation['title']

    global book_message
    book_message[title] = BookInformation


if __name__ == "__main__":
    main()
