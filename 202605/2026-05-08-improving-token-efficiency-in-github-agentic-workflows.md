# Improving token efficiency in GitHub Agentic Workflows
- URL: https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/
- Added At: 2026-05-08 15:33:07
- Tags: #read #agent

## TL;DR
本文介绍了GitHub优化Agentic Workflows令牌使用的方法，包括统一数据收集、自动审计与改进建议。通过移除未用工具和替换数据获取操作，令牌使用量显著下降，如Auto-Triage Issues减少62%。文章还提出有效令牌指标以标准化成本计算，最终实现显著成本节约。

## Summary
本文介绍了GitHub如何优化其Agentic Workflows中的令牌使用效率。首先，通过API代理统一收集各代理框架的令牌使用数据，生成标准化日志。随后，构建了每日令牌使用审计器和优化器，自动识别低效工作流并提出改进建议。主要优化措施包括：移除未使用的MCP工具以减少上下文开销，以及用GitHub CLI替代MCP数据获取操作，从而降低LLM推理开销。优化后，多个工作流的令牌使用量显著下降，例如Auto-Triage Issues减少62%，Security Guard减少43%。文章还讨论了衡量效率提升的挑战，如模型成本差异、工作负载变化和质量评估，并提出了有效令牌（ET）指标来标准化成本计算。最终，通过减少不必要的LLM调用和工具冗余，实现了显著的成本节约。
