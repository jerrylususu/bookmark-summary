# Gaslight-driven development
- URL: https://tonsky.me/blog/gaslight-driven-development/
- Added At: 2025-07-17 13:31:20

## TL;DR


文章探讨了AI驱动的“Gaslight-driven development”现象，指出随着LLM生成代码比例增加，开发者被迫调整API设计以适配其建议。如Soundslice和Instant公司因AI错误建议或生成习惯而修改API。尽管可能优化设计并帮助发现文档问题，但也可能限制创新并导致设计趋同。结论建议开发者应简化API设计，因AI正推动技术规范向其训练数据中的常见模式靠拢。

## Summary


文章讨论了人工智能（尤其是大语言模型LLM）如何反向影响软件开发流程的现象，称其为“Gaslight-driven development”。随着LLM生成代码的比例增加（预计未来90%的代码由AI编写），开发者被迫调整API设计以适应AI的“习惯”：

1. **现象背景**  
   - 用户长期被迫执行无意义的计算机指令（如确认邮件、解决验证码）。现在，LLM开始对API设计提出“建议”，开发者需遵从以避免用户困惑。

2. **案例展示**  
   - Soundslice因ChatGPT错误建议不存在的功能而最终添加该功能；作者所在公司Instant因LLM频繁使用`tx.create`，虽原有API用`tx.update`统一处理增删改，仍新增`tx.create`以匹配AI生成的代码。

3. **利弊分析**  
   - **优点**：LLM基于海量API经验提出常见设计，可能优化开发者未注意的细节；提供“新手视角测试”，帮助发现API文档的不足。  
   - **缺点**：若项目旨在创新或做独特之事，LLM可能因缺乏相关数据而误导设计；过度迁就LLM可能导致API设计趋同，丧失差异化。

4. **结论与反思**  
   - 当前API设计或许应回归简洁直观，避免标新立异。AI正从工具进化为设计决策者，通过“让开发者怀疑自身设计”的方式，推动技术规范向其训练数据中常见的模式靠拢。
