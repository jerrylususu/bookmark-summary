# The Unexpected Effectiveness of One-Shot Decompilation with Claude
- URL: https://blog.chrislewis.au/the-unexpected-effectiveness-of-one-shot-decompilation-with-claude/
- Added At: 2025-12-07 12:55:39
- Tags: #read #llm #guide
- [Link To Text](2025-12-07-the-unexpected-effectiveness-of-one-shot-decompilation-with-claude_raw.md)

## TL;DR
文章介绍了一种利用Claude AI在无头模式下自动化反编译的方法，通过评分器、Claude、工具集和驱动脚本协同工作，大幅提升了效率。例如，在《Snowboard Kids 2》项目中，3周内取得的进展超过过去3个月。Claude表现优于其他工具，但输出代码可读性仍需人工优化。方法强调自动化减少人力，但LLM的输出和资源限制仍是挑战。

## Summary
文章讨论了使用Claude进行“单次”反编译的方法及其出人意料的高效性。该方法通过Claude的无头模式自动循环处理函数，显著提升了反编译项目（以《Snowboard Kids 2》为例）的进度，在3周内取得的进展超过了过去3个月的总和。

**工作流程**  
核心是通过一个名为`vacuum.sh`的脚本自动化执行反编译，该系统包含四个组件：  
1. **评分器（Scorer）**：选择最可能匹配的函数优先处理，使用基于指令数、分支数等特征的逻辑回归模型优化评分。  
2. **Claude**：执行实际反编译，遵循明确提示（如尝试10次后放弃，成功则提交更改）。  
3. **工具集（Toolbox）**：提供防御性工具（如明确的错误处理说明），避免Claude陷入无效循环，同时注重令牌效率。  
4. **驱动脚本（Driver）**：管理循环执行、错误处理和日志记录。

**性能对比**  
- Claude（尤其是Opus 4.5）表现优于Codex等代理，后者存在指令遵循和Git操作问题。  
- 预计79%的函数可通过Claude匹配，但剩余函数难度较高，且输出代码可能存在可读性问题（如过度使用goto语句）。

**关键洞见**  
- **效率提升**：自动化减少了人工干预，但需防范Claude的异常行为（如令牌浪费）。  
- **未来方向**：反编译工作的限制因素可能从人力转向计算资源，而LLM输出仍需人工清理和优化以提升可读性。  
- **社区价值**：项目依赖开源工具（如Splat、m2c）和社区支持，强调人类专家在复杂任务中不可替代。

文章最后鼓励读者尝试挑战Claude未能处理的函数，并参与相关讨论。
