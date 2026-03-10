# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-03-10) [Production query plans without production data](202603/2026-03-10-production-query-plans-without-production-data.md)
  - PostgreSQL 18 引入便携式优化器统计信息功能，通过 `pg_restore_relation_stats` 和 `pg_restore_attribute_stats` 函数，允许在测试环境中注入生产级统计信息，从而在不需要实际数据的情况下模拟真实查询计划，提升CI/CD测试与本地调试效率。
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

- (2026-03-06) [Disable Your SSH Access With This One Simple Trick](202603/2026-03-06-disable-your-ssh-access-with-this-one-simple-trick.md)
  - 作者使用 scp 传输目录后，因目标目录权限被设为 777，导致 SSH 登录失败。原因是 OpenSSH 安全策略拒绝过宽权限。将权限恢复为 700 后问题解决，该问题已在后续版本修复。
  - Tags: #read #tips

- (2026-03-06) [2026 年，我把自己做成了一个 AI](202603/2026-03-06-2026-%E5%B9%B4%EF%BC%8C%E6%88%91%E6%8A%8A%E8%87%AA%E5%B7%B1%E5%81%9A%E6%88%90%E4%BA%86%E4%B8%80%E4%B8%AA-ai.md)
  - 作者罗磊于2026年构建AI数字分身，通过多模型画像和RAG对话技术管理知识，强调主动构建个人系统的重要性。
  - Tags: #read #llm

- (2026-03-06) [Cognitive Debt: When Velocity Exceeds Comprehension | rockoder](202603/2026-03-06-cognitive-debt-when-velocity-exceeds-comprehension-rockoder.md)
  - AI辅助开发导致代码生成速度远超工程师理解速度，形成“认知债务”。组织过度关注产出指标而忽视理解深度，引发审查失效、知识流失和系统风险。需改革绩效评估，纳入理解深度以应对长期挑战。
  - Tags: #read #career

- (2026-03-06) [AI=true is an Anti-Pattern](202603/2026-03-06-ai%3Dtrue-is-an-anti-pattern.md)
  - 文章批评了编程中针对AI设计文档、工具和工作流的反模式，主张统一接口与通用设计，以兼顾人类与AI，提升协作效率和互操作性。
  - Tags: #read

## Monthly Archive

- [2026-03](202603/monthly-index.md) (28 entries)
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
