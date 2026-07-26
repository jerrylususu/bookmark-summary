# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-07-26) [A faster way to copy SQLite databases between computers](202607/2026-07-26-a-faster-way-to-copy-sqlite-databases-between-computers.md)
  - 使用 `rsync` 直接传输大型 SQLite 数据库缓慢且易损坏。改用 `.dump` 导出为 SQL 文本，索引仅存命令，压缩后体积大幅缩小，再通过 SSH 和 rsync 传输，本地重建数据库，既提速又可靠。
  - Tags: #read #tips

- (2026-07-26) [LLMs reward expertise](202607/2026-07-26-llms-reward-expertise.md)
  - 文章以陶哲轩和编程为例，指出领域专业知识是高效使用大语言模型的关键，专业判断力能让模型输出更精炼、价值更高，人类的角色不可替代。
  - Tags: #read #llm

- (2026-07-26) [Being Linux Torvalds - <antirez>](202607/2026-07-26-being-linux-torvalds---antirez.md)
  - Linus的卓越在于早期停止编码，专注设计领导与一致性把控。AI编程时代，专家应扮演类似角色，主导AI代理并注入设计判断，而非亲自写代码。工具降低门槛，但设计能力仍是核心竞争力。
  - Tags: #read #agent

- (2026-07-22) [Not just development, distribution of software may change as well - <antirez>](202607/2026-07-22-not-just-development%2C-distribution-of-software-may-change-as-well---antirez.md)
  - AI编程让用户能自行修改源码，传统分支模式过时。代码库正成为可演化的模板，实验性分支与范例代码价值凸显，文档也需对代理友好。开发者应适应这种流动、可塑的软件分发新范式。
  - Tags: #read

- (2026-07-21) [Stop Using OpenCode](202607/2026-07-21-stop-using-opencode.md)
  - OpenCode 体验极差且安全形同虚设：性能低下、上下文混乱、界面反人类；权限过滤易被绕过、默认联网泄密、存在远程代码执行漏洞。作者强烈建议立即停用。
  - Tags: #read #agent #security

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

## Monthly Archive

- [2026-07](202607/monthly-index.md) (25 entries)
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
