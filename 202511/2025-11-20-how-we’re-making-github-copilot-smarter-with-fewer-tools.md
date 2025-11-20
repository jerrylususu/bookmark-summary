# How we’re making GitHub Copilot smarter with fewer tools
- URL: https://github.blog/ai-and-ml/github-copilot/how-were-making-github-copilot-smarter-with-fewer-tools/
- Added At: 2025-11-20 15:06:08
- Tags: #read #llm
- [Link To Text](2025-11-20-how-we’re-making-github-copilot-smarter-with-fewer-tools_raw.md)

## TL;DR
GitHub Copilot通过自适应工具聚类、嵌入引导工具路由和精简默认工具集三大技术优化，显著提升了响应速度和工具选择效率。改进后，工具使用覆盖率提升至94.5%，延迟降低，为未来智能代理工作流打下基础。

## Summary
GitHub Copilot 通过减少工具数量并优化工具选择机制来提高智能性和响应速度。文章核心改进包括以下三个方面：

1.  **问题背景**：GitHub Copilot Chat 在 VS Code 中通过 Model Context Protocol (MCP) 可访问数百个工具，但工具过多会导致模型推理缓慢、延迟增加和性能下降。例如，用户可能遇到“Optimizing tool selection...”的加载提示。

2.  **关键技术改进**：
    - **自适应工具聚类**：使用 GitHub Copilot 的嵌入模型对工具进行向量化，并通过余弦相似度聚类相似工具，形成“虚拟工具组”。这替代了原本依赖 LLM 分组的方法，提高了稳定性和效率，同时降低令牌成本和缓存未命中率。
    - **嵌入引导的工具路由**：在用户查询时，系统通过比较查询嵌入与工具向量的语义相似度，预先选择最相关的工具组，避免模型逐一探索所有工具。这减少了不必要的调用，将工具使用覆盖率从默认的 69.0% 提升至 94.5%，并显著降低延迟。
    - **精简默认工具集**：基于使用数据，将默认工具从 40 个缩减至 13 个核心工具（如代码库解析、文件编辑等），非核心工具归入虚拟组（如 Jupyter Notebook 工具）。这使模型推理更简单，在线测试显示首次令牌时间（TTFT）平均减少 190 毫秒，最终令牌时间减少 400 毫秒。

3.  **效果与未来方向**：改进后在 SWE-Lancer 等基准测试中成功率提升 2-5 个百分点。未来计划结合嵌入、记忆和强化学习，实现长上下文推理，使模型能记忆历史工具使用、推断意图并规划多步操作。

这些优化旨在使 GitHub Copilot 更快速、高效，同时为更智能的代理工作流奠定基础。
