# What's the best way to do authentication in modern applications
- URL: https://neciudan.dev/most-secure-way-to-store-auth-token
- Added At: 2026-07-26 06:31:38
- Tags: #read #deepdive #security

## TL;DR
前端身份验证应将令牌优先存于httpOnly Cookie（配合Session），而非localStorage，以防XSS窃取。同时需防御CSRF、采用BFF架构或OAuth拆分存储，将凭证尽量隐藏于服务端，并结合refresh token轮换与设备绑定，最大限度缩小泄露风险。

## Summary
在讨论现代应用的身份验证时，前端令牌存在哪一直是争议焦点。最常见的做法是把 JWT 放进 localStorage，然后每次请求用 `Authorization: Bearer <token>` 发出去。这种方式简单又能跨域，但它有一个致命问题：任何能在你页面上运行的 JavaScript（包括正常依赖、第三方脚本，以及攻击者注入的 XSS 代码）都可以直接读取 `localStorage`，一行代码就把 token 偷走。攻击者拿到 token 后可以在自己电脑上随时冒充用户，一直到 token 过期为止。

有人会说“如果攻击者已经能在你的页面执行 JS，那他们本来就能做任何事，保护 token 没用”。作者指出这混淆了两种攻击面：如果能**读取** token，攻击者能把凭证带回家，在任意时间、任意地点继续攻击；但如果无法读取 token（比如 token 在 httpOnly 的 cookie 里），攻击者就只能在当前浏览器标签页存活期间，经由你的服务器发起请求，这样你的服务器还能通过限流、日志和检测来发现异常。所以安全的目标是减小爆炸半径——让 JavaScript 读不到 token。

**内存存储：治标不治本**  
把 token 存在变量里（而非 localStorage）能增加攻击难度，因为变量不像 localStorage 是公开可枚举的。但攻击者仍可以劫持 `window.fetch`，当你的代码把 token 加到请求头时窃取它。更麻烦的是，刷新页面或打开新标签页变量就丢了，用户必须重新登录。引入 refresh token 似乎能解决这个问题，但如果把 refresh token 也放在 JS 可触及的地方，安全又回到原点。

**httpOnly cookie + session：防御升级**  
彻底方案是把凭证存在浏览器里 JavaScript 无法触达的地方——`httpOnly` 的 cookie。设置 `Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax; Path=/` 后，cookie 只能由浏览器自动附加到请求里，任何脚本都读不到。前端代码变得更简单，连 token 都不用自己管理。

然而，cookie 引入了新的威胁：CSRF（跨站请求伪造）。攻击者可以在第三方网站构造指向你域名的表单并自动提交，浏览器会自动带上你的登录 cookie。解决 CSRF 可以靠三道防线：

1. **CSRF Token**：服务器在页面生成一个随机 token（可读 cookie），前端在发起状态变更请求时把它放到自定义头（如 `X-CSRF-Token`）中，服务器比对 cookie 和请求头是否一致。外部网站无法读取不同源的页面，所以拿不到 token。
2. **SameSite 属性**：设置 `SameSite=Lax`（或 `Strict`）能让浏览器默认不跨站发送 cookie。但要注意 Lax 对顶级 GET 导航例外，因此绝不能让 GET 请求更改数据；另外 SameSite 是以“站点”为单位，同站不同子域之间它不起作用。
3. **源检查**：利用浏览器自动添加的 `Origin` 或 `Sec-Fetch-Site` 头，服务器拒绝非同源的变更请求。

最佳实践是把 session cookie 命名为 `__Host-session`，这会强制安全属性，浏览器会确保它仅 HTTPS、不设域、路径为根。

**为什么用 Session 而不是 JWT**  
JWT 的核心卖点是无状态：服务器不用查数据库就能验证用户。但无状态意味着无法撤销——用户登出、改密码或账号被封，已发出的 JWT 在其过期前依然有效。为了实现撤销，你不得不在服务端维护一个撤销列表，每次请求还得查一次，这恰恰又回到了有状态会话，而且还多了更大的 token 体积。相反，传统的 session 机制（cookie 存随机字符串，服务端查库获取用户信息）天然支持即时登出和权限变更，每次请求都拿到最新状态。那微乎其微的数据库查询开销，对绝大多数应用来说根本不构成瓶颈。

JWT 的真正用武之地在于微服务间传递身份或者单点登录（SSO）这类场景：多个服务不用共享数据库就能各自验证用户身份。

**OAuth 中的拆分模式**  
在 OAuth 场景下，我们无法选择 token 格式，但可以合理安排存储：短时效的 access token（5-15分钟）存在内存里，长时效的 refresh token 放在 `httpOnly` cookie，且通过 `Path=/api/refresh` 限制该 cookie 仅发往刷新端点。配合**refresh token 轮换（rotation）**——每次使用 refresh token 后服务端都生成一个新的，并将旧的作废——如果攻击者偷到了一个 refresh token 并用它换到了新 token，正常用户的客户端稍后也会尝试使用那个已被消耗的旧 token，服务端检测到同一链条的重用，就立刻吊销整条链，迫使攻击者和用户都重新登录。

**React 中的实际封装**  
在 React 等前端应用中，应当封装一个统一的请求函数 `api()`。当检测到 401 时，自动调用刷新接口获取新 token 并重试。关键是要防止多个并发请求同时触发刷新：用一个全局的刷新 Promise，让所有需要刷新的请求都等待同一个 Promise，避免 refresh token 因并发被误判为重用攻击。

**BFF：终极浏览器安全架构**  
最安全的模式是后端前置（BFF）：在浏览器与真实 API 之间加一层薄服务。前端只持有一个平凡的 httpOnly session cookie，该 cookie 对应 BFF 服务器上保存的真实 OAuth token。浏览器任何请求都经 BFF 代理，BFF 负责用存于服务端的 token 去调用真实 API，并返回结果。这样浏览器这一生都不会接触到任何 token，彻底杜绝前端窃取。而且 BFF 作为机密客户端可以使用更强的 OAuth 授权码流程，而纯浏览器端属于公开客户端，安全性较弱。代价是需要额外的基础设施和稍高延迟。

**新威胁：信息窃取木马**  
以上的所有防护都假设攻击者在浏览器范围内。但现实中，窃密木马可以直接读取用户硬盘上的 cookie 数据库，绕过 `httpOnly` 限制，把完整 session cookie 盗走。这种“传递 cookie”攻击在 2025 年已经增长 72%。为了对抗这种威胁，出现了**设备绑定会话凭证（DBSC）**：浏览器登录时在 TPM 等硬件安全芯片中生成无法导出的私钥，session cookie 短期有效，续期时需要浏览器用该私钥签名挑战请求。这样即使 cookie 被盗，几分钟后也会过期，攻击者因为没有硬件密钥而无法续期，cookie 立即作废。目前 Chrome 146 等已经开始支持。

**总结**  
对于现代单页应用，安全从高到低依次是：  
- 将 token 完全藏在服务端（BFF + httpOnly session cookie + CSRF 防护 + 设备绑定）
- OAuth 拆分存储（access token 在内存，refresh token 在 httpOnly cookie + 轮换）
- 纯 httpOnly session cookie + session 机制
- 避免使用 localStorage 或直接暴露 token 给 JS

同时要始终注意 CSRF 防御、绝不让 GET 改变状态、登录及权限提升时重新生成 session ID，以及紧跟设备绑定等新标准，才能最大程度降低凭证泄露风险。
