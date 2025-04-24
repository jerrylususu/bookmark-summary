# Better typography with text-wrap pretty
- URL: https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/
- Added At: 2025-04-24 13:35:55
- [Link To Text](2025-04-24-better-typography-with-text-wrap-pretty_raw.md)

## TL;DR


Safari Technology Preview 216引入CSS属性`text-wrap`优化排版，其中`pretty`通过全局多行算法减少短行、参差边缘及排版间隙，提升可读性，适合长文本；`balance`则均衡短文本行距，适合标题但可能缩窄段落宽度。此属性性能强于Chrome等竞品，开发者可采用`auto`(默认)、`stable`(逐行断行)等值适配不同场景，未来将扩展支持并分段优化长文本，建议通过在线工具测试并反馈效果。

## Summary


- **功能概述**：Safari Technology Preview 216引入了`text-wrap: pretty`，通过段落级算法优化排版，解决末行短行、参差边缘、连字符滥用及排版河流问题，提升可读性和美观度。
- **传统排版规则**：
  - 避免末行单字短行。
  - 减少“糟糕的参差边缘”（不规则的段落版心）。
  - 避免过多或不必要的连字符。
  - 消除排版河流（字词间隙对齐形成的空白路径）。
- **现代Web排版问题**：浏览器长期以来仅逐行断行，缺乏多行优化，导致排版不佳，而软件如Adobe InDesign通过多行算法改善这种情况。
- **text-wrap: pretty**：
  - 全局优化段落内所有行，调整断行位置以减少参差边缘和连字符，同时确保末行非短行。
  - 相较于Chrome等浏览器仅优化最后四行，WebKit的实现覆盖整段，性能优化更强，适合长文本。
  - 提供“显示引导线”和“幽灵文本”功能，直观对比调整效果。
- **text-wrap: balance**：
  - 调整多行长度使其均衡，适合标题等短文本，但可能使段落整体宽度缩窄，影响容器对齐。
  - 若用于长文本会导致排版混乱，应谨慎使用。
- **其他text-wrap值**：
  - **avoid-short-last-lines**（新值）：仅解决末行短行，尚未实现。
  - **auto**：默认逐行算法，未来可能升级为多行优化。
  - **stable**：保持逐行断行，避免动态内容排版变化，适用于编辑区域或动画场景。
- **性能考量**：
  - `pretty`的性能不受元素应用数量影响，但在超长段落（数百行以上）可能有潜在问题。
  - WebKit计划分段优化长文本以提升性能。
- **属性结构**：`text-wrap`是简写属性，实际控制`text-wrap-style`（算法选择）和`text-wrap-mode`（换行模式），开发者可独立设置。
- **浏览器支持**：
  - `pretty`已支持Safari、Chrome、Edge等，但各浏览器效果不同。
  - `text-wrap`长属性在2024年10月后成为主流。
- **使用建议**：
  - `pretty`用于正文优化排版，`balance`用于标题、摘要等短文本。
  - 测试不同值组合以适配设计需求，注意长文本性能及兼容性。
- **实用工具与反馈**：通过提供的在线Demo对比效果，开发者可在WebKit平台测试并提交问题反馈，作者通过社交媒体收集建议。
