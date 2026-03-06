# Agentic manual testing - Agentic Engineering Patterns
- URL: https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/
- Added At: 2026-03-06 13:34:48
- Tags: #read #agent #tips

## TL;DR
文章强调在代理工程中手动测试的重要性，指出自动化测试不足以发现所有问题。通过Python代码片段、curl测试API及浏览器工具如Playwright、Rodney和Showboat进行手动测试，可发现遗漏问题、生成文档，并补充自动化测试，形成闭环。

## Summary
文章探讨了在代理工程中进行手动测试的重要性及具体方法。核心观点是：编码代理能执行自己编写的代码，但仅靠自动化测试不足以确保代码按预期工作，手动测试能发现自动化测试遗漏的问题。

主要机制包括：
- 对于Python库，使用 `python -c` 直接执行代码片段进行测试。
- 对于Web应用，使用 `curl` 命令探索和测试JSON API。
- 对于交互式Web UI，推荐使用浏览器自动化工具如Playwright，并介绍了作者开发的Rodney（基于Chrome DevTools Protocol）和Showboat（用于记录测试过程）工具。

文章强调，通过代理进行手动测试不仅能发现问题，还能生成文档和演示，帮助验证代理的工作成果。同时，发现的问题可以补充到自动化测试中，形成闭环。
