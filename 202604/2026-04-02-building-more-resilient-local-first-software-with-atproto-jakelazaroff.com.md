# Building More Resilient Local-First Software with atproto | jakelazaroff.com
- URL: https://jakelazaroff.com/words/building-more-resilient-local-first-software-with-atproto/
- Added At: 2026-04-02 14:45:08
- Tags: #read #deepdive

## TL;DR
本文探讨利用 atproto 协议构建本地优先软件，通过 CRDT 与个人数据服务器（PDS）实现无服务器的实时协作文本编辑。方案结合持久化、同步与实时机制，但也指出 Jetstream 等局限性。作者认为 atproto 与本地优先理念契合，并提供了简化实现的 npm 包。

## Summary
本文探讨了如何利用 atproto 协议构建更具弹性的本地优先软件。作者通过一个实时协作文本编辑器的案例，展示了如何在没有专用同步服务器的情况下，仅依赖 atproto 实现数据同步与协作。

核心思路是结合 CRDT（无冲突复制数据类型）与 atproto 的个人数据服务器（PDS）。每个用户通过 DID 标识，其数据存储在 PDS 中。应用将文档的更新记录为 JSON 结构，存储在 PDS 的特定集合中。通过 CRDT 库（如 Yjs）合并来自不同用户的更新，确保最终一致性。

协作机制包括：
- **持久化**：将文档更新编码后存入用户自己的 PDS，并通过缓冲机制避免速率限制。
- **发现与同步**：文档所有者通过一个“文档记录”维护编辑者列表，各编辑者从彼此的 PDS 拉取更新。
- **实时编辑**：使用 atproto 的 Jetstream（WebSocket 流）监听 PDS 中的更新事件，并通过验证内容标识符（CID）确保数据真实性。
- **状态感知**：使用独立的集合存储光标位置等临时状态，并通过 Jetstream 实现实时同步。

文章也指出了当前方案的局限性：Jetstream 缺乏签名验证、数据公开性、文档所有权模型限制、公开编辑困难以及实时性延迟问题。

最终，作者认为 atproto 与本地优先社区目标一致（用户自主、数据所有权、互操作性），并希望激发更多交叉领域的探索。文末还提到了一个现成的 npm 包 `y-atproto`，可简化类似实现。
