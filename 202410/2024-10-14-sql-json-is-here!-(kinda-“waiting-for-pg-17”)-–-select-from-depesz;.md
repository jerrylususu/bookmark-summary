# SQL/JSON is here! (kinda “Waiting for Pg 17”) – select * from depesz;
- URL: https://www.depesz.com/2024/10/11/sql-json-is-here-kinda-waiting-for-pg-17/
- Added At: 2024-10-14 14:41:29
- [Link To Text](2024-10-14-sql-json-is-here!-(kinda-“waiting-for-pg-17”)-–-select-from-depesz;_raw.md)

## TL;DR
PostgreSQL通过SQL/JSON标准新增了处理JSON数据的功能，包括构造器、测试函数和查询函数，增强了处理复杂数据结构的能力。

## Summary
1. **SQL/JSON简介**：
   - SQL/JSON是一个标准，由非PostgreSQL专属的组织制定，意味着该标准最终可能在其他数据库中实现。
   - PostgreSQL已经支持部分SQL/JSON特性，如JSON数据类型和JSON PATH表达式，但现在有了更多新功能。

2. **现有功能**：
   - 之前支持JSON和JSONB数据类型，以及一些函数和操作符（包括使用JSONPATH数据类型的操作符）。
   - 这些功能不会消失，但会新增更多功能，其中一些是对已有功能的补充，另一些则是全新的。

3. **新功能概览**：
   - **构造器**：
     - JSON()：将输入转换为JSON类型，支持文本、字节数组、JSON和JSONB类型，否则会报错。
     - JSON_SCALAR()：生成正确引用的JSON标量值，数字和布尔值不加引号，其他类型加引号。
     - JSON_SERIALIZE()：将SQL/JSON表达式转换为字符或二进制字符串。
     - JSON_ARRAY()：创建JSON数组，支持列表和查询两种模式，可处理NULL值。
     - JSON_ARRAYAGG()：聚合函数，生成JSON数组。
     - JSON_OBJECT()：创建JSON对象，支持键值对，可处理重复键。
     - JSON_OBJECTAGG()：聚合函数，生成JSON对象。

4. **测试函数**：
   - 提供一系列表达式，如IS (NOT)? JSON _TYPE_，用于测试给定值是否为有效的JSON类型。

5. **查询函数**：
   - **JSON_EXISTS**：测试给定的JSON路径表达式是否存在。
   - **JSON_QUERY**：应用JSON路径表达式并返回结果，支持多种选项如返回类型、包装器、引号处理和错误处理。
   - **JSON_VALUE**：类似于JSON_QUERY，但只能返回单个标量值，默认返回类型为TEXT。
   - **JSON_TABLE**：将JSON数据转换为表格形式，支持嵌套结构和多种选项。

6. **总结**：
   - SQL/JSON标准为PostgreSQL带来了更多处理JSON数据的功能，包括构造器、测试函数和查询函数，增强了数据库处理复杂数据结构的能力。
