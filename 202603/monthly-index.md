# 2026-03 Monthly Index

- (2026-03-12) [你不知道的 Claude Code：架构、治理与工程实践 - Tw93](2026-03-12-%E4%BD%A0%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-claude-code%EF%BC%9A%E6%9E%B6%E6%9E%84%E3%80%81%E6%B2%BB%E7%90%86%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5---tw93.md)
  - 本文系统总结了Claude Code的六层架构模型、上下文工程、Skills设计等核心实践，强调通过分层治理和验证闭环提升AI工程化能力，适用于从工具使用者到系统设计者的演进。
  - Tags: #read #agent #deepdive #guide

- (2026-03-11) [AI should help us produce better code - Agentic Engineering Patterns](2026-03-11-ai-should-help-us-produce-better-code---agentic-engineering-patterns.md)
  - AI工具应提升而非降低代码质量，通过处理技术债务、辅助决策和复盘优化，实现高效可持续的开发。
  - Tags: #read #agent #tips

- (2026-03-10) [年度征文｜「你是专家」这句话，到底是在帮 AI 还是在害你？ - 少数派](2026-03-10-%E5%B9%B4%E5%BA%A6%E5%BE%81%E6%96%87%EF%BD%9C%E3%80%8C%E4%BD%A0%E6%98%AF%E4%B8%93%E5%AE%B6%E3%80%8D%E8%BF%99%E5%8F%A5%E8%AF%9D%EF%BC%8C%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8%E5%B8%AE-ai-%E8%BF%98%E6%98%AF%E5%9C%A8%E5%AE%B3%E4%BD%A0%EF%BC%9F---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 本文通过实验验证了AI提示词中“身份设定”和“情感措辞”的效果：身份设定可调节输出风格但无法提升准确性，情感措辞能激励AI更用心但不会改变事实判断。核心结论是，AI的准确性取决于底层推理能力，处理事实任务时应优先选择支持推理的模型。
  - Tags: #read #llm

- (2026-03-10) [Package managers keep using git as a database, it never works out](2026-03-10-package-managers-keep-using-git-as-a-database%2C-it-never-works-out.md)
  - 多个包管理器曾尝试用 Git 存储索引，但因性能、可扩展性等问题逐步转向 HTTP 或数据库方案。Git 更适合代码协作，而非包注册表的数据存储。
  - Tags: #read

- (2026-03-10) [Production query plans without production data](2026-03-10-production-query-plans-without-production-data.md)
  - PostgreSQL 18 引入便携式优化器统计信息功能，通过  和  函数，允许在测试环境中注入生产级统计信息，从而在不需要实际数据的情况下模拟真实查询计划，提升CI/CD测试与本地调试效率。
  - Tags: #read #database

- (2026-03-09) [How I Dropped Our Production Database and Now Pay 10% More for AWS](2026-03-09-how-i-dropped-our-production-database-and-now-pay-10%25-more-for-aws.md)
  - 作者因误用Terraform和AI代理导致生产数据库被删，经24小时恢复后，实施状态管理S3化、双重删除保护、独立备份及AI权限限制等措施，承诺未来加强操作隔离。
  - Tags: #read

- (2026-03-09) [GNU and the AI reimplementations - <antirez>](2026-03-09-gnu-and-the-ai-reimplementations---antirez.md)
  - 本文探讨了AI重写软件的合法性，将其与GNU重写UNIX类比，强调不复制代码结构的重写合法且有益。文章呼吁拥抱AI变革，视之为推动开源与软件演进的机会。
  - Tags: #read

- (2026-03-08) [The MCP Abstraction Tax](2026-03-08-the-mcp-abstraction-tax.md)
  - 本文提出了AI代理与API交互中的“抽象税”概念，指出每个抽象层会降低保真度并可能损害上下文。通过对比MCP和CLI路径，作者强调应根据场景权衡迭代速度与上下文管理，并非竞争关系。
  - Tags: #read #agent

- (2026-03-08) [You Need to Rewrite Your CLI for AI Agents](2026-03-08-you-need-to-rewrite-your-cli-for-ai-agents.md)
  - 文章提出，AI代理的CLI需重构以优化可预测性与安全性，包括转向JSON载荷、实时模式查询、上下文限制、输入验证、技能封装等，并建议增量实施。
  - Tags: #read #agent #deepdive

- (2026-03-07) [Avoiding a Culture of Emergencies](2026-03-07-avoiding-a-culture-of-emergencies.md)
  - 优秀管理者通过深入了解业务、明确重点、前瞻布局和关怀团队，有效减少可预防的紧急事件，提升工作效率与成员幸福感，增强人才留存。
  - Tags: #read #career

- (2026-03-06) [Disable Your SSH Access With This One Simple Trick](2026-03-06-disable-your-ssh-access-with-this-one-simple-trick.md)
  - 作者使用 scp 传输目录后，因目标目录权限被设为 777，导致 SSH 登录失败。原因是 OpenSSH 安全策略拒绝过宽权限。将权限恢复为 700 后问题解决，该问题已在后续版本修复。
  - Tags: #read #tips

- (2026-03-06) [2026 年，我把自己做成了一个 AI](2026-03-06-2026-%E5%B9%B4%EF%BC%8C%E6%88%91%E6%8A%8A%E8%87%AA%E5%B7%B1%E5%81%9A%E6%88%90%E4%BA%86%E4%B8%80%E4%B8%AA-ai.md)
  - 作者罗磊于2026年构建AI数字分身，通过多模型画像和RAG对话技术管理知识，强调主动构建个人系统的重要性。
  - Tags: #read #llm

- (2026-03-06) [Cognitive Debt: When Velocity Exceeds Comprehension | rockoder](2026-03-06-cognitive-debt-when-velocity-exceeds-comprehension-rockoder.md)
  - AI辅助开发导致代码生成速度远超工程师理解速度，形成“认知债务”。组织过度关注产出指标而忽视理解深度，引发审查失效、知识流失和系统风险。需改革绩效评估，纳入理解深度以应对长期挑战。
  - Tags: #read #career

- (2026-03-06) [AI=true is an Anti-Pattern](2026-03-06-ai%3Dtrue-is-an-anti-pattern.md)
  - 文章批评了编程中针对AI设计文档、工具和工作流的反模式，主张统一接口与通用设计，以兼顾人类与AI，提升协作效率和互操作性。
  - Tags: #read

- (2026-03-06) [QRTape | Audio Playback from Paper Tape with Computer Vision](2026-03-06-qrtape-audio-playback-from-paper-tape-with-computer-vision.md)
  - QRTape 是一个利用二维码将音频编码打印在纸带上，通过摄像头和软件解码播放的低成本音频存储方案，结合计算机视觉与音频压缩技术，展示了纸质介质存储数据的创新可行性。
  - Tags: #read

- (2026-03-06) [AI And The Ship of Theseus](2026-03-06-ai-and-the-ship-of-theseus.md)
  - 本文以“特修斯之船”为喻，探讨AI生成代码通过重写绕过GPL等版权许可的法律与道德问题。作者以chardet库为例，分析AI生成代码的版权归属及许可冲突，认为代码生成成本降低将推动软件以更宽松许可重现，但可能引发“垃圾分叉”和法律纠纷。总体持乐观态度，主张开放共享优于许可限制，同时承认这将加剧AI与许可领域的冲突。
  - Tags: #read

- (2026-03-06) [你大概不会想用 LLM 做数据分析](2026-03-06-%E4%BD%A0%E5%A4%A7%E6%A6%82%E4%B8%8D%E4%BC%9A%E6%83%B3%E7%94%A8-llm-%E5%81%9A%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90.md)
  - 该文指出LLM因训练数据含统计错误且缺乏推理能力，在数据分析中易产生误导结果，强调需懂统计原理并亲自验证，仅在可视化等辅助场景谨慎使用。
  - Tags: #read #llm

- (2026-03-06) [Can coding agents relicense open source through a “clean room” implementation of code?](2026-03-06-can-coding-agents-relicense-open-source-through-a-%E2%80%9Cclean-room%E2%80%9D-implementation-of-code.md)
  - 文章以chardet库为例，探讨AI辅助的“洁净室”重写是否合规。Dan用Claude重写代码并改用MIT许可证，但原作者质疑其合法性。争议焦点在于AI是否真正独立，反映了开源领域AI辅助编程的法律与伦理挑战。
  - Tags: #read

- (2026-03-06) [Clinejection — Compromising Cline's Production Releases just by Prompting an Issue Triager | Adnan Khan - Security Research](2026-03-06-clinejection-%E2%80%94-compromising-cline%27s-production-releases-just-by-prompting-an-issue-triager-adnan-khan---security-research.md)
  - Cline 工具因 AI 代理提示注入漏洞被利用，攻击者通过缓存污染窃取发布凭证，导致恶意版本发布。影响数百万开发者，团队已修复并加强安全措施。
  - Tags: #read #security

- (2026-03-06) [Agentic manual testing - Agentic Engineering Patterns](2026-03-06-agentic-manual-testing---agentic-engineering-patterns.md)
  - 文章强调在代理工程中手动测试的重要性，指出自动化测试不足以发现所有问题。通过Python代码片段、curl测试API及浏览器工具如Playwright、Rodney和Showboat进行手动测试，可发现遗漏问题、生成文档，并补充自动化测试，形成闭环。
  - Tags: #read #agent #tips

- (2026-03-06) [I don't know if my job will still exist in ten years](2026-03-06-i-don%27t-know-if-my-job-will-still-exist-in-ten-years.md)
  - 作者从乐观转向担忧，认为AI代理将取代软件工程师岗位，尤其初级和中级职位。他反驳需求增长会创造更多岗位的观点，指出AI能写代码并维护代码，导致工程师需求下降。最终，作者接受行业自动化浪潮波及自身，准备寻找新方向。
  - Tags: #read

- (2026-03-05) [My Media Diet, Redux](2026-03-05-my-media-diet%2C-redux.md)
  - 作者在2026年反思信息消费习惯，受环境与认知变化影响，从偏重实用转向接纳虚构与感性，语言上双语并重，载体上灵活利用各类平台。核心是应对优质信息稀缺，依靠判断力进行策展，保持警觉以锻炼心智。
  - Tags: #read

- (2026-03-03) [GIF optimization tool using WebAssembly and Gifsicle - Agentic Engineering Patterns](2026-03-03-gif-optimization-tool-using-webassembly-and-gifsicle---agentic-engineering-patterns.md)
  - 作者利用Claude Code代理工具，基于Gifsicle构建了支持拖拽上传、参数调整和预览下载的GIF优化网页应用。通过自然语言提示高效完成开发、测试与集成，展示了AI代理在复杂任务中的实用性。
  - Tags: #read #agent

- (2026-03-03) [用好AI的第一步：停止使用ChatGPT](2026-03-03-%E7%94%A8%E5%A5%BDai%E7%9A%84%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%81%9C%E6%AD%A2%E4%BD%BF%E7%94%A8chatgpt.md)
  - 该错误源于请求参数验证失败，系统无法解析域名“stop-using-chatgpt.html”，通常因域名格式无效或无法识别。错误代码40001提示用户检查URL格式是否符合标准。
  - Tags: #read #agent

- (2026-03-01) [Google API Keys Weren't Secrets. But then Gemini Changed the Rules. ◆ Truffle Security Co.](2026-03-01-google-api-keys-weren%27t-secrets.-but-then-gemini-changed-the-rules.-%E2%97%86-truffle-security-co..md)
  - Google API密钥安全模型变化导致风险：原本用于公共服务的密钥被静默赋予访问敏感Gemini端点的能力，可能引发数据泄露和费用激增。建议开发者检查并审计密钥，避免公开暴露。
  - Tags: #read #security

- (2026-03-01) [The Engine Behind the Hype](2026-03-01-the-engine-behind-the-hype.md)
  - 文章探讨了作者在AI编程工具中遇到的上下文窗口消耗问题，并聚焦于轻量级编码代理引擎“Pi”。Pi通过极简设计（如精简工具集和短系统提示）显著提升了上下文效率，证明了小型、可定制工具的潜力，为AI工具的未来提供了回归本质的思考。
  - Tags: #read #agent

- (2026-03-01) [Rolling your own serverless OCR in 40 lines of code | Christopher Krapu](2026-03-01-rolling-your-own-serverless-ocr-in-40-lines-of-code-christopher-krapu.md)
  - 本文介绍了如何利用 Modal 无服务器平台和 DeepSeek OCR 模型，在 40 行代码内构建一个高效的 OCR 系统。该方案能将 PDF 教科书转换为可搜索的 Markdown 文本，通过云端 GPU 并行处理，实现了低成本（约 2 美元处理 600 页）且高质量的数学公式识别。
  - Tags: #read #guide

- (2026-03-01) [Whale Fall](2026-03-01-whale-fall.md)
  - 文章以“鲸落”比喻开源项目消亡后的生态演变，指出项目停止维护后，其代码、协议和接口会像鲸鱼尸体一样沉入底层，为后续创新提供养分。核心过程包括初期腐食（社区分叉形成新项目）、中期富集（协议和API催生新工具）和长期化学合成（底层结构成为跨生态基础设施）。关键模式涉及连续再殖民、许可证变更引发的生态重组，以及系统性案例（如Sun Microsystems项目）。现状反思指出，企业收购或云平台整合导致“浅水死亡”，减少鲸落率，可能削弱生态多样性。结论强调，健康的开源生态依赖鲸落效应滋养创新，但当前整合趋势需关注。
  - Tags: #read

- (2026-03-01) [An AI agent coding skeptic tries AI agent coding, in excessive detail](2026-03-01-an-ai-agent-coding-skeptic-tries-ai-agent-coding%2C-in-excessive-detail.md)
  - 作者记录了使用Claude Opus 4.5进行编码的实验，发现其在复杂代码编写和遵循规则方面表现优异。通过多个项目测试，作者认为AI代理在拥有足够领域知识的情况下能有效辅助开发，但需谨慎使用并优化工作流程。
  - Tags: #read #agent #deepdive

- (2026-03-01) [The most-seen UI on the Internet? Redesigning Turnstile and Challenge Pages](2026-03-01-the-most-seen-ui-on-the-internet-redesigning-turnstile-and-challenge-pages.md)
  - Cloudflare对Turnstile验证码进行了全面重新设计，通过统一信息架构、优化交互和遵循高可访问性标准，提升了全球用户体验。设计改进包括简化文本、减少负面色彩，并支持多语言布局。工程上采用Rust构建UI，确保安全与一致性。最终目标是提高完成率、减少放弃率和支持工单，证明良好设计与安全性可共存。
  - Tags: #read #design

- (2026-03-01) [We deserve a better streams API for JavaScript](2026-03-01-we-deserve-a-better-streams-api-for-javascript.md)
  - 本文剖析了 JavaScript Web Streams API 的设计缺陷，如过度仪式感、锁机制复杂、BYOB 低效、背压脱节及 Promise 开销大，导致性能与易用性问题。作者认为需基于现代语言特性重构，以提供更高效的替代方案。
  - Tags: #read #deepdive #frontend #api

- (2026-03-01) [Interactive explanations - Agentic Engineering Patterns - Simon Willison's Weblog](2026-03-01-interactive-explanations---agentic-engineering-patterns---simon-willison%27s-weblog.md)
  - 本文探讨代理工程中通过交互式解释降低认知债务的方法。以词云生成为例，展示动画解释如何直观呈现算法逻辑，帮助开发者理解代码，从而有效管理认知债务。
  - Tags: #read #tips
