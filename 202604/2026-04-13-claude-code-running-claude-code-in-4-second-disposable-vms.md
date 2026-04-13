# Claude Code Running Claude Code in 4-Second Disposable VMs
- URL: https://jonno.nz/posts/claude-code-running-claude-code-in-4-second-disposable-vms/
- Added At: 2026-04-13 13:24:23
- Tags: #read #agent #deepdive

## TL;DR
本文介绍作者为Claude Code构建的Firecracker微虚拟机隔离执行环境，通过硬件级隔离解决Docker容器的安全风险，支持快速启动、完全隔离、资源可控及vsock通信，采用Go语言实现主机协调器与VM代理，支持CLI、API和MCP服务器，实现自动化任务流程。

## Summary
本文介绍了作者为Claude Code构建的一个隔离执行环境系统，旨在解决在Docker容器中以高权限运行AI代理的安全问题。作者认为容器共享主机内核，存在逃逸风险，因此选择了更安全的Firecracker微虚拟机（MicroVM），实现硬件级隔离。

系统核心特点：
- **快速启动**：Firecracker VM在约4秒内启动，适用于20-120秒的任务，4秒开销可接受。
- **完全隔离**：每个VM拥有独立内核、内存和硬件强制隔离，即使内核漏洞也无法影响主机。
- **资源使用**：默认分配2GB RAM，主机可并发运行12-13个VM；使用稀疏拷贝的4GB根文件系统镜像，磁盘开销可控。
- **通信机制**：采用vsock（AF_VSOCK）实现主机与VM间无网络通信，避免SSH的密钥管理和端口问题，通过Unix域套接字直接交互。
- **系统架构**：由两个Go二进制文件组成——主机端的协调器（14MB，嵌入React仪表板）和VM内的代理（2.5MB静态二进制），共享协议定义文件。
- **任务流程**：从提示开始，自动创建VM、注入配置、运行Claude Code、流式输出、收集文件并销毁VM，全程无需人工干预。
- **使用方式**：支持CLI、REST API（带Web仪表板）和MCP服务器，允许Claude Code在其他机器上委托任务。

作者选择Go语言因其静态二进制、并发支持（goroutines）、原生系统调用和快速编译，适合构建轻量级代理和协调器。

后续文章将深入探讨实现细节，包括根文件系统构建、网络配置（如iptables调试）、代理和流式管道。
