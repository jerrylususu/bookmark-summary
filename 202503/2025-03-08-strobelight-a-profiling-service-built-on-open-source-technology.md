# Strobelight: A profiling service built on open source technology
- URL: https://engineering.fb.com/2025/01/21/production-engineering/strobelight-a-profiling-service-built-on-open-source-technology/
- Added At: 2025-03-08 11:54:50
- [Link To Text](2025-03-08-strobelight-a-profiling-service-built-on-open-source-technology_raw.md)

## TL;DR
Strobelight是Meta研发的高性能分析系统，整合42种开源分析工具（如eBPF、jemalloc），通过低开销的数据采集和符号化技术，实时监控CPU/内存等指标，并支持火焰图等可视化分析。其动态采样与自动调优功能可减少20% CPU消耗，单次代码优化即节省年均1.5万台服务器容量，同时提供冲突规避机制及开源扩展能力，显著提升资源利用率与开发效率。

## Summary
Strobelight 是 Meta 开发的基于开源技术的分析协调服务，通过整合 42 种不同分析器（如内存、函数调用、事件、AI/GPU、延迟追踪等），帮助工程师优化代码性能并提升计算资源利用率。其核心依赖 eBPF 技术实现低开销的数据采集，并支持自定义扩展（如通过 bpftrace 脚本快速添加新分析器）。用户可通过命令行或 Web UI 按需获取数据，并通过配置文件设置持续或触发式分析策略。

主要功能和技术特点：
1. **多技术整合**：结合 eBPF、jemalloc、BOLT 等开源工具，支持对 CPU 使用、内存分配等多维度性能指标的实时监控。
2. **动态采样与自动调优**：通过每日动态调整采样概率，确保数据采集既足够精确又不影响服务性能，同时通过权重调整实现跨主机的服务数据聚合分析。
3. **符号化服务**：基于 DWARF、gsym、blazesym 等技术构建符号解析服务，高效转换地址为函数名及源代码信息，避免内存占用过高。
4. **多样化工具集成**：与 Scuba（数据查询/可视化）、Tracery（追踪数据时间线分析）协同，提供火焰图、分布图等多形式数据展示。Crochet 分析器可结合服务请求跨度、CPU 栈和非 CPU 时间数据，精准定位性能瓶颈。

关键价值：
- **效率提升**：LBR 分析器生成的优化数据使 Meta 200 个主要服务 CPU 周期减少最高 20%，相当于减少 10-20% 服务器需求。
- **成本节约**：通过代码审查工具预判性能问题（如优化 C++ 复制操作），单次代码修改（如添加“&”符号）实现年省 15000 台服务器容量。
- **数据增强机制**：Stack Schemas 过滤无关函数并添加标签，Strobemeta 关联动态元数据（如请求标识符），提升数据可分析性。

安全与扩展性：内置冲突避免机制（如确保 PMU 计数器不冲突）、队列系统防止性能降级，并通过配置控制允许服务所有者按需调整分析强度。当前已开源部分组件，支持社区贡献与技术迭代。
