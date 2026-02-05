# Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel
- URL: https://simonwillison.net/2026/Feb/4/distributing-go-binaries/
- Added At: 2026-02-05 13:47:27
- Tags: #read #tips

## TL;DR
本文介绍go-to-wheel工具，它能自动将Go二进制打包为Python wheel并通过PyPI分发，简化安装（如`uvx sqlite-scanner`），使Go高性能工具无缝集成到Python项目中。

## Summary
文章讨论了通过PyPI分发Go二进制文件的方法，特别是使用go-to-wheel工具自动化此过程。以下是结构化总结：

### 背景
- Simon Willison探索使用Go构建小型、快速的二进制应用，但分发是挑战。
- 通过PyPI分发Go二进制文件，用户只需运行如`uvx sqlite-scanner`即可安装和使用，无需手动编译或处理操作系统兼容性问题。

### sqlite-scanner工具
- sqlite-scanner是一个Go编写的CLI工具，用于递归扫描文件系统中的SQLite数据库文件，通过检查文件头魔法数字识别。
- 支持多种输出格式（如纯文本、JSON、JSONL），并可显示文件大小。
- 用户可以通过GitHub下载、编译或直接使用PyPI安装（如`uvx sqlite-scanner`）。

### PyPI分发机制
- PyPI根据文件名自动选择适合用户操作系统和架构的wheel文件（如macOS、Linux、Windows的不同版本）。
- wheel文件包含Go二进制和一个Python包装器，其中`__init__.py`文件处理二进制执行：在Unix系统设置可执行权限，在Windows使用子进程。
- 通过entry point定义，Python包可直接执行二进制。

### 作为依赖项的优势
- 这种分发方式允许Go二进制作为Python包的依赖项，例如在datasette-scan插件中，使用sqlite-scanner扫描数据库并集成到Datasette实例。
- 演示了如何通过`uv run --with datasette-scan`直接使用，无需预先安装。

### go-to-wheel工具
- Willison开发了go-to-wheel工具，自动化从Go包构建Python wheel的过程。
- 工具通过命令行参数设置版本、作者等信息，生成多平台wheel文件，并使用twine上传到PyPI。
- 示例命令：`uvx go-to-wheel`构建包，然后测试和发布。

### 结论与展望
- 这种模式结合了Go的高性能、并发优势和Python的易用性，允许无缝集成Go二进制到Python项目。
- Willison计划广泛使用此模式，因Go适合HTTP工具和WebAssembly等场景，提升开发效率。
