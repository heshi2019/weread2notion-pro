import json
import os
import pendulum
from weread2notionpro import du_api
from weread2notionpro.du_api import DUApi


def main():
    du_api = DUApi()

    #网易蜗牛读书API，获取基本数据
    Books = du_api.get_book_list()

    books = Books.get("bookWrappers")

    bookIdStr = ""
    BookList = {}

    if books!= None:
        for index, book in enumerate(books):

            # 书名
            title = book.get("book").get("title")
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

    # 获取对应数据id章节
    Chapter = du_api.get_Chapter(bookIdStr)
    # 获取划线信息
    Annotations = du_api.get_Annotations()
    # 整合书籍，划线，章节信息
    temp = MyExtend(BookList,Annotations, Chapter)

    # 保存数据
    os.makedirs("Data_End", exist_ok=True)
    output_path = os.path.join("Data_End", "du.json")

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(json.dumps(temp, indent=4, ensure_ascii=False))

def MyExtend(BookList,Annotations, Chapter):

    # 章节信息
    BookCh = {}
    for mes in Chapter.get("catalogs"):
        
        num = 1.0
        # 一本书的章节
        BookList_OneBooke = {}
        # 全章节信息
        BookCh_temp = {}

        for mes_1 in mes.get("catalog"):
            if mes_1.get("children") == []:
                BookList_OneBooke[mes_1.get("articleId")] = {"title":mes_1.get("title")}

                BookCh_temp[num] = mes_1.get("title")
                num = num + 1

            elif mes_1.get("children") != []:
                # 这里的小节，0.01则每章节最大为99小节，且最后写入时需要指定保留两位小数，否则会导致会导致数字自动扩展为10位左右
                numF = 0.01
                BookCh_temp[num] = mes_1.get("title")

                for mes_2 in mes_1.get("children"):
                    BookList_OneBooke[mes_2.get("articleId")] = {"title":mes_2.get("title")}
                    BookCh_temp[round(num + numF,2)] = mes_2.get("title")
                    numF = numF + 0.01
                num = num + 1
                
        BookList_OneBooke[1000000] = BookCh_temp
        BookCh[mes.get("bookId")] = BookList_OneBooke

    # 划线信息
    BookAn = {}

    for BookInformation in Annotations.get("updated"):
        # 这两个数字需要转换为字符串，否则再次提取时会报错
        bookId = str(BookInformation.get("bookNote").get("bookId"))
        # 章节id
        articleId = str(BookInformation.get("bookNote").get("articleId"))
        
        # 如果temp不初始化，会报错
        if BookAn.get(bookId,{}).get(articleId,{}) != {}:
            temp = BookAn[bookId].get(articleId)
        else:
            temp = []
        # 划线
        markText = BookInformation.get("bookNote").get("markText")
        # 笔记
        remark = BookInformation.get("bookNote").get("remark")
        # 创建时间
        createTime = BookInformation.get("bookNote").get("createTime")
        # 更新时间
        uploadTime = BookInformation.get("bookNote").get("uploadTime")

        #拼接
        temp.append({"markText":markText,"remark":remark,"createTime":str(createTime),"uploadTime":str(uploadTime)})
        
        # 还是BookAn需要初始化，否则报错。并且分不同的赋值方式，否则会被覆盖
        if BookAn.get(bookId, {}) == {}:
            BookAn[bookId]= {articleId: temp}
        else:
            BookAn[bookId][articleId] = temp
            
    # 章节和笔记整合
    for title in BookCh:
        for key,value in BookCh[title].items():
            if key == 1000000:
                continue
            BookCh[title][key]["markText"] = BookAn.get(str(title),{}).get(str(key),None)
    # 书籍和章节，笔记整合
    for title, BookInformation in BookList.items():
        BookList[title]["chapter"] = BookCh.get(BookInformation.get("bookId"))

    return BookList

if __name__ == "__main__":
    main()
