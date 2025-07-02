# Using Playwright MCP with Claude Code
- URL: https://til.simonwillison.net/claude-code/playwright-mcp-claude-code
- Added At: 2025-07-02 13:35:46
- [Link To Text](2025-07-02-using-playwright-mcp-with-claude-code_raw.md)

## TL;DR


本文介绍Playwright MCP与Claude Code的集成方法：通过`claude mcp add playwright`命令在项目目录配置服务，使用自然语言指令操控浏览器（如「打开example.com需明确提及Playwright」），配置存储于`~/.claude.json`。认证需手动登录保存Cookie。提供20+工具支持导航、截图、表单提交等操作，Claude可自动匹配工具，输入`/mcp playwright`查看工具列表。

## Summary


本文介绍了如何将Playwright MCP与Claude Code结合使用。关键步骤如下：

1. **安装配置**：运行 `claude mcp add playwright npx '@playwright/mcp@latest'` 命令添加Playwright MCP服务，需在目标项目目录下执行以确保配置仅影响该目录。

2. **使用方法**：启动`claude`后，通过指令如「Use playwright mcp to open a browser to example.com」可控制可见的Chrome窗口。首次需明确提及「playwright mcp」，避免Claude默认调用Bash执行Playwright。

3. **配置存储**：配置信息保存在`~/.claude.json`中，包含各项目的MCP工具和允许的命令列表。

4. **认证机制**：通过弹出登录页面手动输入凭证，会话期间Cookie将被持久化保存。

5. **工具功能**：Playwright MCP提供20+工具，涵盖浏览器操作（如导航、截图、点击、表单提交等），Claude可自动匹配合适工具无需手动指定。部分工具为只读（如查看控制台消息），关键操作如`browser_click`、`browser_type`等可直接用于自动化任务。

6. **MCP管理**：输入`/mcp playwright`可查看所有可用工具列表。
