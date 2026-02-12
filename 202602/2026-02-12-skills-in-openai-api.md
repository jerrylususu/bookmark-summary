# Skills in OpenAI API
- URL: https://developers.openai.com/cookbook/examples/skills_in_api/
- Added At: 2026-02-12 13:53:32
- Tags: #read #agent

## TL;DR
技能是包含指令和脚本的可重用文件包，通过SKILL.md定义，适用于重复性工作流。它与系统提示和工具不同，用于打包稳定流程。创建时需上传文件夹或zip包，通过API调用并挂载到执行环境，例如生成CSV洞察报告。

## Summary
**技能定义与作用**
技能是可重用的文件包（包含指令、脚本和资源），由 `SKILL.md` 清单文件定义。它被上传到执行环境，供模型在需要时读取指令并执行代码。技能适用于重复性工作流，尤其适合需要版本控制、代码执行和共享标准的场景。

**适用场景**
- 需要可重用、独立版本化的行为（如报告生成、数据清洗）。
- 工作流高度条件化或分支复杂。
- 需要代码执行和本地资源（脚本、模板、测试数据）。
- 希望保持系统提示简洁，将稳定流程放入技能。
- 多代理或团队共享相同标准。
- 需要可复现性（通过版本控制）。

**不适用场景**
- 一次性任务（可直接在对话中编写脚本）。
- 主要依赖实时外部数据或副作用（应使用工具/API 调用）。
- 流程每日变化（技能适合稳定的工作流）。

**技能 vs. 工具 vs. 系统提示**
- **系统提示**：用于全局行为和约束（如安全边界、语气），避免放入长流程。
- **工具**：用于与外部服务交互或产生副作用（如调用 API、发送邮件），应窄范围、强类型输入。
- **技能**：用于打包可重复的工作流，包含代码和资源，可按需调用。

**技能打包：SKILL.md 与文件夹结构**
- **文件夹结构**：包含 `SKILL.md`（必需）、脚本（如 `.py`、`.js`）、辅助文件（如 `requirements.txt`）和资源（模板、示例输入）。
- **SKILL.md 前言**：必须包含 `name` 和 `description`，用于模型发现和路由。每个技能包对应一个 `SKILL.md`，多个技能需分别上传。

**通过 API 创建技能**
使用 `POST /v1/skills` 上传技能包（支持目录或 zip 上传）。推荐 zip 上传以避免服务器错误。上传后返回技能 ID 和版本指针（如 `default`、`latest`）。

**将技能挂载到执行环境**
通过响应 API 的 shell 工具使用技能，指定 `tools[].environment.skills`。支持托管 shell（`environment.type="container_auto"`）和本地 shell（`environment.type="local"`）。引用方式：
- `skill_reference`（通过 `skill_id`，可指定版本或 `"latest"`）。
- `inline`（base64 编码的 zip 包，无需创建托管技能）。

**示例：CSV 洞察技能**
1. **创建文件夹**：包含 `SKILL.md`、`requirements.txt`、`run.py` 和 `assets/example.csv`。
2. **编写 `SKILL.md`**：定义名称、描述、使用场景、输入输出和运行步骤。
3. **编写 `run.py`**：使用 pandas 和 matplotlib 生成 CSV 摘要、统计和可视化。
4. **打包并上传**：压缩为 zip 文件，通过 API 上传。
5. **调用技能**：在响应 API 中引用技能，通过托管 shell 执行。
