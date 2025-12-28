# 2024-10 Monthly Index

- (2024-10-31) [Creating a LLM-as-a-Judge That Drives Business Results –](2024-10-31-creating-a-llm-as-a-judge-that-drives-business-results-%E2%80%93.md)
  - 文章提出通过“批评影子”技术解决AI团队在构建系统时的数据过载问题，包括找到领域专家、创建多样性数据集、指导专家进行通过/失败判断、修复错误、迭代构建LLM法官、进行错误分析等步骤，强调数据分析和反馈循环的重要性。
  - Tags: #deepdive #llm

- (2024-10-31) [ASCII control characters in my terminal](2024-10-31-ascii-control-characters-in-my-terminal.md)
  - 文章探讨了终端控制字符的用途、分类及其在不同操作系统中的处理方式，介绍了ASCII控制字符表和键盘快捷键冲突问题，并提供了识别和处理控制字符的工具和方法。作者认为这些内容虽有趣，但日常使用中了解基本控制字符功能即可。
  - Tags: #read

- (2024-10-31) [curl source code age](2024-10-31-curl-source-code-age.md)
  - 作者通过编写脚本分析curl项目的代码年龄，使用gnuplot进行数据可视化，最终发现超过50%的代码是在2020年后编写的，约25%的代码在2014年前编写，1254行代码在2000年前编写。
  - Tags: #read

- (2024-10-30) [Being Glue — No Idea Blog](2024-10-30-being-glue-%E2%80%94-no-idea-blog.md)
  - 文章讨论了软件工程师的非编码职责（胶水工作）的重要性，指出这些工作对团队成功至关重要，但常被忽视。强调公平分配胶水工作，避免职业发展受限，并建议通过职业对话和展示工作影响来应对晋升困境。
  - Tags: #read #people

- (2024-10-29) [15 rules for blogging, and my current streak](2024-10-29-15-rules-for-blogging%2C-and-my-current-streak.md)
  - 作者分享了其博客写作的规则和流程，包括每周发布三篇博文、每篇只讨论一个主题、简洁表达、放弃追求正确和有趣等，强调写作应面向大众且即时，同时避免写作负担。
  - Tags: #read

- (2024-10-29) [The CAP Theorem of Clustering: Why Every Algorithm Must Sacrifice Something](2024-10-29-the-cap-theorem-of-clustering-why-every-algorithm-must-sacrifice-something.md)
  - 聚类算法无法同时满足尺度不变性、丰富性和一致性，Kleinberg定理揭示了这一数学缺陷。实际应用中，需根据需求选择牺牲某一属性，如单链接聚类牺牲丰富性，k-means牺牲丰富性和一致性。理解这些限制有助于设计更有效的系统。
  - Tags: #read #algo

- (2024-10-29) [When to use std::string_view](2024-10-29-when-to-use-std-string_view.md)
  - `std::string_view` 是C++17引入的轻量级字符串视图类，适用于廉价传递多种字符串类型。它通过指针和长度实现，支持多种创建方式，但需注意其数据不保证以空字节结尾。在性能上，`std::string_view` 适用于参数类型多样的情况，而在参数多为 `std::string` 左值时，`const std::string&` 更优。
  - Tags: #read #cpp

- (2024-10-29) [Colophon](2024-10-29-colophon.md)
  - 文章详细介绍了自建博客系统的技术架构、写作流程、持久性策略及其他功能，包括使用Markdown格式、Python的Flask和Jinja模板生成页面，以及通过GitHub和Working Copy进行移动端编辑。强调了网页持久性原则和自托管的控制与灵活性，同时提到了RSS订阅、邮件订阅、多人光标等特色功能。
  - Tags: #read

