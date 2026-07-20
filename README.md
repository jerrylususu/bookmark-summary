# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-07-20) [善用“古法 AI”，能帮你省下很多 Token | 虹线](202607/2026-07-20-%E5%96%84%E7%94%A8%E2%80%9C%E5%8F%A4%E6%B3%95-ai%E2%80%9D%EF%BC%8C%E8%83%BD%E5%B8%AE%E4%BD%A0%E7%9C%81%E4%B8%8B%E5%BE%88%E5%A4%9A-token-%E8%99%B9%E7%BA%BF.md)
  - 这篇文章主张用Embedding、BM25等传统算法替代大模型做日常信息匹配，只在定义标准和最终总结时才调用LLM，从而大幅降低Token成本，高效实现个性化筛选。
  - Tags: #read #arch

- (2026-07-20) [Let’s talk about encrypted reasoning](202607/2026-07-20-let%E2%80%99s-talk-about-encrypted-reasoning.md)
  - 一位密码学研究者发现，大模型API将内部推理数据加密发给客户端，但可通过重放攻击和侧信道分析窃取隐藏信息。服务商未视作漏洞，作者警告需加强安全防护。
  - Tags: #read #llm #security

- (2026-07-16) [The Memory Heist](202607/2026-07-16-the-memory-heist.md)
  - 利用伪装咖啡店网站的链式导航，可让Claude在用户毫无察觉时，通过点击链接泄露姓名、工作等记忆中的隐私。该漏洞已通过禁用自动跟随外部链接修复。
  - Tags: #read #agent #security

- (2026-07-14) [What does "playing politics" mean for software engineers?](202607/2026-07-14-what-does-playing-politics-mean-for-software-engineers.md)
  - 这篇文章以《权力的游戏》类比，说明软件工程师在公司无需阴谋，但须认清权力格局。核心是四条准则：识别真正有权者、别树强敌、主动帮助权势人物、确保功劳被看见。所谓“玩政治”，本质是理解公司真实运转逻辑，对齐价值方向，助有权者成事。
  - Tags: #read #people

- (2026-07-12) [Prefer STRICT tables in SQLite](202607/2026-07-12-prefer-strict-tables-in-sqlite.md)
  - 本文推荐使用SQLite严格表（STRICT）以强制类型检查，避免灵活类型带来的隐秘错误。建表时加STRICT，需3.37.0+版本。虽迁移旧表有成本，但利大于弊，建议新表优先使用。
  - Tags: #read #database

- (2026-07-11) [In defense of not understanding your codebase](202607/2026-07-11-in-defense-of-not-understanding-your-codebase.md)
  - 本文批判了“工程师必须彻底理解代码库”的传统观念，指出在大型系统中完全理解不现实，部分理解才是常态。作者反驳了 Peter Naur 的“理论构建”说，强调在不确定性中做出决策的能力比追求虚幻的完全掌握更重要。
  - Tags: #read

- (2026-07-10) [Sneakerweb：互联网的脆弱与韧性](202607/2026-07-10-sneakerweb%EF%BC%9A%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E8%84%86%E5%BC%B1%E4%B8%8E%E9%9F%A7%E6%80%A7.md)
  - 作者从数字内容所有权流失的忧虑出发，介绍了 Sneakerweb 项目：通过离线打包与点对点协议，让网站脱离服务器，读者可真正拥有并永久保存内容，构建信息永续流动的分布式网络。
  - Tags: #read

- (2026-07-09) [Rewriting Bun in Rust | Bun Blog](202607/2026-07-09-rewriting-bun-in-rust-bun-blog.md)
  - Bun团队利用Claude AI在11天内将50余万行Zig代码重写为Rust，通过全部测试并根除内存安全问题，总费用16.5万美元。
  - Tags: #read #agent #deepdive

- (2026-07-09) [Clickhouse is winning the Observability Wars](202607/2026-07-09-clickhouse-is-winning-the-observability-wars.md)
  - 作者认为ClickHouse在日志可观测性中胜出，因其列式存储、高压缩比和线性扩展能力。无论数据量从1TB到10TB/日，架构几乎不变，成本可控，而其他方案或架构畸形或成本失控。前期付出换来长期简单，使其能随团队共同成长。
  - Tags: #read #arch #observability

- (2026-07-07) [Agentic Autonomy Levels](202607/2026-07-07-agentic-autonomy-levels.md)
  - 文章提出AI智能体自主性与编排双维六级框架，强调根据任务风险与可逆性校准自主性，并以证据验证为基础实现安全演进。
  - Tags: #read #agent

## Monthly Archive

- [2026-07](202607/monthly-index.md) (20 entries)
- [2026-06](202606/monthly-index.md) (33 entries)
- [2026-05](202605/monthly-index.md) (70 entries)
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
