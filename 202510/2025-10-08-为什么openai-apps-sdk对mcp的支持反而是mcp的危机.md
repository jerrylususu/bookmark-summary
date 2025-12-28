# 为什么OpenAI Apps SDK对MCP的支持反而是MCP的危机
- URL: https://grapeot.me/mcp-revisited.html
- Added At: 2025-10-08 11:33:13

## TL;DR
OpenAI的Apps SDK扩展了MCP，引入私有dialect以绕过context window限制，但导致协议分裂和生态绑定。MCP面临设计偏科研、缺乏工程考量的问题，可能走向类似SQL的厂商碎片化。未来或出现更高层抽象协议来统一变种，结果取决于技术演进和厂商博弈。

## Summary
MCP（Model Context Protocol）最初由Anthropic设计，作为一种开放协议，主要服务于AI科学研究，强调所有信息必须通过LLM的context window传递，以支持Agentic AI的探索。然而，随着工程应用的广泛关注，MCP在现实场景中面临诸多挑战，如状态管理、调试困难和协议设计的工程不成熟性。

OpenAI推出的Apps SDK扩展了MCP，引入`_meta`域以绕过context window限制，支持GUI渲染等功能。这一做法虽然务实，却导致协议分裂，形成私有dialect（如`openai/*`结构），威胁MCP的开放性和统一性。开发者一旦依赖这些扩展，应用将高度绑定OpenAI生态，削弱MCP的通用性。

历史类比表明，表达性协议（如SQL、CSS）容易因厂商定制而分裂，而管道式协议（如HTTP、USB）更易保持兼容。MCP更可能走向前者，因其设计初衷偏重科研，缺乏工程考量，且过早被工程界广泛采用。

未来可能的发展包括：OpenAI通过dialect架空MCP成为事实标准，或出现更高层抽象协议（如类似JDBC/ODBC的解决方案）以统一各变种。结果取决于技术演进和各厂商的政治博弈。总体而言，Apps SDK的发布凸显了MCP的潜在危机，而非单纯的成功标志。