- (2024-10-29) [纯 Web 视频剪辑 | 风痕 · 術&思](2024-10-29-%E7%BA%AF-web-%E8%A7%86%E9%A2%91%E5%89%AA%E8%BE%91-%E9%A3%8E%E7%97%95-%C2%B7-%E8%A1%93%26%E6%80%9D.md)
  - 文章介绍了如何利用WebCodecs API在Web平台上实现视频剪辑，分析了不同实现方案的优缺点，并详细讲解了素材管理、画布、时间轴等模块的基础能力实现。强调了基础能力的重要性，并提供了相关资源供进一步学习。
  - Tags: #guide

- (2024-10-16) [9001/copyparty](2024-10-16-9001-copyparty.md)
  - copyparty是一个便携式文件服务器，支持多种功能如断点续传、去重、WebDAV等，采用MIT许可证，目前有634星标和37分叉，活跃开发中，有6个开放问题，无拉取请求。
  - Tags: #tools

- (2024-10-16) [Why techies leave Big Tech](2024-10-16-why-techies-leave-big-tech.md)
  - 本文探讨了技术人员离开大科技公司的原因，包括稳定性下降、职业成长受限、职业路径封闭、被迫离职、初创公司“大科技化”、薪酬下降等。通过具体案例分析，揭示了大科技公司薪酬结构和内部调动的要求，并观察到市场招聘放缓和经验需求的变化。总结指出，职业成长和薪酬影响是主要驱动因素，离开大科技公司可能是追求新目标的起点。
  - Tags: #read #deepdive

- (2024-10-16) [Web Browser Engineering](2024-10-16-web-browser-engineering.md)
  - 《Web Browser Engineering》通过Python代码构建基本Web浏览器，详细解释其工作原理，涵盖网络、JavaScript等。支持通过Twitter、博客、Patreon等平台获取更新和讨论。
  - Tags: #books

- (2024-10-15) [Investigation of a Workbench UI Latency Issue](2024-10-15-investigation-of-a-workbench-ui-latency-issue.md)
  - Netflix的Workbench产品中，JupyterLab UI因_jupyter-resource-usage_扩展的资源监控功能与不准确的CPU数量和虚拟内存使用相结合，导致延迟。通过禁用该扩展，解决了用户的问题。
  - Tags: #read

- (2024-10-14) [SQL/JSON is here! (kinda “Waiting for Pg 17”) – select * from depesz;](2024-10-14-sql-json-is-here%21-%28kinda-%E2%80%9Cwaiting-for-pg-17%E2%80%9D%29-%E2%80%93-select-from-depesz%3B.md)
  - PostgreSQL通过SQL/JSON标准新增了处理JSON数据的功能，包括构造器、测试函数和查询函数，增强了处理复杂数据结构的能力。
  - Tags: #read #db

- (2024-10-13) [Making algorithms faster](2024-10-13-making-algorithms-faster.md)
  - 文章探讨了通过优化和并行化算法来提升计算勾股数的效率。初始实现使用三重嵌套循环，优化后减少了内层循环范围，速度提升2.81倍。进一步并行化使用`std::for_each()`和执行策略，最终并行无序执行速度提升18.47倍。结论是并行化效果显著，优化也值得进行。
  - Tags: #cpp

- (2024-10-12) [The Copenhagen Book](2024-10-12-the-copenhagen-book.md)
  - 《The Copenhagen Book》是一本关于Web应用认证的开源指南，涵盖服务器端令牌、会话管理、密码认证、OAuth等多方面内容，建议与OWASP Cheat Sheet结合使用，支持社区反馈和捐赠。
  - Tags: #books

- (2024-10-11) [How Hard Should Your Employer Work To Retain You?](2024-10-11-how-hard-should-your-employer-work-to-retain-you.md)
  - 文章讨论了公司在留住关键人才上的策略，强调员工应基于职业满足和家庭需求做出决策，公司需确保岗位匹配和公平补偿，管理者应提供职业机会和诚实反馈，同时行业应转向公平透明的薪酬体系。
  - Tags: #read

