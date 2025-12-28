# 2025-01 Monthly Index

- (2025-01-31) [The surprising way to save memory with BytesIO](2025-01-31-the-surprising-way-to-save-memory-with-bytesio.md)
  - 是Python中用于内存中存储字节数据的类。使用会导致内存使用量翻倍，而和方法则更高效，前者返回视图，后者返回对象且不增加内存。建议避免使用，优先使用或以最小化内存开销。
  - Tags: #read #py

- (2025-01-28) [DeepSeek FAQ](2025-01-28-deepseek-faq.md)
  - DeepSeek发布了多个高效AI模型，如和，通过技术创新如DeepSeekMoE和DeepSeekMLA显著降低了训练和推理成本。在芯片禁令背景下，DeepSeek优化模型架构，展示了在受限硬件上实现高性能的可能性。其开源策略与OpenAI的闭源形成对比，推动了AI模型的普及和成本降低，预示着AI领域接近通用人工智能的实现。
  - Tags: #read

- (2025-01-28) [Nomadic Infrastructure Design for AI workloads](2025-01-28-nomadic-infrastructure-design-for-ai-workloads.md)
  - 演讲者Xe分享了如何设计高效、低成本的生产级AI系统，重点讨论了计算、网络和存储的优化策略，如缩放到零、批量操作和加速冷启动。通过Docker镜像优化和游牧计算，系统可跨平台运行，减少对特定供应商的依赖。演讲还展示了按需启动GPU的现场演示，并提供了联系方式供观众提问。
  - Tags: #read

- (2025-01-27) [My failed attempt to shrink all npm packages by 5%](2025-01-27-my-failed-attempt-to-shrink-all-npm-packages-by-5%25.md)
  - 作者提出使用Zopfli压缩工具减少npm包大小的提案，实验证明可行且能减少约6.2%的大小。尽管提案被npm维护者拒绝，作者从中学会了如何提交RFC，并认识到实施改进需权衡利弊。尽管提案未通过，作者仍在自己项目中继续使用Zopfli进行优化。
  - Tags: #read

- (2025-01-27) [The Short Case for Nvidia Stock](2025-01-27-the-short-case-for-nvidia-stock.md)
  - 作者凭借丰富的投资分析和技术背景，分析了Nvidia在AI领域的强势地位及其面临的挑战。Nvidia凭借技术垄断、高利润率和强大的研发投入，在AI硬件市场占据主导地位。然而，市场竞争加剧、硬件创新和价格压力可能对其未来增长构成威胁。尽管如此，作者对Nvidia的长期前景持乐观态度，认为其将继续在AI领域发挥重要作用。
  - Tags: #read

- (2025-01-25) [Learn Yjs by Jamsocket](2025-01-25-learn-yjs-by-jamsocket.md)
  - Learn Yjs 是一个交互式教程系列，专注于使用 Yjs CRDT 库构建实时协作应用。教程涵盖基础知识、分布式状态处理、CRDT 介绍及挑战解决方案，通过互动演示和代码练习帮助用户深入理解。项目由 Jamsocket 开发，使用 Astro 和 React 构建，支持实时同步和多用户互动。
  - Tags: #books

- (2025-01-25) [OS in 1,000 Lines](2025-01-25-os-in-1%2C000-lines.md)
  - 本书介绍了如何用1000行C语言代码构建一个小型操作系统，涵盖上下文切换、分页、用户态、命令行shell、磁盘驱动和文件读写等基础功能。开发过程中调试困难但成就感强，适合熟悉C语言和类UNIX环境的读者。示例代码可在GitHub下载，书籍和代码分别基于CC BY 4.0和MIT协议。鼓励读者探索操作系统开发的乐趣。
  - Tags: #books

- (2025-01-25) [Safe Assignment | Alan Johnson](2025-01-25-safe-assignment-alan-johnson.md)
  - Alan Johnson 讨论了 JavaScript 中新的安全赋值操作符（?=）提案，旨在简化 try/catch 块中的错误处理。他实现了一个  函数，支持同步和异步操作，减少代码冗余。虽然不确定是否会实际使用，但他认为这次探索很有趣，并邀请读者反馈。
  - Tags: #read #js

- (2025-01-25) [A WebAssembly compiler that fits in a tweet](2025-01-25-a-webassembly-compiler-that-fits-in-a-tweet.md)
  - 该项目通过JavaScript实现了一个极简的WebAssembly编译器，将逆波兰表示法的算术表达式编译为WebAssembly模块。通过一系列代码优化技巧，编译器从最初的269字节优化至192字节。文章详细解析了优化过程、隐式设计决策以及未实现的优化技巧，并推荐了相关学习资源。最终，项目不仅展示了WebAssembly的内部机制，还为未来改进提供了方向。
  - Tags: #read #web

