# Claude Skills are awesome, maybe a bigger deal than MCP
- URL: https://simonwillison.net/2025/Oct/16/claude-skills/
- Added At: 2025-10-17 13:14:46

## TL;DR
Claude Skills是Anthropic推出的轻量化AI技能框架，通过Markdown文件和脚本即可扩展模型的专业任务能力。相比复杂协议MCP，它具有简单高效、跨模型通用的优势，未来或引发技能生态爆发式增长。设计核心在于利用模型自主推理能力，降低开发门槛。

## Summary
本文介绍了 Anthropic 推出的 Claude Skills，并分析其设计原理、应用场景及与 MCP 的对比。

### Claude Skills 概述
- **定义**：Claude Skills 是一种让 Claude 模型具备特定任务能力的新模式。每个技能是一个文件夹，包含 Markdown 说明文件、脚本和资源。模型仅在任务相关时加载技能，提升专业化任务（如处理 Excel 或遵循品牌指南）的表现。
- **发布背景**：技能功能与 9 月推出的文档创建能力和代码解释器一同发布，后者已通过技能实现。
- **技术细节**：技能采用 token 高效设计。会话开始时，Claude 仅读取每个技能的 YAML 元数据（占几十个 token），仅在需要时才加载完整细节。

### 技能的工作原理与示例
- **依赖环境**：技能完全依赖模型的编码环境（如文件系统和命令执行能力），类似于 ChatGPT Code Interpreter 或 Claude Code。
- **示例应用**：作者测试了 Anthropic 提供的 slack-gif-creator 技能，Claude 成功生成符合 Slack 尺寸限制的 GIF，并调用技能中的验证函数检查文件大小。
- **优势**：技能易于迭代，通过 Markdown 文件和简单脚本即可扩展模型能力，无需复杂开发。

### 技能与 MCP 的对比
- **MCP 的局限**：Model Context Protocol 虽受关注，但存在 token 消耗大（如 GitHub MCP 占用数万 token）、协议复杂（涉及多种规范和传输方式）的问题。
- **技能的优势**：
  - **简单性**：技能仅需 Markdown 文件和可选脚本，无需额外协议，更符合 LLM 的文本处理本质。
  - **通用性**：技能可被其他模型（如 Codex CLI 或 Gemini CLI）直接使用，不限于 Claude。
  - **效率**：模型可通过 `--help` 等命令自主学> 习工具用法，减少 token 开销。

### 技能的应用前景
- **广义代理能力**：Claude Code 实为“通用代理”，可自动化任何计算机操作。技能进一步明确了这一潜力，例如可构建“数据新闻代理”，通过技能文件夹指导数据获取、处理分析和可视化。
- **生态发展**：技能易于共享和定制，作者预计将出现“寒武纪爆发”式增长。Anthropic 已提供文档和示例，鼓励社区贡献。
- **安全考虑**：技能依赖安全沙箱环境，需防范提示注入等攻击，确保编码环境可控。

### 核心价值：简单性
- 技能的设计极简（Markdown + YAML + 脚本），降低了使用门槛，强调 LLM 的自主推理能力。相比之下，MCP 等复杂协议可能过度设计。技能将难题外包给模型和环境，体现了对 LLM 工具使用能力的信任。