- (2024-10-11) [Can You Get Root With Only a Cigarette Lighter? | Blog](2024-10-11-can-you-get-root-with-only-a-cigarette-lighter-blog.md)
  - 文章探讨了使用低成本工具如打火机进行硬件故障注入（EMFI）以获取Root权限的可能性，并通过实验验证了这一方法。作者成功利用打火机诱导内存错误，实现了CPython和Linux系统的漏洞利用，展示了其在游戏反作弊和Android设备安全检查绕过中的潜在应用。
  - Tags: #deepdive #read

- (2024-10-10) [A static business is a healthy business](2024-10-10-a-static-business-is-a-healthy-business.md)
  - 文章强调通过均匀的客户基础和固定定价策略，如Basecamp的每月$99定价，来减少对大客户的依赖，从而降低业务风险，确保业务的稳定和健康。
  - Tags: #read

- (2024-10-09) [jazz - Instant sync](2024-10-09-jazz---instant-sync.md)
  - Jazz是一个开源框架，旨在简化本地优先应用程序的开发，减少后端复杂性。它提供实时同步、存储、认证等功能，支持多种数据结构和协作特性。Jazz Mesh作为默认同步和存储节点，免费使用。开发工具包括Jazz Toolkit，支持多平台开发。
  - Tags: #tools

- (2024-10-09) [temporal - Open Source Durable Execution](2024-10-09-temporal---open-source-durable-execution.md)
  - Temporal是一个开源的持久执行框架，通过抽象复杂性、简化代码和消除恢复逻辑，显著提高软件的可靠性和开发效率。它支持多语言开发，广泛应用于各种场景，并得到行业专家的高度评价。Temporal Cloud提供可靠的云服务，进一步简化部署和管理。
  - Tags: #tools

- (2024-10-09) [Turning a conference talk into an annotated presentation - Jacob Kaplan-Moss](2024-10-09-turning-a-conference-talk-into-an-annotated-presentation---jacob-kaplan-moss.md)
  - 作者利用现代AI工具将会议演讲视频转化为书面版本，通过Keynote准备演讲稿、下载和处理视频、生成和清理转录，最终手动编辑和完善内容，使其更适合书面阅读。
  - Tags: #hack

- (2024-10-09) [curl bug-bounty stats | daniel.haxx.se](2024-10-09-curl-bug-bounty-stats-daniel.haxx.se.md)
  - curl漏洞赏金计划自2019年启动以来，已支付84,260美元给69个CVE漏洞的发现者。资金来源包括curl基金和Internet Bug Bounty，奖励金额根据漏洞严重性从500美元到5,000美元不等。共收到477份报告，其中73份为有效安全漏洞。安全团队高效响应，平均36小时内确认漏洞。未来预计将继续收到有效报告，但严重性可能较低。
  - Tags: #read #oss

