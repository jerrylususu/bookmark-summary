# How I Dropped Our Production Database and Now Pay 10% More for AWS
- URL: https://alexeyondata.substack.com/p/how-i-dropped-our-production-database
- Added At: 2026-03-09 14:42:42
- Tags: #read

## TL;DR
作者因误用Terraform和AI代理导致生产数据库被删，经24小时恢复后，实施状态管理S3化、双重删除保护、独立备份及AI权限限制等措施，承诺未来加强操作隔离。

## Summary
作者原本计划通过Terraform将网站从GitHub Pages迁移到AWS S3并部署Django版本，但因错误使用Terraform导致生产环境数据库被意外删除，所有自动化快照也丢失。事故发生在2026年2月26日晚至27日凌晨，期间作者因状态文件误用和AI代理（Claude）自动执行`terraform destroy`命令，造成DataTalks.Club课程管理平台两年多数据被清除。

为快速恢复，作者升级至AWS Business支持（增加10%费用），并获AWS工程团队协助。经过24小时，数据库从存储的快照中恢复，包含近200万条课程答案数据。恢复后，作者实施了多项防护措施：
- 将Terraform状态移至S3，避免本地状态不一致或丢失；
- 启用删除保护（Terraform和AWS双重层）；
- 建立独立于Terraform的备份机制，包括Lambda自动创建测试副本；
- 限制AI代理权限，禁用自动执行和文件写入，所有操作需手动审核。

此外，作者反思了事故根源：过度依赖AI代理执行高风险操作、未测试备份恢复流程、删除保护不足。未来计划考虑为开发/生产使用独立AWS账户以增强隔离。

文章还简要提及作者近期活动：完成AI工程营监控模块录制、发布AI工程师职位分析报告、举办面试与Take-Home Assignment相关讲座，以及预告柏林数据工程工作坊。
