# What we learned copying all the best code assistants
- URL: https://blog.val.town/blog/fast-follow/
- Added At: 2025-01-05 02:53:40
- [Link To Text](2025-01-05-what-we-learned-copying-all-the-best-code-assistants_raw.md)

## TL;DR
Val Town团队通过不断集成最新代码生成工具（如GitHub Copilot、ChatGPT、Claude Artifacts等），优化代码补全和生成体验。他们开发了Townie工具，支持快速生成全栈应用，并计划引入多文件编辑和自动错误修复功能。团队致力于提供无需部署的托管服务和API，未来将继续开发完全集成的Web AI代码编辑器，保持合作精神并鼓励用户反馈。

## Summary
1. **Val Town背景**：
   - Val Town自2022年推出代码托管服务以来，用户一直期待获得最先进的LLM代码生成体验。
   - 随着技术的快速发展，Val Town团队不断跟进最新的代码生成工具，如GitHub Copilot、ChatGPT、Claude Artifacts等。

2. **GitHub Copilot体验**：
   - 最初，Val Town用户希望获得类似GitHub Copilot的代码补全体验。
   - 团队通过使用Asad Memon的codemirror-copilot插件，初步实现了基于ChatGPT的代码补全功能，但存在速度慢和准确性不足的问题。
   - 最终，团队转向使用Codeium，并开源了codemirror-codeium组件，提供了更快速和准确的代码补全体验。

3. **ChatGPT集成**：
   - 用户开始使用ChatGPT生成Val Town代码，团队为此开发了Townie工具，提供预填充的系统提示和一键保存生成代码的功能。
   - 初始版本的Townie基于GPT-3.5，但由于编程语言的模糊性，用户需要多次对话才能获得满意的结果。

4. **ChatGPT工具使用**：
   - 团队尝试通过OpenAPI规范让AI调用Val Town的功能，但效果不佳，AI经常产生幻觉，调用不存在的函数。
   - 尽管功能调用有所改进，但界面过于通用，无法有效支持代码迭代。

5. **Claude Artifacts**：
   - Claude 3.5 Sonnet在代码生成方面表现出色，Claude Artifacts解决了反馈循环问题。
   - 团队基于此开发了当前版本的Townie，能够在几分钟内生成全栈应用并部署。

6. **Val Town的贡献**：
   - **速度优化**：团队致力于减少代码生成时间，尝试通过生成差异（diffs）来优化反馈循环，但尚未完全解决。
   - **自动错误检测**：团队开发了自动检测错误并提供解决方案的UI交互，虽然不具创新性，但可能影响了其他工具的开发。

7. **托管运行时和API**：
   - Val Town提供了无需部署的托管服务、持久化数据存储以及无需API密钥即可使用LLM的功能。
   - 这些功能可能影响了GitHub Spark等工具的开发。

8. **Cursor和Windsurf**：
   - Cursor在大规模代码库开发中表现出色，而Windsurf的Cascade功能则提供了多文件编辑和工具使用的体验。
   - 团队计划为Townie引入类似功能，使其能够搜索公共代码库和资源。

9. **Devin的启发**：
   - 团队受到Devin的启发，设想Townie能够自动检测并修复错误，甚至在没有人工干预的情况下进行多次迭代。
   - 未来，Townie可能能够生成复杂的应用，如Hacker News克隆，并在用户睡觉时完成开发。

10. **合作与竞争**：
    - 尽管Val Town在快速跟进其他工具的功能，但整体氛围更倾向于合作而非竞争。
    - 团队公开系统提示和技术选择，希望保持这种合作精神。

11. **未来方向**：
    - 团队考虑是否退出竞争，专注于核心差异化功能，或继续快速跟进其他工具的功能。
    - 最终决定继续开发完全集成的Web AI代码编辑器体验，尽管可能落后于大公司几个月。

12. **Townie的推荐**：
    - 文章最后推荐用户尝试Townie，并鼓励用户提供反馈，帮助团队改进工具。

13. **致谢**：
    - 感谢Tom MacWright、JP Posma和Simon Willison对文章草稿的反馈。
