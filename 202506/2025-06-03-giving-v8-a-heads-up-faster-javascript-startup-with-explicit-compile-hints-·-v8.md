# Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints · V8
- URL: https://v8.dev/blog/explicit-compile-hints
- Added At: 2025-06-03 14:38:44

## TL;DR


V8引擎新增显式编译提示功能，允许开发者通过`//# allFunctionsCalledOnLoad`注释提前编译JavaScript函数，减少网页加载时的延迟。测试显示此方法可平均缩短编译时间630毫秒，但需避免过度使用以防资源浪费。未来计划支持更精准的函数级编译控制。

## Summary


1. V8引擎引入显式编译提示功能，旨在通过允许开发者控制JavaScript代码的即时编译来优化网页加载性能。在页面启动阶段，延迟编译的函数会在调用时触发按需编译，导致额外延迟；而即时编译能在后台执行并利用网络加载并行，减少重复解析成本。  
2. 开发者可通过在JS文件头部添加`//# allFunctionsCalledOnLoad`注释，告知V8对整文件所有函数进行提前编译。实验表明，20个常见网页中17个的FG（前台）编译时间缩短平均630毫秒。  
3. 测试案例对比显示：未标注的script1.js需在调用时解析函数testfunc1，产生额外事件（如parse-function）；标注后的script2.js则在加载阶段完成编译，调用时无需二次解析。运行实验需关闭代码缓存，通过Chrome命令行参数查看编译日志。  
4. 功能需谨慎使用，过量编译可能导致内存和CPU资源浪费，影响整体性能。  
5. 未来计划支持按函数级别指定编译，精准控制关键函数的预编译流程，进一步提升加载效率。
