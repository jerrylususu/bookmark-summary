# Absurd Workflows: Durable Execution With Just Postgres
- URL: https://lucumr.pocoo.org/2025/11/3/absurd-workflows/
- Added At: 2025-11-03 14:22:30
- Tags: #read #distributed #hack
- [Link To Text](2025-11-03-absurd-workflows-durable-execution-with-just-postgres_raw.md)

## TL;DR
Absurd是一个轻量级持久化执行库，仅依赖Postgres实现可靠的工作流和AI代理。它将任务分解为步骤，利用Postgres的队列和状态存储功能，在故障时支持任务重试和状态恢复，无需第三方服务，简化部署和运维。

## Summary
本文介绍了一个名为Absurd的轻量级、仅依赖Postgres的持久化执行（durable execution）库，用于简化构建可靠的工作流和AI代理系统。

## 背景与动机
- **持久化执行的挑战**：随着AI代理的普及，构建可靠的代理系统需要解决历史性难题，如确保任务在崩溃、重启或网络故障后不丢失状态或不重复执行。现有解决方案通常复杂且依赖第三方服务。
- **Absurd的目标**：作者旨在探索如何仅用Postgres实现持久化执行，避免引入额外复杂性。因此开发了Absurd，一个基于SQL的微型库，无需Postgres扩展即可支持持久化工作流。

## 持久化执行核心概念
- **定义**：持久化执行是将长时运行的任务分解为小步骤（step functions），每个步骤的状态被记录在数据库中。当执行中断时，系统可从最近检查点恢复，确保连续性。
- **Postgres的优势**：利用Postgres的`SELECT ... FOR UPDATE SKIP LOCKED`特性实现队列功能（如pgmq），同时作为状态存储数据库，兼具队列和状态管理能力。

## Absurd系统设计
- **核心组件**：仅包含一个SQL文件（`absurd.sql`），应用于数据库；SDK则提供语言友好的抽象接口。
- **工作流程**：
  - **任务（Task）**：被分发到队列中。
  - **工作器（Worker）**：从队列获取任务，按顺序执行步骤（Steps）。
  - **检查点（Checkpoint）**：每个步骤的结果存储在Postgres中，用于恢复状态。
  - **运行（Run）**：任务失败或暂停后可重试，但步骤不会重复执行（仅任务级重试）。
- **关键特性**：
  - **事件与睡眠**：支持任务暂停（如`ctx.sleep()`等待指定时间）或等待外部事件（如`ctx.waitForEvent()`），事件缓存确保无竞争条件。
  - **AI代理集成**：代理工作流本质是单步迭代过程（如循环处理消息），Absurd通过自动递增步骤名（如`iteration#2`）支持状态持久化，仅存储增量变化而非完整历史。

## 应用示例
- **代理任务定义**：以天气查询代理为例，任务通过`absurd.spawn()`启动，步骤函数（如`singleStep`）调用AI模型并处理工具调用（如获取天气）。若步骤失败，任务会重试，且之前步骤的状态自动从检查点加载。
- **简化部署**：无需复杂运行时或编译器插件，仅依赖Postgres，适合自托管场景，降低系统复杂度。

## 总结
Absurd通过将持久化执行简化为“队列+状态存储”模式，证明复杂问题可用轻量方案解决。相比Temporal等工具，它更注重简洁性和可自托管性，适用于不需要大规模复杂性的场景。作者强调，持久化工作流本质简单，Absurd旨在回归这一本质。
