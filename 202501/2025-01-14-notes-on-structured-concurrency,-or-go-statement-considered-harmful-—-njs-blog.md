# Notes on structured concurrency, or: Go statement considered harmful — njs blog
- URL: https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/
- Added At: 2025-01-14 14:33:53
- [Link To Text](2025-01-14-notes-on-structured-concurrency,-or-go-statement-considered-harmful-—-njs-blog_raw.md)

## TL;DR
文章总结了并发API的常见实现方式，介绍了Trio库的Nursery机制及其优势，讨论了`goto`语句的历史与问题，并类比了`go`语句的破坏性。Nursery机制通过结构化并发控制流，解决了`go`语句带来的问题，保留了函数抽象，支持自动资源清理和错误传播。未来，移除`go`语句有望提升并发编程的可靠性和可维护性。

## Summary
1. **并发API的常见实现方式**：
   - **线程/任务启动**：
     - Golang: `go myfunc()`
     - C (POSIX线程): `pthread_create(&thread_id, NULL, &myfunc)`
     - Erlang: `spawn(modulename, myfuncname, [])`
     - Python (线程): `threading.Thread(target=myfunc).start()`
     - Python (asyncio): `asyncio.create_task(myfunc())`
   - **回调机制**：
     - C++ (Qt): `QObject::connect(&emitter, SIGNAL(event()), &receiver, SLOT(myfunc()))`
     - C (GObject): `g_signal_connect(emitter, "event", myfunc, NULL)`
     - JavaScript: `document.getElementById("myid").onclick = myfunc`
     - JavaScript (Promises): `promise.then(myfunc, errorhandler)`
     - Python (Twisted): `deferred.addCallback(myfunc)`
     - Python (asyncio): `future.add_done_callback(myfunc)`

2. **Trio库的独特设计**：
   - **Nursery机制**：
     - 使用`async with trio.open_nursery() as nursery`创建nursery块。
     - 通过`nursery.start_soon(myfunc)`启动并发任务。
     - 所有任务必须在nursery块退出前完成，确保控制流的结构化。
   - **Nursery的优势**：
     - 保留函数抽象：函数返回时，所有任务已完成。
     - 支持动态任务生成：可以在nursery块内动态启动任务。
     - 自动资源清理：确保资源在任务完成后释放。
     - 自动错误传播：任务中的错误会自动传播到父任务。

3. **goto语句的历史与问题**：
   - **goto的起源**：
     - 早期编程语言（如FLOW-MATIC）使用`JUMP TO`或`goto`实现控制流。
     - 导致“面条代码”（spaghetti code），难以维护和理解。
   - **Dijkstra的贡献**：
     - 提出结构化编程，主张移除`goto`，使用`if/else`、循环和函数调用等结构化控制流。
     - 结构化控制流遵循“黑盒规则”，支持局部推理和抽象。
   - **goto的现代替代**：
     - 现代语言（如C、C#、Golang）仍保留`goto`，但限制其使用范围，禁止跨函数跳转。

4. **go语句的问题与类比**：
   - **go语句的破坏性**：
     - 破坏函数抽象：调用函数时无法确定是否启动了后台任务。
     - 破坏资源清理：后台任务可能导致资源在`with`块结束后仍被使用。
     - 破坏错误处理：后台任务的错误可能被忽略，缺乏自动传播机制。
   - **go语句与goto的类比**：
     - `go`语句类似于`goto`，导致控制流分裂，难以推理和维护。
     - 移除`go`语句可以启用新的语言特性（如自动资源清理和错误传播）。

5. **Nursery的实践与优势**：
   - **Nursery的设计目标**：
     - 替代`go`语句，提供结构化的并发控制流。
     - 确保所有任务在nursery块退出前完成，遵循“黑盒规则”。
   - **Nursery的具体实现**：
     - 使用`async with`语法创建nursery块。
     - 通过`nursery.start_soon`启动任务，任务在nursery块内执行。
     - nursery块退出前等待所有任务完成。
   - **Nursery的扩展性**：
     - 支持定义类似nursery的新类型。
     - 确保任务退出时自动清理资源和传播错误。

6. **结论**：
   - **Nursery的意义**：
     - 提供了一种结构化的并发控制流机制，解决了`go`语句带来的问题。
     - 保留了函数抽象，支持自动资源清理和错误传播。
   - **未来展望**：
     - 移除`go`语句可以启用更多语言特性，提升并发编程的可靠性和可维护性。
