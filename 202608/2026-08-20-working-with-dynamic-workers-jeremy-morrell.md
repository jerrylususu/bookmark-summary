# Working with Dynamic Workers | Jeremy Morrell
- URL: https://jeremymorrell.dev/blog/working-with-dynamic-workers/
- Added At: 2026-08-20 13:52:09
- Tags: #read #guide #deepdive

## TL;DR
Cloudflare推出Dynamic Workers，可在隔离沙箱中安全运行用户代码，避免eval的线程、内存和网络风险。它支持CPU限制、禁用网络、自定义绑定及对象能力控制，并提供日志捕获，让普通Web应用低成本实现用户可编程扩展。

## Summary
这篇文章介绍了 Cloudflare 新推出的 **Dynamic Workers** 这一基础能力，它可以让开发者以极低成本、快速且安全地运行用户提交的任意代码。作者的重点不是它在 AI Agent 上的应用，而是如何用它让普通 Web 应用变得“可编程”——把一部分逻辑交给最终用户去写，同时还能保证服务本身的安全和稳定。

## 与传统 `eval()` 的区别

文章一开始就用对比的方式说明 Dynamic Workers 不是简单的 `eval()`。`eval()` 有几个致命问题：

1. **共享执行线程**：`eval("while (true) {}")` 会直接卡死整个服务，无法从外部中断。
2. **共享内存**：用户代码可以无限分配内存，拖垮服务器。
3. **访问外部作用域**：`eval` 能读写调用位置的局部变量，甚至篡改计费逻辑。
4. **可访问网络**：用户代码可以向外发送任意数据，造成数据泄露。

而 Dynamic Workers 运行在 Cloudflare Workers 的隔离环境中，经过多年大规模安全加固，天然规避了以上问题。每个 Dynamic Worker 都是独立、轻量、有严格资源限制的沙箱。

## 基本工作方式

使用 Dynamic Workers 非常简单，核心是一个 `LOADER.load()` 调用：

```js
const worker = env.LOADER.load({
  compatibilityDate: "2026-06-28",
  mainModule: "src/index.js",
  modules: {
    "src/index.js": `
      export default add(a, b) {
        return a + b;
      };
    `,
  },
});

let response = worker.getEntrypoint().add(1, 2);
```

你只需要把用户代码以模块形式传入，就能获得一个可调用的 Worker 入口。调用一次或成千上万次都可以，成本低、启动快。

## 实际应用示例：可编程网页抓取

作者构建了一个示例场景：一个网页抓取服务，系统负责抓取网页内容，然后让用户提供一个 **transform 函数**，对抓取到的 HTML、响应头、状态码等进行处理，返回 Markdown 或 JSON。

用户的函数签名大致如下：

```ts
export default async function transform(env, input) {
  // 用户自定义处理逻辑
}
```

其中 `input` 包含 URL、最终 URL、状态码、响应头、响应体等。系统用一段 **harness（外壳）代码** 包裹用户代码，统一调用入口，方便后续添加日志、权限等逻辑。

这个场景下，用户可以写各种有趣的转换：

- 用正则提取 Open Graph 元标签（用于社交分享预览）。
- 引入 npm 包（如 `defuddle`）把 HTML 转成 Markdown。
- 处理非 HTML 内容，比如把 Hacker News 的 Algolia API 响应转成高分评论摘要。

这些例子说明用户有能力写相当复杂的逻辑，不再局限于固定选项。

## 资源限制与安全控制

Dynamic Workers 允许在加载时设置 CPU 时间限制和禁用网络：

```js
const worker = env.LOADER.load({
  // ...
  globalOutbound: null,       // 禁用 fetch
  limits: { cpuMs: 50 },      // CPU 时间上限
});
```

因此，用户代码中的死循环会在 50ms 后被终止，尝试 `fetch` 会失败。这保证了平台不会被滥用。

## 向用户代码传递自定义绑定（Bindings）

只返回一个值有时不够，用户可能需要访问存储或其他服务。作者展示了如何把自定义工具传入用户函数。

最简单的做法是把 Cloudflare 的 KV 命名空间直接传进去：

```ts
const userEnv = { KV: getKVForUser(env.USER_ID) };
return transform(userEnv, input);
```

用户代码里就能像使用普通 KV 绑定一样调用 `env.KV.get(...)`。

更精细的做法是包装 KV，加上调用次数限制，每次调用都经过一个计数器：

```ts
function wrapKV(kv, maxOperations = 5) {
  let operations = 0;
  function consume() {
    if (operations >= maxOperations) throw new Error("limit exceeded");
    operations++;
  }
  return Object.freeze({
    async get(key) { consume(); return kv.get(key); },
    async put(key, value) { consume(); return kv.put(key, value); },
    async delete(key) { consume(); return kv.delete(key); },
  });
}
```

这样用户只能使用你暴露的方法，而且每次运行共享一个调用预算。这种控制如果放在 HTTP 代理层做会非常困难，因为难以关联到单次运行。

## 更安全的设计：对象能力（OCaps）

作者认为直接给用户受限的 `fetch` 仍然有风险，因为用户可能想尽办法绕过限制。更好的思路来自**对象能力（Object Capabilities）**：不提供“可以请求任意 URL”的能力，而是只提供“访问当前页面中出现的特定 URL”的能力。

具体做法是：系统解析用户抓取的 HTML 页面，提取其中出现的链接，为每个链接生成一个 `ResourceCapability` 对象，放进 `env.resources` 这个只读 Map 中。用户代码只能通过这个 Map 获取某个 URL 的资源，且该 URL 必须在原始页面中出现过。

用户代码示例：

```ts
const article = env.resources?.get(articleUrl);
if (!article) {
  throw new Error(`The page did not grant access to ${articleUrl}`);
}
const response = await article.read();  // read() 不接受 URL，对象本身已绑定 URL
```

这样即使用户知道其他 URL，也无法访问，因为能力没有授予。系统还可以在 `read()` 内部加入速率限制、抓取次数限制等。

这种方式本质上限制了用户的“能力面”，而不是试图过滤用户的每一次请求。作者提到，让他感到惊喜的是，如果告诉 LLM “从 OCaps 角度思考”，生成的 API 设计质量会高很多。

## 日志与可观测性

用户代码需要调试，他们会大量使用 `console.log`。但平台的日志不能直接暴露给用户。Dynamic Workers 支持 **tail worker**，可以在创建 Worker 时附加一个 tail：

```js
const tail = ctx.exports.LogTailer({ props: { runId } });

const worker = env.LOADER.load({
  // ...
  tails: [tail],
});
```

tail worker 会收到该 Worker 产生的所有日志和未捕获异常，然后可以把它们存入一个 Durable Object，最终在返回结果前收集并展示给用户。这样用户代码完全不需要修改，其 `console.log` 就能被平台捕获。

## 总结

Dynamic Workers 提供了一种新的抽象：你可以把“运行用户代码”作为平台的一个基础功能，而不是靠 `eval` 或笨重的容器。它具备：

- 轻量、快速、可大规模创建
- 强安全边界，避免 `eval` 的各种问题
- 可配置 CPU 限制和网络禁用
- 可传递自定义绑定，甚至设计为对象能力模型
- 内建日志捕获机制

适合构建“用户可编程”的 Web 应用，例如可定制的网页抓取器、数据处理管道等。作者认为这将开启一类新的应用形态，让终端用户能够以安全、受控的方式扩展平台功能。
