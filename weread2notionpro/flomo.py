import json
import os
import pendulum
from weread2notionpro import du_api
from weread2notionpro.flomo_api import FlomoApi
from bs4 import BeautifulSoup
import json

# 网页加载flomo首页时，会发送18个请求，其中某一个将返回数据用户数据，存入浏览器 应用-存储-本地存储空间-key为flomo
# 但我不知道具体哪一个请求会返回具体数据，好在flomo提供了一次性数据导出按钮，会直接生成一个静态html。风格我还挺喜欢的，
# 但依赖于官网的功能总让人不安，解决方案 1.继续想办法解析18个请求；2.flomo提供了编程推送API，可以通过该接口推送数据，则数据可控

# 下面脚本则解析导出的html文件，转为json文件方便后续处理




def main():
    file_path = r'C:\Users\28484\Desktop\谢柯的笔记.html'  # 必须是文件路径！
    data = html_file_to_json(file_path)

    # 保存数据
    os.makedirs("Data_End", exist_ok=True)
    output_path = os.path.join("Data_End", "flomo.json")

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(data)

def html_file_to_json(file_path):  # 参数改为文件路径
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_to_json(html_content)  # 复用原有解析逻辑
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到")
        return None
    except Exception as e:
        print(f"错误：读取文件时发生异常 - {str(e)}")
        return None

def html_to_json(html_content):  # 保留原有解析逻辑，专注于 HTML 处理
    soup = BeautifulSoup(html_content, 'html.parser')
    memos = []
    for memo_div in soup.find_all('div', class_='memo'):
        time = memo_div.find('div', class_='time').text if memo_div.find('div', class_='time') else ''
        content = memo_div.find('div', class_='content').text if memo_div.find('div', class_='content') else ''
        files = [img['src'] for img in memo_div.find_all('img')] if memo_div.find_all('img') else []
        memo = {
            "time": time,
            "content": content,
            "files": files
        }
        memos.append(memo)
    return json.dumps(memos, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
