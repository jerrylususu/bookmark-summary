# smol machines — the same smol machine on your laptop, in the cloud, or self-hosted
- URL: https://smolmachines.com/
- Added At: 2026-08-20 13:03:09
- Tags: #tools

## TL;DR
smol machines 是基于 libkrun 的轻量虚拟机项目，提供硬件隔离、快速启动（<200ms）的 Linux 微VM。工件 .smolmachine 可在本地、云和自托管一致运行，支持沙箱不可信代码、打包便携可执行文件、持久化开发机及 GPU 加速。

## Summary
smol machines 是一个提供快速、硬件隔离 Linux 虚拟机的开源项目。它的核心是 **smolvm**，一个基于 libkrun 的轻量级虚拟机运行时。设计目标是让同一个虚拟机工件（`.smolmachine`）能够在本地（macOS、Linux、Windows）、托管云（smol cloud）或你自己的服务器上完全一致地运行。你可以先在本地开发调试，然后直接部署到云端或自托管环境，无需修改任何配置。

## 安装与基本使用

在 macOS 或 Linux 上，通过官方脚本一键安装：

```bash
curl -sSL https://smolmachines.com/install.sh | bash
```

Windows 需要从 GitHub releases 下载 zip 包并启用 Windows Hypervisor Platform (WHP)。

常用命令示例：

- 运行一次性命令（临时 VM，退出后自动清理）：
  ```bash
  smolvm machine run --net --image alpine -- sh -c "echo 'Hello world from a microVM' && uname -a"
  ```
- 启动交互式 shell：
  ```bash
  smolvm machine run --net -it --image alpine -- /bin/sh
  ```
- 卸载：
  ```bash
  curl -sSL https://smolmachines.com/install.sh | bash -s -- --uninstall
  ```

## 主要用途

1. **沙箱不可信代码**  
   每个工作负载运行在独立的硬件虚拟机中，宿主机文件系统、网络和凭据被 hypervisor 边界隔离。默认网络关闭，可防止不可信程序外联；需要网络时可手动开启，并可通过 `--allow-host` 精确限制允许访问的域名。

2. **打包为便携可执行文件**  
   使用 `smolvm pack create` 可以把任何工作负载（如 Python 3.12）打包成一个自包含二进制文件，所有依赖已预置，无需安装步骤，启动时间低于 200 毫秒。例如：
   ```bash
   smolvm pack create --image python:3.12-alpine -o ./python312
   ./python312 run -- python3 --version
   ```

3. **持久化开发机器**  
   可以创建、启动、停止命名虚拟机，安装的软件包在重启后依然保留。适合需要长期运行开发环境的场景。

4. **GPU 加速工作负载**  
   支持 Vulkan 访问宿主机 GPU，可以在隔离虚拟机内运行图形相关任务（如无头 Chromium 截图）。

## 与其他方案对比

对比容器、QEMU 和 Firecracker：

- **隔离性**：smolvm 每个工作负载有自己的虚拟机（独立内核），而容器共享宿主机内核；QEMU 和 Firecracker 也是独立 VM，但 smolvm 在架构上更轻。
- **启动速度**：smolvm 小于 200ms，接近 Firecracker（小于 125ms），远快于 QEMU（15-30 秒），容器约 100ms。
- **架构**：smolvm 将 VMM（libkrun）作为库链接进二进制，没有守护进程；容器依赖 Docker 守护进程，QEMU/Firecracker 是独立进程。
- **GPU 支持**：smolvm 原生支持 Vulkan，QEMU 需要 VFIO，Firecracker 不支持，容器通常是宿主机直通。
- **macOS 原生**：smolvm 和 QEMU 支持，容器需要通过 Docker VM，Firecracker 不支持。
- **便携构件**：smolvm 提供 `.smolmachine` 工件，容器镜像需要守护进程，QEMU 和 Firecracker 没有这种机制。

## 工作原理

每个 smolvm 工作负载都运行在真正的硬件隔离环境中，拥有自己的内核。底层 hypervisor 根据宿主机系统自动选择：macOS 使用 Hypervisor.framework，Linux 使用 KVM，Windows 使用 Windows Hypervisor Platform。

默认分配 4 个 vCPU 和 8 GiB 内存，但内存通过 virtio balloon 实现弹性分配，宿主机只在实际使用时才提交内存，避免浪费。

核心技术栈是 **libkrun**（VMM）和 **libkrunfw**（定制内核）。VMM 作为一个库直接链接到 smolvm 二进制中，没有独立守护进程，所以架构更简洁、资源占用更低。

打包后的 `.smolmachine` 工件只要宿主机 CPU 架构匹配（x86_64 或 aarch64），就可以在任何支持平台上直接运行。

## 平台支持

| 宿主机 | 客户机架构 | 要求 |
|--------|------------|------|
| macOS Apple Silicon | arm64 Linux | macOS 11+ |
| macOS Intel | x86_64 Linux | macOS 11+（未充分测试） |
| Linux x86_64 | x86_64 Linux | 需要 KVM（/dev/kvm） |
| Linux aarch64 | aarch64 Linux | 需要 KVM（/dev/kvm） |
| Windows x86_64 | x86_64 Linux | 需要启用 WHP，从 GitHub releases 下载 |

总结：smol machines 提供了一种介于容器和传统虚拟机之间的方案，强调快速启动、硬件级隔离、跨平台一致性和便携性，尤其适合沙箱执行不可信代码、打包独立工具、以及需要 GPU 访问的隔离环境。
