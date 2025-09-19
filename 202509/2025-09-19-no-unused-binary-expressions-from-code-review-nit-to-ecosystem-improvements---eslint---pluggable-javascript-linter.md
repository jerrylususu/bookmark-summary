# no-unused-binary-expressions: From code review nit to ecosystem improvements - ESLint - Pluggable JavaScript Linter
- URL: https://eslint.org/blog/2024/10/code-review-nit-to-ecosystem-improvements/
- Added At: 2025-09-19 14:33:12
- [Link To Text](2025-09-19-no-unused-binary-expressions-from-code-review-nit-to-ecosystem-improvements---eslint---pluggable-javascript-linter_raw.md)

## TL;DR
从代码审查发现启发，作者开发了ESLint规则 `no-constant-binary-expressions`，能检测逻辑错误。该规则经4年演进，被纳入ESLint和TypeScript，在大型代码库中发现近百个错误，展现了跨团队合作与开源社区共享的重要性。

## Summary
四年前，一次代码审查中发现TypeFlow未警告无效的null检查，启发了作者创建ESLint规则 `no-constant-binary-expressions`，该规则能捕获各种逻辑错误，例如空对象误判和运算符优先级混淆。这一规则随后影响了TypeScript 5.6的更新，新增了类似的默认验证，在GitHub顶级仓库中发现了近百个错误。

关键时间线包括：
- 2020年5月，作者在Meta内部提出疑问，ESLint专家Brad Zacher建议用语法方法而非类型方法解决问题。
- 2020年8月，作者在Meta内部实现ESLint规则，发现数百个错误。
- 2020年10月，规则提议为ESLint核心规则并被接受。
- 2022年7月，规则在ESLint官方博客介绍，引发关注。
- 2024年4月，ESLint v9.0.0默认启用该规则。
- 2024年7月，TypeScript团队采纳类似验证，基于ESLint规则的启发。
- 2024年9月，TypeScript 5.6发布默认验证功能。

成功因素包括：Meta的内部文化支持工程师自主创新、ESLint的可插拔架构、团队对新贡献的开放态度，以及通过博客和社交媒体的积极传播。作者强调，持续的社会化交流使小想法最终产生广泛生态影响。

未来展望：TypeScript和Flow可基于可靠类型扩展验证；其他不健全语言可采用类似方法；编译器前端的死代码消除技术可用于错误检测。

结论：跨组织协作的关键是社会化分享，从代码审查到公共讨论，逐步扩大影响力。Meta、ESLint和微软各司其职，共同推动了这一改进。
