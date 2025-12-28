# Python Practical Package Packing 2024
- URL: https://matt.sh/python-project-structure-2024
- Added At: 2024-07-23 14:10:07

## TL;DR
现代Python项目应使用`pyproject.toml`和Poetry管理依赖和环境，避免过时的工具如`requirements.txt`和`setup.py`，推荐使用Poetry进行依赖解析和虚拟环境管理，以及使用`@dataclass`和标准代码格式化工具提高代码质量。

## Summary
1. **项目结构要求**：
   - **必须使用** `pyproject.toml` 文件来声明所有本地包的方面。
   - **每个单一用途的仓库** 应只有一个 `pyproject.toml` 文件在顶层。
   - **所有Python包代码** 应放在一个以包名命名的目录中。
   - **目录结构示例**：
     - `project_name/`
       - `pyproject.toml`
       - `project_name/__init__.py`

2. **依赖管理**：
   - **避免使用** `requirements.txt` 或 `setup.py / setup.cfg`，这些方法已过时。
   - **推荐使用** `pyproject.toml` 来定义依赖，更可靠且定义更清晰。
   - **最佳工具** 是 [Poetry](https://github.com/python-poetry/poetry)，它提供版本依赖解析、自动虚拟环境管理、包构建/上传和命令运行等功能。

3. **最佳实践**：
   - **使用Poetry的`init`向导** 来创建默认设置。
   - **添加初始依赖** 时，依赖管理器会自动高效地拉取依赖并生成哈希锁文件。
   - **查看依赖树** 对于大型项目尤其有用，特别是在处理安全警报时。

4. **虚拟环境管理**：
   - **避免手动创建和管理虚拟环境**，应由依赖/包管理器自动控制。
   - **不应生成** `requirements.txt` 文件，所有包和项目应在Poetry管理的虚拟环境中管理。

5. **脚本入口点管理**：
   - **使用Poetry** 自动生成全局Python命令，从简单的 `package.module:function` 声明。
   - **示例**：
     - 创建 `hello/entrypoint.py` 文件。
     - 更新 `pyproject.toml` 文件以指定命令入口点。
     - 运行示例以验证功能。

6. **代码结构和工具使用**：
   - **避免** 手动设置 `PYTHONPATH`，应使用 `pyproject.toml` 和 Poetry 管理依赖和环境。
   - **推荐使用** `fire.Fire` 或 `jsonargparse` 来生成CLI接口。
   - **使用 `@dataclass`** 来定义类，避免手动编写 `__init__` 方法。
   - **推荐使用** `loguru` 替代内置的 `logging` 模块。
   - **使用标准代码格式化工具**，如 `black`, `ufmt`, `ruff format`。

7. **常见错误**：
   - **使用过时的工具和方法**，如 `requirements.txt`, `setup.py`, `setup.cfg`, `argparse`, `click`, `os.path`, `logging` 等。
   - **手动配置虚拟环境** 和 `PYTHONPATH`。
   - **不使用 `@dataclass`** 和标准代码格式化工具。
   - **使用过时的Python版本**，应使用Python 3.11+ 或 3.12+。

8. **总结**：
   - **现代Python项目** 应使用 `pyproject.toml` 和 Poetry 来管理依赖和环境。
   - **避免过时的工具和方法**，使用推荐的工具和最佳实践来提高项目的可维护性和效率。
