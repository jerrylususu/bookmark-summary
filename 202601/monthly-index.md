# 2026-01 Monthly Index

- (2026-01-31) [My Favorite Self-Hosted Apps Launched in 2025](2026-01-31-my-favorite-self-hosted-apps-launched-in-2025.md)
  - 本文基于2025年自托管应用筛选，从约900个新应用中挑选出20个突出应用，涵盖Docker管理、PDF工具、书籍管理、笔记应用等领域，这些应用以概念、质量或设计见长。
  - Tags: #read

- (2026-01-31) [Guest Post: How I Scanned all of GitHub’s “Oops Commits” for Leaked Secrets ◆ Truffle Security Co.](2026-01-31-guest-post-how-i-scanned-all-of-github%E2%80%99s-%E2%80%9Coops-commits%E2%80%9D-for-leaked-secrets-%E2%97%86-truffle-security-co..md)
  - 本文介绍了如何扫描GitHub上因强制推送删除的提交（Oops Commits）以发现泄露的秘密。作者开发了开源工具Force Push Scanner，通过分析GitHub Archive数据，成功检测出价值约25,000美元的漏洞赏金秘密，强调秘密一旦提交就必须立即撤销，并呼吁开发者提高安全意识。
  - Tags: #read #deepdive #security

- (2026-01-31) [Selectively Disabling HTTP/1.0 and HTTP/1.1 - Mark McBride](2026-01-31-selectively-disabling-http-1.0-and-http-1.1---mark-mcbride.md)
  - 文章总结Mark McBride选择性禁用HTTP/1.X的经验。启用HTTP/3后，恶意流量多通过HTTP/1.X传输。作者实验两种方法：排除法（排除坏用户代理）比包含法更灵活，能有效减少恶意请求，建议结合日志监控和速率限制以平衡安全与可用性。
  - Tags: #read #network

- (2026-01-31) [How does AI impact skill formation?](2026-01-31-how-does-ai-impact-skill-formation.md)
  - 论文发现AI用户完成任务速度未提升且技能下降，主要因半数用户无效使用AI；剔除后速度可提高25%。学习效果在适度使用AI时较好，完全依赖则差。作者认为AI加速交付价值更重要，建议研究长期使用模式。
  - Tags: #read #llm

- (2026-01-31) [Automatic programming - <antirez>](2026-01-31-automatic-programming---antirez.md)
  - 本文介绍自动编程概念，即AI辅助编程中人类通过愿景和引导发挥核心作用。作者区分自动编程与用户参与度低的氛围编程，强调高质量软件需严格遵循用户意图，生成代码可视为用户产物。以Redis为例，说明软件成功依赖创意。结论是编程自动化，但愿景仍需人类主导。
  - Tags: #read #llm

- (2026-01-29) [Some notes on starting to use Django](2026-01-29-some-notes-on-starting-to-use-django.md)
  - Julia Evans分享了学习Django框架的积极体验，赞赏其显式文件结构、强大ORM、自动迁移和丰富内置功能，文档质量高。尽管对settings.py的全局变量设计略有担忧，但总体满意，计划继续探索表单验证等特性。
  - Tags: #read #tips #python

- (2026-01-29) [We have a Discord now. You can view the Q&A from Google. | Tigris Object Storage](2026-01-29-we-have-a-discord-now.-you-can-view-the-q%26a-from-google.-tigris-object-storage.md)
  - Tigris Data 使用 ETL 框架将论坛问答数据迁移到 Discord，通过 AI 处理文本和生成头像，集成 Answer Overflow 实现公开搜索，成功提升社区参与度。
  - Tags: #read

- (2026-01-29) [From pixels to characters: The engineering behind GitHub Copilot CLI’s animated ASCII banner](2026-01-29-from-pixels-to-characters-the-engineering-behind-github-copilot-cli%E2%80%99s-animated-ascii-banner.md)
  - GitHub Copilot CLI 团队开发动画ASCII横幅，面临终端环境限制如颜色不一致和可访问性挑战。他们利用自定义工具和TypeScript代码处理动画与兼容性，最终实现可维护架构并开源工具，为CLI开发提供宝贵经验。
  - Tags: #read #design #deepdive

