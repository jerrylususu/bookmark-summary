# Some notes on starting to use Django
- URL: https://jvns.ca/blog/2026/01/27/some-notes-on-starting-to-use-django/
- Added At: 2026-01-29 15:18:27
- Tags: #read #tips #python

## TL;DR
Julia Evans分享了学习Django框架的积极体验，赞赏其显式文件结构、强大ORM、自动迁移和丰富内置功能，文档质量高。尽管对settings.py的全局变量设计略有担忧，但总体满意，计划继续探索表单验证等特性。

## Summary
作者Julia Evans分享了她开始学习Django框架的初步体验。她喜欢学习成熟的老牌技术，因为问题大多已有解决方案，能快速上手。

首先，与Rails相比，Django更显式，文件结构清晰（如urls.py、models.py等），便于长期维护，无需依赖隐式约定。

其次，Django内置的管理界面易于自定义，只需少量代码即可配置字段显示和搜索。

第三，ORM功能强大，使用双下划线表示JOIN操作，简化了复杂查询，虽然作者过去偏好手写SQL，但现在认为ORM更便捷。

第四，自动迁移功能能根据模型变更生成脚本，方便数据库模式管理。

第五，文档质量高，得益于社区文化，提供了实用指南。

第六，作者选择SQLite作为数据库，操作简单，备份方便，适合小规模应用。

第七，Django内置丰富功能，如CSRF保护、邮件发送等，配置灵活。

最后，作者对settings.py文件感到些许不安，因为它是全局变量设置，易出错，但总体对Django持积极态度，并计划继续探索表单验证和认证系统。
