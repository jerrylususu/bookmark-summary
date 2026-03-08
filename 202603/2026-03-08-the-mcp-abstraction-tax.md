# The MCP Abstraction Tax
- URL: https://justin.poehnelt.com/posts/mcp-abstraction-tax/
- Added At: 2026-03-08 16:12:05
- Tags: #read #agent

## TL;DR
本文提出了AI代理与API交互中的“抽象税”概念，指出每个抽象层会降低保真度并可能损害上下文。通过对比MCP和CLI路径，作者强调应根据场景权衡迭代速度与上下文管理，并非竞争关系。

## Summary
本文探讨了AI代理与API之间的抽象层级问题，提出了“抽象税”的概念。作者指出，从数据到API再到MCP（Model Context Protocol），每增加一层抽象，都会损失一定的保真度，尤其在处理复杂企业API时，这种损失会叠加。文章对比了MCP和CLI两种路径：MCP通过工具定义提供可发现性和标准化，但可能因上下文限制而损失表达能力；CLI结合“技能”（Skills）方法，则支持按需加载上下文，实现更高保真度。作者认为两者并非竞争关系，而是优化不同目标的曲线上的点；关键在于理解每种方法的代价，并根据具体场景选择合适方案。此外，API本身的不友好性会进一步加剧抽象税，因此需要权衡迭代速度、上下文管理和客户端智能程度。
