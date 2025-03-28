# 微信读书数据导出

本项目原作者[malinkang](https://github.com/malinkang/)，通过工作流和定时任务将微信读书的数据同步到notion

本项目将原来代码简化，只保留与微信读书的数据交互部分
- 将导出为一个josn文件，目前不做任何处理
考虑后续将json文件持久化到mysql中，当然不会只有微信读书，也不会只是存入数据库

最后要实现的效果是如项目[QZoneExport](https://github.com/ShunCai/QZoneExport)所示
执行后会生成一个打包好的前端文件夹，可点击index.html直接打开

最后数据会涵盖包括
1.微信读书中已读数据以及相关划线笔记，章节
2.知乎我的收藏、回答
3.豆瓣已标记电影
4.机核收藏和电台信息

不知道能不能实现
5.小米手环中的个人健康数据



要设置的仓库密钥如下：

WEREAD_COOKIE - 网页打开微信读书，登录自己的账号后找到 weread.qq.com 的请求，将cook粘出来



