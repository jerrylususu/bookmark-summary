# Quick and dirty bar-charts using HTML's meter element
- URL: https://shkspr.mobi/blog/2025/10/quick-and-dirty-bar-charts-using-htmls-meter-element/
- Added At: 2025-10-11 13:08:53

## TL;DR
这篇文章介绍了一种利用HTML的`<meter>`元素和CSS的`writing-mode`属性创建简易垂直条形图的轻量级方法。该方法无需依赖外部库，支持样式定制和交互，简单实用但样式较为基础。

## Summary
这篇文章介绍了一种使用HTML的`<meter>`元素快速制作简单垂直条形图的方法。作者Terence Eden旨在避免依赖第三方库、外部CSS或SVG，以实现轻量级解决方案。

文章首先说明了`<meter>`元素的基本用法，例如通过`min`、`max`和`value`属性设置范围，但其样式化选项有限，且浏览器支持不佳。初始尝试使用CSS的`transform: rotate(-90deg)`旋转元素会导致布局问题，需调整原点或包裹`<div>`来修复，但过程繁琐。

关键解决方案来自Marius Gundersen的建议：使用CSS的`writing-mode`属性设置垂直书写方向，使条形图垂直显示而水平排列，形成条形图效果。该方法支持基本样式，如根据值范围设置颜色和背景色，并增强了可访问性（优于栅格图像），同时可通过JavaScript交互。

作者总结认为，对于快速、简易的条形图需求，这种方法实用且有效，尽管外观简陋但功能足够。
