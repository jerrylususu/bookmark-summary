# Migrating Dillo from GitHub
- URL: https://dillo-browser.org/news/migration-from-github/
- Added At: 2025-12-01 14:14:01
- Tags: #read

## TL;DR
Dillo项目从GitHub迁移至自托管服务器以规避平台风险，包括兼容性差、单点故障和过度依赖JavaScript等问题。新方案使用cgit和轻量级工具，并设置多镜像保障数据安全，支持离线开发。迁移后GitHub仓库将归档，项目通过捐赠维持运行。

## Summary
Dillo项目计划从GitHub迁移到自托管服务器，并设置多个镜像，以解决GitHub的多种问题。迁移背景是原网站dillo.org在2022年因域名丢失而失效，导致项目数据损失。作者希望避免此类单点故障，确保项目可持续性。

GitHub存在的问题包括：
- 前端严重依赖JavaScript，无法在Dillo浏览器中正常使用（如查看问题、代码或CI日志）。
- 作为单点故障源，GitHub由单一实体控制，可能单方面封禁仓库或账户，导致数据丢失风险。
- 平台速度变慢，影响开发效率，且需持续高速网络连接。
- 采用“推送模型”通知机制，作者更偏好“拉取模型”，便于离线工作。
- 缺乏有效用户管理工具，非技术用户评论可能干扰开发，导致开发者倦怠。
- 过度关注生成式AI，加剧了JavaScript依赖，不利于Dillo用户访问。

自托管方案包括：
- 购买域名dillo-browser.org，搭建轻量VPS托管网站。
- 使用cgit作为Git前端工具，无需JavaScript，兼容Dillo浏览器。
- 开发简易bug跟踪工具buggy，基于Markdown文件生成静态HTML页面，数据存储在Git仓库中，避免数据库依赖。
- 邮件列表存档暂由第三方服务处理。

为分散风险，在Codeberg和Sourcehut设置Git镜像，确保数据冗余。但DNS入口仍是潜在单点故障，可通过邮件列表、Fediverse或IRC等方式应对。

页面使用OpenPGP签名增强权威性，签名与Git镜像同步，防止数据丢失。迁移期间GitHub仓库将持续更新，完成后标记为归档，不删除历史数据以保障下游依赖。项目自托管成本低，预计可维持至少3年，支持通过Liberapay捐赠。
