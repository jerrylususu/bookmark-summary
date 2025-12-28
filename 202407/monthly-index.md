# 2024-07 Monthly Index

- (2024-07-31) [We had an AI attempt to make a data-driven story like we do at The Pudding](2024-07-31-we-had-an-ai-attempt-to-make-a-data-driven-story-like-we-do-at-the-pudding.md)
  - 文章探讨了AI在数据驱动视觉故事讲述中的应用，通过使用Claude进行实验，评估其在创意生成、数据收集与分析、故事板与原型设计、开发与写作各阶段的表现。结果显示AI在特定任务上表现出色，但在整体项目连贯性和复杂任务处理上仍需改进，表明AI目前无法替代人类故事讲述者的精细工艺和迭代过程。未来计划将AI作为工具用于特定任务，如脚本写作和创意头脑风暴。
  - Tags: #read

- (2024-07-29) [The Many Lives of Null Island | Stamen](2024-07-29-the-many-lives-of-null-island-stamen.md)
  - Null Island是一个地图制作者间的内部笑话，位于0º纬度和0º经度，常因数据错误显示在此。实际例子包括PurpleAir传感器、Weather Underground和Strava的GPS轨迹地图。其在地图上的表现形式多样，历史悠久，形状设计独特，且具有一定的社会和文化影响。尽管地理位置偏远，Null Island已成为地图文化中的一个持久现象。
  - Tags: #read

- (2024-07-27) [Exposition of Frontend Build Systems](2024-07-27-exposition-of-frontend-build-systems.md)
  - 前端构建系统通过转译、打包和压缩等步骤，解决语言特性支持不足和性能问题。转译工具如Babel将现代JavaScript转换为旧版本，打包工具如Webpack合并文件减少请求，压缩工具如Terser减少文件大小。此外，元框架和构建工具提供预配置系统，源映射支持调试，热重载提高开发效率，单一代码库促进多团队协作。趋势显示，性能导向的新工具和SSR的普及是当前的发展方向。
  - Tags: #frontend #deepdive

- (2024-07-26) [Anyone can Access Deleted and Private Repository Data on GitHub ◆ Truffle Security Co.](2024-07-26-anyone-can-access-deleted-and-private-repository-data-on-github-%E2%97%86-truffle-security-co..md)
  - GitHub允许访问已删除和私有仓库的数据，这些数据永久可用。通过跨分支对象引用（CFOR）漏洞，用户可以访问不应见的提交数据。常见工作流程中，分叉和删除仓库后，提交的代码仍可访问，导致API密钥等敏感信息泄露。GitHub已知此设计并文档化，用户应预期上述情况发生。
  - Tags: #hack

- (2024-07-24) [How to review code effectively: A GitHub staff engineer’s philosophy](2024-07-24-how-to-review-code-effectively-a-github-staff-engineer%E2%80%99s-philosophy.md)
  - 代码审查是提高软件质量的关键，通过GitHub的拉取请求系统，可以有效管理和优化审查流程。良好的审查应清晰沟通、提供具体示例，并避免偏见。自我审查和使用自动化工具能进一步提升审查效率和价值。
  - Tags: #guide #deepdive

- (2024-07-24) [We need visual programming. No, not like that.](2024-07-24-we-need-visual-programming.-no%2C-not-like-that..md)
  - 可视化编程应关注开发者实际需求，如代码库、网络拓扑、内存布局、状态机和请求/响应协议的可视化，而非替代代码语法和业务逻辑。现有工具如Sourcetrail、AWS服务拓扑图等已展示其价值，但仍需更多发展以满足开发者需求。
  - Tags: #read

- (2024-07-24) [How we improved availability through iterative simplification](2024-07-24-how-we-improved-availability-through-iterative-simplification.md)
  - 文章讨论了GitHub如何通过使用Datadog、Splunk等工具和自定义监控器来提高系统可用性和性能，特别是在优化数据库查询和移除未使用代码方面取得了显著成效。强调了投资于可观察性和逐步变更的重要性，以及持续监控对于预防性能问题恶化的关键作用。
  - Tags: #read

- (2024-07-23) [Python Practical Package Packing 2024](2024-07-23-python-practical-package-packing-2024.md)
  - 现代Python项目应使用和Poetry管理依赖和环境，避免过时的工具如和，推荐使用Poetry进行依赖解析和虚拟环境管理，以及使用和标准代码格式化工具提高代码质量。
  - Tags: #python #guide

- (2024-07-23) [Panic! at the Tech Job Market](2024-07-23-panic%21-at-the-tech-job-market.md)
  - 文章通过分析技术工作市场的多个方面，揭示了招聘流程的不合理性、工作描述的不切实际以及收入不平等的问题，强调了实际工作经验和能力的重要性。
  - Tags: #read #job

- (2024-07-22) [How not to use box shadows](2024-07-22-how-not-to-use-box-shadows.md)
  - 本文探讨了box shadows的创造性应用，包括多层叠加、颜色变化、3D效果模拟等，展示了其在图形设计中的深度和性能优势，并通过Ray Tracing实验展示了其潜力。
  - Tags: #hack #deepdive #visual

- (2024-07-20) [Mapping the landscape of gen-AI product user experience](2024-07-20-mapping-the-landscape-of-gen-ai-product-user-experience.md)
  - 文章讨论了生成式AI产品的多样性和设计模式，从第一代AI产品地图到当前用户体验地图，涵盖了工具、副驾驶、代理和聊天等多种用户体验分类。文章还指出了用户体验的挑战，并介绍了地图的应用和局限性。
  - Tags: #read #guide

- (2024-07-20) [Mocking is an Anti-Pattern](2024-07-20-mocking-is-an-anti-pattern.md)
  - 文章强调了测试的重要性，指出使用mock测试可能忽略边缘情况和失败模式。建议通过增加单元测试、简化IO测试、分离逻辑与IO、进行E2E集成测试等替代方案来提高测试覆盖率和准确性，避免mock带来的问题。
  - Tags: #deepdive
