
本项目原作者[malinkang](https://github.com/malinkang/)，通过工作流和定时任务将微信读书的数据同步到notion

### 项目简介
本项目将原来代码简化，只保留与微信读书的数据交互部分
- 将微信读书中已读数据和划线，笔记，导出为一个josn文件，目前不做任何处理

### 项目后续
- 考虑后续将json文件持久化到mysql中

最后要实现的效果是如项目[QZoneExport](https://github.com/ShunCai/QZoneExport)所示
执行后会生成一个打包好的前端文件夹，可点击index.html直接打开

最后数据会涵盖包括<br>


|         平台功能         | 最后更新       | 开发状态     | 备注               |
|:--------------------:|------------|----------|------------------|
| 微信读书中已读数据以及相关划线笔记，章节 | 2025-04-01 | ✅ 已完成    | -                |
|      知乎我的收藏、回答       | -          | ❌ 未开始    | 暂时延后             |
|       豆瓣已标记电影        | 2025-04-06 | ✅ 已完成    | -                |
|        机核电台信息        | 2025-04-08 | ✅ 已完成    | -                |
|        掌阅读书信息        | 2025-04-03 | ✅ 已完成    | 无API，数据整合脚本      |
|       网易蜗牛读书信息       | 2025-04-01 | ✅ 已完成    | -                |
|         魅族便签         | 2025-04-02 | ✅ 已完成    | -                |
|        flomo         | 2025-04-08 | ✅ 已完成    | 无API，数据整合脚本      |
|          钱迹          | 2025-04-08 | 官方导出JSON | 无API，app直接导出JSON |



不知道能不能实现<br>
8.小米手环中的个人健康数据<br>
9、整合qq空间内容，也就是QZoneExport项目中的内容

### 项目设置
要设置的仓库密钥如下：

WEREAD_COOKIE - 网页打开微信读书，登录自己的账号后找到 weread.qq.com 的请求，将cook粘出来