- (2025-01-25) [Working fast and slow](2025-01-25-working-fast-and-slow.md)
  - 作者分享了自己适应不同工作节奏的经验，强调接受高效日和低效日的差异。高效日专注于高优先级任务，低效日则处理简单任务。作者认为这种策略在大科技公司中尤为适用，能够有效平衡工作压力和提高生产力。
  - Tags: #read #career

- (2025-01-24) [Is TypeScript Good?—A Reply to Rach Smith — Sympolymathesy, by Chris Krycho](2025-01-24-is-typescript-good-%E2%80%94a-reply-to-rach-smith-%E2%80%94-sympolymathesy%2C-by-chris-krycho.md)
  - 文章讨论了TypeScript在JavaScript开发中的实用性，强调了其错误捕捉、代码可持续性和系统“库存”提升的价值。作者Chris Krycho认同TypeScript可能引发“聪明代码”陷阱，但也指出其在提高代码质量和未来扩展能力方面的优势。文章建议在引入TypeScript时平衡短期功能交付和长期维护投入，强调其对代码库长期可持续性的重要性。
  - Tags: #read #design

- (2025-01-24) [Why are big tech companies so slow?](2025-01-24-why-are-big-tech-companies-so-slow.md)
  - 大公司开发速度慢的主要原因是功能数量庞大且复杂，新功能与现有功能的交互增加了开发难度。尽管减少功能可能简化开发，但大公司依赖功能驱动收入，因此更关注边际功能的开发。复杂性导致认知负担增加，开发速度变慢，但大公司仍愿意为高薪支付以捕获边际价值。
  - Tags: #read

- (2025-01-24) [The Essence of Successful Abstractions — Sympolymathesy, by Chris Krycho](2025-01-24-the-essence-of-successful-abstractions-%E2%80%94-sympolymathesy%2C-by-chris-krycho.md)
  - 文章探讨了软件开发中复杂性的不可避免性，并介绍了如何通过类型系统、测试、Rust和TypeScript等工具来管理和隔离复杂性。Rust通过类型系统和借用检查器隔离复杂性，而TypeScript则揭示并帮助管理现有复杂性。文章强调了复杂性隔离的价值，尽管并非总能实现，但它有助于提高开发效率和代码质量。
  - Tags: #read

- (2025-01-22) [AI Mistakes Are Very Different from Human Mistakes - Schneier on Security](2025-01-22-ai-mistakes-are-very-different-from-human-mistakes---schneier-on-security.md)
  - AI错误与人类错误有显著差异，表现为随机性和怪异性，且不伴随无知。应对AI错误需要新的安全系统和研究方向，如使AI错误更接近人类错误或建立专门的错误纠正系统。理解AI错误的相似性和差异性有助于更好地设计和应用AI系统。
  - Tags: #read #llm

