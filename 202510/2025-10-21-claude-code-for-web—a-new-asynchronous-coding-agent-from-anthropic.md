# Claude Code for web—a new asynchronous coding agent from Anthropic
- URL: https://simonwillison.net/2025/Oct/20/claude-code-for-web/
- Added At: 2025-10-21 13:34:50

## TL;DR
Anthropic于2025年10月推出Claude Code for web异步编码代理，支持GitHub仓库操作与网络隔离沙盒环境。该工具提供简单任务部署、性能测试及本地CLI同步功能，通过容器化服务兼顾效率与安全性，适合快速开发测试。

## Summary
Anthropic于2025年10月20日推出了Claude Code for web，这是一个异步编码代理，类似于OpenAI的Codex Cloud和Google的Jules。该工具基于Claude Code CLI，通过容器技术实现，并支持“危险跳过权限”模式，提供网络和移动端界面。

### 主要功能
- **操作流程**：用户可以指定GitHub仓库，选择环境（无网络访问、受信任网络访问或自定义域名访问），并输入提示启动任务。运行中可添加新提示，任务完成后会自动创建分支并可发起拉取请求。
- **特点**：包含“传送”功能，可将聊天记录和编辑文件同步到本地CLI工具；支持异步处理，任务队列顺序执行。
- **应用示例**：
  - 创建并部署简单的GitHub Pages工具。
  - 性能对比任务（如MiniJinja与Jinja2模板引擎的基准测试），自动生成脚本、文档和图表。

### 安全性策略
Anthropic将Claude Code for web视为沙盒策略的一部分，强调文件系统和网络隔离：
- **文件系统沙盒**：使用macOS的seatbelt和Linux的Bubblewrap实现。
- **网络隔离**：通过Unix域套接字连接代理服务器，限制域名访问，防止数据泄露和“致命三重奏”攻击。
- **环境模式**：提供“无网络访问”、“受信任网络访问”（默认域名列表较广，存在潜在风险）和自定义允许列表（如“*”全开放）。
- **开源工具**：发布了Apache 2许可证的sandbox-runtime库，推动安全实践。

### 优势与成本
- **便利性**：托管式容器服务省去本地设置，适合快速测试；结果与CLI版本一致。
- **成本**：作者使用Claude Max计划，通过非官方工具估算每日成本约1-5美元，但实际费用需用户自行评估。

整体上，Claude Code for web通过沙盒化平衡了自动化编码的效率和安全性，成为Anthropic在AI开发工具领域的重要布局。
