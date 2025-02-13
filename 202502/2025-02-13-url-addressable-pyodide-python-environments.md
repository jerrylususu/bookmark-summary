# URL-addressable Pyodide Python environments
- URL: https://simonwillison.net/2025/Feb/13/url-addressable-python/
- Added At: 2025-02-13 14:17:33
- [Link To Text](2025-02-13-url-addressable-pyodide-python-environments_raw.md)

## TL;DR
作者在使用Datasette Lite时发现并修复了一个Bug，展示了URL可寻址的Python环境的优势。文章详细描述了Datasette Lite的功能、插件支持及修复Bug的过程，强调了WebAssembly在复现和保存Bug方面的潜力。

## Summary
1. **发现问题**：
   - 作者在使用Datasette Lite时发现了一个不明显的Bug，并认为这是展示URL可寻址的Python环境（由Pyodide和WebAssembly驱动）的绝佳机会。

2. **相关URL**：
   - 作者提供了发现Bug的页面URL，并解释了URL中的各个组件。

3. **Datasette Lite**：
   - Datasette Lite是Datasette的浏览器版本，完全在浏览器中运行，基于Pyodide。
   - 作者最初将其作为周末项目构建，后来添加了许多功能，如通过URL加载SQLite、CSV、JSON或Parquet文件。
   - 作者认为Datasette Lite的浏览器版本非常实用，尤其是在不需要安装任何其他软件的情况下。

4. **Datasette 1.0 alphas**：
   - 作者发布了多个Datasette 1.0的alpha版本，并将其发布到PyPI上。
   - Datasette Lite可以通过URL参数加载特定版本的Datasette，使用Pyodide的micropip机制从PyPI安装所需包。

5. **插件支持**：
   - Datasette Lite支持通过URL安装插件，使用`?install=`参数指定需要安装的插件。
   - 并非所有插件都能在Pyodide中工作，特别是那些依赖编译二进制文件或运行自定义JavaScript的插件。

6. **datasette-visible-internal-db插件**：
   - 该插件允许在Datasette UI中浏览Datasette的内部数据库，主要用于调试和开发。

7. **发现Bug**：
   - 作者在尝试使用`datasette-visible-internal-db`插件时，发现了一个404错误，原因是内部数据库表的名称已更改，但外键引用未更新。

8. **修复Bug**：
   - 作者通过更新外键引用并添加自动化测试来修复了该Bug。

9. **URL可寻址的复现步骤**：
   - 作者强调了URL可寻址的复现步骤在修复Bug中的重要性，并认为Datasette Lite的模式可以为其他项目提供参考。
   - WebAssembly的持久性和稳定性使其成为未来长期保存和复现Bug的理想选择。
