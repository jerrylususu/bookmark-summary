# The surprising way to save memory with BytesIO
- URL: https://pythonspeed.com/articles/bytesio-reduce-memory-usage/
- Added At: 2025-01-31 08:47:05

## TL;DR
`BytesIO`是Python中用于内存中存储字节数据的类。使用`BytesIO.read()`会导致内存使用量翻倍，而`getbuffer()`和`getvalue()`方法则更高效，前者返回`memoryview`视图，后者返回`bytes`对象且不增加内存。建议避免使用`read()`，优先使用`getvalue()`或`getbuffer()`以最小化内存开销。

## Summary
1. **BytesIO简介**：
   - `BytesIO`是Python内置的`io`模块中的一个类，用于创建一个文件对象，该对象在内存中存储字节数据。
   - 示例代码展示了如何使用`BytesIO`写入和读取数据。

2. **BytesIO.read()的内存问题**：
   - 使用`BytesIO.read()`方法读取数据时，会在内存中创建一个新的数据副本，导致内存使用量翻倍。
   - 通过一个工具函数`report_allocated`，可以测量内存使用情况，验证了`read()`方法的内存开销。

3. **高效访问BytesIO数据的两种方法**：
   - **方法一：`BytesIO.getbuffer()`**：
     - 返回一个`memoryview`对象，该对象是对现有内存的视图，不会分配新的内存。
     - 示例代码展示了使用`getbuffer()`时内存使用量没有增加。
     - **`memoryview`的限制**：
       - 缺少一些`bytes`对象的方法，如`find()`。
       - 在Python 3.11之前，编译扩展中访问`memoryview`对象需要使用Python的缓冲区协议，这在某些项目中可能不可行。
       - 通过`bytes(data_view)`可以将`memoryview`转换为`bytes`，但这会复制数据并增加内存使用量。
   - **方法二：`BytesIO.getvalue()`**：
     - 返回`BytesIO`的内容作为一个`bytes`对象，但不会分配新的内存。
     - 示例代码展示了使用`getvalue()`时内存使用量没有增加。
     - **工作原理**：
       - `BytesIO`使用写时复制（copy-on-write）机制，只有在写入`BytesIO`时才会分配新的内存。
       - 示例代码展示了写入`BytesIO`时内存使用量的增加。

4. **总结与建议**：
   - 为了最小化从`BytesIO`提取数据时的内存使用：
     - 避免使用`BytesIO.read()`。
     - 如果需要`bytes`对象，使用`BytesIO.getvalue()`。
     - 如果可以接受`memoryview`，使用`BytesIO.getbuffer()`。

5. **实际应用案例**：
   - 提供了一个实际应用案例的链接，展示了从`read()`切换到`getvalue()`的实际效果。