- (2026-01-28) [How to do Parallelization Right with Promise.all](2026-01-28-how-to-do-parallelization-right-with-promise.all.md)
  - 在JavaScript中，错误地在Promise.all中使用await会导致并行化失效，代码顺序执行。正确做法是直接传递Promise，或使用parallelize函数进行类型检查，以提升性能并避免错误。
  - Tags: #read #tips

- (2026-01-28) [Management as AI superpower](2026-01-28-management-as-ai-superpower.md)
  - 基于宾大实验，EMBA学生利用AI工具在四天内快速创建初创原型。AI委托决策需权衡任务时间、成功率和处理时间。管理技能如清晰指令和评估能提升AI效率，成为AI时代的核心优势，预示未来工作可能转向管理AI代理。
  - Tags: #read #llm

- (2026-01-28) [One Human + One Agent = One Browser From Scratch](2026-01-28-one-human-%2B-one-agent-%3D-one-browser-from-scratch.md)
  - 本文记录作者与LLM代理在三天内合作开发跨平台浏览器的经历，支持HTML/CSS渲染，代码超2万行。实验表明一人一代理模式高效，协作质量比代理数量更重要。
  - Tags: #read #agent

- (2026-01-27) [Tips for getting coding agents to write good Python tests](2026-01-27-tips-for-getting-coding-agents-to-write-good-python-tests.md)
  - 本文分享了让AI代理编写高质量Python测试的技巧，包括选择Python语言利用丰富数据、使用pytest工具优化代码、在良好测试环境中促进学习，以及模仿现有项目模式。
  - Tags: #read #llm #guide

- (2026-01-26) [State of the Windows: What is going on with Windows 11?](2026-01-26-state-of-the-windows-what-is-going-on-with-windows-11.md)
  - 文章批评Windows 11自2023年质量下降，更新频发错误、系统臃肿运行慢、AI功能强制集成但实用性低，微软被指忽视用户体验，呼吁回归稳定可靠系统。
  - Tags: #read

- (2026-01-26) [the browser is the sandbox](2026-01-26-the-browser-is-the-sandbox.md)
  - 文章探讨浏览器作为沙箱运行AI自动化任务的安全潜力，通过文件系统API、内容安全策略和代码隔离机制（如Web Workers）来降低风险。作者以Co-do项目为例指出浏览器沙箱可行，但需厂商改进以提升安全性。
  - Tags: #read #llm #deepdive

- (2026-01-26) [You have to know how to drive the car](2026-01-26-you-have-to-know-how-to-drive-the-car.md)
  - 本文以“开车”为喻，强调软件工程师必须理解公司内部政治和流程，才能实现晋升、工作平衡或用户价值等目标。若不掌握，可能失败或被边缘化；唯一避免方式是离开大公司，但会失去影响力。留下则必须学习运作机制。
  - Tags: #read #career

- (2026-01-25) [The Value of Things – journal.stuffwithstuff.com](2026-01-25-the-value-of-things-%E2%80%93-journal.stuffwithstuff.com.md)
  - 文章探讨生成式 AI 对价值的影响，区分效用（实用性）和意义（情感价值）。AI 能提升效用效率，但会稀释意义。建议在实用任务中使用 AI，在情感连接中避免依赖，以平衡价值。
  - Tags: #read

- (2026-01-24) [Common misunderstandings about large software companies – Vallified](2026-01-24-common-misunderstandings-about-large-software-companies-%E2%80%93-vallified.md)
  - Philip O'Toole的文章反驳了对大型软件公司的常见误解。作者指出，批评者常忽略规模带来的结构性原因：会议多为协调必需，高管主导是决策关键，流程确保可靠性。这些是组织逻辑的体现，应先理解运作逻辑而非简单指责。
  - Tags: #read

- (2026-01-24) [Light Mode InFFFFFFlation — Will Richardson](2026-01-24-light-mode-infffffflation-%E2%80%94-will-richardson.md)
  - 文章分析MacOS界面亮度从2009年Snow Leopard起逐年上升，设计师偏好亮色致界面过亮，用户被迫使用深色模式。作者建议采用50%灰色以改善视觉舒适度，并呼吁回归平衡设计。
  - Tags: #read #design

