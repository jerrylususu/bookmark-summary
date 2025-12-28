# How a Kernel Bug Froze My Machine: Debugging an Async-profiler Deadlock | QuestDB
- URL: https://questdb.com/blog/async-profiler-kernel-bug/
- Added At: 2025-12-16 13:54:28
- Tags: #read #kernel #deepdive

## TL;DR
作者在使用 async-profiler 时遭遇一个由 Linux 内核 6.17 引入的 bug，导致系统死锁。该问题在于 cpu-clock 事件处理中的 hrtimer 回调陷入循环等待。解决方案是内核补丁将 hrtimer_cancel 改为非阻塞调用并引入延迟停止标志，临时规避方法是使用 -e ctimer 选项。作者通过 QEMU 和 GDB 成功调试并定位问题。

## Summary
本文详细记录了作者在使用 async-profiler 进行性能分析时遇到的一个 Linux 内核 bug，该 bug 导致机器完全死锁，以及作者如何通过调试和分析最终理解并解决了问题。

### 问题描述
- 作者在使用 async-profiler 对 QuestDB 进行 CPU 热图分析时，机器完全冻结，无法响应任何输入，只能强制重启。
- 初步怀疑是 QuestDB 集成代码的问题，但测试旧版本后问题依旧，最终确定问题出在系统环境上。
- 发现与 Ubuntu 25.10 和 Fedora 中使用的内核版本 6.17 相关，并通过社区报告确认了 bug 的存在。

### 根本原因
- bug 由内核提交 18dbcbfabfff 引入，该提交原本旨在修复另一个问题，但意外导致 cpu-clock 事件处理中出现死锁。
- 死锁发生流程：
  1. `perf_swevent_hrtimer` 在 hrtimer 中断上下文中被调用。
  2. 事件溢出处理函数 `__perf_event_overflow` 决定停止事件，调用 `cpu_clock_event_stop`。
  3. `cpu_clock_event_stop` 调用 `hrtimer_cancel` 取消定时器。
  4. `hrtimer_cancel` 等待当前回调完成，但此时正在执行该回调，导致 CPU 无限等待，系统冻结。

### 解决方案
- 内核补丁通过两个关键修改修复死锁：
  1. 将 `hrtimer_cancel` 替换为非阻塞的 `hrtimer_try_to_cancel`，避免在回调内等待。
  2. 引入 `PERF_HES_STOPPED` 标志作为延迟停止信号，确保定时器正确终止。
- 临时规避措施：使用 async-profiler 时添加 `-e ctimer` 选项，绕过有问题的 `perf_events` 路径。

### 调试过程
- 作者使用 QEMU 搭建虚拟机环境复现问题，并通过 GDB 连接内核进行调试。
- 步骤包括：安装 Ubuntu 25.10、配置内核符号、禁用 KASLR 以正确加载符号、捕获死锁时的堆栈跟踪。
- 通过 GDB 确认死锁发生在 `hrtimer_cancel` 循环中，并尝试手动修改寄存器值“修复”问题，但未成功。

### 总结
- 该 bug 凸显了内核代码的复杂性，以及异步事件处理中潜在的死锁风险。
- 对于用户，建议在使用 async-profiler 时添加 `-e ctimer` 选项，或等待内核更新或 QuestDB 集成修复版本。
- 作者通过此次调试深入理解了 Linux 性能监控机制，并掌握了内核调试的基本技能。
