# @celine/celine
- URL: https://maxbo.me/celine/
- Added At: 2024-11-24 07:30:53
- [Link To Text](2024-11-24-@celine-celine_raw.md)

## TL;DR
@celine/celine 是一个用于构建 HTML 笔记本的库，支持 `display: block` 和 `contenteditable` 属性，旨在简化研究成果的 HTML 发布。它封装了 Observable Notebook 运行时，提供反应性单元格和丰富的 API 接口，支持多种字体和样式，并兼容多个第三方库。

## Summary
1. **库简介**：@celine/celine 是一个用于构建具有 `display: block` 和 `contenteditable` 属性的 HTML 笔记本的库。它封装了 [Observable Notebook](https://observablehq.com/documentation/notebooks/) 运行时的一部分，以实现单元格间的反应性，类似于 [Observable Framework](https://observablehq.com/framework/reactivity) 和 [Quarto](https://quarto.org/docs/interactive/ojs/)。其目标是使发布研究成果更容易，以 HTML 文件而非 PDF 文件的形式。

2. **名称由来**：最初考虑将此库命名为 _incel_，即 inline cell 的缩写，但后来被建议放弃这一名称。

3. **安装指南**：
   - **添加脚本**：在 HTML 文件的 `<head>` 块中添加以下 `<script>` 元素。
   - **链接样式表**：在 `<head>` 块中链接 [cell.css](https://maxbo.me/celine/#.echo) 和 [libertine.css](https://maxbo.me/celine/#libertine.css)。

4. **演示示例**：
   - **Observable Plot + SQLite**：尝试删除 `WHERE` 条件中的一个 `0`，然后点击 `<script>` 元素外以失去焦点并重新评估。

5. **API 接口**：
   - **`.echo` 类**：用于内联显示 `<script>` 和 `<style>` 元素，使用内置语法高亮的字体。
   - **`.reflect` 类**：强制 `<script>` 和 `<style>` 元素显示其开始和结束标签、`type`、`class`、`id` 和 `contenteditable` 属性。
   - **`celine.cell` 构造函数**：声明一个名为 `"${name}"` 的反应性单元格，`definition` 可以是 `T` 或 `(...inputs) => T`，其中 `T` 可以是 `object`、`Promise<?>`、`Iterator<?>` 或 `AsyncIterator<?>`。
   - **`celine.viewof` 构造函数**：专门用于与 [Observable Inputs](https://github.com/observablehq/inputs) 一起工作，声明两个反应性单元格：一个名为 `"${name}"`，另一个名为 `"viewof ${name}"`。
   - **`celine.silentCell` 构造函数**：声明一个不尝试在任何地方显示其当前值的单元格。
   - **`celine.mutable` 和 `celine.silentMutable` 构造函数**：声明一个单元格并返回一个可变引用，变异会传播到依赖它的单元格。
   - **`celine.library` 和 Observable 标准库**：包含许多有用的工具，如 TeX、Markdown、Graphviz、Mermaid 和 Leaflet。

6. **字体和样式**：
   - **@celine/libertine/libertine.css**：基于 [Linux Libertine](https://en.wikipedia.org/wiki/Linux_Libertine) 字体的样式表，提供了多种字体面、变体和 [OpenType 特性](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/OpenType_fonts_guide)。

7. **第三方库配对**：
   - **Pyodide**：将 CPython 移植到 WebAssembly。
   - **WebR**：使用 WebAssembly 编译的 R 语言版本。
   - **References Web Component**：用于在类似维基的方式中引用和引用来源的实验性 Web 组件。
   - **Penrose**：通过在纯文本中键入符号来创建美丽图表的系统。

8. **更新日志**：
   - **celine/changelog.xml**：使用 [Semantic Versioning 2.0.0](https://semver.org/) 记录更新。

9. **资源**：
   - **Observable Runtime**
   - **Observable Inputs**
   - **Observable standard library**
   - **How Observable Runs**
   - **Synchronized Inputs**
   - **Module require debugger**
   - **Observable Plot**
   - **Reactive HTML Notebooks**
