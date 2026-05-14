# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-05-14) [What’s with all the slide decks?](202605/2026-05-14-what%E2%80%99s-with-all-the-slide-decks.md)
  - 现代职场流行幻灯片沟通，源于管理咨询业推动与技术便利，而非必然选择。亚马逊等机构证明书面备忘录同样有效，作者呼吁支持博客文化以对抗幻灯片主导趋势。
  - Tags: #read

- (2026-05-14) [High Performance Rate Limiting at Databricks](202605/2026-05-14-high-performance-rate-limiting-at-databricks.md)
  - Databricks 2023 年重构限流系统，以内存分片、异步批量报告和令牌桶算法替代原有 Redis 架构，提升性能与扩展性，牺牲严格准确性以容忍小幅超限。
  - Tags: #read #backend

- (2026-05-14) [一盎司黄金 - Miao Yu | 于淼](202605/2026-05-14-%E4%B8%80%E7%9B%8E%E5%8F%B8%E9%BB%84%E9%87%91---miao-yu-%E4%BA%8E%E6%B7%BC.md)
  - 本文以“一盎司黄金”为切入点，指出古今中外婚姻支付均以约一年生活成本的硬通货为经济安全垫。作者引入“鲍莫尔成本病”理论，解释现代住房、教育等竞争层成本膨胀的必然性，呼吁从经济结构共性理解婚姻支付演变。
  - Tags: #read

- (2026-05-12) [工程师如何把多个 Coding Agent 真正带起来：一套比“开更多聊天窗口”更像工程流程的方法 - 白宦成](202605/2026-05-12-%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%A6%82%E4%BD%95%E6%8A%8A%E5%A4%9A%E4%B8%AA-coding-agent-%E7%9C%9F%E6%AD%A3%E5%B8%A6%E8%B5%B7%E6%9D%A5%EF%BC%9A%E4%B8%80%E5%A5%97%E6%AF%94%E2%80%9C%E5%BC%80%E6%9B%B4%E5%A4%9A%E8%81%8A%E5%A4%A9%E7%AA%97%E5%8F%A3%E2%80%9D%E6%9B%B4%E5%83%8F%E5%B7%A5%E7%A8%8B%E6%B5%81%E7%A8%8B%E7%9A%84%E6%96%B9%E6%B3%95---%E7%99%BD%E5%AE%A6%E6%88%90.md)
  - Vibe Kanban通过看板机制管理多Agent任务，支持并行执行与流程串联，显著提升工程效率。它适合擅长任务拆解的工程师，但已停止运营并转向开源，为未来Agent管理方案提供了参考。
  - Tags: #read #agent

- (2026-05-12) [AI如何导致和修复了我的失眠问题](202605/2026-05-12-ai%E5%A6%82%E4%BD%95%E5%AF%BC%E8%87%B4%E5%92%8C%E4%BF%AE%E5%A4%8D%E4%BA%86%E6%88%91%E7%9A%84%E5%A4%B1%E7%9C%A0%E9%97%AE%E9%A2%98.md)
  - 该错误源于请求参数验证失败，因域名“ai-sleep.html”含文件扩展名，不符合有效格式。需检查并修正URL，确保使用正确域名或完整路径。
  - Tags: #read

- (2026-05-12) [Neural Computer：一种新的机器形态，正在出现](202605/2026-05-12-neural-computer%EF%BC%9A%E4%B8%80%E7%A7%8D%E6%96%B0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%BD%A2%E6%80%81%EF%BC%8C%E6%AD%A3%E5%9C%A8%E5%87%BA%E7%8E%B0.md)
  - Neural Computer（NC）是一种以运行时为核心的新机器形态，区别于传统计算机和Agent，强调能力沉淀与持续运行。它需满足图灵完备、通用可编程等条件，当前原型已展示部分能力，但尚不完善。若成立，将重塑软件、硬件及编程概念，推动机器内部进化。
  - Tags: #read

- (2026-05-12) [Learning on the Shop floor](202605/2026-05-12-learning-on-the-shop-floor.md)
  - Shopify内部开发的River工具在Slack公共频道运行，实现透明协作与知识共享，类似Midjourney的Discord模式，促进团队效率和渗透式学习。
  - Tags: #read

- (2026-05-12) [James Shore: You Need AI That Reduces Maintenance Costs](202605/2026-05-12-james-shore-you-need-ai-that-reduces-maintenance-costs.md)
  - AI编程工具若仅提升编码速度却增加维护成本，短期收益将被长期负担抵消。关键在于AI必须按比例降低维护成本（如速度翻倍则维护减半），才能实现可持续的生产力提升。团队需兼顾编码效率与维护优化，避免“短期加速、长期锁死”的陷阱。
  - Tags: #read

- (2026-05-11) [Index 1,600,000,000 Keys with Automata and Rust - Andrew Gallant's Blog](202605/2026-05-11-index-1%2C600%2C000%2C000-keys-with-automata-and-rust---andrew-gallant%27s-blog.md)
  - 本文介绍基于有限状态机（FSM）的高效字符串索引方法，通过Rust的库实现有序集合与映射的压缩存储与快速查询。实验表明，该技术在压缩率和查询速度上优于传统工具，适用于静态大规模数据，但不支持频繁更新。
  - Tags: #read #data #deepdive #rust

- (2026-05-11) [Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binary](202605/2026-05-11-replacing-a-3-gb-sqlite-database-with-a-10-mb-fst-%28finite-state-transducer%29-binary.md)
  - 作者用 Rust 和 FST 库重写芬兰语-英语词典应用，将体积从 3GB 压缩至 10MB，实现 300 倍空间优化，同时保持搜索性能。
  - Tags: #read #hack

## Monthly Archive

- [2026-05](202605/monthly-index.md) (42 entries)
- [2026-04](202604/monthly-index.md) (57 entries)
- [2026-03](202603/monthly-index.md) (70 entries)
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
