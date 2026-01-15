# What came first- the CNAME or the A record
- URL: https://blog.cloudflare.com/cname-a-record-order-dns-standards/
- Added At: 2026-01-15 14:12:19
- Tags: #read #network

## TL;DR
2026年1月，Cloudflare因优化代码意外改动CNAME记录顺序，导致部分DNS客户端解析失败。问题源于RFC对记录顺序规定模糊，旧客户端依赖固定顺序解析。事后Cloudflare恢复原有顺序，并向IETF提交草案推动标准化。

## Summary
2026年1月8日，Cloudflare的1.1.1.1 DNS解析器在例行更新中，为降低内存使用而修改代码，意外改变了CNAME记录在DNS响应中的顺序，导致部分用户DNS解析失败。事件时间线显示，代码变更于2025年12月引入，2026年1月部署后触发问题，Cloudflare在数小时内回滚了变更。

问题根源在于代码优化时，将CNAME记录从响应列表的顶部移至底部。DNS CNAME链机制要求解析器按顺序追踪别名，最终指向A记录。一些DNS客户端实现（如glibc的getaddrinfo函数和某些Cisco交换机）依赖于CNAME记录出现在其他记录之前进行顺序解析；当顺序颠倒时，客户端无法正确匹配记录，导致解析失败。相比之下，大多数现代客户端（如systemd-resolved）通过解析整个记录集来避免此问题。

RFC 1034定义了DNS协议，但未明确规定CNAME记录的顺序，仅含糊提到“可能前置”，而未使用强制性术语如“MUST”。这种模糊性源于RFC的年龄和术语差异，例如资源记录集（RRset）内部的顺序不重要，但不同RRset间的顺序未定义。

Cloudflare基于此事件教训，决定保持CNAME记录优先的顺序，以避免兼容性问题，并向IETF提交了互联网草案，旨在澄清DNS响应中CNAME处理的标准化行为。此举旨在防止未来类似问题，促进DNS生态系统的一致性。
