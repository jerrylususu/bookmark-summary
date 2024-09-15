# Notes on running Go in the browser with WebAssembly - Eli Bendersky's website
- URL: https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/
- Added At: 2024-09-15 03:39:12
- [Link To Text](2024-09-15-notes-on-running-go-in-the-browser-with-webassembly---eli-bendersky's-website_raw.md)

## TL;DR
本文总结了通过WebAssembly在浏览器中运行Go的模式，包括从JS调用Go、DOM操作、完整示例、使用TinyGo优化、Web Worker解决阻塞问题等，并提供了GitHub代码示例。

## Summary
1. **概述**：
   - 作者最近在几个小项目中使用WebAssembly将Go编译到浏览器中运行，并对WebAssembly进行了一些研究。
   - 本文总结了通过WebAssembly在浏览器中运行Go的一些有用模式，所有示例代码可在GitHub仓库中找到。

2. **基础：从JS调用Go**：
   - **示例代码**：编写一个Go函数，通过JS在浏览器中调用。
   - **功能**：使用Go的`math/big`包计算调和级数的和，并返回高精度结果。
   - **导出函数**：通过`js.Global().Set`将Go函数导出到JS。
   - **编译与加载**：使用`GOOS=js GOARCH=wasm go build`编译为WASM，并通过JS加载。
   - **UI交互**：JS代码监听按钮点击事件，调用Go函数并更新UI。

3. **DOM操作**：
   - **示例代码**：将更多逻辑移到Go中，包括DOM操作。
   - **功能**：Go代码获取DOM元素，添加事件监听器，获取和设置DOM元素的值。
   - **UI交互**：所有UI逻辑都在Go中实现，JS仅负责加载WASM模块。

4. **完整示例**：
   - **示例代码**：实现一个简单的Game of Life游戏，完全在Go中运行。
   - **功能**：游戏逻辑、画布操作和事件管理都在Go中完成。

5. **使用TinyGo**：
   - **概述**：TinyGo是Go的替代编译器，专注于嵌入式和小型环境。
   - **优势**：生成的WASM文件更小，加载更快。
   - **限制**：编译速度较慢，部分标准库不支持反射，可能需要替代JSON包。
   - **示例代码**：展示如何使用TinyGo编译项目。

6. **Web Worker**：
   - **概述**：解决长时间计算阻塞主线程的问题，使用Web Worker在单独线程中运行WASM。
   - **示例代码**：展示如何在Web Worker中加载WASM模块，使UI线程保持响应。
   - **UI交互**：添加旋转动画，直到Web Worker返回计算结果。

7. **附注**：
   - **调和级数**：调和级数发散但非常缓慢，需要超过2亿个元素才能达到和为20。
   - **WASM文件大小**：Go编译的WASM文件较大，加载时间较长，TinyGo可以减小文件大小。
