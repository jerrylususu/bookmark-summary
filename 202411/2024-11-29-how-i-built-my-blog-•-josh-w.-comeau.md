# How I Built My Blog • Josh W. Comeau
- URL: https://www.joshwcomeau.com/blog/how-i-built-my-blog-v2/
- Added At: 2024-11-29 15:13:53
- [Link To Text](2024-11-29-how-i-built-my-blog-•-josh-w.-comeau_raw.md)

## TL;DR
作者更新了博客，采用MDX、Next.js等技术，优化了内容管理、样式、代码片段和交互体验，新增了点赞、搜索等功能，提升了可访问性，并分享了开发经验。

## Summary
1. **博客更新**：
   - 作者在过去几个月中致力于全新版本的博客开发，并于几周前正式上线。
   - 新旧版本在设计上的变化不大，主要改进在于细节和内部技术架构。

2. **核心技术栈**：
   - 博客使用了多种前沿技术，包括MDX、Next.js、React Server Components等。
   - 选择这些技术的原因包括：MDX支持、减少上下文切换、体验最新React特性。
   - 作者考虑过使用Astro或Remix，但最终选择了Next.js。

3. **内容管理**：
   - 使用MDX编写博客文章，MDX结合了Markdown和JSX，允许在内容中嵌入自定义React组件。
   - 直接在VS Code中编辑MDX文件，并通过Git进行版本控制。
   - 使用next-mdx-remote处理MDX内容，未来可能尝试Next.js内置的MDX支持。

4. **样式与CSS**：
   - 旧版使用styled-components，新版切换到Linaria，以兼容React Server Components。
   - Linaria通过编译为CSS模块来避免运行时开销，但与Next.js集成存在一些问题。
   - 作者对Linaria的稳定性持保留态度，未来可能转向Pigment CSS。

5. **代码片段**：
   - 新版博客使用了自定义的语法主题，视觉效果显著提升。
   - 使用Shiki进行语法高亮，支持多种语言且不影响JavaScript包大小。
   - Shiki在性能和内存使用上存在一些问题，特别是在动态内容生成时。

6. **代码交互**：
   - 使用Sandpack创建React代码交互环境，使用自定义的Playground处理HTML/CSS代码。
   - 通过React Spring和Framer Motion实现动画效果，动态加载Framer Motion以优化性能。

7. **数据库与功能**：
   - 添加了点赞功能，数据存储在MongoDB中，通过Next.js的Route Handler处理请求。
   - 用户ID基于IP地址生成，确保匿名性。

8. **细节优化**：
   - 花费大量时间优化组件间的上下文样式，确保整体视觉效果的一致性。
   - 添加了彩虹动画和配置器，使用PartyKit实现实时同步。
   - 使用View Transitions API实现页面过渡动画，提升用户体验。

9. **搜索功能**：
   - 引入Algolia实现博客搜索，未来可能结合AI技术提升搜索体验。

10. **图标与交互**：
    - 重新设计了图标，添加了微交互效果，提升用户体验。
    - 使用React Spring和Framer Motion实现动画，动态加载以优化性能。

11. **可访问性**：
    - 新版博客全面采用rem单位进行媒体查询，提升可访问性。
    - 作者持续学习可访问性知识，并应用于博客开发中。

12. **技术选择对比**：
    - 从Pages Router切换到App Router，体验了新的Server Components范式。
    - 新系统在性能上未见显著提升，但提供了更强大的功能和更好的开发体验。
    - 存在一些性能问题，如CSS打包和静态组件的动态化处理。

13. **总结**：
    - 新版博客在技术栈、功能和用户体验上都有显著提升。
    - 作者分享了开发过程中的挑战和解决方案，为其他开发者提供了有价值的参考。
