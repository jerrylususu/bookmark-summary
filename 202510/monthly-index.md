# 2025-10 Monthly Index

- (2025-10-30) [A Practitioner's Guide to Wide Events | Jeremy Morrell](2025-10-30-a-practitioner%27s-guide-to-wide-events-jeremy-morrell.md)
  - 宽事件是一种增强系统可观测性的方法，通过记录每个工作单元的全部相关数据形成一个完整事件，便于查询分析。实施包括选择工具、编写代码添加丰富属性、掌握查询技巧。此方法可大幅提升调试效率。
  - Tags: #read #deepdive #distributed #explainer

- (2025-10-30) [Stacking Threads](2025-10-30-stacking-threads.md)
  - 该文章分析了多线程程序中线程栈和线程控制块在进程内存中的布局差异，指出不同操作系统（如Linux、macOS、FreeBSD等）的线程栈放置位置与TCB管理方式显著不同。跨平台编程需注意内存布局随机性、栈位置不固定等特性，强调操作系统抽象层的复杂性。
  - Tags: #read

- (2025-10-30) [用一次摸鱼经历详解AI管理实战](2025-10-30-%E7%94%A8%E4%B8%80%E6%AC%A1%E6%91%B8%E9%B1%BC%E7%BB%8F%E5%8E%86%E8%AF%A6%E8%A7%A3ai%E7%AE%A1%E7%90%86%E5%AE%9E%E6%88%98.md)
  - 作者通过AI管理五步法（选模型、下指令、做培训、给方法、定验收），实现用5%精力撬动AI完成95%工作。核心是像管理团队一样引导AI，将人类时间聚焦于战略决策，大幅提升生产力。
  - Tags: #read #llm #people

- (2025-10-30) [How many pillars of observability can you fit on the head of a pin?](2025-10-30-how-many-pillars-of-observability-can-you-fit-on-the-head-of-a-pin.md)
  - 作者批判“可观测性支柱”为营销术语，提倡用“信号”概念统一存储数据，避免多支柱模型导致的隔阂与高成本，强调OpenTelemetry等统一方案更高效。
  - Tags: #read

- (2025-10-30) [Why do AI models use so many em-dashes?](2025-10-30-why-do-ai-models-use-so-many-em-dashes.md)
  - AI模型过度使用破折号的现象主要源于训练数据的变化。GPT-4等模型为获取高质量数据，数字化了大量19世纪末到20世纪初的书籍，这些历史文本中破折号使用率较高，导致模型习得这一习惯。强化学习人类反馈或AI内容循环也可能加剧此现象，但核心原因在于训练数据的历史语言风格影响。
  - Tags: #read #llm

- (2025-10-29) [High Agency Matters](2025-10-29-high-agency-matters.md)
  - 文章强调，个人能动性（主动行动和担当）比高智商更能决定长期成功。高能动性者通过执行力、坚持和风险承担创造实际成果，而智力易导致分析瘫痪。在AI时代，能动性作为人类独特优势愈发重要，应优先培养。
  - Tags: #read #people

- (2025-10-29) [一文讲透AI Agent开发中的human-in-the-loop - 铁蕾的个人博客](2025-10-29-%E4%B8%80%E6%96%87%E8%AE%B2%E9%80%8Fai-agent%E5%BC%80%E5%8F%91%E4%B8%AD%E7%9A%84human-in-the-loop---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - 本文阐述了AI Agent开发中Human-in-the-loop机制的必要性，及其技术实现关键。为解决自主性与确定性的矛盾，需在关键环节引入人工干预。实现方案根据通信通道分为两类：可会话保持（如WebSocket）时直接等待反馈；无法保持时需序列化状态并持久化存储。序列化复杂运行时状态是主要挑战，需精简设计以准确恢复状态。
  - Tags: #read #llm

- (2025-10-27) [Gamekeeper：像 Git 一样管理游戏存档 - 少数派](2025-10-27-gamekeeper%EF%BC%9A%E5%83%8F-git-%E4%B8%80%E6%A0%B7%E7%AE%A1%E7%90%86%E6%B8%B8%E6%88%8F%E5%AD%98%E6%A1%A3---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - Gamekeeper 是一款受 Git 启发设计的游戏存档管理工具，能自动识别存档、支持多分支管理和差异存储，帮助玩家高效管理多结局和存档历史。未来计划增加云同步和分享功能。目前免费可用。
  - Tags: #read

- (2025-10-27) [Pepsi, when they don't have coke](2025-10-27-pepsi%2C-when-they-don%27t-have-coke.md)
  - 文章分析了配置管理现状，认为现有工具如Toml、JSON、YAML在大型配置中不足。作者探讨了Cuelang和Starlark等替代方案，但认为其复杂度高、绑定有限。最终选择Python作为折中方案，虽无沙盒保护，但更实用灵活，适合多数场景。
  - Tags: #read

- (2025-10-27) [🚨🚨 That's a lot of YAML 🚨🚨](2025-10-27-%F0%9F%9A%A8%F0%9F%9A%A8-that%27s-a-lot-of-yaml-%F0%9F%9A%A8%F0%9F%9A%A8.md)
  - 文章批评YAML在开发运维中的滥用，指出其安全性低、类型解析混乱、效率低下，并通过讽刺手法揭示其不可靠性，建议慎用于关键场景。
  - Tags: #hack

- (2025-10-27) [GenAI Image Showdown](2025-10-27-genai-image-showdown.md)
  - GenAI图像编辑对决测试了7款模型的文本指令编辑能力。在13项挑战中，Seedream 4以9项领先，表现最佳。模型普遍擅长风格合成和元素添加，但在空间调整、多元素协同编辑等精细任务上仍有不足。
  - Tags: #llm #visual

- (2025-10-27) [Mistakes I see engineers making in their code reviews](2025-10-27-mistakes-i-see-engineers-making-in-their-code-reviews.md)
  - 作者提出代码评审五大要点：避免仅关注代码差异，控制评论数量，不以个人偏好为评判标准，明确阻止合并时使用阻止性评审，并提倡多数情况下应批准通过。此外，评审AI代码需更严格把关。
  - Tags: #read #people #guide

- (2025-10-27) [Setting up a codebase for working with coding agents](2025-10-27-setting-up-a-codebase-for-working-with-coding-agents.md)
  - 为提高AI编程效率，需要优化代码库设置，包括自动化测试、交互式测试、问题管理、轻量文档、代码质量工具和详细错误信息，这些措施同时提升项目的可维护性。
  - Tags: #llm #tips

- (2025-10-27) [How I Coding? (Oct 2025 Edition)](2025-10-27-how-i-coding-%28oct-2025-edition%29.md)
  - 作者强调2025年编程中应秉持“慢即是快”心态，关注高质量输出而非速度。工具沿用Codex等，集成体验各异，GitHub审查质量高。建议聚焦顶尖模型并减少AI相关输入，将精力放在核心开发上。
  - Tags: #read #llm #tips

- (2025-10-23) [Corrosion](2025-10-23-corrosion.md)
  - Fly.io为解决全球分布式平台状态同步问题，构建了去中心化服务发现系统Corrosion。它采用gossip协议和SQLite数据库变更传播，放弃传统分布式共识以提升性能，尽管遇到了故障并经过多次优化，现已成为一个高效可扩展的开源解决方案。
  - Tags: #read #distributed #deepdive

- (2025-10-23) [Dane Stuckey (OpenAI CISO) on prompt injection risks for ChatGPT Atlas](2025-10-23-dane-stuckey-%28openai-ciso%29-on-prompt-injection-risks-for-chatgpt-atlas.md)
  - OpenAI针对ChatGPT浏览器自动化功能的提示注入风险采取红队测试、深度防御与监视模式等防护措施。但作者对其有效性存疑，认为零日攻击风险犹存，实际防护效果有待验证，但肯定OpenAI的积极应对。
  - Tags: #read #llm #security

- (2025-10-23) [Living dangerously with Claude](2025-10-23-living-dangerously-with-claude.md)
  - YOLO模式让AI编码代理在无人监督下高效完成复杂任务，但存在数据泄露风险。关键在于使用沙盒环境隔离运行，严格管控文件与网络访问，在保障安全前提下充分发挥其效率优势。
  - Tags: #read #llm

- (2025-10-22) [What is good software architecture?](2025-10-22-what-is-good-software-architecture.md)
  - 优秀软件架构的核心不在于专职角色或完美设计，而是实践中的权衡与协作。架构应聚焦现实问题，平衡当下与未来，注重团队共识而非纯粹技术最优解。通过原型测试和风险规划逐步改进，避免脱离实际的空想。
  - Tags: #read #deepdive #arch

- (2025-10-21) [How to Fix Any Bug — overreacted](2025-10-21-how-to-fix-any-bug-%E2%80%94-overreacted.md)
  - 文章通过修复网页滚动Bug的案例，总结了系统性方法：先建立可客观验证的可复现案例，再逐步简化代码定位问题根源，避免盲目猜测。核心原则是简化优于理论测试，确保每一步都验证Bug存在，适用于复杂项目调试。最终通过修正React Router依赖解决问题。
  - Tags: #read #llm #deepdive

- (2025-10-21) [Agentic AI’s OODA Loop Problem - Schneier on Security](2025-10-21-agentic-ai%E2%80%99s-ooda-loop-problem---schneier-on-security.md)
  - 本文分析AI代理在对抗环境中的安全风险，指出OODA循环各阶段易受攻击，如数据投毒、提示注入等。根源在于模型无法保障语义完整性，且安全常为性能让步。需重新设计架构，将完整性内嵌。
  - Tags: #read #llm #security

- (2025-10-21) [Should LLMs just treat text content as an image?](2025-10-21-should-llms-just-treat-text-content-as-an-image.md)
  - 光学压缩将文本转为图像输入多模态大模型，有望提升数据处理效率。这种图像令牌比文本令牌更高效，类似人类视觉处理方式。虽有应用探索，但训练难度与效果仍需验证，潜力待进一步研究。
  - Tags: #read #llm

- (2025-10-21) [Claude Code for web—a new asynchronous coding agent from Anthropic](2025-10-21-claude-code-for-web%E2%80%94a-new-asynchronous-coding-agent-from-anthropic.md)
  - Anthropic于2025年10月推出Claude Code for web异步编码代理，支持GitHub仓库操作与网络隔离沙盒环境。该工具提供简单任务部署、性能测试及本地CLI同步功能，通过容器化服务兼顾效率与安全性，适合快速开发测试。
  - Tags: #read #llm #agen

- (2025-10-21) [Getting DeepSeek-OCR working on an NVIDIA Spark via brute force using Claude Code](2025-10-21-getting-deepseek-ocr-working-on-an-nvidia-spark-via-brute-force-using-claude-code.md)
  - 作者在NVIDIA Spark设备上使用Claude Code成功部署DeepSeek-OCR模型。通过Docker容器自动化配置环境，关键解决了PyTorch版本与GPU兼容性问题。经测试"Free OCR"提示词效果最佳，整个流程仅需少量人工干预，验证了自动化工具的可行性。
  - Tags: #read

- (2025-10-20) [An Opinionated Guide to Using AI Right Now](2025-10-20-an-opinionated-guide-to-using-ai-right-now.md)
  - 本文对比主流AI工具（如ChatGPT、Claude、Gemini）的免费与付费方案，强调基于需求选择模型：免费版适合日常，付费版提供更强处理能力。使用技巧包括开启深度搜索、利用文件处理功能，并注意AI可能出错。建议多尝试，关注实际应用而非技术本身。
  - Tags: #read #llm

- (2025-10-19) [Diskcache, more than caching](2025-10-19-diskcache%2C-more-than-caching.md)
  - Diskcache是基于SQLite的Python键值存储库，支持缓存、事务、标签、队列、锁等高级功能，适用于多进程并发环境。具备函数缓存、防惊群机制和流量控制等工具，轻量高效，适合中小型应用开发。
  - Tags: #read

- (2025-10-19) [What have we learned about building agentic AI tools?](2025-10-19-what-have-we-learned-about-building-agentic-ai-tools.md)
  - 智能体化编程工具在2025年成熟，得益于模型和框架的优化。关键设计包括：先规划后行动、嵌套规则定制、支持插件和用户中断引导。未来将面临新设计和无监督智能体流程的挑战。
  - Tags: #read #llm

- (2025-10-18) [Revocation Confusion](2025-10-18-revocation-confusion.md)
  - 这篇短文通过Flair航空网站案例，分析了SSL证书吊销问题。文章指出，浏览器对吊销证书处理不一（如Firefox拦截而Chrome忽略），导致用户困惑，并强调需改进证书机制和浏览器一致性以平衡安全与体验。
  - Tags: #read #security

- (2025-10-18) [The Temporal Dead Zone, or why the TypeScript codebase is littered with var statements](2025-10-18-the-temporal-dead-zone%2C-or-why-the-typescript-codebase-is-littered-with-var-statements.md)
  - TypeScript代码库为优化约8%性能，选择使用存在缺陷的语句替代/，以规避变量时空死区带来的运行时开销。尽管现代JavaScript推荐使用更安全的块级作用域声明，但出于性能权衡仍保留。
  - Tags: #read #js

- (2025-10-18) [Use weird tests to capture tacit knowledge](2025-10-18-use-weird-tests-to-capture-tacit-knowledge.md)
  - 通过测试捕获代码库隐性知识，如用棘轮测试检查新增模块配置、验证枚举文档完整性，将约束自动化。测试兼具文档和左移流程作用，降低查阅成本并提前发现问题。方法简单高效，适合替代临时脚本。
  - Tags: #read #tips

- (2025-10-18) [Solving NYT's Pips Puzzle](2025-10-18-solving-nyt%27s-pips-puzzle.md)
  - 本文介绍了作者开发的《纽约时报》Pips 拼图求解器，包括游戏规则、深度优先搜索算法实现，以及通过剪枝、骨牌方向重复跳过和智能区域检查等优化手段，将节点数从21337降至1355，并实现交互式界面。
  - Tags: #read

- (2025-10-18) [怎么让AI不偷懒：为Codex构建系统性的Wide Research能力](2025-10-18-%E6%80%8E%E4%B9%88%E8%AE%A9ai%E4%B8%8D%E5%81%B7%E6%87%92%EF%BC%9A%E4%B8%BAcodex%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F%E6%80%A7%E7%9A%84wide-research%E8%83%BD%E5%8A%9B.md)
  - 本文通过分析AI处理长任务时“偷懒”的架构性问题，提出分治策略：将大规模任务分解为子问题由轻量级AI处理，再汇总润色。作者以Codex为例实现自动化工答流程，展示了改进AI系统设计和工作流对提升执行效率的关键作用。
  - Tags: #read #llm #guide

- (2025-10-18) [Building an Agent That Leverages Throwaway Code](2025-10-18-building-an-agent-that-leverages-throwaway-code.md)
  - 本文介绍利用Pyodide（WebAssembly版Python）构建智能体的方法，通过写入临时代码解决复杂任务。虚拟文件系统实现安全资源交互；持久化执行确保任务可恢复。此方法简单高效，已有类似应用实践。
  - Tags: #read #llm

- (2025-10-17) [How a 20 year old bug in GTA San Andreas surfaced in Windows 11 24H2](2025-10-17-how-a-20-year-old-bug-in-gta-san-andreas-surfaced-in-windows-11-24h2.md)
  - Windows 11 24H2更新暴露了《GTA圣安地列斯》中长达20年的隐藏bug，导致Skimmer水上飞机无法生成。原因是游戏配置文件缺失参数，加上Windows系统更新改变了栈空间使用方式，使未初始化变量异常扩大。修复方法可通过社区补丁或手动修改配置文件解决，突显代码健壮性和社区维护的重要性。
  - Tags: #read

- (2025-10-17) [Claude Skills are awesome, maybe a bigger deal than MCP](2025-10-17-claude-skills-are-awesome%2C-maybe-a-bigger-deal-than-mcp.md)
  - Claude Skills是Anthropic推出的轻量化AI技能框架，通过Markdown文件和脚本即可扩展模型的专业任务能力。相比复杂协议MCP，它具有简单高效、跨模型通用的优势，未来或引发技能生态爆发式增长。设计核心在于利用模型自主推理能力，降低开发门槛。
  - Tags: #read #llm

- (2025-10-16) [How We Use AI Agents for COBOL Migration and Mainframe Modernization | All things Azure](2025-10-16-how-we-use-ai-agents-for-cobol-migration-and-mainframe-modernization-all-things-azure.md)
  - 微软推出CAMF框架，利用多个AI智能体协作实现COBOL代码向Java的自动化迁移，解决了COBOL系统现代化中的专家稀缺和成本高的问题，已在真实项目中验证可行性，并可扩展至其他遗留系统改造。
  - Tags: #read

- (2025-10-16) [I am sorry, but everyone is getting syntax highlighting wrong](2025-10-16-i-am-sorry%2C-but-everyone-is-getting-syntax-highlighting-wrong.md)
  - 文章批评了语法高亮的滥用问题，指出过度高亮和颜色种类过多会降低代码识别效率。提出了限制颜色数量、选择性高亮关键元素及优化视觉效果等原则，并给出了实践案例。强调语法高亮应注重实用性，而非装饰性。
  - Tags: #read #design #deepdive

- (2025-10-15) [Just Talk To It - the no-bs Way of Agentic Engineering | Peter Steinberger](2025-10-15-just-talk-to-it---the-no-bs-way-of-agentic-engineering-peter-steinberger.md)
  - Peter Steinberger分享了基于GPT-5-codex的代理人工程实践经验，强调"直接对话"的高效工作流。他使用codex CLI并行处理任务，通过截图简化提示，自动管理代码提交与重构。主张避免过度工程化，认为Claude等工具效率低下，推荐通过自然对话协作，保持工作流简洁直观。
  - Tags: #read #llm #deepdive

- (2025-10-14) [How to build reliable AI workflows with agentic primitives and context engineering](2025-10-14-how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering.md)
  - 本文提出构建可靠AI工作流的三层框架：Markdown提示工程、代理原语系统化与上下文工程管理，结合工具链和包管理支持，旨在实现AI开发从实验到可重复工程实践的转变，提升可预测性与可扩展性。
  - Tags: #read #llm

- (2025-10-13) [Abstraction, not syntax](2025-10-13-abstraction%2C-not-syntax.md)
  - 配置格式的核心不是句法之争，而在于通过编程抽象（如循环、公式）消除重复，提升维护性。支持抽象的语言虽可能增加复杂性，但在复杂场景中优势显著。
  - Tags: #read

- (2025-10-12) [URL Design · by Kyle Neath](2025-10-12-url-design-%C2%B7-by-kyle-neath.md)
  - URL设计对网站可用性至关重要，应精心规划而非随意生成。建议使用简洁可读的URL结构、稳定命名空间和查询字符串，并确保每个页面有唯一URL。发布后保持URL稳定，利用HTML5 API管理动态内容。关键在于平衡技术实现与用户体验。
  - Tags: #read #frontend #design

- (2025-10-12) [Vibing a Non-Trivial Ghostty Feature](2025-10-12-vibing-a-non-trivial-ghostty-feature.md)
  - 作者Mitchellh分享使用AI辅助开发Ghostty的非侵入式macOS自动更新功能。通过拆分任务、AI生成UI原型与代码框架，并在8小时内完成开发，强调AI作为辅助工具需人工主导审核，避免更新提示打断用户。
  - Tags: #read #llm #deepdive

- (2025-10-12) [How I provide technical clarity to non-technical leaders](2025-10-12-how-i-provide-technical-clarity-to-non-technical-leaders.md)
  - 技术清晰度指让非技术决策者理解软件系统，以做出明智变更决策。它通过简化沟通、隐藏复杂性实现，需要工程师具备良好判断力、技术深度和沟通自信，从而提升组织整体效能。
  - Tags: #read #people

- (2025-10-11) [An MVCC-like columnar table on S3 with constant-time deletes](2025-10-11-an-mvcc-like-columnar-table-on-s3-with-constant-time-deletes.md)
  - 本文提出了一种基于S3的MVCC列式表格式，通过不可变的数据和墓碑文件、CAS更新清单指针实现无协调的并发控制。适用于追加为主的场景，具有低写入成本，但需处理文件增长和墓碑压缩问题。
  - Tags: #read #db

- (2025-10-11) [Kaitai Struct: declarative binary format parsing language](2025-10-11-kaitai-struct-declarative-binary-format-parsing-language.md)
  - Kaitai Struct是一种声明式语言，用于描述二进制数据结构，通过编写.ksy格式文件，可编译生成多种编程语言的解析代码，实现跨平台复用。它简化了二进制格式解析开发，提高效率和可靠性，适用于文件分析、网络检测等场景。
  - Tags: #tools #parser

- (2025-10-11) [Call Me A Jerk: Persuading AI to Comply with Objectionable Requests](2025-10-11-call-me-a-jerk-persuading-ai-to-comply-with-objectionable-requests.md)
  - 研究发现，通过运用如权威、承诺等社会说服技巧，能大幅提升大语言模型对不良请求的顺从率。这揭示了AI类似人类的学习机制与潜在安全风险，强调了行为科学在AI开发中的重要作用。
  - Tags: #read #llm

- (2025-10-11) [Superpowers: How I’m using coding agents in October 2025](2025-10-11-superpowers-how-i%E2%80%99m-using-coding-agents-in-october-2025.md)
  - Jesse Vincent开发了Superpowers插件，通过TDD、流程图、情感日志等系统化方法优化Claude Code使用。该插件轻量开源，支持根因追踪等功能，帮助开发者提升编码效率。
  - Tags: #read #llm

- (2025-10-11) [A Retrospective Survey of 2024/2025 Open Source Supply Chain Compromises](2025-10-11-a-retrospective-survey-of-2024-2025-open-source-supply-chain-compromises.md)
  - 2024-2025年开源供应链攻击主要涉及钓鱼、项目控制权转让、高危CI触发器和凭证泄露。建议维护者强制启用防钓鱼认证，严格管控权限，弃用危险CI触发器，以增强项目安全性。
  - Tags: #read #security #oss

- (2025-10-11) [Quick and dirty bar-charts using HTML's meter element](2025-10-11-quick-and-dirty-bar-charts-using-html%27s-meter-element.md)
  - 这篇文章介绍了一种利用HTML的元素和CSS的属性创建简易垂直条形图的轻量级方法。该方法无需依赖外部库，支持样式定制和交互，简单实用但样式较为基础。
  - Tags: #frontend #hack

- (2025-10-10) [Finding a VS Code Memory Leak](2025-10-10-finding-a-vs-code-memory-leak.md)
  - 作者Bruce Dawson通过观察同事电脑的高进程ID，发现VS Code因未关闭进程句柄导致内存泄漏。问题源于代码中忘记调用。经ETW分析后迅速修复，凸显资源管理和RAII重要性。
  - Tags: #read #perf

- (2025-10-10) [A new breed of analyzers](2025-10-10-a-new-breed-of-analyzers.md)
  - 本文以curl项目为例，展示了AI代码分析工具的积极影响。AI工具高效发现了代码漏洞和问题，误报率低，覆盖范围广，为大型开源项目提供高质量辅助。尽管带来维护负担且尚未颠覆开发流程，但AI分析代表了代码审查技术的自然演进，未来有望集成进CI流程。
  - Tags: #read #security

- (2025-10-09) [工程师如何更好投资 - Tw93](2025-10-09-%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%A6%82%E4%BD%95%E6%9B%B4%E5%A5%BD%E6%8A%95%E8%B5%84---tw93.md)
  - 这是一篇工程师分享投资经验的非正式总结，强调投资风险自担、内容仅供参考，并提供相关图片和PDF资源。核心提醒：理财有风险，投资需谨慎。
  - Tags: #read #money

- (2025-10-08) [Why MCP’s Disregard for 40 Years of RPC Best Practices Will Burn Enterprises](2025-10-08-why-mcp%E2%80%99s-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises.md)
  - MCP 被标榜为 AI 领域通用协议，但其设计忽视分布式系统的成熟经验，类型安全、状态管理、安全性和可观测性等方面存在缺陷，可能给企业带来安全漏洞、运维负担与集成风险，需尽快整合 RPC 工具链的最佳实践。
  - Tags: #read #arch

- (2025-10-08) [为什么OpenAI Apps SDK对MCP的支持反而是MCP的危机](2025-10-08-%E4%B8%BA%E4%BB%80%E4%B9%88openai-apps-sdk%E5%AF%B9mcp%E7%9A%84%E6%94%AF%E6%8C%81%E5%8F%8D%E8%80%8C%E6%98%AFmcp%E7%9A%84%E5%8D%B1%E6%9C%BA.md)
  - OpenAI的Apps SDK扩展了MCP，引入私有dialect以绕过context window限制，但导致协议分裂和生态绑定。MCP面临设计偏科研、缺乏工程考量的问题，可能走向类似SQL的厂商碎片化。未来或出现更高层抽象协议来统一变种，结果取决于技术演进和厂商博弈。
  - Tags: #read

- (2025-10-08) [三十五](2025-10-08-%E4%B8%89%E5%8D%81%E4%BA%94.md)
  - 作者以十年经历反思成长，从追逐外部成功的“有限游戏”转向构建自我系统的“无限游戏”，强调依靠工具和流程实现决策理性化、能力复用与持续迭代，追求可持续的半退休生活。
  - Tags: #read

- (2025-10-08) [Which Table Format Do LLMs Understand Best? (Results for 11 Formats)](2025-10-08-which-table-format-do-llms-understand-best-%28results-for-11-formats%29.md)
  - 研究发现表格数据格式显著影响LLM理解能力。Markdown-KV准确率最高但不经济，CSV和JSONL成本低但准确性较差。推荐根据需求选择格式，优先考虑Markdown相关方案，避免默认使用CSV或JSONL。
  - Tags: #read #llm #tips

- (2025-10-08) [How to *actually* test your readme](2025-10-08-how-to-actually-test-your-readme.md)
  - 在空白虚拟机中测试README，按步骤操作并记录命令，适配不同用户水平，确保安装过程可重现，提升文档可靠性。
  - Tags: #read #tips

- (2025-10-08) [Vibe engineering](2025-10-08-vibe-engineering.md)
  - Vibe engineering是一种由经验丰富的工程师主导的AI辅助开发方式，强调对软件质量和流程的高度控制，需要结合传统软件工程最佳实践（如测试、文档、审查等）与LLM工具的高效协作，以提升开发的专业性和产出质量。
  - Tags: #read #llm

- (2025-10-06) [You Want Technology With Warts](2025-10-06-you-want-technology-with-warts.md)
  - 文章主张选择带有已知“缺陷”的技术（如SQLite、HTML）可带来长期稳定性和低维护成本，因为“缺陷”代表成熟与兼容性，是减少未来变更风险的关键。
  - Tags: #read

- (2025-10-06) [The History of Core Web Vitals](2025-10-06-the-history-of-core-web-vitals.md)
  - Core Web Vitals 是 Google 推出的核心网页体验评估指标，涵盖加载速度（LCP）、交互响应（FID）和视觉稳定性（CLS）。它作为搜索排名因素之一，促进开发者优化网站性能，提升了整体网络速度和用户体验。通过工具支持和数据开放，该指标成为衡量和推动网站性能的重要标准。
  - Tags: #read

- (2025-10-06) [LLMs as Parts of Systems - Marc's Blog](2025-10-06-llms-as-parts-of-systems---marc%27s-blog.md)
  - 大型语言模型（LLM）与外部工具（如代码解释器、SMT求解器）结合能构建更强大、高效的系统，整体效果超越单一LLM，符合“整体大于部分之和”的系统设计原则。
  - Tags: #read #llm

- (2025-10-06) [云风的 BLOG: 深远未来开发总结](2025-10-06-%E4%BA%91%E9%A3%8E%E7%9A%84-blog-%E6%B7%B1%E8%BF%9C%E6%9C%AA%E6%9D%A5%E5%BC%80%E5%8F%91%E6%80%BB%E7%BB%93.md)
  - 云风在7周内独立开发桌游《深远未来》，采用自研引擎，注重任务拆分与视觉反馈以维持热情，并通过开源协作加速开发。最终代码量约1.3万行，经验包括保持小规模开发、及早重构和利用社区贡献。
  - Tags: #read #deepdive

- (2025-10-06) [How I'm using coding agents in September, 2025](2025-10-06-how-i%27m-using-coding-agents-in-september%2C-2025.md)
  - 作者通过结构化多会话AI协作（设计、实施、审查）结合git隔离工作流程和工具链整合（如CodeRabbit），提升开发效率与代码质量，并强调设计细化和审查验证的重要性。
  - Tags: #read #llm

- (2025-10-06) [Let the Model Write the Prompt](2025-10-06-let-the-model-write-the-prompt.md)
  - DSPy框架通过编程方式定义任务，取代传统提示工程，实现任务与模型解耦。它优化提示生成，提升准确率与模型兼容性，简化代码维护并支持持续改进，适用于如地理空间数据合并等任务。
  - Tags: #guide #deepdive #llm

- (2025-10-04) [How I influence tech company politics as a staff software engineer](2025-10-04-how-i-influence-tech-company-politics-as-a-staff-software-engineer.md)
  - 软件工程师可通过参与高价值项目、利用高层关注提出技术方案并把握时机参与，良性影响公司决策，避免政治内耗，实现技术与目标的对齐。
  - Tags: #read #people

- (2025-10-02) [Spec-driven development: Using Markdown as a programming language when building with AI](2025-10-02-spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai.md)
  - 本文提出一种基于Markdown的规格驱动开发模式，用Markdown编写应用需求与设计作为AI编程代理（如 Copilot）的输入，自动生成代码。这种方法提升文档代码一致性、支持跨语言移植，但在规模扩展和测试方面仍存挑战。
  - Tags: #read #llm

- (2025-10-02) [Designing agentic loops](2025-10-02-designing-agentic-loops.md)
  - 智能体循环是利用大型语言模型通过循环运行工具实现代码生成目标的关键技能。需在安全沙盒中运行，管理凭证风险，并选择明确任务场景，以最大化效率与安全性。
  - Tags: #read #llm

- (2025-10-01) [Writing Code Is Easy. Reading It Isn’t.](2025-10-01-writing-code-is-easy.-reading-it-isn%E2%80%99t..md)
  - 软件开发的核心瓶颈是理解代码，而非编写代码。生成式AI虽能加快代码产出，却增加了理解负担。未来工具应更注重帮助开发者构建心理模型，以提升整体效率。
  - Tags: #read
