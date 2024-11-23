# How decentralized is Bluesky really? -- Dustycloud Brainstorms
- URL: https://dustycloud.org/blog/how-decentralized-is-bluesky/
- Added At: 2024-11-23 00:21:26
- [Link To Text](2024-11-23-how-decentralized-is-bluesky-really----dustycloud-brainstorms_raw.md)

## TL;DR
Bluesky作为Twitter替代品成功吸引了大量用户，但其架构和技术实现并未真正实现去中心化和联邦化。尽管在用户体验和内容持久性方面表现出色，但其中心化问题和资源需求限制了去中心化的可能性。Bluesky应明确“可信退出”的定位，并逐步实现真正的去中心化。

## Summary
1. **背景介绍**：
   - **Bluesky的兴起**：由于X-Twitter用户大量流失，Bluesky及其底层协议ATProto变得非常流行。
   - **作者背景**：作者曾参与ActivityPub的开发，该协议连接了Mastodon、Sharkey、Peertube等平台。

2. **Bluesky与ActivityPub的对比**：
   - **作者观点**：Bluesky和ATProto在技术上并不具备真正的去中心化，也不是联邦化的。
   - **Bluesky的目标**：主要目标是提供一个Twitter的替代品，而非构建一个去中心化的Twitter。

3. **Bluesky的优势**：
   - **快速扩展**：成功应对了用户激增的挑战，成为逃离X-Twitter用户的首选。
   - **用户体验**：提供了与旧版Twitter几乎相同的功能，满足了用户的需求。
   - **内容持久性**：使用内容寻址技术，确保内容在节点宕机后仍可访问。

4. **Bluesky的架构与中心化问题**：
   - **博客与搜索引擎的比喻**：Bluesky的架构类似于博客被Bluesky作为搜索引擎聚合，但实际上是一个封闭的花园。
   - **资源需求**：运行Bluesky节点需要大量资源，尤其是存储空间，这限制了去中心化的可能性。

5. **架构对比**：
   - **消息传递与共享堆栈架构**：ActivityPub采用消息传递架构，而Bluesky采用共享堆栈架构，后者导致更高的资源需求和中心化问题。
   - **存储与带宽需求**：Bluesky的存储需求随用户增长呈指数级上升，使得去中心化变得不切实际。

6. **隐私与身份问题**：
   - **公开的屏蔽信息**：Bluesky中的屏蔽信息是公开的，这与ActivityPub的设计理念相悖。
   - **直接消息的中心化**：Bluesky的直接消息系统是完全中心化的，且不支持端到端加密。

7. **身份系统的挑战**：
   - **DID方法的局限**：Bluesky使用的DID方法（如did:web和did:plc）存在中心化问题，且与DNS系统有循环依赖。
   - **身份迁移的困难**：用户即使迁移身份，仍需依赖Bluesky的服务，无法实现真正的去中心化。

8. **对Fediverse的建议**：
   - **改进方向**：Fediverse应采用内容寻址存储、便携式身份、宠物名系统等技术，以增强去中心化和隐私保护。
   - **技术挑战**：尽管这些改进在技术上是可行的，但需要社区的广泛支持和实施。

9. **Bluesky的未来与组织挑战**：
   - **组织的自我反思**：Bluesky团队认识到“组织是未来的对手”，这有助于其长期发展。
   - **资金与商业模式**：Bluesky已获得多轮融资，但需平衡投资者回报与去中心化目标。
   - **可信退出策略**：Bluesky应专注于实现“可信退出”，即用户可以在不依赖Bluesky的情况下继续使用其数据和身份。

10. **结论**：
    - **Bluesky的定位**：作为一个Twitter替代品，Bluesky是成功的，但在去中心化和联邦化方面存在明显不足。
    - **建议**：Bluesky应明确其“可信退出”的定位，并在技术上逐步实现真正的去中心化。
