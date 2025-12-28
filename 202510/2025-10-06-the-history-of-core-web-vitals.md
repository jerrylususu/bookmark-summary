# The History of Core Web Vitals
- URL: https://addyosmani.com/blog/core-web-vitals/
- Added At: 2025-10-06 06:41:19

## TL;DR
Core Web Vitals 是 Google 推出的核心网页体验评估指标，涵盖加载速度（LCP）、交互响应（FID）和视觉稳定性（CLS）。它作为搜索排名因素之一，促进开发者优化网站性能，提升了整体网络速度和用户体验。通过工具支持和数据开放，该指标成为衡量和推动网站性能的重要标准。

## Summary
Core Web Vitals（核心网页指标）是衡量网站性能以评估用户体验的关键指标，由Google发起并推广，旨在推动开放网络朝着更快、更稳定的方向发展。

**1. 背景与动机**
- 早期Google已经将网站速度和用户体验视为网络核心原则，2010年Google搜索开始使用桌面端网站速度作为轻量级排名信号。
- 2015年，Google推出AMP（Accelerated Mobile Pages）以提升移动页面加载速度，但它是一个封闭框架，引发了开放性和灵活性担忧。
- 2018年，Google扩展性能关注，推出移动搜索的“Speed Update”，并强调速度是页面质量的一部分。
- 最终，Google决定转向开放网络性能指标，与Chrome和搜索团队合作，定义了一套用户中心、可测量的公开标准，即Core Web Vitals，目标是为任何网站提供统一的性能评估，无需依赖特殊框架。

**2. Core Web Vitals的定义与组成**
- 2020年5月正式推出，包括三大指标：
  - **Largest Contentful Paint (LCP)**：衡量加载速度，关注主要内容渲染时间，目标值为2.5秒内（第75百分位）。
  - **First Input Delay (FID)**：衡量交互响应性，关注用户首次输入延迟，目标值为100毫秒内（第75百分位）。
  - **Cumulative Layout Shift (CLS)**：衡量视觉稳定性，关注布局偏移，目标值低于0.1（第75百分位）。
- 这些指标基于广泛用户研究，强调与用户感知（如加载时间低于2-3秒可避免挫败感）和业务成果（如减少24%的页面中途放弃率）的相关性。
- Google确保指标标准化、开放，并通过WICG和Web性能标准组织发布规范，同时提供开源JavaScript库和Chrome扩展工具，便于开发者测量。

**3. 页面体验与搜索排名**
- Google搜索将Core Web Vitals纳入“Page Experience”信号，于2021年6月（移动端）和2022年2月（桌面端）更新排名算法。
- Page Experience结合了Core Web Vitals、移动友好性、HTTPS安全性和无侵入性插页广告，作为排名因素之一。内容相关性仍优先，但Core Web Vitals可在相似内容中作为决胜因素。
- 重要变化：移动端Top Stories不再要求AMP，任何符合页面体验标准的开放网页均可入选，降低了AMP的依赖性。
- Google提供Search Console报告，帮助网站所有者监控指标表现。

**4. 工具与数据支持**
- **Chrome UX Report (CrUX)**：自2017年存在，提供真实用户性能数据，支持查询LCP、FID和CLS，并通过BigQuery、API和仪表板公开访问。
- 开发者工具集成：Lighthouse、Chrome DevTools和PageSpeed Insights更新以突出Core Web Vitals，提供诊断和改进建议。
- 第三方工具支持：多个RUM服务商（如Akamai、New Relic）和网络提供商（如Cloudflare）集成指标，使监控普及化。
- 数据驱动进步：公开指标促进了生态竞争，整体网络性能稳步提升。

**5. 影响与改进成果**
- Chrome团队优化浏览器性能，包括：
  - 内容优先级调整，提升LCP。
  - 增强Back/Forward Cache (BFCache)，实现即时导航。
  - 推出Prerender2，预渲染页面以减少LCP。
  - 网络和调度优化，如指针按下预连接，改善响应性。
  - 渲染和JavaScript引擎改进，如RenderingNG架构和cookie访问优化。
- 成果：2023年，Chrome页面加载平均快166毫秒，节省用户超10,000年加载等待时间和1,200年输入响应时间。符合“良好”标准的流量比例从约33%提升至68%（桌面）和64%（移动）。
- 商业效益：企业通过优化Core Web Vitals提升了收入和用户参与度，累计节省用户超30,000年等待时间（截至2025年）。

总体而言，Core Web Vitals通过标准化指标、工具支持和生态协作，显著推动了网络性能优化，提升了全球用户体验。
