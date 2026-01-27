# Tips for getting coding agents to write good Python tests
- URL: https://simonwillison.net/2026/Jan/26/tests/
- Added At: 2026-01-27 13:24:40
- Tags: #read #llm #guide

## TL;DR
本文分享了让AI代理编写高质量Python测试的技巧，包括选择Python语言利用丰富数据、使用pytest工具优化代码、在良好测试环境中促进学习，以及模仿现有项目模式。

## Summary
本文分享了如何让编码代理（如AI助手）编写高质量Python测试的实用技巧。关键建议包括：

- 选择Python语言，因为训练数据中有丰富的pytest测试示例，代理能理解特定指令，如使用pytest-httpx模拟HTTP端点。
- 监控测试代码，避免重复设置代码，推荐使用pytest.mark.parametrize和pytest fixture来重构。
- 优先在已有良好测试模式的项目中工作，代理会自动学习并匹配高质量测试。
- 通过克隆和模仿现有项目（如datasette/datasette-enrichments）的测试模式，快速指导代理。
