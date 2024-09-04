# Greppability is an underrated code metric
- URL: https://morizbuesing.com/blog/greppability-code-metric/
- Added At: 2024-09-04 14:19:02
- [Link To Text](2024-09-04-greppability-is-an-underrated-code-metric_raw.md)

## TL;DR
文章强调了代码可搜索性的重要性，提出了避免拆分标识符、在整个堆栈中使用相同名称和扁平化结构的规则，以提高代码的可维护性和安全性。

## Summary
1. **代码可搜索性的重要性**：
   - 在维护不熟悉的代码库时，花费大量时间搜索代码中的字符串，如函数名、错误消息、类名等。
   - 如果无法找到所需内容，可能导致挫败感或危险情况，如误认为某些代码不再需要。

2. **保持代码可搜索的规则**：
   - **避免拆分标识符**：
     - 动态构造标识符会导致问题，如动态生成数据库表名或列名，使搜索变得困难。
     - 示例：动态生成表名 `shipping_addresses` 和 `billing_addresses`，导致难以搜索。
     - 重构为直接返回表名，提高可搜索性。
   - **在整个堆栈中使用相同名称**：
     - 避免在应用边界重命名字段以匹配命名方案，如将 `snake_case` 转换为 `camelCase`，导致需要搜索多个字符串。
     - 示例：直接返回对象，避免转换，提高搜索效率。

3. **扁平化优于嵌套**：
   - 从 [Zen of Python](https://peps.python.org/pep-0020/) 中获得灵感，扁平化命名空间和对象结构通常更好。
   - 示例：选择扁平化的翻译文件结构，便于搜索键名。
   - 示例：React 组件结构中，扁平化路径如 `./components/AttributeFilterCombobox.tsx` 优于嵌套路径，便于搜索整个命名空间组件。

4. **总结**：
   - 代码的可搜索性是一个被低估的代码指标，通过避免拆分标识符、使用相同名称和扁平化结构，可以提高代码的可维护性和安全性。
