# State of Terminal Emulators in 2025: The Errant Champions · Articles
- URL: https://www.jeffquast.com/post/state-of-terminal-emulation-2025/
- Added At: 2025-11-04 15:12:25
- Tags: #read #guide

## TL;DR
2023年测试的后续更新：使用改进的ucs-detect工具评估终端Unicode支持。Ghostty和Kitty表现最佳，但终端处理零宽度字符等问题仍存挑战。文本尺寸协议有望改善复杂脚本显示，推动超越等宽限制。测试发现性能和兼容性存在差异。

## Summary
本文是对2023年《终端模拟器大乱斗——Unicode版！》文章的后续，使用更新的ucs-detect工具测试终端模拟器的Unicode支持，覆盖DEC私有模式、Sixel图形、像素尺寸和软件版本检测。主要内容可结构化如下：

### 测试方法与工具更新
- **ucs-detect工具增强**：在原有Unicode支持测试基础上，新增对DEC私有模式、Sixel图形、像素尺寸和软件版本的自动检测。
- **测试原理**：通过发送控制序列请求光标位置，与Python wcwidth库结果对比，记录差异。

### Unicode支持的核心挑战
- **宽度问题**：终端需将Unicode字符映射到固定宽度网格，但零宽度连接符、变体选择器和字素簇等导致预测失败，引发光标错位和输出损坏。
- **测试目标**：评估终端对Unicode的支持程度，减少此类问题。

### 领先终端表现
- **Ghostty**：2025年新发布，基于Zig语言开发，Unicode支持最全面，得分最高。其作者Mitchell Hashimoto还发布了libghostty库，可能替代libvte。
- **Kitty**：得分与Ghostty相当，作者Kovid Goyal发布的文本分割算法与wcwidth规范一致，支持变体选择器15等高级功能。两者是唯一正确支持该功能的终端。

### 测试结果概览
- **性能问题**：iTerm2和Extraterm测试缓慢，消耗大量CPU；GNOME Terminal等基于VTE的终端耗时超5小时，但CPU占用低。事件循环效率低是普遍问题。
- **wcwidth优化**：通过位向量、布隆过滤器和LRU缓存优化后，确认二进制搜索加LRU缓存方案最佳，能高效处理重复Unicode子集。

### 终端特定问题
- **Terminology**：测试结果不一致，可能存在状态损坏。
- **iTerm2**：报告所有DEC私有模式“支持但不可更改”，包括虚构模式。
- **Konsole**：不回复DEC模式查询，但实际支持部分模式。
- **Contour**：因响应模式号错误和转义键配置问题，显示无DEC模式支持，需手动修复。
- **libvte终端**：性能得分低，但新议题显示2026年可能改进Emoji支持。

### 模式2027的局限性
- **用途有限**：DEC模式2027可检测终端Unicode支持，但仅提供二进制指示，无法区分具体功能。实际需像ucs-detect那样交互测试特定功能。

### 超越固定宽度的未来
- **文本尺寸协议**：Kitty提出的协议支持可变尺寸文本，可能提升复杂脚本（如Khün语）的可读性，打破等宽限制。
- **示例比较**：Contour与wcwidth在Khün文本测量上存在分歧，但可变尺寸模式有望改善显示效果。

总结：终端Unicode支持在2025年有显著进步，Ghostty和Kitty领先，但性能和技术挑战仍存。可变文本尺寸可能是解决复杂脚本显示问题的方向。
