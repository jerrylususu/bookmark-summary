# Why is hash(-1) == hash(-2) in Python?
- URL: https://omairmajid.com/posts/2021-07-16-why-is-hash-in-python/
- Added At: 2025-01-08 15:26:34
- [Link To Text](2025-01-08-why-is-hash(-1)-==-hash(-2)-in-python_raw.md)

## TL;DR
作者在Reddit上发现Python中`hash(-1)`和`hash(-2)`都返回`-2`的现象，通过查看Python源码发现`-1`被用作错误标志，因此哈希函数返回`-2`以避免冲突。文章强调了阅读源码的重要性，并鼓励通过源码解决问题。

## Summary
1. **问题发现**：
   - 在Reddit上发现一个问题：`hash(-1) == hash(-2)`在Python中是否为彩蛋？
   - 通过Python解释器验证，发现`hash(-1)`和`hash(-2)`确实都返回`-2`。

2. **初步探索**：
   - 检查其他常见整数的哈希值，发现大多数小整数的哈希值等于其自身，但`-1`例外。
   - 决定通过查看Python源码来寻找答案。

3. **源码获取**：
   - 通过Google搜索“python implementation”，找到CPython的官方GitHub仓库。
   - 使用`git clone`命令获取CPython源码，并限制历史记录以加快克隆速度。

4. **源码分析**：
   - 通过`help(hash)`查看`hash`函数的文档，确定其实现位于`Python/bltinmodule.c`文件中。
   - 发现`hash`函数的核心逻辑是调用`PyObject_Hash`，并将结果转换为`PyLongObject`。
   - 注意到`-1`被用作错误标志，因此哈希函数不会返回`-1`。

5. **深入挖掘**：
   - 查找`PyObject_Hash`的实现，发现其位于`Objects/object.c`文件中。
   - 进一步发现`PyLongObject`的`tp_hash`函数是`long_hash`，位于`Objects/longobject.c`文件中。
   - 在`long_hash`函数中，发现当哈希值为`-1`时，会显式将其转换为`-2`。

6. **验证答案**：
   - 通过Reddit上的回答确认了作者的发现，即`-1`被用作错误标志，因此哈希函数返回`-2`以避免冲突。

7. **总结**：
   - 通过阅读源码，作者成功解答了`hash(-1) == hash(-2)`的原因。
   - 强调了阅读源码的重要性，并鼓励其他人也尝试通过源码解决问题。

8. **关键点**：
   - **错误标志**：`-1`被用作错误标志，因此哈希函数不会返回`-1`。
   - **源码阅读**：通过阅读源码，可以深入理解语言内部的实现细节。
   - **社区验证**：通过社区中的回答验证了自己的发现，确保答案的准确性。
