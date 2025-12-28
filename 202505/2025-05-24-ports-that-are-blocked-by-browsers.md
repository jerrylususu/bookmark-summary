# Ports that are blocked by browsers
- URL: https://www.keenformatics.com/ports-that-are-blocked-by-browsers
- Added At: 2025-05-24 10:39:40

## TL;DR


主流浏览器为防范跨协议脚本攻击，直接封锁6000（X11）、25（SMTP）、110（POP3）等60余个敏感端口，访问时Chrome显示ERR_UNSAFE_PORT，Firefox明确提示限制，而Safari直接空白。此机制阻止通过HTML强制调用安全端口的恶意行为，但开发者可用curl等终端工具绕过限制。

## Summary


文章探讨了浏览器阻止特定端口访问的现象。作者在实验中发现，访问本地6000端口时出现ERR_UNSAFE_PORT错误，而8000端口正常。通过测试Python内置HTTP服务器及排除Docker影响，确认问题源于浏览器层面拦截。原因与“跨协议脚本攻击”漏洞相关，攻击者可能利用该漏洞通过HTML强制受害者服务（如邮件、FTP）发送恶意数据。主流浏览器为防范此风险，直接封锁特定端口（如SMTP的25端口、POP3的110端口、X11的6000端口等）。不同浏览器提示不同：Chrome显示ERR_UNSAFE_PORT，Safari空白，Firefox明确提示“该地址受限制”。使用curl等终端工具可绕过限制直接访问被屏蔽端口。Firefox封锁的端口列表包含60余个常用服务端口，涵盖网络协议、邮件、文件传输等关键功能。
