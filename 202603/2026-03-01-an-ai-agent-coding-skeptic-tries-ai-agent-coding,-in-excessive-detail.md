# An AI agent coding skeptic tries AI agent coding, in excessive detail
- URL: https://minimaxir.com/2026/02/ai-agent-coding/
- Added At: 2026-03-01 08:43:38
- Tags: #read #agent #deepdive

## TL;DR
作者记录了使用Claude Opus 4.5进行编码的实验，发现其在复杂代码编写和遵循规则方面表现优异。通过多个项目测试，作者认为AI代理在拥有足够领域知识的情况下能有效辅助开发，但需谨慎使用并优化工作流程。

## Summary
作者以AI代理编码怀疑论者的身份，详细记录了自己尝试使用AI代理（特别是Claude Opus 4.5）进行编码的全过程。文章首先回顾了作者此前对AI代理的负面看法，认为其不可靠、昂贵且效果不佳。然而，通过一系列实验，作者发现Claude Opus 4.5的表现远超预期，尤其是在编写复杂代码和遵循详细规则方面。

作者首先介绍了`AGENTS.md`文件的重要性，该文件用于指导AI代理的行为，如代码格式和最佳实践。通过精心设计的规则（如禁止使用表情符号、避免冗余注释），作者显著提升了AI代理的输出质量。

随后，作者通过多个项目测试了Opus 4.5的能力：
1. **YouTube数据抓取与可视化**：Opus 4.5成功编写了Python脚本，从YouTube API抓取数据并存储到SQLite数据库，还生成了Jupyter Notebook进行数据分析，并创建了一个使用FastAPI、HTMX和Pico CSS的Web应用。
2. **Rust项目**：作者测试了Opus 4.5在Rust语言上的表现，包括：
   - **icon-to-image**：一个将图标字体渲染为图像的Rust/Python包，使用PyO3实现Python绑定。
   - **word clouds**：一个基于Rust的词云生成器，支持WebAssembly输出。
   - **miditui**：一个终端内的MIDI作曲和播放器。
   - **ballin**：一个终端内的物理模拟器，使用Braille Unicode字符实现高细节渲染。

作者发现，Opus 4.5能够处理复杂的任务，甚至在某些情况下一次性完成编码。尽管在测试和调试方面存在局限（如无法直接查看终端输出），但作者通过QA技能协助AI修复了问题。

文章总结指出，AI代理在作者拥有足够领域知识的情况下表现最佳，能够帮助实现那些作者知道如何做但缺乏时间或精力去实现的项目。作者对AI代理的未来持乐观态度，但仍强调需要谨慎使用，并持续优化工作流程。
