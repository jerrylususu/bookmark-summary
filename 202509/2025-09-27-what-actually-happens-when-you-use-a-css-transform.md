# What actually happens when you use a CSS transform
- URL: https://alastair.is/learning-about-what-happens-when-you-use-a-css-transform/
- Added At: 2025-09-27 03:24:07

## TL;DR
CSS transform通过创建独立图层并启用硬件加速来提升动画性能，避免频繁重绘，但需注意避免滥用导致内存增加。这是解决Web动画性能的关键机制。

## Summary
本文探讨了CSS `transform` 属性的渲染机制及其对性能的影响。核心发现如下：

1.  **transform 的功能与副作用**  
    `transform` 不仅用于旋转、缩放等变换，还会默认创建新的“堆叠上下文”，导致元素层级（z-index）发生变化，即使未显式设置。这是CSS规范明确规定的行为。

2. **浏览器渲染机制**  
    浏览器（以WKWebView为例）采用“分块渲染”（tiled rendering）方式，将页面划分为多个“瓦片”（tiles）进行绘制。普通CSS属性（如`top`、`left`）的动画会触发频繁的瓦片重绘，导致性能低下。

3. **transform 的性能优势原理**  
    - 当应用 `transform`（尤其是3D变换）或设置 `will-change: transform` 时，浏览器会为元素创建独立的原生图层（如iOS的`CALayer`）。  
    - 该图层由硬件加速的图形框架（如Core Animation）直接处理，动画通过原生系统（如`CAKeyFrameAnimation`）执行，无需重复绘制整个屏幕，从而显著提升性能。

4. **注意事项**  
    滥用硬件加速（如全局设置 `will-change`）可能导致内存开销增加，需权衡性能与资源消耗。后续文章将深入讨论内存管理问题。

总结：CSS transform 通过触发硬件加速机制，将动画交由原生系统处理，实现了接近原生应用的流畅性能，但其使用需结合具体场景优化。
