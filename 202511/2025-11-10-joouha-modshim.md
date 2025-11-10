# joouha/modshim
- URL: https://github.com/joouha/modshim
- Added At: 2025-11-10 13:42:20
- Tags: #py #tools
- [Link To Text](2025-11-10-joouha-modshim_raw.md)

## TL;DR
Modshim 是为Python模块提供轻量级增强的框架，无需修改原始代码。通过创建隔离的合并模块，它能修复bug、添加功能，相比猴子补丁或代码分叉更安全和易维护。

## Summary
modshim 是一个 Python 库，用于在不修改源代码的情况下增强现有模块的功能，可作为 forking、vendoring 和 monkey-patching 的替代方案。

**核心特性：**
- 创建一个"shimmed"新模块，将原始模块与自定义增强功能结合，保持原始模块不变。
- 适用于修复第三方库 bug、修改函数行为、添加新功能或隔离测试等场景。

**使用方法：**
- 安装：通过 `pip install modshim` 安装。
- 基本流程：创建自定义模块（如子类化原始类），使用 `shim()` 函数将自定义模块（upper）与原始模块（lower）合并到新挂载点（mount）。
- 示例：增强 `textwrap` 模块，为 `TextWrapper` 添加 `prefix` 参数。通过 `shim()` 生成合并模块 `super_textwrap`，使用新功能时需从该模块导入，原始模块不受影响。
- 创建增强包：可在包内调用 `shim()`，使导入包时自动应用增强（如创建 `requests_extra` 包为 `requests` 添加自动重试功能）。

**高级功能：**
- AST 重写：自动重定向模块内部引用，确保增强类（如 `Session`）被顶级函数（如 `requests.get()`）使用。
- 线程安全，支持子模块递归处理和字节码缓存。

**优势对比：**
- **vs Monkey-Patching**：避免全局污染（原始模块不变）、更稳定（不依赖运行时修改）、代码更清晰（增强功能通过显式导入使用）。
- **vs Forking**：减少维护负担（直接依赖官方库，无需合并更新）、避免代码分歧、便于贡献上游。
- **vs Vendoring**：无需复制依赖代码、易于更新原始库、增强代码更易维护和测试。

**工作原理：**
- 通过自定义导入查找器（`ModShimFinder`）拦截导入系统。
- 合并时先执行原始模块代码，再执行增强模块代码以覆盖或扩展属性。
- AST 转换确保内部引用指向合并后的模块，保持一致性。

总之，modshim 提供了一种隔离、可维护的方式增强 Python 模块，适用于需要定制第三方库而不影响原始功能的场景。
