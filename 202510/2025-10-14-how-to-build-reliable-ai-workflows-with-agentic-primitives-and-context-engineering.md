# How to build reliable AI workflows with agentic primitives and context engineering
- URL: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/
- Added At: 2025-10-14 14:21:53
- [Link To Text](2025-10-14-how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering_raw.md)

## TL;DR
本文提出构建可靠AI工作流的三层框架：Markdown提示工程、代理原语系统化与上下文工程管理，结合工具链和包管理支持，旨在实现AI开发从实验到可重复工程实践的转变，提升可预测性与可扩展性。

## Summary
本文介绍了构建可靠AI工作流的三层框架，核心是通过代理原语和上下文工程将AI开发从临时实验转变为可重复的工程实践。

### 框架概述
框架包含以下三层：
1. **Markdown提示工程**：使用Markdown结构（如标题、列表）编写清晰、结构化的提示，通过上下文加载、角色激活、工具集成等技术提高AI输出的可预测性。
2. **代理原语**：将提示工程系统化为可复用的模块，包括指令文件（.instructions.md）、聊天模式文件（.chatmode.md）、工作流文件（.prompt.md）等，实现模块化和可配置性。
3. **上下文工程**：管理AI的上下文窗口，通过会话拆分、模块化指令、记忆驱动开发等技术，确保AI聚焦相关信息，提升可靠性和效率。

### 工具链与生态
- **自然语言即代码**：代理原语类似软件代码，需要工具链支持其模块化、依赖管理和分发。
- **运行时环境**：如Copilot CLI，支持从命令行执行代理原语，实现自动化集成。
- **包管理**：APM（Agent Package Manager）提供运行时管理、依赖解决和打包分发功能，类似npm，支持团队协作和生产部署。
- **生产部署**：通过CI/CD流水线（如GitHub Actions）自动化运行AI工作流，确保可靠性和一致性。

### 实施步骤
1. **指令架构**：创建全局和模块化的.instructions.md文件，应用applyTo语法针对特定文件类型提供指导。
2. **聊天模式配置**：定义.chatmode.md文件，设置角色边界和MCP工具权限，防止跨域干扰。
3. **代理工作流**：使用.prompt.md文件构建端到端流程，内置验证环节，支持本地或自动化执行。
4. **规范模板**：采用.spec.md文件标准化需求规划，使用工具如Spec-kit生成可执行的任务清单。

### 生态演进
AI原生开发遵循编程语言的演进规律：从原始代理原语，到运行时和包管理工具，最终形成共享库和社区生态。APM等工具加速了这一过程，使自然语言程序可规模化管理。

该框架旨在通过结构化方法，提升AI工作流的可靠性、可重复性和可扩展性，适用于从个人开发到企业级部署的全场景。
