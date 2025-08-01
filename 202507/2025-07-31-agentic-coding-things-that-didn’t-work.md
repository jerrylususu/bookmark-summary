# Agentic Coding Things That Didn’t Work
- URL: https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/
- Added At: 2025-07-31 14:01:45
- [Link To Text](2025-07-31-agentic-coding-things-that-didn’t-work_raw.md)

## TL;DR


作者尝试使用Claude Code等自动化工具后反思：高频操作外的自动化易失败，预设命令（如Slash Commands）和复杂功能（如Hooks、Print Mode）因体验不佳被弃用。实践表明直接对话、手动引导更高效，需动态维护提示而非僵化预设，并警惕过度依赖工具导致技术能力退化。核心原则是保持简单，持续验证自动化价值。（99字）

## Summary


本文总结作者在尝试使用Claude Code等智能编码工具时遇到的失败经验和反思，主要围绕自动化工具的实际应用效果展开：

### **1. 自动化原则**
- **核心规则**：仅自动化高频操作，若自动化失败则直接删除，避免工作流混乱。
- **常见问题**：非必要自动化常因难用、遗忘或过度调试而失败，作者倾向于保持简单：直接与AI对话、提供上下文并依赖剪贴板处理。

### **2. Slash Commands（斜杠命令）的局限性**
- **设计初衷**：预设提示指令以提升效率，但多数命令未被使用。
- **具体案例**：
  - `/fix-bug`：无法超越手动提供GitHub链接加口头说明的效果。
  - `/commit`：生成的提交信息与作者风格不符，最终弃用。
  - `/add-tests`：自动化生成测试代码不如直接用工具可靠。
  - `/fix-nits`：重复编辑未形成习惯，直接对话更高效。
  - `/next-todo`：自动生成待办任务未提升效率。
- **有效案例**：基于Git状态的文件自动修复命令（如语法检查），通过上下文推断文件路径，减少显式参数输入。

### **3. Hooks（钩子）的尝试与挫败**
- **挑战**：无法有效操控执行流程，Yolo模式下钩子的约束限制功能实现。
- **变通方案**：
  - 用拦截脚本强制工具路径，例如通过`uv run`替代普通Python执行。
  - 尝试格式化 Hook 但需频繁重复操作，未能简化流程。
- **结论**：当前钩子使用不如简单脚本有效，仍需探索更优路径。

### **4. Claude Print Mode（打印模式）的不足**
- **潜力与局限**：虽青睐其“确定性脚本+局部推理”的概念，但实际因速度慢、调试困难而使用率低。
- **核心问题**：AI推理的随机性不适合需要明确规则的任务（如格式化、提交代码），这部分工作应由工具而非LLM处理。

### **5. 子任务与代理（Sub Tasks/Agents）的实践**
- **探索结果**：
  - 并行任务分割未能显著提升效率，尤其在读写混合场景易出错。
  - 子代理虽理论上可隔离上下文，但实际效果与手动记录、切换界面无异。
- **替代方案**：优先使用基础工具（如Markdown记录）或外部编辑器（如o3）处理复杂协同任务。

### **6. 自动化的核心挑战**
- **结构化缺失**：缺乏标准化工作流（如模板化提交信息）限制AI学习能力。
- **上下文管理**：静态预设提示易导致信息过载或遗漏，动态口头表达更灵活。
- **思维惰性风险**：过度依赖自动化可能削弱工程思维，需主动监督输出质量，避免过度信任AI。

### **7. 经验总结**
- **简单为王**：多数场景下，直接语音输入+手动引导比复杂自动化更高效。
- **动态调整优先**：通过剪贴板维护常用提示，而非僵化预设命令。
- **警惕盲区**：自动化需持续验证价值，避免因工具依赖导致技术退化与理解下降。
