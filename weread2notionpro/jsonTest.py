import json

import pendulum


def main():
    get_notebooklist = {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou',
                        'book': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'title': '世上为什么要有图书馆',
                                 'author': '杨素秋',
                                 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover',
                                 'version': 1668358002, 'format': 'epub', 'type': 0, 'price': 0, 'originalPrice': 0,
                                 'soldout': 0, 'bookStatus': 1, 'payingStatus': 0, 'payType': 134217761, 'centPrice': 0,
                                 'finished': 1, 'free': 1, 'mcardDiscount': 0, 'ispub': 0, 'cpid': 0, 'publishTime': '',
                                 'hasLecture': 0, 'lastChapterIdx': 31, 'paperBook': {'skuId': ''},
                                 'copyrightChapterUids': [], 'limitShareChat': 0, 'blockSaveImg': 0,
                                 'language': 'zh-wr', 'hideUpdateTime': False, 'isEPUBComics': 0, 'isVerticalLayout': 0,
                                 'isShowTTS': 1, 'isHideTTSButton': 0, 'webBookControl': 0,
                                 'selfProduceIncentive': False, 'isAutoDownload': 1}, 'reviewCount': 5,
                        'reviewLikeCount': 0, 'reviewCommentCount': 0, 'noteCount': 5, 'bookmarkCount': 0,
                        'sort': 1737684426}
    String = get_notebooklist.get("bookId")
    title = get_notebooklist.get("book").get("title")
    print(f"bookId：{String}")
    print(f"书名：{title}")

    String2 = ""
    if get_notebooklist.get("categories"):
        String2=get_notebooklist.get("categories").get("title")
    print(f"分类：{String2}")

    name = get_notebooklist.get("book").get("author")
    print(f"作者：{name}")
    String3 = get_notebooklist.get("book").get("cover")
    print(f"封面：{String3}")


    get_chapter_info1 = {'bookId': '3300003969', 'book': {'bookId': '3300003969', 'title': '重走：在公路、河流和驿道上寻找西南联大', 'author': '杨潇', 'cover': 'https://cdn.weread.qq.com/weread/cover/88/cpPlatform_3300003969/s_cpPlatform_3300003969.jpg', 'version': 972366750, 'format': 'epub', 'type': 0, 'price': 68.6, 'originalPrice': 0, 'soldout': 0, 'bookStatus': 1, 'payingStatus': 2, 'payType': 1048577, 'centPrice': 6860, 'finished': 1, 'free': 0, 'mcardDiscount': 0, 'ispub': 1, 'extra_type': 5, 'cpid': 16460839, 'publishTime': '2021-05-01 00:00:00', 'categories': [{'categoryId': 300000, 'subCategoryId': 300002, 'categoryType': 0, 'title': '文学-纪实文学'}], 'hasLecture': 0, 'lastChapterIdx': 48, 'paperBook': {'skuId': '12836419'}, 'copyrightChapterUids': [2], 'blockSaveImg': 0, 'language': 'zh', 'hideUpdateTime': False, 'isEPUBComics': 0, 'isVerticalLayout': 0, 'isShowTTS': 1, 'isHideTTSButton': 0, 'webBookControl': 0, 'selfProduceIncentive': False, 'isAutoDownload': 1}, 'reviewCount': 0, 'reviewLikeCount': 0, 'reviewCommentCount': 0, 'noteCount': 6, 'bookmarkCount': 0, 'sort': 1662656844}

    String1 = get_chapter_info1.get("book").get("categories")[0].get("title")
    print(f"分类：{String1}")

    get_bookinfo = {'bookId': '3300003969', 'title': '重走：在公路、河流和驿道上寻找西南联大', 'author': '杨潇', 'cover': 'https://cdn.weread.qq.com/weread/cover/88/cpPlatform_3300003969/s_cpPlatform_3300003969.jpg', 'version': 972366750, 'format': 'epub', 'type': 0, 'price': 68.6, 'originalPrice': 0, 'soldout': 0, 'bookStatus': 1, 'payType': 1048577, 'intro': '这是单读出版推出的首部长篇非虚构作品，一个青年写作者徒步重走西南联大西迁路的故事。1938年，“湘黔滇旅行团”徒步跨越三省穿过西南腹地；2018年，处于人生转折点的青年作者杨潇重新踏上这条长路。现实中非典型的公路徒步与历史上知识人的流亡之旅交织、对话、共振，层累的、不同的“中国”缓缓浮现。\n杨潇带着海量的史料积累与强大的问题意识，与沿途遇见的人交流，与西南的人文风光交流，与那个遥远的动荡时代交流。在两个不确定的年代，在国家与个人的危机时刻，我们用真实的生命体验，追问思想与行动的关系，开启一个全新的“寻路之年”。', 'centPrice': 6860, 'finished': 1, 'maxFreeChapter': 9, 'maxFreeInfo': {'maxFreeChapterIdx': 9, 'maxFreeChapterUid': 9, 'maxFreeChapterRatio': 32}, 'free': 0, 'mcardDiscount': 0, 'ispub': 1, 'extra_type': 5, 'cpid': 16460839, 'publishTime': '2021-05-01 00:00:00', 'category': '文学-纪实文学', 'categories': [{'categoryId': 300000, 'subCategoryId': 300002, 'categoryType': 0, 'title': '文学-纪实文学'}], 'hasLecture': 0, 'lastChapterIdx': 48, 'paperBook': {'skuId': '12836419'}, 'copyrightChapterUids': [2], 'hasKeyPoint': False, 'blockSaveImg': 0, 'language': 'zh', 'hideUpdateTime': False, 'isEPUBComics': 0, 'isVerticalLayout': 0, 'isShowTTS': 1, 'isHideTTSButton': 0, 'webBookControl': 0, 'selfProduceIncentive': False, 'isAutoDownload': 1, 'payingStatus': 2, 'chapterSize': 48, 'updateTime': 1690530215, 'onTime': 1639389915, 'unitPrice': 0, 'marketType': 0, 'isbn': '9787532179374', 'publisher': '上海文艺出版社', 'totalWords': 395010, 'bookSize': 1499564, 'shouldHideTTS': 0, 'recommended': 0, 'lectureRecommended': 0, 'follow': 0, 'secret': 0, 'offline': 0, 'lectureOffline': 0, 'finishReading': 0, 'hideReview': 0, 'hideFriendMark': 0, 'blacked': 0, 'isAutoPay': 0, 'availables': 0, 'paid': 0, 'isChapterPaid': 0, 'showLectureButton': 1, 'wxtts': 1, 'star': 88, 'ratingCount': 1841, 'ratingDetail': {'one': 36, 'two': 0, 'three': 141, 'four': 4, 'five': 1658, 'recent': 14}, 'newRating': 898, 'newRatingCount': 1692, 'deepVRating': 914, 'showDeepVRatingLabel': 0, 'newRatingDetail': {'good': 1534, 'fair': 130, 'poor': 28, 'recent': 14, 'deepV': 221, 'myRating': '', 'title': '好评如潮'}, 'ranklist': {}, 'copyrightInfo': {'id': 16460839, 'name': '铸刻文化', 'userVid': 0, 'role': 0, 'avatar': '', 'cpType': 0}, 'authorSeg': [{'words': '杨潇', 'highlight': 1, 'authorId': '392193'}], 'coverBoxInfo': {'blurhash': 'K7SY]i9FH?xu%MD%4TM{IU', 'colors': [{'key': '6/4', 'hex': '#b68980'}, {'key': '4/4', 'hex': '#82544d'}, {'key': '3/4', 'hex': '#693b36'}, {'key': '3/6', 'hex': '#74342d'}, {'key': '3/8', 'hex': '#7f2b24'}, {'key': '2/4', 'hex': '#4d2525'}, {'key': '2/6', 'hex': '#571d1f'}, {'key': '2/8', 'hex': '#62101a'}, {'key': '1/4', 'hex': '#370e16'}, {'key': '1/6', 'hex': '#400214'}, {'key': '1/8', 'hex': '#480013'}, {'key': '6/6', 'hex': '#c48375'}, {'key': '4/6', 'hex': '#8f4e44'}, {'key': '9/2', 'hex': '#f2dfda'}, {'key': '4/10', 'hex': '#a63d30'}, {'key': '5/10', 'hex': '#c35946'}, {'key': '5/4', 'hex': '#9c6e66'}, {'key': '8/4', 'hex': '#ecbdb3'}, {'key': '5/8', 'hex': '#b76151'}, {'key': '6/8', 'hex': '#d27c6b'}, {'key': '8/6', 'hex': '#fdb7a6'}, {'key': '7/8', 'hex': '#f09682'}, {'key': '3/12', 'hex': '#940111'}, {'key': '9/12', 'hex': '#ffb89a'}, {'key': '1/100', 'hex': '#d27c6b'}, {'key': '2/100', 'hex': '#f09682'}, {'key': '3/100', 'hex': '#ffffff'}, {'key': '4/100', 'hex': '#F3E8E5'}, {'key': '5/100', 'hex': '#F3E8E5'}, {'key': '6/100', 'hex': '#270500'}], 'dominate_color': {'hex': '#fce0d9', 'hsv': [12.920651632685134, 13.945618847829596, 98.66887203485558]}, 'custom_cover': 'https://weread-1258476243.file.myqcloud.com/bookalphacover/969/3300003969/s_3300003969.jpg', 'custom_rec_cover': 'https://weread-1258476243.file.myqcloud.com/bookreccover/969/3300003969/s_3300003969.jpg'}, 'skuInfo': {'miniProgramId': 'gh_78fd80800407', 'path': '/pages/product/product?pid=29260627&unionid=P-136100358m'}, 'shortTimeRead': {'active': 0}, 'AISummary': ''}

    String4 = get_bookinfo.get("intro")
    print(f"简介：{String4}")

    String5 = get_bookinfo.get("category")
    print(f"分类获取方式2：{String5}")

    get_read_info = {'isSecret': 1, 'finishedBookCount': 72, 'finishedBookIndex': 72, 'finishedDate': 1738751717, 'readingBookCount': 128, 'readingBookDate': 1737382426, 'readingProgress': 100, 'readingReviewId': 'R_386501755_CB.8Bs5zc63491i6ta6t68n69ou', 'canCancelReadstatus': 0, 'markedStatus': 4, 'readingTime': 27171, 'totalReadDay': 6, 'recordReadingTime': 0, 'deepestNightReadTime': 1737827246, 'continueReadDays': 3, 'continueBeginDate': 1737475200, 'continueEndDate': 1737648000, 'showSummary': 1, 'showDetail': 1, 'readDetail': {'totalReadingTime': 27171, 'totalReadDay': 6, 'continueReadDays': 3, 'continueBeginDate': 1737475200, 'continueEndDate': 1737648000, 'deepestNightReadDate': 1737827246, 'beginReadingDate': 1737382426, 'lastReadingDate': 1740067200, 'longestReadingDate': 1737475200, 'avgReadingTime': 4528, 'longestReadingTime': 13451, 'data': [{'readDate': 1737475200, 'readTime': 13451}, {'readDate': 1737561600, 'readTime': 1123}, {'readDate': 1737648000, 'readTime': 7157}, {'readDate': 1737820800, 'readTime': 1059}, {'readDate': 1738684800, 'readTime': 4249}, {'readDate': 1740067200, 'readTime': 105}]}, 'noteCount': 10, 'reviewCount': 5, 'underlineCount': 5, 'markCount': 0, 'recommendReviewCount': 0, 'contentReviewCount': 5, 'bookInfo': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'title': '世上为什么要有图书馆', 'author': '杨素秋', 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover', 'version': 1668358002, 'format': 'epub', 'type': 0, 'soldout': 0, 'bookStatus': 1, 'payType': 134217761, 'finished': 1, 'free': 1, 'mcardDiscount': 0, 'ispub': 0, 'cpid': 0, 'publishTime': '', 'lastChapterIdx': 31, 'paperBook': {'skuId': ''}, 'centPrice': 0, 'copyrightChapterUids': [], 'limitShareChat': 0, 'blockSaveImg': 0, 'language': 'zh-wr', 'hideUpdateTime': False, 'isEPUBComics': 0, 'isVerticalLayout': 0, 'isShowTTS': 1, 'isHideTTSButton': 0, 'selfProduceIncentive': False, 'webBookControl': 0, 'isAutoDownload': 1}}
    String6 = get_read_info.get("markedStatus")
    print(f"阅读状态：{String6}")

    String7 = get_read_info.get("readingProgress")
    print(f"阅读进度：{String7}")

    String8 = get_read_info.get("readingTime")
    print(f"阅读市场（秒）：{String8}")


    String9 = get_read_info.get("totalReadDay")
    print(f"阅读天数：{String9}")

    String11 = get_read_info.get("readDetail").get("beginReadingDate")
    print(f"开始阅读时间：{String11}")

    String10 = pendulum.from_timestamp(get_read_info.get("readDetail").get("beginReadingDate")).to_datetime_string() if get_read_info.get("readDetail").get("beginReadingDate") else None
    print(f"开始阅读时间：{String10}")



    String12 = get_read_info.get("readDetail").get("lastReadingDate")
    print(f"最后阅读时间：{String12}")

    String13 = pendulum.from_timestamp(
    get_read_info.get("readDetail").get("lastReadingDate")).to_datetime_string() if get_read_info.get("readDetail").get("lastReadingDate") else None
    print(f"最后阅读时间：{String13}")


    get_chapter_info = {1: {'chapterUid': 1, 'chapterIdx': 1, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '作者说明', 'wordCount': 93, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter02.xhtml']}, 2: {'chapterUid': 2, 'chapterIdx': 2, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '序', 'wordCount': 3684, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter03.xhtml']}, 3: {'chapterUid': 3, 'chapterIdx': 3, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '初到南院门', 'wordCount': 8596, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter04.xhtml']}, 4: {'chapterUid': 4, 'chapterIdx': 4, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '两个人的图书馆', 'wordCount': 5277, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter05.xhtml']}, 5: {'chapterUid': 5, 'chapterIdx': 5, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_5', 'title': '开会了', 'wordCount': 6909, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter06.xhtml']}, 6: {'chapterUid': 6, 'chapterIdx': 6, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '今日斩获写作素材', 'wordCount': 6540, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter07.xhtml']}, 7: {'chapterUid': 7, 'chapterIdx': 7, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '批评一连串', 'wordCount': 8927, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter08.xhtml']}, 8: {'chapterUid': 8, 'chapterIdx': 8, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '小米稀饭慢火火熬', 'wordCount': 8693, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter09.xhtml']}, 9: {'chapterUid': 9, 'chapterIdx': 9, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '十分吻合“十四运”', 'wordCount': 7380, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter10.xhtml']}, 10: {'chapterUid': 10, 'chapterIdx': 10, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '个人英雄主义', 'wordCount': 8446, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter11.xhtml']}, 11: {'chapterUid': 11, 'chapterIdx': 11, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '真实意见', 'wordCount': 6679, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter12.xhtml']}, 12: {'chapterUid': 12, 'chapterIdx': 12, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '为什么要有图书馆？', 'wordCount': 6602, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter13.xhtml']}, 13: {'chapterUid': 13, 'chapterIdx': 13, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '他想自己走进海水', 'wordCount': 7608, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter14.xhtml']}, 14: {'chapterUid': 14, 'chapterIdx': 14, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '“做题家”，我们一起读诗吧', 'wordCount': 5653, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter15.xhtml']}, 15: {'chapterUid': 15, 'chapterIdx': 15, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '碑帖外不外借', 'wordCount': 5739, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter16.xhtml']}, 16: {'chapterUid': 16, 'chapterIdx': 16, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '“娟娟发屋”与“睡觉无聊”', 'wordCount': 5248, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter17.xhtml']}, 17: {'chapterUid': 17, 'chapterIdx': 17, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_17', 'title': '武侠奶爸', 'wordCount': 6040, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter18.xhtml']}, 18: {'chapterUid': 18, 'chapterIdx': 18, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '在脂肪中寻找肌肉', 'wordCount': 5373, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter19.xhtml']}, 19: {'chapterUid': 19, 'chapterIdx': 19, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_19', 'title': '这一幅里没有爱情', 'wordCount': 7658, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter20.xhtml']}, 20: {'chapterUid': 20, 'chapterIdx': 20, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_20', 'title': '书房里，你不是孤身一人', 'wordCount': 7411, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter21.xhtml']}, 21: {'chapterUid': 21, 'chapterIdx': 21, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '小砝码', 'wordCount': 5476, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter22.xhtml']}, 22: {'chapterUid': 22, 'chapterIdx': 22, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_22', 'title': '山外有山', 'wordCount': 6774, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter23.xhtml']}, 23: {'chapterUid': 23, 'chapterIdx': 23, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '雨打芭蕉', 'wordCount': 4602, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter24.xhtml']}, 24: {'chapterUid': 24, 'chapterIdx': 24, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '雪夜的老虎', 'wordCount': 5835, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter25.xhtml']}, 25: {'chapterUid': 25, 'chapterIdx': 25, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_25', 'title': '阅读树枝的女人', 'wordCount': 6434, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter26.xhtml']}, 26: {'chapterUid': 26, 'chapterIdx': 26, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '石榴果挂满枝头', 'wordCount': 4654, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter27.xhtml']}, 27: {'chapterUid': 27, 'chapterIdx': 27, 'updateTime': 0, 'readAhead': 0, 'tar': 'https://res.weread.qq.com/wrco/tar_CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_27', 'title': '最后的阵地', 'wordCount': 7870, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter28.xhtml']}, 28: {'chapterUid': 28, 'chapterIdx': 28, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '像云杉那样生长', 'wordCount': 6507, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter29.xhtml']}, 29: {'chapterUid': 29, 'chapterIdx': 29, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '书中出现的书名', 'wordCount': 1938, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter30.xhtml']}, 30: {'chapterUid': 30, 'chapterIdx': 30, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '书中出现的作者', 'wordCount': 510, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter31.xhtml']}, 31: {'chapterUid': 31, 'chapterIdx': 31, 'updateTime': 0, 'readAhead': 0, 'tar': '', 'title': '后记', 'wordCount': 2845, 'price': 0, 'paid': 0, 'isMPChapter': 0, 'level': 1, 'files': ['EPUB/xhtml/chapter32.xhtml']}, 1000000: {'chapterUid': 1000000, 'chapterIdx': 1000000, 'updateTime': 1683825006, 'readAhead': 0, 'title': '点评', 'level': 1}}

    # 提取章节ID与标题映射关系（新增代码）
    chapter_title_map = {
        info.get("chapterUid"): info.get("title")
        for uid, info in get_chapter_info.items()
        if isinstance(info, dict) and "title" in info
    }
    print(f"章节ID-标题映射字典: {chapter_title_map}")

    # 这个不对，python字典中的值要求key唯一，这里用的是章节作为key，但其实会有一章中存在多个划线的情况存在
    get_bookmark_list = [{'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'chapterUid': 13, 'bookVersion': 1668358002, 'colorStyle': 5, 'type': 1, 'style': 1, 'range': '11182-11278', 'markText': '我离开时，他让我装一些他母亲自制的凉皮。一个大塑料袋里，微黄的面皮已经切成条，团在一起，有菜籽油的淡淡香气。他用另一个袋子帮我装了豆芽黄瓜和面筋，第三个袋子装上料汁。这么多，我大概要吃好几天。', 'createTime': 1737684426, 'bookmarkId': 'CB_8Bs5zc63491i6ta6t68n69ou_13_11182-11278'}, {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '个人英雄主义', 'chapterUid': 10, 'colorStyle': 5, 'contextAbstract': '', 'markText': '这一天忽上忽下，我刚刚低头认错，却又获得认可。白天，面对眼前的责难，我可以在内心凝固一张盾牌，听戈矛敲击折落的声音。夜晚，背后突如其来的支撑，却骤然让我柔弱，如同一滴热水化开冰层。挂了电话，我眼角里有一股酸楚，直冲鼻腔。', 'range': '5227-5337', 'style': 1, 'type': 1, 'createTime': 1737557004, 'bookmarkId': 'CB_8Bs5zc63491i6ta6t68n69ou_10_5227-5337'}, {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '批评一连串', 'chapterUid': 7, 'colorStyle': 5, 'contextAbstract': '', 'markText': '下一步，我们要购买电子书，某公司宣称自己有几百万册，年费只需两万。他递过来手机，向我展示书库。我输入畅销作者“东野圭吾”，无；“村上春树”，仅一本，而且并非名作；再试试经典作家，“莎士比亚”仅一种，汕头某某出版社。我把手机还给他，我和他的矛盾，是人民群众日益增长的美好生活需求与他的书库不平衡不充分的发展之间的矛盾，暂时不可能调和。', 'range': '4202-4368', 'style': 1, 'type': 1, 'createTime': 1737550347, 'bookmarkId': 'CB_8Bs5zc63491i6ta6t68n69ou_7_4202-4368'}, {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'chapterUid': 6, 'bookVersion': 1668358002, 'colorStyle': 5, 'type': 1, 'style': 1, 'range': '2483-2790', 'markText': '我俩挽在一起走路已经成了习惯，加班时，她给我巧克力，我给她芒果干。我语速很快，容易兴奋，为买到的一只多汁的橙子笑个不停。她慢言细语，没那么欢快，但显然比我沉稳。我过去和学生讲话的书生气在新的工作面前可能太单调了。现在我需要扮演精明、擅长砍价、拍板定局的“大Boss”\u200b，也许声线要提高，体态要正式一些，是不是得穿一双细高跟鞋？小宁需要扮演木讷、手头拮据、拿不定主意的“小管家”——事实上，她不需要扮演，这就是她。\u200b“双簧”是必须的，我用轻笑戳破商人花招，她用愁容表明持家之难。我俩一唱一和，商家渐渐让步。', 'createTime': 1737539352, 'bookmarkId': 'CB_8Bs5zc63491i6ta6t68n69ou_6_2483-2790'}, {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '序', 'chapterUid': 2, 'colorStyle': 5, 'contextAbstract': '', 'markText': '西安这座城市是由西安人填满的，杨素秋的文字是由她所记录的西安人的生机所填满的', 'range': '3365-3403', 'style': 1, 'type': 1, 'createTime': 1737514088, 'bookmarkId': 'CB_8Bs5zc63491i6ta6t68n69ou_2_3365-3403'}]
    bookmark_data = {
        str(info["chapterUid"]): {  # 将章节ID转为字符串作为主键
            "chapterUid": info.get("chapterUid"),
            "markText": info.get("markText", ""),
            "createTime": info.get("createTime")
        }
        for info in get_bookmark_list
        if isinstance(info, dict) and "chapterUid" in info
    }
    bookmark_data = sorted(bookmark_data.items(), key=lambda item: int(item[0]))
    print(f"划线数据: {bookmark_data}")


    get_review_list = [{'abstract': '我们聊得久，续了汤，吃了许多羊肉。走出饭馆时，他跟我说：“第一，下次吃饭还是我付账。第二，你以后多穿平底鞋，矮个子挺好看的，你要自信一点。”', 'atUserVids': [], 'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '真实意见', 'chapterUid': 11, 'content': '这位大爷的观察非常犀利，我没有去过图书馆，不知道这部分的真实，但从高跟鞋这部分，看起来是说到了作者心里并得到了认可。老人家说的文人没有政治智慧确实是实话，自己上班后，才知道不止是工作压力，与其他人斡旋交流，才不至于让自己一直处于被动', 'contextAbstract': '', 'friendship': 0, 'htmlContent': '', 'isPrivate': 1, 'notVisibleToFriends': 0, 'range': '10183-10253', 'createTime': 1737559409, 'title': '', 'type': 1, 'reviewId': '386501755_7XoHSKvzG', 'userVid': 386501755, 'topics': [], 'isLike': 0, 'isReposted': 0, 'book': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'format': 'epub', 'version': 1668358002, 'soldout': 0, 'bookStatus': 1, 'type': 0, 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover', 'title': '世上为什么要有图书馆', 'author': '杨素秋', 'payType': 134217761}, 'chapterIdx': 11, 'chapterTitle': '真实意见', 'author': {'userVid': 386501755, 'name': '谢轲', 'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/s6nAada4KV5F4DZOxlTaNbXcDoSic4lJqeUVshmotzN4trgib6NAib8svxwqINwe0GJfUhurUiaAuWMokDsdYjMg2Q/132', 'isFollowing': 1, 'isFollower': 1, 'isBlacking': 0, 'isBlackBy': 0, 'isHide': 1, 'isV': 0, 'roleTags': [], 'followPromote': '', 'isDeepV': False, 'deepVTitle': '', 'signature': '', 'medalInfo': {'id': 'M3-0-365', 'desc': '阅读天数', 'title': '阅读天数', 'levelIndex': 365}}}, {'abstract': '我不知道她在哭什么，又知道她在哭什么。', 'atUserVids': [], 'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '个人英雄主义', 'chapterUid': 10, 'content': '真的很委屈，生活中我可能就是宁馆这样的人，我理解他的委屈，他的苦楚。所以读到这里我也落泪，', 'contextAbstract': '', 'friendship': 0, 'htmlContent': '', 'isPrivate': 1, 'notVisibleToFriends': 0, 'range': '8227-8246', 'createTime': 1737557373, 'title': '', 'type': 1, 'reviewId': '386501755_7XoFEYl75', 'userVid': 386501755, 'topics': [], 'isLike': 0, 'isReposted': 0, 'book': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'format': 'epub', 'version': 1668358002, 'soldout': 0, 'bookStatus': 1, 'type': 0, 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover', 'title': '世上为什么要有图书馆', 'author': '杨素秋', 'payType': 134217761}, 'chapterIdx': 10, 'chapterTitle': '个人英雄主义', 'author': {'userVid': 386501755, 'name': '谢轲', 'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/s6nAada4KV5F4DZOxlTaNbXcDoSic4lJqeUVshmotzN4trgib6NAib8svxwqINwe0GJfUhurUiaAuWMokDsdYjMg2Q/132', 'isFollowing': 1, 'isFollower': 1, 'isBlacking': 0, 'isBlackBy': 0, 'isHide': 1, 'isV': 0, 'roleTags': [], 'followPromote': '', 'isDeepV': False, 'deepVTitle': '', 'signature': '', 'medalInfo': {'id': 'M3-0-365', 'desc': '阅读天数', 'title': '阅读天数', 'levelIndex': 365}}}, {'abstract': '……', 'atUserVids': [], 'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '小米稀饭慢火火熬', 'chapterUid': 8, 'content': '最后一句是 不争气的裤带咋就解不开。', 'contextAbstract': '妹妹搂了在怀 \t…… \t我和宁馆忍着', 'friendship': 0, 'htmlContent': '', 'isPrivate': 1, 'notVisibleToFriends': 0, 'range': '10222-10224', 'createTime': 1737554460, 'title': '', 'type': 1, 'reviewId': '386501755_7XoCtOGPb', 'userVid': 386501755, 'topics': [], 'isLike': 0, 'isReposted': 0, 'book': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'format': 'epub', 'version': 1668358002, 'soldout': 0, 'bookStatus': 1, 'type': 0, 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover', 'title': '世上为什么要有图书馆', 'author': '杨素秋', 'payType': 134217761}, 'chapterIdx': 8, 'chapterTitle': '小米稀饭慢火火熬', 'author': {'userVid': 386501755, 'name': '谢轲', 'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/s6nAada4KV5F4DZOxlTaNbXcDoSic4lJqeUVshmotzN4trgib6NAib8svxwqINwe0GJfUhurUiaAuWMokDsdYjMg2Q/132', 'isFollowing': 1, 'isFollower': 1, 'isBlacking': 0, 'isBlackBy': 0, 'isHide': 1, 'isV': 0, 'roleTags': [], 'followPromote': '', 'isDeepV': False, 'deepVTitle': '', 'signature': '', 'medalInfo': {'id': 'M3-0-365', 'desc': '阅读天数', 'title': '阅读天数', 'levelIndex': 365}}}, {'abstract': '元旦假期，陈越老师将他主编的一本书寄给我——雅克·朗西埃《无知的教师》，他说：“素秋，我猜你一定会喜欢这本书。”', 'atUserVids': [], 'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '批评一连串', 'chapterUid': 7, 'content': '从这本书开始，我就很喜欢这位作者，看到这一句，莫名感到伤感落泪。只看作者本人，古灵精怪，硕士，博士，大学任职，挂职。他可能吃过很多苦，无论如何，他现在走到了这里，风趣和有趣的人，像是一位朋友，可能我觉得他像是我的一个朋友，委屈的落泪，我吃过很多苦，我有很多话，请有一个人来拥抱我', 'contextAbstract': '', 'friendship': 0, 'htmlContent': '', 'isPrivate': 1, 'notVisibleToFriends': 0, 'range': '12060-12116', 'createTime': 1737552186, 'title': '', 'type': 1, 'reviewId': '386501755_7XozZSZFo', 'userVid': 386501755, 'topics': [], 'isLike': 0, 'isReposted': 0, 'book': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'format': 'epub', 'version': 1668358002, 'soldout': 0, 'bookStatus': 1, 'type': 0, 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover', 'title': '世上为什么要有图书馆', 'author': '杨素秋', 'payType': 134217761}, 'chapterIdx': 7, 'chapterTitle': '批评一连串', 'author': {'userVid': 386501755, 'name': '谢轲', 'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/s6nAada4KV5F4DZOxlTaNbXcDoSic4lJqeUVshmotzN4trgib6NAib8svxwqINwe0GJfUhurUiaAuWMokDsdYjMg2Q/132', 'isFollowing': 1, 'isFollower': 1, 'isBlacking': 0, 'isBlackBy': 0, 'isHide': 1, 'isV': 0, 'roleTags': [], 'followPromote': '', 'isDeepV': False, 'deepVTitle': '', 'signature': '', 'medalInfo': {'id': 'M3-0-365', 'desc': '阅读天数', 'title': '阅读天数', 'levelIndex': 365}}}, {'abstract': '下一步，我们要购买电子书，某公司宣称自己有几百万册，年费只需两万。他递过来手机，向我展示书库。我输入畅销作者“东野圭吾”，无；“村上春树”，仅一本，而且并非名作；再试试经典作家，“莎士比亚”仅一种，汕头某某出版社。我把手机还给他，我和他的矛盾，是人民群众日益增长的美好生活需求与他的书库不平衡不充分的发展之间的矛盾，暂时不可能调和。', 'atUserVids': [], 'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'bookVersion': 1668358002, 'chapterName': '批评一连串', 'chapterUid': 7, 'content': '真是一位有趣的人', 'contextAbstract': '', 'friendship': 0, 'htmlContent': '', 'isPrivate': 1, 'notVisibleToFriends': 0, 'range': '4202-4368', 'createTime': 1737550359, 'title': '', 'type': 1, 'reviewId': '386501755_7Xoy0frCv', 'userVid': 386501755, 'topics': [], 'isLike': 0, 'isReposted': 0, 'book': {'bookId': 'CB_8Bs5zc63491i6ta6t68n69ou', 'format': 'epub', 'version': 1668358002, 'soldout': 0, 'bookStatus': 1, 'type': 0, 'cover': 'https://res.weread.qq.com/wrepub/CB_6sc9LO9L4EOJ6rj6sx7EG5Gl_parsecover', 'title': '世上为什么要有图书馆', 'author': '杨素秋', 'payType': 134217761}, 'chapterIdx': 7, 'chapterTitle': '批评一连串', 'author': {'userVid': 386501755, 'name': '谢轲', 'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/s6nAada4KV5F4DZOxlTaNbXcDoSic4lJqeUVshmotzN4trgib6NAib8svxwqINwe0GJfUhurUiaAuWMokDsdYjMg2Q/132', 'isFollowing': 1, 'isFollower': 1, 'isBlacking': 0, 'isBlackBy': 0, 'isHide': 1, 'isV': 0, 'roleTags': [], 'followPromote': '', 'isDeepV': False, 'deepVTitle': '', 'signature': '', 'medalInfo': {'id': 'M3-0-365', 'desc': '阅读天数', 'title': '阅读天数', 'levelIndex': 365}}}]

    get_review_list1 = {
        # print(info)
        str(info["chapterUid"]): {  # 将章节ID转为字符串作为主键
            "abstract": info.get("abstract"),
            "content": info.get("content", ""),
            "createTime": info.get("createTime"),
            "chapterUid": info.get("chapterUid"),
            "chapterName": info.get("chapterName", "")
        }
        for info in get_review_list

    }
    print(f"笔记数据2：{get_review_list1}")


    get_review_list.extend(get_bookmark_list)
    temp = sort_notes_temp(get_chapter_info1,get_review_list)
    print(f"尝试数据整合{temp}")


def sort_notes_temp(chapter, bookmark_list):
    """对笔记进行排序（纯净版，仅保留核心排序逻辑）"""
    # 1. 主排序逻辑保持不变
    bookmark_list = sorted(
        bookmark_list,
        key=lambda x: (
            x.get("chapterUid", 1),
            0 if (x.get("range", "") == "" or x.get("range").split("-")[0] == "")
            else int(x.get("range").split("-")[0]),
        ),
    )

    notes = []
    if chapter != None:
        # 2. 移除所有Notion相关操作
        d = {}
        # 3. 保留分组逻辑
        for data in bookmark_list:
            chapterUid = data.get("chapterUid", 1)
            if chapterUid not in d:
                d[chapterUid] = []
            d[chapterUid].append(data)

        # 4. 简化后的合并逻辑
        for key, value in d.items():
            if key in chapter:
                # 不再处理blockId
                notes.append(chapter.get(key))
            notes.extend(value)
    else:
        notes.extend(bookmark_list)

    return notes

if __name__ == "__main__":
    main()

