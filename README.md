# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-12-01) [Migrating Dillo from GitHub](202512/2025-12-01-migrating-dillo-from-github.md)
  - Dillo项目从GitHub迁移至自托管服务器以规避平台风险，包括兼容性差、单点故障和过度依赖JavaScript等问题。新方案使用cgit和轻量级工具，并设置多镜像保障数据安全，支持离线开发。迁移后GitHub仓库将归档，项目通过捐赠维持运行。
  - Tags: #read

- (2025-11-30) [Context plumbing](202511/2025-11-30-context-plumbing.md)
  - 作者强调AI系统的核心在于意图识别和动态上下文管理。意图识别需抢占用户需求瞬间，上下文需通过实时管道传递以避免延迟。基于Cloudflare的成功实践验证了该架构的有效性。
  - Tags: #read #llm

- (2025-11-29) [Own A Graph](202511/2025-11-29-own-a-graph.md)
  - 资深工作者应创建核心图表，以简洁沟通工作价值、获取反馈并提升业绩。建议聚焦关键指标，结合目标迭代优化，让他人引用是成功标志。缺少图表时应尽快补上。
  - Tags: #read #career

- (2025-11-29) [How I Coding? (Nov 2025 Edition)](202511/2025-11-29-how-i-coding-%28nov-2025-edition%29.md)
  - 文章介绍了作者2025年11月的编程心得，强调在高级AI模型时代需重视提示词优化，推荐使用Conductor工具提升效率，并建议基于个人需求构建评估体系，以平衡实践与乐趣。
  - Tags: #read

- (2025-11-29) [How good engineers write bad code at big companies](202511/2025-11-29-how-good-engineers-write-bad-code-at-big-companies.md)
  - 大公司代码质量差主要源于组织结构问题：高人员流动率、忽略专业积累、资深工程师负担过重及工作压力，公司为了组织灵活性牺牲代码质量。个人难以改变，需积极适应和积累专长。
  - Tags: #read #career #people

- (2025-11-26) [Becoming unblockable](202511/2025-11-26-becoming-unblockable.md)
  - 文章提出六项核心策略帮助职场人减少受阻：多任务并行、提前规划关键环节、优化开发工具、主动跨领域调试、建立人际关系网和高层协作。这些方法能显著提升工作效率和问题解决能力。
  - Tags: #read #career

- (2025-11-24) ["Good engineering management" is a fad](202511/2025-11-24-good-engineering-management-is-a-fad.md)
  - 文章指出，工程管理的“良好管理”标准实为受商业现实驱动的暂时潮流，不同时期的需求会变化。作者建议培养八项核心与成长技能（如执行、清晰度、应对模糊性），并强调自我认知与职业规划，以灵活应对行业变化，避免固守过时理念。核心是适应力胜过盲目追随潮流。
  - Tags: #read #career

- (2025-11-24) [写在 PicGo 即将 8 周年之际 | MARKSZのBlog](202511/2025-11-24-%E5%86%99%E5%9C%A8-picgo-%E5%8D%B3%E5%B0%86-8-%E5%91%A8%E5%B9%B4%E4%B9%8B%E9%99%85-marksz%E3%81%AEblog.md)
  - PicGo是一款便捷的跨平台图片上传工具，自2017年起伴随开发者从学生到职场人的成长。项目经历了技术提升、生态扩展，职业变动则体现其追求技术价值与用户需求结合，坚持团队合作与生活平衡的价值观。
  - Tags: #read

- (2025-11-24) [Exfiltration via ffmpeg](202511/2025-11-24-exfiltration-via-ffmpeg.md)
  - 允许用户自定义ffmpeg参数存在安全风险：攻击者可能利用-attach参数窃取本地文件或发起SSRF攻击，通过tcp/tls协议外泄数据。建议严格过滤参数并加强网络隔离防御。
  - Tags: #read #security #hack

- (2025-11-23) [LLM APIs are a Synchronization Problem](202511/2025-11-23-llm-apis-are-a-synchronization-problem.md)
  - 文章指出当前LLM API设计存在底层状态与消息抽象不匹配的问题，导致同步困难和效率低下。建议借鉴本地优先软件的状态同步理念，将对话历史作为可增量同步的日志，而非全量传输，并倡导未来API转向明确状态管理的设计标准。
  - Tags: #read #llm #distributed

## Monthly Archive

- [2025-12](202512/monthly-index.md) (1 entries)
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
