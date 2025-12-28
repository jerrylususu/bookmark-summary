# LocalStorage vs. IndexedDB vs. Cookies vs. OPFS vs. WASM-SQLite | RxDB - JavaScript Database
- URL: https://rxdb.info/articles/localstorage-indexeddb-cookies-opfs-sqlite-wasm.html
- Added At: 2024-11-29 14:27:44

## TL;DR
文章讨论了Web应用中数据存储的需求和技术演进，从早期的Cookies到现代的IndexedDB和OPFS，分析了各技术的功能、性能和限制，并展望了未来的改进方向。

## Summary
1. **存储数据需求**：
   - 构建Web应用程序时，需要在用户浏览器中存储数据。
   - 可能需要存储小标志或完全成熟的数据库。

2. **Web应用类型变化**：
   - 早期提供静态HTML文件。
   - 动态渲染HTML。
   - 单页应用程序（SPA），大部分逻辑在客户端运行。
   - 未来可能构建本地优先应用，处理复杂数据操作，支持离线使用，实现零延迟用户交互。

3. **早期存储选项**：
   - 早期只有Cookies用于存储小键值对。
   - JavaScript和浏览器发展，引入更好的存储API，支持更大和更复杂的数据操作。

4. **存储技术概览**：
   - **Cookies**：1994年由Netscape引入，主要用于会话管理、个性化和跟踪。
   - **LocalStorage**：2009年作为WebStorage规范的一部分引入，提供简单的键值对存储API。
   - **IndexedDB**：2015年引入，低级API，用于存储大量结构化JSON数据。
   - **OPFS**：相对较新的API，允许Web应用直接在浏览器中存储大文件。
   - **WASM SQLite**：通过WebAssembly在浏览器中运行SQLite。
   - **WebSQL**：2009年引入，基于SQLite的客户端存储API，已从浏览器中移除。

5. **功能对比**：
   - **复杂JSON文档存储**：
     - 只有IndexedDB和WASM SQLite原生支持JSON对象存储。
   - **多标签支持**：
     - LocalStorage通过storage事件自动共享写事件。
     - 其他解决方案如BroadcastChannel API和SharedWorker。
   - **索引支持**：
     - 只有IndexedDB和WASM SQLite支持索引。
   - **WebWorker支持**：
     - LocalStorage和Cookies无法在WebWorker中使用。
     - OPFS的快速版本只能在WebWorker中使用。

6. **存储大小限制**：
   - **Cookies**：约4KB。
   - **LocalStorage**：4MB到10MB。
   - **IndexedDB和OPFS**：取决于可用磁盘空间。

7. **性能对比**：
   - **初始化时间**：
     - IndexedDB和OPFS需要较长时间初始化。
     - WASM SQLite初始化时间最长。
   - **小写入延迟**：
     - LocalStorage延迟最低。
     - IndexedDB和WASM SQLite较慢。
   - **小读取延迟**：
     - LocalStorage读取速度最快。
   - **大块写入和读取**：
     - OPFS在WebWorker中表现更好。
     - WASM SQLite在批量操作中表现良好。

8. **性能结论**：
   - LocalStorage速度快，但不适合大块操作和索引查询。
   - OPFS在WebWorker中表现显著优于主线程。
   - WASM SQLite初始化时间长，但长期使用可能不构成问题。

9. **可能的改进**：
   - IndexedDB性能优化。
   - OPFS单文件存储优化。
   - 混合技术优化不同场景。
   - 内存映射存储插件。
   - 数据压缩。
   - 多WebWorker分片。

10. **未来改进**：
    - 直接从WebAssembly访问持久存储。
    - 改进主线程和WebWorker之间的数据传输。
    - IndexedDB存储桶支持。

11. **后续行动**：
    - 分享公告推文。
    - 在GitHub仓库中复现基准测试。
    - 学习RxDB快速入门。
    - 查看RxDB GitHub仓库并留下星标。
