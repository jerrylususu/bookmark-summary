# Shedding old code with ecdysis: graceful restarts for Rust services at Cloudflare
- URL: https://blog.cloudflare.com/ecdysis-rust-graceful-restarts/
- Added At: 2026-02-13 15:22:19
- Tags: #read #network

## TL;DR
Cloudflare 开源 Rust 库 ecdysis，通过 fork-exec 模型和共享套接字实现服务零停机重启，已在生产环境使用五年，支撑全球 Rust 基础设施。

## Summary
Cloudflare 开源了其 Rust 库 **ecdysis**，用于实现服务的零停机优雅重启。该库已在 Cloudflare 生产环境中使用五年，支撑其全球 Rust 基础设施，每次重启可避免数百万次请求失败。

**核心问题与挑战**
传统服务重启（停止旧进程再启动新进程）会导致连接中断和新连接拒绝，对于高吞吐服务影响巨大。使用 `SO_REUSEPORT` 虽允许多进程绑定同一端口，但会导致连接在进程退出时被内核终止，无法实现真正的优雅重启。

**ecdysis 的解决方案**
ecdysis 采用类似 NGINX 的 **fork-exec 模型**：
1.  **父进程 fork 子进程**：子进程通过 `execve` 替换为新版本代码。
2.  **共享监听套接字**：通过命名管道将监听套接字的文件描述符从父进程传递给子进程，两者共享内核数据结构。
3.  **平滑过渡**：子进程初始化期间，父进程继续处理连接。子进程就绪后通知父进程，父进程关闭其套接字副本并开始排空（drain）现有连接，子进程开始接受新连接。
4.  **崩溃安全**：若子进程初始化失败退出，父进程仍在监听，服务不受影响。

**关键特性与集成**
*   **异步支持**：原生支持 Tokio，也支持同步服务。
*   **systemd 集成**：支持 `systemd-notify` 和 `systemd` 命名套接字。
*   **平台限制**：依赖 Unix 系统调用，不支持 Windows。
*   **安全设计**：遵循 fork-then-exec 模式，确保子进程环境干净；仅显式传递套接字和通信管道；兼容 seccomp 过滤器（需允许 fork/exec）。

**生产与对比**
*   **生产规模**：自 2021 年起在 Cloudflare 全球 330+ 数据中心运行，处理数十亿日请求。
*   **替代方案**：
    *   **tableflip**：Cloudflare 的 Go 语言优雅重启库。
    *   **shellflip**：Cloudflare 的另一 Rust 库，更适用于复杂有状态服务（如 Oxy 代理），支持应用状态传递，但开销较大。

**总结**
ecdysis 为 Rust 网络服务提供了生产级的优雅重启能力，通过共享套接字和 fork-exec 模型实现零停机升级，适用于高性能代理、长连接 API 服务器等对可用性要求高的场景。
