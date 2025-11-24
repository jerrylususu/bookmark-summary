# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

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

- (2025-11-23) [Why it takes months to tell if new AI models are good](202511/2025-11-23-why-it-takes-months-to-tell-if-new-ai-models-are-good.md)
  - 评估AI模型质量面临三大难题：现有基准易被操纵且脱离实际，主观判断不可靠，真实场景测试又耗时费力。当模型智能超越人类后，进步更难被感知，导致AI是否停滞的争议无解。
  - Tags: #read #llm #eval

- (2025-11-23) [一次性软件与被压缩的现实：AI Native 的本质是策略重构](202511/2025-11-23-%E4%B8%80%E6%AC%A1%E6%80%A7%E8%BD%AF%E4%BB%B6%E4%B8%8E%E8%A2%AB%E5%8E%8B%E7%BC%A9%E7%9A%84%E7%8E%B0%E5%AE%9E%EF%BC%9Aai-native-%E7%9A%84%E6%9C%AC%E8%B4%A8%E6%98%AF%E7%AD%96%E7%95%A5%E9%87%8D%E6%9E%84.md)
  - AI时代下，一次性软件通过低成本生成实现高解析度决策，使组织从依赖直觉转向数据驱动，推动协作透明化和代码工具化，实现决策范式升级。
  - Tags: #read #llm

- (2025-11-22) [Zed Is Our Office - Zed Blog](202511/2025-11-22-zed-is-our-office---zed-blog.md)
  - Zed编辑器内置团队协作功能，以频道系统为核心，支持多人实时编辑、屏幕共享及角色管理，适用于会议记录、项目协作等场景。目前处于免费alpha阶段，旨在打造无缝协作的软件开发工具。
  - Tags: #read

- (2025-11-22) [Intermediate Developer](202511/2025-11-22-intermediate-developer.md)
  - 文章总结了中级开发者的成长要点：注重代码质量与团队协作，强调文档、测试和持续学习的重要性，认为沟通是编程的核心能力。
  - Tags: #read

- (2025-11-22) [We should all be using dependency cooldowns](202511/2025-11-22-we-should-all-be-using-dependency-cooldowns.md)
  - 文章主张通过设定“依赖冷却期”（如7-14天）延迟引入新依赖，以避开开源供应链攻击的高风险窗口。该措施成本低、易实施，能防御多数短期攻击，虽非万能但可显著降低风险，建议广泛采用。
  - Tags: #read #security

- (2025-11-22) [What if you don't need MCP at all?](202511/2025-11-22-what-if-you-don%27t-need-mcp-at-all.md)
  - 本文提倡用自定义命令行工具和代码替代复杂的MCP服务器，以浏览器工具为例展示了简单方案的优越性。通过短小精悍的脚本实现浏览器控制、页面操作等功能，显著节省上下文资源且易于扩展。强调利用代码组合性和代理执行能力可构建高效灵活的工作流，适合需要代码执行的场景。
  - Tags: #read #llm

## Monthly Archive

- [2025-11](202511/monthly-index.md) (73 entries)
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
