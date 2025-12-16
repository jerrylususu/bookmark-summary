# I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in 4.5 hours
- URL: https://simonwillison.net/2025/Dec/15/porting-justhtml/
- Added At: 2025-12-16 13:18:24
- Tags: #read #llm
- [Link To Text](2025-12-16-i-ported-justhtml-from-python-to-javascript-with-codex-cli-and-gpt-5.2-in-4.5-hours_raw.md)

## TL;DR
作者使用GPT-5.2在4.5小时内将Python库JustHTML移植为JavaScript版本，成果包含9000行代码并通过9200项测试。项目利用AI自动编写和测试代码，费用极低，凸显了AI在代码移植中的高效性，但也引发了关于伦理、版权与生成代码质量的争议。

## Summary
本文记录了作者使用Codex CLI和GPT-5.2在4.5小时内将JustHTML Python库移植为JavaScript版本的过程与反思。

### 项目概述
- **目标**：将Emil Stenström开发的纯Python HTML5解析库JustHTML移植为JavaScript版本，保持无依赖、通过html5lib-tests测试套件。
- **成果**：创建了[simonw/justjshtml](https://github.com/simonw/justjshtml)库，包含9000行代码，通过9200项测试，支持浏览器和Node.js。
- **工具与成本**：使用GPT-5.2和Codex CLI（启用`--yolo`模式），消耗约208万令牌（理论成本$29.41，实际因ChatGPT Plus订阅未产生额外费用）。

### 实施过程
1. **准备阶段**：克隆原库和测试库，创建新项目目录。
2. **制定规范**：通过提示词让AI分析原库并生成API设计文档（[spec.md](https://github.com/simonw/justjshtml/blob/19b8eb1f2ca80f428a3c40862d5ec05d36e5166b/spec.md)），明确分阶段实现计划。
3. **迭代开发**：
   - 从“里程碑0.5”（解析简单文档）开始，逐步完善。
   - 配置CI/CD（GitHub Actions），实时监控提交记录。
   - AI自动完成代码编写、测试和提交，期间因令牌限额暂停后继续。
4. **收尾工作**：添加浏览器playground界面和详细README文档。

### 关键洞察
- **LLM能力**：前沿模型（如GPT-5.2）能胜任复杂、长时间的任务，需最小人工干预。
- **测试驱动**：拥有健全测试套件是成功部署智能代理循环（agentic loop）的关键。
- **代码成本**：生成代码的成本极低，但确保其可靠性仍需投入。
- **移植效率**：AI能高效完成跨语言库移植，但引发伦理与法律争议。

### 伦理与法律疑问
作者提出开放性问题，反思这种开发方式的潜在影响：
- **合法性**：直接移植是否侵犯原库（Python/Rust）版权？
- **道德性**：快速生成代码是否合乎开源伦理？是否会损害开源生态？
- **责任性**：AI生成的代码能否主张版权？此类库是否适合投入生产环境？
- **质量对比**：与专家数月手工开发的库相比，AI生成库的质量差距如何？

总结而言，项目展示了AI在代码移植中的高效性，同时凸显了技术普及后面临的伦理、法律与质量保障挑战。
