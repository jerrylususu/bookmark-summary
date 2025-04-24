# Suffering-oriented programming - thoughts from the red planet - thoughts from the red planet
- URL: http://nathanmarz.com/blog/suffering-oriented-programming.html
- Added At: 2025-04-24 13:54:54
- [Link To Text](2025-04-24-suffering-oriented-programming---thoughts-from-the-red-planet---thoughts-from-the-red-planet_raw.md)

## TL;DR


痛苦导向编程主张通过分阶段迭代降低技术项目风险：先快速实现可行方案，暴露问题（如Storm用队列探索流处理局限）；接着基于真实痛点重构抽象设计（提炼核心概念，避免第二系统效应）；最后优化性能。其核心是通过实际需求而非预设目标驱动开发，逐步精简架构，消除冗余。

## Summary


痛苦导向编程强调在构建技术前先经历“痛苦”，确保需求真实存在且理解充分，从而降低项目风险。其核心分三阶段：  
1. **先让其可行**：在未知领域不预设通用方案，直接解决当下问题，通过快速“实践”积累经验，暴露系统局限。例如Storm早期通过队列和工作进程摸索流处理痛点，发现扩展性和容错性不足。  
2. **再让其优雅**：基于积累的真实用例（如“计算URL传播范围”需求），提炼简洁抽象（如Storm的流、Spout、Bolt等概念），避免过度设计。关键在于用实际场景而非预判驱动设计，防止“第二系统效应”。  
3. **最后让其高效**：待架构稳定后进行微优化，避免过早优化浪费资源。  
该方法通过持续迭代扩展能力，逐步深化问题理解（如Storm新增多流、事务拓扑等特性），并强调通过重构消除冗余，以真实使用案例而非预设需求指导开发，避免复杂性。其核心信仰是：设计必须由切实的痛点驱动，而非追求通用性。