- (2026-01-24) [Personal infrastructure setup 2026](2026-01-24-personal-infrastructure-setup-2026.md)
  - Morten Linderud在2026年的个人基础设施设置旨在自托管邮件、博客等服务，使用Incus管理容器和虚拟机，Opentofu实现自动化。硬件包括NAS和NUC设备，网络通过WireGuard VPN和Nginx代理解决ISP限制。设置强调简单可靠，代码开源供学习。
  - Tags: #read

- (2026-01-24) [A Few Things About the Anchor Element’s href You Might Not Have Known](2026-01-24-a-few-things-about-the-anchor-element%E2%80%99s-href-you-might-not-have-known.md)
  - 文章探讨了HTML锚元素href属性的多种用法，包括协议链接、特殊值行为（如href="#"滚动到顶部）、数据URL和媒体片段等，作者通过JavaScript测试验证了这些行为的准确性。
  - Tags: #read #frontend

- (2026-01-24) [How I estimate work as a staff software engineer](2026-01-24-how-i-estimate-work-as-a-staff-software-engineer.md)
  - 文章作者指出软件项目估算本质上不可行，因未知工作占主导，无法精确预测。估算实为组织政治工具，用于资源协商；作者建议通过风险分析和多方案评估来支持决策，而非追求准确时间。
  - Tags: #read #career

- (2026-01-23) [Why read novels?](2026-01-23-why-read-novels.md)
  - 文章探讨阅读小说的价值，作者通过多个理论分析，如提升心灵空间、减少被动消费等，认为没有单一原因，但阅读能带来积极体验，促进主动思考。
  - Tags: #read

- (2026-01-23) [Interfaces and traits in C](2026-01-23-interfaces-and-traits-in-c.md)
  - 本文探讨了在C语言中实现类似Go和Rust接口多态的方法，比较了多种实现方式，推荐使用方法表（vtable）作为高效安全的实用方案，尽管不如原生语言优雅。
  - Tags: #read #c #deepdive

- (2026-01-23) [Previewing Claude Code for web branches with GitHub Pages](2026-01-23-previewing-claude-code-for-web-branches-with-github-pages.md)
  - 作者西蒙·威利森通过GitHub Pages部署私有仓库分支，解决了在Claude Code中开发HTML时预览困难的问题。该方法支持持续会话、自动刷新预览，且无时间限制，实用方便。
  - Tags: #read #tips

- (2026-01-23) [SSH has no Host header - exe.dev blog](2026-01-23-ssh-has-no-host-header---exe.dev-blog.md)
  - exe.dev平台SSH协议缺乏Host头，无法区分虚拟机。解决方案是采用共享IPv4地址池，通过DNS CNAME记录和用户公钥与IP组合路由连接。该定制方案确保域名行为一致，适用于其特定需求。
  - Tags: #read #hack

- (2026-01-22) [The Product-Minded Engineer: The importance of good errors and warnings](2026-01-22-the-product-minded-engineer-the-importance-of-good-errors-and-warnings.md)
  - 本文强调产品导向工程师需重视错误警告设计。在AI时代，清晰、可操作的消息能提升用户体验、减少成本，通过系统分类、早期验证实现。书中建议工程师培养产品意识，构建健壮产品。
  - Tags: #read #deepdive

- (2026-01-22) [Codeless: From idea to software - Anil Dash](2026-01-22-codeless-from-idea-to-software---anil-dash.md)
  - 无代码技术通过AI编排编码机器人，基于英语描述自动生成软件。核心创新是编排和容错机制，特点包括开源免费、处理AI幻觉。它能赋权个人，提高创新效率，但面临设置复杂、成本高等挑战，有潜力重塑软件开发。
  - Tags: #read #llm

- (2026-01-21) [AI-supported vulnerability triage with the GitHub Security Lab Taskflow Agent](2026-01-21-ai-supported-vulnerability-triage-with-the-github-security-lab-taskflow-agent.md)
  - GitHub Security Lab 开发了基于 AI 的漏洞分类方法，利用开源 Taskflow Agent 和 LLM 自动化处理 CodeQL 警报。通过分解任务步骤，减少了假阳性，自 2025 年 8 月以来发现约 30 个真实漏洞。相关代码开源，支持社区扩展。
  - Tags: #read #guide

