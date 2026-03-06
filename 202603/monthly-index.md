# 2026-03 Monthly Index

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
