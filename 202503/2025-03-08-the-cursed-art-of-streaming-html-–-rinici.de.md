# The Cursed Art of Streaming HTML – rinici.de
- URL: https://rinici.de/posts/streaming-html
- Added At: 2025-03-08 10:50:18

## TL;DR
文章介绍一种无需JavaScript或WebSockets的流式传输HTML技术，通过浏览器保持连接特性逐段推送内容实现实时更新。其核心技术包括框架流式接口（如Node.js的res.write）、iframe隔离聊天内容追加新消息，解决响应流未关闭及表单刷新问题。兼容旧版浏览器，支持分块加载但需注意XSS防护，附代码示例。

## Summary
文章介绍了通过流式传输HTML实现实时网页更新的技术，无需依赖JavaScript或WebSockets。核心观点如下：

1. **流式HTML原理**  
   浏览器默认使用`Connection: keep-alive`，允许服务器逐步推送HTML内容，实现类似SSE的实时更新。此方法兼容性极强，甚至支持旧版浏览器。

2. **技术实现**  
   - 通过框架提供的流式接口（如Node.js的`res.write()`、Actix的`HttpResponse::streaming()`）逐步输出HTML片段。  
   - 示例使用Express框架构建实时聊天应用：  
     * 使用iframe隔离聊天历史和输入表单，避免页面刷新。  
     * 服务器监听消息事件，通过`res.write()`向客户端追加新消息。  
     * 添加资源清理机制，防止内存泄漏。

3. **关键问题与解决方案**  
   - **未关闭响应流**：浏览器因未收到响应结束标记持续显示加载状态。  
     部分解决方案：使用`loading="lazy"`延迟加载iframe（不兼容无JS环境），或通过JavaScript延迟加载iframe内容。  
   - **表单提交刷新问题**：通过iframe嵌套和重定向（`/chat#text`）保持页面状态，并自动聚焦输入框。

4. **可扩展性与局限性**  
   - 支持分块加载、优先渲染核心内容（如eBay的Async Fragments技术）。  
   - 安全警告：未提及XSS防护，需自行处理用户输入。  
   - 部分功能需微量JS辅助（如延迟加载iframe），但核心功能保持无JS兼容性。

文章附代码实现及 GitHub 源码链接，演示了该技术在个人网站的实践。
