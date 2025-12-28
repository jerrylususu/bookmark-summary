# Gist of Go: Concurrency internals
- URL: https://antonz.org/go-concurrency/internals/
- Added At: 2025-12-07 13:18:49
- Tags: #read #go #deepdive

## TL;DR
文章《Go并发内部机制》核心解析了Go语言并发实现，包括goroutine调度器、GOMAXPROCS配置、并发原语及性能工具。调度器通过少量OS线程高效运行大量goroutine，自动管理并发细节。建议借助pprof、tracing等工具优化应用，鼓励实践掌握并发编程。

## Summary
文章《Go并发内部机制》详细解析了Go语言并发实现的核心原理，重点围绕goroutine调度器、并发原语、性能分析工具等展开。主要内容总结如下：

### 一、并发基础
- **硬件层面**：CPU核心并行执行指令。
- **操作系统层面**：线程是基本执行单元，操作系统调度器管理线程在有限核心上的切换。
- **Go运行时层面**：goroutine是轻量级执行单元，Go调度器将大量goroutine映射到少量OS线程上（通常每个核心一个线程），通过队列和切换实现并发。

### 二、Goroutine调度器
- **作用**：管理M个goroutine在N个OS线程上运行（M >> N）。
- **简化模型**：
  - 使用队列管理goroutine。
  - 采用抢占式调度，每约10毫秒检查并切换goroutine，防止饥饿。
  - 处理系统调用时，若线程阻塞，会创建新线程运行其他goroutine，完成后回收多余线程。
- **参考资源**：推荐观看Dmitry Vyukov的演讲以深入了解。

### 三、GOMAXPROCS
- **定义**：控制Go调度器可用的最大OS线程数（不含系统调用线程），默认值为`runtime.NumCPU()`。
- **设置方式**：通过环境变量或`runtime.GOMAXPROCS()`函数调整，Go 1.25+支持`runtime.SetDefaultGOMAXPROCS()`恢复默认。
- **容器环境适配**：
  - Go 1.25+开始尊重cgroup的CPU配额（如Docker的`--cpus`限制），自动调整`GOMAXPROCS`为逻辑CPU数与配额下限。
  - 支持小数配额向上取整，多CPU环境下最小值默认为2。

### 四、并发原语内部实现
- **Goroutine**：由`runtime.g`结构表示，栈默认2KB，内存效率高，切换快速。
- **Channel**：由`runtime.hchan`结构实现，包含缓冲区、等待队列和锁机制。
- **Select**：通过`runtime.selectgo`处理多路复用，随机选择就绪case以避免饥饿。

### 五、调度器指标与性能分析
- **指标监控**：使用`runtime/metrics`包获取指标（如goroutine数量、线程数），可集成Prometheus等工具。
- **性能分析（Profiling）**：
  - Go分析器适用于生产环境，支持CPU、堆内存、goroutine、阻塞、互斥锁等分析。
  - 通过`net/http/pprof`包提供HTTP接口，使用`go tool pprof`可视化结果（如火焰图、源代码视图）。
- **追踪（Tracing）**：
  - 记录goroutine生命周期、系统调用等事件，通过`go tool trace`工具查看。
  - Go 1.25+引入飞行记录器（FlightRecorder），支持滑动窗口追踪，便于捕获未知事件。

### 六、总结与推荐
- Go调度器自动处理并发细节，开发者通常只需关注goroutine和channel等高级抽象。
- 文章摘自作者书籍《Gist of Go: Concurrency》，推荐阅读完整版以通过实践深化理解。

文章强调实践的重要性，鼓励读者结合工具和示例掌握并发编程。
