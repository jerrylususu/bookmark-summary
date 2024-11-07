# Parsing JSON is a Minefield
- URL: https://seriot.ch/projects/parsing_json.html
- Added At: 2024-11-07 14:59:17
- [Link To Text](2024-11-07-parsing-json-is-a-minefield_raw.md)

## TL;DR
文章《解析JSON是一场地雷战》详细探讨了JSON解析的复杂性，指出JSON规范分散且不精确，导致解析器行为不一致。通过300多个测试文件，文章展示了不同解析器在处理相同输入时的差异，强调了互操作性问题。作者还开发了STJSON解析器，并建议进一步研究JSON相关领域。

## Summary
1. **文章概述**：
   - 文章标题为《解析JSON是一场地雷战》，讨论了JSON解析的复杂性和潜在问题。
   - 文章发布于2016年10月26日，并在多个会议上进行了演示。
   - 文章详细介绍了JSON规范的演变、解析测试、测试架构、解析结果、解析内容、自定义JSON解析器STJSON以及结论和附录。

2. **JSON规范**：
   - JSON自2001年由Douglas Crockford提出，已成为Web和移动编程中数据序列化和交换的事实标准。
   - JSON规范分散在至少七个不同的文档中，包括json.org、RFC 4627、ECMAScript 262、ECMA 404、RFC 7158、RFC 7159和RFC 8259。
   - RFC 8259虽然澄清了一些问题，但仍有许多细节未明确指定，导致解析器行为不一致。

3. **解析测试**：
   - 作者创建了超过300个测试文件，涵盖结构、数字、数组、对象、字符串和RFC 8259的模糊之处。
   - 测试文件名以字母开头，表示预期结果（y表示成功解析，n表示解析错误，i表示实现定义）。
   - 测试包括标量、尾随逗号、注释、未闭合结构、嵌套结构、空白字符、NaN和Infinity、十六进制数字、范围和精度、指数表示法、数组、对象、字符串编码、字节顺序标记、控制字符、转义字符、无效转义字符和原始非Unicode字符。

4. **测试架构**：
   - 作者选择了多种JSON解析器（包括Swift、Objective-C、C、Python、Ruby、R、Lua、Perl、Bash和Rust）进行测试。
   - 使用Python脚本`run_tests.py`运行每个解析器并记录结果，生成HTML表格展示解析结果。

5. **解析测试结果**：
   - 结果显示，没有两个解析器表现出完全相同的行为，可能导致严重的互操作性问题。
   - 结果分为全结果、C解析器、Objective-C解析器、Apple (NS)JSONSerialization、Swift Freddy、Bash JSON.sh、其他解析器、JSON Checker和正则表达式。

6. **解析内容**：
   - 讨论了极端数值、重复键对象、字符串中的无效Unicode字符等情况下解析器的行为差异。
   - 结果表明，不同解析器在处理相同输入时可能产生不同的输出，导致互操作性问题。

7. **STJSON**：
   - 作者编写了一个名为STJSON的Swift 3 JSON解析器，旨在通过所有测试。
   - STJSON API简单，支持自定义参数，如最大解析深度和选项。

8. **结论**：
   - JSON不是一个可以盲目依赖的数据格式，规范分散且不精确，导致解析器行为不一致。
   - 作者建议继续研究更多解析器、JSON生成、JSON映射器、潜在的漏洞和其他序列化格式。

9. **附录**：
   - 提供了解析结果、转换结果、JSONTestSuite和STJSON的链接。

10. **致谢**：
    - 感谢@Reversity、@GEndignoux、@ccorsano、@BalestraPatrick和@iPlop的贡献。
