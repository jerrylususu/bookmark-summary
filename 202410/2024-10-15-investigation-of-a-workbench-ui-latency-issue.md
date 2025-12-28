# Investigation of a Workbench UI Latency Issue
- URL: https://netflixtechblog.com/investigation-of-a-workbench-ui-latency-issue-faa017b4653d
- Added At: 2024-10-15 15:03:18

## TL;DR
Netflix的Workbench产品中，JupyterLab UI因_jupyter-resource-usage_扩展的资源监控功能与不准确的CPU数量和虚拟内存使用相结合，导致延迟。通过禁用该扩展，解决了用户的问题。

## Summary
1. **概述**：
   - Netflix的数据平台部门提供了一个名为Workbench的产品，这是一个基于Titus的远程开发工作区，允许数据从业者处理大规模的数据和机器学习用例。
   - 最近，用户报告在运行某些Notebook时，JupyterLab UI变得缓慢且无响应。

2. **症状**：
   - 用户报告在运行某些Notebook时，JupyterLab UI变得缓慢且无响应。
   - 重启_ipykernel_进程可能会暂时缓解问题，但随着运行更多Notebook，问题仍然存在。

3. **量化延迟**：
   - 为了量化UI的延迟，开发了一种简单的方法：在JupyterLab中打开终端并按住一个键（如“j”）15秒，同时运行用户的Notebook。
   - 通过分析_.har_文件，观察到延迟范围从1到10秒，平均为7.4秒。

4. **初步调查**：
   - 怀疑特定Notebook中的代码有问题，特别是使用了_pystan_库，该库通过_nest_asyncio_注入到现有的_asyncio_事件循环中。
   - 尽管_pystan_的使用可能有问题，但用户报告即使在未使用_pystan_的Notebook中，UI也会变慢。

5. **排除网络问题**：
   - 怀疑网络可能是问题的原因，但通过捕获数据包发现，延迟主要发生在JupyterLab服务器端，而不是网络。

6. **最小化复现**：
   - 通过逐步简化“问题”Notebook，最终找到一个最小化的代码片段，可以在不依赖第三方库的情况下复现问题。
   - 该代码片段读取一个2GB的文件并启动多个进程，尽管这些进程只是休眠，但仍会导致JupyterLab UI延迟。

7. **深入分析**：
   - 使用_py-spy_对_jupyter-lab_进程进行分析，发现大部分CPU时间（89%）花在一个名为__parse_smaps_rollup的函数上。
   - 该函数是_jupyter_resource_usage_扩展的一部分，用于获取资源使用信息。

8. **根本原因**：
   - 该扩展定期调用_/metrics/v1_ API端点，获取所有子进程的内存使用信息。
   - 由于_os.cpu_count()返回的CPU数量不准确（96而不是64），导致创建了过多的子进程，增加了__parse_smaps_rollup函数的执行时间。
   - 读取2GB文件增加了虚拟内存的使用，进一步增加了_smaps_rollup文件的读取时间。

9. **解决方案**：
   - 用户确认禁用_jupyter-resource-usage_扩展可以满足其对UI响应性的需求，因此提供了一种禁用该扩展的方法。

10. **总结**：
    - 这是一个复杂的调试过程，涉及从UI到Linux内核的各个层面。
    - 问题的根本原因是扩展的资源监控功能与不准确的CPU数量和虚拟内存使用相结合，导致了UI的延迟。
    - 通过禁用相关扩展，解决了用户的问题。
