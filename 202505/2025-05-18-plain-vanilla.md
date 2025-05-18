# Plain Vanilla
- URL: https://plainvanillaweb.com/index.html
- Added At: 2025-05-18 11:38:45
- [Link To Text](2025-05-18-plain-vanilla_raw.md)

## TL;DR


文章介绍了通过原生Web技术开发Web应用的方法，主张用Web Components实现组件化、原生CSS处理样式、静态部署网站及纯JS构建SPA，避免框架和构建工具带来的复杂性。认为现代浏览器支持已足够支撑复杂开发，这种"零依赖"方案适合有基础的开发者长期维护。

## Summary


该网站介绍了一种基于纯HTML、CSS和JavaScript开发网页及应用的“无构建工具、无框架”方法，核心内容由四大主题构成：

1. **组件化开发**  
通过Web Components（自定义元素、阴影DOM等标准技术）构建模块化组件，替代React或Vue框架的组件体系，实现功能复用与封装。

2. **现代CSS styling**  
利用CSS原生功能（如CSS变量、Calc()、自定义属性继承等）直接进行样式管理，无需依赖CSS Modules、PostCSS或SASS等工具，提升样式灵活性与浏览器兼容性。

3. **静态网站搭建**  
基于Web Components构建无需服务器端逻辑的静态项目，通过简单部署工具（如HTTP服务器或静态托管服务）直接上线，省去构建配置复杂度。

4. **单页应用开发**  
使用纯JS实现SPA路由管理和状态控制，依赖History API、Fetch API等标准，而非框架提供的虚拟DOM或状态管理库。

**核心价值主张**：  
牺牲框架的短期便利性，换取长期维护的简洁性，因为现代浏览器对Web标准的支持已足够支撑复杂功能，而传统框架会导致工具链臃肿和持续更新负担。适合有基础的前端开发者进阶，新手可先学习基础教程（如The Odin Project或MDN文档）。

**推荐学习路径**：  
以[Web Components](https://plainvanillaweb.com/pages/components.html)为起始点，逐步掌握原生实现组件化、样式管理、路由控制及状态管理的技术。
