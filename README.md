# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-12-19) [The Architecture of "Not Bad": Decoding the Chinese Source Code of the Void](202512/2025-12-19-the-architecture-of-not-bad-decoding-the-chinese-source-code-of-the-void.md)
  - 中文倾向以否定间接肯定（如“没错”），英语则偏好直接肯定（如“great”）。这种差异塑造了灰度思维与直接分类的认知模式，并影响社会互动与商业策略。语言不仅是表达工具，更潜在地决定了现实认知方式。
  - Tags: #read

- (2025-12-19) [AI agents are starting to eat SaaS](202512/2025-12-19-ai-agents-are-starting-to-eat-saas.md)
  - AI代理正颠覆SaaS行业，使企业更易自建定制化工具替代通用SaaS，导致后者客户增长和收入保留率下降。高可用性、网络效应等护城河强的SaaS受影响较小，但后台类工具风险最高。SaaS市场将面临重组，企业需评估技术能力以应对变化。
  - Tags: #read

- (2025-12-19) [Introducing RSC Explorer — overreacted](202512/2025-12-19-introducing-rsc-explorer-%E2%80%94-overreacted.md)
  - 本文介绍了开源工具RSC Explorer，它通过可视化方式帮助开发者理解React Server Components协议。该工具模拟RSC通信，展示组件序列化、异步渲染、动态组件加载及服务器动作调用等场景，旨在提供无需网络请求的教育体验。
  - Tags: #read #deepdive #frontend

- (2025-12-18) [Making our own spectrogram](202512/2025-12-18-making-our-own-spectrogram.md)
  - 这篇文章介绍了用Rust开发音频频谱图可视化工具的全过程，包括傅里叶变换理论、分块加窗处理、多线程架构设计，以及性能优化方案。文章通过实际代码和多种音乐频谱演示，实现了实时音频分析，并讨论了工程实践中的关键权衡。
  - Tags: #read #rust #deepdive

- (2025-12-18) [CET Perceptually Uniform Colour Maps](202512/2025-12-18-cet-perceptually-uniform-colour-maps.md)
  - CET配色方案通过感知均匀设计解决数据可视化中的对比度不均问题，包含线性、发散、彩虹等类型，适用于一般数据、参考数值及色盲友好场景，并提供了相关工具与资源。
  - Tags: #tools

- (2025-12-18) [Inside PostHog: How SSRF, a ClickHouse SQL Escaping 0day, and Default PostgreSQL Credentials Formed an RCE Chain (ZDI-25-099, ZDI-25-097, ZDI-25-096) - Mehmet Ince @mdisec](202512/2025-12-18-inside-posthog-how-ssrf%2C-a-clickhouse-sql-escaping-0day%2C-and-default-postgresql-credentials-formed-an-rce-chain-%28zdi-25-099%2C-zdi-25-097%2C-zdi-25-096%29---mehmet-ince-%40mdisec.md)
  - 本文披露PostHog平台中存在一条组合漏殻链，利用SSRF、ClickHouse SQL注入0day与PostgreSQL默认凭证，实现远程代码执行。攻击可绕过前端验证，将Webhook重定向至内部服务并执行任意命令。漏洞已通过ZDI协调披露，凸显了系统纵深防御的多重失效。
  - Tags: #read #deepdive #security

- (2025-12-18) [What Actually Is Claude Code’s Plan Mode?](202512/2025-12-18-what-actually-is-claude-code%E2%80%99s-plan-mode.md)
  - 本文解析了Claude的“计划模式”，指出它通过系统提示和文件系统路径管理生成Markdown计划，依赖于UI实现审批流程。作者认为这一模式核心功能可通过自定义提示模拟，但集成UX是其独特之处，不过个人更偏好灵活的自然语言编辑方式。
  - Tags: #read #llm

- (2025-12-18) [Announcing support for GROUP BY, SUM, and other aggregation queries in R2 SQL](202512/2025-12-18-announcing-support-for-group-by%2C-sum%2C-and-other-aggregation-queries-in-r2-sql.md)
  - Cloudflare R2 SQL 新增支持的聚合查询功能包含GROUP BY、SUM等，利用Scatter-Gather和Shuffling两种分布式策略处理数据，帮助用户快速获取大数据摘要并支持报告生成和异常检测。该功能已上线，适用于R2存储的Parquet文件。
  - Tags: #read #db

- (2025-12-17) [时间+项目的双维度工作笔记法 - 少数派](202512/2025-12-17-%E6%97%B6%E9%97%B4%2B%E9%A1%B9%E7%9B%AE%E7%9A%84%E5%8F%8C%E7%BB%B4%E5%BA%A6%E5%B7%A5%E4%BD%9C%E7%AC%94%E8%AE%B0%E6%B3%95---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 本文提出“时间+项目”双维度工作笔记法，通过日志、任务、项目、知识四要素整合，帮助职场人应对多任务与长周期项目挑战。方法强调高效记录与检索，支持快速复盘和知识复用，可借助Notion等工具实现，以提高工作效率并减轻大脑负担。
  - Tags: #read

- (2025-12-16) [How a Kernel Bug Froze My Machine: Debugging an Async-profiler Deadlock | QuestDB](202512/2025-12-16-how-a-kernel-bug-froze-my-machine-debugging-an-async-profiler-deadlock-questdb.md)
  - 作者在使用 async-profiler 时遭遇一个由 Linux 内核 6.17 引入的 bug，导致系统死锁。该问题在于 cpu-clock 事件处理中的 hrtimer 回调陷入循环等待。解决方案是内核补丁将 hrtimer_cancel 改为非阻塞调用并引入延迟停止标志，临时规避方法是使用 -e ctimer 选项。作者通过 QEMU 和 GDB 成功调试并定位问题。
  - Tags: #read #kernel #deepdive

## Monthly Archive

- [2025-12](202512/monthly-index.md) (47 entries)
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