- (2025-01-21) [ What I've learned about writing AI apps so far | Seldo.com](2025-01-21-what-i%27ve-learned-about-writing-ai-apps-so-far-seldo.com.md)
  - 作者分享了基于大语言模型（LLM）开发AI应用的经验，强调LLM本质上是高级的文本压缩工具，擅长将大量文本转化为简洁内容，但在生成长文本或复杂任务时表现有限。开发者应明确LLM的局限性，优先使用常规编程，避免过度依赖其能力。LLM无法替代人类工作，合理设计应用场景是关键。
  - Tags: #read #llm

- (2025-01-19) [Protecting your time from predators in large tech companies](2025-01-19-protecting-your-time-from-predators-in-large-tech-companies.md)
  - 在大型科技公司中，软件工程师需要谨慎管理时间，避免被“时间掠夺者”利用。帮助他人虽有益，但不应影响核心项目责任。识别并应对低努力请求，保护时间，专注于主要工作。
  - Tags: #read #people

- (2025-01-18) [一个副业应用的开发心得](2025-01-18-%E4%B8%80%E4%B8%AA%E5%89%AF%E4%B8%9A%E5%BA%94%E7%94%A8%E7%9A%84%E5%BC%80%E5%8F%91%E5%BF%83%E5%BE%97.md)
  - 诗鲸是一款专注于诗词学习的Android应用，主要面向学生群体，提供诗词查找、推荐等功能。应用采用订阅收费模式，初期收入较好，后期趋于稳定。开发过程中面临版权、支付、推广等挑战，未来计划尝试独立开发新项目。
  - Tags: #read #deepdive

- (2025-01-16) [布局 2025：我的时间管理三原则 - 少数派](2025-01-16-%E5%B8%83%E5%B1%80-2025%EF%BC%9A%E6%88%91%E7%9A%84%E6%97%B6%E9%97%B4%E7%AE%A1%E7%90%86%E4%B8%89%E5%8E%9F%E5%88%99---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 文章介绍了三个时间管理原则：根据能量等级安排任务、主动规划时间而非依赖截止日期、快速验证避免完美主义。作者建议通过记录能量等级、任务批处理和工具使用来提高效率，最终目标是高效完成重要事项并享受生活。
  - Tags: #read

- (2025-01-15) [「君の名は。」の二人は例の階段で出会えるのか](2025-01-15-%E3%80%8C%E5%90%9B%E3%81%AE%E5%90%8D%E3%81%AF%E3%80%82%E3%80%8D%E3%81%AE%E4%BA%8C%E4%BA%BA%E3%81%AF%E4%BE%8B%E3%81%AE%E9%9A%8E%E6%AE%B5%E3%81%A7%E5%87%BA%E4%BC%9A%E3%81%88%E3%82%8B%E3%81%AE%E3%81%8B.md)
  - 文章通过模拟实验探讨了电影《你的名字》中男女主角在新宿地区随机行走相遇的可能性。实验结果显示，两人在4天内能够相遇，但通过优化行走策略，如倾向于对方可能的方向或增加对须贺神社的偏好，可以显著缩短相遇时间。最终结论验证了两人在新宿地区相遇的可能性，并提出了优化相遇策略的方法。
  - Tags: #read

- (2025-01-14) [Timeouts and cancellation for humans — njs blog](2025-01-14-timeouts-and-cancellation-for-humans-%E2%80%94-njs-blog.md)
  - 文章讨论了在处理外部系统交互时，超时和取消机制的重要性及其挑战。传统的超时处理方法存在局限性，而Trio库提出的取消范围（Cancel Scopes）机制通过自动化传递取消令牌，简化了代码复杂性，提升了可靠性和可维护性。该机制适用于同步单线程Python、asyncio及其他编程语言，为超时和取消处理提供了创新解决方案。
  - Tags: #read #language

- (2025-01-14) [Notes on structured concurrency, or: Go statement considered harmful — njs blog](2025-01-14-notes-on-structured-concurrency%2C-or-go-statement-considered-harmful-%E2%80%94-njs-blog.md)
  - 文章总结了并发API的常见实现方式，介绍了Trio库的Nursery机制及其优势，讨论了语句的历史与问题，并类比了语句的破坏性。Nursery机制通过结构化并发控制流，解决了语句带来的问题，保留了函数抽象，支持自动资源清理和错误传播。未来，移除语句有望提升并发编程的可靠性和可维护性。
  - Tags: #read #language

- (2025-01-14) [浅谈DSPy和自动化提示词工程（中） - 铁蕾的个人博客](2025-01-14-%E6%B5%85%E8%B0%88dspy%E5%92%8C%E8%87%AA%E5%8A%A8%E5%8C%96%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B%EF%BC%88%E4%B8%AD%EF%BC%89---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - DSPy是一个通过编程简化语言模型交互的框架，使用函数签名形式隐藏提示词生成过程。其核心优化器MIPROv2通过生成和筛选few-shot示例及指令候选集来优化模型性能。下一篇文章将探讨DSPy与APE的区别及工程启示。
  - Tags: #read #llm

- (2025-01-14) [Playground Wisdom: Threads Beat Async/Await](2025-01-14-playground-wisdom-threads-beat-async-await.md)
  - Armin Ronacher认为async/await在大多数编程语言中是不良抽象，主张使用线程作为更好的并发模型。他指出async/await存在背压处理不足、函数着色、未解决Promise等问题，而线程提供了更灵活的挂起能力和并发处理。作者推崇Java的Project Loom等虚拟线程实现，并认为结构化并发和通道是未来并发编程的关键方向。
  - Tags: #read #language

- (2025-01-14) [Crushing JIRA tickets is a party trick, not a path to impact](2025-01-14-crushing-jira-tickets-is-a-party-trick%2C-not-a-path-to-impact.md)
  - 文章强调了工程师应关注对公司战略有重大影响的项目，而非仅仅完成JIRA票务。建议定期评估工作的重要性，果断放弃不再重要的任务，不依赖管理层的明确指示，并谨慎推动新想法。
  - Tags: #read #people

- (2025-01-13) [o1 isn’t a chat model (and that’s the point)](2025-01-13-o1-isn%E2%80%99t-a-chat-model-%28and-that%E2%80%99s-the-point%29.md)
  - o1是一款新型AI工具，擅长生成完整报告和解决复杂问题，尤其在医学诊断和概念解释方面表现优异。然而，其写作风格单一，构建完整应用仍需迭代。用户体验上存在延迟和界面设计不足的问题。未来，o1有望在需要高延迟、深度推理的任务中发挥更大作用，开发者也将探索更多创新应用。
  - Tags: #read #llm

- (2025-01-12) [Agents](2025-01-12-agents.md)
  - 智能代理是AI研究的核心目标，能够感知环境并采取行动，广泛应用于多个领域。其成功依赖于工具选择和规划能力，基础模型的发展为其提供了巨大潜力，但也带来了新的挑战和安全风险。
  - Tags: #read #llm

- (2025-01-12) [What's involved in getting a "modern" terminal setup?](2025-01-12-what%27s-involved-in-getting-a-modern-terminal-setup.md)
  - 现代终端体验需要多方面的配置，包括支持多行复制粘贴、无限历史记录、24位颜色、剪贴板集成等功能。推荐使用或作为shell，支持24位颜色的终端模拟器，以及开箱即用的文本编辑器如或。配置过程中需注意相互影响，逐步调整，找到适合自己的稳定状态。
  - Tags: #read

- (2025-01-11) [Start Presentations on the Second Slide](2025-01-11-start-presentations-on-the-second-slide.md)
  - 文章探讨了在技术演示中如何通过调整演示顺序来吸引观众注意力。建议将第二张幻灯片（通常是问题或挑战）放在开头，以立即引起观众兴趣。这种方法能激发程序员的解决问题欲望，使他们对背景信息和解决方案产生兴趣，从而提高演示效果。
  - Tags: #read #hack

- (2025-01-11) [Collection of insane and fun facts about SQLite - blag](2025-01-11-collection-of-insane-and-fun-facts-about-sqlite---blag.md)
  - SQLite是全球最广泛使用的数据库，由三人团队维护，起源于美国军舰上的需求。它采用公共领域许可证，不接受外部贡献，测试代码量远超实际代码量。SQLite通过销售许可证和支持服务盈利，性能优异，但存在一些限制。其独特性和高效性使其在数据库领域占据重要地位。
  - Tags: #read

- (2025-01-11) [Everything Must Be Paid for Twice](2025-01-11-everything-must-be-paid-for-twice.md)
  - 文章探讨了“双重支付理论”，即购买物品的第一价格（金钱）和使用物品的第二价格（努力和时间）。现代生活中，人们往往支付了第一价格却忽略了第二价格，导致资源浪费和未实现的潜力。通过减少不必要的购买并专注于支付第二价格，可以更充分地利用已有资源，获得更大的满足感。
  - Tags: #read

- (2025-01-09) [Double-keyed Caching: How Browser Cache Partitioning Changed the Web](2025-01-09-double-keyed-caching-how-browser-cache-partitioning-changed-the-web.md)
  - 双键缓存模型通过引入顶级站点和资源URL作为缓存键，有效防止跨站点跟踪和隐私泄露，但导致缓存命中率下降和网络带宽增加。为应对这一变化，建议优化域名策略、自托管关键资源、调整包边界与域边界对齐，并实施性能监控。尽管带来性能成本，双键缓存是网络隐私演变的必要步骤，未来需平衡隐私与性能。
  - Tags: #read #frontend

- (2025-01-08) [Why is hash(-1) == hash(-2) in Python?](2025-01-08-why-is-hash%28-1%29-%3D%3D-hash%28-2%29-in-python.md)
  - 作者在Reddit上发现Python中和都返回的现象，通过查看Python源码发现被用作错误标志，因此哈希函数返回以避免冲突。文章强调了阅读源码的重要性，并鼓励通过源码解决问题。
  - Tags: #read #py

- (2025-01-08) [How I program with LLMs](2025-01-08-how-i-program-with-llms.md)
  - 作者通过实验发现，LLMs在编程中具有显著价值，尤其在自动补全、搜索和聊天驱动编程方面。LLMs能提升生产力，减少重复性工作，并生成初稿代码，尽管有时需要验证和修复。未来，编程方式可能趋向专门化，测试将更全面，代码复用减少。作者还开发了自动化工具sketch.dev，以提升LLMs在Go编程中的效率。
  - Tags: #read #llm

- (2025-01-07) [htmx ~ The future of htmx](2025-01-07-htmx-~-the-future-of-htmx.md)
  - htmx起源于intercooler.js，旨在模仿jQuery的易用性和稳定性，成为构建长期在线网站的有用工具。htmx团队强调API稳定性，避免频繁更新，并通过扩展API和改进工具来增强功能。未来，htmx计划通过标准化和推广超媒体理念，进一步融入Web平台。
  - Tags: #read #frontend

- (2025-01-05) [What we learned copying all the best code assistants](2025-01-05-what-we-learned-copying-all-the-best-code-assistants.md)
  - Val Town团队通过不断集成最新代码生成工具（如GitHub Copilot、ChatGPT、Claude Artifacts等），优化代码补全和生成体验。他们开发了Townie工具，支持快速生成全栈应用，并计划引入多文件编辑和自动错误修复功能。团队致力于提供无需部署的托管服务和API，未来将继续开发完全集成的Web AI代码编辑器，保持合作精神并鼓励用户反馈。
  - Tags: #read #llm

- (2025-01-05) [Using LLMs and Cursor to become a finisher](2025-01-05-using-llms-and-cursor-to-become-a-finisher.md)
  - 作者在2024年通过使用LLMs和Cursor IDE显著提升了业余项目的开发效率，完成了多个项目的v1版本。他分享了项目开发流程和技巧，强调通过细化需求、快速初始化和迭代开发来保持动力，并建议读者尝试这些工具以提升项目完成效率。
  - Tags: #read #llm

- (2025-01-04) [Mistakes engineers make in large established codebases](2025-01-04-mistakes-engineers-make-in-large-established-codebases.md)
  - 大型代码库的维护面临诸多挑战，如学习难度高、一致性要求严格等。一致性是避免问题、便于未来改进的关键。工程师需理解服务使用情况、依赖管理和测试限制，并谨慎处理代码移除。大型代码库通常产生公司主要价值，值得投入精力维护。在开发新功能时，必须研究现有实践并遵循模式，同时依赖监控和防御性编程来捕捉错误。
  - Tags: #read #guide

- (2025-01-04) [The 70% problem: Hard truths about AI-assisted coding](2025-01-04-the-70%25-problem-hard-truths-about-ai-assisted-coding.md)
  - AI辅助开发显著提升了生产力，但软件质量未显著改善。高级工程师通过AI加速已知任务和原型设计，而初级工程师则面临代码质量低和学习障碍的问题。AI工具的最佳用途是作为经验丰富开发者的原型加速器和学习辅助工具。未来，AI将具备更高的自主性和多模态能力，但创建高质量软件仍需人类的同理心和工程纪律。AI的真正价值在于加速迭代和实验，而非替代良好的软件实践。
  - Tags: #read #llm

- (2025-01-04) [What can strong engineers do that weak engineers can't?](2025-01-04-what-can-strong-engineers-do-that-weak-engineers-can%27t.md)
  - 文章讨论了工程师的能力差异，强调强工程师的核心在于完成其他工程师无法完成的任务，如复杂项目交付和解决难题。普通工程师能处理大多数常规任务，而弱工程师几乎无法完成任何任务。文章还提供了与弱高级工程师合作的建议，强调保持职业态度和保护团队时间。结论呼吁工程师扩大自己的能力范围，并在与弱工程师合作时保持友好但保护自己的时间。
  - Tags: #read

- (2025-01-03) [Can LLMs write better code if you keep asking them to “write better code”?](2025-01-03-can-llms-write-better-code-if-you-keep-asking-them-to-%E2%80%9Cwrite-better-code%E2%80%9D.md)
  - 2023年11月，OpenAI在ChatGPT中集成了DALL-E 3的图像生成功能，展示了LLM在生成内容时的迭代能力。随后，实验探讨了通过不断要求LLM“write better code”来改进代码质量的可能性。实验使用Claude 3.5 Sonnet生成Python代码，并通过多次迭代优化代码性能，最终提升100倍。实验表明，提示工程可以显著加速代码优化，但仍需人工干预以确保代码的正确性和效率。所有代码和实验数据可在GitHub上获取。
  - Tags: #read

- (2025-01-03) [alufers/mitmproxy2swagger](2025-01-03-alufers-mitmproxy2swagger.md)
  - mitmproxy2swagger是一个自动化工具，可将mitmproxy捕获的流量或浏览器导出的HAR文件转换为OpenAPI 3.0规范，逆向工程REST API。支持Python和Docker安装，提供详细的安装和使用指南，开发者可通过poetry和pytest进行依赖管理和测试。项目采用MIT许可证。
  - Tags: #tools
