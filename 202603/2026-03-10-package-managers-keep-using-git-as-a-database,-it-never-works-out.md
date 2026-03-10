# Package managers keep using git as a database, it never works out
- URL: https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html
- Added At: 2026-03-10 13:57:42
- Tags: #read

## TL;DR
多个包管理器曾尝试用 Git 存储索引，但因性能、可扩展性等问题逐步转向 HTTP 或数据库方案。Git 更适合代码协作，而非包注册表的数据存储。

## Summary
包管理器将 Git 用作数据库是一种诱人的想法，它提供了免费版本历史、分布式协作和 GitHub 托管，但实践中屡屡失败。多个主流包管理器都曾尝试使用 Git 作为索引或数据存储，最终因性能、可扩展性和用户体验问题而转向其他方案。

**Cargo（Rust）**
- 起初 crate 索引以 Git 仓库形式存在，克隆完整索引导致性能问题，尤其在 CI 中浪费时间和带宽。
- 2025 年通过 RFC 2789 引入稀疏 HTTP 协议，按需下载元数据，99% 的请求现使用稀疏索引，Git 索引仍存在但多数用户不再接触。

**Homebrew**
- GitHub 要求停止深度克隆，因树状布局和流量导致更新昂贵。
- 2023 年的 Homebrew 4.0.0 转向 JSON 下载更新，自动更新提速且不再依赖 Git 操作。

**CocoaPods**
- Spec 仓库结构复杂，克隆和更新耗时长，触发 GitHub 速率限制。
- 1.8 版本默认使用 CDN 提供模组说明文件，大幅提升安装速度并节省磁盘空间。

**Nixpkgs**
- 客户端通过通道和 CDN 获取 tarball，无需克隆 Git。
- 但仓库本身（83GB、大量 Fork）给 GitHub 基础设施带来压力，曾出现维护故障。

**vcpkg**
- 使用 Git 树哈希版本化端口，依赖完整历史记录，浅克隆会导致错误。
- 缺乏 HTTP 替代方案，用户需克隆完整历史或使用变通方法，没有转向其他格式的计划。

**Go Modules**
- 早期 `go get` 需克隆完整仓库以读取 go.mod 文件，效率低下且存在安全风险。
- 现通过 GOPROXY 和 checksum 数据库提供 HTTP 源码归档和模块验证，不再依赖 Git。

**Beyond Package Managers**
- Git-based 工具如维基（Gollum）、CMS（Decap）和 GitOps（ArgoCD）均面临性能、速率限制或存储问题。

**核心问题与模式**
- 文件系统限制（目录文件量、大小写敏感性、路径长度）使 Git 不适合作为数据库。
- Git 缺乏数据库特性（约束、索引、锁、迁移），导致包管理器需自行构建验证和查询层。
- 进展规律：从平面目录开始 → 触发文件系统限制 → 实施分片 → 遇跨平台问题 → 构建服务端强制措施 → 最终转向 HTTP 或真实数据库。

**结论**
- Git 擅长分布式代码协作，但不适合作为包注册表的数据存储。包管理器应避免重蹈覆辙，直接采用 HTTP 或数据库方案以提供快速查询和更好体验。
