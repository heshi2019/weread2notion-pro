import json
import os
import pendulum
from weread2notionpro.flyme_api import FlymeApi


def main():
    print("开始获取魅族便签笔记")
    flyme_api = FlymeApi()

    # 获取分类，这个分类中还有每个分类所包含的笔记个数，要怎样才能利用起来
    Classification = flyme_api.get_Classification()

    # 将分类的id和名车整合为一个字典
    ClassificationDict = {}
    for item in Classification:
        ClassificationDict[item.get("id")] = item.get("name")

    # 获取笔记数据
    data = flyme_api.get_Flyme_data()
    # 格式转换
    flyme_list_data = []
    for index,item in enumerate(data):
        print(f"正在同步魅族便签笔记,一共{len(data)}条，当前是第{index + 1}条，创建时间：{item.get("createTime")}")
        temp = {"uuid": item.get("uuid"),"lastUpdate":item.get("lastUpdate"),
                "createTime":item.get("createTime"),"modifyTime":item.get("modifyTime"),
                "body":item.get("body"),"title":item.get("title"),"firstImg":item.get("firstImg"),
                "fileList":item.get("fileList"),"topdate":item.get("topdate"),"files":item.get("files"),
                "firstImgSrc":item.get("firstImgSrc"),
                "groupStatus":ClassificationDict.get(item.get("groupStatus"))}
        flyme_list_data.append(temp)

    #整理图片链接 部分，其实这里可以直接通过API下载图片，但为了知道总图片和目前下载图片个数，
    # 选择了先整理，再下载
    imgList = {}
    for item in flyme_list_data:
        for key,value in item["files"].items():
            imgList[key] = value

    # 图片下载部分
    for index,(key,value) in enumerate(imgList.items()):
        print(f"开始下载图片，一共{len(imgList)},当前是第{index+1}张")
        flyme_api.get_FirstImg(imgList.get(key))


    # 将笔记文字部分输出到json文件
    os.makedirs("Data_End", exist_ok=True)
    output_path = os.path.join("Data_End", "flyme.json")

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(json.dumps(flyme_list_data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()





