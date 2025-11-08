# Spinning up an Onion Mirror is Stupid Easy | flower.codes
- URL: https://flower.codes/2025/10/23/onion-mirror.html
- Added At: 2025-11-08 08:52:28
- Tags: #read
- [Link To Text](2025-11-08-spinning-up-an-onion-mirror-is-stupid-easy-flower.codes_raw.md)

## TL;DR
本文介绍了基于 Debian 系统和 Caddy 服务器快速创建.onion镜像网站的步骤，包括安装并配置 Tor、获取.onion地址、调整 Caddy 设置和添加Onion-Location提示，过程简单实用，旨在提升网站的可访问性与抗审查能力。

## Summary
本文介绍了如何轻松创建.onion镜像网站，主要面向已有网站的用户，旨在提高可访问性和抗审查性。整个过程基于Debian系统、Caddy服务器和Tor服务，步骤简明：

1. **前提条件**：使用Caddy作为Web服务器、DigitalOcean VPS作为主机、Debian操作系统。
2. **安装Tor**：通过`sudo apt install tor`命令安装。
3. **配置Tor**：编辑`/etc/tor/torrc`文件，设置隐藏服务端口为80，禁用其他不必要功能（如SOCKS代理和中继）。
4. **重启Tor**：运行`sudo systemctl restart tor`使配置生效。
5. **获取.onion地址**：使用`sudo cat /var/lib/tor/hidden_service/hostname`查看生成的地址。
6. **配置Caddy**：若Caddy已监听80端口，无需额外配置；否则需添加站点区块支持.onion地址的HTTP服务（因.onion不支持HTTPS证书，但Tor内置加密已足够安全）。
7. **可选广告**：通过设置`Onion-Location`HTTP头，在主流网站上自动提示用户访问.onion镜像。
8. **测试**：使用Tor浏览器访问.onion地址验证服务。

整个过程仅需几个命令和简单配置，强调易用性和实用性。
