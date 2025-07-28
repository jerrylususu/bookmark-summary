# The many, many, many JavaScript runtimes of the last decade
- URL: https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/
- Added At: 2025-07-28 14:09:59
- [Link To Text](2025-07-28-the-many,-many,-many-javascript-runtimes-of-the-last-decade_raw.md)

## TL;DR


过去十年，JavaScript通过多样化运行时和引擎扩展应用场景。在边缘计算领域，Cloudflare Workers、Deno、Bun等竞相推出；微控制器则依赖Duktape、JerryScript等轻量引擎；React Native和Electron主导原生应用开发；多语言引擎如Graal.js推动跨平台整合。趋势显示，引擎解耦与多样性驱动JavaScript生态扩展至边缘设备、物联网及多硬件平台，成为通用开发语言。

## Summary


过去十年中，JavaScript 运行时和引擎的多样化发展显著扩展了其应用场景，从边缘计算、微控制器到跨平台原生应用。以下是关键领域的总结：

---

### **边缘计算（Edge Computing）**
- **初期探索**：Akamai 2002年首次尝试边缘计算（Java/.NET），Node.js 2009年推动服务器端 JavaScript，AWS Lambda 2014年引入 Node.js 伺服器less，2017年 Lambda@Edge 将 Node.js 带入边缘。
- **竞争格局**：
  - **Cloudflare Workers**（2017）：基于 Service Worker API 的轻量级运行时，主打低延迟边缘计算，迅速获得市场认可。
  - **Deno**（2018）：2021年成立公司 Deno Land，并推出边缘计算服务 Deno Deploy，挑战 Cloudflare 领域。
  - **Bun**（2022）：获700万美元融资，推出边缘计算服务及 CI/CD 工具，采用 JavaScriptCore 引擎。
  - **Wasmer**（2023）：推出 WinterJS（SpiderMonkey）和 Wasmer Edge，扩展边缘计算选项。
  - **AWS LLRT**（2024）：基于 QuickJS 的低延迟边缘运行时，但尚未提供边缘工作服务。
- **引擎多样性**：V8（Deno/Cloudflare）、JavaScriptCore（Bun）、SpiderMonkey（WinterJS）、QuickJS（LLRT）等引擎在边缘场景中竞逐。

---

### **微控制器（Microcontrollers）**
- **硬件限制**：RAM 有限（如3美分的微控制器仅几十字节），需极轻量级引擎。
- **关键引擎**：
  - **Duktape**（2013）、**JerryScript**（2014）、**Moddable**（2018）等，均在64 KB RAM 以下运行，牺牲性能换取资源效率。
- **运行时衍生**：
  - **IoT.js**（JerryScript 支持物联网）、**low.js**（基于 Duktape 的轻量级 Node.js 重构）。
- **目标场景**：智能家电、传感器等低功耗设备的 JavaScript 控制。

---

### **多语言引擎（Polyglot Engines）**
- **JVM 集成**：
  - **Rhino**（1997）：首个 Java 生态 JavaScript 引擎，支持双向互操作，后被 Nashorn（2014，JDK 8）取代，再由 Graal.js（2018）继承。
  - **Graal.js**：支持 Node.js 全栈，并通过 GraalVM 实现跨语言优化。
- **其他语言生态**：
  - **C#**：Jint（2013）。
  - **Python**：PyNarcissus、jispy。
  - **JavaScript 自制引擎**：Narcissus（2007）、Porffor（2023，基于 WebAssembly 的高性能实现），部分获技术领袖支持（如 Chris Wanstrath）。

---

### **原生应用（Native Apps）**
#### **Web 视图（WebView）框架**
- **移动端**：
  - **PhoneGap/Cordova**（2009）：被 40 多万开发者采用，后开源为 Apache Cordova，并衍生 Ionic 框架。
  - **Capacitor**（2019，Ionic 团队）：针对桌面优化的 WebView 框架，支持插件化 API。
- **桌面端**：
  - **Electron**：源自 NW.js（2012），主流桌面应用框架，用于 Discord、VS Code 等。
  - **NW.js**：基于 Chromium 与 Node.js，持续开发但 Electron 更具主导地位。
- **智能电视**：Cordova 支持 Tizen/Samsung 等平台，TVMLKit JS（Apple TV）非基于 WebView。

#### **React Native**
- **移动端崛起**：
  - 2015 年由 Facebook 发布，以“原生渲染+JS 脚本”结合闻名，2023 年占据顶级 iOS 应用的30%市场份额。
  - **Hermes 引擎**（2019）：针对移动端优化，2022 年成默认引擎，计划用 Static Hermes 实现 C++ 级性能。
  - **多引擎支持**：通过 JSI 和 Node-API 适配 V8/JSC/QuickJS 等。
- **桌面与电视**：Windows/macOS 支持有限，Electron 主导桌面主流；React Native 在智能电视（如 tvOS/Android TV）应用广泛。
- **竞争框架**：
  - **NativeScript**（2014）：支持 V8/JSC，通过 Node-API 接口扩展引擎兼容性，但市场份额小（未入 Top 100 iOS 应用）。
  - **Node.js 移动端**：Janea Systems 的 Node.js Mobile（2017）和 Samsung 的 Lightweight Node.js，但主要用于工具链而非 UI 开发。

---

### **Node.js 扩展**
- **移动端尝试**：
  - **Node-ChakraCore/SpiderNode**（2017-2018）：因 iOS 禁用 JIT 需要，采用无 JIT 引擎变体。
  - **JITless V8**（2020 后）：使 Node.js 兼容 iOS，但未显著影响 React Native。
- **原生平台绑定库**：
  - macOS（NodObjC、NativeScript）、Windows（NodeRT）、Qt（NodeGUI）等库推动 Node.js 与原生 UI 框架整合。

---

### **趋势总结**
- **多样性驱动**：特定场景（边缘计算、低功耗设备）推动全新运行时与引擎涌现。
- **引擎解耦**：跨语言互操作（如 Graal.js）与多引擎支持（React Native/Node-API）使 JavaScript 更易嵌入复杂系统。
- **生态扩张**：从 Web 扩展至智能设备、电视、嵌入式系统，JavaScript 成为跨硬件通用语。
