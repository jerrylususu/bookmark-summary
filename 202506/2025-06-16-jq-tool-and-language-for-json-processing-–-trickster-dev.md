# jq: tool and language for JSON processing – Trickster Dev
- URL: https://www.trickster.dev/post/jq-tool-and-language-for-json-processing/
- Added At: 2025-06-16 14:54:54
- [Link To Text](2025-06-16-jq-tool-and-language-for-json-processing-–-trickster-dev_raw.md)

## TL;DR


JQ是专为Unix/Linux设计的JSON处理工具，支持命令行操作和图灵完备的DSL，可通过包管理器、Docker等方式安装。基础功能包括JSON解析、字段提取及数据生成；高级功能涵盖数学运算、函数式编程、条件循环及模块化扩展。常与脚本结合处理API数据，衍生工具包括Gojq和浏览器扩展，内核基于C语言并提供多语言接口，适用于数据解析与转换场景。

## Summary


* JQ是专为Unix/Linux环境设计的JSON处理工具，支持命令行操作和图灵完备的领域特定语言，用于解析、生成、修改和分析JSON数据。
* 安装方法：通过包管理器（如macOS Homebrew、Debian apt-get、Arch Linux pacman、FreeBSD pkg）、Docker（`docker pull ghcr.io/jqlang/jq:latest`）或直接下载二进制文件。在线Playground可访问https://jqplay.org/。
* 基础用法：
  * 美化输出：`echo '{"x":1}' | jq '.'`，压缩输出可通过`-c`参数。
  * 创建JSON对象/数组：使用`jq --null-input '{a: 1}'`生成对象、`[1,3,5]`生成数组。
  * 提取字段：通过`.`访问嵌套字段（如`.coord.y`）、数组索引（如`.coords[0].y`）和切片（`.[1:3]`提取范围索引）。
  * 选项操作符`?`：处理可能缺失的字段，避免程序崩溃。
* 高级功能：
  * 数学运算符：支持基本运算（`+`、`-`、`*`、`/`、`%`）及字符串重复（`"cyber" * 3`）。
  * 内置函数：如`length`计算长度，`map`和`select`实现函数式编程（替代Python的`map()`和`filter()`）。
  * 条件控制：使用`if-then-else`语句（示例给出FizzBuzz代码）。
  * 循环：通过`range`和`[]`迭代操作替代传统循环结构。
  * 模块化支持：可定义自定义函数模块（扩展名为.jq），参考标准库源码。
* 实际应用案例：
  * 结合Bash脚本和curl从Shopify商店API提取产品数据，生成CSV文件。示例脚本通过分页参数读取数据直至无新结果。
  * 使用Python包装库简化API数据提取（如`jq.compile().input().all()`方法提取标题字段）。
* 相关项目与扩展：
  * Go语言实现的Gojq支持独立库集成。
  * 工具jnv（终端JSON浏览器）和jqview（基于Go的GUI程序）助于原型开发。
  * Terraform工具tq支持用JQ处理对象。
* 技术细节：JQ内核基于C语言，但提供了跨语言接口，包括Python、Rust、Node.js和Perl的包装库，支持IEEE754浮点运算和复杂函数操作。
