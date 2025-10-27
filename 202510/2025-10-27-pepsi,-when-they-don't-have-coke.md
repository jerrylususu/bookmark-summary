# Pepsi, when they don't have coke
- URL: https://www.bitecode.dev/p/pepsi-when-they-dont-have-coke
- Added At: 2025-10-27 14:56:03
- [Link To Text](2025-10-27-pepsi,-when-they-don't-have-coke_raw.md)

## TL;DR
文章分析了配置管理现状，认为现有工具如Toml、JSON、YAML在大型配置中不足。作者探讨了Cuelang和Starlark等替代方案，但认为其复杂度高、绑定有限。最终选择Python作为折中方案，虽无沙盒保护，但更实用灵活，适合多数场景。

## Summary
这篇文章探讨了配置管理的现状及不同配置语言的优劣。作者指出，对于小型配置，现有工具如Toml、Pydantic和argparse已足够，但大型配置文件需要逻辑生成和分文件管理时，现有方案变得复杂且不足。

- **常见配置格式的缺点**：Toml不擅长嵌套结构，JSON缺乏注释和导入功能，YAML被认为是最差的选项，因为它们都缺乏DRY（Don't Repeat Yourself）特性，如导入和函数支持。
- **替代方案**：作者提到Cuelang（简称Cue）作为一种优秀的配置语言，支持强类型、DRY特性和沙盒环境，但缺点是仅支持Go语言绑定，在Python环境中使用需通过子进程调用，不适用于企业环境。
- **Starlark的探索**：出于无奈，作者尝试了Starlark（一种源自Bazel的Python风格语言）。它支持沙盒执行、基本数据类型和函数，但语法与Python差异大，且默认无导入功能。通过Python绑定（基于Rust实现），可以控制沙盒访问权限，但需要自定义导入逻辑，使用复杂。
- **结论**：尽管Starlark灵活，但作为配置语言，它需要额外工作（如集成Pydantic验证），不如直接使用Python编写配置。作者最终选择Python作为折中方案，认为它虽不完美（如无沙盒保护），但比替代方案更实用。Starlark可能适用于需要自定义DSL的不可信第三方场景。整体上，配置管理问题仍未完美解决。
