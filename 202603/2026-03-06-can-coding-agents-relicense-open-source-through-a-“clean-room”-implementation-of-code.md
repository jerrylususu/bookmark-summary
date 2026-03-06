# Can coding agents relicense open source through a “clean room” implementation of code?
- URL: https://simonwillison.net/2026/Mar/5/chardet/
- Added At: 2026-03-06 14:04:05
- Tags: #read

## TL;DR
文章以chardet库为例，探讨AI辅助的“洁净室”重写是否合规。Dan用Claude重写代码并改用MIT许可证，但原作者质疑其合法性。争议焦点在于AI是否真正独立，反映了开源领域AI辅助编程的法律与伦理挑战。

## Summary
文章探讨了编码代理是否能通过“洁净室”实现来重新授权开源代码。作者以Python库chardet为例，说明了当前面临的争议：chardet的维护者Dan Blanchard使用AI工具Claude从头重写了代码，并将其从LGPL许可证改为MIT许可证，声称这是独立的“洁净室”实现。然而，原作者Mark Pilgrim反对这一做法，认为由于Dan长期接触原始代码，这并非真正的洁净室实现，违反了LGPL许可证。

Dan通过代码相似度工具JPlag证明新版本与旧版本相似度极低（最高1.29%），并详细描述了重写过程：他在空仓库中开始，明确指示Claude不基于LGPL代码，并逐步迭代。但争议点在于：Dan对原始代码的深入了解、Claude可能参考了代码库、以及AI模型训练数据可能包含chardet代码，这些都使“洁净室”的合法性存疑。

文章指出，这一案例反映了AI辅助编程在开源领域的法律和伦理挑战，可能预示着商业世界中类似问题的出现，甚至引发诉讼。作者个人倾向于认为重写是合法的，但双方论点均有合理性。
