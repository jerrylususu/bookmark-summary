# Automate your project with GitHub Models in Actions
- URL: https://github.blog/ai-and-ml/generative-ai/automate-your-project-with-github-models-in-actions/
- Added At: 2025-08-05 14:11:38

## TL;DR


GitHub通过Actions集成AI模型实现自动化任务，例如自动补充bug细节、生成PR发布说明及每周问题汇总。需配置仓库权限，支持替换40+模型，利用分支逻辑控制流程，减少外部API调用，提供多层级集成方案，提升开发效率与任务管理智能化。

## Summary


1. GitHub Models在Actions中的集成与自动化  
通过GitHub Actions将AI功能（如代码分析、文本生成）无缝嵌入项目流程，实现自动化处理。

2. 前置条件：权限配置  
在工作流中添加权限设置：  
- contents: read（读取仓库内容）  
- issues: write（管理问题）  
- models: read（访问AI模型）

3. 示例一：自动补充bug报告信息  
- 触发场景：新问题创建时  
- 流程：  
  1) 通过GitHub Script获取问题标题和内容  
  2) 使用AI模型分析（如Mistral-3B）判断信息完整性  
  3) 若缺失必要细节（复现步骤、环境等），自动回复友好的补充提示  
- 模型可扩展性：支持替换为GitHub模型市场中的其他40+模型

4. 示例二：从合并PR生成发布说明  
- 触发场景：PR被合并时  
- 流程：  
  1) 安装gh-models扩展  
  2) 提取PR的标题/正文/评论等信息  
  3) 调用模型（如Grok-3-Mini）生成简洁的变更摘要  
  4) 自动追加到标记为"release"的待发布issue中  
- 输出格式：带PR编号的清单项（e.g. "- 新增功能：XXX (#123)"）

5. 示例三：定期问题汇总与优先级排序  
- 触发场景：每周一9点定时执行  
- 流程：  
  1) 收集过去一周的所有开放问题  
  2) 使用模型（如GPT-4.1）生成结构化摘要：  
     - 按主题分类  
     - 提出优先级建议  
  3) 创建含三部分的周报issue：具体问题清单、主题归纳、优先级排序  
- 配置要点：通过prompt文件管理复杂提示，支持可视化迭代优化

6. 核心优势：  
- 通过分支逻辑(GitHub Actions条件判断)实现AI引导流程控制  
- 统一工作流中代码与AI模型操作，避免外部API调用  
- 支持从简单API调用到复杂prompt工程的多层级集成方式
