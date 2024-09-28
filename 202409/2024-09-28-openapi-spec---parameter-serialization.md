# OpenAPI Spec - Parameter Serialization
- URL: https://docs.bump.sh/guides/openapi/specification/v3.1/understanding-structure/parameter-serialization/
- Added At: 2024-09-28 11:45:48
- [Link To Text](2024-09-28-openapi-spec---parameter-serialization_raw.md)

## TL;DR
文章详细介绍了API参数序列化的定义、关键字（如Explode和Style）及其在不同位置（路径、查询、头部、Cookie）的应用方式。通过示例展示了如何处理不同类型的参数，并强调了选择合适风格和位置的重要性。

## Summary
1. **参数序列化概述**：参数序列化定义了API接受的输入格式，即参数如何被序列化。

2. **关键字**：
   - **Explode**：定义参数是否应分解为逻辑组件。
     - `true`：多值参数将被序列化为每个值作为单独的参数。
     - `false`：参数作为单个参数，无论有多少值。
     - 默认值取决于`style`。
   - **Style**：定义API期望的参数序列化方式。
     - `in:path`：默认`simple`，可选`label`或`matrix`。
     - `in:query`：默认`form`，可选`spaceDelimited`、`pipeDelimited`或`deepObject`。
     - `in:header`：默认`simple`。
     - `in:cookie`：默认`form`。

3. **路径参数**：
   - **Simple**：默认`explode:false`，多值数组用逗号分隔，对象键值对用逗号连接。
   - **Label**：所有参数前缀为“.”，多值数组用点分隔，对象键值对用点连接。
   - **Matrix**：所有参数前缀为“;”，多值数组每个值前缀为“;参数名=”，对象键值对用分号分隔。

4. **查询参数**：
   - **Form**：默认`explode:true`，多值数组用“&”分隔，对象键值对用“&”连接。
   - **Space Delimited**：多值数组用空格分隔，对象键值对用空格连接。
   - **Pipe Delimited**：多值数组用管道分隔，对象键值对用管道连接。
   - **Deep Object**：仅在`explode:true`时定义，对象键值对用方括号表示。

5. **头部参数**：
   - 仅支持`simple`风格，不推荐依赖`style`、`explode`和`schema`，建议使用`content`字段。

6. **Cookie参数**：
   - 仅支持`form`风格，不推荐依赖`style`、`explode`和`schema`，建议使用`content`字段。

7. **示例与推荐**：
   - **通用指南**：
     - **Location**：根据参数的通用性和敏感性选择`in:header`或`in:cookie`，特定路径参数选择`in:path`或`in:query`。
     - **Style**：默认风格通常是最简单和最通用的选择。
   - **可选布尔值**：示例展示了如何在查询参数中使用可选布尔值。
   - **必填字符串**：示例展示了如何在路径参数中使用必填字符串。
   - **字符串列表**：示例展示了如何在查询参数中使用字符串列表。
   - **对象或字符串**：示例展示了如何使用`deepObject`风格处理对象或字符串参数。

8. **总结**：参数序列化是API设计中的关键部分，选择合适的风格和位置可以简化API的使用和实现。