- (2026-01-21) [Giving University Exams in the Age of Chatbots](2026-01-21-giving-university-exams-in-the-age-of-chatbots.md)
  - 文章介绍作者在大学课程中创新的考试方式：允许使用所有资源，包括聊天机器人，但需负责任声明。学生大多不使用聊天机器人，成绩更优。考试强调协作和思考过程记录，促进学习。作者反思技术使用，主张教育应鼓励负责任创新。
  - Tags: #read

- (2026-01-20) [The Art of Nested Code Fencing in Markdown - Susam Pal](2026-01-20-the-art-of-nested-code-fencing-in-markdown---susam-pal.md)
  - Susam Pal的文章探讨了如何在CommonMark和GFM Markdown中安全嵌套代码块分隔符，如三重反引号。通过使用代字号或多重反引号作为分隔符，避免渲染错误，帮助用户正确展示代码示例。基于CommonMark规范。
  - Tags: #read #tips

- (2026-01-20) [LocSend · 局域网极速传文件与消息](2026-01-20-locsend-%C2%B7-%E5%B1%80%E5%9F%9F%E7%BD%91%E6%9E%81%E9%80%9F%E4%BC%A0%E6%96%87%E4%BB%B6%E4%B8%8E%E6%B6%88%E6%81%AF.md)
  - LocSend 是一款基于 WebRTC 的快速文件传输工具，支持局域网或 IPv6 公网的点对点传输，无需注册和云服务器，采用端到端加密确保安全。提供离线版和在线版，适合不同场景，兼容多平台和多种文件类型。
  - Tags: #tools

