# Which Table Format Do LLMs Understand Best? (Results for 11 Formats)
- URL: https://improvingagents.com/blog/best-input-data-format-for-llms
- Added At: 2025-10-08 02:35:54
- [Link To Text](2025-10-08-which-table-format-do-llms-understand-best-(results-for-11-formats)_raw.md)

## TL;DR
研究发现表格数据格式显著影响LLM理解能力。Markdown-KV准确率最高但不经济，CSV和JSONL成本低但准确性较差。推荐根据需求选择格式，优先考虑Markdown相关方案，避免默认使用CSV或JSONL。

## Summary
该研究评估了11种表格数据格式对大型语言模型（LLM）理解能力的影响，重点关注格式选择对系统准确性和令牌成本的作用。实验使用GPT-4.1-nano模型，基于1000条员工记录（含8个属性）和1000个随机查询，测试每种格式的准确性和令牌消耗。

结果显示，不同格式在准确性和令牌使用上存在显著差异。Markdown-KV（非标准键值对格式）表现最佳，准确率达60.7%，但令牌使用较高（52,104 tokens），是CSV格式的2.7倍。CSV和JSONL格式准确率最低（分别为44.3%和45.0%），但令牌效率高（CSV仅19,524 tokens）。其他格式如XML、INI、YAML、HTML、JSON、Markdown表格、自然语言和管道分隔格式的准确率居中（41.1%至56.0%）。

关键发现包括：格式选择对LLM理解至关重要，Markdown-KV适合高准确性需求场景，Markdown表格在可读性和成本间提供平衡，而CSV和JSONL可能降低系统准确性。实验局限性包括仅测试单一模型和数据模式，未来需研究其他模型、数据结构（如嵌套数据）、表大小、标题重复和问题类型的影响。

建议用户根据需求测试不同格式，优先考虑Markdown-KV或Markdown表格，避免默认使用CSV或JSONL以优化系统性能。
