# My LLM codegen workflow atm
- URL: https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
- Added At: 2025-02-22 05:08:41
- [Link To Text](2025-02-22-my-llm-codegen-workflow-atm_raw.md)

## TL;DR
本文介绍了使用大语言模型进行代码生成的工作流程，包括头脑风暴、规划和执行，适用于Greenfield和非Greenfield开发。强调了提示词魔法和规划的重要性，同时提到当前LLM工作流主要为单人模式，期待多人协作的改进。

## Summary
1. **概述**：作者分享了使用大语言模型（LLM）进行代码生成的流程，适用于构建小型产品。流程包括头脑风暴、规划和执行，采用离散循环的方式。

2. **开发路径**：
   - **Greenfield开发**：从头开始的新项目。
   - **Legacy现代代码**：迭代和增量工作在现有代码库上。

3. **Greenfield开发的流程**：
   - **步骤1：头脑风暴**：
     - 使用LLM（如ChatGPT 4o / o3）细化想法，迭代地生成详细规范。
     - 将生成的规范保存为`spec.md`，用于后续步骤。
   - **步骤2：规划**：
     - 使用推理模型（如o1*、o3*、r1）细化规划，生成详细的蓝图和分步计划。
     - 输出`prompt_plan.md`和`todo.md`，便于执行和状态跟踪。
   - **步骤3：执行**：
     - 使用多种工具（如github workspace、aider、cursor等）进行代码生成。
     - 作者偏好使用Claude和aider进行迭代编程，通过repomix工具处理问题。

4. **非Greenfield开发的流程**：
   - **获取上下文**：使用工具（如repomix）将代码库内容高效输入LLM。
   - **任务执行**：针对每个任务进行规划和执行，使用Claude或aider进行代码生成和调试。

5. **提示词魔法**：
   - 提供了一系列用于代码审查、GitHub问题生成和缺失测试生成的提示词模板，便于快速改进代码库。

6. **滑雪隐喻**：
   - 强调保持控制的重要性，使用规划步骤和测试来避免“失控”。

7. **团队协作的挑战**：
   - 当前的LLM工作流主要是单人模式，作者希望有人能解决多人协作的问题，使其成为多人游戏体验。

8. **时间管理**：
   - 由于LLM处理时间较长，作者采取多种方式利用等待时间，如开始新项目头脑风暴、听音乐、玩游戏等。

9. **反对者的观点**：
   - 作者理解并尊重对LLM的怀疑态度，同时推荐Ethan Mollick的书《Co-Intelligence: Living and Working with AI》来解释LLM的益处。
