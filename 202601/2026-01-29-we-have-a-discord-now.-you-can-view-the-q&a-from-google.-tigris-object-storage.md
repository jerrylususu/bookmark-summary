# We have a Discord now. You can view the Q&A from Google. | Tigris Object Storage
- URL: https://www.tigrisdata.com/blog/discord-backfill/
- Added At: 2026-01-29 14:43:44
- Tags: #read

## TL;DR
Tigris Data 使用 ETL 框架将论坛问答数据迁移到 Discord，通过 AI 处理文本和生成头像，集成 Answer Overflow 实现公开搜索，成功提升社区参与度。

## Summary
### 文章概述
本文介绍了 Tigris Data 如何将现有问答数据从外部论坛迁移到 Discord 社区，并通过 Answer Overflow 实现公开搜索。迁移过程遵循 ETL（提取、转换、加载）框架，旨在避免新社区内容空白问题，提升用户参与度。

### 迁移步骤
1. **数据提取**：
   - 从 Discourse 论坛提取问答数据，使用礼貌的爬虫策略（如附加 `.json` 获取 JSON 格式数据），并包含详细 User-Agent 信息以便管理员识别。
   - 数据缓存到 Tigris 对象存储中，利用其快照功能防止数据丢失。

2. **数据转换**：
   - 使用 AI 模型（如 GPT-OSS 120b）处理数据：将 HTML 转换为 Markdown、移除个人可识别信息、总结长文本以适应 Discord 的字符限制。
   - 生成用户头像：通过 Z-Image Turbo 模型基于用户 ID 创建个性化头像，存储于 Tigris 并设置公共 ACL。

3. **数据加载**：
   - 利用 Discord webhook 和线程功能，模拟多用户对话，将问答数据导入 Discord 频道。
   - 通过 Answer Overflow 集成，使问答内容可在网页端搜索（如 community.tigrisdata.com）。

### 技术亮点
- **工具应用**：Tigris 对象存储用于数据管理，开源代码库公开在 GitHub。
- **AI 辅助**：本地和云端 AI 模型处理文本和图像，确保数据适配。
- **用户体验优化**：通过头像生成和线程模拟，提升迁移内容的真实感。

### 成果与建议
- 迁移成功率达 99.9%，问答数据可在 Discord 和网页端搜索，便于用户获取帮助。
- 作者建议社区成员积极参与 Discord，分享知识，并利用 MCP 服务器集成 AI 代理访问知识库。
