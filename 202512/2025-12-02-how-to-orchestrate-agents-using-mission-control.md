# How to orchestrate agents using mission control
- URL: https://github.blog/ai-and-ml/github-copilot/how-to-orchestrate-agents-using-mission-control/
- Added At: 2025-12-02 15:41:14
- Tags: #read #llm #guide

## TL;DR
GitHub Copilot的Mission Control功能通过统一界面管理多个AI代理，实现并行工作流。关键点包括：编写清晰提示、自定义代理以确保一致性、主动监控并干预问题、高效审查PR。其优势在于提升效率，实现批量处理和并行工作。

## Summary
本文介绍 GitHub Copilot 的 Mission Control 功能，该功能提供统一界面来管理和编排多个 AI 代理（agents），实现从串行到并行的工作流转变。核心内容包括：

- **心智模型转变**：从逐个处理任务变为同时启动多个代理，提升效率，但需注意任务依赖和冲突。
- **使用技巧**：
  - 编写清晰、具体的提示（prompts），包含上下文如截图或代码片段。
  - 利用自定义代理（通过 agents.md 文件）确保一致性。
- **主动编排**：监控会话日志，识别问题信号（如测试失败、范围蔓延），及时干预并精准引导。
- **审查阶段**：高效审查拉取请求，关注会话日志、文件变更和测试结果，可让 Copilot 自审并批量处理类似审查。
- **优势总结**：通过规范提示、早期干预和批量审查，实现在相同时间内解锁更多并行工作。
