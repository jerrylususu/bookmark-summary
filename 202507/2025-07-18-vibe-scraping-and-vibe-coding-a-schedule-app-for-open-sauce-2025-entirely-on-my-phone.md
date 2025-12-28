# Vibe scraping and vibe coding a schedule app for Open Sauce 2025 entirely on my phone
- URL: https://simonwillison.net/2025/Jul/17/vibe-scraping/
- Added At: 2025-07-18 13:23:08

## TL;DR


作者利用Codex和Claude Artifacts工具手机端开发会议日程应用，通过Playwright自动化爬取并解析官网数据，部署至GitHub Pages解决移动端显示与日历问题。优化中压缩图片93KB、增强无障碍功能，验证AI辅助移动端开发可行性，强调开发者策略与AI协作的重要性，同时需预先规划性能与无障碍需求。

## Summary


作者结合 Codex 和 Claude Artifacts 工具，通过手机完成了 Open Sauce 2025 会议日程应用的开发。首先，用 Codex 执行 Playwright 自动化脚本爬取了官网非移动端友好的日程页面，并通过一系列命令提取隐含的 316KB JavaScript 文件中的结构化日程数据，最终生成并提交包含完整 JSON 数据的 Pull Request。接着尝试用 Claude Artifacts 构建网页前端时多次受挫，因沙盒限制和网络问题无法调用本地文件，最终改用直接拉取 GitHub 上的 JSON 数据并部署到 GitHub Pages，解决了移动端显示和日历 ICS 导入问题。项目过程中因错误日期信息触发了紧急修复，再次通过 Codex 自动化脚本快速修正了部署代码。尽管手机开发受限于工具交互性，但整体流程展示了 AI 辅助编程在手机端独立完成复杂任务的可能性。后续因用户反馈发现性能与可访问性缺陷：最初版本加载了 130MB 未经压缩的头像图片，作者通过 Codex 移除冗余图片元素将体积压缩至 93KB；又因 HTML 结构不符合无障碍标准，Codex 在第二次迭代中新增导航链接、优化 ARIA 标签，使网页通过 VoiceOver 检测。作者强调，25 年的开发经验在选择策略（如通过 Playwright 执行网络请求而非图像识别解析）、规避工具限制（Claude 沙盒无法访问文件系统）中起到关键作用，但实际编码细节大多由 AI 生成。此次实践验证了 AI 代理在移动端自动化任务的可行性，但也提醒需主动在初始指令中强调性能和无障碍需求，避免后期返工。
