# TIL: timeout in Bash scripts | Heitor's log
- URL: https://heitorpb.github.io/bla/timeout/
- Added At: 2025-05-31 11:04:19

## TL;DR


本文总结了解决Bash脚本中`until curl`循环无限等待的问题。原脚本因服务器异常可能无限卡死，直接使用`timeout`无效，因为`until`是内置命令。解决方案包括：将循环嵌入子进程（如`timeout 1m bash -c "循环命令"`）或分离为独立脚本后调用，从而实现超时控制避免脚本僵死。

## Summary


本文介绍了在Bash脚本中使用`timeout`命令解决无限等待问题的方法：

1. **问题背景**：原脚本使用`until curl`循环等待Web服务器启动，但若服务器异常崩溃，会导致`sleep`无限循环，脚本卡死。

2. **超时工具`timeout`**：通过指定时间参数强制终止命令。例如`timeout 1s sleep 5`会在1秒后终止`sleep`进程，返回退出码124。默认发送`SIGTERM`信号，也可自定义信号（如`SIGKILL`）。

3. **直接结合失败**：`timeout until ...`无法生效，因为`until`是Bash内置命令，无法被外部信号终止。

4. **解决方案**：
   - **子进程包裹**：将`until`循环放在子Bash进程执行，如：
     `timeout 1m bash -c "until curl ...; do sleep 1; done"`
   - **脚本分离**：将循环逻辑写入单独脚本（如`until.sh`），再通过`timeout 1m ./until.sh`调用。

5. **总结**：尽管无法直接组合`timeout`和`until`，但通过子进程或独立脚本可实现超时控制，避免脚本无限挂起。
