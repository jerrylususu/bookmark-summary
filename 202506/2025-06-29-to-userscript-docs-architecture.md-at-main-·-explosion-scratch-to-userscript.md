# to-userscript/docs/architecture.md at main · Explosion-Scratch/to-userscript
- URL: https://github.com/Explosion-Scratch/to-userscript/blob/main/docs/article.md
- Added At: 2025-06-29 11:27:22
- [Link To Text](2025-06-29-to-userscript-docs-architecture.md-at-main-·-explosion-scratch-to-userscript_raw.md)

## TL;DR


to-userscript通过环境模拟技术（Proxy/定制存储）、消息总线及资源内联等方法，将浏览器扩展自动转换为无依赖的用户脚本，支持跨浏览器兼容性并最小化原代码修改。其采用多语言支持及API补丁机制，解决作用域、通信和资源嵌入问题，实现浏览器扩展到用户脚本的自动转换方案。

## Summary


转换浏览器扩展为用户脚本的工具to-userscript开发过程及技术要点：

1. **核心目标**  
   - 将浏览器扩展转换为用户脚本时最小化修改原始代码  
   - 最大限度保持功能性并兼容多种浏览器  
   - 生成无依赖且尽可能简洁的vanilla JavaScript代码  

2. **环境模拟技术**  
   - 使用Proxy和定制存储对象（customStorage）实现全局变量（chrome/brower对象）的动态绑定  
   - 通过with语句创建polyfill作用域，支持扩展中定义的全局变量和对象  
   - 自动向window/globalThis等全局对象同步变量值以确保兼容性

3. **消息通信机制**  
   - 设计内部消息总线(internalMessagingBus)处理内容脚本与后台脚本通信  
   - 采用模板系统分离不同组件的通信方式：  
     - userscript模板处理主逻辑  
     - postmessage模板用于选项/弹出窗口与父页面通信  
     - handle_postmessage监听器将消息转发到真实runtime

4. **资源内联处理**  
   - 创建EXTENSION_ASSETS_MAP存储所有静态资源：  
     - 文本资源直接存储内容  
     - 二进制资源转为Base64编码  
   - 自动替换CSS中@import和url()引用为内联数据  
   - 处理选项页面的srcdoc注入安全问题，防止</script>标签截断

5. **多语言支持**  
   - CLI参数指定locale，过滤非目标语言的资源  
   - 在生成的选项页面HTML中注入对应语言文件  
   - 确保语言资源整合到不同模板组件中

6. **扩展特性适配**  
   - 选项/弹出页面单独生成iframe模板，集成必要的API polyfill  
   - 处理后台脚本的嵌套polyfill需求，通过字符串构建逐步应用  
   - 补丁机制解决不兼容特性：  
     - 替换不被GM认可的content_security_policy内容  
     - 处理webRequest等无法polyfill的API的降级方案

7. **工具使用流程**  
   ```bash
   # 安装工具
   bun install -g to-userscript
   # 通过URL转换扩展
   to-userscript convert "https://chrome.google.com/webstore/detail/..." --minify -o my-script.user.js
   # 直接下载Firefox附加组件
   to-userscript download "https://addons.mozilla.org/en-US/firefox/addon/..."
   ```

该实现通过系统化解决变量作用域、跨域通信、资源嵌入等核心问题，为浏览器扩展到用户脚本的自动转换提供了可行方案。
