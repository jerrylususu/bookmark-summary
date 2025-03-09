# Perplexity: Interactive language modeling visualization
- URL: https://perplexity.vercel.app/
- Added At: 2025-03-09 15:20:41
- [Link To Text](2025-03-09-perplexity-interactive-language-modeling-visualization_raw.md)

## TL;DR
用户开发了基于GPT-2的可视化工具，通过高亮与注释展示文本生成过程中的词预测概率。当输入数列时，模型准确性随序列递增；随机词汇组合重复输入后，模型能快速学习模式（验证Transformer的归纳能力）。工具在浏览器端运行，采用transformers.js和Oak框架，注重隐私保护。

## Summary
用户开发了一个工具，用于直观展示自回归语言模型的工作过程。该工具基于124M参数的GPT-2模型，通过高亮和注释形式显示文本中每个词对模型的“意外程度”及可能的替代词。例如，当用户数数到十时，模型的预测准确率随序列进展逐步提升，最终对末尾词达到100%确定；若输入包含随机词汇（如“南瓜、小丑、推特”）的句子，模型首次遇到时难以预测后续内容，但重复出现时能准确预期每个词，印证了Transformer模型快速学习重复模式的能力（即“归纳”机制）。该工具完全基于浏览器运行，数据不上传至服务器，技术上采用transformers.js和Oak框架实现。项目灵感来自关于归纳头的研究及类似工具（如https://joel.tools/codegen/）。
