# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-03-12) [你不知道的 Claude Code：架构、治理与工程实践 - Tw93](202603/2026-03-12-%E4%BD%A0%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-claude-code%EF%BC%9A%E6%9E%B6%E6%9E%84%E3%80%81%E6%B2%BB%E7%90%86%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5---tw93.md)
  - 本文系统总结了Claude Code的六层架构模型、上下文工程、Skills设计等核心实践，强调通过分层治理和验证闭环提升AI工程化能力，适用于从工具使用者到系统设计者的演进。
  - Tags: #read #agent #deepdive #guide

- (2026-03-11) [AI should help us produce better code - Agentic Engineering Patterns](202603/2026-03-11-ai-should-help-us-produce-better-code---agentic-engineering-patterns.md)
  - AI工具应提升而非降低代码质量，通过处理技术债务、辅助决策和复盘优化，实现高效可持续的开发。
  - Tags: #read #agent #tips

- (2026-03-10) [年度征文｜「你是专家」这句话，到底是在帮 AI 还是在害你？ - 少数派](202603/2026-03-10-%E5%B9%B4%E5%BA%A6%E5%BE%81%E6%96%87%EF%BD%9C%E3%80%8C%E4%BD%A0%E6%98%AF%E4%B8%93%E5%AE%B6%E3%80%8D%E8%BF%99%E5%8F%A5%E8%AF%9D%EF%BC%8C%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8%E5%B8%AE-ai-%E8%BF%98%E6%98%AF%E5%9C%A8%E5%AE%B3%E4%BD%A0%EF%BC%9F---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 本文通过实验验证了AI提示词中“身份设定”和“情感措辞”的效果：身份设定可调节输出风格但无法提升准确性，情感措辞能激励AI更用心但不会改变事实判断。核心结论是，AI的准确性取决于底层推理能力，处理事实任务时应优先选择支持推理的模型。
  - Tags: #read #llm

- (2026-03-10) [Package managers keep using git as a database, it never works out](202603/2026-03-10-package-managers-keep-using-git-as-a-database%2C-it-never-works-out.md)
  - 多个包管理器曾尝试用 Git 存储索引，但因性能、可扩展性等问题逐步转向 HTTP 或数据库方案。Git 更适合代码协作，而非包注册表的数据存储。
  - Tags: #read

- (2026-03-10) [Production query plans without production data](202603/2026-03-10-production-query-plans-without-production-data.md)
  - PostgreSQL 18 引入便携式优化器统计信息功能，通过  和  函数，允许在测试环境中注入生产级统计信息，从而在不需要实际数据的情况下模拟真实查询计划，提升CI/CD测试与本地调试效率。
  - Tags: #read #database

- (2026-03-09) [How I Dropped Our Production Database and Now Pay 10% More for AWS](202603/2026-03-09-how-i-dropped-our-production-database-and-now-pay-10%25-more-for-aws.md)
  - 作者因误用Terraform和AI代理导致生产数据库被删，经24小时恢复后，实施状态管理S3化、双重删除保护、独立备份及AI权限限制等措施，承诺未来加强操作隔离。
  - Tags: #read

- (2026-03-09) [GNU and the AI reimplementations - <antirez>](202603/2026-03-09-gnu-and-the-ai-reimplementations---antirez.md)
  - 本文探讨了AI重写软件的合法性，将其与GNU重写UNIX类比，强调不复制代码结构的重写合法且有益。文章呼吁拥抱AI变革，视之为推动开源与软件演进的机会。
  - Tags: #read

- (2026-03-08) [The MCP Abstraction Tax](202603/2026-03-08-the-mcp-abstraction-tax.md)
  - 本文提出了AI代理与API交互中的“抽象税”概念，指出每个抽象层会降低保真度并可能损害上下文。通过对比MCP和CLI路径，作者强调应根据场景权衡迭代速度与上下文管理，并非竞争关系。
  - Tags: #read #agent

- (2026-03-08) [You Need to Rewrite Your CLI for AI Agents](202603/2026-03-08-you-need-to-rewrite-your-cli-for-ai-agents.md)
  - 文章提出，AI代理的CLI需重构以优化可预测性与安全性，包括转向JSON载荷、实时模式查询、上下文限制、输入验证、技能封装等，并建议增量实施。
  - Tags: #read #agent #deepdive

- (2026-03-07) [Avoiding a Culture of Emergencies](202603/2026-03-07-avoiding-a-culture-of-emergencies.md)
  - 优秀管理者通过深入了解业务、明确重点、前瞻布局和关怀团队，有效减少可预防的紧急事件，提升工作效率与成员幸福感，增强人才留存。
  - Tags: #read #career

## Monthly Archive

- [2026-03](202603/monthly-index.md) (32 entries)
- [2026-02](202602/monthly-index.md) (58 entries)
- [2026-01](202601/monthly-index.md) (67 entries)
- [2025-12](202512/monthly-index.md) (68 entries)
- [2025-11](202511/monthly-index.md) (78 entries)
- [2025-10](202510/monthly-index.md) (67 entries)
- [2025-09](202509/monthly-index.md) (40 entries)
- [2025-08](202508/monthly-index.md) (46 entries)
- [2025-07](202507/monthly-index.md) (77 entries)
- [2025-06](202506/monthly-index.md) (75 entries)
- [2025-05](202505/monthly-index.md) (65 entries)
- [2025-04](202504/monthly-index.md) (61 entries)
- [2025-03](202503/monthly-index.md) (49 entries)
- [2025-02](202502/monthly-index.md) (32 entries)
- [2025-01](202501/monthly-index.md) (41 entries)
- [2024-12](202412/monthly-index.md) (45 entries)
- [2024-11](202411/monthly-index.md) (57 entries)
- [2024-10](202410/monthly-index.md) (34 entries)
- [2024-09](202409/monthly-index.md) (46 entries)
- [2024-08](202408/monthly-index.md) (31 entries)
- [2024-07](202407/monthly-index.md) (12 entries)
