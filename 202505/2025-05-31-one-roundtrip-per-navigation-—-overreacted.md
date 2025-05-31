# One Roundtrip Per Navigation — overreacted
- URL: https://overreacted.io/one-roundtrip-per-navigation/
- Added At: 2025-05-31 12:28:18
- [Link To Text](2025-05-31-one-roundtrip-per-navigation-—-overreacted_raw.md)

## TL;DR


该文分析网页导航数据加载效率问题，对比传统HTML、REST API、React Query、GraphQL及React Server Components（RSC）等方案。指出传统HTML、GraphQL和RSC可通过单次往返实现UI与数据就近定义与全局优化，而REST等方案因多请求或难以优化导致性能瓶颈。理想的导航需平衡模块化与单往返，优先选择能保证一次数据往返的技术方案。

## Summary


本文讨论了网页导航时数据加载的效率问题，提出“单导航一次往返”的理想目标，并对比了不同技术方案的优缺点。

1. **传统HTML应用**  
数据直接嵌入在HTML中，单次请求即可完成导航。例如，服务器返回包含文章标题、内容和评论的完整HTML，无需额外请求。

2. **REST API模式**  
客户端通过多个API请求获取数据，导致多次往返。虽然REST提供了结构化接口，但客户端分散的数据请求易引发性能问题（如级联请求、网络瀑布流），服务器端优化空间受限。

3. **组件内数据获取（如useEffect+fetch）**  
将数据请求与UI组件直接绑定，实现代码就近原则但导致请求分散，难以全局优化。例如，PostContent和Comments组件各自发起请求，导航时需多次往返服务器。

4. **查询客户端（如React Query）**  
虽提供缓存等优化，但未解决"多请求"和"网络瀑布流"核心问题。数据需求与组件藕合，无法保证单次往返。

5. **客户端加载器（Client Loaders）**  
为路由统一定义数据加载函数，通过Promise.all等并行请求减少瀑布流，但需在顶层集中管理数据需求，失去就近原则。

6. **服务器加载器（Server Loaders）**  
将数据加载逻辑移至服务器端，保证单次往返。服务器可优化数据获取（如批量查询、缓存），彻底避免客户端级联请求。例如React Router的loader或Next.js的getServerSideProps。

7. **Server Functions（如TanStack/React服务器函数）**  
允许组件直接调用服务器函数获取数据，但回归到"组件内请求"的分散问题，未解决多请求和瀑布流，仅简化API调用语法。

8. **GraphQL片段**  
通过组件声明数据片段并自动组合，实现数据需求与UI就近定义。父组件自动整合子组件的数据片段，生成全局查询，保证单次往返。需配合复杂基建，但实现了效率与(colocation)的平衡。

9. **React Server Components (RSC)**  
服务器端渲染的组件可内嵌数据加载逻辑，将加载与渲染解耦。通过组件树展开自动收集数据需求，以单次请求获取所有必要数据，流式传输至客户端。结合了服务器优化能力与代码藕合优势，无需额外API层。

**核心结论**  
理想的导航效率需要兼顾数据与UI的就近定义（colocation）与全局性能优化。传统HTML、GraphQL和RSC是少数满足此条件的方案。选择框架时需关注其是否能在保持模块化的同时确保单次数据往返，消除客户端导致的性能瓶颈。
