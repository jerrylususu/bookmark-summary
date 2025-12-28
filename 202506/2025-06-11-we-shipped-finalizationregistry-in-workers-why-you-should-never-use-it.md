# We shipped FinalizationRegistry in Workers: why you should never use it
- URL: https://blog.cloudflare.com/we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it/
- Added At: 2025-06-11 15:24:48

## TL;DR


Cloudflare Workers新增对FinalizationRegistry API的支持以管理WebAssembly内存释放，但建议开发者改用显式资源管理方案（如Symbol.dispose与using语法）。因JavaScript自动垃圾回收与WebAssembly手动内存管理存在差异，FinalizationRegistry可能因非确定性定时引发内存泄漏。平台已限制I/O操作并优化回调执行，并倡导结合显式管理与兜底机制以提升内存处理可靠性。

## Summary


Cloudflare Workers新增支持FinalizationRegistry API以管理WebAssembly内存释放，但建议开发者避免直接使用。JavaScript采用自动垃圾回收处理内存，而WebAssembly需手动管理内存，二者需通过线性内存和绑定工具交互。FinalizationRegistry允许通过GC触发回调实现清理，但存在非确定性定时问题，可能导致内存泄漏或回调未执行。Cloudflare在Workers中实施该API时添加了安全机制，如限制最终回调中的I/O操作，确保回调在微任务队列清空后执行，并经安全评估排除跨隔离边界风险。推荐改用显式资源管理方案（如Symbol.dispose与using语法），其提供确定性清理，更适配WebAssembly与JavaScript协同场景。未来趋势将结合二者，用显式资源管理控制核心清理，以FinalizationRegistry作为安全兜底，共同优化内存管理。
