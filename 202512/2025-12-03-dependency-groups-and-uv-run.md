# Dependency groups and uv run
- URL: https://til.simonwillison.net/uv/dependency-groups
- Added At: 2025-12-03 14:33:24
- Tags: #read #tips

## TL;DR
本文介绍了一种基于uv工具的新型Python开发模式，利用PEP 735依赖组简化项目流程。核心是使用`uv init`创建库项目，通过`uv add`添加dev依赖组，运行`uv run pytest`自动处理环境和测试。模式无需手动管理虚拟环境，便于协作与打包，提升开发效率。

## Summary
文章介绍了作者在使用uv工具时采用的一种新开发模式，利用PEP 735依赖组来简化Python项目的开发流程。

**核心模式**：  
- 使用`uv init --lib`创建新Python库项目，生成`pyproject.toml`文件。  
- 通过`uv add --dev pytest`添加开发依赖（如pytest），自动在`pyproject.toml`中创建`[dependency-groups]`节定义`dev`组。  
- 运行`uv run pytest`可直接执行测试，无需手动管理虚拟环境。

**关键点**：  
1. `dev`依赖组是`uv run`的特殊处理组，运行时会自动安装这些依赖，但不会包含在分发包中。  
2. `[build-system]`节或`[tool.uv] package = true`标记项目为“包”，确保`uv run`将当前目录以可编辑模式安装到虚拟环境。删除`[build-system]`会导致导入错误。  
3. 替代方案：使用`pip install . --group dev`在CI中安装依赖组。  

**优势**：  
- 项目更易协作：仅需`git clone`后运行`uv run pytest`即可测试，无需关心虚拟环境设置。  
- 打包简单：`uv build`一键生成分发包（.whl和.tar.gz文件），其中.tar.gz包含测试文件。  

此模式提升了开发效率，以datasette-extract项目为例展示了其便捷性。