- (2026-01-20) [I'm addicted to being useful](2026-01-20-i%27m-addicted-to-being-useful.md)
  - 文章探讨软件工程师的内在驱动力：作者自称沉迷于被需要和解决问题的满足感，引用文学比喻说明工作与个人特质的契合，建议通过时间管理和专注核心任务来驾驭这种内部强迫。
  - Tags: #read #career

- (2026-01-19) [从“代码补全”到“全托管 Agent”：我的 2025 AI Coding 进化论 - 白宦成](2026-01-19-%E4%BB%8E%E2%80%9C%E4%BB%A3%E7%A0%81%E8%A1%A5%E5%85%A8%E2%80%9D%E5%88%B0%E2%80%9C%E5%85%A8%E6%89%98%E7%AE%A1-agent%E2%80%9D%EF%BC%9A%E6%88%91%E7%9A%84-2025-ai-coding-%E8%BF%9B%E5%8C%96%E8%AE%BA---%E7%99%BD%E5%AE%A6%E6%88%90.md)
  - 白宦成分享2025年使用AI编码工具的经历，强调L3 Agent模式提升效率、降低开发门槛。作者建议工程师适应角色转变，从代码Review起步，确保AI生成代码质量。用好AI工具是未来发展的关键。
  - Tags: #read #llm #agent

- (2026-01-18) [A Social Filesystem — overreacted](2026-01-18-a-social-filesystem-%E2%80%94-overreacted.md)
  - Dan Abramov探讨社交文件系统概念，主张将社交数据视为文件，通过AT协议实现用户数据所有权和开放互操作，类似传统文件系统的自由与兼容性。
  - Tags: #read #distributed #deepdive

- (2026-01-17) [My Claude Code Workflow And Personal Tips](2026-01-17-my-claude-code-workflow-and-personal-tips.md)
  - 本文介绍作者使用Claude Code和Cursor的AI编码工作流程，核心是通过ROADMAP.md文件进行结构化规划，结合任务管理和实用技巧，提升开发效率。
  - Tags: #read #llm #guide

- (2026-01-17) [Minimal GitHub Workflow - Susam Pal](2026-01-17-minimal-github-workflow---susam-pal.md)
  - 本文通过逐步实验，从空文件开始构建GitHub工作流，最终成功运行"hello, world"示例。关键发现是：最小配置需包含on事件触发器、jobs定义、job ID、runs-on环境、steps步骤和run命令。
  - Tags: #read

- (2026-01-17) [The Most Important Teams in Tech](2026-01-17-the-most-important-teams-in-tech.md)
  - 在B2B软件公司中，工程和销售团队是核心：工程负责产品构建，销售驱动增长；其他团队需提供支持。核心团队必须持续改进，避免失败风险。
  - Tags: #read #career

- (2026-01-17) [The natural home for AI agents is your Reminders app](2026-01-17-the-natural-home-for-ai-agents-is-your-reminders-app.md)
  - 文章探讨AI代理的协调问题，建议通过扩展苹果Reminders等提醒应用作为共享任务管理器，使AI代理能读写任务、处理子任务，从而降低行政负担并提升效率。
  - Tags: #read #agent

- (2026-01-17) [The Design & Implementation of Sprites](2026-01-17-the-design-%26-implementation-of-sprites.md)
  - Sprites 是 Fly.io 推出的新型 Linux 虚拟机，设计为一次性计算机，具有秒级创建、持久存储和低成本特性。其实现基于无容器镜像、对象存储和内部编排，适用于原型开发和交互式任务，与 Fly Machines 互补，未来可无缝转换到生产环境。
  - Tags: #read #arch #deepdive

- (2026-01-16) [Tormentmaxxing 'simple requests'](2026-01-16-tormentmaxxing-%27simple-requests%27.md)
  - 本文探讨了深度工作被打断导致效率损失的问题，尤其在创业公司环境中。作者提出“tormentmaxxing”概念，利用AI工具自动化任务以减少中断，尽管对AI伦理有顾虑，但强调智能工作的重要性。
  - Tags: #read #llm

- (2026-01-15) [What came first- the CNAME or the A record](2026-01-15-what-came-first--the-cname-or-the-a-record.md)
  - 2026年1月，Cloudflare因优化代码意外改动CNAME记录顺序，导致部分DNS客户端解析失败。问题源于RFC对记录顺序规定模糊，旧客户端依赖固定顺序解析。事后Cloudflare恢复原有顺序，并向IETF提交草案推动标准化。
  - Tags: #read #network

- (2026-01-14) [How to write a good spec for AI agents](2026-01-14-how-to-write-a-good-spec-for-ai-agents.md)
  - 本文提出了一套为AI代理编写规格说明的框架，强调通过四方面设计高质量文档：从高层愿景出发逐步细化、采用结构化文档分领域覆盖需求、模块化拆分任务以避免指令过载、以及内置约束与领域知识以提升质量。核心在于平衡指导清晰度和计算负载，使AI在边界内高效工作。
  - Tags: #read #llm #guide

- (2026-01-14) [Monky Business: Creating a Cistercian Numerals Generator | Christian Heilmann](2026-01-14-monky-business-creating-a-cistercian-numerals-generator-christian-heilmann.md)
  - 本文介绍了西多会数字生成器的开发，该系统能将1-9999的数字转换为基于线条组合的字符。生成器提供在线工具和时钟应用，支持多种输出格式。开发过程通过手动分析符号结构实现核心逻辑，代码开源可用。
  - Tags: #read

- (2026-01-14) [Porting MiniJinja to Go With an Agent](2026-01-14-porting-minijinja-to-go-with-an-agent.md)
  - 作者通过AI代理在约45分钟内将MiniJinja从Rust移植到Go，使用测试驱动方法完成核心功能。过程中AI灵活调整设计以符合Go习惯，作者在细节上少量干预。移植成本约60美元，作者认为AI降低了跨语言门槛，但削弱了社区贡献的意义。
  - Tags: #read #llm #agent

- (2026-01-13) [How to know if that job will crush your soul - Anil Dash](2026-01-13-how-to-know-if-that-job-will-crush-your-soul---anil-dash.md)
  - 文章提出七个评估工作机会的关键问题：从社会价值、资金来源、核心假设、员工体验、纠错能力、实际薪酬到职业发展，帮助求职者全面判断职位是否值得选择，强调坚持高标准以避免职业风险。
  - Tags: #read #career

- (2026-01-11) [Don't fall into the anti-AI hype - <antirez>](2026-01-11-don%27t-fall-into-the-anti-ai-hype---antirez.md)
  - AI将彻底改变编程，从手动写代码转向理解问题并指导AI生成代码，效率极大提升。作者认为AI不可逆转，呼吁积极适应以提升效率，同时关注技术垄断和就业冲击等社会问题，需政策配合实现平衡发展。
  - Tags: #read #llm

- (2026-01-11) [A Survey of Dynamic Array Structures](2026-01-11-a-survey-of-dynamic-array-structures.md)
  - 文章系统比较了六类动态数组结构，包括双倍复制数组、内存池数组、分块数组、链接块数组、树结构数组和指数数组，分析了各自的设计特点、优缺点及适用场景。作者倾向于使用内存池管理，强调需根据数据连续性、指针稳定性和内存效率等需求权衡选择。
  - Tags: #read #deepdive

- (2026-01-11) [Writing First, Tooling Second - Susam's Maze](2026-01-11-writing-first%2C-tooling-second---susam%27s-maze.md)
  - 建立个人网站应优先写作而非纠结工具选择。从纯HTML起步，发布至少5篇文章后再考虑工具优化，避免过度工程化。内容是核心，工具应服务于表达而非取代创作。
  - Tags: #read

- (2026-01-11) [A Software Library with No Code](2026-01-11-a-software-library-with-no-code.md)
  - 作者提出“无代码”软件库（如whenwords），仅依赖规格说明和测试用例，通过AI自动生成代码。这种方法适合简单工具，但复杂、高性能或需社区支持的场景仍需传统代码库。AI或改变编码方式，但代码实现和社区价值不会消失。
  - Tags: #read

- (2026-01-10) [John Carmack on Inlined Code](2026-01-10-john-carmack-on-inlined-code.md)
  - 约翰·卡马克认为内联代码能减少状态依赖和bug，提升可读性与性能。建议优先内联单次调用函数，用注释分隔代码块，并注重纯函数与一致性执行路径。需根据场景权衡内联与模块化，特别适用于游戏开发等实时系统。
  - Tags: #read #design

- (2026-01-10) [A complete guide to the HTML number input](2026-01-10-a-complete-guide-to-the-html-number-input.md)
  - 本文全面介绍了HTML数字输入框的特性、使用方法和注意事项，包括如何自定义按钮、处理本地化、验证数据和移动端支持，强调在现代浏览器中合理使用可以提升用户体验。
  - Tags: #read #deepdive #frontend

- (2026-01-10) [Fly’s new Sprites.dev addresses both developer sandboxes and API sandboxes at the same time](2026-01-10-fly%E2%80%99s-new-sprites.dev-addresses-both-developer-sandboxes-and-api-sandboxes-at-the-same-time.md)
  - Fly.io推出Sprites.dev，提供持久化沙盒环境与API服务，支持快速创建、检查点回滚和安全运行代码。旨在通过按需计费和隔离环境，为开发者及API用户提供安全、经济的沙盒解决方案。
  - Tags: #read #llm #security

- (2026-01-09) [HTTP caching, a refresher · Dan Cătălin Burzo](2026-01-09-http-caching%2C-a-refresher-%C2%B7-dan-c%C4%83t%C4%83lin-burzo.md)
  - 本文基于RFC 9111标准，解析了HTTP缓存的运行机制，包括缓存新鲜度判断、存储控制、关键Cache-Control指令及其应用场景。文章强调缓存默认启用，但需结合浏览器和中间件的实际兼容性谨慎配置。
  - Tags: #read #deepdive

- (2026-01-09) [Why Object of Arrays (SoA pattern) beat interleaved arrays: a JavaScript performance rabbit hole | Royal Bhati's Blog](2026-01-09-why-object-of-arrays-%28soa-pattern%29-beat-interleaved-arrays-a-javascript-performance-rabbit-hole-royal-bhati%27s-blog.md)
  - 通过对比数组结构（AoS）和结构数组（SoA）在JavaScript中的性能，发现SoA模式速度提升4倍，优势源于减少对象分配、优化循环和属性访问。SoA核心通过连续内存布局降低开销，更适合大数据场景。
  - Tags: #read #perf

- (2026-01-09) [Opus 4.5 is going to change everything](2026-01-09-opus-4.5-is-going-to-change-everything.md)
  - Burke Holland通过亲身体验Claude Opus 4.5 AI编码代理，认为它已能完全替代开发者，可高效完成图像转换、视频编辑、社交媒体工具等复杂项目。作者强调需转向"AI可维护"的编程范式，优化代码结构以适应AI迭代，同时警惕安全风险。
  - Tags: #read #llm

- (2026-01-09) [How Markdown took over the world - Anil Dash](2026-01-09-how-markdown-took-over-the-world---anil-dash.md)
  - Markdown是一种轻量级标记语言，2004年由John Gruber创建，旨在简化文本格式化。它因简洁、开源、恰逢博客兴起而迅速普及，成为开发者及日常工具的通用格式。其成功源于解决实际需求、开放社区协作和免费共享精神。
  - Tags: #read #deepdive #history

- (2026-01-09) [Your AI coding agents need a manager](2026-01-09-your-ai-coding-agents-need-a-manager.md)
  - 随着AI编程代理普及，开发者需转变为AI管理者的角色。关键管理技能包括清晰沟通、任务委派、验证和异步协调。文章建议先用少量代理处理后台任务，再逐步管理并行工作，重点强调查过程把控和质量验证，而非依赖工具本身。
  - Tags: #read #llm #agent

- (2026-01-07) [A field guide to sandboxes for AI](2026-01-07-a-field-guide-to-sandboxes-for-ai.md)
  - 此内容为错误页面提示，因请求过多（错误码429）无法加载博客文章，仅显示安全检查标题和令牌信息。
  - Tags: #read #deepdive #security

- (2026-01-07) [Fast Code, Expensive Confidence: Building Software With LLMs | Dmitry Danilov](2026-01-07-fast-code%2C-expensive-confidence-building-software-with-llms-dmitry-danilov.md)
  - 本文指出，LLM加速了代码生成但也增加了风险，软件架构因此更加关键。强调模块化、标准接口和强类型语言能缩小上下文范围、降低错误，同时验证和测试成为核心优势。架构确保AI生成代码的可靠迭代，而非盲目加速。
  - Tags: #read

- (2026-01-06) [Freestyle linked lists tricks](2026-01-06-freestyle-linked-lists-tricks.md)
  - 本文介绍了链表的高级优化技巧，在保持基础结构不变的前提下，通过构建哈希Trie或索引表将查找复杂度从O(n)优化到O(1)或O(log n)，适用于静态或频繁查询场景，支持多映射和遍历操作。
  - Tags: #read #c

- (2026-01-05) [21 Lessons From 14 Years at Google](2026-01-05-21-lessons-from-14-years-at-google.md)
  - 谷歌前员工总结14年职业经验，强调持续学习与团队协作。核心包括：职业成长靠积累，避免工作过度；团队合作重共识、透明与贡献可视；工程决策以用户为中心，代码清晰优先；管理需对齐目标、简化流程。整体倡导谦逊、服务用户的心态。
  - Tags: #read #guide

- (2026-01-05) [It’s hard to justify Tahoe icons](2026-01-05-it%E2%80%99s-hard-to-justify-tahoe-icons.md)
  - 作者批评macOS Tahoe新增菜单图标存在功能性、一致性和可用性缺陷，认为其违背经典设计原则，导致识别困难、逻辑混乱，并呼吁设计师避免类似错误。
  - Tags: #read #visual #design

- (2026-01-05) [Facilitating AI adoption at Imprint](2026-01-05-facilitating-ai-adoption-at-imprint.md)
  - 作者总结了18个月在内部推动AI采用的经验，强调务实迭代和领导亲身体验。关键策略包括消除采用障碍、全公司定制化部署和领导以身作则。具体措施涉及工具标准化、提示词管理、代理开发等。核心观点是AI采用需结合实际问题、持续学习和高效协作，避免形式主义。
  - Tags: #read #llm #deepdive

- (2026-01-05) [My LLM coding workflow going into 2026](2026-01-05-my-llm-coding-workflow-going-into-2026.md)
  - AI应被视为需明确指导的编程伙伴，而非全自动工具。2026年实践显示，通过分解任务、提供详细上下文、结合测试与自动化工具，并保持人工监督，可最大化AI辅助编程效率。开发者需主导工作流，并对代码质量负责。
  - Tags: #read #llm #guide

- (2026-01-05) [The future of agentic coding: conductors to orchestrators](2026-01-05-the-future-of-agentic-coding-conductors-to-orchestrators.md)
  - 文章比较了AI辅助编程的两种模式：Conductor（实时指导单一AI，控制精细但效率低）和Orchestrator（协调多个AI并行工作，自动化程度高）。未来趋势是开发者角色转向任务管理与质量审查，实现规模化开发，但人类仍需主导关键决策与创新。
  - Tags: #read #llm
