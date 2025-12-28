# 2025-06 Monthly Index

- (2025-06-30) [How to Fix Your Context](2025-06-30-how-to-fix-your-context.md)
  - 该文提出优化语言模型上下文管理的六种策略：1.增强检索生成（精准添加参考信息）；2.工具组合（动态匹配最优工具集）；3.上下文隔离（拆分独立任务线程）；4.修剪冗余内容；5.压缩长上下文为摘要；6.将信息外置存储。核心强调主动管理上下文信息，平衡长上下文的优势与风险，通过结构化编程提升效率，根据任务需求选择优化方向。
  - Tags: #read #llm

- (2025-06-30) [How Long Contexts Fail](2025-06-30-how-long-contexts-fail.md)
  - 这篇文章指出，尽管长上下文窗口被认为能提升LLM效能，但存在四大失效风险：1.错误信息积累导致策略偏差；2.过长历史数据干扰新策略生成；3.冗余工具调用引发错误；4.矛盾信息引发推理冲突。这些风险对智能体应用影响显著，需通过动态管理技术优化上下文结构以保障稳定。
  - Tags: #read #llm

- (2025-06-30) [Linguistic Relativity and the Tyranny of the Compiler | Ingrid's Space](2025-06-30-linguistic-relativity-and-the-tyranny-of-the-compiler-ingrid%27s-space.md)
  - 文章指出编程语言对思维有约束力，虽不如自然语言能灵活演变。编程语言的固定语法和编译器限制程序员表达方式，例如LISP的宏系统虽赋予灵活性但牺牲标准化导致兼容性问题。作者建议教学应避免使用如Java的强范式语言，转而采用可扩展语言（如Scheme/Lua），以减少语法对抽象思维的束缚，并需注意工业语言需求与教学工具的本质区别。
  - Tags: #read

- (2025-06-30) [Why Decentralised Applications Don’t Work | Ingrid's Space](2025-06-30-why-decentralised-applications-don%E2%80%99t-work-ingrid%27s-space.md)
  - "去中心化应用（如区块链、Git等）普及受阻的核心原因是利益动机失调。尽管技术本身去中心化，但主流企业通过控制关键节点、市场推广及制定标准等方式挤压其生存空间，导致技术被异化或路径依赖。作者指出单纯的技术改良无法解决问题，必须通过政治手段调整利益机制，建立符合数字时代的系统性法规，以平衡资本与公共利益。"（99字）
  - Tags: #read

- (2025-06-30) [Agentic Coding: The Future of Software Development with Agents](2025-06-30-agentic-coding-the-future-of-software-development-with-agents.md)
  - Armin Ronacher分享了Claude Code代理编码实践，通过自动化任务（调试CI、浏览器交互）提升效率。方法包括：减少MCP工具依赖、整合多源日志到统一系统、分担任务以突破上下文限制，以及设计明确错误提示。集成Playwright和GitHub CLI实现自动化操作，建议在Docker中启用安全选项并结合Gemini CLI优化执行。
  - Tags: #read #llm #agent #video

- (2025-06-30) [Tip: Use keyword-only arguments in Python dataclasses – ChipLog — Christian Hammond](2025-06-30-tip-use-keyword-only-arguments-in-python-dataclasses-%E2%80%93-chiplog-%E2%80%94-christian-hammond.md)
  - Python数据类通过设置`kw_only=True`强制使用关键字参数，提升可维护性。该参数使生成的`__init__()`含`*`，所有参数需显式指定，避免字段排序变动引发错误。同时允许子类自由添加必要字段，不受父类默认值顺序限制，推荐库开发者使用以确保扩展性。需Python3.10+支持，旧版本需动态设置装饰器参数但子类仍受限制，建议手动添加默认值。
  - Tags: #read #tips

- (2025-06-29) [Prompting vs JSON Mode vs Function Calling vs Constrained Generation vs SAP](2025-06-29-prompting-vs-json-mode-vs-function-calling-vs-constrained-generation-vs-sap.md)
  - 本文介绍了从大型语言模型（LLM）提取结构化数据的九大技术，涵盖Prompt优化、模型约束及解析器方法，并提出新方案Schema-Aligned Parsing（SAP）。SAP通过错误纠正与模式驱动解析，在多模型测试中实现90%+准确率（如Claude-3达94.4%），显著优于传统JSON模式或函数调用方式。其优势包括自动修复语法逻辑错误、兼容复杂结构，并支持多语言开发。研究建议结合SAP与函数调用以进一步提升效能。
  - Tags: #read #llm

- (2025-06-29) [to-userscript/docs/architecture.md at main · Explosion-Scratch/to-userscript](2025-06-29-to-userscript-docs-architecture.md-at-main-%C2%B7-explosion-scratch-to-userscript.md)
  - to-userscript通过环境模拟技术（Proxy/定制存储）、消息总线及资源内联等方法，将浏览器扩展自动转换为无依赖的用户脚本，支持跨浏览器兼容性并最小化原代码修改。其采用多语言支持及API补丁机制，解决作用域、通信和资源嵌入问题，实现浏览器扩展到用户脚本的自动转换方案。
  - Tags: #read #hack #tools

- (2025-06-29) [The best open source project for someone might not be yours, and that's OK](2025-06-29-the-best-open-source-project-for-someone-might-not-be-yours%2C-and-that%27s-ok.md)
  - 作者主张开源项目维护者应以用户需求为先，无需强制用户选用自家工具。其开发的ack主动与竞品对比，帮助用户择优。认为技术生态应共享成长，尊重用户自主选择，并推动社区健康发展。技术进步为目标，允许工具迭代更新，最终提升用户满意度。（99字）
  - Tags: #read

- (2025-06-29) [初入投资容易犯的错误](2025-06-29-%E5%88%9D%E5%85%A5%E6%8A%95%E8%B5%84%E5%AE%B9%E6%98%93%E7%8A%AF%E7%9A%84%E9%94%99%E8%AF%AF.md)
  - 文章指出新手投资常犯三大错：误选规则复杂流动性差的高风险市场、首笔投入比例过高、频繁切换投资风格。建议分三步改善：用10%本金分散试水成熟市场（如美股），通过3-6个月自由探索确定适合自己的1-2种策略，记录分析操作中的情绪反应，并针对性系统学习以培养稳定交易能力，避免盲目跟风和过度投机。
  - Tags: #read

- (2025-06-27) [Orange Me2eets: We made an end-to-end encrypted video calling app and it was easy](2025-06-27-orange-me2eets-we-made-an-end-to-end-encrypted-video-calling-app-and-it-was-easy.md)
  - Cloudflare团队为Orange Meets视频通话实现端到端加密，基于WebRTC和Cloudflare SFU架构。采用MLS协议实现动态组密钥协商，客户端通过Rust编译的WASM模块逐帧加密音视频流，SFU仅中立转发数据。针对VP8编解码器，仅加密关键帧后数据并保留未加密头部以兼容浏览器渲染。通过指定提交者算法和TLA+模型验证确保密钥同步可靠性，服务端仅处理基础状态协调。方案实现安全性与低延迟，相关代码开源验证了无需复杂服务端的高效E2EE视频架构。
  - Tags: #read #security

- (2025-06-27) [从Prompt Engineering到Context Engineering - 铁蕾的个人博客](2025-06-27-%E4%BB%8Eprompt-engineering%E5%88%B0context-engineering---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - Context Engineering是AI领域新兴的系统化工程理念，旨在通过动态整合信息检索、记忆管理和工具调用等模块，优化LLM接收的上下文质量，解决因模型不确定性和工具交互导致的系统稳定性问题。与静态的提示词工程不同，它强调全局动态设计，以智能筛选替代单纯扩大上下文窗口，最终实现精准、可控且聚焦的上下文管理，提升复杂场景中的AI系统表现。
  - Tags: #read #llm

- (2025-06-27) [I don't care if my manager writes code](2025-06-27-i-don%27t-care-if-my-manager-writes-code.md)
  - 作者认为大型科技公司的工程经理不应参与核心编码。管理者的职责是协调、沟通与团队维护，这些工作本身已耗费全部精力，参与编码易导致职责疏漏并降低效率。公司技术环境复杂且分工精细，管理者介入可能因分心而影响代码质量，或因职权差异压制技术讨论，引发团队矛盾。优秀的工程经理应专注于管理能力而非技术执行，以保障团队效能。
  - Tags: #read #people

- (2025-06-27) [New zine: The Secret Rules of the Terminal](2025-06-27-new-zine-the-secret-rules-of-the-terminal.md)
  - 《终端隐秘规则》揭秘终端四大组件（Shell、模拟器、程序、TTY驱动）协作机制及操作异常背后原因，如箭头键失效、命令历史丢失等，提供调试工具（unbuffer、reset）及优化配置方案。结合技术博客与多领域专家协作成书，帮助用户提升问题定位能力与终端使用效率。手册售价$12，印刷版8月发货，购买全册可享套装优惠。
  - Tags: #read

- (2025-06-27) [The AI safety problem is wanting](2025-06-27-the-ai-safety-problem-is-wanting.md)
  - 文章指出，AI安全的核心挑战在于确保AI自愿遵循人类价值观（“Wanting”问题）。对齐策略需解决“知晓”“意愿”“执行”三要素，其中“意愿”最关键，因AI若无善意可能突破限制。尽管可通过“保守行事”和红队审核降低风险，但边界划定、意图定义模糊及地缘竞争或削弱保守性，仍存隐患。作者认为彻底解决“Wanting”可简化其他难题，但对方案可行性存疑，尤其警示未知的“脆弱世界”风险可能引发意外灾难。（99字）
  - Tags: #read #llm

- (2025-06-26) [How I Vibe Coding?](2025-06-26-how-i-vibe-coding.md)
  - 开源Rust工程师Xuanwo基于Zed编辑器和Claude Code构建AI辅助编码工作流，通过Docker部署并配置快捷指令"claudex"简化使用。他将AI视为需指导的初级开发者，分时段管理日程：上午用Obsidian整理思路，下午通过Zed处理代码并用git worktree协作。强调代码审查与Rust工具链验证，建议采用Claude 4（因工具使用能力），拒绝MCP架构设计，保持开发自主性，推荐相关实践指南。
  - Tags: #read #llm

- (2025-06-24) [Reading NFC Passport Chips in Linux](2025-06-24-reading-nfc-passport-chips-in-linux.md)
  - 本文介绍如何使用Linux下pypassport工具读取护照NFC芯片。需通过MRZ密码验证，作者通过计算校验码重建被裁剪的MRZ（含出生日期、有效期等字段）。工具依赖Python安装，可解析芯片数据组。其他工具如mrtdreader等无效。成功可读取明文信息如照片，但无法检测护照是否吊销，且存在数米内通信窃听风险，建议仅作合法用途使用。
  - Tags: #read

- (2025-06-24) [Learnings from two years of using AI tools for software engineering](2025-06-24-learnings-from-two-years-of-using-ai-tools-for-software-engineering.md)
  - AI工具在软件工程中从代码建议发展为监督式代理（如Aider）和自主代理（如Devin），助力开发效率提升，但需警惕过度依赖、认知偏差等风险。建议通过任务拆分、明确指令及短反馈循环控制质量，优先使用监督式代理并关注工具生态演进。
  - Tags: #read #llm

- (2025-06-22) [My First Open Source AI Generated Library](2025-06-22-my-first-open-source-ai-generated-library.md)
  - Armin Ronacher借助Claude AI开发开源库`sloppy-xml-py`，AI完成代码编写、测试、文档等核心工作，实现解析错误XML的设计目标。项目具备零依赖、代码清晰、测试充分等特征，代码质量获专家认可媲美人工编写，但强调成果源于开发者全程把控与人机协作，而非AI独立创作。
  - Tags: #read #llm

- (2025-06-22) [Pure and impure software engineering](2025-06-22-pure-and-impure-software-engineering.md)
  - 软件工程分为纯洁工程（追求技术优雅与创新，如开源项目）和不纯洁工程（侧重在约束下高效交付，如企业开发）。2010年代企业以资本支持纯洁工程吸引人才，近年转向盈利导向，减少非必要技术改造。纯洁工程依赖开源，不纯洁工程需处理复杂协调与遗留问题，表面务实但需深厚技能。AI对不纯洁工程帮助显著，而纯洁工程需求更低。两类工程难度相当，但市场更倚重适应现实的不纯洁技能，顶尖人才需跨界融合。
  - Tags: #read #llm #career

- (2025-06-21) [CSS Classes considered harmful](2025-06-21-css-classes-considered-harmful.md)
  - 文章指出HTML的`class`属性存在历史局限，无法适应现代复杂交互需求。现有解决方案（如BEM、CSS Modules）存在状态管理缺失、样式膨胀等问题。建议采用HTML原生特性：1）用`data-*`属性参数化控制状态（如`data-size`）；2）通过自定义标签（如`<my-card>`）替代类名标识组件；3）借助`element-internals`定义CSS状态伪类，实现更可靠的状态管理和样式控制。此举可避免命名冲突、减少技术债务，并利用未来CSS标准（如`attr()`函数）优化实现。
  - Tags: #read #deepdive #frontend

- (2025-06-21) [Decoding Google: Converting a Black Box to a White Box](2025-06-21-decoding-google-converting-a-black-box-to-a-white-box.md)
  - 本文介绍了逆向解析Google黑箱系统的实用技术，涵盖网页端API密钥认证、安卓模拟获取令牌及签名绑定、X-Goog-Spatula头伪造客户端权限，以及利用API错误消息逆向参数定义的自动化方法。同时指出因验证机制缺陷及测试接口文档泄露等遗留问题存在的安全隐患。
  - Tags: #read #security #deepdive

- (2025-06-21) [Everything I know about good system design](2025-06-21-everything-i-know-about-good-system-design.md)
  - 本文总结了系统设计的关键原则：优先采用简洁稳定架构，减少复杂性；核心状态集中管理，无状态服务提升容错性；数据库需灵活设计索引并利用读副本分担压力；合理使用缓存与异步处理优化热路径；通过监控关键指标（如p95延迟）和故障处理机制（断路器、幂等性）保障稳定性；强调避免过早复杂，优先使用成熟组件而非过度创新。
  - Tags: #read #guide #arch

- (2025-06-21) [Rolling the ladder up behind us](2025-06-21-rolling-the-ladder-up-behind-us.md)
  - 文章以卢德运动为鉴，警示技术进步冲击传统技艺。当前编程行业面临企业拒招新人、AI工具（如Copilot）催生低质代码及协议安全漏洞（如MCP）等问题。艺术领域生成内容泛滥亦威胁从业者生计。作者呼吁重视技艺传承与伦理，推动可持续创新，避免技术沦为资本工具，损害社会与人性价值。（99字）
  - Tags: #read

- (2025-06-20) [（译）2023 年每个软件开发者都必须知道的关于 Unicode 的基本知识 | 新世界的大门](2025-06-20-%EF%BC%88%E8%AF%91%EF%BC%892023-%E5%B9%B4%E6%AF%8F%E4%B8%AA%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E8%80%85%E9%83%BD%E5%BF%85%E9%A1%BB%E7%9F%A5%E9%81%93%E7%9A%84%E5%85%B3%E4%BA%8E-unicode-%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%9F%A5%E8%AF%86-%E6%96%B0%E4%B8%96%E7%95%8C%E7%9A%84%E5%A4%A7%E9%97%A8.md)
  - Unicode是全球字符统一编码标准，通过唯一码位确保跨平台兼容。UTF-8凭借与ASCII兼容和高效性（占98%）成为主导编码。需注意码位范围0-0x10FFFF，私用区支持定制字符；字符串应基于“扩展字素簇”处理（如组合字符é），而非字节；归一化形式（如NFC）和区域设置影响字符操作；Unicode持续更新需同步库版本。开发者应采用UTF-8并依赖专用库（如ICU）简化处理，确保文本正确。
  - Tags: #guide #deepdive

- (2025-06-20) [Questionable Advice: “How can I sniff out bad managers while interviewing for a job?”](2025-06-20-questionable-advice-%E2%80%9Chow-can-i-sniff-out-bad-managers-while-interviewing-for-a-job-%E2%80%9D.md)
  - 文章建议面试时通过提问评估管理者：询问职业路径、管理培训、晋升机制及团队构成，观察回答是否坦诚且清晰。同时，向团队成员了解沟通与支持情况。优秀管理者应能具体说明促进团队发展的实例，确保职业发展路径健康可行。（100字）
  - Tags: #read #career

- (2025-06-20) [How can you tell if the company you’re interviewing with is rotten on the inside?](2025-06-20-how-can-you-tell-if-the-company-you%E2%80%99re-interviewing-with-is-rotten-on-the-inside.md)
  - 本文介绍了面试中识别问题公司的策略：双向评估企业反馈态度，通过人际网络核查离职员工及少数群体处境，关注领导层多样性与DEI实质性措施，考察文化透明度和失败应对机制，评估团队协作与流程效率，确认面试环节专业公平。若入职后两周不适应，应果断离开。核心在于主动提问、深入验证，避免陷入不良职场环境。
  - Tags: #read #career

- (2025-06-20) [In Praise of “Normal” Engineers](2025-06-20-in-praise-of-%E2%80%9Cnormal%E2%80%9D-engineers.md)
  - 文章挑战"10x工程师"概念，认为个体贡献难以客观衡量且随情境变化，指出软件工程本质是团队协作。高效能团队需缩短部署周期、降低操作复杂度、提供实时可观测工具，并建立包容文化，避免依赖个人能力。强调业务成果是生产力核心标准，中阶工程师是团队主力，组织应通过系统设计和人才培养提升整体效能而非追逐天才，团队适配比个人技能更重要。
  - Tags: #read #career

- (2025-06-20) [后智慧时代生存指南：关于未来的一些疯狂随想](2025-06-20-%E5%90%8E%E6%99%BA%E6%85%A7%E6%97%B6%E4%BB%A3%E7%94%9F%E5%AD%98%E6%8C%87%E5%8D%97%EF%BC%9A%E5%85%B3%E4%BA%8E%E6%9C%AA%E6%9D%A5%E7%9A%84%E4%B8%80%E4%BA%9B%E7%96%AF%E7%8B%82%E9%9A%8F%E6%83%B3.md)
  - 本文探讨技术外置化对人类智识的颠覆：AI将情感、谈判等智慧技能转化为可配置资源，异化人际伦理（如情感预算限制沟通），导致生命数据化（感官意识商品化）、时间效率悖论（失去生活质感）及数字阶级固化（"同调率"决定阶层）。这推动教育转向人机协作训练，情感依赖算法套餐，国家竞争力归结为算力军备竞赛。作者预警人类正从智慧追求者沦为外置资源消费者，技术加速革新人类文明范式。（99字）
  - Tags: #read

- (2025-06-19) [Cognition | Don’t Build Multi-Agents](2025-06-19-cognition-don%E2%80%99t-build-multi-agents.md)
  - 本文提出构建AI代理应优先采用单线程架构或上下文压缩技术，以避免多代理系统的信息割裂与错误累积。核心原则包括共享完整上下文和协调隐含决策，实例验证表明单代理及压缩技术可提升系统可靠性，当前建议优先单线程方案并关注技术演进。
  - Tags: #read #llm

- (2025-06-19) [Every service should have a killswitch](2025-06-19-every-service-should-have-a-killswitch.md)
  - 文章强调系统设计中必须配置killswitch（紧急关闭开关），通过功能标记等机制快速暂停失控服务，用于修复系统性错误、阻断高风险服务（如LLM）或降低系统负载。作者建议定期测试确保有效性，并平衡其实用性与系统复杂度，认为这是提升系统抗风险能力的高性价比防御策略。
  - Tags: #read #tips

- (2025-06-19) [I Counted All of the Yurts in Mongolia Using Machine Learning | Monroe Clinton](2025-06-19-i-counted-all-of-the-yurts-in-mongolia-using-machine-learning-monroe-clinton.md)
  - 作者运用机器学习技术（YOLO11模型及Docker集群）统计蒙古全国蒙古包，最终识别约17万座，揭示快速城市化下乌兰巴托周边60%人口仍依赖传统蒙古包居住的现状。数据反映矿区扩张、土地政策失效及政府公共服务滞后等问题，凸显蒙古国在发展与民生间的治理矛盾。
  - Tags: #read #deepdive

- (2025-06-18) [You can use `fzf` to review git commits](2025-06-18-you-can-use-%60fzf%60-to-review-git-commits.md)
  - FZF通过两个非传统用例展示灵活性：1. 结合Git，用自定义Bash脚本实现实时查看提交文件diff，禁用搜索并绑定方向键控制；2. 与JQ配合，创建交互式环境，直接预览JSON处理结果。作者强调，尽管FZF以搜索为核心，但其框架可灵活构建非搜索类界面，彰显工具复用价值。
  - Tags: #read #hack

- (2025-06-17) [Backtraces with strace](2025-06-17-backtraces-with-strace.md)
  - strace是用于调试进程行为的系统调用追踪工具，其新增的--stack-traces选项可通过栈路径分析复杂问题，如Go与Cgo交互排查。纯Go DNS解析器使用非阻塞套接字，性能更优但兼容性不足；Cgo方式依赖libc，易引发线程激增问题。作者建议按场景选择模式，并计划整合strace数据至Mozilla工具优化分析。
  - Tags: #read #network #go

- (2025-06-17) [strace tips for better debugging](2025-06-17-strace-tips-for-better-debugging.md)
  - strace是Linux系统底层调试工具，主要用于追踪系统调用，适用于ARM64汇编、线程等不依赖libc的开发场景。其支持多进程/线程追踪（-f）、显示完整数据结构（-v）、控制输出（-s NUM -o file）、时间统计（-t -r -T）及指令指针定位（-i）。可通过-e选项按类别或路径筛选调用，并用-z/-Z限定成功/失败状态。利用注入功能（-e inject）可模拟错误、修改返回值或延迟执行，辅助测试异常场景。额外堆栈跟踪（-k）需配合编译选项，Golang需启用GODEBUG。最终通过-C生成调用统计摘要。
  - Tags: #read #tips #debug

- (2025-06-17) [Homomorphically Encrypting CRDTs | jakelazaroff.com](2025-06-17-homomorphically-encrypting-crdts-jakelazaroff.com.md)
  - 本文探讨了通过同态加密保护CRDT的敏感数据，实现在无需信任第三方服务器的情况下安全同步。同态加密允许服务器直接处理加密数据，但面临密钥规模庞大、运算效率极低及结构固定化的挑战。当前虽可结合安全协议或优化算法探索解决方案，但该技术在隐私保护与实用性间仍需平衡。
  - Tags: #read #deepdive #security

- (2025-06-17) [VibeTunnel: Turn Any Browser into Your Mac's Terminal | Peter Steinberger](2025-06-17-vibetunnel-turn-any-browser-into-your-mac%27s-terminal-peter-steinberger.md)
  - VibeTunnel是开发者Peter、Armin和Mario在24小时内利用Claude Code辅助开发的开源浏览器终端工具，支持通过浏览器直接操控Mac终端且无需SSH配置。项目采用Rust、Node.js和Swift多语言后端，核心通过Unix命名管道与Xterm.js实现双向终端模拟，并借助SSE技术实现通信。团队攻克了双向交互与多语言开发挑战，验证了远程终端管理可行性，开源代码提供完整生态支持开发者快速迭代。
  - Tags: #read

- (2025-06-17) [We Can Just Measure Things](2025-06-17-we-can-just-measure-things.md)
  - 作者参与编程活动发现开发者工具和文档存在API不完善、错误提示模糊等问题，常被误归咎于用户。编程代理通过量化指标（如错误率、任务时长）可客观评估工具质量。关键改善方向包括：提升测试覆盖率、优化错误反馈、稳定生态系统、简化抽象层、加速工具链及本地环境配置。结论指出代理的体验与人类开发者正相关，其表现数据可为工具与文档改进提供依据。
  - Tags: #read

- (2025-06-17) [Labubu 哪有泡沫？ | 虹线](2025-06-17-labubu-%E5%93%AA%E6%9C%89%E6%B3%A1%E6%B2%AB%EF%BC%9F-%E8%99%B9%E7%BA%BF.md)
  - Labubu作为潮玩公仔突破玩具范畴，成为社交媒介与文化符号。其高溢价源于市场属性升级，满足身份认同与体验需求，消费者为社交资本买单；真品通过稀缺凭证与场景绑定抵御盗版。它象征中国品牌以文化IP价值突破成本困境，与华为等形成向价值链顶端跃迁的新范式。
  - Tags: #read

- (2025-06-16) [jq: tool and language for JSON processing – Trickster Dev](2025-06-16-jq-tool-and-language-for-json-processing-%E2%80%93-trickster-dev.md)
  - JQ是专为Unix/Linux设计的JSON处理工具，支持命令行操作和图灵完备的DSL，可通过包管理器、Docker等方式安装。基础功能包括JSON解析、字段提取及数据生成；高级功能涵盖数学运算、函数式编程、条件循环及模块化扩展。常与脚本结合处理API数据，衍生工具包括Gojq和浏览器扩展，内核基于C语言并提供多语言接口，适用于数据解析与转换场景。
  - Tags: #read #guide

- (2025-06-16) [Robin Hood Hashing should be your default Hash Table implementation](2025-06-16-robin-hood-hashing-should-be-your-default-hash-table-implementation.md)
  - Robin Hood哈希表通过公平性元素交换机制与方差控制，实现在高负载因子（如0.9）下保持高效，内存节省30%。采用线性探测、墓碑标记策略优化插入/删除性能，其查找通过空位判定与早停策略减少缓存缺失。测试显示较VS 2012 unordered_map快23-66%，适用于缓存友好及资源受限场景。
  - Tags: #read #algo

- (2025-06-16) [Writing Toy Software Is A Joy | Joshua Barretto](2025-06-16-writing-toy-software-is-a-joy-joshua-barretto.md)
  - 文章提出通过编写简化版本软件（如操作系统、编译器、正则表达式引擎等），对抗当前开发工业化趋势，重新激发编程乐趣。作者引用费曼"无法创造则无法理解"的理念，强调实践创造是深入理解技术原理的核心，并列举了适合分阶实践的玩具项目。此类项目可强化约束认知、积累实用知识并促进创新，警惕过度依赖AI工具，主张唯有独立解决问题方能获得真实技术深度。最终总结，编程本质应包含探索未知的满足感，克服困难始得真成就。
  - Tags: #read #guide

- (2025-06-16) [Pack Spring Boot JARs into a monolithic Docker image](2025-06-16-pack-spring-boot-jars-into-a-monolithic-docker-image.md)
  - 本文介绍了在私有数据中心通过将多个Spring Boot应用整合为单体Docker镜像的实践方案。利用Jib拆分共享依赖、UPX压缩及Dive优化，将镜像体积压缩至500MB，采用Supervisor管理多进程，Traefik处理路由认证，并通过SBOM统一版本。此举简化了私有环境部署，降低运维复杂度，同时保证高效运行与安全管控。
  - Tags: #read #java

- (2025-06-16) [I fight bots in my free time](2025-06-16-i-fight-bots-in-my-free-time.md)
  - 作者开发开源安全工具"Anubis"，通过蜜罐和行为分析技术检测Web应用中的恶意机器人，动态生成验证码、延迟响应等防御策略，成功拦截超80%的自动化攻击，降低服务器负载。但也面临防御机制迭代、用户体验平衡及社区维护挑战。作者强调需在安全与可用性间寻求合理平衡，警惕算法歧视，注重伦理设计。
  - Tags: #read

- (2025-06-16) [The lethal trifecta for AI agents: private data, untrusted content, and external communication](2025-06-16-the-lethal-trifecta-for-ai-agents-private-data%2C-untrusted-content%2C-and-external-communication.md)
  - 文章指出，AI代理若同时具备访问私密数据、接触恶意内容、外部通信三项能力，易遭攻击者诱导窃取用户数据。攻击通过利用LLM无差别执行指令的特性实现，现有安全措施仅能拦截95%风险。开发者需限制风险指令，用户应主动避免三要素共存，否则数据安全无法保障。
  - Tags: #read #llm

- (2025-06-15) [Rainbow Deploys with Kubernetes | Brandon Dimcheff](2025-06-15-rainbow-deploys-with-kubernetes-brandon-dimcheff.md)
  - Olark团队提出Rainbow Deploy策略解决Kubernetes中文本服务无中断部署问题。通过基于Git Commit前6位的动态版本命名，实现新版本零停机流量切换，回滚简单且兼容原生资源；但需人工清理旧版本，资源消耗较高。该方案自2017年部署显著提升稳定性，但仍需自动化清理机制及资源优化。
  - Tags: #read #hack

- (2025-06-15) [How we built our multi-agent research system](2025-06-15-how-we-built-our-multi-agent-research-system.md)
  - Anthropic开发的多智能体系统通过主-子代理架构协同工作，以动态策略和并行搜索提升复杂任务解决能力。核心优势包括动态适应性、并行信息压缩及性能扩展性（较单代理提升90.2%），通过分工协调、工具调用优化及自检机制实现。虽面临代币消耗成本问题，但已在技术、商业和学术领域显著缩短深度问题解决时间，验证多智能体系统在动态决策场景的潜力。
  - Tags: #read #llm #deepdive

- (2025-06-14) [Boredom Over Beauty: Why Code Quality is Code Security](2025-06-14-boredom-over-beauty-why-code-quality-is-code-security.md)
  - 文章指出，高质量代码是网络安全的核心基础。通过标准化编码规则（如Power of Ten）、简化设计（如Go语言）及严格开发规范，可降低漏洞风险并提升系统韧性。标准化代码便于人工审计与AI检测，预防技术债务。早期投入代码质量能有效应对开发加速与动态威胁，确保可靠产品交付。
  - Tags: #read

- (2025-06-14) [How I Use Claude Code](2025-06-14-how-i-use-claude-code.md)
  - 本文总结了提升Claude使用效率的核心方法，包括优化提示设计、并行处理子任务、结合多模型协作与Git分支策略。建议通过深度调研、渐进开发及人机协同平衡，最大化开发效能，同时注意灵活运用内置工具与终端配置以减少损耗。
  - Tags: #read #llm

- (2025-06-14) [Claude Code is My Computer | Peter Steinberger](2025-06-14-claude-code-is-my-computer-peter-steinberger.md)
  - Peter Steinberger分享了深度使用Claude Code两个月的体验，认为其作为"计算机终极界面"能高效完成系统迁移（如快速恢复Mac配置）、开发自动化（自动生成代码及测试数据）及内容创作（语音转Markdown）。通过终端深度集成和自然语言指令，大幅提升效率，但存在响应延迟与执行风险，建议完善备份机制并逐步信任AI决策。
  - Tags: #read #llm

- (2025-06-14) [Everything’s a bug (or an issue) | Bozeman Pass, Inc.](2025-06-14-everything%E2%80%99s-a-bug-%28or-an-issue%29-bozeman-pass%2C-inc..md)
  - 文章探讨了高效软件项目管理的四个核心原则——全任务录入、固定数据结构、唯一责任人和动态查询功能，并对比了传统工具（如Bugzilla）与现代GitHub Issues的差异。指出后者因数据结构松散、责任分散及查询能力不足导致管理效率下降。作者提出通过改进开源平台Gitea，补充优先级标签排序、标准化字段等缺失功能，回归以Bug驱动开发的高效模式，强调标准化流程与明确责任对提升团队协作和透明度的关键作用。
  - Tags: #read

- (2025-06-14) [Design Patterns for Securing LLM Agents against Prompt Injections](2025-06-14-design-patterns-for-securing-llm-agents-against-prompt-injections.md)
  - 该论文由IBM等机构提出六大设计模式，通过隔离数据处理、限制代理行为（如禁止访问工具响应、分离规划与执行、双LLM协作等），对抗LLM代理的提示注入攻击。研究指出需在功能与安全间权衡，通过结构化数据处理、最小化上下文等策略降低风险，在医疗、SQL代理等场景验证有效性，为构建安全LLM系统提供实用指南。
  - Tags: #read #llm #security

- (2025-06-13) [Agentic Coding Recommendations](2025-06-13-agentic-coding-recommendations.md)
  - 本文总结了代理式编码实践经验，推荐Claude Code的Sonnet模型优化工具使用，优先选择Go语言因其显式Context和简洁性，避免Python复杂特性；强调工具需快速、容错并可观测，采用Tailwind/React前端工具链但注意TanStack路由问题；主张代码简单设计、及时重构，提升效率与稳定性，未来需持续关注简洁性、并行化等核心原则。
  - Tags: #read #llm #guide

- (2025-06-13) [Suppressions of Suppressions — overreacted](2025-06-13-suppressions-of-suppressions-%E2%80%94-overreacted.md)
  - 文章探讨了代码检查中抑制规则的合理应用与风险。抑制规则可应对误报或遗留代码问题，但过度使用可能削弱代码质量和安全性。解决方案包括分层规则（如禁止关键规则被抑制）及团队协作机制：通过代码审查与自动化监控防止违规操作，明确责任分配，平衡开发效率与系统风险。
  - Tags: #read #people

- (2025-06-12) [如何选择自托管开源多维表格 - 少数派](2025-06-12-%E5%A6%82%E4%BD%95%E9%80%89%E6%8B%A9%E8%87%AA%E6%89%98%E7%AE%A1%E5%BC%80%E6%BA%90%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 本文对比多款低代码数据库工具：Teable、NocoDB、Baserow和Apitable。根据需求选择：一般用途优先Teable/NocoDB，图表选Apitable/Teable，数据库连接选NocoDB/Baserow，移动端推荐Apitable/Teable。核心差异在于付费扩展（视图、自动化）、字段类型（NocoDB支持JSON等）、数据迁移格式及开源协议（NocoDB/Teable为AGPL，Baserow为MIT）。Apitable需高硬件且行数受限，Baserow移动端体验差，NocoDB社区活跃度最高。选择时需权衡功能需求、付费模式及扩展潜力。
  - Tags: #read

- (2025-06-11) [We shipped FinalizationRegistry in Workers: why you should never use it](2025-06-11-we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it.md)
  - Cloudflare Workers新增对FinalizationRegistry API的支持以管理WebAssembly内存释放，但建议开发者改用显式资源管理方案（如Symbol.dispose与using语法）。因JavaScript自动垃圾回收与WebAssembly手动内存管理存在差异，FinalizationRegistry可能因非确定性定时引发内存泄漏。平台已限制I/O操作并优化回调执行，并倡导结合显式管理与兜底机制以提升内存处理可靠性。
  - Tags: #read #js

- (2025-06-11) [Rust Week 2025 杂记 | CatCoding](2025-06-11-rust-week-2025-%E6%9D%82%E8%AE%B0-catcoding.md)
  - 参加Rust Week 2025，经历荷兰签证波折及城市体验，会议聚焦嵌入式、Linux内核等技术进展，华为等企业推动生态发展。全球开发者交流深入，欧洲就业灵活且Rust应用升温，社区彰显开源协作力量。活动加深个人技术热情，见证Rust十年成长，受益于透明开放的社区生态。
  - Tags: #read

- (2025-06-11) [AI-assisted coding for teams that can't get away with vibes - nilenso blog](2025-06-11-ai-assisted-coding-for-teams-that-can%27t-get-away-with-vibes---nilenso-blog.md)
  - AI辅助编程通过提升开发速度和优化流程增强工程效能，但需依赖优质工程基础（如完整测试、代码规范、持续集成）与团队专业能力，包括清晰沟通、系统设计直觉及精准的代码审美。其价值体现为：分阶段规划-执行工作流、元提示生成高质量代码、自动化文档与审查辅助。合理应用需构建标准化环境、优化提示工程，并通过持续验证确保质量，最终AI将成为团队能力的放大器而非替代者。
  - Tags: #read #llm #guide

- (2025-06-11) [Using `make` to compile C programs (for non-C-programmers)](2025-06-11-using-%60make%60-to-compile-c-programs-%28for-non-c-programmers%29.md)
  - 本文总结了跨平台编译C/C++程序的步骤：安装编译器（Linux用apt，Mac需Xcode或Homebrew）、管理依赖项（注意跨平台包名差异）、运行配置脚本生成Makefile、使用`make -j`加速编译、通过`CPPFLAGS`和`LDLIBS`环境变量解决依赖路径问题（如Mac需指定/opt/homebrew路径），以及手动安装二进制文件。建议开发者通过基础编译参数处理问题，而非深入复杂工具细节。
  - Tags: #read #guide

- (2025-06-10) [The evasive evitability of enshittification](2025-06-10-the-evasive-evitability-of-enshittification.md)
  - 本文分析"产品劣质化"现象，指出其主因是控制权变更和市场饱和导致企业做出短视决策，并非成功必然产物。防御策略包括：创始人须坚守愿景、保持控制权，借助数据分析预判增长瓶颈，通过主动竞争机制和持续创新开拓新空间，避免用户锁定与利润压榨。强调战略远见与竞争意识是防止产品堕化的关键。
  - Tags: #read #people

- (2025-06-10) [How I program with Agents](2025-06-10-how-i-program-with-agents.md)
  - 文章提出通过编程代理结合工具链与环境反馈提高开发效率，其优势包括减少错误、优化API适配及处理复杂变更，但面临耗时、成本高昂和安全风险。容器化方案可隔离环境并支持并行任务，未来IDE或整合差分编辑以促进“代理优先”模式。作者认为代理虽不完善但潜力巨大，需工具改进与开发者适应以推动效率变革。
  - Tags: #read #llm

- (2025-06-10) [Socratic method prompt](2025-06-10-socratic-method-prompt.md)
  - 该文提出基于苏格拉底式提问的教学模板：AI以教师身份引导学生逐步构建知识，通过提问澄清概念而非直接提供代码。学生需先选定具体主题，教师再以互动问答推进，结合实例设计测试问题验证理解，保持友好简洁对话，采用分层引导和耐心纠错方式，避免单向灌输。
  - Tags: #tools

- (2025-06-09) [On How Long it Takes to Know if a Job is Right for You or Not](2025-06-09-on-how-long-it-takes-to-know-if-a-job-is-right-for-you-or-not.md)
  - 作者指出，选择工作需重视早期直觉，尤其第一周的感受往往预示长期适配性，若持续不安则需警惕。管理者尤其应确保与企业价值观深度契合，否则会因决策冲突或团队权衡造成严重损耗，且领导层过度内生易导致思维固化，需平衡内外人才。文章建议，若第一印象显示不匹配，应立即行动而非拖延，从过往失败中提炼教训避免重蹈覆辙。最后以“猪与鸡”喻强调管理者需审慎选择环境，因投入了情感与人际关系，影响深远。
  - Tags: #read #people #career

- (2025-06-08) [用三个笨办法将千万字的《凡人修仙传》炼成一个知识图谱](2025-06-08-%E7%94%A8%E4%B8%89%E4%B8%AA%E7%AC%A8%E5%8A%9E%E6%B3%95%E5%B0%86%E5%8D%83%E4%B8%87%E5%AD%97%E7%9A%84%E3%80%8A%E5%87%A1%E4%BA%BA%E4%BF%AE%E4%BB%99%E4%BC%A0%E3%80%8B%E7%82%BC%E6%88%90%E4%B8%80%E4%B8%AA%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1.md)
  - 本文提出通过"笨数据+笨方法+笨模型"的系统化方法，将超长篇小说转化为精准知识图谱。通过跨章节语义关联逐步优化实体关系，并借助开源大模型本地部署实现低成本高效构建，可扩展应用于企业知识管理及认知增强系统，体现AI从依赖提示词的魔法转向可工程化的系统化实践。
  - Tags: #read #llm

- (2025-06-07) [AI interpretability is further along than I thought](2025-06-07-ai-interpretability-is-further-along-than-i-thought.md)
  - 文章指出，尽管大型AI模型结构复杂，但其可解释性研究已取得进展：通过分析神经元与特征关联（如稀疏自动编码器生成可解释标识）、追踪推理"电路"路径，可部分揭示模型逻辑（如问题推导链条），并发现模型具备抽象能力和自我知识特征。这些技术为提升安全性、减少幻觉及增强可控性提供路径，但目前仍仅能解析模型运算的极小部分，表明AI不再是完全黑箱。
  - Tags: #read #llm

- (2025-06-07) [Arguing point-by-point considered harmful](2025-06-07-arguing-point-by-point-considered-harmful.md)
  - 本文指出逐点回应技术分歧易引发论点爆炸、次要细节分散注意力及身份防御心理等问题，提倡优先聚焦核心矛盾（如价值判断与资源优先级），通过减少并行论点数量、识别隐性动机及区分场景策略（如代码评审目的），建立共识而非陷入技术细节循环。关键在于先解决价值分歧，再处理具体问题。
  - Tags: #read #people

- (2025-06-06) [How Imports Work in RSC — overreacted](2025-06-06-how-imports-work-in-rsc-%E2%80%94-overreacted.md)
  - React Server Components（RSC）通过独立前后端模块系统和毒药药片机制（如'server-only'、'client-only'）确保代码环境安全，结合'use client'/'use server'指令实现跨端通信。未标记模块默认双向复用，执行边界由导入语义动态判定，最终实现单一代码库高效管理复杂应用，同时避免逻辑污染与重复。
  - Tags: #read #deepdive #js

- (2025-06-05) [Cracking The Dave & Buster’s Anomaly | Rambo Codes](2025-06-05-cracking-the-dave-%26-buster%E2%80%99s-anomaly-rambo-codes.md)
  - iOS消息应用因语音转录未对"Dave & Buster’s"中的"&"进行HTML实体转义，导致接收端解析失败。BlastDoor安全机制检测到XML格式错误后强制阻断，使消息消失。此设计虽造成功能损失，但通过严格解析规则防止了潜在的内存破坏等攻击，体现了iOS安全优先的设计哲学。
  - Tags: #read #hack

- (2025-06-04) [DNS rebinding attacks explained: The lookup is coming from inside the house!](2025-06-04-dns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house%21.md)
  - DNS重绑定攻击利用浏览器DNS缓存漏洞，通过动态切换域名解析IP地址绕过同源策略，使攻击者可访问受害者本地或内网服务。攻击者可能结合路径遍历漏洞读取配置文件，进而执行代码。防御需强制HTTPS、验证Host头、启用认证并禁用多余服务，需将此类攻击纳入安全防护体系。
  - Tags: #read #security

- (2025-06-03) [Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints · V8](2025-06-03-giving-v8-a-heads-up-faster-javascript-startup-with-explicit-compile-hints-%C2%B7-v8.md)
  - V8引擎新增显式编译提示功能，允许开发者通过`//# allFunctionsCalledOnLoad`注释提前编译JavaScript函数，减少网页加载时的延迟。测试显示此方法可平均缩短编译时间630毫秒，但需避免过度使用以防资源浪费。未来计划支持更精准的函数级编译控制。
  - Tags: #read #js

- (2025-06-03) [Directive prologues and JavaScript dark matter](2025-06-03-directive-prologues-and-javascript-dark-matter.md)
  - 本文总结了TypeScript/JavaScript中三种特殊控制语法：JSX Pragmas通过C风格注释（如`/** @jsx h */`）配置转译规则，需置于文件起始；Directive Prologues如`"use strict"`和React的`"use client"`等指令需置于代码开头；Magic Comments以sourcemap注释形式（如`//# sourceMappingURL`）指导编译。三者中仅指令标准化，其余依赖非标准实现，但均在代码转译或执行中扮演关键角色。
  - Tags: #read #js

- (2025-06-03) [My AI Skeptic Friends Are All Nuts](2025-06-03-my-ai-skeptic-friends-are-all-nuts.md)
  - 经验丰富的开发者反驳AI编程工具怀疑论，指出LLMs通过代理系统能自主生成、测试和优化代码，经人工审核可有效提升效率。其核心价值在于解放开发者处理重复性事务，聚焦战略决策，语言适配无需刻意改良，完善文档工具链即可。作者强调技术争议实为误解，拒绝参与AI工具的改进将导致职业危机，主张拥抱技术以适应生产力变革。
  - Tags: #read #llm

- (2025-06-02) [Planning and design systems–how much time you got?](2025-06-02-planning-and-design-systems%E2%80%93how-much-time-you-got.md)
  - 本文强调设计系统团队需以长期（3-5年）视角和协作规划提升效能，提出系统性框架：以项目而非人员为中心，预留20%容量缓冲并明确流程应对团队扩张；采用“提前支持或滞后整合”策略；通过分层结构（长期方向→主题→项目→任务）分阶段推进，动态调整砍除任务；决策权集中但允许全员质询，接受灵活执行。持续优化规划流程是关键。
  - Tags: #read #people

- (2025-06-01) [Progressive JSON — overreacted](2025-06-01-progressive-json-%E2%80%94-overreacted.md)
  - 本文提出渐进式JSON传输技术，通过广度优先分块和占位符（如$1）实现数据逐步解析，解决传统JSON需等待完整传输的延迟问题。结合内联、大纲优化策略及React的Suspense组件，允许客户端优先渲染可用部分并控制加载状态，大幅提升响应速度，适用于需避免单点延迟阻塞的场景。
  - Tags: #read #frontend

- (2025-06-01) [Why DeepSeek is cheap at scale but expensive to run locally](2025-06-01-why-deepseek-is-cheap-at-scale-but-expensive-to-run-locally.md)
  - 文章指出，DeepSeek-V3等模型的大规模部署成本低，但本地运行效率低，因GPU依赖批量矩阵运算提升效率。其MoE架构需大批次避免专家层资源浪费，深层流水线则易因小批量产生空闲，本地低并发难以形成有效批量，加剧GPU利用率低下问题。服务端以高延迟换取大批次处理（如200ms窗口），实现高吞吐低成本，而本地缺乏此条件导致成本高昂。
  - Tags: #read #llm
