# Gwtar: a static efficient single-file HTML format
- URL: https://gwern.net/gwtar
- Added At: 2026-02-16 02:43:49
- Tags: #tools #deepdive #web

## TL;DR
Gwtar 是一种新型单文件 HTML 归档格式，通过拼接 HTML 与 tarball 并利用 JavaScript 拦截资源请求，实现静态自包含与按需懒加载的平衡。它解决了大型网页归档的效率问题，但受限于浏览器安全策略和服务器对 Range 请求的支持。

## Summary
Gwtar 是一种新型的单文件 HTML 归档格式，旨在同时满足静态性（自包含）、单文件和高效性（按需懒加载）这三个通常难以兼得的属性。它通过将完整的 HTML 文件与一个附加的 tarball（包含原始 HTML 和所有资源）拼接，并利用 JavaScript 在浏览器端拦截资源请求，改写为 HTTP Range 请求来实现部分下载，从而避免了传统单文件归档（如 SingleFile）必须下载全部内容的效率问题。

该格式解决了 Gwern.net 在归档大型网页（如包含内嵌音频的讲座页面）时面临的困境：既需要长期可靠的静态存档，又希望用户能快速访问，同时保持文件管理的简便性。Gwtar 的实现依赖于浏览器支持的 `window.stop()` 方法来中断初始加载，以及 HTTP Range 请求来按需获取资源。它通过一个 PHP 脚本从 SingleFile 快照生成，并可选择添加 PAR2 前向纠错数据以增强文件完整性。

尽管 Gwtar 在服务器端无需特殊支持且具有前向兼容性，但它也存在局限性：本地文件查看可能因浏览器安全策略（CORS）而失效，且依赖于服务器正确支持 Range 请求（例如 Cloudflare 默认会剥离 HTML 响应的 Range 头，需通过自定义 MIME 类型 `x-gwtar` 绕过）。总体而言，Gwtar 为长期、高效的网页归档提供了一种创新的解决方案。
