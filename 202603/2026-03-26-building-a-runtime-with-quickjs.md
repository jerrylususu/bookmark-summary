# Building a Runtime with QuickJS
- URL: https://healeycodes.com/building-a-runtime-with-quickjs
- Added At: 2026-03-26 14:07:41
- Tags: #read #js #deepdive

## TL;DR
本文介绍如何基于QuickJS构建轻量级JavaScript运行时，逐步实现console.log、process.uptime()、定时器、事件循环及同步/异步文件I/O功能，并通过线程池处理异步任务。最终运行时在启动速度和文件读取方面优于Node.js，代码已开源。

## Summary
本文介绍了如何基于QuickJS构建一个轻量级JavaScript运行时，实现了console.log、process.uptime()、setTimeout/clearTimeout、fs.readFileSync和fs.readFile等功能，并包含事件循环和用于文件I/O的线程池。

首先，作者从零开始嵌入QuickJS引擎，创建JSRuntime和JSContext，并通过自定义可执行文件运行JavaScript代码。随后逐步添加功能：
1. **console.log**：通过将C函数绑定到全局对象的console.log方法实现。
2. **process.uptime()**：使用单调时钟跟踪进程启动时间，并通过JS_SetRuntimeOpaque存储运行时状态。
3. **setTimeout/clearTimeout**：使用排序链表管理定时器，通过JS_DupValue/JS_FreeValue管理回调引用。
4. **事件循环**：主机控制回调执行时机，通过select监控唤醒管道和定时器超时，确保微任务（如Promise）在下一个回调前执行。
5. **fs.readFileSync**：同步文件读取，返回字符串或抛出错误。
6. **fs.readFile**：使用线程池实现异步文件读取，通过条件变量和互斥锁管理任务队列，主事件循环处理完成的任务并触发Promise解析/拒绝。

最后，作者对比了该运行时与Node.js的性能，显示在启动时间和文件读取部分有较快表现。源代码可在GitHub获取。
