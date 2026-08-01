# smevals - a small eval suite for evaluating models, prompts, and harnesses | Prime Radiant
- URL: https://primeradiant.com/blog/2026/smevals.html
- Added At: 2026-08-01 05:12:52
- Tags: #read #agent #llm

## TL;DR
smevals 是评估小模型的 CLI 工具，可自定义任务和评分，对比多模型，支持编码代理辅助搭建评估，并提供可视化报告，帮助从廉价模型中找到最佳方案。

## Summary
smevals 是一个基于 Python 的 CLI 工具，专为评估小型语言模型而设计。它的目标不是追逐最前沿、昂贵的模型，而是在大量廉价模型（包括本地运行的开源模型）中找到最适合特定任务的方案。随着前沿模型价格持续上涨，这种评估体系变得尤为重要。

smevals 的核心概念十分明确：
- **eval**：一组用于回答某个模型能力问题的挑战集合，例如“模型生成 SVG 的能力如何？”
- **task**：eval 中的单一具体挑战，比如“生成一幅鹈鹕骑自行车的 SVG”。
- **config**：运行评估时所用的配置，可指定模型、系统提示词、模型参数甚至代理外壳，同一个 eval 可以同时应对多个 config。
- **run**：用某个 config 执行某个 task 的完整记录，产生的数据由 runner 脚本负责收集。
- **grader**：对 run 的结果进行评分的组件，产生 grade。每个 grader 包含一系列 check，既可以是简单检查（如输出中是否包含特定字符串、是否为合法 XML），也可以是通过自定义脚本（称为 checker）实现的复杂评判，甚至可以利用其他模型来辅助判断。

使用 smevals 的流程大致分四步：
1. 为 eval 设计和实现 task。
2. 确定评分方式，设计 grader 和 checker。
3. 针对一个或多个模型配置运行 task，生成 run 记录。
4. 运行 grader 对结果进行打分，得出每个 run 的成绩。

运行结果既能在终端直接查看，也能通过内置的 Web 应用可视化浏览（`smevals serve`），或者构建为纯静态站点（`smevals build`）以便部署到静态托管服务。

文章特别强调了 smevals 能让编码代理（如 Claude Code、OpenAI Codex 等）直接参与 eval 的构建。只需让代理运行 `uvx smevals docs` 阅读文档，然后给出类似“构建一个测试模型写俳句能力的 eval，包含两个任务：写一首关于鹈鹕的俳句，以及一首关于两情相悦的水獭的俳句”的指令，代理就能在当前目录生成完整的 eval 目录结构（包含 eval.yaml、tasks 文件、configs、graders、checkers 和执行脚本等）。开发者随后可以用 `uvx smevals run . -g` 一键运行并评分，还能通过 `-m` 参数指定多个模型进行对比。

grader 的灵活性很强，初始可能只是一个简单的检查脚本（如判断输出是否恰好包含三个非空行），但可以不断改进。例如在俳句案例中，作者让 Codex 增加了一个使用 gpt-5.5 的 checker，通过 LLM 评判俳句的音节是否符合 5-7-5 规律、主题是否相符、诗意如何，并设定 pass_threshold 为 0.8。由于 smevals 将运行和评分解耦，更新 grader 后只需执行 `uvx smevals grade . --regrade` 就能对历史 run 重新打分，无需重复运行模型。

最终，无论是 Web 应用还是静态报告，都能清晰展示不同模型在各项任务上的得分、通过率、最近运行记录等，帮助团队直观地比较各类小型模型在特定场景下的真实表现，从而为生产环境选出性价比最优的选择。
