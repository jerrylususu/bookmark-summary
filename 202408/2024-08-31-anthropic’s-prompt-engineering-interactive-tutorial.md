# Anthropic’s Prompt Engineering Interactive Tutorial
- URL: https://simonwillison.net/2024/Aug/30/anthropic-prompt-engineering-interactive-tutorial/
- Added At: 2024-08-31 11:46:59
- [Link To Text](2024-08-31-anthropic’s-prompt-engineering-interactive-tutorial_raw.md)

## TL;DR
本教程介绍了Anthropic的提示工程，包括安装、API密钥管理、使用XML标签组织提示、避免拼写错误、利用prefill功能和预知策略，以及如何避免幻觉，通过收集证据来提高回答准确性。

## Summary
1. **教程概述**：Anthropic提供的提示工程互动教程，作为Jupyter笔记本形式呈现，展示了Anthropic在LLM供应商中提供的最佳文档之一。

2. **教程使用**：
   - **安装与启动**：通过uvx工具安装Jupyter系统，快速启动服务器并在浏览器中打开。
   - **环境配置**：使用`%pip install anthropic`确保包安装在正确的虚拟环境中，并提交了相关问题和PR。

3. **API密钥管理**：
   - **存储API密钥**：使用`%store`命令将Anthropic API密钥存储在IPython store中，便于后续笔记本中恢复。
   - **存储位置**：在macOS系统中，这些变量存储在`~/.ipython/profile_default/db/autorestore`目录下的同名文件中。

4. **章节内容**：
   - **第四章：分离数据和指令**：
     - **XML标签支持**：Claude支持XML标签风格的定界符，推荐使用XML标签作为提示组织机制。
     - **避免拼写错误**：强调提示中的小细节重要性，避免拼写和语法错误，以减少模型出错概率。
   - **第五章：格式化输出和为Claude代言**：
     - **prefill功能**：介绍Claude的prefill功能，允许用户指定响应的开始部分。
   - **第六章：预知（逐步思考）**：
     - **使用XML标签**：建议使用XML标签帮助模型在生成最终答案前考虑不同论点。
     - **顺序敏感性**：指出Claude对选项顺序的敏感性，通常更倾向于选择第二个选项。
   - **第八章：避免幻觉**：
     - **收集证据**：建议让Claude先收集证据，再基于这些证据回答问题，以减少长文档中的幻觉。
     - **示例提示**：提供了一个示例提示，指导Claude在处理复杂问题时先提取相关引文，再基于引文给出简短的数字答案。
