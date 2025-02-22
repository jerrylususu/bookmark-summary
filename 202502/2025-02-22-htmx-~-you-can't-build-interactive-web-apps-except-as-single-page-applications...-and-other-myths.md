# </> htmx ~ You Can't Build Interactive Web Apps Except as Single Page Applications... And Other Myths
- URL: https://htmx.org/essays/you-cant/
- Added At: 2025-02-22 11:04:14
- [Link To Text](2025-02-22-htmx-~-you-can't-build-interactive-web-apps-except-as-single-page-applications...-and-other-myths_raw.md)

## TL;DR
文章探讨了多页面应用（MPA）和HTMX在现代浏览器中的应用，反驳了MPA性能差、不能离线操作等常见误解。通过使用Service workers、Speculation Rules API等技术，MPA可以实现高效的页面切换和离线功能，用户体验不亚于单页应用（SPA）。

## Summary
1. **背景介绍**：
   - 作者在Reddit和YCombinator上经常看到开发者讨论技术栈选择，总有人认为不使用SPA框架（如React或AngularJS）就无法构建高质量的应用程序。
   - 作者在两年前构建一个[observability平台](https://apitoolkit.io/)时，选择了使用HTMX的多页面应用（MPA）方法，并发现服务器渲染的MPA在注意细节的情况下可以表现出色。

2. **常见MPA的误解**：
   - **误解1：MPA页面切换慢**：
     - 原因是每次页面导航时都会下载JavaScript和CSS，但浏览器在过去十年中已经做了显著改进。
     - 使用库如PJAX、Turbolinks和HTMX Boost可以劫持页面重新加载，只交换HTML的body部分，减少资源重新下载。
     - 通过Service workers进行客户端缓存，可以进一步优化页面切换速度，减少DOMContentLoaded事件时间。
   - **误解2：MPA不能离线操作**：
     - Service workers可以缓存所有内容，使应用完全离线操作。
     - 可以使用Workbox配置离线场景，支持离线POST请求并在网络恢复后重试。
   - **误解3：MPA在页面切换时总是闪白**：
     - 自2019年起，大多数浏览器在页面切换时不再闪白，因为浏览器会等待所有必要资源加载完毕或超时后才绘制页面。
   - **误解4：MPA不能实现复杂的跨文档页面切换动画**：
     - Chrome 126引入了跨文档视图转换（cross-document view transitions），可以使用CSS或CSS+JavaScript实现复杂的页面切换动画。
   - **误解5：使用HTMX或MPA时，所有用户操作必须在服务器端进行**：
     - 这并不完全正确，HTMX和MPA用户仍然可以在适当的地方使用JavaScript、Alpine或Hyperscript。
   - **误解6：直接操作DOM很慢，因此应该使用React/虚拟DOM**：
     - 虚拟DOM操作在某些复杂应用中可能更快，但对于大多数应用来说，直接DOM操作并不会显著影响性能。
   - **误解7：每个小的交互都需要编写JavaScript**：
     - 随着浏览器技术的进步，许多交互可以通过HTML和CSS实现，例如使用HTML输入复选框和标签来显示/隐藏内容。

3. **Service workers的应用**：
   - Service workers是浏览器的内置功能，可以在用户和服务器之间拦截请求，决定如何处理这些请求。
   - 通过Service workers缓存资源，可以显著减少页面加载时间，实现平滑的用户体验。
   - 使用Workbox库可以自动生成Service workers，简化配置过程。

4. **Speculation Rules API**：
   - Speculation Rules API用于优化未来导航的性能，允许开发者指定哪些链接应预取或预渲染。
   - 通过配置Speculation Rules，可以实现即时页面导航。

5. **组件岛架构**：
   - 在需要高度交互性的情况下，可以使用组件岛架构，结合WebComponents或JavaScript框架（如React、Angular等）来实现特定部分的应用程序交互。

6. **结论**：
   - 2024年的浏览器已经吸取了SPA框架的许多优点，使得使用HTML、CSS和少量JavaScript就可以构建高度交互的、甚至离线的Web应用程序。
   - 浏览器的进步使得MPA和HTMX等技术在用户体验上并不逊色于SPA框架。
