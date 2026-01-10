# Fly’s new Sprites.dev addresses both developer sandboxes and API sandboxes at the same time
- URL: https://simonwillison.net/2026/Jan/9/sprites-dev/
- Added At: 2026-01-10 11:08:54
- Tags: #read #llm #security

## TL;DR
Fly.io推出Sprites.dev，提供持久化沙盒环境与API服务，支持快速创建、检查点回滚和安全运行代码。旨在通过按需计费和隔离环境，为开发者及API用户提供安全、经济的沙盒解决方案。

## Summary
Fly.io 推出了 Sprites.dev，这是一个兼具开发者沙盒和 API 沙盒功能的新产品。其核心特点包括：

**关键特性**
- **状态持久化沙盒**：Sprites.dev 提供持久的虚拟环境（配置约 8GB RAM 和 8 CPU），预装了 Claude Code、Python、Node.js 等开发工具。用户通过命令行快速创建和连接沙盒，支持 SSH 访问和端口转发，并可生成公开 URL 供他人访问。
- **存储与检查点**：沙盒文件系统在会话间持久保存，支持快速检查点功能（约 300ms 创建）。检查点采用写时复制技术，可捕获磁盘状态并回滚，最近 5 个检查点可直接访问。用户可通过命令行或 API 管理检查点。
- **集成 Claude Skills**：沙盒预置 Skills 文件，使 Claude 等编码代理能学习 Sprites 的操作方法，例如指导用户配置端口等。
- **沙盒 API**：提供 JSON API 及多语言客户端库（如 Go、TypeScript），支持创建沙盒、执行命令、配置网络策略（基于 DNS 的允许/拒绝列表）等功能，便于安全运行不受信任的代码。
- **按需计费**：沙盒在闲置 30 秒后自动休眠，仅按唤醒时的 CPU、RAM 和存储使用量计费。例如，4 小时高强度编码会话约 0.46 美元，低流量应用月费约 4 美元。

**解决的问题**
- **开发者沙盒**：为编码代理（如 Claude Code）提供安全的“YOLO 模式”环境，避免因错误或恶意代码导致系统损坏，沙盒可随时丢弃和替换。
- **API 沙盒**：解决运行不受信任代码的安全需求，通过隔离环境限制潜在风险，支持检查点回滚以确保清洁状态。

**优势与定位**
- Sprites.dev 同时面向开发者和 API 用户，简化了沙盒管理，但产品概念可能较难解释。
- 与 Cloudflare、Modal 等竞争对手相比，Fly.io 专注于“慢创建、快启停”架构，平衡了资源效率和灵活性。

作者认为该产品有望推动沙盒技术发展，并已开始基于其构建原型项目。
