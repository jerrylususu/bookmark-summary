# Building Python tools with a one-shot prompt using uv run and Claude Projects
- URL: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/
- Added At: 2024-12-19 14:45:47

## TL;DR
作者分享了使用Claude和uv构建一次性Python工具的经验，通过内联依赖和uv run实现快速开发和运行，展示了如何利用LLM生成高效的单文件工具。

## Summary
1. **背景介绍**：
   - 作者使用Claude构建一次性HTML+JavaScript应用程序的经验丰富。
   - 最近开始使用类似模式创建一次性Python工具，结合Claude项目和uv的依赖管理功能。

2. **一次性提示**：
   - 在LLM术语中，“一次性”提示是指首次尝试就能生成完整结果的提示。

3. **示例工具**：
   - **S3访问调试工具**：
     - 作者在处理Amazon S3文件访问问题时，使用Claude生成一个Python CLI工具。
     - 该工具使用Click和boto3库，尝试使用所有boto3技巧来调试404错误。
     - 工具生成的脚本可以直接运行，无需额外安装依赖。

4. **内联依赖和uv run**：
   - **内联依赖**：脚本开头包含一个魔法注释，声明所需的Python版本和依赖库。
   - **uv run**：运行脚本时，uv会自动创建临时虚拟环境并安装所需依赖，过程快速且高效。
   - **URL支持**：脚本可以通过URL指定，任何人只需安装uv即可运行。

5. **Claude项目的帮助**：
   - **Claude项目**：作者设置了一个名为“Python app”的Claude项目，包含自定义指令。
   - **自定义指令**：教导Claude如何利用内联脚本依赖，生成单文件Python工具。
   - **自动选择依赖**：Claude会根据需要自动选择合适的库，如在`debug_s3_access.py`中使用了rich库。

6. **其他示例**：
   - **HTML标签去除工具**：
     - 作者提示Claude生成一个Starlette Web应用，用于去除HTML标签并返回纯文本。
     - 生成的脚本可以直接运行，使用beautifulsoup库处理HTML。

7. **自定义指令**：
   - **模式创新**：通过自定义指令或系统提示，向LLM展示如何实现新模式，即使这些模式不在其训练数据中。
   - **uv run**：尽管uv run较新，但提供简短示例足以让模型生成利用其功能的代码。
   - **HTML和JavaScript工具**：作者还使用类似方法生成单页HTML和JavaScript工具，避免使用React，保持依赖最小化。
