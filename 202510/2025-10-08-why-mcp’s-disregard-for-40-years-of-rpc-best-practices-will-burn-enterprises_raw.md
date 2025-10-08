Title: Why MCP’s Disregard for 40 Years of RPC Best Practices Will Burn Enterprises

URL Source: https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b

Published Time: 2025-07-29T18:11:30Z

Markdown Content:
Fool me once, shame on you; fool me twice, shame on me.
-------------------------------------------------------

[![Image 1: Julien Simon](https://miro.medium.com/v2/resize:fill:64:64/1*gvYwkCghT_2Yp9Pv7XlJsA.jpeg)](https://julsimon.medium.com/?source=post_page---byline--8ef85ce5bc9b---------------------------------------)

9 min read

Jul 29, 2025

![Image 2](https://miro.medium.com/v2/resize:fit:496/1*jEwTbSxSg73s-8cARprlow.jpeg)

The Model Context Protocol (MCP) promises to standardize AI-tool interactions as the “USB-C for AI.” While its simplicity accelerates adoption, MCP systematically overlooks four decades of hard-won lessons from distributed systems. This isn’t an academic concern: enterprises deploying MCP today are building on foundations that lack fundamental capabilities that every production remote-procedure calling (RPC) system, since 1982, has deemed essential.

The Dangerous Gap Between Hype and Reality
------------------------------------------

MCP advocates position the protocol as production-ready infrastructure, but its design philosophy, prioritizing ease of adoption over operational robustness, creates a ticking time bomb for enterprises. The same simplicity that enables a developer to integrate a tool in an afternoon becomes a liability when that tool handles millions of requests with real business impact.

The AI hype cycle has accelerated adoption beyond the architectural maturity of MCP. Companies are deploying MCP not because it meets their operational requirements, but because the AI gold rush demands immediate action. This mismatch between expectations and capabilities will lead to painful production failures.

Four Decades of Lessons Ignored
-------------------------------

Let’s start with UNIX RPC, introduced in 1982. The creators understood something fundamental: when systems speak different languages or run on heterogeneous architectures, you need more than good intentions to ensure a 32-bit integer on one system doesn’t become garbage data on another. Their solution, External Data Representation (XDR), wasn’t over-engineering. It was essential for systems where data corruption could result in system failure. The Interface Definition Language (IDL) with compiler-generated stubs caught type mismatches at build time, not runtime.

MCP discards this lesson, opting for schemaless JSON with optional, non-enforced hints. Type validation happens at runtime, if at all. When an AI tool expects an ISO-8601 timestamp but receives a Unix epoch, the model might hallucinate dates rather than failing cleanly. In financial services, this means a trading AI could misinterpret numerical types and execute trades with the wrong decimal precision. In healthcare, patient data types get coerced incorrectly, potentially leading to wrong medication dosing recommendations. Manufacturing systems lose sensor reading precision during JSON serialization, leading to quality control failures.

CORBA emerged in 1991 with another crucial insight: in heterogeneous environments, you can’t just “implement the protocol” in each language and hope for the best. The OMG IDL generated consistent bindings across C++, Java, Python, and more, ensuring that a C++ exception thrown by a server was properly caught and handled by a Java client. The generated bindings guaranteed that all languages saw identical interfaces, preventing subtle serialization differences.

MCP ignores this completely. Each language implements MCP independently, guaranteeing inconsistencies. Python’s JSON encoder handles Unicode differently than JavaScript’s JSON encoder. Float representation varies. Error propagation is ad hoc. When frontend JavaScript and backend Python interpret MCP messages differently, you get integration nightmares. Third-party tools using different MCP libraries exhibit subtle incompatibilities only under edge cases. Language-specific bugs require expertise in each implementation, rather than knowledge of the protocol.

The year 2000 brought two major protocols with complementary lessons. REST taught us that statelessness enables horizontal scaling: any server can handle any request, allowing for load balancing and fault tolerance. Cache headers reduced backend load by orders of magnitude. The uniform interface with clear verb semantics made request intent obvious to intermediaries.

MCP mixes stateful and stateless operations without a clear distinction. While it maintains sessions via Mcp-Session-Id headers, there are no cache control mechanisms, no standardized operation semantics that enable safe retry. Tool invocations can’t be safely retried or load-balanced without understanding their side effects. You can’t horizontally scale MCP servers without complex session affinity. Every request hits the backend even for identical, repeated queries.

SOAP, despite its verbosity, understood something that MCP doesn’t: machine-readable contracts matter. WSDL enabled automated client generation, contract validation, and compatibility checking. WS-Security meant security tokens traveled with messages. Standardized fault contracts enabled consistent error handling across platforms.

MCP has none of this richness. No machine-readable contracts beyond basic JSON schemas means you can’t generate type-safe clients or prove to auditors that AI interactions follow specified contracts. While MCP now includes OAuth 2.1 support (as of the 2025–03–26 revision), this critical security feature wasn’t part of the original protocol that enterprises rushed to adopt. Even now, it only applies to HTTP transports. The stdio transport relies on environment variables for credentials, a 1970s approach that lacks the granular access control modern enterprises require. Schema changes break clients silently with no versioning support beyond the protocol level.

Fast forward to 2016, and gRPC showed us why observability isn’t optional in distributed systems. Built-in distributed tracing with metadata propagation enables debugging. Bidirectional streaming enabled responsive UIs. Deadline propagation prevented cascade failures. Structured status codes distinguish retriable from permanent failures.

MCP’s streaming support reveals the gulf between checkboxes and capabilities. Yes, it supports Server-Sent Events for streaming responses, and yes, servers can initiate requests. However, it lacks gRPC’s bidirectional streaming within a single RPC call, forcing complex interaction patterns to be implemented through multiple round-trips. There’s no trace context propagation. You can’t follow an AI’s decision path through multiple tool calls. Without deadline propagation, a single slow tool can block an entire AI agent. While MCP uses JSON-RPC’s error structure with code and message fields, it lacks the rich, actionable error taxonomies that distinguish, for example, “rate limit exceeded, retry in 30 seconds” from “invalid input, fix your request.”

The “Just Use This Library” Trap
--------------------------------

Here’s where MCP advocates reveal the protocol’s fundamental failure. Point out any of these gaps, and they’ll immediately respond with “Oh, but there’s mcp-oauth-wrapper that adds authentication!” or “Check out mcp-tracing-extension for distributed tracing!” or “Company X open-sourced mcp-schema-generator that solves the IDL problem!”

This response pattern is itself the problem. When your protocol’s answer to critical enterprise requirements is a constellation of third-party libraries, you haven’t built a protocol. You’ve built a recipe for fragmentation.

Consider what this means for an enterprise architect:

*   Which of the five competing MCP authentication libraries should we standardize on?
*   Are these libraries maintained? Will they be around in two years?
*   Do they interoperate? Can Tool A, using mcp-auth-li,b, work with Tool B using mcp-security-wrapper?
*   Who’s responsible for fixing security vulnerabilities?
*   How do we ensure consistent implementation across our 200-person engineering team?

This is exactly the fragmentation that protocols are supposed to prevent. gRPC doesn’t need a third-party tracing library. It’s built in. REST doesn’t require external caching semantics. They’re part of HTTP. CORBA didn’t need community-maintained IDL generators. The ORB vendors provided them.

The enterprise cost of this ecosystem fragmentation is staggering. Instead of training developers on one protocol, you’re training them on MCP plus a dozen semi-compatible extensions. Instead of conducting a single security audit, you’re auditing multiple authentication libraries. Instead of managing a single vendor relationship, you’re managing relationships with several open-source projects of varying quality and commitment levels.

The Patchwork Protocol Problem
------------------------------

The 2025–03–26 protocol revision reads like a patch notes list of everything enterprises discovered was missing in production. OAuth support, tool annotations for distinguishing read-only from destructive operations, session management, and progress notifications. These aren’t enhancements, they’re admissions of premature release.

Get Julien Simon’s stories in your inbox
----------------------------------------

Join Medium for free to get updates from this writer.

Consider tool annotations. MCP now supports marking tools as “read-only” or “destructive,” but this feature was introduced after early adopters had already built systems without such distinctions. It’s capability-based security as an afterthought, retrofitted after production incidents rather than designed from first principles.

The security additions are particularly telling. Authentication wasn’t an oversight. It was deemed unnecessary for the initial release. This reveals a fundamental misunderstanding of enterprise requirements. No Fortune 500 company would deploy a database without authentication, yet MCP advocates expect them to connect AI to critical business tools without it.

The Debugging Nightmare
-----------------------

Here’s a scenario I’ve lived in different forms across multiple protocols. Imagine debugging a production issue where an AI agent made 20 tool calls across five other services to answer a customer query, and the response was wrong.

With gRPC, distributed tracing would show you the exact call that failed in minutes. You’d see the full request flow, latency at each step, and the specific error that caused the problem. The trace ID would correlate logs across all services.

With MCP, you’re grepping through JSON logs across multiple services with no correlation IDs, trying to reconstruct what happened. Each service has its log format. There’s no standard way to track a request across tool boundaries. You can’t even reliably match requests to responses without building your correlation mechanism. I’ve lived both scenarios. One takes 30 minutes, the other takes 3 days.

The Cost Attribution Crisis
---------------------------

When OpenAI bills $50,000 for last month’s API usage, can you tell which department’s MCP tools drove that cost? Which specific tool calls? Which individual users or use cases?

MCP does not provide a mechanism for this basic operational requirement. No token counting at the protocol level. No cost attribution headers. No quota management. You’re flying blind on AI spend, unable to optimize or even understand where the money goes.

In contrast, cloud providers learned this lesson decades ago. Every AWS API call can be tagged, attributed, and cost-tracked. Every Google Cloud operation flows into detailed billing breakdowns. MCP asks enterprises to consume expensive AI resources with 1990s-level cost visibility.

Critical Operational Gaps That Remain
-------------------------------------

Service discovery might sound like a nice-to-have until you try to build resilient multi-region deployments. MCP’s manual configuration assumes you are familiar with all tools at the time of deployment. This breaks the moment you need dynamic scaling or failover. You can’t build systems that adapt to infrastructure changes.

Version management becomes critical when you have dozens of tools evolving independently of one another. MCP has protocol version negotiation but no schema versioning. Tool interfaces can change without warning. Any tool update risks breaking all clients. You face a choice: never update tools, or coordinate massive deployment efforts across your entire ecosystem.

Performance may not matter for demos, but the overhead of JSON and the lack of connection pooling don’t scale. When you need low-latency, high-throughput AI systems for real-time applications, MCP’s text-based protocol becomes a bottleneck. There’s no binary protocol option, no compression beyond transport-level gzip. The stdio transport, in particular, creates a new process connection for every interaction, a pattern we abandoned in the 1990s for good reason.

Why These Omissions Matter Now
------------------------------

The adoption curve for enterprise AI is steepening. Companies aren’t experimenting anymore. They’re deploying AI into revenue-critical and safety-critical systems. Financial services use AI for trading decisions, fraud detection, and risk assessment. Healthcare systems offer diagnostic support and personalized treatment recommendations. Industrial systems rely on AI for quality control and predictive maintenance. Customer service handles sensitive data through AI interactions.

Each of these domains has spent decades building robust integration patterns. MCP asks them to abandon these patterns for a protocol that’s still retrofitting basic security features. The “move fast and break things” approach that works for demos becomes catastrophic when applied to systems where failures have real consequences.

The Path Forward: Learning from History
---------------------------------------

MCP doesn’t need to become CORBA, but it must incorporate proven patterns. The recent additions show that the maintainers are listening, but they’re playing catch-up with problems that their elders solved decades ago.

Immediate needs that remain unaddressed include improved type safety, distributed tracing with correlation IDs integrated into the protocol, capability-based authorization that extends beyond simple tool annotations, standardized audit trail formats for compliance, and schema versioning that is independent of protocol version.

Short-term evolution should focus on operational necessities, including service discovery mechanisms for dynamic environments, connection pooling and persistent connections for improved performance, binary protocol options for high-throughput scenarios, deadline propagation to prevent cascading failures, and comprehensive error taxonomies with standardized retry semantics.

Long-term maturity requires enterprise-grade features: true bidirectional streaming for complex interactions, built-in rate limiting and quota management, SLA enforcement mechanisms, comprehensive cost attribution for token usage, and workflow orchestration primitives.

The Bottom Line
---------------

MCP’s current design reflects a bet that simplicity trumps robustness for AI tool integration. This bet makes sense for experimentation but fails catastrophically for production deployment. The protocol’s rapid adoption, driven by AI hype rather than operational readiness, is setting up enterprises for painful failures.

The pattern of retrofitting critical features proves that MCP was released prematurely. Enterprises adopted it based on promises and hype, not operational reality. Now they’re discovering that adding security, observability, and proper error handling after the fact is akin to adding airbags to a car after it has crashed.

We have forty years of experience in distributed systems, demonstrating which patterns enable reliable, secure, and scalable operations. These aren’t academic exercises. They’re solutions to problems that cost real companies real money when systems fail.

The window is closing. As enterprises reach the limitations of MCP, they’ll build proprietary solutions. So will software vendors. The fragmentation that MCP aimed to prevent will still emerge, albeit with additional steps and wasted effort.

The AI industry has a choice: learn from four decades of RPC evolution or repeat every painful mistake. Based on the current trajectory, with critical features being bolted on as afterthoughts, we’re choosing repetition, and enterprises will pay the price in failed deployments, security breaches, and operational nightmares that were entirely preventable.

[Julien](https://www.julien.org/)

—

_This analysis is based on the latest MCP specification:_[_https://modelcontextprotocol.io/specification/2025-06-18_](https://modelcontextprotocol.io/specification/2025-06-18)