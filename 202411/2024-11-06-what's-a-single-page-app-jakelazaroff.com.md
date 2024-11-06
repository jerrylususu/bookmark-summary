# What's a Single-Page App? | jakelazaroff.com
- URL: https://jakelazaroff.com/words/whats-a-single-page-app/
- Added At: 2024-11-06 14:12:54
- [Link To Text](2024-11-06-what's-a-single-page-app-jakelazaroff.com_raw.md)

## TL;DR
文章讨论了单页应用（SPA）的定义和技术实现，包括服务器端渲染（SSR）、客户端渲染（CSR）、多页应用（MPA）等。介绍了传统Web框架、JavaScript框架、元框架和岛屿框架的优缺点，强调工具应提供灵活性，避免开发者被锁定在特定架构中。

## Summary
1. **单页应用定义**：
   - 单页应用（SPA）通常被定义为使用大量JavaScript来提升用户体验的网站，通过显示加载指示器来实现。
   - 这种定义带有讽刺意味，反映了大多数人使用的实际定义，即“单页应用”通常是“JavaScript框架应用”的委婉说法。

2. **技术讨论**：
   - **htmx与SPA**：作者使用htmx构建了一个单页应用，并讨论了htmx与单页应用并非对立的观点。
   - **渲染光谱**：Thomas Broyer的文章将渲染分为多个层次，包括服务器端渲染（SSR）、客户端渲染（CSR）等。

3. **渲染与导航定义**：
   - **服务器端渲染（SSR）**：HTML在服务器上生成并发送到浏览器。
   - **客户端渲染（CSR）**：HTML在客户端生成并应用于DOM。
   - **多页应用（MPA）**：点击链接或提交表单时，浏览器会用全新的文档替换当前页面。
   - **单页应用（SPA）**：浏览器不会用新文档替换页面，而是通过客户端DOM操作进行所有更改。

4. **工具与架构**：
   - **传统Web框架和静态站点生成器**：包括WordPress、Django、Rails（pre-Turbolinks）、Jekyll、Hugo、Eleventy等，属于服务器端渲染的多页应用。
     - **优点**：浏览器处理重要可访问性功能，内容在CSS或JavaScript加载失败时仍可见，页面加载更快。
     - **缺点**：每次导航都需要下载和替换整个页面，每次交互都需要网络往返。
   - **JavaScript框架**：如Backbone、Angular 1、React（自定义Webpack设置），属于客户端渲染的单页应用。
     - **优点**：初始页面加载更快，页面导航即时，元素在导航间持久化，UI修改无需网络请求。
     - **缺点**：客户端需要下载100%的UI代码，初始页面加载慢，导航默认不可访问，搜索引擎索引困难。
   - **JavaScript元框架**：如Next.js、Remix、SvelteKit、Nuxt和Solid Start，结合了服务器端和客户端渲染。
     - **优点**：解决了客户端渲染SPA的冷缓存初始页面加载和SEO问题。
     - **缺点**：UI在JavaScript加载前可能无用。
   - **岛屿框架**：如Astro、Deno Fresh和Enhance，结合了服务器端渲染和客户端交互。
     - **优点**：减少静态部分的复杂性，提供更好的开发者控制。
   - **部分交换**：如htmx、Unpoly和Turbo，通过HTTP请求服务器渲染的HTML片段插入页面。
     - **优点**：更容易替换页面细粒度区域，创建服务器端渲染的SPA。

5. **总结**：
   - 讨论了不同架构的优缺点，强调了工具不应将开发者锁定在特定区域，而是应提供灵活性。
