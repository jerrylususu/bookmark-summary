# Visual Effect - Interactive Effect Playground
- URL: https://effect.kitlangton.com/
- Added At: 2025-11-14 13:57:14
- Tags: #guide

## TL;DR
本文概述了 TypeScript 库 Effect 的主要功能模块，包括构造器、并发处理、错误管理、调度机制、引用和资源作用域，通过代码示例直观展示用法。

## Summary
本文介绍了 TypeScript 库 Effect 的交互式示例，展示了不同功能分类及相应代码用法。内容分为以下部分：

- **构造器**：包括创建成功、失败、异常、同步和异步效果的方法，如 `Effect.succeed`、`Effect.fail`、`Effect.sync` 和 `Effect.promise`。
- **并发处理**：涉及组合多个效果的方法，如 `Effect.all` 用于并行执行并返回所有结果，`Effect.race` 和 `Effect.raceAll` 用于竞速返回首个成功结果。
- **错误处理**：提供错误管理功能，如短路处理、备选效果、超时控制和重复尝试，例如 `Effect.orElse`、`Effect.timeout` 和 `Effect.eventually`。
- **调度**：包括重复执行和重试机制，支持固定间隔、条件控制和指数退避策略，如 `Effect.repeat` 和 `Effect.retry`。
- **引用（Ref）**：演示了线程安全的可变引用操作，如 `Ref.make` 创建引用和 `Ref.updateAndGet` 更新值。
- **作用域（Scope）**：展示了资源管理和清理功能，如 `Effect.addFinalizer` 注册清理动作和 `Effect.acquireRelease` 确保资源释放。

每个部分均通过简洁的代码示例说明用法，便于交互式学习和测试。
