# When to use std::string_view
- URL: https://learnmoderncpp.com/2024/10/29/when-to-use-stdstring_view/
- Added At: 2024-10-29 14:20:02
- [Link To Text](2024-10-29-when-to-use-std-string_view_raw.md)

## TL;DR
`std::string_view` 是C++17引入的轻量级字符串视图类，适用于廉价传递多种字符串类型。它通过指针和长度实现，支持多种创建方式，但需注意其数据不保证以空字节结尾。在性能上，`std::string_view` 适用于参数类型多样的情况，而在参数多为 `std::string` 左值时，`const std::string&` 更优。

## Summary
1. **概述**：
   - `std::string_view` 是C++17引入的标准库类，被宣传为一种轻量级、非拥有的类似字符串实体，可以廉价地作为函数参数传递。
   - 本文探讨了 `std::string_view` 的最佳实践使用场景，以及在哪些情况下使用它既不必要也无益。

2. **创建方式**：
   - `std::string_view` 可以从C风格字符串、`std::string`（隐式转换）、另一个 `std::string_view` 或一对迭代器创建。
   - 示例代码展示了如何从不同来源创建 `std::string_view` 并传递给函数。

3. **实现细节**：
   - `std::string_view` 通常实现为一个指针和一个长度，在64位机器上占用16字节，最佳传递方式是按值传递。
   - 可以通过成员函数 `data()` 访问字符串数据，通过 `size()` 或 `length()` 获取长度。

4. **注意事项**：
   - `data()` 返回的 `const char*` 指针不保证以空字节结尾，没有 `c_str()` 成员函数。
   - 从字面量或整个 `std::string` 创建的 `std::string_view` 通常以空字节结尾。

5. **隐式转换**：
   - 表格展示了不同字符串类型之间的隐式转换关系。
   - `std::string` 可以转换为 `std::string_view`，但反之不行。
   - 从C风格字符串字面量构造 `const std::string&` 或 `std::string&&` 不一定廉价。

6. **性能考量**：
   - 如果参数可以是 `std::string` 以外的类型，使用 `std::string_view` 可能对性能有益。
   - 如果参数总是 `std::string` 左值，使用 `std::string_view` 没有性能优势，应优先使用 `const std::string&`。
   - 在多层函数调用中传递值时，保持 `const std::string&` 可能提高性能。

7. **功能特性**：
   - `std::string_view` 包含 `begins_with()`、`ends_with()`、`substr()`、`compare()`、`contains()` 和 `find()` 等成员函数。
   - 还包含 `remove_prefix()` 和 `remove_suffix()`，可以从头或尾缩小对象。
   - 缺乏功能通常不是不使用 `std::string_view` 的原因。

8. **总结**：
   - `std::string_view` 的主要优点是可以廉价地按值传递给接受多种标准字符串类型的函数。
   - 但在参数几乎总是 `std::string` 左值的情况下，使用 `const std::string&` 更优。
