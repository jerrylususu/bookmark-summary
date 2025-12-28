# I’m Switching to Python and Actually Liking It
- URL: https://www.cesarsotovalero.net/blog/i-am-switching-to-python-and-actually-liking-it.html
- Added At: 2025-09-07 13:27:57

## TL;DR
作者分享转向Python开发AI应用的经验，推荐使用uv、ruff、ty、FastAPI等工具链，采用Monorepo结构和Docker部署，强调自动化与生产级实践。

## Summary
作者基于AI技术的兴起，决定从Java/JavaScript/R等语言转向Python，并分享了其使用Python的经验和工具链。

### 动机
- Python是AI领域的标准编程语言，提供了众多机会。
- 曾用Python编写过小型脚本（如爬取YouTube元数据），发现其语法友好、工具链便捷，适合自动化和跨平台开发。

### Python生态的优势
1. 成熟的数据处理库和工具（如Jupyter）。
2. 性能优化工具（如Cython）提升了速度。
3. 语法改进，隐藏了部分遗留问题（如减少init等冗余代码）。
4. 与VSCode集成良好，适合构建AI应用（如RAG、Agents等）。

### 生产环境挑战
- 实际开发中发现，生产级应用与Jupyter脚本工作流存在差距，需更专业的工具支持。

### 项目结构
- 采用Monorepo结构（后端+前端），理由包括：
  - 避免代码分散，便于搜索和管理。
  - 减少不必要复杂度，适合个人或小团队。
  - 简化构建、测试和部署流程。
- 项目目录结构示例包含API后端、UI前端、文档、CI/CD配置等，强调前后端分离（UI轻量，处理逻辑委托给后端API）。

### 工具链推荐
- **uv**: Python包管理和构建工具，替代pip，高效管理依赖。
- **ruff**: 快速代码检查和格式化工具，集成多种linter功能。
- **ty**: 类型检查器，增强代码质量。
- **pytest**: 测试框架，支持fixtures和参数化测试。
- **Pydantic**: 数据验证和设置管理，支持环境变量加载。
- **MkDocs**: 文档生成工具，用于项目网站。
- **FastAPI**: 高性能API框架，基于Starlette和Pydantic。
- **Dataclasses**: Python内置功能，减少数据类样板代码。

### 版本控制和CI/CD
- **GitHub Actions**: 用于跨OS的CI/CD，示例工作流包括Docker构建和测试。
- **Dependabot**: 自动更新依赖。
- **Gitleaks**: 防止敏感信息泄露。
- **Pre-commit Hooks**: 提交前运行代码检查和格式化（如ruff、gitleaks）。

### 基础设施管理
- **Make**: 自动化常见任务（测试、构建、部署）。
- **Docker**: 容器化应用，确保环境一致性；使用Docker Compose管理多服务。
- 示例Dockerfile和docker-compose.yml展示了如何封装后端API和前端UI。

### 总结
作者通过实际项目验证了Python的实用性，强调工具链集成和自动化的重要性，旨在帮助开发者构建生产就绪的Python应用。整体偏向个人偏好，但提供了可复用的实践参考。
