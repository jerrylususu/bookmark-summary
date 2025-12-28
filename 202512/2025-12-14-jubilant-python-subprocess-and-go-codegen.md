# Jubilant: Python subprocess and Go codegen
- URL: https://benhoyt.com/writings/jubilant/
- Added At: 2025-12-14 13:33:36
- Tags: #read

## TL;DR
Jubilant 是利用 Python 封装 Juju CLI 的项目，通过 subprocess.run 调用 CLI 简化架构，使用代码生成确保数据模型一致，并基于 uv 和 Make 管理开发流程，体现了简洁实用的设计思路。

## Summary
## Jubilant 项目总结

Jubilant 是 Canonical 开发的 Python API，用于操作 Juju（一个部署和管理工具）。文章重点介绍了其设计中的三个关键技术选型。

### 1. 使用 subprocess.run 调用 CLI
- **方法**：通过 `subprocess.run` 直接调用 `juju` 命令行工具，而非使用复杂的旧版 Python API（python-libjuju）。
- **优势**：
  - 简化架构，避免旧版 API 的 RPC、WebSocket 和异步复杂性。
  - Juju CLI 本身是异步操作，无需在 Python 中处理异步逻辑。
  - 进程创建开销小（尤其在 Linux 上），对耗时命令（如部署）影响可忽略。
  - Juju CLI 的 JSON 输出格式稳定，保障了兼容性。
- **局限**：不支持事件订阅等高级功能，但满足集成测试等主要需求。
- **测试**：通过自定义 Mock 替换 `subprocess.run`，简化单元测试（如使用 Pytest 验证命令输出解析）。

### 2. 代码生成：从 Go 结构体生成 Python 数据类
- **背景**：Jubilant 需将 Juju CLI 的 JSON 输出（如 `juju status --format json`）转换为类型化的 Python 对象。
- **挑战**：手动编写 28 个嵌套数据类容易出错，且需与 Juju 源码中的 Go 结构体（如 `formattedStatus`）保持一致。
- **解决方案**：用 Go 编写一次性代码生成器，通过反射解析 Go 结构体，自动生成 Python 数据类及 `_from_dict` 反序列化方法。
- **意义**：确保类型定义精确匹配源数据，避免手动转录错误，体现了"编写临时工具简化跨语言转换"的实用主义。

### 3. 开发工具链：Make 和 uv
- **依赖管理**：使用 `uv` 管理 Python 依赖（仅需 PyYAML）和开发环境（集成 Pyright、Pytest、Ruff 等）。
- **任务自动化**：通过 Makefile 统一常用命令（如格式检查、测试、文档构建），并通过 `make help` 提供友好提示。
- **开发流程**：编码后运行 `make all` 一键完成代码格式化、静态检查和测试，提升效率。

### 设计特点
- **API 设计**：CLI 命令与 Python 方法一一对应，位置参数和关键字参数映射自然，利用类型注解和 `@overload` 支持多态调用。
- **兼容性**：保留 Juju 用户熟悉的 CLI 交互模式，同时提供 Pythonic 的类型安全体验。

### 总结建议
对于复杂工具集成，可优先考虑：
- 用 `subprocess.run` 包装稳定 CLI。
- 通过代码生成减少跨语言数据转换错误。
- 结合 `uv` 和 `Make` 优化开发流程。
项目强调简洁性与实用性，旨在降低维护成本。
