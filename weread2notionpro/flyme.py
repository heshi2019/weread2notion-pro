import json
import os
import pendulum
from weread2notionpro.flyme_api import FlymeApi


def main():
    print("开始获取笔记数据")
    flyme_api = FlymeApi()

    # 获取分类，这个分类中还有每个分类所包含的笔记个数，要怎样才能利用起来
    Classification = flyme_api.get_Classification()

    # 将分类的id和名车整合为一个字典
    ClassificationDict = {}
    for index in Classification:
        ClassificationDict[Classification[index].get("id")] = Classification[index].get("name")

    # 获取笔记数据
    data = flyme_api.get_Flyme_data()
    # 格式转换
    flyme_list_data = []
    for index in len(data):
        print(f"正在同步魅族便签笔记,一共{len(data)}条，当前是第{index + 1}条。")
        temp = {"uuid": data[index].get("uuid"),"lastUpdate":data[index].get("lastUpdate"),
                "createTime":data[index].get("createTime"),"modifyTime":data[index].get("modifyTime"),
                "body":data[index].get("body"),"title":data[index].get("title"),"firstImg":data[index].get("firstImg"),
                "fileList":data[index].get("fileList"),"topdate":data[index].get("topdate"),"files":data[index].get("files"),
                "groupStatus":ClassificationDict.get(data[index].get("groupStatus")),"firstImgSrc":data[index].get("firstImgSrc")}
        flyme_list_data.append(temp)

    # 输出到json文件
    os.makedirs("Data_End", exist_ok=True)
    output_path = os.path.join("Data_End", "flyme.json")

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(json.dumps(flyme_list_data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()





