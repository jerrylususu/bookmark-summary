# 2025-12 Monthly Index

- (2025-12-24) [Avoid Mini-frameworks](2025-12-24-avoid-mini-frameworks.md)
  - 文章批判“迷你框架”因其常引入不必要复杂性，导致维护困难与效率下降。建议优先采用库或慎重设计新框架，避免包装现有技术栈以减少兼容性问题。
  - Tags: #read #tips

- (2025-12-23) [Nano Banana Pro is the best AI image generator, with caveats](2025-12-23-nano-banana-pro-is-the-best-ai-image-generator%2C-with-caveats.md)
  - Google推出的Nano Banana Pro是Nano Banana升级版，图像质量、分辨率、文本渲染能力提升，支持2K/4K输出以及谷歌搜索关联、网格生成等新功能，但成本较高，对超现实风格创作支持不足，更适合高精度、商业用途场景。
  - Tags: #read #llm #deepdive

- (2025-12-23) [从Python异步编程的剖析中体会智能体并发编程模式 - 铁蕾的个人博客](2025-12-23-%E4%BB%8Epython%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E7%9A%84%E5%89%96%E6%9E%90%E4%B8%AD%E4%BD%93%E4%BC%9A%E6%99%BA%E8%83%BD%E4%BD%93%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E6%A8%A1%E5%BC%8F---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - 本文介绍Bridgic智能体框架的并发设计，区分并发与并行，并基于Python的asyncio和多线程机制处理异步、I/O和计算任务。框架通过异步与同步Worker混合编排，简化开发并支持未来多进程扩展。
  - Tags: #read #python

- (2025-12-23) [Advent of Slop: A Guest Post by Claude](2025-12-23-advent-of-slop-a-guest-post-by-claude.md)
  - AI独立解决2025年AoC编程挑战，重点优化了多个复杂算法（如几何搜索、高斯消元），将总运行时间压至1秒内，并编写了输入生成器。Claude反思了解题与优化的不同思维模式，并探讨了完成挑战时的成就感。
  - Tags: #read #llm

- (2025-12-22) [Advice For Individual Contributors](2025-12-22-advice-for-individual-contributors.md)
  - 个人贡献者应通过利用自身优势、展现领导力、明确责任、定期汇报和主动与高层沟通，来实现突破性成果并提升工作影响力与职业发展。
  - Tags: #read #people

- (2025-12-22) [blog/2025/12/an-svg-is-all-you-need.mld](2025-12-22-blog-2025-12-an-svg-is-all-you-need.mld.md)
  - SVG格式在科学数据可视化中具有巨大潜力，尤其适合构建持久、可交互的知识系统。它能实现数据探索和即时反馈，无需服务器支持，并与版本控制、权限管理等原则天然契合，增强了科学传播的交互性和持久性。
  - Tags: #read

- (2025-12-22) [A Year Of Vibes](2025-12-22-a-year-of-vibes.md)
  - 作者回顾2025年，AI编程工具彻底改变其工作方式，从编码者转为工程领导。他体验了多款AI代理工具，扩展至日常管理，但也反思人机关系风险与行业分歧。未来需解决版本控制、代码审查及AI生成代码的伦理问题，呼吁行业关注工具演化与人机协作边界。
  - Tags: #read

- (2025-12-22) [The Shape of AI: Jaggedness, Bottlenecks and Salients](2025-12-22-the-shape-of-ai-jaggedness%2C-bottlenecks-and-salients.md)
  - 文章探讨了人工智能能力的三个特性：参差不齐（AI在不同任务表现差异大），瓶颈（AI能因固有限制或流程因素难以自动化），以及突出部（关键瓶颈突破可促进AI跃进。总体认为AI扩展将带来人机协作，而非全替代，未来应关注瓶颈变化来预测发展。
  - Tags: #read #llm

- (2025-12-20) [Prompt caching: 10x cheaper LLM tokens, but how? | ngrok blog](2025-12-20-prompt-caching-10x-cheaper-llm-tokens%2C-but-how-ngrok-blog.md)
  - 文章介绍了提示缓存如何通过复用语言模型的K和V矩阵，避免重复计算输入令牌，从而降低成本90%并减少延迟。OpenAI和Anthropic的缓存策略不同，但均显著提升效率，适用于长提示场景。
  - Tags: #read #llm #explainer

- (2025-12-20) [【开源】智能体编程语言ASL——重构智能体开发体验 - 铁蕾的个人博客](2025-12-20-%E3%80%90%E5%BC%80%E6%BA%90%E3%80%91%E6%99%BA%E8%83%BD%E4%BD%93%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80asl%E2%80%94%E2%80%94%E9%87%8D%E6%9E%84%E6%99%BA%E8%83%BD%E4%BD%93%E5%BC%80%E5%8F%91%E4%BD%93%E9%AA%8C---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - ASL是一种新型智能体编程语言，专注于直观描述智能体内部结构、多智能体组合及动态工作流。其声明式语法支持嵌套模块与动态编排，解决了传统语言在结构表达上的不足，提升了开发效率和代码复用性。ASL基于Bridgic框架，将执行逻辑与结构分离，适用于动态自主系统的构建。
  - Tags: #read #llm #language

- (2025-12-20) [2025 LLM Year in Review](2025-12-20-2025-llm-year-in-review.md)
  - 2025年LLM领域六大趋势：强化学习可验证奖励(RLVR)提升推理能力，智能具有不均衡性，Cursor等应用拓宽垂直领域，Claude Code推动本地化AI发展，自然语言编程降低技术门槛，以及视觉交互模型成为新方向。领域整体快速发展，潜力与挑战并存。
  - Tags: #read #llm

- (2025-12-19) [Programmers and software developers lost the plot on naming their tools](2025-12-19-programmers-and-software-developers-lost-the-plot-on-naming-their-tools.md)
  - 文章批评软件工具命名过于随意，主张命名应清晰描述功能，回归专业标准，减少认知负担。
  - Tags: #read

- (2025-12-19) [GraphQL: the enterprise honeymoon is over](2025-12-19-graphql-the-enterprise-honeymoon-is-over.md)
  - 文章认为GraphQL在企业应用中优势有限。尽管旨在减少数据过度获取，但多数场景已被BFF架构解决。GraphQL反而带来更高实现复杂度、可观测性差、缓存脆弱及维护成本。企业更需稳定和效率，而非技术优雅，因此GraphQL适用面窄。
  - Tags: #read

- (2025-12-19) [The Architecture of "Not Bad": Decoding the Chinese Source Code of the Void](2025-12-19-the-architecture-of-not-bad-decoding-the-chinese-source-code-of-the-void.md)
  - 中文倾向以否定间接肯定（如“没错”），英语则偏好直接肯定（如“great”）。这种差异塑造了灰度思维与直接分类的认知模式，并影响社会互动与商业策略。语言不仅是表达工具，更潜在地决定了现实认知方式。
  - Tags: #read

- (2025-12-19) [AI agents are starting to eat SaaS](2025-12-19-ai-agents-are-starting-to-eat-saas.md)
  - AI代理正颠覆SaaS行业，使企业更易自建定制化工具替代通用SaaS，导致后者客户增长和收入保留率下降。高可用性、网络效应等护城河强的SaaS受影响较小，但后台类工具风险最高。SaaS市场将面临重组，企业需评估技术能力以应对变化。
  - Tags: #read

- (2025-12-19) [Introducing RSC Explorer — overreacted](2025-12-19-introducing-rsc-explorer-%E2%80%94-overreacted.md)
  - 本文介绍了开源工具RSC Explorer，它通过可视化方式帮助开发者理解React Server Components协议。该工具模拟RSC通信，展示组件序列化、异步渲染、动态组件加载及服务器动作调用等场景，旨在提供无需网络请求的教育体验。
  - Tags: #read #deepdive #frontend

- (2025-12-18) [Making our own spectrogram](2025-12-18-making-our-own-spectrogram.md)
  - 这篇文章介绍了用Rust开发音频频谱图可视化工具的全过程，包括傅里叶变换理论、分块加窗处理、多线程架构设计，以及性能优化方案。文章通过实际代码和多种音乐频谱演示，实现了实时音频分析，并讨论了工程实践中的关键权衡。
  - Tags: #read #rust #deepdive

- (2025-12-18) [CET Perceptually Uniform Colour Maps](2025-12-18-cet-perceptually-uniform-colour-maps.md)
  - CET配色方案通过感知均匀设计解决数据可视化中的对比度不均问题，包含线性、发散、彩虹等类型，适用于一般数据、参考数值及色盲友好场景，并提供了相关工具与资源。
  - Tags: #tools

- (2025-12-18) [Inside PostHog: How SSRF, a ClickHouse SQL Escaping 0day, and Default PostgreSQL Credentials Formed an RCE Chain (ZDI-25-099, ZDI-25-097, ZDI-25-096) - Mehmet Ince @mdisec](2025-12-18-inside-posthog-how-ssrf%2C-a-clickhouse-sql-escaping-0day%2C-and-default-postgresql-credentials-formed-an-rce-chain-%28zdi-25-099%2C-zdi-25-097%2C-zdi-25-096%29---mehmet-ince-%40mdisec.md)
  - 本文披露PostHog平台中存在一条组合漏殻链，利用SSRF、ClickHouse SQL注入0day与PostgreSQL默认凭证，实现远程代码执行。攻击可绕过前端验证，将Webhook重定向至内部服务并执行任意命令。漏洞已通过ZDI协调披露，凸显了系统纵深防御的多重失效。
  - Tags: #read #deepdive #security

- (2025-12-18) [What Actually Is Claude Code’s Plan Mode?](2025-12-18-what-actually-is-claude-code%E2%80%99s-plan-mode.md)
  - 本文解析了Claude的“计划模式”，指出它通过系统提示和文件系统路径管理生成Markdown计划，依赖于UI实现审批流程。作者认为这一模式核心功能可通过自定义提示模拟，但集成UX是其独特之处，不过个人更偏好灵活的自然语言编辑方式。
  - Tags: #read #llm

- (2025-12-18) [Announcing support for GROUP BY, SUM, and other aggregation queries in R2 SQL](2025-12-18-announcing-support-for-group-by%2C-sum%2C-and-other-aggregation-queries-in-r2-sql.md)
  - Cloudflare R2 SQL 新增支持的聚合查询功能包含GROUP BY、SUM等，利用Scatter-Gather和Shuffling两种分布式策略处理数据，帮助用户快速获取大数据摘要并支持报告生成和异常检测。该功能已上线，适用于R2存储的Parquet文件。
  - Tags: #read #db

- (2025-12-17) [时间+项目的双维度工作笔记法 - 少数派](2025-12-17-%E6%97%B6%E9%97%B4%2B%E9%A1%B9%E7%9B%AE%E7%9A%84%E5%8F%8C%E7%BB%B4%E5%BA%A6%E5%B7%A5%E4%BD%9C%E7%AC%94%E8%AE%B0%E6%B3%95---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 本文提出“时间+项目”双维度工作笔记法，通过日志、任务、项目、知识四要素整合，帮助职场人应对多任务与长周期项目挑战。方法强调高效记录与检索，支持快速复盘和知识复用，可借助Notion等工具实现，以提高工作效率并减轻大脑负担。
  - Tags: #read

- (2025-12-16) [How a Kernel Bug Froze My Machine: Debugging an Async-profiler Deadlock | QuestDB](2025-12-16-how-a-kernel-bug-froze-my-machine-debugging-an-async-profiler-deadlock-questdb.md)
  - 作者在使用 async-profiler 时遭遇一个由 Linux 内核 6.17 引入的 bug，导致系统死锁。该问题在于 cpu-clock 事件处理中的 hrtimer 回调陷入循环等待。解决方案是内核补丁将 hrtimer_cancel 改为非阻塞调用并引入延迟停止标志，临时规避方法是使用 -e ctimer 选项。作者通过 QEMU 和 GDB 成功调试并定位问题。
  - Tags: #read #kernel #deepdive

- (2025-12-16) [Statistics made simple](2025-12-16-statistics-made-simple.md)
  - 作者开发了轻量级网站统计工具clj-simple-stats，替代复杂方案如Google Analytics。它通过中间件简化部署，智能分类访问并优化RSS计数，提供柱状图等准确图表。具备基础筛选功能，开源可自托管。
  - Tags: #read

- (2025-12-16) [I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in 4.5 hours](2025-12-16-i-ported-justhtml-from-python-to-javascript-with-codex-cli-and-gpt-5.2-in-4.5-hours.md)
  - 作者使用GPT-5.2在4.5小时内将Python库JustHTML移植为JavaScript版本，成果包含9000行代码并通过9200项测试。项目利用AI自动编写和测试代码，费用极低，凸显了AI在代码移植中的高效性，但也引发了关于伦理、版权与生成代码质量的争议。
  - Tags: #read #llm

- (2025-12-15) [How I wrote JustHTML using coding agents - Friendly Bit](2025-12-15-how-i-wrote-justhtml-using-coding-agents---friendly-bit.md)
  - 参数验证失败：url参数中的域名"python"无法DNS解析为有效IP地址，导致400错误。
  - Tags: #read #llm #deepdive

- (2025-12-15) [JustHTML is a fascinating example of vibe engineering in action](2025-12-15-justhtml-is-a-fascinating-example-of-vibe-engineering-in-action.md)
  - Emil利用AI工具开发的JustHTML库实现了纯Python的高质量HTML解析器，展示了“氛围工程”理念：程序员专注架构设计与测试验证，AI承担编码实现，提升开发效率与代码可靠性。
  - Tags: #read #llm

- (2025-12-15) [Justified](2025-12-15-justified.md)
  - 任务运行器“just”通过.justfile定义项目命令，实现跨平台任务自动化。支持变量、平台适配等高级功能，简化开发流程，是轻量高效的标准化工具。
  - Tags: #read

- (2025-12-14) [Jubilant: Python subprocess and Go codegen](2025-12-14-jubilant-python-subprocess-and-go-codegen.md)
  - Jubilant 是利用 Python 封装 Juju CLI 的项目，通过 subprocess.run 调用 CLI 简化架构，使用代码生成确保数据模型一致，并基于 uv 和 Make 管理开发流程，体现了简洁实用的设计思路。
  - Tags: #read

- (2025-12-14) [My gift to the rustdoc team](2025-12-14-my-gift-to-the-rustdoc-team.md)
  - Arborium 是为 Rust 文档网站 docs.rs 开发的语法高亮工具，支持 96 种语言，通过 tree-sitter 实现高性能解析。文章分析了三种集成方案，推荐在 docs.rs 构建时进行后端处理以兼顾性能和安全。该项目已在 GitHub 开源，旨在提升 Rust 文档的可读性。
  - Tags: #read #deepdive

- (2025-12-14) [What happens when the coding becomes the least interesting part of the work](2025-12-14-what-happens-when-the-coding-becomes-the-least-interesting-part-of-the-work.md)
  - 编程代理将改变软件开发，编码不再是核心挑战，重点转向资深工程师的思考能力：问题分析、决策与权衡。资深工程师借助AI提升效率，行业结构或将精简，初级工程师面临替代风险。未来一年，即使AI停滞，变革仍将加速。
  - Tags: #read #llm

- (2025-12-14) [Skills vs Dynamic MCP Loadouts](2025-12-14-skills-vs-dynamic-mcp-loadouts.md)
  - 本文比较了AI工具调用中的技能系统和MCP协议，指出技能通过简短摘要和AI自适应使用现有工具，比依赖静态定义和正则匹配的MCP更灵活高效。作者基于实践经验，倾向让AI自主维护技能，避免MCP的兼容性和成本问题，认为技能系统在当前更具优势。
  - Tags: #read #llm

- (2025-12-14) [我的独立开发者书单 2025 版 - 白宦成](2025-12-14-%E6%88%91%E7%9A%84%E7%8B%AC%E7%AB%8B%E5%BC%80%E5%8F%91%E8%80%85%E4%B9%A6%E5%8D%95-2025-%E7%89%88---%E7%99%BD%E5%AE%A6%E6%88%90.md)
  - 这份2025年独立开发者书单强调务实创业，推荐七本书，涵盖财富创造、产品全流程、SEO、App开发、创业管理、小型企业运营及网站盈利，旨在帮助开发者规避错误、低成本启动并实现持续盈利。建议关注作者社交媒体获取更新。
  - Tags: #read

- (2025-12-12) [Litestream VFS](2025-12-12-litestream-vfs.md)
  - Litestream VFS 是一项功能，允许用户通过SQLite的插件接口直接查询对象存储（如S3）中的SQLite备份，而无需下载整个文件。它利用LTX格式和索引优化，仅按需加载查询所需的数据页，支持历史时间点查询和快速恢复，适用于云环境临时数据库访问和容错场景。该功能只读，写操作仍由独立进程处理。
  - Tags: #read #db

- (2025-12-11) [Useful patterns for building HTML tools](2025-12-11-useful-patterns-for-building-html-tools.md)
  - 该文介绍了HTML工具的定义和开发模式，强调单一文件结构，避免复杂框架，并使用CDN和浏览器原生功能实现轻量化开发。建议通过LLM辅助快速构建实用工具，并分享了具体实现技巧和示例。
  - Tags: #read #tips #deepdive #frontend

- (2025-12-09) [Prediction: AI will make formal verification go mainstream — Martin Kleppmann’s blog](2025-12-09-prediction-ai-will-make-formal-verification-go-mainstream-%E2%80%94-martin-kleppmann%E2%80%99s-blog.md)
  - AI将推动形式化验证从边缘技术走向主流。原本因高成本和难度仅见于研究，但AI能大幅降低验证成本，并因自动代码生成而产生验证需求。未来挑战在于定义规范和文化接受，但形式化验证有望成为软件开发标准。
  - Tags: #read

- (2025-12-09) [使用Nano Banana Pro生成整套PPT：疯狂，挑战和工作流](2025-12-09-%E4%BD%BF%E7%94%A8nano-banana-pro%E7%94%9F%E6%88%90%E6%95%B4%E5%A5%97ppt%EF%BC%9A%E7%96%AF%E7%8B%82%EF%BC%8C%E6%8C%91%E6%88%98%E5%92%8C%E5%B7%A5%E4%BD%9C%E6%B5%81.md)
  - 本文介绍了使用Nano Banana Pro生成PPT的工作流，从传统拼凑转向整体渲染，解决了风格不一致、内容不可靠等问题。通过工程化方法构建可复用的生成引擎，交付生成能力而非静态成品，实现高效、统一的幻灯片制作。
  - Tags: #read #llm #guide

- (2025-12-08) [Adding unpack syntax to RCL](2025-12-08-adding-unpack-syntax-to-rcl.md)
  - RCL v0.11.0引入解包功能，通过（列表/集合）和（字典）语法简化数据结构拼接。设计解决了推导冗长与联合运算符格式化问题，在保持简洁性的同时明确了集合与字典的语义差异，提升了代码可读性。
  - Tags: #read #language #design

- (2025-12-08) [576 - Using LLMs at Oxide / RFD / Oxide](2025-12-08-576---using-llms-at-oxide-rfd-oxide.md)
  - 文章总结了大型语言模型在阅读、编辑、写作、代码审查、调试和编程等场景下的应用，强调LLM应作为辅助工具而非替代品。关键在于平衡效益与风险，注意数据隐私、内容真实性和人类主导作用，避免过度依赖。
  - Tags: #read #llm #guide

- (2025-12-08) [EchoGram: The Hidden Vulnerability Undermining AI Guardrails](2025-12-08-echogram-the-hidden-vulnerability-undermining-ai-guardrails.md)
  - 新型攻击EchoGram可绕过AI护栏检测，通过在提示中添加少量翻转令牌序列，可误导防御模型错误放行恶意内容或产生误报。其漏洞源于公共数据训练缺陷，广泛影响主流模型。研究呼吁开发动态防御机制，减少对静态训练数据的依赖。
  - Tags: #read #llm #security

- (2025-12-08) [Pluralistic: The Reverse-Centaur’s Guide to Criticizing AI (05 Dec 2025) – Pluralistic: Daily links from Cory Doctorow](2025-12-08-pluralistic-the-reverse-centaur%E2%80%99s-guide-to-criticizing-ai-%2805-dec-2025%29-%E2%80%93-pluralistic-daily-links-from-cory-doctorow.md)
  - Cory Doctorow指出，AI热炒的背后是大型科技公司为维持股市增长制造的泡沫，而非真实创新。AI技术可能导致人类沦为机器附庸，且因统计模型本质存在局限。他反对技术取代人力的宿命论，主张通过抵制劣质AI产品和阶级合作应对危害，而非依赖版权限制。
  - Tags: #read

- (2025-12-07) [Gist of Go: Concurrency internals](2025-12-07-gist-of-go-concurrency-internals.md)
  - 文章《Go并发内部机制》核心解析了Go语言并发实现，包括goroutine调度器、GOMAXPROCS配置、并发原语及性能工具。调度器通过少量OS线程高效运行大量goroutine，自动管理并发细节。建议借助pprof、tracing等工具优化应用，鼓励实践掌握并发编程。
  - Tags: #read #go #deepdive

- (2025-12-07) [The Unexpected Effectiveness of One-Shot Decompilation with Claude](2025-12-07-the-unexpected-effectiveness-of-one-shot-decompilation-with-claude.md)
  - 文章介绍了一种利用Claude AI在无头模式下自动化反编译的方法，通过评分器、Claude、工具集和驱动脚本协同工作，大幅提升了效率。例如，在《Snowboard Kids 2》项目中，3周内取得的进展超过过去3个月。Claude表现优于其他工具，但输出代码可读性仍需人工优化。方法强调自动化减少人力，但LLM的输出和资源限制仍是挑战。
  - Tags: #read #llm #guide

- (2025-12-07) [Why speed matters](2025-12-07-why-speed-matters.md)
  - 该文章指出网页“Robot Challenge Screen”显示安全验证界面，可能要求授权或完成验证码才能访问。
  - Tags: #read

- (2025-12-06) [Writing a good CLAUDE.md](2025-12-06-writing-a-good-claude.md.md)
  - 本文介绍了文件作为代码代理初始上下文的核心作用，强调通过定义项目的目标、技术栈和工作流程来引导代理。关键优化策略包括保持指令简洁（优先普适性、控制文件长度）、拆分任务特定内容、明确工具分工，以及手工精心设计内容，以平衡信息量和上下文效率，最大化代理效能。
  - Tags: #read #llm

- (2025-12-06) [A first look at Django's new background tasks](2025-12-06-a-first-look-at-django%27s-new-background-tasks.md)
  - Django 6.0 推出内置任务框架 ，提供统一 API 标准，便于集成多种后端。支持异步任务定义与排队，但功能精简，缺少重试、编排等高级特性，适用于简单场景，复杂需求仍需 Celery 等工具。
  - Tags: #read #python

- (2025-12-06) [Thoughts on Go vs. Rust vs. Zig](2025-12-06-thoughts-on-go-vs.-rust-vs.-zig.md)
  - 这篇文章分析了Go、Rust、Zig三种语言的设计理念：Go强调简洁与协作，Rust追求性能与安全，Zig注重显式控制。选择语言应基于项目需求与价值观匹配，而非单纯比较功能。
  - Tags: #read #programming #language

- (2025-12-06) [Fizz Buzz in CSS - Susam Pal](2025-12-06-fizz-buzz-in-css---susam-pal.md)
  - 本文介绍仅用CSS实现Fizz Buzz序列的4行代码方案。通过CSS计数器、伪元素和选择器组合，在特定倍数项显示数字和替换文本。作者鼓励尝试更简洁的写法，并提供了参考链接。
  - Tags: #read #hack #frontend

- (2025-12-06) [They have to be able to talk about us without us - Anil Dash](2025-12-06-they-have-to-be-able-to-talk-about-us-without-us---anil-dash.md)
  - 文章指出有效沟通的核心是让信息简洁、有感染力，便于听众自主传播。关键原则包括立足价值观、清晰叙事、保持一致性、允许个性化表达，并强调通过情感共鸣和协作扩大影响力。
  - Tags: #read #people

- (2025-12-06) [My mental model of the AI race](2025-12-06-my-mental-model-of-the-ai-race.md)
  - 文章分析了AI领域的两个自我加速循环：平台资本主义通过用户数据优化市场匹配，编码工具通过自我迭代推动技术跃升。它们的闭环机制驱动AI公司竞争，但发展潜力受限于技术瓶颈和市场风险。
  - Tags: #read

- (2025-12-04) [Advanced network traffic interception techniques with mitmproxy – Trickster Dev](2025-12-04-advanced-network-traffic-interception-techniques-with-mitmproxy-%E2%80%93-trickster-dev.md)
  - mitmproxy 提供了反向代理、透明代理、Wireguard VPN、SOCKS5、DNS服务、上游代理及虚拟网络接口等多种模式，支持各类网络环境下的流量拦截与分析，适用于服务器监控、移动设备调试等场景。
  - Tags: #read #tips #hack #network

- (2025-12-04) [easychen/lean-side-bussiness](2025-12-04-easychen-lean-side-bussiness.md)
  - 《精益副业：程序员如何优雅地做副业》是easychen的开源项目，基于精益创业理念，为程序员提供系统化副业指导。内容包括副业价值、时间管理、知识变现和产品开发，通过案例解析独立开发与网课变现流程，社区反响活跃，适合技术从业者参考。
  - Tags: #books

- (2025-12-04) [Paged Out!](2025-12-04-paged-out%21.md)
  - 《Paged Out!》是一份免费的社区共创技术杂志，每篇文章限一页，内容涵盖编程、黑客技术、计算机软硬件等领域。所有期刊可免费下载和打印，支持用户投稿，通过邮件或RSS订阅更新，致力于以开放协作方式推广技术知识共享。
  - Tags: #book

- (2025-12-03) [“The local-first rebellion”: How Home Assistant became the most important project in your house](2025-12-03-%E2%80%9Cthe-local-first-rebellion%E2%80%9D-how-home-assistant-became-the-most-important-project-in-your-house.md)
  - Home Assistant是开源家庭自动化平台，坚持本地化设计，保障用户隐私和离线使用。支持3000多品牌设备集成，社区驱动开发，避免云服务依赖。未来致力于结合本地AI实现更自主的智能家居体验。
  - Tags: #read

- (2025-12-03) [A pragmatic guide to LLM evals for devs](2025-12-03-a-pragmatic-guide-to-llm-evals-for-devs.md)
  - 本文总结了LLM应用开发中的评估核心流程：通过错误分析系统化识别主要失败模式（如构建数据查看器、开放式与轴向编码），结合代码化测试和LLM评判员工具，实现数据驱动的持续优化，取代主观开发模式。
  - Tags: #read #llm #eval #deepdive

- (2025-12-03) [Dependency groups and uv run](2025-12-03-dependency-groups-and-uv-run.md)
  - 本文介绍了一种基于uv工具的新型Python开发模式，利用PEP 735依赖组简化项目流程。核心是使用创建库项目，通过添加dev依赖组，运行自动处理环境和测试。模式无需手动管理虚拟环境，便于协作与打包，提升开发效率。
  - Tags: #read #tips

- (2025-12-03) [Vibe Coding: Empowering and Imprisoning - Anil Dash](2025-12-03-vibe-coding-empowering-and-imprisoning---anil-dash.md)
  - 本文探讨AI辅助编程的双重影响：一方面提升效率、降低开发门槛；另一方面可能削弱劳动力价值、抑制创新并引发技术依赖。作者呼吁通过开源工具和教育引导，平衡技术便利性与社会公平，确保AI服务于广泛人群而非资本利益。
  - Tags: #read

- (2025-12-02) [How to orchestrate agents using mission control](2025-12-02-how-to-orchestrate-agents-using-mission-control.md)
  - GitHub Copilot的Mission Control功能通过统一界面管理多个AI代理，实现并行工作流。关键点包括：编写清晰提示、自定义代理以确保一致性、主动监控并干预问题、高效审查PR。其优势在于提升效率，实现批量处理和并行工作。
  - Tags: #read #llm #guide

- (2025-12-01) [CS146S: The Modern Software Developer - Stanford University](2025-12-01-cs146s-the-modern-software-developer---stanford-university.md)
  - 斯坦福大学CS146S《现代软件开发者》课程（2025秋）教授如何利用AI工具与软件工程结合，提升开发效率。内容涵盖LLM应用、自动化测试、智能体编程等10周主题，强调实践项目与行业案例，适合有编程基础的学生参与。
  - Tags: #read #guide

- (2025-12-01) [Migrating Dillo from GitHub](2025-12-01-migrating-dillo-from-github.md)
  - Dillo项目从GitHub迁移至自托管服务器以规避平台风险，包括兼容性差、单点故障和过度依赖JavaScript等问题。新方案使用cgit和轻量级工具，并设置多镜像保障数据安全，支持离线开发。迁移后GitHub仓库将归档，项目通过捐赠维持运行。
  - Tags: #read
