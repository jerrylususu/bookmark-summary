# llm-docsmith | MPN
- URL: https://mathpn.com/posts/llm-docsmith/
- Added At: 2025-04-11 14:22:29

## TL;DR


llm-docsmith是一款AI驱动的Python代码文档生成工具，通过解析源代码的Concrete/AST语法树提取函数签名，结合结构化指令约束LLM输出高质量docstrings，支持多模型集成和零代码改动的文档生成。用户可通过LLM插件快速安装和使用，但存在上下文过长的token消耗问题，开发者已开源并计划优化触发机制。

## Summary


本文介绍了作者开发的AI文档生成工具llm-docsmith，用于自动生成Python代码的docstrings。现有工具未能满足以下需求：无需复杂依赖的良好用户体验、仅修改docstrings而不改动代码、充分利用代码中的类型提示等信息，因此作者决定重新开发。

技术实现采用以下步骤：
1. 通过libcst解析源代码为保留格式信息的Concrete Syntax Tree，确保改写docstrings时不影响代码格式；
2. 将语法树转换为Abstract Syntax Tree，提取函数/类的完整签名（包括参数、默认值、类型提示）；
3. 使用结构化输出指令约束LLM，使其按固定格式生成包含参数说明、返回值等的docstrings；
4. 通过LLM工具内置的API密钥管理功能整合多模型支持，改善用户配置体验。

工具使用方式包括：
- 安装LLM插件：`llm install llm-docsmith`
- 生成指定文件文档：`llm docsmith ./script.py`

当前局限性：
- 可能因包含过多上下文代码导致token消耗过高；
- 会重写所有docstrings而非仅修改缺失部分；
- 未来计划通过Git集成优化触发条件。

开发者认为该工具在当前模式下已能生成高质量docstrings，并开放源代码邀请社区反馈。
