# Useful patterns for building HTML tools
- URL: https://simonwillison.net/2025/Dec/10/html-tools/
- Added At: 2025-12-11 12:23:09
- Tags: #read #tips #deepdive #frontend
- [Link To Text](2025-12-11-useful-patterns-for-building-html-tools_raw.md)

## TL;DR
该文介绍了HTML工具的定义和开发模式，强调单一文件结构，避免复杂框架，并使用CDN和浏览器原生功能实现轻量化开发。建议通过LLM辅助快速构建实用工具，并分享了具体实现技巧和示例。

## Summary
作者将 HTML 工具定义为结合 HTML、JavaScript 和 CSS 的单一文件应用，用于提供实用功能，并分享了构建这些工具的模式和经验。

### 核心理念
- **单一文件结构**：内联 JavaScript 和 CSS，便于托管和分发，易于从 LLM 响应中复制粘贴。
- **避免 React 或构建步骤**：简化开发，提升便捷性。
- **依赖项从 CDN 加载**：减少依赖，优先使用 CDNjs 或 jsDelivr 等可靠来源。
- **保持小型化**：代码量控制在几百行内，便于 LLM 理解和重写。

### 开发模式
1. **原型设计**：使用 ChatGPT、Claude 或 Gemini 的 Artifacts/Canvas 功能快速构建工具，并明确要求“No React”。
2. **复杂项目处理**：转向 Claude Code 等编码代理，利用其测试能力处理更复杂任务。
3. **依赖管理**：通过 CDN 加载库，避免 npm 和构建步骤。
4. **托管选择**：优先自托管于 GitHub Pages 等静态托管服务，避免 LLM 平台的限制和不可靠性。
5. **利用复制粘贴**：设计工具支持粘贴输入和复制输出，并添加“复制到剪贴板”按钮提升移动端体验。
6. **构建调试工具**：如 clipboard-viewer 等，帮助理解浏览器功能。
7. **状态持久化**：
   - 使用 URL 存储状态，便于分享和书签。
   - 使用 localStorage 存储敏感信息（如 API 密钥）或较大数据。
8. **利用 CORS 启用 API**：集成如 iNaturalist、PyPI、GitHub 等支持 CORS 的 API，扩展工具功能。
9. **直接调用 LLM API**：通过 CORS 调用 OpenAI、Anthropic 或 Gemini 的 API，结合 localStorage 管理 API 密钥。
10. **文件处理**：使用 `<input type="file">` 直接处理本地文件，无需上传服务器。
11. **生成可下载文件**：利用 JavaScript 库生成 PNG、JPEG 或 ICS 等格式文件。
12. **集成 Pyodide**：在浏览器中运行 Python 代码，支持加载 PyPI 包。
13. **重用和记录**：复用现有工具，并记录提示和转录过程以便追溯。

### 示例工具
- **功能型**：svg-render（SVG 转图片）、pypi-changelog（生成 PyPI 版本差异）、bluesky-thread（Bluesky 线程视图）。
- **调试型**：clipboard-viewer（查看剪贴板数据）、keyboard-debug（键盘事件调试）。
- **API 集成型**：species-observation-map（iNaturalist 数据展示）、github-issue-to-markdown（GitHub issue 转 Markdown）。

### 总结
作者强调 HTML 工具的优势在于轻量、易部署和灵活性，鼓励通过 LLM 辅助快速构建实用工具，并充分利用浏览器原生功能和外部 API。
