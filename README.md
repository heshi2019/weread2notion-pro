---
2024.11.22
该项目暂停使用，目前项目中的热力图是通过将数据发送到原博主的服务器https://heatmap.malinkang.com/  进行渲染，目前不清楚数据泄露风险

具体代码查看read_time.py  88行

---


# 将微信读书划线和笔记同步到Notion


本项目通过Github Action每天定时同步微信读书划线到Notion。

本项目原作者[malinkang](https://github.com/malinkang/)，感谢大佬的开源项目


步骤还是一样，详情请看douban2notion

本次要设置的变量如下所示：

WEREAD_COOKIE - 网页打开微信读书，登录自己的账号后找到 weread.qq.com 的请求，将cook粘出来

NOTION_TOKEN

NOTION_PAGE

这两个变量用这个链接获取[授权notion微信读书模板链接](https://api.notion.com/v1/oauth/authorize?client_id=f86ce456-f9cb-4cd5-8e4b-07bd9e18a8f8&response_type=code&owner=user&redirect_uri=https%3A%2F%2Fnotion-auth.malinkang.com%2Fweread2notionpro-oauth-callback)



