# Moving away from Tailwind, and learning to structure my CSS
- URL: https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/
- Added At: 2026-05-17 13:43:08
- Tags: #read #frontend

## TL;DR
作者从 Tailwind CSS 迁移至语义化 HTML 和原生 CSS，通过借鉴 Tailwind 的系统（如重置、颜色变量、字体比例）构建了自己的 CSS 结构，包括组件化、响应式设计和现代特性使用。迁移原因包括 Tailwind 的依赖性、项目体积及个人 CSS 技能提升，强调深入掌握 CSS 的复杂性和强大功能。

## Summary
作者回顾了自己从使用 Tailwind CSS 转向语义化 HTML 和原生 CSS 的过程，并分享了在此过程中学到的 CSS 结构化方法。文章首先指出，尽管 Tailwind 曾帮助作者快速构建小型项目，但随着对 CSS 理解的加深，作者决定迁移以更好地掌握 CSS 本身。

迁移过程中，作者从 Tailwind 中借鉴了一些系统，如重置样式、颜色调色板和字体比例，并在此基础上构建了自己的 CSS 结构。具体包括：

1. **重置**：复制了 Tailwind 的预设样式，如 `box-sizing: border-box`，以保持一致性。
2. **组件**：将 CSS 按组件组织，每个组件有独立的类和文件，避免样式冲突。
3. **颜色**：使用 CSS 变量定义颜色，确保所有颜色集中管理。
4. **字体大小**：定义字体大小变量，模仿 Tailwind 的比例系统。
5. **工具类**：保留少量通用工具类，如屏幕阅读器专用类。
6. **基础样式**：谨慎添加全局样式，如链接颜色和段落布局。
7. **间距**：采用更系统的方法管理间距，如使用相邻兄弟选择器。
8. **响应式设计**：更多使用 CSS Grid 和媒体查询，减少对 Tailwind 断点类的依赖。
9. **构建系统**：使用 esbuild 打包 CSS，利用现代 CSS 特性如嵌套选择器。

作者迁移 Tailwind 的原因包括：Tailwind 对构建系统的依赖增强、项目体积过大、个人 CSS 技能提升、以及 Tailwind 对 CSS 专业知识的潜在贬低。作者强调，通过深入学习 CSS，认识到其复杂性和强大功能，并希望更尊重和掌握这门技术。

此外，作者提到对 CSS 新特性（如 `@layer`、`@scope`、容器查询和子网格）的兴趣，并感谢 CSS 社区分享的实践和灵感。
