# Personal infrastructure setup 2026
- URL: https://linderud.dev/blog/personal-infrastructure-setup-2026/
- Added At: 2026-01-24 04:58:38
- Tags: #read

## TL;DR
Morten Linderud在2026年的个人基础设施设置旨在自托管邮件、博客等服务，使用Incus管理容器和虚拟机，Opentofu实现自动化。硬件包括NAS和NUC设备，网络通过WireGuard VPN和Nginx代理解决ISP限制。设置强调简单可靠，代码开源供学习。

## Summary
本文总结了Morten Linderud在2026年个人基础设施的设置，重点包括硬件、软件工具和网络配置。

**背景和动机**  
作者长期维护个人基础设施，目的是自托管电子邮件、博客、IRC等服务，并简化管理流程。由于家庭ISP限制，需要通过WireGuard隧道暴露服务到互联网。

**硬件配置**  
- NAS：配备2x8 TB硬盘，硬件可能来自2012年。  
- Intel NUC（2015年）：Intel i5-6260U处理器，16 GB RAM。  
- AMD NUC：AMD Ryzen 7 8745HS处理器，64 GB RAM，购自AliExpress。  
- OpenWRT One路由器：支持OpenWRT系统。

**容器化平台（Incus）**  
- 使用Incus管理容器和虚拟机，支持LXC、QEMU VM和OCI容器。  
- 集群包括两个NUC节点（amd和byggmester），使用扁平网络配置，通过桥接设备（br0）分配IP。  
- 默认配置文件简化了网络和存储设置。

**基础设施即代码（Opentofu）**  
- 通过Opentofu声明式管理Incus资源，项目化组织服务（如Immich、DNS、Miniflux）。  
- 代码存储于GitHub，便于部署和实验。  
- 示例展示了如何从Docker镜像启动服务（如Valkey）。

**网络和暴露服务**  
- 使用WireGuard点对点VPN连接到黑客空间的VPS，解决ISP NAT和动态IP问题。  
- Nginx作为反向代理，配合nginx-acme自动管理TLS证书。  
- 配置示例展示了如何代理内部服务（如Immich）到互联网。

**静态网站托管**  
- 静态网站（如博客）通过Hugo构建，输出到本地目录（/srv/linderud.dev）。  
- 使用Syncthing同步到Web服务器，避免复杂CI/CD依赖。

**其他工具**  
- OpenWRT One：使用自定义Opentofu provider管理路由器，计划未来引入VLAN。  
- usbkvm：小型KVM设备，便于连接和管理多个计算机。

**结论**  
作者强调设置的简单性和可靠性，旨在为自托管爱好者提供灵感，并保持代码开放供学习。设置注重本地控制，避免云服务依赖。
