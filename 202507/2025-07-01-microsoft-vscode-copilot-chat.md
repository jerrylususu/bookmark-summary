# microsoft/vscode-copilot-chat
- URL: https://simonwillison.net/2025/Jun/30/vscode-copilot-chat/
- Added At: 2025-07-01 14:01:45
- [Link To Text](2025-07-01-microsoft-vscode-copilot-chat_raw.md)

## TL;DR


微软开源VS Code Copilot Chat扩展（MIT协议），当前提供聊天功能，未来整合补全能力。扩展优化工具指令交互，如文件读取、终端串行执行，并支持用户偏好存储及精准代码替换。内置代码总结模板与Python环境修复规范，通过SQLite缓存实现LLM测试可复现。现有代码补全功能仍依赖闭源扩展。（99字）

## Summary


微软开源了VS Code Copilot Chat扩展，采用MIT许可证。当前版本仅包含Copilot的聊天功能，补全功能预计后续整合至VS Code核心。该扩展通过工具指令提升交互效率，例如：

- **文件操作工具**：要求优先使用ReadFile读取大段内容而非多次调用，利用FindTextInFiles搜索单个文件以快速获取概览。
- **终端工具**：禁止并行调用RunInTerminal，需等待前一命令输出后再执行后续命令。
- **用户偏好**：使用UpdateUserPreferences工具存储用户纠正或表达的偏好。
- **代码编辑**：仅在用户明确要求时才允许通过终端命令编辑文件，推荐使用ReplaceString工具进行精准字符串替换。

在代码总结方面，extension/prompt/node/summarizer.ts文件设计了结构化总结模板，涵盖对话标题、用户意图、待办事项、代码状态及关键代码片段等内容。此外，针对Python环境的错误修复，扩展内置了规范性指导，例如推荐使用`python -m pip install`替代直接的`pip install`命令，强调虚拟环境创建等。

测试与评估模块通过SQLite缓存机制实现LLM响应的确定性测试，确保测试结果可复现。测试架构由prompt_crafting等组件构成，旨在验证提示工程效果（如文件路径或代码修改需求），其详细文档由Gemini 2.5 Pro生成并包含Mermaid流程图说明。未来计划将补全功能迁移至开源扩展，但现有原生Copilot补全扩展仍为闭源状态。
