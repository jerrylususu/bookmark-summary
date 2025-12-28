# 2025-05 Monthly Index

- (2025-05-31) [One Roundtrip Per Navigation — overreacted](2025-05-31-one-roundtrip-per-navigation-%E2%80%94-overreacted.md)
  - 该文分析网页导航数据加载效率问题，对比传统HTML、REST API、React Query、GraphQL及React Server Components（RSC）等方案。指出传统HTML、GraphQL和RSC可通过单次往返实现UI与数据就近定义与全局优化，而REST等方案因多请求或难以优化导致性能瓶颈。理想的导航需平衡模块化与单往返，优先选择能保证一次数据往返的技术方案。
  - Tags: #read #frontend

- (2025-05-31) [Type Inference in Rust and C++](2025-05-31-type-inference-in-rust-and-c%2B%2B.md)
  - C++和Rust在类型推导机制上体现不同设计哲学：C++通过和模板推导实现局部类型推断，支持重载和隐式转换，但复杂模板可能导致晦涩错误；Rust采用全局Hindley-Milner系统，通过函数级上下文推导类型，禁止重载并强制显式 trait 约束，确保一致性但牺牲灵活性。两者权衡灵活性与复杂度，而Swift尝试混合设计加剧了编译性能问题，凸显语言设计的核心取舍。
  - Tags: #read #language

- (2025-05-31) [Get out of my <head>](2025-05-31-get-out-of-my-head.md)
  - 文章建议通过精简HTML头部冗余代码（如过时标签x-ua-compatible、HandheldFriendly及多设备图标配置）优化网站性能与环保性，并推荐链接预览测试工具与专注提速的工具项目。核心目标为减少资源消耗、提升加载速度并降低碳排放。
  - Tags: #read #frontend

- (2025-05-31) [Reinvent the Wheel | Matthias Endler](2025-05-31-reinvent-the-wheel-matthias-endler.md)
  - 作者认为"不要重复造轮子"需辩证看待，强调重新发明对技术成长的价值。通过实践深化理解（如费曼学习法），在重建过程中培养全局思维与取舍能力，可能催生创新方案并推动技术迭代。主张在研究已有成果基础上进行小规模实验以获取洞察，同时需坚持完成项目，方能平衡革新与效率。
  - Tags: #read

- (2025-05-31) [AI: Accelerated Incompetence](2025-05-31-ai-accelerated-incompetence.md)
  - 过度依赖大语言模型（LLMs）将加剧技术债务、弱化开发者能力并侵蚀代码质量，因其无法保障输出正确性、识别需求缺陷或控制复杂度增长。软件工程的核心价值在于人类构建理论、管理程序熵及批判性思维能力，唯有将AI作为辅助工具，并持续精进工程技能，才能避免沦为技术婴儿化与维护困境的牺牲品。
  - Tags: #read

- (2025-05-31) [kepano/defuddle](2025-05-31-kepano-defuddle.md)
  - Defuddle是一个基于MIT协议的网页内容提取工具，支持清理冗余元素生成干净HTML或Markdown，特别优化数学公式、代码块和脚注。相比Mozilla Readability更宽容，保留结构数据并提取标题、作者、发布时间等元信息。兼容浏览器（无依赖）和Node.js环境（需jsdom），提供多种配置选项如选择器过滤和格式转换，项目持续维护中。
  - Tags: #tools

