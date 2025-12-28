# Backtraces with strace
- URL: https://shane.ai/posts/backtraces-with-strace/
- Added At: 2025-06-17 14:27:28

## TL;DR


strace是用于调试进程行为的系统调用追踪工具，其新增的--stack-traces选项可通过栈路径分析复杂问题，如Go与Cgo交互排查。纯Go DNS解析器使用非阻塞套接字，性能更优但兼容性不足；Cgo方式依赖libc，易引发线程激增问题。作者建议按场景选择模式，并计划整合strace数据至Mozilla工具优化分析。

## Summary


strace 是基于 ptrace 的系统调用追踪工具，自 2005 年起被广泛用于调试和分析进程行为。尽管其性能开销较大，不适合生产环境，但在开发阶段可有效展示进程操作的时间线。文中作者介绍了 strace 新增的 `--stack-traces` 选项，该功能于 2014 年加入，使用户能直观看到引发系统调用的代码路径，极大提升了对复杂信号处理（如 Go 与 Cgo 交互）的排查效率。

作者通过 Go 程序演示 DNS 解析的差异分析：
1. **纯 Go DNS 解析器**：  
   使用 `SOCK_DGRAM` 非阻塞套接字连接本地 DNS 服务（如 127.0.0.53），退出主线程独立执行，采用 Happy Eyeballs 算法并行查询 IPv4 和 IPv6 地址。堆栈跟踪显示 Go 自主控制 I/O 流程，避免 libc 的兼容性问题。

2. **Cgo DNS 解析器**：  
   依赖 libc 的 getaddrinfo 函数，尝试连接 AF_UNIX 套接字（如 systemd 的 nscd 服务）未果后，转用 AF_INET 阻塞模式套接字。导致系统额外创建大量线程（可能远超默认 GOMAXPROCS 值），可能引发资源耗尽问题，增加运维复杂度。

关键发现：  
- 纯 Go 解析器性能更优但兼容性不足，Cgo 方式可能导致线程激增和阻塞问题。  
- `--stack-traces` 可快速定位代码路径，例如揭示 Go 的并行机制或外部库（libc）的介入。  

作者建议根据需求选择解析器模式，同时提到未来可能将 strace 数据整合到 Mozilla 的跟踪工具中以优化分析流程。
