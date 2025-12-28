# My gift to the rustdoc team
- URL: https://fasterthanli.me/articles/my-gift-to-the-rust-docs-team#solutions
- Added At: 2025-12-14 13:29:17
- Tags: #read #deepdive

## TL;DR
Arborium 是为 Rust 文档网站 docs.rs 开发的语法高亮工具，支持 96 种语言，通过 tree-sitter 实现高性能解析。文章分析了三种集成方案，推荐在 docs.rs 构建时进行后端处理以兼顾性能和安全。该项目已在 GitHub 开源，旨在提升 Rust 文档的可读性。

## Summary
这篇文章介绍了作者为 Rust 文档团队开发的工具 Arborium，旨在为 Rust 文档网站 docs.rs 中的代码块提供语法高亮功能。文章结构如下：

1. **背景与问题**：
   - Rust 的 rustdoc 工具可为 crate 生成 HTML 和 JSON 文档，但 docs.rs 上的代码块默认无语法高亮（白底黑字），影响可读性。
   - docs.rs 的文档构建后不可变，重新构建所有历史版本不现实，且语法高亮面临多种技术挑战，如工具选择、语言支持、性能和安全问题。

2. **解决方案：Arborium**：
   - 作者基于 tree-sitter（一个高效的语法解析库）开发了 Arborium，支持 96 种语言的语法高亮。
   - Arborium 提供简单的 API，可输出 HTML 或终端友好的高亮代码，并内置多种主题。
   - 它通过 Cargo 特性标志集成语言语法，自动处理依赖（如 Svelte 需要 HTML、CSS 和 JavaScript 支持）。
   - 支持 WebAssembly 编译，可在浏览器中运行。

3. **三种实现角度**：
   - **角度1：前端脚本注入**：用户可通过添加脚本在 docs.rs 页面上启用高亮，但存在安全风险（第三方 JavaScript 可能被恶意利用）和性能问题（需下载大体积语法包）。
   - **角度2：集成到 rustdoc**：作者提交了 PR，将 Arborium 直接嵌入 rustdoc 工具，但会导致 rustdoc 二进制文件显著增大（从 22MB 增至 171MB），可能影响采纳。
   - **角度3：后端处理**：推荐方案，使用 arborium-rustdoc 作为 docs.rs 的后置处理器，在构建时高亮代码，仅增加少量存储开销（测试中 900MB 文档仅增 24KB），且无安全顾虑。

4. **开发挑战**：
   - CI/CD 设置复杂，需协调大量构建任务，作者感谢 Depot.dev 提供高效 CI 资源。
   - 使用 cargo-xtask 管理构建逻辑，确保 WebAssembly 包兼容性。

5. **结论**：
   - Arborium 开源（Apache2+MIT 许可），旨在长期改善网络上的语法高亮。
   - 对于 docs.rs，作者推荐角度3的后端处理方案，因其安全、高效且可扩展。
   - 文章以节日祝福结尾，并附带作者其他内容推广。

整体上，文章详细阐述了语法高亮问题的痛点、Arborium 的设计优势，以及多种落地方案的利弊，突出了对 Rust 生态的贡献。
