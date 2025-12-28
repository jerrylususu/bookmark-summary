# Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs
- URL: https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs
- Added At: 2025-04-14 13:30:53

## TL;DR


Stevens是一个基于SQLite和定时任务的轻量级AI助手，整合Google日历、天气API、OCR邮件等数据，通过Telegram发送家庭日程摘要。其核心为按日期分类的记忆数据库，未指定日期的条目作为长期背景信息。系统可通过新增“导入器”扩展功能，强调通过外部数据打破应用孤岛，并开源提倡Vibe Coding等趣味化开发方式。

## Summary


本文介绍了一个名为Stevens的简单AI助手，通过单一SQLite表和定时任务实现家庭日程管理与信息整合。系统核心是SQLite数据库存储记忆条目，包含日程、天气、包裹提醒等信息，并通过Telegram发送每日摘要。技术架构基于Val.town平台，利用HTTP请求、定时任务和Claude API生成自然语言输出。数据来源包括Google日历API、天气API、OCR处理的邮件扫描件及Telegram/E-mail消息。记忆条目按日期分类，未指定日期的条目作为背景信息长期保留。系统可通过新增“导入器”扩展功能，只需将新数据写入数据库表。作者强调结合外部数据打破应用孤岛的重要性，并指出简单记忆设计在信息量较小时的有效性。最后分享源码链接，提倡通过Vibe Coding等轻量化开发方式提升工具趣味性。
