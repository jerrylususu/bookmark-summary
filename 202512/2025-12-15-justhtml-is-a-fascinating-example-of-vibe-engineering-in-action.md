# JustHTML is a fascinating example of vibe engineering in action
- URL: https://simonwillison.net/2025/Dec/14/justhtml/
- Added At: 2025-12-15 13:46:21
- Tags: #read #llm

## TL;DR
Emil利用AI工具开发的JustHTML库实现了纯Python的高质量HTML解析器，展示了“氛围工程”理念：程序员专注架构设计与测试验证，AI承担编码实现，提升开发效率与代码可靠性。

## Summary
本文介绍了作者Simon Willison对Emil Stenström开发的Python库JustHTML的评论，重点探讨了其作为AI辅助编程案例和“氛围工程”的实践。

### JustHTML库的特点
- **纯Python实现**：无C扩展，易于在Pyodide等非标准环境使用。
- **高兼容性**：通过9,200+个html5lib测试套件，符合HTML5规范。
- **高质量代码**：100%测试覆盖率，仅3,000行实现代码和约11,000行测试代码。
- **功能丰富**：支持CSS选择器查询等。

### AI辅助开发过程
- Emil使用VS Code的Copilot Agent模式，结合Claude、Gemini等多模型，通过自动批准指令和黑名单设置进行开发。
- 开发历时数月，Emil的角色更侧重于架构设计而非编码，体现了“氛围工程”理念。

### 氛围工程 vs. 氛围编程
- **氛围编程**：LLM快速生成代码，无审查，适合原型项目。
- **氛围工程**：专家程序员以专业方式使用AI，确保代码高质量和可靠，JustHTML是典型范例。关键实践包括：
  - 早期集成html5lib测试套件。
  - 自主设计API（如TagHandler基类）。
  - 性能基准测试和Rust优化实验。
  - 重构代码，移植Servo的html5ever库。
  - 使用分析器和模糊测试强化解析器。

### 结论
Emil强调，AI负责“打字”，而开发者负责“思考”，这种分工提升了效率。作者赞同此观点，认为AI辅助让程序员更专注于高价值工作。
