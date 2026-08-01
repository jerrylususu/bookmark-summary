# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-08-01) [Browsers Treat Big Sites Differently](202608/2026-08-01-browsers-treat-big-sites-differently.md)
  - Safari与Firefox因Chrome垄断，被迫为特定网站内置域名级修复，弥补其仅适配Chrome的缺陷。此举虽解燃眉之急，却助长不良循环，重演IE霸权，侵蚀互联网开放。开发者应跨浏览器测试，主动遵循标准。
  - Tags: #read #web

- (2026-08-01) [Should You Use AI for a Task? Here’s a Simple Way to Decide - Schneier on Security](202608/2026-08-01-should-you-use-ai-for-a-task-here%E2%80%99s-a-simple-way-to-decide---schneier-on-security.md)
  - 文章提出以“工作”和“健身房”区分任务：前者重结果，可用AI代劳；后者重过程，须亲力亲为以锻炼能力。务必警惕依赖AI导致技能萎缩，主动保留“健身房”任务。
  - Tags: #read

- (2026-08-01) [smevals - a small eval suite for evaluating models, prompts, and harnesses | Prime Radiant](202608/2026-08-01-smevals---a-small-eval-suite-for-evaluating-models%2C-prompts%2C-and-harnesses-prime-radiant.md)
  - smevals 是评估小模型的 CLI 工具，可自定义任务和评分，对比多模型，支持编码代理辅助搭建评估，并提供可视化报告，帮助从廉价模型中找到最佳方案。
  - Tags: #read #agent #llm

- (2026-08-01) [Write-Only Code | Heavybit](202608/2026-08-01-write-only-code-heavybit.md)
  - 随着大语言模型生成代码能力的提升，软件行业正进入“只写代码”时代：AI直接生成并部署代码，人类审查不再可行。工程师角色将从代码编写者转向系统设计师，专注接口、约束与风险管理，并建立新的信任机制以应对无人阅读代码的现实。
  - Tags: #read #agent

- (2026-07-29) [You don't have to be smart if you can think clearly](202607/2026-07-29-you-don%27t-have-to-be-smart-if-you-can-think-clearly.md)
  - 工程师分“聪明”与“强大”两类：聪明者依赖直觉，遇难题易慌乱；强大者则能放慢思考，识别不变的事实，稳步推导。真正的效能来自这种缓慢而清晰的思维能力，它比瞬时灵感更可靠、更可修炼。
  - Tags: #read

- (2026-07-28) [The Best Prioritization Is No Prioritization](202607/2026-07-28-the-best-prioritization-is-no-prioritization.md)
  - 这篇文章主张创业公司应放弃复杂的优先级排序，转而通过提升执行速度，或组建固定团队各自专注，将跨领域排序转化为资源分配，以此减少内耗、提高效率。
  - Tags: #read

- (2026-07-26) [Printing the web: making webpages look good on paper](202607/2026-07-26-printing-the-web-making-webpages-look-good-on-paper.md)
  - 打印样式常被忽视，却是无障碍与全流程体验的关键。本文介绍媒体查询打印、分页控制、链接显示与墨水优化等技巧，指出打印设计能反哺屏幕体验。
  - Tags: #read #frontend #css

- (2026-07-26) [AI Hot Takes From A Platform Engineer / SRE](202607/2026-07-26-ai-hot-takes-from-a-platform-engineer-sre.md)
  - 本文是平台工程师对AI热潮的冷思考：批判术语炒作、落地尴尬，指出AI学习便利无需焦虑追新，但基础设施即代码等领域表现糟糕。建议屏蔽噪音、专注核心，要求生产环境演示验证真实价值。
  - Tags: #read

- (2026-07-26) [What's the best way to do authentication in modern applications](202607/2026-07-26-what%27s-the-best-way-to-do-authentication-in-modern-applications.md)
  - 前端身份验证应将令牌优先存于httpOnly Cookie（配合Session），而非localStorage，以防XSS窃取。同时需防御CSRF、采用BFF架构或OAuth拆分存储，将凭证尽量隐藏于服务端，并结合refresh token轮换与设备绑定，最大限度缩小泄露风险。
  - Tags: #read #deepdive #security

- (2026-07-26) [A faster way to copy SQLite databases between computers](202607/2026-07-26-a-faster-way-to-copy-sqlite-databases-between-computers.md)
  - 使用  直接传输大型 SQLite 数据库缓慢且易损坏。改用  导出为 SQL 文本，索引仅存命令，压缩后体积大幅缩小，再通过 SSH 和 rsync 传输，本地重建数据库，既提速又可靠。
  - Tags: #read #tips

## Monthly Archive

- [2026-08](202608/monthly-index.md) (4 entries)
- [2026-07](202607/monthly-index.md) (30 entries)
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