- (2024-10-08) [感谢捉虫：聊聊自动更正的前世今生 - 少数派](2024-10-08-%E6%84%9F%E8%B0%A2%E6%8D%89%E8%99%AB%EF%BC%9A%E8%81%8A%E8%81%8A%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%AD%A3%E7%9A%84%E5%89%8D%E4%B8%96%E4%BB%8A%E7%94%9F---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 拼写检查器自20世纪50年代发展至今，经历了从基于规则到AI智能化的转变，广泛应用于PC和智能手机。Microsoft的AutoCorrect和Apple的NsSpellChecker是重要里程碑。未来，拼写检查器将受网络和商业模式影响，同时需平衡规范与用户表达自由。
  - Tags: #read

- (2024-10-08) [Thoughts on the Treasurer Role at Tech NonProfits - Will Vincent](2024-10-08-thoughts-on-the-treasurer-role-at-tech-nonprofits---will-vincent.md)
  - 文章讨论了非营利组织财务主管面临的挑战和风险，特别是资金被盗用的普遍性问题。作者分享了在Django Software Foundation的财务管理经验，提出通过支付报酬、统一沟通、内部报表和双重审核等措施来预防财务问题。强调了财务管理的专业性和复杂性，并对Catherine Holmes的贡献表示感谢。
  - Tags: #read

- (2024-10-08) [Some notes on upgrading Hugo](2024-10-08-some-notes-on-upgrading-hugo.md)
  - 作者从Hugo v0.40升级到v0.135，经历了模板语法、页面数据、Markdown渲染器等多方面的变更。主要挑战包括从Blackfriday到Goldmark的转换，导致大量Markdown文件需更新。通过详细对比和配置调整，作者成功完成升级，并认为新渲染器修复了旧问题，对未来有益。
  - Tags: #read

- (2024-10-07) [VTracer](2024-10-07-vtracer.md)
  - VTracer是一款由Vision Cortex开发的图像转SVG工具，支持拖拽和粘贴操作，提供多种参数调整选项以优化转换效果，包括颜色处理、图像清理、曲线拟合和路径精度设置。用户可通过官方文档、GitHub仓库获取资源并参与开发，直接下载转换后的SVG文件。
  - Tags: #tools

- (2024-10-06) [Wikidata is a Giant Crosswalk File](2024-10-06-wikidata-is-a-giant-crosswalk-file.md)
  - 文章介绍了如何利用Wikidata的结构化数据构建跨平台数据表，通过DuckDB和Ruby脚本处理近140GB的JSON数据集，分割数据以避免性能问题，并探索了Wikidata的声明系统及其外部ID的应用。
  - Tags: #read

- (2024-10-05) [Hybrid full-text search and vector search with SQLite](2024-10-05-hybrid-full-text-search-and-vector-search-with-sqlite.md)
  - 文章讨论了全文搜索与向量搜索的结合，通过`sqlite-vec`扩展在SQLite中实现混合搜索。全文搜索和语义搜索各有优劣，结合使用能提高搜索效果。文章还提供了构建和查询示例，并探讨了不同混合搜索方法的应用场景和未来改进方向。
  - Tags: #read #db

- (2024-10-03) [Terminal colours are tricky](2024-10-03-terminal-colours-are-tricky.md)
  - 文章讨论了终端配色方案的复杂性，涉及蓝黑色、亮黄色、256色、Solarized主题、vim主题匹配等多个问题，并提供了重新配置颜色、最小对比度功能等解决方案。作者强调处理这些细节虽有趣但令人沮丧，推荐使用base16-shell和base16-vim简化配置。
  - Tags: #read

- (2024-10-02) [A Local-First Case Study | jakelazaroff.com](2024-10-02-a-local-first-case-study-jakelazaroff.com.md)
  - 作者因不满现有旅行规划工具，开发了本地优先的网页应用Waypoint，结合富文本编辑器和地图，实现快速数据输入和结构化行程规划，并支持实时协作和离线编辑，展示了本地优先架构的可行性和优势。
  - Tags: #deepdive #frontend

- (2024-10-02) [OpenAI DevDay 2024 live blog](2024-10-02-openai-devday-2024-live-blog.md)
  - 文章详细介绍了OpenAI的o1模型在多个领域的应用和更新，包括实时API的引入、模型定制、价格调整、模型蒸馏工具的发布，以及结构化输出和多模态应用的讨论。重点展示了o1在语音输入输出、AI助手、语言学习等场景的实际应用，并强调了模型微调和价格优化的重要性。
  - Tags: #read

- (2024-10-01) [Rowboat](2024-10-01-rowboat.md)
  - Rowboat是一款快速数据分析工具，通过即时可视化、地理映射和交互功能，帮助用户快速理解大型数据集，无需复杂设置或编码。
  - Tags: #tools

- (2024-10-01) [Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More](2024-10-01-conflating-overture-places-using-duckdb%2C-ollama%2C-embeddings%2C-and-more.md)
  - 文章讨论了地理空间数据合并的挑战，介绍了使用DuckDB、Ollama和Python在本地机器上合并阿拉米达县餐厅检查数据与Overture Maps地点数据的方法。通过H3瓦片分组和多步骤合并管道（包括精确名称匹配、字符串相似度和嵌入模型），显著提高了数据匹配率。嵌入模型因其易用性和高效性被推荐为合并工具，未来可进一步优化。
  - Tags: #read #guide
