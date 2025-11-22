# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-11-22) [We should all be using dependency cooldowns](202511/2025-11-22-we-should-all-be-using-dependency-cooldowns.md)
  - 文章主张通过设定“依赖冷却期”（如7-14天）延迟引入新依赖，以避开开源供应链攻击的高风险窗口。该措施成本低、易实施，能防御多数短期攻击，虽非万能但可显著降低风险，建议广泛采用。
  - Tags: #read #security

- (2025-11-22) [What if you don't need MCP at all?](202511/2025-11-22-what-if-you-don%27t-need-mcp-at-all.md)
  - 本文提倡用自定义命令行工具和代码替代复杂的MCP服务器，以浏览器工具为例展示了简单方案的优越性。通过短小精悍的脚本实现浏览器控制、页面操作等功能，显著节省上下文资源且易于扩展。强调利用代码组合性和代理执行能力可构建高效灵活的工作流，适合需要代码执行的场景。
  - Tags: #read #llm

- (2025-11-22) [Agent Design Is Still Hard](202511/2025-11-22-agent-design-is-still-hard.md)
  - 2025年智能体开发经验显示，构建智能体仍面临多项挑战：推荐直接使用底层SDK以灵活处理工具调用与缓存；需显式管理缓存、注入引导信息强化任务推进，并通过子代理隔离失败；模型选择需兼顾成本与效能，测试尚无理想方案。整体看，智能体开发仍处精细探索阶段。
  - Tags: #read #llm #deepdive #guide

- (2025-11-21) [Programmers and Sadomasochism](202511/2025-11-21-programmers-and-sadomasochism.md)
  - 文章通过HTML属性示例，比较了严格（如XML）与宽松（如HTML）解析器的行为，主张遵循Postel定律，建议采用宽容的解析策略来提高互操作性，认为严格验证反而增加沟通成本，不利于实际应用。
  - Tags: #read #people

- (2025-11-21) [Make product worse, get money](202511/2025-11-21-make-product-worse%2C-get-money.md)
  - 文章探讨产品服务质量差的原因，指出商家虽有动机降低质量，但问题在于竞争缺失或消费者需求偏好。核心因素包括：消费者追求低价、信息不对称、品味差异和市场垄断，这些因素共同导致劣质服务持续存在。
  - Tags: #read

- (2025-11-21) [Fizz Buzz with Cosines - Susam Pal](202511/2025-11-21-fizz-buzz-with-cosines---susam-pal.md)
  - 本文通过数学建模将Fizz Buzz问题转化为有限傅里叶级数，利用余弦函数构造闭合表达式，并用Python代码实现。这种方法将简单游戏抽象为三角函数组合，展现了数学趣味性而非实用性。
  - Tags: #read #math #hack

- (2025-11-21) [Systems design 3: LLMs and the semantic revolution](202511/2025-11-21-systems-design-3-llms-and-the-semantic-revolution.md)
  - 本文回顾了系统互联的历史，强调互联网基于Postel容错法则取得成功，指出严格标准（如XML）常失效。近年来LLM突破性地解决了语义层互联问题，但带来新风险。互联本质是渐进过程，需在创新与治理间寻找平衡。
  - Tags: #read #llm #deepdive

- (2025-11-20) [How we’re making GitHub Copilot smarter with fewer tools](202511/2025-11-20-how-we%E2%80%99re-making-github-copilot-smarter-with-fewer-tools.md)
  - GitHub Copilot通过自适应工具聚类、嵌入引导工具路由和精简默认工具集三大技术优化，显著提升了响应速度和工具选择效率。改进后，工具使用覆盖率提升至94.5%，延迟降低，为未来智能代理工作流打下基础。
  - Tags: #read #llm

- (2025-11-20) [Are large language models worth it?](202511/2025-11-20-are-large-language-models-worth-it.md)
  - 网站nicholas.carlini.com因疑似遭受DoS攻击（DOM元素过多）被阻止匿名访问，封禁持续至2039年底，错误代码45102。
  - Tags: #read #llm

- (2025-11-20) [谈谈工作中的犯错 | CatCoding](202511/2025-11-20-%E8%B0%88%E8%B0%88%E5%B7%A5%E4%BD%9C%E4%B8%AD%E7%9A%84%E7%8A%AF%E9%94%99-catcoding.md)
  - 文章通过真实案例总结了工作中常见错误类型及教训，如信息泄露、接口问题、并发和配置错误。建议通过防御编程、自动化流程和良好工作习惯，如测试、代码审查和风险控制，来降低犯错风险。强调保持敬畏，避免小错误引发大问题。
  - Tags: #read

## Monthly Archive

- [2025-11](202511/monthly-index.md) (65 entries)
- [2025-10](202510/monthly-index.md) (67 entries)
- [2025-09](202509/monthly-index.md) (40 entries)
- [2025-08](202508/monthly-index.md) (46 entries)
- [2025-07](202507/monthly-index.md) (77 entries)
- [2025-06](202506/monthly-index.md) (75 entries)
- [2025-05](202505/monthly-index.md) (65 entries)
- [2025-04](202504/monthly-index.md) (61 entries)
- [2025-03](202503/monthly-index.md) (49 entries)
- [2025-02](202502/monthly-index.md) (32 entries)
- [2025-01](202501/monthly-index.md) (41 entries)
- [2024-12](202412/monthly-index.md) (45 entries)
- [2024-11](202411/monthly-index.md) (57 entries)
- [2024-10](202410/monthly-index.md) (34 entries)
- [2024-09](202409/monthly-index.md) (46 entries)
- [2024-08](202408/monthly-index.md) (31 entries)
- [2024-07](202407/monthly-index.md) (12 entries)
