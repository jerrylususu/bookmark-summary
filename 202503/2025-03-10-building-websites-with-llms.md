# Building Websites With LLMS
- URL: https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/
- Added At: 2025-03-10 14:06:23
- [Link To Text](2025-03-10-building-websites-with-llms_raw.md)

## TL;DR
本文提出LLMS网站构建方法，通过多小HTML页面结合CSS过渡技术替代复杂JavaScript交互，简化开发并提升体验。案例显示，用静态生成独立页面管理过滤与导航功能，减少代码且维护更易，更适合静态网站，虽存在跳转局限但更简洁直观，符合Web粒度特性。

## Summary
本文提出了“LLMS（Lots of Little HTML Pages）”的网站构建方法，通过创建多个小的独立HTML页面结合CSS视图过渡技术，简化开发并提升体验。作者反思了过去依赖JavaScript构建页面内交互的做法，认为其复杂度高且维护困难。通过两个案例验证了新方法的优势：

1. **过滤功能重构**  
   原计划通过JavaScript动态筛选内容列表，但发现逻辑复杂（如需处理多个`data`属性和排序），转而用静态生成器创建独立HTML页面，每种筛选结果对应独立页面。通过CSS过渡实现页面间平滑切换，减少代码量并获得更好效果。

2. **导航与搜索重构**  
   将传统JavaScript弹出式导航菜单改为链接到独立的“菜单页面”，用CSS过渡实现视图切换，搜索功能同样采用页面跳转替代JS动态注入。此举省去交互逻辑编写，且便于维护。

作者强调这种方法的核心优势：利用网页基础架构（如链接跳转）和现代CSS技术（视图过渡），避免复杂的客户端JavaScript，尤其适合静态网站。虽然存在页面间跳转等局限，但整体实现更简洁直观，符合Web“粒度”特性——将交互视为独立页面间的自然过渡。
