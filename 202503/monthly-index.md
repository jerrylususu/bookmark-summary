# 2025-03 Monthly Index

- (2025-03-31) [Building native packages is complicated](2025-03-31-building-native-packages-is-complicated.md)
  - 该文章介绍了反自动化防护措施，重点介绍Techaro公司开发的Anubis工具，其通过技术手段区分真人用户与自动化程序。Anubis的GitHub仓库及官网被提及，文章提示部分页面可能因加载问题导致内容不完整，需设置超时时间确保完整加载。核心聚焦于提升网站安全防御以抵御自动化攻击。
  - Tags: #read

- (2025-03-28) [Implementers, Solvers, and Finders](2025-03-28-implementers%2C-solvers%2C-and-finders.md)
  - 本文提出程序员职业分三阶段：实施者（执行任务）、解题者（自主解决问题）、探索者（定义方向），核心是自主权递增。传统职称模糊且晋升机制失效，而职业满足感源于自主、技能提升与目标感。建议按角色需求选择环境（如中型公司适合解题者），强调通过自主权导向而非头衔重新定义路径，技术人亦可不转管理而成长为有决策权的探索者。
  - Tags: #read #people

- (2025-03-28) [Wheel Reinventor's Principles // Tobias Løfgren](2025-03-28-wheel-reinventor%27s-principles-tobias-l%C3%B8fgren.md)
  - 文章探讨了"重新发明车轮"的价值与实践，指出其核心动机包括学习、场景适配、创新及技术乐趣。需注意避免过度投入与偏离目标，并遵循聚焦需求、简化工具、拒绝黑箱及共享成果的原则，强调在理性评估与专注执行中实现可持续创新。
  - Tags: #read #guide

- (2025-03-28) [Async, Sync, in Between](2025-03-28-async%2C-sync%2C-in-between.md)
  - 现代编程中，同步与异步函数混用易引发“异步蔓延”，导致代码级联修改和冗余。通过生成器函数实现自适应执行：根据调用上下文动态选择同步或异步模式，减少代码重复及重构负担。但存在约120ns性能开销，且需显式设计兼容逻辑。该方案适用于需兼容同步/异步场景的库或插件系统。
  - Tags: #read #frontend

- (2025-03-26) [The surreal joy of having an overprovisioned homelab](2025-03-26-the-surreal-joy-of-having-an-overprovisioned-homelab.md)
  - 文章《确保你不是机器人》源自xeiaso.net演讲页面，包含重复标题、两幅表情图及加载延迟提示。其受Techaro公司Anubis系统保护，核心内容未完整加载，可能存在动态加载或安全验证机制，需注意数据完整性风险。
  - Tags: #read #deepdive

- (2025-03-26) [You can’t vibe code a prompt | Building with AI](2025-03-26-you-can%E2%80%99t-vibe-code-a-prompt-building-with-ai.md)
  - incident.io的404页面含导航栏（核心产品、解决方案等）、试用登录入口及社交媒体链接，并提供响应式设计、错误提示及状态监控功能。目标文章因内容调整或迁移导致链接失效，当前仅展示标准404页面，未包含预期内容。（99字）
  - Tags: #read #llm

- (2025-03-26) [Installing NPM Packages Very Quickly](2025-03-26-installing-npm-packages-very-quickly.md)
  - 文章通过开发简易包管理器"caladan"对比bun等工具，指出npm包安装性能差异源于底层语言效率（如Zig的系统调用优势）和资源管理策略。优化包括并行处理、内存直接操作文件及解压算法优化。测试显示bun冷安装速度领先caladan 11%，证明系统级语言（如Zig/Go）更适合性能关键场景，强调需突破网络/IO限制进行系统级优化。
  - Tags: #read #perf #deepdive

- (2025-03-25) [A maintainer's guide to vulnerability disclosure: GitHub tools to make it simple](2025-03-25-a-maintainer%27s-guide-to-vulnerability-disclosure-github-tools-to-make-it-simple.md)
  - 该指南为开源项目维护者提供GitHub漏洞处理流程：启用私有漏洞报告（PVR）接收安全报告，通过草稿安全通告协作修复，申请CVE标识，发布清晰公告并利用Dependabot通知用户更新，确保漏洞保密高效解决，提升项目安全性与用户信任。
  - Tags: #read #guide

- (2025-03-23) [Building SaaS Products with AI: What Actually Works](2025-03-23-building-saas-products-with-ai-what-actually-works.md)
  - 本文系统阐述利用AI工具链高效开发SaaS产品的步骤：通过Lovable进行原型设计，Cursor/Roo Code辅助功能开发，结合Supabase搭建后端，并采用RepoMix进行安全扫描。强调分阶段迭代、日志记录及AI生成代码的分层调试（50%错误率需人工修正），适合基础开发者快速构建原型，但复杂场景仍需专业工程能力。
  - Tags: #read #llm

- (2025-03-22) [Building a (T1D) Smartwatch from Scratch](2025-03-22-building-a-%28t1d%29-smartwatch-from-scratch.md)
  - 作者为患1型糖尿病的儿子开发儿童智能手表，整合CGM数据监测、触觉警报及游戏化界面。项目攻克硬件集成、蓝牙优化、机械设计等难题，制成防水原型，支持5分钟血糖更新及个性化表盘。原型通过半年测试但量产需解决电池寿命、供应链及医疗认证问题，凸显个体开发者利用开源技术突破医疗硬件门槛的潜力与挑战。
  - Tags: #read #deepdive

- (2025-03-22) [Booleans Are a Trap](2025-03-22-booleans-are-a-trap.md)
  - 布尔值因简洁性常被滥用，但会引发领域模型复杂度激增（如门、企业模型因布尔组合导致非法状态激增）。改用枚举（如DoorState）与集合替代，配合状态机定义流转规则，可有效减少无效状态并简化维护，作者建议将布尔值限于技术层，领域层优先采用枚举和状态机管理复杂业务逻辑。
  - Tags: #read

- (2025-03-22) [Ejectable Apps](2025-03-22-ejectable-apps.md)
  - 本文提出"可抽离应用"概念，通过数据完整打包、自托管后端和无缝模式切换等设计，结合云端协作优势与本地数据主权，确保用户可随时脱离云端独立使用数据，兼具灵活性与抗风险性。目前正通过Thymer任务管理工具实践该模式，推动应用生态向更开放持久方向发展。
  - Tags: #read

- (2025-03-22) [The Five-Week Solo Startup](2025-03-22-the-five-week-solo-startup.md)
  - 《Five-Week Solo Startup》提出五阶段创业策略：首周提升创始人能力（形象、沟通、AI工具）；次周验证商业模式并获取首客；第三周拓展客户、融资及品牌建设；第四周搭建系统与营销渠道；末周聚焦增长与团队组建。强调低成本验证、客户需求优先、资源杠杆及价值观坚守，主张五周内构建创业基础，平衡主业与行动力。
  - Tags: #read

- (2025-03-22) [The "think" tool: Enabling Claude to stop and think](2025-03-22-the-think-tool-enabling-claude-to-stop-and-think.md)
  - 当前提供的文章内容不完整，仅有标题"正在加载..."，未检测到可结构化分析的正文内容。请检查原文链接有效性或等待页面完全加载后重试，若需帮助请补充提供可阅读的完整文本。
  - Tags: #read #llm

- (2025-03-21) [图解神经网络和强化学习：400 行 C 代码训练一个井字棋高手（2025）](2025-03-21-%E5%9B%BE%E8%A7%A3%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%92%8C%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%EF%BC%9A400-%E8%A1%8C-c-%E4%BB%A3%E7%A0%81%E8%AE%AD%E7%BB%83%E4%B8%80%E4%B8%AA%E4%BA%95%E5%AD%97%E6%A3%8B%E9%AB%98%E6%89%8B%EF%BC%882025%EF%BC%89.md)
  - 本文介绍了通过400行C代码实现的井字棋强化学习项目。使用含100节点隐藏层的神经网络，经200万局对弈训练后，AI胜率达84%，平局15%，几乎不败。代码仅依赖标准库，训练速度极快（150万局数秒内完成），验证神经网络本质为数学运算组合，非复杂技术黑箱。
  - Tags: #read #deepdive

- (2025-03-21) [Rewarding ideas](2025-03-21-rewarding-ideas.md)
  - 现代社会的信息生产通过版权、专利等机制激励内容创作，但存在保护期限矛盾、技术法律冲突等问题。人工智能因零成本复制与重组信息，冲击现有制度，致侵权界定困难及经济模式崩溃。应对需法律调整（如明确"衍生作品"标准）或技术方案（如自动溯源系统），但路径仍不明确，需重新平衡信息生产与言论自由。
  - Tags: #read

- (2025-03-19) [Base 32](2025-03-19-base-32.md)
  - Crockford的Base32编码通过32个符号（含0-9及22字母，排除易混淆字符）实现数据高效编码，每个符号代表5比特。解码时自动转换大小写（如o→0）、忽略连字符，编码统一为大写。采用模37校验（含额外符号）保障可靠性，适用于需简洁且抗误读的场景，如安全传输公钥等。
  - Tags: #tools

- (2025-03-19) [My Thoughts on the Future of "AI"](2025-03-19-my-thoughts-on-the-future-of-ai.md)
  - 域名nicholas.carlini.com因涉嫌通过网页https://nicholas.carlini.com/writing/2024/how-i-use-ai.html的过度DOM渲染发起DoS攻击，被判定为安全妥协（SecurityCompromiseError），遭封锁至2039年12月31日。该错误属法律政策类（状态码451），具体因安全事件（扩展码45102）触发。
  - Tags: #read #llm

- (2025-03-18) [Wasp](2025-03-18-wasp.md)
  - Wasp是基于React、Node.js和Prisma的全栈框架，提供类Rails的高效开发体验。其核心包含全栈认证、类型安全RPC通信、任务调度及声明式配置功能，通过单一CLI生成前后端代码与部署配置。开发者称赞其配置简洁、学习成本低，适合快速搭建应用。近期将强化Prisma集成与SSR支持，未来扩展多平台及语言，开源并活跃于社区。
  - Tags: #tools

- (2025-03-17) [Big LLMs weights are a piece of history - <antirez>](2025-03-17-big-llms-weights-are-a-piece-of-history---antirez.md)
  - 文章指出互联网历史资料因网页失效快速流失，互联网档案馆受资金和法律限制难完全保存。作者建议利用大语言模型（LLMs）的"有损压缩"能力，通过公开模型权重并纳入预训练，结合技术与人文手段应对信息湮灭，并强调持续支持档案馆的重要性。（99字）
  - Tags: #read #llm

- (2025-03-17) [Extracting content from an LCP "protected" ePub](2025-03-17-extracting-content-from-an-lcp-protected-epub.md)
  - 该文介绍通过调试Electron框架的Thorium阅读器破解LCP加密EPUB的方法：启用调试模式后提取已解密的HTML、图片等资源，重组为DRM-free电子书。作者强调此举仅用于合法购书用户的格式转换，但引发伦理争议，Readium联盟警告可能因此升级DRM限制。文中指出当前LCP方案限制用户设备选择且增加开发者成本，作者坚持技术缺陷需公开以维护用户权益。
  - Tags: #read #hack

- (2025-03-17) [Tips For Better Interactions](2025-03-17-tips-for-better-interactions.md)
  - 文章总结优化沟通与会议的六大技巧：避免情绪化标签，以明确意图发起对话；主动承担会议记录，提升讨论逻辑与焦点；拒绝极端场景反驳，专注具体建议；宽容非核心错误，暂存争议后续沟通；精准安排会议时间（避开低效时段、禁用自动调整）及线上开摄像头；聚焦2-3项高优先级议题，确保深度讨论而非贪多仓促决策。
  - Tags: #read #people

- (2025-03-17) [My Cursor AI Workflow That Actually Works](2025-03-17-my-cursor-ai-workflow-that-actually-works.md)
  - 本文总结使用Cursor AI的编码工作流：通过配置规则文件（如避免占位符）、提供项目上下文（引用代码路径）、分阶段开发与自动化处理重复任务；关键模块需人工审查并生成测试。核心经验为精准指令+上下文支持+严格审核，将AI作为需监督的工具提升生产力，同时注重安全代码人工校验及具体化提问。
  - Tags: #read #llm

- (2025-03-16) [This is what it looks like to be colorblind](2025-03-16-this-is-what-it-looks-like-to-be-colorblind.md)
  - 色盲者常面临辨色困扰（如机票低价日期混淆、停车指示误读），全球约3.5亿人受影响，99%为红绿色盲。设计师过度依赖红绿对立色加剧问题，需采用文字、纹理等非颜色标识辅助。EnChroma眼镜等工具效果有限，近年部分产品（如Wordle色盲模式）改进，但需更深度包容设计，体现共情与多元需求。
  - Tags: #read #design

- (2025-03-14) [Opsec and you: how to navigate having things to hide](2025-03-14-opsec-and-you-how-to-navigate-having-things-to-hide.md)
  - 本文探讨数字时代操作安全（Opsec），建议根据个人威胁模型制定策略。核心包括：使用加密通信、多因素认证、清理文件元数据；采用化名并搭配AI模糊身份；推荐Tor、Signal等工具及自托管服务；强调在隐私与便利间平衡，接受失误并通过分层防御（如加密、自动删除）降低风险。
  - Tags: #read #deepdive #security

- (2025-03-14) [Functional Tests As A Tree Of Continuations – Evan Miller](2025-03-14-functional-tests-as-a-tree-of-continuations-%E2%80%93-evan-miller.md)
  - 本文提出功能测试"延续树"方法，通过树形结构将每个步骤设为节点，子节点继承父节点数据库快照状态，使测试代码量从O(N²)降至O(N)。该方法消除冗余代码，精准定位故障，支持跨步骤数据对比，且结构直观对应用户操作流程。其基于数据库版本控制实现，在Chicago Boss框架中通过嵌套回调构建树形测试结构，显著提升测试效率。
  - Tags: #read

- (2025-03-12) [Here’s how I use LLMs to help me write code](2025-03-12-here%E2%80%99s-how-i-use-llms-to-help-me-write-code.md)
  - 高效利用LLMs编程需明确其辅助角色，结合训练数据时效性选择可靠方案，通过多路径验证、精准指令及工具（如代码沙箱）优化开发。强调强制测试验证、人类主导关键决策，利用上下文迭代与反馈提升效率，同时警惕模型幻觉与安全风险。
  - Tags: #read #llm #guide #deepdive

- (2025-03-12) [Manus爆火的背后，Agentic AI产品如何构筑持久的竞争优势？](2025-03-12-manus%E7%88%86%E7%81%AB%E7%9A%84%E8%83%8C%E5%90%8E%EF%BC%8Cagentic-ai%E4%BA%A7%E5%93%81%E5%A6%82%E4%BD%95%E6%9E%84%E7%AD%91%E6%8C%81%E4%B9%85%E7%9A%84%E7%AB%9E%E4%BA%89%E4%BC%98%E5%8A%BF%EF%BC%9F.md)
  - Manus通过整合AI工具链构建三重复利：工具组合产生爆炸式体验提升，数据全生命周期沉淀形成专属知识库，智能LLM优化策略执行。三者协同进化形成壁垒，关键在于系统化结构化隐性知识的方法论，而非单纯技术参数，最终胜出者需构建AI与人稳定共进化体系。
  - Tags: #read #llm

- (2025-03-11) [Affording your AI chatbot friends](2025-03-11-affording-your-ai-chatbot-friends.md)
  - 本文探讨了AI聊天机器人成本与可控性的平衡策略。核心组件包括模型、推理引擎、代码及用户界面。云服务API虽便捷但存在高昂成本、隐私风险及供应商锁定问题；自托管虽可控但硬件和运维成本高。游牧计算通过多云资源灵活调配、轻量化模型及混合部署（如实例Mimi），结合输入管理、参数优化等实践，可在降低成本的同时保持控制力，关键在于分层管理数据与算力。
  - Tags: #read #llm #deepdive #guide

- (2025-03-11) [Delegating Complex Tasks](2025-03-11-delegating-complex-tasks.md)
  - 文章提出两种管理者授权复杂任务的方法：指数训练（通过深度一对一培训和实战机会，指数级培养专家）和次优标准化（拆解流程为步骤，建立分级审批机制提升决策效率）。强调信息透明是关键，需打破信息壁垒，优先通过流程拆分和实战授权扩大团队能力，而非追求管理者个人微优化。
  - Tags: #read #people

- (2025-03-11) [When worse is better](2025-03-11-when-worse-is-better.md)
  - 本文提出"更糟即更好"原则，主张技术选型应放弃完美主义，在资源限制下优先考虑成本与可行性。通过PHP、Excel等非最优技术流行案例，及过度工程导致项目失控的教训，说明市场更接受"够用"方案。强调接受妥协（如容忍Bug或安全缺口）是合理策略，技术决策本质是价值取舍，需在现实约束下寻求最优妥协路径。（99字）
  - Tags: #read

- (2025-03-10) [Where are we now, system researchers? – Xiangpeng’s blog](2025-03-10-where-are-we-now%2C-system-researchers-%E2%80%93-xiangpeng%E2%80%99s-blog.md)
  - 系统研究因学术界脱离实际需求、学者缺乏工程实践能力（如编码经验不足）及论文评审侧重理论创新而实用性欠奉，导致研究价值被工业界超越。作者主张通过大规模实践（如编写代码、用户交互）积累系统性认知，重建重视实操的研究文化。
  - Tags: #read

- (2025-03-10) [Building Websites With LLMS](2025-03-10-building-websites-with-llms.md)
  - 本文提出LLMS网站构建方法，通过多小HTML页面结合CSS过渡技术替代复杂JavaScript交互，简化开发并提升体验。案例显示，用静态生成独立页面管理过滤与导航功能，减少代码且维护更易，更适合静态网站，虽存在跳转局限但更简洁直观，符合Web粒度特性。
  - Tags: #read #frontend

- (2025-03-09) [Perplexity: Interactive language modeling visualization](2025-03-09-perplexity-interactive-language-modeling-visualization.md)
  - 用户开发了基于GPT-2的可视化工具，通过高亮与注释展示文本生成过程中的词预测概率。当输入数列时，模型准确性随序列递增；随机词汇组合重复输入后，模型能快速学习模式（验证Transformer的归纳能力）。工具在浏览器端运行，采用transformers.js和Oak框架，注重隐私保护。
  - Tags: #llm #tools

- (2025-03-08) [Strobelight: A profiling service built on open source technology](2025-03-08-strobelight-a-profiling-service-built-on-open-source-technology.md)
  - Strobelight是Meta研发的高性能分析系统，整合42种开源分析工具（如eBPF、jemalloc），通过低开销的数据采集和符号化技术，实时监控CPU/内存等指标，并支持火焰图等可视化分析。其动态采样与自动调优功能可减少20% CPU消耗，单次代码优化即节省年均1.5万台服务器容量，同时提供冲突规避机制及开源扩展能力，显著提升资源利用率与开发效率。
  - Tags: #read

- (2025-03-08) [Every Line Is a Potential Bug](2025-03-08-every-line-is-a-potential-bug.md)
  - 文章通过案例说明过度优化和代码复杂性可能引发潜在错误。原始代码虽简单但正确，评审提议动态计算等待时间时，两次修改均引入缺陷（如负数等待或无限期等待）。作者强调代码复杂性与Bug直接相关，主张仅在必要时使用最简方案，抵制冗余优化和过度设计。
  - Tags: #read

- (2025-03-08) [A few words about indie app business – Charlie Monroe](2025-03-08-a-few-words-about-indie-app-business-%E2%80%93-charlie-monroe.md)
  - 该文总结独立开发者经历与经验：作者自幼编程，经历项目失败、兼职维生等挑战，最终通过调整策略实现财务自由。核心建议包括持续改进产品、平衡工作强度、谨慎合作、有效管理用户反馈及分散风险。独立开发需长期投入与高度适应力，成功关键在于耐心与现实评估，虽艰难但成果值得。
  - Tags: #read #job

- (2025-03-08) [How I Automated My Podcast Transcript Production With Local AI](2025-03-08-how-i-automated-my-podcast-transcript-production-with-local-ai.md)
  - 作者开发开源工具roboscribe，通过整合WhisperX语音处理和Llama-3.1等大模型，实现本地AI自动化播客转录与优化。该工具可自动完成转录、时间轴对齐、说话人分离及文本清理（去除冗余、修正语法），处理35分钟音频仅需15分钟，输出质量显著提升。当前需高配GPU运行，未来计划优化适配更多设备。工具已开源（GitHub可获取）。
  - Tags: #read #llm

- (2025-03-08) [The Cursed Art of Streaming HTML – rinici.de](2025-03-08-the-cursed-art-of-streaming-html-%E2%80%93-rinici.de.md)
  - 文章介绍一种无需JavaScript或WebSockets的流式传输HTML技术，通过浏览器保持连接特性逐段推送内容实现实时更新。其核心技术包括框架流式接口（如Node.js的res.write）、iframe隔离聊天内容追加新消息，解决响应流未关闭及表单刷新问题。兼容旧版浏览器，支持分块加载但需注意XSS防护，附代码示例。
  - Tags: #read #frontend

- (2025-03-07) [Great software design looks underwhelming](2025-03-07-great-software-design-looks-underwhelming.md)
  - 优秀的设计通过结构化消除潜在故障而非依赖复杂补丁。其核心方法包括：保护高频路径（如将低效组件移出核心流程）、减少冗余组件（如重构系统为静态网站）、集中数据状态（设置单一数据源）、依赖可靠技术（如选择高稳定服务器）。设计应优先消除高风险问题，即使牺牲性能或灵活性，最终以极简架构实现系统稳定与可维护性。
  - Tags: #read #design

- (2025-03-06) [Graphing Calculator Story](2025-03-06-graphing-calculator-story.md)
  - Ron Avitzur在Apple秘密开发图形计算器，失业后潜入公司继续工作，获得同事支持，最终项目成功成为Macintosh的一部分，推动了教育软件发展，尽管过程充满法律和伦理争议。
  - Tags: #read

- (2025-03-06) [Why "alias" is my last resort for aliases](2025-03-06-why-alias-is-my-last-resort-for-aliases.md)
  - 作者从使用转向脚本实现命令别名，脚本无需重新加载、支持多种编程语言且可处理复杂逻辑，虽然性能稍逊但提供了更多灵活性和功能。
  - Tags: #read #guide

- (2025-03-05) [The Hierarchy of Hazard Controls](2025-03-05-the-hierarchy-of-hazard-controls.md)
  - 文章介绍了控制危害的层次结构（HoC）在软件工程中的应用，包括消除、替代、工程控制、行政控制和个人防护设备五个层次，并讨论了其在软件环境中的具体应用、注意事项及潜在风险。
  - Tags: #read

- (2025-03-05) [DeepSearch/DeepResearch 实施实用指南](2025-03-05-deepsearch-deepresearch-%E5%AE%9E%E6%96%BD%E5%AE%9E%E7%94%A8%E6%8C%87%E5%8D%97.md)
  - DeepSearch是2025年新兴的搜索标准，通过迭代搜索、阅读和推理提供高质量答案。它集成了测试时计算和延迟满足技术，主要区别于DeepResearch，后者生成结构化长篇研究报告。实现细节包括系统提示、查询重写和网页内容抓取等。
  - Tags: #read #llm

- (2025-03-01) [The reality of long-term software maintenance from the maintainer's perspective](2025-03-01-the-reality-of-long-term-software-maintenance-from-the-maintainer%27s-perspective.md)
  - 本文通过作者维护大型软件项目的经验，揭示了长期维护的复杂性，强调初始代码仅占工作量的一小部分，后续维护才是主要挑战。文章通过建筑类比和实际案例，说明了外部贡献者提交的代码可能带来长期负担，呼吁对软件改进持更现实的态度。
  - Tags: #read

- (2025-03-01) [Optimizing with Novel Calendrical Algorithms](2025-03-01-optimizing-with-novel-calendrical-algorithms.md)
  - 作者通过性能审计，设计了新的日期时间算法，优化了 crate的性能，最终实现比现有算法快57.5%，且无分支，过程复杂但结果显著。
  - Tags: #read #deepdive

- (2025-03-01) [Five coding hats](2025-03-01-five-coding-hats.md)
  - 文章探讨了五种不同的编码风格，分别对应不同场景和需求，强调根据具体任务选择合适的编码风格，以提高效率和适应性。
  - Tags: #read #guide

- (2025-03-01) [Smuggling arbitrary data through an emoji](2025-03-01-smuggling-arbitrary-data-through-an-emoji.md)
  - 文章探讨了在表情符号中编码任意数据的可能性，利用Unicode变体选择器实现隐藏信息，并提供了Rust代码示例。讨论了潜在滥用的风险及LLM对此类数据的处理能力。
  - Tags: #read #hack

- (2025-03-01) [Hand Tracking for Mouse Input](2025-03-01-hand-tracking-for-mouse-input.md)
  - 本文作者尝试使用手势控制鼠标输入，通过MediaPipe检测手部位置，Python模拟鼠标操作，解决了延迟、抖动等问题，最终实现了类似Apple Vision Pro的手势控制鼠标功能，代码开源。
  - Tags: #read #hack
