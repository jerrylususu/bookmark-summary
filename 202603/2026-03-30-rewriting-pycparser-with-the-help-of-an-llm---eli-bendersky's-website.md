# Rewriting pycparser with the help of an LLM - Eli Bendersky's website
- URL: https://eli.thegreenplace.net/2026/rewriting-pycparser-with-the-help-of-an-llm/
- Added At: 2026-03-30 13:18:54
- Tags: #read #agent

## TL;DR
作者使用Codex重写pycparser，将其从PLY库转为手写递归下降解析器，提升了性能并解决了维护问题。LLM显著提高了效率（4-5小时完成），但代码仍需人工审查。

## Summary
本文作者讲述了使用LLM编码助手（Codex）重写其开源项目pycparser的经历。pycparser是一个纯Python的C语言解析器，原本使用PLY库进行词法和语法分析。作者决定将其重写为手写的递归下降解析器，以解决PLY带来的维护问题、安全风险以及C语言语法复杂性导致的解析冲突。

重写过程分为几个阶段：首先，作者通过详细的测试套件确保LLM能正确运行并理解项目；接着，LLM成功将解析器从PLY迁移到递归下降实现，并移除了PLY依赖。作者在分支中逐步审查和调整代码，通过多次迭代优化代码质量和性能。最终，新解析器通过了所有测试，性能提升了约30%，并发布了新版本3.00。

作者还探讨了LLM编码助手的优缺点：虽然能高效完成任务，但生成的代码有时可读性差、逻辑混乱，需要人工干预和指导。此外，静态类型标注有助于LLM更好地工作，未来可能更适合强类型语言。

总体而言，这次经历让作者对LLM编码助手的能力印象深刻，认为它们能显著提高开发效率，但代码质量仍需人工把关。作者估计手动完成此项目需30-40小时，而借助LLM仅需4-5小时，且过程更有趣。
