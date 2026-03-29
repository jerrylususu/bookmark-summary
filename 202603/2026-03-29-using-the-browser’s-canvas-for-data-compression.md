# Using the Browser’s <canvas> for Data Compression
- URL: https://jstrieb.github.io/posts/canvas-compress/
- Added At: 2026-03-29 13:17:22
- Tags: #read #frontend #hack

## TL;DR
本文介绍利用 `<canvas>` 元素将数据编码为像素并导出为 PNG 图像，以实现前端数据压缩的方法。该方案适用于旧版浏览器，通过 PNG 格式压缩特性减小体积，支持压缩与解压操作，并提供完整代码示例。

## Summary
本文介绍了如何利用浏览器 `<canvas>` 元素实现数据压缩，适用于静态网站或单页应用（SPA）中需要前端压缩功能的场景。由于浏览器内置了优化的压缩库（如用于 HTTP 请求和图像处理），但旧版本浏览器可能未开放直接的压缩 API，作者提出了一种间接方法：将数据编码为像素数据，通过 Canvas 生成 PNG 图像，利用 PNG 格式的压缩特性减小数据体积。

核心方法包括：
- **压缩**：将 `Uint8Array` 数据转换为像素，存入 Canvas 并导出为 base64 编码的 PNG 图像。
- **解压**：异步加载 PNG 图像，提取像素数据并还原为原始 `Uint8Array`。

文章提供了完整的 JavaScript 代码示例，并附有演示和测试文件。作者指出，尽管现代浏览器已支持 Compression Streams API，但此方法在旧浏览器中仍有效，且能利用浏览器内置的压缩效率。此外，文章强调了该方法在 URL 哈希存储等场景中的实用性，并感谢了相关贡献者。
