# How many pillars of observability can you fit on the head of a pin?
- URL: https://charity.wtf/2025/10/30/the-pillar-is-a-lie/
- Added At: 2025-10-30 14:10:21
- [Link To Text](2025-10-30-how-many-pillars-of-observability-can-you-fit-on-the-head-of-a-pin_raw.md)

## TL;DR
作者批判“可观测性支柱”为营销术语，提倡用“信号”概念统一存储数据，避免多支柱模型导致的隔阂与高成本，强调OpenTelemetry等统一方案更高效。

## Summary
这篇文章批判了“可观测性支柱”的概念，认为这是一种营销术语而非技术术语。作者 Charity Majors 强调，可观测性实际上涉及的是不同类型的“信号”，如跟踪、指标、日志等，而“支柱”的说法容易导致工具商将数据隔离开来，增加成本和复杂度。

文章主要观点包括：
- “支柱”是营销术语，用于推销产品；而“信号”是技术术语，代表数据类型。
- 多支柱模型将不同信号存储在独立数据库中，导致数据重复、成本高昂，且难以关联分析。
- 统一存储模型将所有信号存储在一起，保留上下文，支持灵活查询，降低认知负担。
- OpenTelemetry 支持统一处理信号，但许多工具商仍选择多支柱模式。
- profiling 等工具在统一存储下可作为高分辨率数据集成，而非独立支柱。

作者呼吁行业摒弃“支柱”思维，采用更高效的数据处理方式。
