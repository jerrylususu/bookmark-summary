# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-01-11) [A Survey of Dynamic Array Structures](202601/2026-01-11-a-survey-of-dynamic-array-structures.md)
  - 文章系统比较了六类动态数组结构，包括双倍复制数组、内存池数组、分块数组、链接块数组、树结构数组和指数数组，分析了各自的设计特点、优缺点及适用场景。作者倾向于使用内存池管理，强调需根据数据连续性、指针稳定性和内存效率等需求权衡选择。
  - Tags: #read #deepdive

- (2026-01-11) [Writing First, Tooling Second - Susam's Maze](202601/2026-01-11-writing-first%2C-tooling-second---susam%27s-maze.md)
  - 建立个人网站应优先写作而非纠结工具选择。从纯HTML起步，发布至少5篇文章后再考虑工具优化，避免过度工程化。内容是核心，工具应服务于表达而非取代创作。
  - Tags: #read

- (2026-01-11) [A Software Library with No Code](202601/2026-01-11-a-software-library-with-no-code.md)
  - 作者提出“无代码”软件库（如whenwords），仅依赖规格说明和测试用例，通过AI自动生成代码。这种方法适合简单工具，但复杂、高性能或需社区支持的场景仍需传统代码库。AI或改变编码方式，但代码实现和社区价值不会消失。
  - Tags: #read

- (2026-01-10) [John Carmack on Inlined Code](202601/2026-01-10-john-carmack-on-inlined-code.md)
  - 约翰·卡马克认为内联代码能减少状态依赖和bug，提升可读性与性能。建议优先内联单次调用函数，用注释分隔代码块，并注重纯函数与一致性执行路径。需根据场景权衡内联与模块化，特别适用于游戏开发等实时系统。
  - Tags: #read #design

- (2026-01-10) [A complete guide to the HTML number input](202601/2026-01-10-a-complete-guide-to-the-html-number-input.md)
  - 本文全面介绍了HTML数字输入框的特性、使用方法和注意事项，包括如何自定义按钮、处理本地化、验证数据和移动端支持，强调在现代浏览器中合理使用可以提升用户体验。
  - Tags: #read #deepdive #frontend

- (2026-01-10) [Fly’s new Sprites.dev addresses both developer sandboxes and API sandboxes at the same time](202601/2026-01-10-fly%E2%80%99s-new-sprites.dev-addresses-both-developer-sandboxes-and-api-sandboxes-at-the-same-time.md)
  - Fly.io推出Sprites.dev，提供持久化沙盒环境与API服务，支持快速创建、检查点回滚和安全运行代码。旨在通过按需计费和隔离环境，为开发者及API用户提供安全、经济的沙盒解决方案。
  - Tags: #read #llm #security

- (2026-01-09) [HTTP caching, a refresher · Dan Cătălin Burzo](202601/2026-01-09-http-caching%2C-a-refresher-%C2%B7-dan-c%C4%83t%C4%83lin-burzo.md)
  - 本文基于RFC 9111标准，解析了HTTP缓存的运行机制，包括缓存新鲜度判断、存储控制、关键Cache-Control指令及其应用场景。文章强调缓存默认启用，但需结合浏览器和中间件的实际兼容性谨慎配置。
  - Tags: #read #deepdive

- (2026-01-09) [Why Object of Arrays (SoA pattern) beat interleaved arrays: a JavaScript performance rabbit hole | Royal Bhati's Blog](202601/2026-01-09-why-object-of-arrays-%28soa-pattern%29-beat-interleaved-arrays-a-javascript-performance-rabbit-hole-royal-bhati%27s-blog.md)
  - 通过对比数组结构（AoS）和结构数组（SoA）在JavaScript中的性能，发现SoA模式速度提升4倍，优势源于减少对象分配、优化循环和属性访问。SoA核心通过连续内存布局降低开销，更适合大数据场景。
  - Tags: #read #perf

- (2026-01-09) [Opus 4.5 is going to change everything](202601/2026-01-09-opus-4.5-is-going-to-change-everything.md)
  - Burke Holland通过亲身体验Claude Opus 4.5 AI编码代理，认为它已能完全替代开发者，可高效完成图像转换、视频编辑、社交媒体工具等复杂项目。作者强调需转向"AI可维护"的编程范式，优化代码结构以适应AI迭代，同时警惕安全风险。
  - Tags: #read #llm

- (2026-01-09) [How Markdown took over the world - Anil Dash](202601/2026-01-09-how-markdown-took-over-the-world---anil-dash.md)
  - Markdown是一种轻量级标记语言，2004年由John Gruber创建，旨在简化文本格式化。它因简洁、开源、恰逢博客兴起而迅速普及，成为开发者及日常工具的通用格式。其成功源于解决实际需求、开放社区协作和免费共享精神。
  - Tags: #read #deepdive #history

## Monthly Archive

- [2026-01](202601/monthly-index.md) (19 entries)
- [2025-12](202512/monthly-index.md) (68 entries)
- [2025-11](202511/monthly-index.md) (78 entries)
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
