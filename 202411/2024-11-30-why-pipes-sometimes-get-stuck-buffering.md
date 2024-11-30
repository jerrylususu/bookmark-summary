# Why pipes sometimes get "stuck": buffering
- URL: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/
- Added At: 2024-11-30 04:45:36
- [Link To Text](2024-11-30-why-pipes-sometimes-get-stuck-buffering_raw.md)

## TL;DR
文章讨论了终端命令管道输出卡住的问题，主要原因是程序的缓冲机制。通过分析缓冲行为和编程语言中的缓冲控制，提出了多种解决方案，如使用`grep --line-buffered`、`stdbuf -o0`等，并建议引入标准环境变量来禁用缓冲。

## Summary
1. **问题描述**：
   - 作者多年来遇到一个终端问题，即在使用管道命令时，输出有时会“卡住”，无法显示。
   - 示例命令：`tail -f /some/log/file | grep thing1 | grep thing2`，在日志文件更新较慢时，无输出显示。

2. **原因分析**：
   - **缓冲机制**：程序在写入管道或文件前通常会缓冲输出，以提高性能。
   - **缓冲大小**：通常缓冲至8KB或程序退出时才写入，导致慢速输入时数据可能永远不会被写入。
   - **终端与非终端输出**：`grep`等程序在写入终端时使用行缓冲，而在写入管道时使用块缓冲。

3. **缓冲行为**：
   - **不缓冲的命令**：如`tail`、`cat`、`tee`。
   - **缓冲的命令**：如`grep`（使用`--line-buffered`）、`sed`（使用`-u`）、`awk`（使用`fflush()`）等。

4. **编程语言中的缓冲**：
   - **C语言**：使用`setvbuf`禁用缓冲。
   - **Python**：使用`python -u`或`PYTHON_UNBUFFERED=1`等方法。
   - **Ruby**：使用`STDOUT.sync = true`。
   - **Perl**：使用`$| = 1`。

5. **Ctrl-C中断的影响**：
   - 按下`Ctrl-C`时，缓冲区内容丢失，无法看到未写入的输出。
   - 解决方法：找到程序PID并发送`TERM`信号，使程序在退出前刷新缓冲区。

6. **文件重定向的缓冲**：
   - 重定向到文件时也会缓冲，但`Ctrl-C`不会导致缓冲区内容丢失。

7. **解决方案**：
   - **快速完成程序**：如使用`cat`替代`tail -f`。
   - **使用grep的行缓冲标志**：`grep --line-buffered`。
   - **使用awk重写命令**：如`awk '/thing1/ && /thing2/'`。
   - **使用stdbuf**：`stdbuf -o0`禁用libc缓冲。
   - **使用unbuffer**：强制程序输出为TTY，减少缓冲。

8. **环境变量建议**：
   - 建议引入标准环境变量如`NO_BUFFER`来禁用缓冲。

9. **未讨论内容**：
   - 行缓冲与完全无缓冲的区别。
   - stderr与stdout缓冲的不同。
   - 操作系统TTY驱动的缓冲。
   - 其他需要刷新输出的场景。
