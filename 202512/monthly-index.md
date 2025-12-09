# 2025-12 Monthly Index

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
