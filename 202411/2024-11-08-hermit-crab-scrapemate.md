# hermit-crab/ScrapeMate
- URL: https://github.com/hermit-crab/ScrapeMate
- Added At: 2024-11-08 14:33:40

## TL;DR
ScrapeMate是一款网页抓取助手工具，支持Chrome/Firefox扩展，提供元素选择器、预设编辑器等功能，计划增加嵌套选择器和实际提取功能。项目采用GPL-3.0许可证，主要使用JavaScript、CSS和Vue开发。

## Summary
1. **项目概述**：
   - **名称**：ScrapeMate
   - **功能**：网页抓取助手工具，用于编辑和维护跨网页的CSS/XPath选择器。
   - **平台**：提供Chrome/Chromium和Firefox扩展。

2. **主要特性**：
   - **元素选择器**：基于SelectorGadget的元素选择器。
   - **预设列表**：维护所有工作过的预设列表。
   - **预设编辑器**：JSON编辑器，便于与scrapy或其他类似工具结合使用，支持选择性导入/导出。
   - **快速预览**：当前选定数据的快速预览。
   - **选择器支持**：支持`::text` / `::attr()` CSS伪元素和`has-class()` XPath函数。
   - **JavaScript切换**：为当前工作标签切换JavaScript。

3. **计划特性**：
   - 嵌套选择器
   - 更多模板测试
   - 可能的实际提取功能

4. **构建说明**：
   - 使用npm安装依赖并构建项目。
   - 构建完成后，生成的扩展文件夹可用于Chrome作为未打包扩展，或用于Firefox作为临时扩展。

5. **截图**：
   - 提供了两个截图，展示了工具的界面和功能。

6. **其他说明**：
   - 最初设计为书签工具，但由于各种限制，书签模式已被放弃。

7. **文件结构**：
   - **icons**：图标文件夹
   - **src**：源代码文件夹
   - **vendor**：第三方库文件夹
   - **.gitignore**：Git忽略文件
   - **LICENSE**：GPL-3.0许可证
   - **README.md**：项目说明文件
   - **TODO**：待办事项文件
   - **manifest.json**：扩展清单文件
   - **package-lock.json**：npm锁定文件
   - **package.json**：npm配置文件
   - **package.sh**：打包脚本
   - **webpack.config.js**：Webpack配置文件

8. **社区与统计**：
   - **Stars**：100
   - **Forks**：13
   - **Watchers**：6
   - **语言**：JavaScript（65.4%）、CSS（18.4%）、Vue（15.2%）、其他（1.0%）

9. **许可证**：
   - **GPL-3.0**：项目采用GPL-3.0许可证。
