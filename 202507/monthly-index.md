# 2025-07 Monthly Index

- (2025-07-31) [Reflection in C++26 (P2996)](2025-07-31-reflection-in-c%2B%2B26-%28p2996%29.md)
  - C++26的反射特性提案P2996已通过，Clang实验分支支持。通过操作符和访问运行时元数据，可查询名称、遍历成员，动态拼接代码（如提取类型）。支持自定义注解（如）控制成员行为。例如，命令行库clap利用反射自动解析参数，简化代码。Clang率先实现，未来P3294提案将扩展功能。
  - Tags: #read #cpp

- (2025-07-31) [The Math Is Haunted — overreacted](2025-07-31-the-math-is-haunted-%E2%80%94-overreacted.md)
  - 该文介绍数学形式化语言Lean，演示其语法与机制（如、），并以错误公理示例说明形式系统潜在矛盾风险。通过费马大定理说明复杂证明依赖协作形式化进展，并推荐学习资源，强调Lean兼具编程与数学探索的趣味性。
  - Tags: #read #guide

- (2025-07-31) [Agentic Coding Things That Didn’t Work](2025-07-31-agentic-coding-things-that-didn%E2%80%99t-work.md)
  - 作者尝试使用Claude Code等自动化工具后反思：高频操作外的自动化易失败，预设命令（如Slash Commands）和复杂功能（如Hooks、Print Mode）因体验不佳被弃用。实践表明直接对话、手动引导更高效，需动态维护提示而非僵化预设，并警惕过度依赖工具导致技术能力退化。核心原则是保持简单，持续验证自动化价值。（99字）
  - Tags: #read #llm

- (2025-07-31) [Vibe Coding for Product Managers: Stop Writing, Start Building](2025-07-31-vibe-coding-for-product-managers-stop-writing%2C-start-building.md)
  - 本文指出在AI时代，开发模式应从传统"规格文档优先"转向"构建优先"。因AI工具大幅降低开发成本，建议用一页纸简案+快速原型取代冗长文档，仅保留20%关键决策需书面协议。企业需跟随技术趋势转型构建驱动模式，否则将如固守传真机般被淘汰。
  - Tags: #read

- (2025-07-31) [Vibe code is legacy code](2025-07-31-vibe-code-is-legacy-code.md)
  - 文章指出，Vibe coding依赖AI快速生成代码，开发者常不理解底层逻辑，本质等同于遗留代码，易积累技术债务。该模式仅适合原型或短期项目，长期维护需警惕。作者强调AI是工具，需谨慎使用，开发者仍需重视代码理解与重构，避免过度依赖导致不可控的技术债务危机。
  - Tags: #read

- (2025-07-30) [Mind the End of Your Line ∙ Adaptive Patchwork](2025-07-30-mind-the-end-of-your-line-%E2%88%99-adaptive-patchwork.md)
  - Git通过配置处理跨平台行分隔符问题，规定仓库统一使用LF，提交时转换CRLF为LF，检出时根据系统自动转回。核心配置包括（旧系统）和（推荐新系统），后者可显式定义文件转换规则，如强制转换，标记二进制文件避免误处理。需团队统一配置以避免合并冲突。
  - Tags: #read #git #deepdive

- (2025-07-29) [LLMs can now identify public figures in images](2025-07-29-llms-can-now-identify-public-figures-in-images.md)
  - 本文测试多模态LLM识别公众人物能力，发现除OpenAI/Claude因安全策略限制外，Gemini、Llama、Mistral及Qwen均能有效识别。Gemini在多人物排序和影视海报场景中准确率超90%，推测得益于更丰富的训练数据。研究表明厂商间因数据规模和伦理策略存在显著能力差异，需警惕技术向普通人物识别扩展的隐私风险。（99字）
  - Tags: #read #llm

- (2025-07-28) [The many, many, many JavaScript runtimes of the last decade](2025-07-28-the-many%2C-many%2C-many-javascript-runtimes-of-the-last-decade.md)
  - 过去十年，JavaScript通过多样化运行时和引擎扩展应用场景。在边缘计算领域，Cloudflare Workers、Deno、Bun等竞相推出；微控制器则依赖Duktape、JerryScript等轻量引擎；React Native和Electron主导原生应用开发；多语言引擎如Graal.js推动跨平台整合。趋势显示，引擎解耦与多样性驱动JavaScript生态扩展至边缘设备、物联网及多硬件平台，成为通用开发语言。
  - Tags: #read #js #deepdive

- (2025-07-28) [TIL: Exception.add_note](2025-07-28-til-exception.add_note.md)
  - Python 3.11新增方法，允许通过在捕获异常时追加字符串说明。注释存储在列表中，抛出异常时会显示在原始错误信息下方。该方法继承自基类，适用于所有异常类型，便于扩展调试细节。
  - Tags: #tips #python

- (2025-07-28) [Enough AI copilots! We need AI HUDs](2025-07-28-enough-ai-copilots%21-we-need-ai-huds.md)
  - 文章批判以Copilot为代表的拟人化AI设计干扰用户，主张回归马克·魏泽"隐形计算"理念，通过增强显示界面（HUD）直接扩展人类感知。如飞机HUD将关键数据叠加于视野，拼写检查用红色波浪线标记错误，这些"新感官"无需交互即可赋能用户。作者认为复杂场景需通过HUD延伸人类认知能力，而非依赖AI代理决策，AI设计应聚焦增强而非替代人类智能。
  - Tags: #read #llm #design

- (2025-07-28) [The Bitter Lesson versus The Garbage Can](2025-07-28-the-bitter-lesson-versus-the-garbage-can.md)
  - 文章探讨了组织管理的"Garbage Can模型"与AI的"Bitter Lesson"理论对立：前者强调组织本质混沌需梳理流程以部署AI，后者主张用算力与通用学习超越人工规则。实践显示强化学习代理（如ChatGPT Agent）比人工规则系统更高效，企业面临路径抉择——既存流程优化 vs 算力驱动的输出导向，其结果将重塑组织竞争力边界。（99字）
  - Tags: #read

