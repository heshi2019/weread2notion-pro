import json
import os

import pendulum

from weread2notionpro import du_api
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
            print(title)
            # if "刺杀骑士团长" not in title:
            #     continue  # 跳过不符合条件的书籍


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

    temp = MyExtend(BookList,BookAnnotations, Chapter)

    # print(f"这是整合后的信息{temp}")


    os.makedirs("Data_End", exist_ok=True)
    output_path = os.path.join("Data_End", "du.json")

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(json.dumps(temp, indent=4, ensure_ascii=False))

def MyExtend(BookList,BookAnnotations, Chapter):

    # 章节信息
    BookListAll = {}
    for mes in Chapter.get("catalogs"):
        num = 1.0
        BookList_OneBooke = {}
        BookListAll_temp = {}

        for mes_1 in mes.get("catalog"):
            if mes_1.get("children") == []:
                BookList_OneBooke[mes_1.get("articleId")] = {"title":mes_1.get("title")}

                BookListAll_temp[num] = mes_1.get("title")
                num = num + 1

            elif mes_1.get("children") != []:
                numF = 0.01
                BookListAll_temp[num] = mes_1.get("title")

                for mes_2 in mes_1.get("children"):
                    BookList_OneBooke[mes_2.get("articleId")] = {"title":mes_2.get("title")}
                    BookListAll_temp[round(num + numF,2)] = mes_2.get("title")
                    numF = numF + 0.01
                num = num + 1
        BookList_OneBooke[1000000] = BookListAll_temp
        BookListAll[mes.get("bookId")] = BookList_OneBooke
    print(f"这是整合后的章节信息{BookListAll}")

    # 划线信息
    BookListAnnotations = {}

    for BookInformation in BookAnnotations.get("updated"):

        bookId = str(BookInformation.get("bookNote").get("bookId"))
        # if bookId != "5180007350420015658":
        #     continue  # 跳过不符合条件的书籍
        print(f"这是测试数据：{BookInformation}")
        articleId = str(BookInformation.get("bookNote").get("articleId"))


        if BookListAnnotations.get(bookId,{}).get(articleId,{}) != {}:
            temp = BookListAnnotations[bookId].get(articleId)
        else:
            temp = []

        markText = BookInformation.get("bookNote").get("markText")
        remark = BookInformation.get("bookNote").get("remark")
        createTime = BookInformation.get("bookNote").get("createTime")
        uploadTime = BookInformation.get("bookNote").get("uploadTime")

        if remark == "" :
            temp.append({"markText":markText,"createTime":str(createTime),"uploadTime":str(uploadTime)})

        else :
            temp.append({"markText":markText,"remark":remark,"createTime":str(createTime),"uploadTime":str(uploadTime)})

        if BookListAnnotations.get(bookId, {}) == {}:
            BookListAnnotations[bookId]= {articleId: temp}
        else:
            BookListAnnotations[bookId][articleId] = temp

    print(f"这是整合后的划线信息{BookListAnnotations}")

    for title in BookListAll:
        for key,value in BookListAll[title].items():
            if key == 1000000:
                continue
            print(f"测试2：{BookListAnnotations.get(str(title),{})}")
            print(f"测试2：{BookListAnnotations.get(str(title),{}).get(str(key),None)}")
            BookListAll[title][key]["markText"] = BookListAnnotations.get(str(title),{}).get(str(key),None)

    print(f"这是整合1后的划线信息{BookListAll}")

    for title, BookInformation in BookList.items():
        print(title, BookInformation)
        BookList[title]["chapter"] = BookListAll.get(BookInformation.get("bookId"))

    return BookList
def assemble_BookMessage(MyExtendList,BookInformation):

    BookInformation['chapter'] = MyExtendList
    title = BookInformation['title']

    global book_message
    book_message[title] = BookInformation


if __name__ == "__main__":
    main()