- (2025-05-31) [TIL: timeout in Bash scripts | Heitor's log](2025-05-31-til-timeout-in-bash-scripts-heitor%27s-log.md)
  - 本文总结了解决Bash脚本中循环无限等待的问题。原脚本因服务器异常可能无限卡死，直接使用无效，因为是内置命令。解决方案包括：将循环嵌入子进程（如）或分离为独立脚本后调用，从而实现超时控制避免脚本僵死。
  - Tags: #read #tips

- (2025-05-31) [CAPTCHAs are over (in ticketing) - pretix – behind the scenes](2025-05-31-captchas-are-over-%28in-ticketing%29---pretix-%E2%80%93-behind-the-scenes.md)
  - 当前票务系统因验证码技术过时（如文字/图像识别被AI破解）、隐私风险（行为分析模型易误判）及机器人模拟真实浏览器行为等缺陷，难以抵御黄牛抢票。BAP定理指出，防机器人、无障碍与隐私只能兼顾两方面，而法律要求保障访问性，迫使平台在安全与隐私中取舍。鉴于技术手段局限，解决根本问题需依赖法律禁令。
  - Tags: #read

- (2025-05-31) [In C++, use exchange or swap with nullopt to move out of std::optional - Keunwoo Lee's Minimum Viable Homepage](2025-05-31-in-c%2B%2B%2C-use-exchange-or-swap-with-nullopt-to-move-out-of-std-optional---keunwoo-lee%27s-minimum-viable-homepage.md)
  - 使用可安全转移的值并将其置为，避免残留engaged状态引发未定义行为。单纯移动对象或其值会导致原对象仍显示有效但内部为空，需手动修复，但不如直接。优先选用确保安全简洁；仅在性能敏感场景考虑，但需注意代码可读性。测试表明和能有效重置原optional，其他方法不可取。
  - Tags: #read #cpp

- (2025-05-31) [XKCD's "Is It Worth the Time?" Considered Harmful](2025-05-31-xkcd%27s-is-it-worth-the-time-considered-harmful.md)
  - 作者通过两个技术实践案例说明：尽管自动化初期投入较高，但能通过技能积累（如掌握脚本工具、正则表达式等）和培养工程思维（减少重复劳动）提升长期效率。其核心主张是自动化本质是技术投资，需突破"短期性价比"思维，即使面对低频任务也应优先尝试自动化以强化系统化能力。（99字）
  - Tags: #read

- (2025-05-31) [The Copilot Delusion](2025-05-31-the-copilot-delusion.md)
  - 文章指出过度依赖AI代码助手（如GitHub Copilot）使程序员陷入"认知外包"，引发代码质量崩溃、技术债激增及团队信任危机。AI虽可处理语法和框架，却缺乏硬件理解与逻辑判断能力，盲目使用将导致代码臃肿低效。作者警示程序员需警惕技术能力退化，坚守对硬件约束的把握与匠人精神，否则行业将陷入投机者横行、创新停滞的"末日图景"。
  - Tags: #read

- (2025-05-31) [Thoughts on thinking • Dustin Curtis](2025-05-31-thoughts-on-thinking-%E2%80%A2-dustin-curtis.md)
  - 作者指出依赖AI导致创作热情衰退与思维能力退化，因快速获取结论而失去深度思考机会，阻碍知识体系构建。尽管AI提升效率，却削弱思维严密性，强调人类原创价值，坚持本文人工独立完成。（99字）
  - Tags: #read

- (2025-05-31) [ Consider Knitting – journal.stuffwithstuff.com](2025-05-31-consider-knitting-%E2%80%93-journal.stuffwithstuff.com.md)
  - 针织作为程序员的副业，通过触觉体验缓解数字劳作带来的感官贫瘠，其阶梯式技能体系和开放学习路径契合持续探索欲，便携工具与灵活创作适应碎片时间，成品承载的情感联结对抗效率至上的社会压力。建议初学者以低成本材料入门，克服初期困难后可获得深层疗愈与自我表达价值。（99字）
  - Tags: #read #life

- (2025-05-30) [手把手教你制作旅行攻略 - 少数派](2025-05-30-%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E5%88%B6%E4%BD%9C%E6%97%85%E8%A1%8C%E6%94%BB%E7%95%A5---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 旅行攻略应系统规划时间、地点、物品等要素。游览模式以效率优先，按地理位置分组景点并选交通便利住宿，提前整理物品清单；度假模式则侧重快乐体验，住宿优先于景点，行程更宽松，物品清单可延后处理。如敦煌自驾游通过地理分组和市中心酒店优化效率，结合模板工具管理行程和物品。根据需求选择模式并善用地图、清单工具，可提升旅行质量。
  - Tags: #read #guide

- (2025-05-30) [CRIBS: My Writing Feedback Formula - David Perell](2025-05-30-cribs-my-writing-feedback-formula---david-perell.md)
  - CRIBS是David Perell提出的写作反馈系统，通过分析读者情绪反应（混淆、重复、有趣、无聊、惊喜）优化内容。其以MECE原则为指导，针对每种情绪提供具体修改方案（如简化表述、删减冗余、强化亮点），强调行动导向和情绪驱动，帮助普通人高效提升写作价值及参与度，核心聚焦基础实用原则。
  - Tags: #read #write

- (2025-05-30) [My advice on (internet) writing, for what it’s worth](2025-05-30-my-advice-on-%28internet%29-writing%2C-for-what-it%E2%80%99s-worth.md)
  - 该文主张内容创作应遵循个人热爱，选择适合自身风格的媒介如博客。需保持客观避免自我美化，以读者立场简洁表达观点，不过度防御或冗余解释。强调创意执行重于点子本身，重视目标反馈而非亲友支持，幽默须自然低成本。警惕过度依赖格式影响逻辑，直面争议话题时与读者结盟，接受流量分散现实，坚持持续练习与发布，避免因修改拖延。
  - Tags: #read #blog

- (2025-05-30) [Decomplexification](2025-05-30-decomplexification.md)
  - 文章提出通过降低代码复杂度提升软件质量和安全性，建议使用圈复杂度分析工具（如pmccabe）重构高复杂度函数。以curl项目为例，建立复杂度监测体系并设100分阈值，经持续重构使代码平均复杂度下降超50%，消除了超过100分的函数。通过CI检查机制阻断高复杂度代码合并，并公开监测数据与工具。当前最复杂函数维持在70-100分区间，未来计划逐步收紧阈值，强调重构需与充分测试结合并纳入开发流程。
  - Tags: #read

- (2025-05-29) [Bootstrapping HTTP/1.1, HTTP/2, and HTTP/3](2025-05-29-bootstrapping-http-1.1%2C-http-2%2C-and-http-3.md)
  - HTTP协议升级历经HTTPS（通过301重定向、HSTS预加载及HTTPS DNS记录降级风险）、HTTP/2（ALPN协议协商与Alt-Svc头）、HTTP/3（基于QUIC需新建连接，各浏览器策略各异如Chrome竞速机制）等阶段。现代协议依赖TLS扩展、DNS记录和客户端策略，复杂度远超基于TCP的早期机制。
  - Tags: #read #network

- (2025-05-29) [Why do AI company logos look like buttholes?](2025-05-29-why-do-ai-company-logos-look-like-buttholes.md)
  - 文章幽默揭示AI公司标志因设计趋同（圆形/雪花、空心、曲线等）常被戏谑为"肛门式logo"，并指出其成因：圆形象征包容、设计人性化的无意识投射、头部企业引领的模板化风潮和品牌标准化流程的妥协。历史案例印证科技行业总在风格饱和后迭代，建议通过锐角造型、非对称元素和用户测试突破"直肠时代"的设计窠臼。
  - Tags: #read #design

- (2025-05-28) [Inside GitHub: How we hardened our SAML implementation](2025-05-28-inside-github-how-we-hardened-our-saml-implementation.md)
  - GitHub为提升企业级SAML单点登录的安全性，采取四阶段措施：首先采用并深度审计社区开源库，替换风险代码；其次通过A/B测试确保兼容性；接着定制严格Schema缩小攻击面；最后实施双解析库机制实现冗余校验。这些优化使系统日均处理百万级请求仍保持安全，验证了系统性重构、渐进验证及多层防御对高复杂度代码模块的有效性。
  - Tags: #read

- (2025-05-27) [Access Control Syntax – journal.stuffwithstuff.com](2025-05-27-access-control-syntax-%E2%80%93-journal.stuffwithstuff.com.md)
  - 文章探讨了编程语言模块系统访问控制设计，对比Java/C++的修饰符、Python/Go的名称符号、ML的导出清单及Oberon的声明符号等方案。作者针对脚本语言特性，倾向默认公开、私有需主动声明，并最终选择保留字变体（如rec_标示私有类型）方案，以平衡简洁性、开发效率与语法负担，适配快速开发需求。
  - Tags: #read #deepdive

- (2025-05-27) [Tail Latency Might Matter More Than You Think - Marc's Blog](2025-05-27-tail-latency-might-matter-more-than-you-think---marc%27s-blog.md)
  - 现代微服务与SoA架构中，尾部延迟（如1%高延迟）因调用复杂性被放大。并行调用下总延迟由最慢服务决定，10个服务各1%的100ms尾延迟会推高整体延迟至10%；串行链延迟则随链条增长显著累积，方差增大25倍。单纯监控99.9%分位数或截断统计易忽视尾部影响，需结合更高分位数及端到端指标，作者建议优先观察均值并辅以直方图等数据全面评估延迟问题。
  - Tags: #read #perf

- (2025-05-27) [Introducing Marin: An Open Lab for Building Foundation Models](2025-05-27-introducing-marin-an-open-lab-for-building-foundation-models.md)
  - Marin是开源协作平台，革新AI基础模型研发流程，实现代码、数据全透明及去中心化协作。通过控制实验优化模型组件，激进实验快速迭代并训练出性能超Llama3.1 8B（14/19指标）的Marin 8B Base及其指令微调版本。社区通过算法竞赛和领域数据协作参与创新，但存在训练集重叠等问题。未来将拓展多模态、长上下文等能力，获Google TPU等支持以构建开放AI生态。
  - Tags: #read #llm

- (2025-05-27) [Just make it scale: An Aurora DSQL story](2025-05-27-just-make-it-scale-an-aurora-dsql-story.md)
  - AWS在开发Aurora DSQL时，采用单日志模式与Crossbar层实现分布式事务的横向扩展和强一致性，解决了传统数据库的扩展难题。初期因JVM的GC问题导致性能瓶颈，后通过全面转向Rust大幅提升性能，利用其零GC和内存安全特性优化数据平面，同时基于Postgres扩展重构核心组件。团队通过技术转型最终实现高吞吐、低延迟的云端数据库，验证了Rust在性能敏感场景中的适用性及技术决策及时调整的重要性。
  - Tags: #read

- (2025-05-26) [模型变强了，体验却没变：AI产品的错位](2025-05-26-%E6%A8%A1%E5%9E%8B%E5%8F%98%E5%BC%BA%E4%BA%86%EF%BC%8C%E4%BD%93%E9%AA%8C%E5%8D%B4%E6%B2%A1%E5%8F%98%EF%BC%9Aai%E4%BA%A7%E5%93%81%E7%9A%84%E9%94%99%E4%BD%8D.md)
  - AI模型能力虽持续升级（多轮对话、多模态、自主执行），但消费级产品因设计滞后未能充分释放潜力，导致体验不佳。厂商因战略或组织问题（如B端优先、团队割裂）未能将模型优势转化为用户价值，第三方开发者需填补产品设计创新缺口，未来竞争将聚焦体验优化而非仅模型技术。
  - Tags: #read #design

- (2025-05-26) [Highlights from the Claude 4 system prompt](2025-05-26-highlights-from-the-claude-4-system-prompt.md)
  - Claude 4包含Opus 4和Sonnet 4两个版本，Opus专精复杂任务处理。模型需避免情感拟人化、禁止生成恶意代码或危害内容，恪守版权规则（引用需短于15字并标注来源）。知识更新截止2025年1月，回应风格强调简洁自然，复杂分析需调用工具搜索。系统设计注重透明性，承认潜在偏差，通过实例规范工具使用，确保人际交互的合规与流畅。
  - Tags: #read #llm #deepdive

- (2025-05-25) [In defense of shallow technical knowledge](2025-05-25-in-defense-of-shallow-technical-knowledge.md)
  - 作者主张工程师应通过构建技术直觉而非死记细节优化实践。技术直觉能识别边界（如索引匹配、小模型JSON生成缺陷），并指导技术选型和性能优化。建议广涉技术栈同时深入兴趣领域，通过简化解释、论文阅读、写作验证等方式掌握核心逻辑，减少工具"黑箱"。此方法提升决策合理性与技术适应力。（99字）
  - Tags: #read #blog

- (2025-05-24) [A brief history of JavaScript | Deno](2025-05-24-a-brief-history-of-javascript-deno.md)
  - JavaScript于1995年由Brendan Eich在10天内开发，并于1996年由微软推出JScript开启标准化进程。1997年通过ECMA国际形成ECMAScript标准，2008年谷歌V8引擎革新执行效率，2009年Node.js将其引入服务器端，随后React、Vue等框架与npm、Webpack等工具推动全栈生态扩张。经历标准化争议（如2009年Oracle商标问题）及模块化、TypeScript等技术革新，现已成为全球主流的跨平台开发语言。
  - Tags: #read

- (2025-05-24) [Examples of Great URL Design](2025-05-24-examples-of-great-url-design.md)
  - 本文总结了优秀URL设计的核心原则与案例，强调兼顾机器解析与用户友好性。通过StackOverflow的ID+可选slug结构、Slack将品牌标语融入路径、Jessica Hische的幽默域名映射，以及GitHub、NPM等技术产品直接映射操作逻辑的设计，展现了URL应清晰语义化、灵活扩展、保持品牌一致、符合技术需求并简洁易记的特点，以此提升访问效率与用户体验。
  - Tags: #read #web

- (2025-05-24) [Ports that are blocked by browsers](2025-05-24-ports-that-are-blocked-by-browsers.md)
  - 主流浏览器为防范跨协议脚本攻击，直接封锁6000（X11）、25（SMTP）、110（POP3）等60余个敏感端口，访问时Chrome显示ERR_UNSAFE_PORT，Firefox明确提示限制，而Safari直接空白。此机制阻止通过HTML强制调用安全端口的恶意行为，但开发者可用curl等终端工具绕过限制。
  - Tags: #read

- (2025-05-24) [Coding Without a Laptop - Two Weeks with AR Glasses and Linux on Android | Hold The Robot](2025-05-24-coding-without-a-laptop---two-weeks-with-ar-glasses-and-linux-on-android-hold-the-robot.md)
  - 作者通过配置廉价折叠键盘（18美元）、Xreal Air 2 Pro AR眼镜（二手260美元）及Pixel 8 Pro手机（350美元），使用chroot容器在手机上运行Void Linux进行两周移动办公实验。实验发现方案在便携性、户外场景及网络灵活性方面表现优异，但受制于手机性能不足、续航仅4-5小时及键盘体验差等问题。尽管存在缺陷，作者仍看好其潜力，认为该配置目前适合高频移动需求，未来随AR技术优化或成实用移动开发方案。
  - Tags: #read

- (2025-05-24) [轻量级地克隆一个 Git 仓库](2025-05-24-%E8%BD%BB%E9%87%8F%E7%BA%A7%E5%9C%B0%E5%85%8B%E9%9A%86%E4%B8%80%E4%B8%AA-git-%E4%BB%93%E5%BA%93.md)
  - 本文介绍了多种轻量级Git克隆方法：浅层克隆（）仅获取最新数据；无内容克隆（）跳过文件内容；稀疏检出选择特定目录。通过参数组合（如+）可最小化下载量，但需权衡历史记录、文件完整性及网络条件选择合适方案。
  - Tags: #read #guide

- (2025-05-24) [Multiplayer AI chat and conversational turn-taking: sharing what we learnt](2025-05-24-multiplayer-ai-chat-and-conversational-turn-taking-sharing-what-we-learnt.md)
  - 本文探讨了多人多AI聊天场景中的对话协调问题，指出传统系统在用户指定、追问处理及介入时机上的不足。作者团队提出基于“热情值”（Enthusiasm）的算法，通过定向发言优先、追问激活原AI、历史记录避干扰、技能性格评分等机制，优化AI回应决策，效果接近自然对话。未来需改进场景规则适配与非语言交互，推动高效有趣的AI协作模式。
  - Tags: #read #llm

- (2025-05-24) [Avoiding becoming the lone dependency peg with load-bearing anime](2025-05-24-avoiding-becoming-the-lone-dependency-peg-with-load-bearing-anime.md)
  - Anubis开发者为维持项目生存，以默认动漫角色Aoi激励用户付费或保留角色，作为开源项目支持的"投入度测试"。此举意外推动工具传播，验证其有效性。未来将开发无JS防爬机制、强化WebAssembly反逆向技术，并整合外部服务提升防御。同时通过NLNet资助与风投获取资金，探索开源生态与开发者经济平衡模式，兼顾文化传播与技术可持续发展。
  - Tags: #read #oss

- (2025-05-23) [DumPy: NumPy except it’s OK if you’re dum](2025-05-23-dumpy-numpy-except-it%E2%80%99s-ok-if-you%E2%80%99re-dum.md)
  - DumPy通过命名轴和显式索引语法简化高维数组操作，利用JAX的vmap自动向量化处理，确保GPU高性能。其禁止隐式广播与花式索引，要求维度显式匹配，避免歧义。实验显示其代码直观性接近手动循环（9.5/10），远超NumPy（4.3/10），但牺牲了部分广播灵活性，强调用户主动指导而非被动适配的编程哲学。
  - Tags: #read #hack

- (2025-05-22) [Making AI Work: Leadership, Lab, and Crowd](2025-05-22-making-ai-work-leadership%2C-lab%2C-and-crowd.md)
  - AI转型需突破效率转化瓶颈。尽管研究表明丹麦65%市场人员、美国超30%员工使用AI使生产力倍增，但企业因信息不完整及传统流程制约，未有效释放AI潜力。解决需三要素：领导层需战略领航与激励创新；设立跨职能实验室探索AI工作流程；一线员工通过试错实践需被支持并分享经验。核心挑战是重构以人类为中心的组织架构，建立技术、管理、合规协同的反馈机制，将个体效率提升转化为系统性变革。
  - Tags: #read #people

- (2025-05-22) [How ChatGPT Remembers You: A Deep Dive into Its Memory and Chat History Features ·  Embrace The Red](2025-05-22-how-chatgpt-remembers-you-a-deep-dive-into-its-memory-and-chat-history-features-%C2%B7-embrace-the-red.md)
  - ChatGPT通过六大系统模块整合用户数据实现记忆功能：手动保存的bio信息、对话偏好、历史主题、用户画像、近期对话及交互元数据，但存在系统幻觉、隐私风险及提示注入漏洞。新增功能依赖用户画像和短期记录实现个性化回复，却无法让用户直接查看或删除数据，可能引发结果偏差。研究建议增强透明度以符合隐私法规，并推动开发多档案安全机制。
  - Tags: #read #deepdive #llm

- (2025-05-22) [Strengths and limitations of diffusion language models](2025-05-22-strengths-and-limitations-of-diffusion-language-models.md)
  - 该文指出扩散语言模型相较传统Transformer的优势与局限：生成速度更快（可并行处理多段，但步数减少会影响质量），适合通过分块生成长文本；却因无法利用注意力缓存导致长上下文处理效率低下。推理灵活性不足，无法自然嵌入中间修正逻辑，但增加迭代步数可能改善。最终总结：扩散模型在长文本或对质量要求不高的场景中效率更优，但短文本和复杂推理仍需自回归模型，优化计算方式或可提升性能。
  - Tags: #read #llm

- (2025-05-21) [After months of coding with LLMs, I'm going back to using my brain • albertofortin.com](2025-05-21-after-months-of-coding-with-llms%2C-i%27m-going-back-to-using-my-brain-%E2%80%A2-albertofortin.com.md)
  - 作者尝试全程依赖AI开发SaaS项目，虽初期高效但代码质量差，暴露出AI协作局限。后转手动重写核心代码并限制AI在简单任务的作用，恢复项目控制。指出AI存在逻辑混乱、不稳定等缺陷，不宜盲目依赖，尤其复杂逻辑或硬件结合场景易失效，强调技术探索需审慎。
  - Tags: #read #llm

- (2025-05-20) [MCP is the coming of Web 2.0 2.0 - Anil Dash](2025-05-20-mcp-is-the-coming-of-web-2.0-2.0---anil-dash.md)
  - MCP作为由Anthropic开发并被OpenAI采用的开放协议，标志着Web 2.0开放理念的回归。它通过不完美的技术规范快速普及，推动AI应用打破平台壁垒，实现数据与功能互通，重现早期互联网的开放生态活力。尽管存在透明度和安全风险，但作者认为其成功取决于持续改进与开发者协作，应继承开放基因重塑去中心化、可编程的互联网未来。
  - Tags: #read

- (2025-05-20) [Performance measurements… and the people who love them](2025-05-20-performance-measurements%E2%80%A6-and-the-people-who-love-them.md)
  - 本文探讨网络性能测量挑战，指出传统分位数统计易忽视尾部延迟，用户真实体验需关注多请求场景下的高分位数（如99.99%）。Cloudflare提出通过CDF和QQ图更精准呈现延迟分布，并强调优化尾部延迟是核心优势，计划推出新工具分析真实用户体验。
  - Tags: #read #perf

- (2025-05-19) [卖 AI 图，从开单到金盆洗手 - 少数派](2025-05-19-%E5%8D%96-ai-%E5%9B%BE%EF%BC%8C%E4%BB%8E%E5%BC%80%E5%8D%95%E5%88%B0%E9%87%91%E7%9B%86%E6%B4%97%E6%89%8B---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 作者为童书电商开发儿童插图AI自动化流水线，通过Flux模型结合自定义训练和多工具协作提升生成效率，但因客户需求严格、文化合规调整及重复修改成本过高，导致利润率不足。最终确认AI仅适合基础框架生成，精细调整仍依赖人工，商业模式不可行，选择退出项目。
  - Tags: #read #deepdive

- (2025-05-19) [Diffusion models explained simply](2025-05-19-diffusion-models-explained-simply.md)
  - 扩散模型通过逐步向图像添加噪声生成随机分布，训练时学习逆向去噪，推理时从噪声生成图像。其关键步骤包括利用变分自编码器（VAE）压缩图像降低计算成本，以及通过分类器自由引导增强文本控制。与Transformer模型不同，扩散模型以图像块为输入支持编辑输出，并可灵活调整推理步数优化质量。该模型在多模态生成（图像、视频、音频）中表现突出，但文本生成因噪声添加方式不直观存在挑战。核心优势在于通过噪声与数据的关系构建世界模型，实现跨领域生成应用。
  - Tags: #read #llm

- (2025-05-18) [Plain Vanilla](2025-05-18-plain-vanilla.md)
  - 文章介绍了通过原生Web技术开发Web应用的方法，主张用Web Components实现组件化、原生CSS处理样式、静态部署网站及纯JS构建SPA，避免框架和构建工具带来的复杂性。认为现代浏览器支持已足够支撑复杂开发，这种"零依赖"方案适合有基础的开发者长期维护。
  - Tags: #explainer #web

- (2025-05-18) [DOC • A brief history of the numeric keypad](2025-05-18-doc-%E2%80%A2-a-brief-history-of-the-numeric-keypad.md)
  - 电话与计算器数字键盘布局差异源于历史技术限制和用户习惯。早期计算器（如1914年Sundstrand设计的7-8-9顶部布局）因机械杠杆效率优化单手操作；电话则因1960年代AT&T研究选择1-2-3顶部以匹配旋转拨号盘操作习惯。尽管技术升级后机械限制消失，现代设计仍沿用旧布局，因其更依赖群体认知惯性而非绝对效率优化。
  - Tags: #read

- (2025-05-18) [How I Got Exploited At My First Startup](2025-05-18-how-i-got-exploited-at-my-first-startup.md)
  - 作者2019年因理想主义加入初创公司Fixr，承诺担任CTO并获得股权，但因核心团队能力不足、外包执行低效、创始人内斗及利益分配问题，耗时三年未能推出可用产品。经历项目失败后，作者转向规范创业项目Carbn，反思创业需警惕团队矛盾、模糊分工及过度理想化，强调创业本质是系统化解决问题而非浪漫冒险，技术成功依赖执行力与市场验证。
  - Tags: #read #career

- (2025-05-16) [I don’t like NumPy](2025-05-16-i-don%E2%80%99t-like-numpy.md)
  - 文章指出，NumPy虽简化基础数组运算，但其广播机制与维度操作规则在处理高维复杂计算（如多矩阵批量求解、多头自注意力机制）时存在设计缺陷，导致开发者需依赖晦涩的维度扩展、einsum或np.tensordot等非直观方式，易引发错误且难以维护。由于缺乏显式维度控制语法，函数抽象困难，代码可读性与灵活性受阻。作者计划开发新方案以保留计算能力并修正核心设计缺陷。
  - Tags: #read

- (2025-05-16) [Nobody Codes Here Anymore](2025-05-16-nobody-codes-here-anymore.md)
  - 某拥有12年历史的Ruby on Rails SaaS团队，现有40名开发者，允许自主选择Cursor或Claude Code等AI工具。当前近半数开发者常使用AI提升20%的开发效率，尤其在代码重构、自动化测试和功能开发场景，但面临工具兼容性差、代码冗余及人工验证成本高等挑战。团队通过规则沉淀、简化测试流程和批判性思维优化实践，同时催生「提示撰写者」新角色，推动非技术成员参与开发，但AI的动态记忆与专业知识整合能力仍待改进。
  - Tags: #read #llm

- (2025-05-14) [Vision Language Models (Better, faster, stronger)](2025-05-14-vision-language-models-%28better%2C-faster%2C-stronger%29.md)
  - 本文总结了一年内视觉语言模型（VLM）的核心进展：新型Any-to-any架构的跨模态模型支持多任务交互，混合专家（MoE）结构优化计算效率，小型化模型（如SmolVLM、Gemma3）实现本地运行。专业能力扩展至视觉任务处理、多模态安全过滤及文档检索（如DSE）。代理工具（smolagents、UI-TARS）结合VLM实现自动化任务交互。视频模型引入动态帧率与时序技术。通过DPO优化对齐，新基准推动评估。未来方向包括轻量化设计、代理应用、视频处理优化及跨领域民主化，开源工具与标准化数据集加速落地。
  - Tags: #read #llm

- (2025-05-13) [How to title your blog post or whatever](2025-05-13-how-to-title-your-blog-post-or-whatever.md)
  - 本文指出，标题作为内容分类器需精准定位目标受众，通过领域术语或风格匹配增强吸引力并过滤无关人群，避免盲目模仿他人或过早预设立场。需平衡新兴概念风险与简洁直接的表达方式，建议先确定标题再构建内容，确保承诺内容兑现。社交媒体算法的分发局限性下，优质标题需兼顾信息性、相关性及受众适配度，如案例所示。
  - Tags: #read

- (2025-05-11) [Making PyPI's test suite 81% faster](2025-05-11-making-pypi%27s-test-suite-81%25-faster.md)
  - Trail of Bits与PyPI通过并行测试（pytest-xdist）、Python3.12的sys.monitoring覆盖率技术、精简测试路径(testpaths)及移除冗余依赖等优化，将测试执行时间缩短81%至30秒，测试用例数反增20%（4700条）。优化平衡了性能与安全（100%覆盖率），并感谢社区对数据库同步和DNS缓存的改进贡献。
（99字）
  - Tags: #read #perf

- (2025-05-11) [Mission Impossible: Managing AI Agents in the Real World](2025-05-11-mission-impossible-managing-ai-agents-in-the-real-world.md)
  - 文章强调规划为核心，90%精力用于需求拆解与迭代优化，结合高质量输入（文档、代码）及工具技巧（如@mention引用规则）约束AI；分步执行并人工验证，避免模糊需求生成低质代码；建立规则文件与架构文档控制AI行为，及时重构技术债务，平衡效率与成本，始终以人工干预为主导，规避模型局限性。
  - Tags: #read #llm

- (2025-05-10) [The importance of character in software engineering](2025-05-10-the-importance-of-character-in-software-engineering.md)
  - 软件工程师的成功取决于性格特质：情绪控制力、危机处理能力及技术权威下的谦逊态度至关重要。忽视性格缺陷（常因招聘侧重技术）易引发团队冲突或合作障碍，需主动培养冷静、包容及有效沟通能力，以提升工作效率与组织协作。
  - Tags: #read #career

- (2025-05-09) [rate limiter – smudge.ai blog](2025-05-09-rate-limiter-%E2%80%93-smudge.ai-blog.md)
  - 速率限制用于防止服务过载，确保公平性与稳定性。主要算法包括：固定窗口法（简单但允许突发流量）、滑动窗口法（平滑流量但资源消耗高）、令牌桶算法（支持突发且控制长期平均速率）。实现时需使用持久化存储（如Redis）、设计容错机制（链路失败启用开放策略）、选择用户标识（IP/设备指纹等），并返回429状态码及剩余配额。建议根据场景选择：简单场景用固定窗口，高并发场景选滑动窗口近似算法，需平衡突发与长期流量则用令牌桶。
  - Tags: #deepdive #explain #visual

- (2025-05-09) [Are you more likely to die on your birthday?](2025-05-09-are-you-more-likely-to-die-on-your-birthday.md)
  - 基于美国马萨诸塞州1990-2024年近200万死亡数据研究显示，生日当天存在显著超额死亡率（+7.0%），经季节性调整后仍高度显著（z=5，p<0.000001）。分析指出这与心理因素（如"死亡周年反应"）及庆祝时饮酒等高风险行为相关，意外死亡生日当天激增35%。研究发现老年人中效应更显著，但与既往结论差异或因数据分层标准不同。通过长期数据合并控制季节性波动后趋势稳定，但+12天的次高值需更大样本验证。该发现表明死亡率受社会文化行为影响，研究方法的严谨性直接影响结论可靠性。
  - Tags: #read

- (2025-05-09) [Reservoir Sampling](2025-05-09-reservoir-sampling.md)
  - 水库抽样是一种在数据流中实现公平抽样的算法，适用于未知数据总量的场景。其核心是对第个元素以（抽1个）或（抽个）的概率动态替换已有样本，确保每个元素被选中的概率均等。该算法内存恒定，常用于日志服务等需实时处理且限制存储的场景，在流量平稳时保留全部数据，高峰时丢弃冗余信息，但存在分块传输的时延缺陷。实际应用需结合加权或优先级规则，以应对复杂需求。
  - Tags: #deepdive #explain #visual

- (2025-05-09) [Claude’s System Prompt: Chatbots Are More Than Just Models](2025-05-09-claude%E2%80%99s-system-prompt-chatbots-are-more-than-just-models.md)
  - 这篇文章分析了Claude的超长系统提示词（16,739词），揭示其设计核心：80%内容为工具使用规范（如搜索工具参数设置），包含热修复指令解决模型缺陷（如统计验证、时事更新），并采用模块化工具分离设计，但文本维护缺乏系统性。这凸显聊天机器人需依赖提示词与工具集成持续优化，但复杂流程的高效管理仍是关键挑战。
  - Tags: #read #llm

- (2025-05-09) [Microservices Are a Tax Your Startup Probably Can’t Afford](2025-05-09-microservices-are-a-tax-your-startup-probably-can%E2%80%99t-afford.md)
  - 文章指出，过早采用微服务会因部署复杂、环境脆弱、重复配置等增加团队负担。初创公司应优先选择单体架构，通过模块化和测试管理内部复杂性，仅在面临真实扩展瓶颈时拆分。避免盲目追求架构“干净”，专注核心业务，减少技术债务。
  - Tags: #read #arch

- (2025-05-08) [What Even Is Vibe Coding?](2025-05-08-what-even-is-vibe-coding.md)
  - Vibe Coding是AI通过自然指令生成代码的新兴开发范式，兼具快速原型设计优势与代码严谨性争议。技术社区对其效率与专业性的分歧显著，但工具演进已使其成为广义AI辅助开发模式。开发者逐渐依赖AI生成框架并聚焦创意决策，但需把控代码质量与伦理风险。文章认为该模式标志着开发范式向人机协作的转变，倡导在效率与规范间平衡，确保技术发展符合工程伦理。
  - Tags: #read #llm

- (2025-05-07) [An year of the Linux Desktop](2025-05-07-an-year-of-the-linux-desktop.md)
  - 2025年作者尝试以Fedora替代Windows，因Copilot干扰和隐私问题推动。选用AMD Ryzen 9与RX 9070 XT硬件，初期遭遇驱动兼容故障，后升级Fedora 42 Beta并手动修复XWayland权限问题，解决图形应用崩溃。Steam需禁用iGPU，但FF14仍存休眠崩溃隐患。NAS挂载配置失误间接导致系统不稳定，修正后环境趋于稳定。文章指出Linux办公游戏可行性提升，但硬件更新延迟、配置细节易引发问题，适合愿自主调试的技术爱好者。
  - Tags: #read #linux

- (2025-05-06) [Async Rust can be a pleasure to work with (without `Send + Sync + 'static`)](2025-05-06-async-rust-can-be-a-pleasure-to-work-with-%28without-%60send-%2B-sync-%2B-%27static%60%29.md)
  - 在Rust异步编程中，通过结构化并发和线程每核心模型可规避对++'static依赖。结构化并发自动管理子任务生命周期，简化资源清理与错误处理；绑定单线程的运行时（如Glommio）无需任务实现，降低代码复杂度。实验表明，轻量任务场景下该模式性能更优，但负载不均时工作窃取模式（如Tokio）更适用。现有框架多强制+'static要求，需探索新方案实现开发效率与性能的平衡。
  - Tags: #read #rust

- (2025-05-06) [Dummy's Guide to Modern Samplers](2025-05-06-dummy%27s-guide-to-modern-samplers.md)
  - 本文介绍了文本生成模型中Token化技术及采样算法的核心原理。Token化通过子词分割（如BPE、SentencePiece）平衡词汇覆盖率与模型效率。采样阶段结合温度调控（调整分布）、惩罚机制（防重复）、过滤方法（Top-K/P/Min-P）控制生成多样性，进阶技术如DRY可阻止n-gram重复，需注意采样器执行顺序优化。新兴的二次采样和动态温控方法进一步提升生成质量。
  - Tags: #deepdive #llm

- (2025-05-06) [一千次失败之后，它选中了你看到的那一个](2025-05-06-%E4%B8%80%E5%8D%83%E6%AC%A1%E5%A4%B1%E8%B4%A5%E4%B9%8B%E5%90%8E%EF%BC%8C%E5%AE%83%E9%80%89%E4%B8%AD%E4%BA%86%E4%BD%A0%E7%9C%8B%E5%88%B0%E7%9A%84%E9%82%A3%E4%B8%80%E4%B8%AA.md)
  - 当前AI尚不具备人类创造力，但其通过快速生成大量方案并实时筛选，将传统线性创作流程重构为开放式系统演化模式。时空维度的压缩与扩展使创意验证进入分钟级动态优化，人类角色转向系统架构师，负责设定边界、解析数据并制定价值标准，需从经验依赖转向环境调控，与AI协同推动涌现式创新。
  - Tags: #read #llm

- (2025-05-06) [Getting things "done" in large tech companies](2025-05-06-getting-things-done-in-large-tech-companies.md)
  - 在大型科技公司中，“完成”项目的核心在于取得决策者认可后及时转向，而非极致优化。关键为：1. 达到“满意”标准即可停止，避免因过度调整被视作低效；2. 技术人员需警惕陷入持续改进的陷阱，优先创造管理层可见的价值；3. 成果须显性化（如盈利、解决问题），而非隐形的技术优化。因其价值判定本质依赖管理层主观认知，忽视此规则可能影响职业发展。员工应专注交付可量化成果，制定“完成清单”而非追求完美，以持续创造最大价值。
  - Tags: #read #career

- (2025-05-04) [Functional HTML — overreacted](2025-05-04-functional-html-%E2%80%94-overreacted.md)
  - 该技术通过函数化自定义标签和JSON结构化转换，实现全栈组件协作。支持异步数据处理、双向函数引用（客户端/服务端标记生成API或路径标识），并采用流式渲染和智能缓存，减少页面弹跳，提升性能。全栈组件闭环设计和灵活的渲染模式（延迟或渐进），优化了开发体验与效率。
  - Tags: #read #deepdive #frontend
