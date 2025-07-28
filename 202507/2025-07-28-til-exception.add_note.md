# TIL: Exception.add_note
- URL: https://daniel.feldroy.com/posts/til-2025-05-exception-add_note
- Added At: 2025-07-28 14:08:34
- [Link To Text](2025-07-28-til-exception.add_note_raw.md)

## TL;DR


Python 3.11新增`Exception.add_note`方法，允许通过`e.add_note("注释")`在捕获异常时追加字符串说明。注释存储在`__notes__`列表中，抛出异常时会显示在原始错误信息下方。该方法继承自`BaseException`基类，适用于所有异常类型，便于扩展调试细节。

## Summary


Python 3.11新增`Exception.add_note`方法，允许在异常中添加补充信息。通过捕获异常后调用`e.add_note("注释内容")`可追加说明文本，最终抛出异常时，注释会显示在原始异常信息下方。例如引发`ZeroDivisionError`时添加三条注释，输出会依次显示所有注释内容。注释内容必须为字符串，存储于`__notes__`属性列表中。该方法属于`BaseException`基类，适用于所有Python异常类型，提供清晰扩展异常信息的方式。
