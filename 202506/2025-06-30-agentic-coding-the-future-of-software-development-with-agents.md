# Agentic Coding: The Future of Software Development with Agents
- URL: https://simonwillison.net/2025/Jun/29/agentic-coding/
- Added At: 2025-06-30 13:34:37
- [Link To Text](2025-06-30-agentic-coding-the-future-of-software-development-with-agents_raw.md)

## TL;DR


Armin Ronacher分享了Claude Code代理编码实践，通过自动化任务（调试CI、浏览器交互）提升效率。方法包括：减少MCP工具依赖、整合多源日志到统一系统、分担任务以突破上下文限制，以及设计明确错误提示。集成Playwright和GitHub CLI实现自动化操作，建议在Docker中启用安全选项并结合Gemini CLI优化执行。

## Summary


本文介绍了Armin Ronacher在使用Claude Code进行代理编码的实践经验及方法论，重点包括以下几点：

### 核心观点
- **代理编码（Agentic Coding）潜力**：代理工具（如Claude Code）可显著提升开发效率，通过自动化执行复杂任务（如调试CI、浏览器操作、GitHub CLI交互）。
- **风险与安全性**：建议在Docker容器内启用`--dangerously-skip-permissions`选项以提高生产力，同时降低风险。

### 实用技巧与工具
1. **减少MCP依赖**  
   - 优先通过脚本、Makefile命令替代MCP工具，仅保留必要工具（如Playwright MCP）。
2. **统一日志系统**  
   - **整合所有日志**：合并`console.log`、服务器日志、SQL日志等，通过API转发浏览器日志至服务器。
   - **集中管理**：创建单一可追踪的日志文件，提供`make tail-logs`命令（显示最后50行日志并实时追踪）。
3. **任务分担与上下文管理**  
   - 使用Gemini CLI启动子代理，避免Claude Code的上下文限制。
4. **清晰错误设计**  
   - 开发工具时需提供明确的错误提示，便于代理工具快速恢复失败任务。

### 自动化实践案例
- **Playwright集成**：Claude Code通过已登录的浏览器实例执行自动化操作（如调试CI、界面交互）。
- **GitHub生态交互**：结合`gh` CLI工具操作GitHub Actions工作流，实现开发流程自动化。

### 关键工具与资源
- **Playwright MCP**：推荐的MCP工具，用于浏览器自动化（GitHub：playwright-mcp）。
- **Gemini CLI**：辅助执行子任务，优化代理工具效率。
