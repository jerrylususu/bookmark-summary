Title: How to build secure and scalable remote MCP servers

URL Source: https://github.blog/ai-and-ml/generative-ai/how-to-build-secure-and-scalable-remote-mcp-servers/

Published Time: 2025-07-25T17:12:02+00:00

Markdown Content:
More context can mean more attack surfaces for your projects. Be prepared for what lies ahead with this guide.

July 25, 2025

|

11 minutes

*    Share: 
*   [](https://x.com/share?text=How%20to%20build%20secure%20and%20scalable%20remote%20MCP%20servers&url=https%3A%2F%2Fgithub.blog%2Fai-and-ml%2Fgenerative-ai%2Fhow-to-build-secure-and-scalable-remote-mcp-servers%2F)
*   [](https://www.facebook.com/sharer/sharer.php?t=How%20to%20build%20secure%20and%20scalable%20remote%20MCP%20servers&u=https%3A%2F%2Fgithub.blog%2Fai-and-ml%2Fgenerative-ai%2Fhow-to-build-secure-and-scalable-remote-mcp-servers%2F)
*   [](https://www.linkedin.com/shareArticle?title=How%20to%20build%20secure%20and%20scalable%20remote%20MCP%20servers&url=https%3A%2F%2Fgithub.blog%2Fai-and-ml%2Fgenerative-ai%2Fhow-to-build-secure-and-scalable-remote-mcp-servers%2F)

[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) enables AI agents to connect to external tools and data sources without having to implement API-specific connectors. Whether you’re extracting key data from invoices, summarizing support tickets, or searching for code snippets across a large codebase, MCP provides a standardized way to connect LLMs with the context they need.

Below we’ll dig into why security is such a crucial component to MCP usage, especially with a [recent specification release](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization), as well as how developers of both MCP clients and MCP servers can build secure integrations from the get-go.

Why security matters for MCP
----------------------------

Unlike traditional APIs that serve known clients in somewhat controlled environments, MCP servers act as bridges between AI agents and an unlimited number of data sources that can include sensitive enterprise resources. So, a security breach won’t just compromise data — it can give malicious actors the ability to manipulate AI behavior and access connected systems.

To help prevent common pitfalls, the MCP specification now includes [security guidelines](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) and best practices that address common attack vectors, like confused deputy problems, token passthrough vulnerabilities, and session hijacking. Following these patterns from the start can help you build systems that can handle sensitive tools and data.

Understanding the MCP authorization
-----------------------------------

The MCP specification uses [OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13) for secure authorization. This allows MCP, at the protocol level, to take advantage of many modern security capabilities, including:

*   **Authorization server discovery**: MCP servers implement OAuth 2.0 Protected Resource Metadata (PRM) ([RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728/)) to advertise the authorization servers that they support. When a client attempts to access a protected MCP server, the server will respond with a `HTTP 401 Unauthorized` and include a `WWW-Authenticate` header pointing to the metadata endpoint.
*   **Dynamic client registration**: This is automatic client registration using OAuth 2.0 Dynamic Client Registration Protocol ([RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591/)). This removes the need for manual client setup when AI agents connect to MCP servers dynamically.
*   **Resource indicators**: The specification also mandates [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) Resource Indicators, ensuring that tokens are bound to specific MCP servers. This prevents token reuse attacks and helps maintain clear security boundaries.

Even with the latest changes to [authorization specs](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization), like the clean split between the responsibilities of the authorization server and the resource server, developers don’t need to worry about implementing security infrastructure from scratch. (Because the requirement to follow the OAuth2.1 conventions didn’t change.) So developers can just use off-the-shelf authorization servers and identity providers.

Because MCP requires implementers to snap to OAuth 2.1 as the default approach to authorization, this also means that developers can use existing OAuth libraries to build the authorization capabilities into their MCP servers without anything super-custom. This is a massive time and effort saver.

### The complete authorization flow

When it comes to connecting to protected MCP servers, a MCP client will need to _somehow_ find out what credentials the server needs. Luckily, because of the aforementioned discovery mechanism, this is a relatively straightforward flow:

1.   **Discovery phase**. MCP client attempts to access MCP server without credentials (that is a token).
2.   **Server response**. MCP server returns a `HTTP 401 Unauthorized` response with a metadata URL in the `WWW-Authenticate` header.
3.   **Metadata retrieval**. MCP client fetches Protected Resource Metadata, parses it, and then gets the authorization server endpoints.
4.   **Client registration**. MCP client automatically registers with authorization server (if supported). Some clients may be pre-registered.
5.   **Authorization request**. MCP client initiates OAuth flow with Proof Key for Code Exchange (PKCE) and the `resource` parameter.
6.   **User consent**. The user authorizes access through the authorization server.
7.   **Token exchange**. MCP client exchanges authorization code for access token.
8.   **Authenticated requests**. All subsequent requests from MCP client to MCP server include `Bearer` token.

Nothing in the flow here is MCP-specific, and that’s the beauty of MCP snapping to a common industry standard. There’s no need to reinvent the wheel because a robust solution already exists.

Implementing authorization in MCP
---------------------------------

Most OAuth providers work well for MCP server authorization without any additional configuration, though one of the more challenging gaps today is the availability of Dynamic Client Registration. However, support for that feature is slowly rolling out across the identity ecosystem, and we expect it to be more common as MCP gains traction.

Aside from the authorization server, when implementing authorization for your MCP server, you will need to consider several key components and behaviors:

*   **PRM endpoint**. The MCP server must implement the `/.well-known/oauth-protected-resource` endpoint to advertise supported authorization server scopes. The [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) already integrates this capability natively, with other MCP SDK support coming very soon.
*   **Token validation middleware**. You need to make sure that your MCP server is only accepting tokens meant for it. Many open source solutions, like [PyJWT](https://github.com/jpadilla/pyjwt), can help you here by: 
    *   Extracting Bearer tokens from Authorization headers
    *   Validating token signatures using your OAuth provider’s JSON Web Key Sets (JWKS) endpoint
    *   Checking token expiration and audience claims
    *   Ensuring tokens were issued specifically for your MCP server (this part is critical for the security of your infrastructure)

*   **Error handling**. Your MCP server will need to return proper HTTP status codes (`HTTP 401 Unauthorized` for missing/invalid tokens, `HTTP 403 Forbidden` for insufficient permissions) with appropriate `WWW-Authenticate` headers.

Anthropic, together with the broader MCP community, is working on integrating a lot of these capabilities directly into the MCP SDKs, removing the need to implement many of the requirements from scratch. For MCP server developers, this will be the recommended path when it comes to building implementations that conform to the MCP specification and will be able to work with _any_ MCP client out there.

### Handling multi-user scenarios

Multi-tenancy in MCP servers introduces unique security challenges that go beyond simple authorization and token validation. When your MCP server handles requests from multiple users — each with their own identities, permissions, and data — you must enforce strict boundaries to prevent unauthorized access and data leakage. This is a classic “confused deputy” problem, where a legitimate user could inadvertently trick the MCP server into accessing resources they shouldn’t.

OAuth tokens are the foundation for securely identifying users. They often contain the necessary user information embedded within their claims (like the `sub` claim for user ID), but this data must be rigorously validated, and not blindly trusted.

As mentioned earlier in the blog post, your MCP server is responsible for:

1.   **Extracting and validating user identity**. After validating the token’s signature and expiration, it can extract the user identifier from the claims.
2.   **Enforcing authorization policies**. Map the user identifier to an internal user profile to determine their specific permissions. Just because a user is authenticated doesn’t mean they are authorized to perform every action or access every piece of data that the MCP server makes available.
3.   **Ensure correct token audience**: Double-check that the token was issued specifically for your MCP server by validating the audience (e.g., in a JSON Web Token this can be the `aud` claim). This prevents a token obtained for one MCP server from being used to access another.

With the user’s identity and permissions established, data isolation becomes the next critical layer of defense. Every database query, downstream API request, cache lookup, and log entry must be scoped to the current user. Failure to do so can lead to one user’s data being accidentally exposed to another. Adhering to the principle of least privilege — where a user can only access the data and perform the actions strictly necessary for their tasks — is paramount.

As with other security-sensitive operations, we strongly recommend you use existing, well-tested libraries and frameworks for handling user sessions and data scoping rather than implementing your own from scratch.

Scaling with AI gateways
------------------------

As your MCP server gains visibility and adoption, raw performance and basic authorization capabilities won’t be enough. You’ll face challenges like traffic spikes from AI agents making rapid-fire requests, the need to transform between different protocol versions as clients evolve at different speeds, and the complexity of managing security policies consistently across multiple server instances.

An [AI gateway](https://learn.microsoft.com/azure/api-management/genai-gateway-capabilities), similar to what you might’ve seen with API gateways before, sits between your MCP client and MCP server, acting as both a shield and a traffic director. It handles the mundane but critical tasks that would otherwise clutter your business logic, such as rate limiting aggressive clients, validating JWT tokens before they reach your servers, and adding security headers that protect against common web vulnerabilities.

### AI gateway configuration for MCP servers

The great thing about using an AI gateway lies in centralizing cross-cutting concerns. Rather than implementing rate limiting in every MCP server instance, you configure it once at the gateway level. The same applies to JWT validation. Let the gateway handle token verification against your OAuth provider’s requirements, then forward only validated requests with clean user context to your MCP server. This separation of concerns makes maintainability and diagnostics much easier, as you don’t need to worry about spaghetti code mixing responsibilities in one MCP server implementation.

Consider implementing these essential policies:

*   Rate limiting to prevent resource exhaustion from runaway AI agents
*   Request/response transformation to handle protocol evolution gracefully
*   Caching for expensive operations that don’t change frequently
*   Circuit breakers that fail fast when downstream services are struggling

The AI gateway also becomes your first line of defense for CORS handling and automatic security header injections.

Production-ready patterns
-------------------------

With the basics out of the way, you’re probably wondering what special considerations you need to keep in mind when deploying MCP servers to production. This section is all about best practices that we recommend you adopt to build secure and scalable MCP infrastructure.

### Better secrets management

We cannot not talk about secrets. Chances are that your MCP server needs to handle its own collection of secrets to talk to many different services, databases, or APIs that are out of direct reach of the MCP server consumers. You wouldn’t want someone to be able to have direct access to the credentials stored on the MCP server to talk to your internal APIs, for example.

Knowing this, secrets in MCP servers present a unique challenge: They’re needed frequently for things like OAuth validation, external API calls, and database connections, which makes them prime targets for attackers. Compromising a MCP server often means gaining access to a wide array of downstream systems. Robust secrets management is a non-negotiable requirement for anything with Internet access.

What we often see is that developers default to very basic implementations that are just enough to get things working, usually based on environment variables. While these are convenient for local development, they are a security anti-pattern in production. Environment variables are difficult to rotate, often leak into logs or build artifacts, and provide a static target for attackers.

The modern approach is to move secrets out of your application’s configuration and into a dedicated secrets management service like [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts), [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), or [HashiCorp Vault](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault). These services provide encrypted storage, fine-grained access control, detailed audit trails, and centralized management.

But the most secure way to access these vaults is by eliminating the “bootstrap secret” problem altogether using **workload identities** (you might’ve heard the term “secretless” or “keyless”). Different providers might have a different term or implementation of it, but the gist is that instead of storing a credential to access the vault, your application is assigned a secure identity by the cloud platform itself. This identity can then be granted specific, limited permissions (e.g., “_read-only access to the database credential_“) in the secrets vault. Your MCP server authenticates using this identity, retrieves the secrets it needs at runtime, and never has to handle long-lived credentials in its own configuration.

This architecture enables you to treat secrets as dynamic, short-lived resources rather than static configuration. You can implement startup validation to fail fast when required secrets are missing and builtin runtime secret rotation capabilities. All your static secrets, such as API keys, can be easily and quickly refreshed without server downtime, dramatically reducing the window of opportunity for an attacker.

Finally, the principle of least privilege is critical at scale. Each instance of your MCP server should only have access to the secrets it absolutely needs for its specific tasks. This compartmentalization limits the blast radius of any single compromised instance, containing the potential damage.

### Observability and monitoring

Building scalable and secure MCP servers implies that you have full visibility into their operations. That means that you need effective observability, having full access to a combination of logs, metrics, and traces.

**Structured logging** forms the foundation. The key is consistency across request boundaries. When an AI agent makes a complex request that triggers multiple tool calls or external API interactions, a unique correlation ID should be attached to every log entry. This lets you trace the entire journey through your logs, from the initial request to the final response.

Beyond basic logs, **distributed tracing** provides a detailed, hop-by-hop view of a request’s lifecycle. Using standards like [OpenTelemetry](https://opentelemetry.io/), you can visualize how a request flows through your MCP server and any downstream services it calls. This is invaluable for pinpointing performance bottlenecks, like if a specific tool invocation is taking too long.

**Security event logging** deserves special attention in MCP servers because they’re high-value targets. Every authentication attempt, authorization failure, and unusual access pattern should be captured with enough context for future forensic analysis. This isn’t just compliance theater; it’s your early warning system for attacks in progress.

In turn, **metrics collection** should focus on the signals that matter: request latency (because AI agents have short attention spans), error rates (especially for authentication and authorization), and resource utilization. You should also implement a dedicated health endpoint that provides a simple up/down status, allowing load balancers and orchestration systems to automatically manage server instances.

Finally, all this data is useless without **alerting and visualization**. Set up automated alerts to notify you when key metrics cross critical thresholds (e.g., a sudden spike in `HTTP 500` errors). Create dashboards that provide an at-a-glance view of your MCP server’s health, performance, and security posture. The goal is to gain end-to-end visibility that helps you detect and diagnose emerging issues before they impact users at scale.

Take this with you
------------------

Building secure and scalable MCP servers requires attention to authentication, authorization, and deployment architecture. The patterns in this guide will give you a head start in creating reliable MCP servers that can handle sensitive tools and data.

When building on top of a fast-paced technology like MCP, it’s key that you start with security as a foundation, not an afterthought. The MCP specification provides basic security primitives, and modern cloud platforms provide the infrastructure to scale them.

Want to dive deeper? Check out the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) and recommended [security best practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) for complete technical details.

**Want to dive deeper?**Check out the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) and recommended [security best practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) for complete technical details.

Written by
----------

![Image 1: Den Delimarsky](https://avatars.githubusercontent.com/u/53200638?v=4&s=200)

Principal Product Manager

Related posts
-------------

We do newsletters, too
----------------------

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address
