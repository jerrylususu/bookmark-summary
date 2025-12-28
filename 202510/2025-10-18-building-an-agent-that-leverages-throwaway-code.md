# Building an Agent That Leverages Throwaway Code
- URL: https://lucumr.pocoo.org/2025/10/17/code/
- Added At: 2025-10-18 13:59:05

## TL;DR
本文介绍利用Pyodide（WebAssembly版Python）构建智能体的方法，通过写入临时代码解决复杂任务。虚拟文件系统实现安全资源交互；持久化执行确保任务可恢复。此方法简单高效，已有类似应用实践。

## Summary
本文探讨了构建能利用“一次性代码”的智能体的方法。核心观点是，代理擅长编写代码，因此可让其编写临时代码来解决非编码问题，这比想象中更简单。

### 关键组件
1. **Pyodide 作为核心运行时**  
   - Pyodide 是通过 WebAssembly 运行的 Python 解释器，支持从 PyPI 安装依赖，并提供类 Unix 环境。  
   - 它易于在 Node.js 环境中部署（可通过 npm 安装），且能通过虚拟文件系统与外部交互。  
   - 建议将 Pyodide 运行在 Web Worker 中以支持中断控制，并利用 Python 丰富的库生态（如处理 PDF、图像等）。

2. **文件系统的核心作用**  
   - 虚拟文件系统是连接代理与外部资源的安全桥梁。通过拦截文件操作，可将特定路径（如 `/network/`）映射到后端 API，实现受控的资源访问（如只读或写入）。  
   - 由于 emscripten 文件系统是同步的，而实际操作（如网络请求）是异步的，作者通过共享内存（`Atomics.wait`）和 Web Worker 实现了同步封装，并提供伪代码示例。

3. **持久化执行的支持**  
   - 为确保长时间运行的代理任务可恢复，需实现持久化执行。作者提出一种简单方法：将任务分解为多步，每步状态缓存至数据库（如 Redis），通过任务 ID 和步数作为键值。若任务中断，可从缓存恢复状态继续执行。

### 扩展工具与实例
- **非代码工具**：除文件系统外，可集成其他工具（如 Cloudflare 提出的 MCP 服务器），或自定义工具（如 `Describe` 用于文件内容推断、`Help` 提供文档查询）。  
- **完整示例**：作者开源了一个迷你代理项目（[mitsuhiko/mini-agent](https://github.com/mitsuhiko/mini-agent)），演示了代理如何通过文件系统获取 IP 地址并用 Python 生成图像。示例包含分步执行、错误处理及状态缓存。

### 行业实践
- Anthropic 的 Claude Skills 和 Cloudflare 的 Code Mode 均采用了类似思路，即让代理在沙盒中生成代码来操作工具或处理文档。

总结：通过结合 Pyodide、虚拟文件系统和持久化执行，可高效构建基于一次性代码的代理，降低开发复杂度，并利用现有生态实现强大功能。