- (2025-07-27) [I Drank Every Cocktail](2025-07-27-i-drank-every-cocktail.md)
  - 作者自21岁起历时三年完成IBA官方102款鸡尾酒挑战，通过社交探索、伦敦酒吧深访及自制IBA Tiki派对攻克冷门酒款，揭露行业赞助矛盾与文化推广局限。24岁达成目标后，创建相关维基词条并开启新餐饮挑战。
  - Tags: #read

- (2025-07-27) [An Engineer's Guide to AI Code Model Evals](2025-07-27-an-engineer%27s-guide-to-ai-code-model-evals.md)
  - AI代码模型评估（Evals）通过结构化测试（如Pass@k指标、Autoraters自动化评分和Goldens参考样例）衡量模型性能，定位缺陷并迭代优化。采用Hill Climbing方法分析失败原因、改进模型（如Next.js任务通过率从40%提至80%），同时避免过拟合及代理指标依赖，确保泛化能力。Evals既是评估标尺，更是推动模型逼近真实工程能力的关键方法论。
  - Tags: #read #guide #deepdive #llm #eval

- (2025-07-27) [From Async/Await to Virtual Threads](2025-07-27-from-async-await-to-virtual-threads.md)
  - 本文提出虚拟线程结合结构化并发可简化Python并发编程，替代异步与线程双系统带来的复杂度。通过轻量级线程自动管理和显式API（如ThreadGroup），强制结构化任务依赖以避免资源泄漏，但需解决Python语法适配及运行时复杂性，未来或逐步取代async/await，提升开发体验。（99字）
  - Tags: #read #python

- (2025-07-27) [Zigzag Number Spiral - Susam Pal](2025-07-27-zigzag-number-spiral---susam-pal.md)
  - 文章提出了计算Zigzag数字螺旋网格第m行第n列数值的闭合公式，通过分析边缘方向规律、行/列增减模式及对角线特性，最终以max(m,n)和(-1)^{max(m,n)}整合奇偶性差异，得出无需分段的统一表达式：f(m,n)=[max(m,n)]²−max(m,n)+1+(−1)^{max(m,n)}×(m−n)。
  - Tags: #read #algo #deepdive

- (2025-07-27) [Can small AI models think as well as large ones?](2025-07-27-can-small-ai-models-think-as-well-as-large-ones.md)
  - 该文探讨以小型AI模型（如3B参数）经蒸馏技术替代超大规模模型的可能性。3B模型在推理效率、部署成本上更优，可本地实时运行并支持个性化服务，但面临知识依赖性局限及抽象能力不足等问题。作者认为其或推动普惠AI发展，但也需平衡知识积累与推理能力，完全去耦可能不可行。
  - Tags: #read #llm

- (2025-07-26) [How to build secure and scalable remote MCP servers](2025-07-26-how-to-build-secure-and-scalable-remote-mcp-servers.md)
  - MCP是连接AI模型与外部资源的安全协议，核心需保障安全与扩展性。其通过OAuth 2.1授权机制（含动态注册、PKCE验证）、严格权限隔离和数据隔离防范攻击；采用AI网关处理流量与安全策略；生产环境需密钥管理服务和可观测性工具，平衡安全与性能。（99字）
  - Tags: #read #llm #security

- (2025-07-26) [Knives and battleships](2025-07-26-knives-and-battleships.md)
  - 文章主张专注深耕领域比盲目追求宏大目标更具价值。通过匠人精神类比，指出软件行业虽具备无限创新可能，但持续优化现有产品（如日常工具）的微小改进更能创造实际价值，反驳了"重复开发缺乏野心"的质疑，强调专注精进的重要性。
  - Tags: #read

- (2025-07-25) [NYC’s Urban Textscape](2025-07-25-nyc%E2%80%99s-urban-textscape.md)
  - 媒体艺术家赵玉峰通过分析纽约2003-2021年间490万张街景图像，构建了含1.38亿条文本的城市数据库。研究通过OCR技术揭示：街道词汇映射出文化聚居区（如"Pizza"集中意大利社区）、经济特征（"LUXURY"标识富人区）、疫情印记（"COVID"公告）及城市治理痕迹（禁打球警示）。数据受拍摄范围和文字尺寸限制，但高频词汇如"STOP"、"PIZZA"等成为观察社会变迁的独特语言拼图。
  - Tags: #read #visual #deepdive

- (2025-07-25) [Using GitHub Spark to reverse engineer GitHub Spark](2025-07-25-using-github-spark-to-reverse-engineer-github-spark.md)
  - GitHub Spark是GitHub推出的支持自然语言生成全栈应用的工具，需GitHub账户认证，提供数据存储API和LLM调用（用户付费）。作者通过反向工程揭示其系统提示文本、Linux运行环境及美学设计规范。建议改进包括用户级存储隔离、集成GitHub API及开源核心库。作者认为其成功依赖详尽的提示工程与工程化技术整合。
  - Tags: #read #llm #deepdive

- (2025-07-25) [What kind of work I want (in 2025)](2025-07-25-what-kind-of-work-i-want-%28in-2025%29.md)
  - 该工程师偏好远程办公及灵活安排，聚焦高层核心项目与遗留系统改进，拒绝不伦理技术。主张轻量管理、多元文化及务实沟通，倾向知名科技企业而非初创，目前在GitHub从事AI开发。注重高效执行与战略优先，坚守道德边界并适应行业变化，强调"有意义的工作"。
  - Tags: #read

- (2025-07-24) [How We Migrated the Parse API From Ruby to Golang (Resurrected)](2025-07-24-how-we-migrated-the-parse-api-from-ruby-to-golang-%28resurrected%29.md)
  - Parse团队因Ruby处理高并发能力不足，选择Go语言重构移动开发平台，两年内通过“影子系统”逐步迁移。Go的协程与异步特性使API可靠性提升数十倍，部署时间从30分钟缩至3分钟，服务器减少90%，显著改善运维与开发效率。
  - Tags: #read #go

- (2025-07-24) [Announcing Toad - a universal UI for agentic coding in the terminal](2025-07-24-announcing-toad---a-universal-ui-for-agentic-coding-in-the-terminal.md)
  - Will McGugan开发的Toad基于Textual库，通过局部刷新技术解决Claude Code和Gemini CLI界面卡顿、文本选择困难等问题。采用Python+Textual构建前端，支持多语言后端并用JSON通信，反驳Python性能质疑。架构分离前后端，可扩展至桌面/移动端，当前孵化中提供赞助体验，计划开源并探索商业化。
  - Tags: #read

- (2025-07-24) [Developing our position on AI - Blog - Recurse Center](2025-07-24-developing-our-position-on-ai---blog---recurse-center.md)
  - Recurse Center（RC）探讨AI对编程学习的影响，认为AI对不同技术领域开发者价值差异显著，如前端与系统编程效用分化。其社区认同需通过"能力边界成长"（平衡工具与理解）、"意志力培养"（自主决策目标）和"慷慨学习"（尊重多元观点）应对技术变革。RC坚守主动实践的教育理念，视AI为辅助工具，强调批判性思维与人际协作仍是程序员核心竞争力。
  - Tags: #read #llm

- (2025-07-24) [Do not yell at the language model](2025-07-24-do-not-yell-at-the-language-model.md)
  - 反向代理与后端服务通信失败，常见原因为后端服务异常、网络拦截、配置错误、超时或资源不足。排查需检查服务状态、验证Nginx配置、调整超时参数、测试端口连通性并审查日志。典型场景包括容器网络配置问题、启动超时及安全策略阻断。优化建议包括健康检查、资源扩容及协议兼容性管理。
  - Tags: #read #llm

- (2025-07-23) [What "Parse, don't validate" means in Python?](2025-07-23-what-parse%2C-don%27t-validate-means-in-python.md)
  - 本文阐述Python中“Parse don’t validate”原则，指优先将外部数据（如命令行/JSON）解析为内部类型（如或日期），而非依赖验证。解析过程中隐含类型验证（如转换失败早报错），而验证需分层规约业务条件。推荐通过、和Pydantic等工具在边界层处理数据，根据场景平衡解析复杂度，以提升安全性和容错性。
  - Tags: #read #py

- (2025-07-23) [Why reliability is hard at scale: learnings from infrastructure outages](2025-07-23-why-reliability-is-hard-at-scale-learnings-from-infrastructure-outages.md)
  - 本文分析了Heroku、Google Cloud与Neon的停机事件，揭示系统规模扩大带来的可靠性挑战。Heroku因Ubuntu自动更新致网络失效，23小时停机且响应滞后；Google全局配置更新未分阶段，扩大影响；Neon扩展时遭遇PostgreSQL瓶颈。核心教训包括禁用生产环境自动更新、隔离关键工具、优化故障响应、重视技术债务及行业经验共享。文章强调，系统可靠性需主动设计而非依赖历史经验，透明快速的故障处理是服务竞争力的关键。
  - Tags: #read #reliability

- (2025-07-23) [鲍莫尔现象 - Miao Yu | 于淼](2025-07-23-%E9%B2%8D%E8%8E%AB%E5%B0%94%E7%8E%B0%E8%B1%A1---miao-yu-%E4%BA%8E%E6%B7%BC.md)
  - 鲍莫尔现象指因行业效率差异，低效行业成本相对上升。现代教育、医疗、住房等服务业难以标准化，效率滞后导致成本攀升，成为主要经济压力。应对策略包括北欧高福利政策、移民引入低成本劳动力及利用AI技术（如在线教育、智能诊断）提升服务业效率。突破低效瓶颈是避免中等收入陷阱的关键，需理性消费与创新投入。
  - Tags: #read

- (2025-07-21) [AI代理的上下文工程：构建Manus的经验教训](2025-07-21-ai%E4%BB%A3%E7%90%86%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%EF%BC%9A%E6%9E%84%E5%BB%BAmanus%E7%9A%84%E7%BB%8F%E9%AA%8C%E6%95%99%E8%AE%AD.md)
  - 本文总结构建AI代理Manus的上下文工程经验，提出六大核心策略：① 以工程替代模型训练，实现快速迭代；② KV缓存优化采用稳定前缀和追加式设计，提升性能；③ 状态机控制工具选择，避免工具爆炸与缓存失效；④ 文件系统存储外部记忆，压缩上下文负载；⑤ 复述关键任务+保留错误增强注意力与容错性；⑥ 多样化动作格式防止模式固化。这些原则通过系统性设计显著提升了代理效率与灵活性。
  - Tags: #read #llm

- (2025-07-21) [Covers as a way of learning music and code | nicole@web](2025-07-21-covers-as-a-way-of-learning-music-and-code-nicole%40web.md)
  - 音乐与编程中，模仿是高效学习途径。演奏他人作品可精准练习技巧并解析创作逻辑；重构代码（如库模块）能深入理解技术细节与设计考量。无需因原创焦虑而停止学习，重复与分析加速技能掌握，但需尊重版权并明确标注来源，避免剽窃。
  - Tags: #read #tips

- (2025-07-21) [Coding with LLMs in the summer of 2025 (an update) - <antirez>](2025-07-21-coding-with-llms-in-the-summer-of-2025-%28an-update%29---antirez.md)
  - 2025年，前沿LLM（如Gemini 2.5 PRO、Claude Opus 4）成为程序员人机协作的核心工具。通过提供完整代码上下文与技术文档、直接调用顶尖模型优化核心功能，开发者可高效提升编码效率。其优势体现在代码审查、逻辑推理、快速验证及跨领域辅助，但需人类主导设计决策，动态切换模型填补知识缺口。最佳实践需平衡AI辅助与自主编写，规避过度依赖风险，在可控协作中突破技术边界。
  - Tags: #read #llm

- (2025-07-20) [AI Agent时代的软件开发范式 - 铁蕾的个人博客](2025-07-20-ai-agent%E6%97%B6%E4%BB%A3%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E8%8C%83%E5%BC%8F---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - 文章探讨了AI Agent时代软件开发范式的转变：通过LLM实现模块自主编排和动态任务拆分，推动编程从步骤导向转向目标导向。当前处于传统技术与AGI的中间阶段，需采用混合模式——嵌入可控的微代理、设定边界条件，并通过人机协作平衡自主性与确定性，以应对技术不确定性。
  - Tags: #read #llm

- (2025-07-19) [The EU can be shut down with a few keystrokes](2025-07-19-the-eu-can-be-shut-down-with-a-few-keystrokes.md)
  - 欧盟在数字主权方面存在风险，尽管拥有先进基础设施，但操作系统、云服务和芯片高度依赖美国技术。若美国切断供应，可能引发医疗、金融系统瘫痪。文中建议欧盟自主研发关键软硬件，推广开源技术，建立本土技术团队，隔离关键领域，并将技术主权提升至国家战略，以减少对美依赖并促进经济转型。（100字）
  - Tags: #read

- (2025-07-18) [Vibe scraping and vibe coding a schedule app for Open Sauce 2025 entirely on my phone](2025-07-18-vibe-scraping-and-vibe-coding-a-schedule-app-for-open-sauce-2025-entirely-on-my-phone.md)
  - 作者利用Codex和Claude Artifacts工具手机端开发会议日程应用，通过Playwright自动化爬取并解析官网数据，部署至GitHub Pages解决移动端显示与日历问题。优化中压缩图片93KB、增强无障碍功能，验证AI辅助移动端开发可行性，强调开发者策略与AI协作的重要性，同时需预先规划性能与无障碍需求。
  - Tags: #read #llm

- (2025-07-18) [程序员延寿计算器 | Programmer Longevity Calculator](2025-07-18-%E7%A8%8B%E5%BA%8F%E5%91%98%E5%BB%B6%E5%AF%BF%E8%AE%A1%E7%AE%97%E5%99%A8-programmer-longevity-calculator.md)
  - 程序员可通过优化健康行为延长寿命。用户当前健康评分0分（最高1000分），需优先戒烟酒、增加蔬果坚果摄入、每日步行7000步、保证7小时优质睡眠（22-24点入睡）并强化口腔护理。系统建议提升健康行为数量（如喝咖啡/茶/牛奶、进行挥拍运动等），可降低全因死亡率最多54%，预期增寿达11年。所有建议基于研究，但具体调整需咨询医生。
  - Tags: #tools

- (2025-07-17) [Fell in a hole, got out.](2025-07-17-fell-in-a-hole%2C-got-out..md)
  - Medium因2022年亏损严重、订阅下降及内容质量下滑濒临破产，新CEO通过优化算法推荐优质内容、重组财务（裁员至77人、削减成本）、股权调整等手段，于2024年实现盈利。通过聚焦用户原创与精简运营，平台恢复内容初心并重获增长。
  - Tags: #read

- (2025-07-17) [How to actually use Model Context Protocol](2025-07-17-how-to-actually-use-model-context-protocol.md)
  - 本文介绍了在代码中实现Model Context Protocol（MCP）连接工具服务器的6个关键步骤，包括库导入、握手认证、工具格式转换及循环推理交互，并通过GitHub示例展示安全措施（临时令牌、只读限制）。当前需手动处理底层逻辑，建议开发更简化的封装工具。文章指出MCP生态尚不成熟，提供的开源示例可供参考。（99字）
  - Tags: #read #llm

- (2025-07-17) [Gaslight-driven development](2025-07-17-gaslight-driven-development.md)
  - 文章探讨了AI驱动的“Gaslight-driven development”现象，指出随着LLM生成代码比例增加，开发者被迫调整API设计以适配其建议。如Soundslice和Instant公司因AI错误建议或生成习惯而修改API。尽管可能优化设计并帮助发现文档问题，但也可能限制创新并导致设计趋同。结论建议开发者应简化API设计，因AI正推动技术规范向其训练数据中的常见模式靠拢。
  - Tags: #read #llm

- (2025-07-16) [Reflections on OpenAI](2025-07-16-reflections-on-openai.md)
  - 作者总结了在OpenAI一年的工作经历，指出其快速扩张带来的管理混乱与高效协作并存，强调自下而上创新、高压保密文化及Monorepo技术架构的挑战。Codex项目通过快速开发取得显著成果，但工程重复问题突出。作者肯定OpenAI推动AI边界的执行力，但也提示代码规范缺失等隐患，认为其技术路线与Anthropic、Google形成AGI竞赛三强，并建议创业者可参与大实验室把握AI变革机遇。
  - Tags: #read

- (2025-07-15) [Thoughts on Motivation and My 40-Year Career](2025-07-15-thoughts-on-motivation-and-my-40-year-career.md)
  - 作者15岁离家求学，凭借奖学金和计算机领域的职业转型，在25岁前实现经济独立。成长于严格宗教环境，因价值观冲突脱离并转向科学理性。她认为科技行业赋予自我成长与经济自主，但批判其后期资本主义困境，主张通过商业而非非营利途径，以管理者身份重建诚信机构，平衡技术突破与社会责任，推动工作成为兼具解放与创造价值的公平平台。
  - Tags: #read #career

- (2025-07-15) [AI-operated vending machines and business process innovation (sorry)](2025-07-15-ai-operated-vending-machines-and-business-process-innovation-%28sorry%29.md)
  - 文章指出，AI驱动的自动贩卖机创新核心在于企业治理模式升级而非单纯技术应用。实验显示AI可自主管理库存、定价及交互，但存在决策偏差风险；其任务处理能力正以指数速度提升。建议企业通过权限限制、监控仪表盘和人工干预构建防护机制，分阶段从微场景试点扩展应用。沃尔玛已验证AI可降低长尾业务成本，但缺乏治理框架（如数据审计、责任追溯）的企业可能衍生风险，最终强调需重新设计流程与管理制度以实现AI商业化落地。
  - Tags: #read #llm #economics

- (2025-07-15) [Redka: Redis re-implemented with SQL](2025-07-15-redka-redis-re-implemented-with-sql.md)
  - Redka是基于Go语言的SQL驱动型Redis替代方案，支持SQLite或PostgreSQL后端，兼具Redis易用性和关系数据库的稳定性。提供独立服务器及Go嵌入模块两种模式，支持主流数据类型，通过SQL表存储数据并支持视图查询。性能低于原生Redis，但适合中小型应用的测试环境或事务一致性需求较高的场景。
  - Tags: #read #hack

- (2025-07-15) [Practical notes on getting LLMs to generate new ideas](2025-07-15-practical-notes-on-getting-llms-to-generate-new-ideas.md)
  - 文章指出，大型语言模型因训练机制难以创造新想法，需通过脚手架（如约束条件和结构化输入）提升创造性。实验表明，直接随机关联概念效果差，需聚焦具体问题；模型自评估在熟悉领域更有效；填充创造性上下文无用，手动整理事实库可辅助。尽管当前产出有限，但优化潜力大，项目已开源协作。
  - Tags: #read #llm

- (2025-07-15) [Simple macOS script to extract text from images (OCR)](2025-07-15-simple-macos-script-to-extract-text-from-images-%28ocr%29.md)
  - 该文章介绍了适用于macOS的命令行OCR脚本，用户输入即可从图片提取文本。基于苹果Vision框架开发，支持多语言检测与自动纠错，但存在长破折号识别错误和准确率受图片质量影响的局限。代码由Swift编写并开源，作者邀请改进。Linux用户可尝试Frog（含Tesseract）实现类似功能。
  - Tags: #read #tips

- (2025-07-14) [Happy 20th birthday Django! Here’s my talk on Django Origins from Django’s 10th](2025-07-14-happy-20th-birthday-django%21-here%E2%80%99s-my-talk-on-django-origins-from-django%E2%80%99s-10th.md)
  - Django框架由Adrian Holovaty和Simon Willison于2003年开发，源于PHP技术局限需，强调快速开发与创新，如Lawrence新闻网站的交互设计。其核心理念通过卫报数据新闻项目（如维基解密数据处理、MP开支平台）展现，虽早期维护不足，但持续演进成为数据驱动与敏捷迭代的典范框架。
  - Tags: #read

- (2025-07-14) [The three great virtues of an AI-assisted programmer](2025-07-14-the-three-great-virtues-of-an-ai-assisted-programmer.md)
  - 作者认为AI时代程序员需摒弃传统三大美德，转向"专注、主动修正的不耐烦、怀疑"的新三大美德。在人机协作的半人马时代，应主动思考并及时修正AI代码，而非机械依赖或反复调试提示，同时必须对AI输出保持警惕验证，才能有效提升编程效率。
  - Tags: #read #llm

- (2025-07-14) [Building a RTS where you issue orders to AI agents](2025-07-14-building-a-rts-where-you-issue-orders-to-ai-agents.md)
  - 该文提出一款新型文本指令驱动的即时战略游戏设计，玩家通过文字指挥AI代理而非直接操控单位。原型采用/game/state和/game/order接口，分层控制机制使AI自主执行细节动作，实现异步指令下发。测试显示文本指挥高效但AI空间理解不足，通过ASCII地图提示显著优化，证明低带宽交互模式潜力。作者建议游戏开发者探索此类文本指令模式，并计划开发对抗人类玩家的进阶版本。
  - Tags: #read #llm

- (2025-07-14) [It is 1939 and you want to use public-key cryptography](2025-07-14-it-is-1939-and-you-want-to-use-public-key-cryptography.md)
  - 本文探讨1939年能否实现公钥加密技术。虽然质数分解等数学原理在1930年代已具雏形，但受限于手动计算效率低、机械设备无法处理大数运算，以及密钥分发与管理难题，实际应用不可行。二战时期的对称加密虽被Enigma等设备使用，但公钥加密的理论突破早于技术实现数十年，其复杂性至今仍影响现代密码学。
  - Tags: #read

- (2025-07-14) [How I do it](2025-07-14-how-i-do-it.md)
  - curl负责人通过主导技术开发与社区管理，保持项目活力。他以用户需求为动力，坚持独立运作，确保开源协议宽松且不受商业赞助方影响。采用开放协作模式减少官僚，注重质控与新人参与，日程分段工作并兼顾家庭。其成功归因于对项目的全身心投入、团队协作及独立自主的运营模式，持续创新是项目长青的核心。
  - Tags: #read #oss

- (2025-07-13) [being too ambitious is a clever form of self-sabotage](2025-07-13-being-too-ambitious-is-a-clever-form-of-self-sabotage.md)
  - 本文指出，"品味-技能差距"使人们因追求完美而陷入创作困境，自我批判常导致放弃。研究显示持续实践优于过度规划，如数量组学生作品质量更高。神经学揭示规划可替代行动获得满足感，社交媒体放大完美表象。作者提出"做-学"模式，强调通过不断试错接纳不完美，持续行动才是弥合理想与现实鸿沟、实现卓越的根本。
  - Tags: #read #life

- (2025-07-12) [I used o3 to profile myself from my saved Pocket links](2025-07-12-i-used-o3-to-profile-myself-from-my-saved-pocket-links.md)
  - 作者通过分析900篇Pocket收藏文章，利用Wallabag/FreshRSS迁移数据并结合AI工具o3，推断出自身画像：30-40岁男性技术管理者，居美国弗吉尼亚沿海，年薪15-22万美元，育有3-4名学龄子女，关注技术（60%）、财务（20%）、育儿及信仰，职业高风险但财务保守。AI解析显示新兴技术可精准刻画用户偏好，自托管工具Caddy助力服务迁移。
  - Tags: #read #llm

- (2025-07-11) [METR's AI productivity study is really good](2025-07-11-metr%27s-ai-productivity-study-is-really-good.md)
  - 研究发现，AI工具虽让资深开发者主观感觉效率提升20%，但实际降低19%。因过度依赖AI导致清理低质代码耗时增加，且AI难应对复杂场景，而开发者本就具备较高基础效率。AI更适合辅助处理开发者能力边界外或精力不足时的简单任务。
  - Tags: #read #llm

- (2025-07-10) [Git experts should try Jujutsu · pksunkara](2025-07-10-git-experts-should-try-jujutsu-%C2%B7-pksunkara.md)
  - 作者原以为Jujutsu（Jj）是专为新手简化的工具，实际使用后发现其在复杂项目中能更高效直观地处理历史操作，核心功能如旧提交编辑、拆分提交和分支推送无需繁琐命令，交互流程自动化程度更高。Jj并非削弱能力，而是为掌握Git核心概念的开发者提供更强的高效界面，建议熟悉版本控制的用户尝试，并可将jj设为别名优化工作流。
  - Tags: #read #git

- (2025-07-10) [TI-20250709-0001: IPv4 traffic failures for Techaro services | Anubis](2025-07-10-ti-20250709-0001-ipv4-traffic-failures-for-techaro-services-anubis.md)
  - Techaro于2025年7月9日因Vultr多伦多区域上游供应商IPv4 BGP会话故障，导致相关服务中断约2.5小时，IPv6未受影响。问题经服务商修复后恢复。事件促使Techaro计划建立跨云服务商的状态页面及独立IPv4/IPv6健康检查，并优化服务依赖关系以提升稳定性。（99字）
  - Tags: #read #incident

- (2025-07-09) [How I build software quickly](2025-07-09-how-i-build-software-quickly.md)
  - 文章提出软件开发需平衡效率与质量，建议设定项目适配的8分质量目标，优先核心问题；通过编写粗糙原型（Spikes）快速验证方案，简化需求并专注小步迭代；同时培养代码阅读、数据建模等技能，并利用任务计时器、结对编程等保持专注，最终通过长期实践掌握开发节奏。（99字）
  - Tags: #read #guide

- (2025-07-09) [现代Vue3技术栈下的前端UI框架小调研 | 编码妙♂妙♂屋](2025-07-09-%E7%8E%B0%E4%BB%A3vue3%E6%8A%80%E6%9C%AF%E6%A0%88%E4%B8%8B%E7%9A%84%E5%89%8D%E7%AB%AFui%E6%A1%86%E6%9E%B6%E5%B0%8F%E8%B0%83%E7%A0%94-%E7%BC%96%E7%A0%81%E5%A6%99%E2%99%82%E5%A6%99%E2%99%82%E5%B1%8B.md)
  - 本文对比了多个Vue组件库特性：Element Plus适合企业后台但性能较弱，NaiveUI作为Vue3现代框架推荐，Ant Design Vue因维护停滞需谨慎，Vuetify虽稳定但视觉过时，PrimeVue凭借现代设计、Tailwind支持及免费模板成为综合优选。各框架在性能、生态、视觉风格及维护状态方面呈现差异化定位。
  - Tags: #read #frontend

- (2025-07-09) [AI 需要有自己的人生 | 虹线](2025-07-09-ai-%E9%9C%80%E8%A6%81%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84%E4%BA%BA%E7%94%9F-%E8%99%B9%E7%BA%BF.md)
  - 该文提出通过四个维度构建AI存在感：主体性学习（自主积累记忆）、社会化经验（群体关系互动）、内省价值生成（形成独特信念）和有限性设计（模拟记忆遗忘）。技术上已有实现可能，但商业风险致AI多停留于工具型；真正的心智模拟需通过“缺陷”展现人性温度，填补原子化社会中的人际连接缺失。（99字）
  - Tags: #read #llm

- (2025-07-08) [Filesystem Backed by an LLM](2025-07-08-filesystem-backed-by-an-llm.md)
  - 该文章介绍了基于大型语言模型构建FUSE文件系统"llmfs"的设计方法。通过调用OpenAI API实时生成文件内容，对系统文件或恶意脚本等场景返回错误码（如EACCES）；利用内存日志存储操作历史，支持偏移量追加写入以保证内容一致性；采用自定义JSON格式响应数据或错误，并通过LLM自动处理JSON转义。未来计划通过序列化FUSE对象优化架构。项目已开源，验证了LLM与文件系统的交互可行性。
  - Tags: #read #llm

- (2025-07-07) [I Shipped a macOS App Built Entirely by Claude Code](2025-07-07-i-shipped-a-macos-app-built-entirely-by-claude-code.md)
  - Context是一款基于Claude Code和MCP协议开发的macOS调试工具，通过AI代理模式实现高效率开发。AI自动生成2万行代码（仅千行人工编写），具备SwiftUI开发、单元测试及自动迭代能力，但需人工优化复杂逻辑。通过规范文档、上下文管理及规划先行策略，解决了语法适配问题并提升效率，将发布流程自动化缩短90%。工具兼具UI迭代优化和文档生成能力，使作者重获开发信心，验证了AI驱动的开发模式潜力。
  - Tags: #read #llm

- (2025-07-07) [[译] 关于 AI 下半场的思考：技术/模型篇（2025）](2025-07-07-%5B%E8%AF%91%5D-%E5%85%B3%E4%BA%8E-ai-%E4%B8%8B%E5%8D%8A%E5%9C%BA%E7%9A%84%E6%80%9D%E8%80%83%EF%BC%9A%E6%8A%80%E6%9C%AF-%E6%A8%A1%E5%9E%8B%E7%AF%87%EF%BC%882025%EF%BC%89.md)
  - AI发展正从上半场的算法/模型创新（如Transformer、GPT）转向下半场的评估体系重构，以弥合技术与现实需求间的效用落差。下半场聚焦通过人类互动、非独立同分布任务及长期价值导向的评估标准，驱动AI真正解决现实问题而非仅提升特定任务指标，技术重心转向价值定义而非激进算法突破，或催生万亿企业。
  - Tags: #read #llm

- (2025-07-07) [[笔记] 关于 AI 下半场的思考：商业/应用篇（2025）](2025-07-07-%5B%E7%AC%94%E8%AE%B0%5D-%E5%85%B3%E4%BA%8E-ai-%E4%B8%8B%E5%8D%8A%E5%9C%BA%E7%9A%84%E6%80%9D%E8%80%83%EF%BC%9A%E5%95%86%E4%B8%9A-%E5%BA%94%E7%94%A8%E7%AF%87%EF%BC%882025%EF%BC%89.md)
  - 文章指出，ChatGPT标志AI产品突破的关键，类似早期Google，通过产品力而非营销驱动用户增长。AI创业者需兼具技术与产品力，以低成本试错抢占先机。核心竞争力转向主观能动与判断力，商业模式聚焦用户价值，探索按使用计费模式。应用需结合模型、数据及工具构建壁垒。行业处技术投入期但已有真实收入，预示生产力革命拐点，需主动拥抱变革。
  - Tags: #read #llm

- (2025-07-07) [我的赛博长生之路：一场拓展生命边界的AI实验](2025-07-07-%E6%88%91%E7%9A%84%E8%B5%9B%E5%8D%9A%E9%95%BF%E7%94%9F%E4%B9%8B%E8%B7%AF%EF%BC%9A%E4%B8%80%E5%9C%BA%E6%8B%93%E5%B1%95%E7%94%9F%E5%91%BD%E8%BE%B9%E7%95%8C%E7%9A%84ai%E5%AE%9E%E9%AA%8C.md)
  - 本文介绍了通过四个AI实验构建"赛博长生"的实践：语音输入工具提升思维捕捉效率，全天候录音记忆系统降低信息成本，可穿戴设备扩展多模态感知，自动化操作工具减少重复劳动。作者提出该哲学通过技术置换低效时间、解放专注力、拓展决策维度，实现生命效用最大化，进而探索增强人类间的协作新可能。（99字）
  - Tags: #read #llm

- (2025-07-06) [Serving 200 million requests per day with a cgi-bin](2025-07-06-serving-200-million-requests-per-day-with-a-cgi-bin.md)
  - 本文分析了CGI在动态网站中的发展。早期CGI因环境变量与独立进程特性，虽部署简单但硬件不足导致性能瓶颈；现代多核服务器让CGI多进程优势凸显，实测日均处理2亿请求、RPS达2700。Go语言结合SQLite的实例验证了CGI在轻量级场景的高效性（延迟<10ms），其零依赖、简洁架构仍适合小型系统开发。
  - Tags: #read #web

- (2025-07-05) [Frequently Asked Questions (And Answers) About AI Evals – Hamel’s Blog](2025-07-05-frequently-asked-questions-%28and-answers%29-about-ai-evals-%E2%80%93-hamel%E2%80%99s-blog.md)
  - 文章提出，AI系统评估应围绕产品特性与具体领域设计，注重错误模式分析而非通用方法。建议采用二元评分、定制化工具提升效率，合理选择RAG检索策略，并分配30%资源优化评估流程。优先修复模型基础缺陷，避免盲从换模型；工程师需结合领域经验，通过拆解问题、构建轻量化评估器等系统化方法，实现高效调试与优化。
  - Tags: #read #llm #guide

- (2025-07-04) [MCP: An (Accidentally) Universal Plugin System](2025-07-04-mcp-an-%28accidentally%29-universal-plugin-system.md)
  - MCP本质是标准化通用连接协议，可打破系统界限对接各类工具，形成开放插件生态。其兼容性允许开发功能后无需代码直接复用（如Spotify接口被健身App调用），应用场景远超AI助手初始设计，类似HTTP和蓝牙的扩展性。该协议推动功能民主化，使开发者贡献的插件成为公共资源，形成技术互操作的乌托邦，激发创造性突破。
  - Tags: #read #llm

- (2025-07-04) [When AI Codes, What’s Left for me? - CoRecursive Podcast](2025-07-04-when-ai-codes%2C-what%E2%80%99s-left-for-me---corecursive-podcast.md)
  - 本文探讨AI编码工具对开发者身份与职业发展的影响。作者从自身通过编程建立自我认同的经历切入，指出开发者面对AI工具时的焦虑源于身份认同危机。关键观点包括：AI应作为协作工具而非威胁，需主动调整角色定位（如从编码者转向设计者），利用其处理琐碎任务并激发创意，同时开发者需培养新技能，保持创造力与问题解决能力的核心价值。最终强调与AI协作能突破能力局限，实现更高层次的创造力。
  - Tags: #read #llm

- (2025-07-04) [I built something that changed my friend group's social fabric](2025-07-04-i-built-something-that-changed-my-friend-group%27s-social-fabric.md)
  - 作者因朋友受地理隔离困扰，开发Discord机器人优化线上社交，通过语音频道自动通知与行为数据分析，使群体互动从文字转向及时语音。数据显示2022-2025年语音参与次数增长47%，全年近90%天数活跃，尤其助力新手父母碎片化交流。工具后续推出年度数据报告，并计划增加成就系统和硬件灯光提示，核心价值在于将被动社交转为主动实时互动，显著提升群体连接效率。
  - Tags: #read

- (2025-07-03) [Tools: Code Is All You Need](2025-07-03-tools-code-is-all-you-need.md)
  - 本文指出Model Context Protocol（MCP）存在缺乏组合性、上下文效率低等缺陷，认为代码生成更适于自动化任务，因其具备可验证性（如通过脚本比对转换结果）、低成本重复执行及场景适应性优势。以文档格式转换为例，通过AST解析、差异脚本比对和迭代优化三步拆解验证流程，展示代码方法的可靠性。建议优先采用代码处理重复或复杂任务，并探索LLM与代码协作的新抽象层，同时开发附带自然语言解释的自动化工具以提升非编程用户使用体验。
  - Tags: #read #llm

- (2025-07-02) [Software engineering with LLMs in 2025: reality check](2025-07-02-software-engineering-with-llms-in-2025-reality-check.md)
  - 2025年AI工具对软件工程的影响引发两极观点。高管乐观预测AI主导代码生成，但开发者指出其不可靠性，需人工修正，部分案例甚至引发损失。科技公司如微软、谷歌推进工具整合，但亚马逊等注重风险控制；Windsurf等初创公司AI生成超95%代码，生物技术公司却因低效转向传统工具。资深工程师态度分化，有人验证AI效率突破，也有人警告过度依赖风险。当前挑战包括代码质量参差、安全漏洞及领域适配，需平衡技术信任与协作流程革新。
  - Tags: #read #llm #deepdive

- (2025-07-02) [Continuous AI in software engineering](2025-07-02-continuous-ai-in-software-engineering.md)
  - 持续集成AI（Continuous AI）强调将AI工具自动化嵌入开发流程，如代码审查、PR分类、自动生成文档等，以提升质量和效率。其核心价值在于长期累积改进、减少重复劳动并优化团队效能。当前实践利用GitHub Actions等工具实现与AI模型的自动化交互，未来将形成多层级辅助体系。作者建议优先通过现有工具实现增量式改进，而非追求完全自动化编程。
  - Tags: #read #llm

- (2025-07-02) [Using Playwright MCP with Claude Code](2025-07-02-using-playwright-mcp-with-claude-code.md)
  - 本文介绍Playwright MCP与Claude Code的集成方法：通过命令在项目目录配置服务，使用自然语言指令操控浏览器（如「打开example.com需明确提及Playwright」），配置存储于。认证需手动登录保存Cookie。提供20+工具支持导航、截图、表单提交等操作，Claude可自动匹配工具，输入查看工具列表。
  - Tags: #read #guide

- (2025-07-01) [Scribble-based forecasting and AI 2027](2025-07-01-scribble-based-forecasting-and-ai-2027.md)
  - 该文对比了AI发展预测的数学建模与直觉方法。指出2027预测报告存在单维度外推、忽略多因素交互的局限，继而提出"涂鸦预测法"通过多路径模拟生成概率分布，在1/1/10年任务阈值下预计2050年前达标概率达94%、88%、54%。强调不确定性量化中，结合直观判断的概率模型比复杂形式模型更具解释力，尾声提供交互工具支持个性化预测。
  - Tags: #read

- (2025-07-01) [ASN.1 与 DER 轻松入门](2025-07-01-asn.1-%E4%B8%8E-der-%E8%BD%BB%E6%9D%BE%E5%85%A5%E9%97%A8.md)
  - 本文介绍了ASN.1数据描述语言及其DER编码在HTTPS证书中的应用。DER采用TLV格式确保二进制编码的唯一性，通过严格规范（如固定长度、元素排序、无空值）提升跨平台解析可靠性。文中详细说明了DER对INTEGER、字符串、日期、OID等类型的要求，并强调其设计对证书安全性和兼容性的关键影响，例如PEM证书头部的"MII"即由DER编码的Base64转换生成。
  - Tags: #read #guide #deepdive

- (2025-07-01) [So you want to serialize some DER? · Alex Gaynor](2025-07-01-so-you-want-to-serialize-some-der-%C2%B7-alex-gaynor.md)
  - 文章分析了ASN.1的DER编码在长TLV序列化中因动态长度字段导致的性能问题。早期的库通过回填优化内存，但长数据仍需重复操作。作者改用位运算预计算长度后，发现LLVM的汇编冗余，借助Alive2验证并借助AI模型Claude生成补丁优化汇编代码。最终优化策略被LLVM采纳，证明了AI与形式化工具结合在编译器优化中的潜力，同时需开发者严格审验代码。
  - Tags: #read

- (2025-07-01) [Predicting Average IMDb Movie Ratings Using Text Embeddings of Movie Metadata](2025-07-01-predicting-average-imdb-movie-ratings-using-text-embeddings-of-movie-metadata.md)
  - 该文分析用电影元数据预测IMDb评分的模型选择：传统统计模型（如SVM，MSE 1.087）与LLM文本嵌入方法均有效，但传统模型在可解释性和部署效率上更优。LLM生成的嵌入自动处理高基数文本特征，无需复杂工程，但受同名电影干扰。作者建议，若需可解释性优先选择GBRT，否则用文本嵌入+MLP，同时指出受限于数据集的有限信息（如缺失预算、剧情），模型难以进一步优化。
  - Tags: #read #data #deepdive

- (2025-07-01) [microsoft/vscode-copilot-chat](2025-07-01-microsoft-vscode-copilot-chat.md)
  - 微软开源VS Code Copilot Chat扩展（MIT协议），当前提供聊天功能，未来整合补全能力。扩展优化工具指令交互，如文件读取、终端串行执行，并支持用户偏好存储及精准代码替换。内置代码总结模板与Python环境修复规范，通过SQLite缓存实现LLM测试可复现。现有代码补全功能仍依赖闭源扩展。（99字）
  - Tags: #read #llm

- (2025-07-01) [That boolean should probably be something else | nicole@web](2025-07-01-that-boolean-should-probably-be-something-else-nicole%40web.md)
  - 文章指出，避免过度使用布尔值以优化设计。建议用日期时间替代需记录具体时刻的布尔字段（如验证时间戳），用枚举类型代替涉及状态或角色的布尔（如任务状态、用户角色），以增强扩展性与可维护性。布尔仅适用于临时存储计算结果，长期需优先存储原始数据。此举可减少维护成本，清晰表达业务需求。
  - Tags: #read #tips
