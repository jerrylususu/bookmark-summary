# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-11-02) [The Linux Boot Process: From Power Button to Kernel](202511/2025-11-02-the-linux-boot-process-from-power-button-to-kernel.md)
  - 计算机启动过程从CPU复位、固件自检开始，逐步解压并加载内核，切换运行模式（实模式到保护模式再到长模式），最终移交控制权给操作系统内核。
  - Tags: #read #linux #deepdive

- (2025-11-02) [Building Multi-Agent Systems (Part 2)](202511/2025-11-02-building-multi-agent-systems-%28part-2%29.md)
  - 自多智能体系统系列首篇发布以来，基于LLM的智能体架构在工具调用能力和长时间运行方面显著进步，其核心思想——任务分解和协作——已成为标准，但架构设计变得更加灵活。重点从复杂流程设计转向提供上下文和目标的“上下文工程”，使智能体更加自主。同时，新挑战出现在系统控制、安全性和长时间任务的用户体验上。
  - Tags: #read #llm

- (2025-11-02) [How I Use Every Claude Code Feature](202511/2025-11-02-how-i-use-every-claude-code-feature.md)
  - 本文总结了Claude Code的高效使用方法，重点包括：通过CLAUDE.md文件维护项目规范，利用上下文管理保持会话连贯，避免过度依赖自定义命令与子代理。建议结合钩子机制优化工作流，使用SDK快速开发工具，并集成GitHub Actions实现自动化。强调以实际产出为导向，逐步完善AI辅助的工程流程。
  - Tags: #read #llm #tips

- (2025-11-02) [Scraping Next.js web sites in 2025 – Trickster Dev](202511/2025-11-02-scraping-next.js-web-sites-in-2025-%E2%80%93-trickster-dev.md)
  - 文章介绍了使用Python库njsparser抓取Next.js网站的方法，重点解析其Flight Data等数据序列化格式。工具可简化从HTML中提取分块数据的过程，适用于现代前端框架的数据抓取场景。
  - Tags: #read #frontend

- (2025-10-30) [A Practitioner's Guide to Wide Events | Jeremy Morrell](202510/2025-10-30-a-practitioner%27s-guide-to-wide-events-jeremy-morrell.md)
  - 宽事件是一种增强系统可观测性的方法，通过记录每个工作单元的全部相关数据形成一个完整事件，便于查询分析。实施包括选择工具、编写代码添加丰富属性、掌握查询技巧。此方法可大幅提升调试效率。
  - Tags: #read #deepdive #distributed #explainer

- (2025-10-30) [Stacking Threads](202510/2025-10-30-stacking-threads.md)
  - 该文章分析了多线程程序中线程栈和线程控制块在进程内存中的布局差异，指出不同操作系统（如Linux、macOS、FreeBSD等）的线程栈放置位置与TCB管理方式显著不同。跨平台编程需注意内存布局随机性、栈位置不固定等特性，强调操作系统抽象层的复杂性。
  - Tags: #read

- (2025-10-30) [用一次摸鱼经历详解AI管理实战](202510/2025-10-30-%E7%94%A8%E4%B8%80%E6%AC%A1%E6%91%B8%E9%B1%BC%E7%BB%8F%E5%8E%86%E8%AF%A6%E8%A7%A3ai%E7%AE%A1%E7%90%86%E5%AE%9E%E6%88%98.md)
  - 作者通过AI管理五步法（选模型、下指令、做培训、给方法、定验收），实现用5%精力撬动AI完成95%工作。核心是像管理团队一样引导AI，将人类时间聚焦于战略决策，大幅提升生产力。
  - Tags: #read #llm #people

- (2025-10-30) [How many pillars of observability can you fit on the head of a pin?](202510/2025-10-30-how-many-pillars-of-observability-can-you-fit-on-the-head-of-a-pin.md)
  - 作者批判“可观测性支柱”为营销术语，提倡用“信号”概念统一存储数据，避免多支柱模型导致的隔阂与高成本，强调OpenTelemetry等统一方案更高效。
  - Tags: #read

- (2025-10-30) [Why do AI models use so many em-dashes?](202510/2025-10-30-why-do-ai-models-use-so-many-em-dashes.md)
  - AI模型过度使用破折号的现象主要源于训练数据的变化。GPT-4等模型为获取高质量数据，数字化了大量19世纪末到20世纪初的书籍，这些历史文本中破折号使用率较高，导致模型习得这一习惯。强化学习人类反馈或AI内容循环也可能加剧此现象，但核心原因在于训练数据的历史语言风格影响。
  - Tags: #read #llm

- (2025-10-29) [High Agency Matters](202510/2025-10-29-high-agency-matters.md)
  - 文章强调，个人能动性（主动行动和担当）比高智商更能决定长期成功。高能动性者通过执行力、坚持和风险承担创造实际成果，而智力易导致分析瘫痪。在AI时代，能动性作为人类独特优势愈发重要，应优先培养。
  - Tags: #read #people

## Monthly Archive

- [2025-11](202511/monthly-index.md) (4 entries)
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
