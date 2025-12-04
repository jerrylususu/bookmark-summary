# Advanced network traffic interception techniques with mitmproxy – Trickster Dev
- URL: https://www.trickster.dev/post/advanced-network-traffic-interception-techniques-with-mitmproxy/
- Added At: 2025-12-04 14:23:22
- Tags: #read #tips #hack #network
- [Link To Text](2025-12-04-advanced-network-traffic-interception-techniques-with-mitmproxy-–-trickster-dev_raw.md)

## TL;DR
mitmproxy 提供了反向代理、透明代理、Wireguard VPN、SOCKS5、DNS服务、上游代理及虚拟网络接口等多种模式，支持各类网络环境下的流量拦截与分析，适用于服务器监控、移动设备调试等场景。

## Summary
本文介绍了 mitmproxy 的高级网络流量拦截技术，除了默认的正向代理模式外，还涵盖了多种其他模式，以扩展其在客户端和服务器间流量分析中的应用。

- **反向代理模式**：将 mitmproxy 配置为反向代理，客户端直接访问 mitmproxy 而非真实服务器。需在客户端修改 DNS 解析（如编辑 `/etc/hosts`）并安装 mitmproxy 的 X.509 证书（例如在 Chrome 中通过证书管理器导入），以拦截 HTTPS 流量。

- **透明代理模式**：在网络层重定向流量，无需应用层代理配置，适用于无法设置代理的应用程序。具体操作参考 mitmproxy 官方文档。

- **Wireguard VPN 服务器模式**：使用 `mitmweb --mode wireguard` 启动，生成 QR 码供移动设备连接，可拦截 HTTP(S)、DNS 等协议流量。建议提前安装证书以确保 TLS 拦截正常。

- **SOCKS 代理模式**：通过 `mitmproxy --mode socks5` 启动 SOCKS5 服务器（默认端口 1080），支持如 curl 等工具测试流量拦截。

- **DNS 服务器模式**：运行 `mitmproxy --mode dns@5333` 作为简易 DNS 服务器，处理 A 和 AAAA 查询，可使用 dnsx 等工具验证。

- **上游代理传递**：通过 `--mode upstream` 选项将流量转发至其他代理（如地理限制场景），支持认证参数。

- **虚拟网络接口模式**：在 Linux 系统下以 root 权限运行 `mitmproxy --mode tun`，创建虚拟接口拦截所有经过流量，可通过修改路由表或指定接口（如 curl 的 `--interface`）实现。

这些模式扩展了 mitmproxy 的适用场景，适用于服务器监控、移动设备调试或复杂网络环境下的流量分析。
