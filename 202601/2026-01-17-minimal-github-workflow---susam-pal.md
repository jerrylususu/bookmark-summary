# Minimal GitHub Workflow - Susam Pal
- URL: https://susam.net/minimal-github-workflow.html
- Added At: 2026-01-17 06:49:24
- Tags: #read

## TL;DR
本文通过逐步实验，从空文件开始构建GitHub工作流，最终成功运行"hello, world"示例。关键发现是：最小配置需包含on事件触发器、jobs定义、job ID、runs-on环境、steps步骤和run命令。

## Summary
本文探讨了构建最小化 GitHub 工作流文件时可能遇到的错误，通过逐步实验从一个空文件开始，直到创建一个能成功运行的“Hello, World”示例。以下是关键步骤和对应的错误或成功信息，按配置顺序组织。

- **空工作流**：创建零字节文件 `hello.yml`，推送后产生错误：未定义事件触发器（`on`）。
- **仅添加 `on:`**：工作流文件内容为 `on:`，错误：缺少 `on` 的值和必需属性 `jobs`。
- **添加 `on: push`**：工作流增加 `on: push`，错误：仍缺少 `jobs` 属性。
- **添加 `jobs:`**：工作流包含 `on: push` 和 `jobs:`，错误：`jobs` 值无效（缺少 job ID）。
- **添加 job ID**：工作流定义 `jobs: world:`，错误：`world` 值无效（缺少 `runs-on` 和 `steps`）。
- **添加 `steps:`**：工作流包含 `jobs: world:` 和 `steps:`，错误：缺少 `runs-on` 属性。
- **添加空 `runs-on:`**：工作流定义 `runs-on:` 和 `steps:`，错误：`runs-on` 值无效。
- **添加 `runs-on: ubuntu-latest`**：工作流固定运行环境，错误：`steps` 值无效（缺少步骤定义）。
- **使用空步骤数组 `steps: []`**：工作流定义空步骤，错误：未定义任何步骤。
- **添加 `run:`**：工作流在步骤中添加 `run:`（空值），成功运行，无具体输出。
- **添加 `run: echo`**：工作流定义 `run: echo`，成功运行，输出空白行。
- **完整示例 `run: echo hello, world`**：工作流添加具体命令，成功运行，输出 "hello, world"。

最终，最小可行的 GitHub 工作流需包含：`on` 事件触发器、`jobs` 定义、job ID、`runs-on` 运行环境、`steps` 步骤，以及至少一个 `run` 命令。所有实验代码保存在 GitHub 仓库中。
