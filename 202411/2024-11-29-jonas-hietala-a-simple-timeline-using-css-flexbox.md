# Jonas Hietala: A simple timeline using CSS flexbox
- URL: https://www.jonashietala.se/blog/2024/08/25/a_simple_timeline_using_css_flexbox/
- Added At: 2024-11-29 14:59:01
- [Link To Text](2024-11-29-jonas-hietala-a-simple-timeline-using-css-flexbox_raw.md)

## TL;DR
作者在更新个人网站时，利用CSS的flexbox特性创建了一个简单的时间线，列出了生活中的重要事件。通过HTML结构和CSS样式，实现了时间线的线条、事件标记和内容的对齐，并使用媒体查询实现了响应式布局。

## Summary
1. **背景介绍**：
   - 作者在更新个人网站的“/now”和“/about”页面时，决定在“/about”页面添加一个时间线元素，以列出生活中的重要事件。
   - 使用CSS的flexbox特性创建时间线，发现这一过程并不复杂。

2. **时间线示例**：
   - 1989年：出生于瑞典北部。
   - 2006年：接触到Visual Basic。
   - 2008年8月：与Veronica在一起。

3. **HTML结构**：
   - 使用两个包装器（`timeline`和`events`）围绕不同的事件（`event`）。
   - 每个事件包含一个事件标记（`svg`）和内容（`time`和`text`）。

4. **CSS样式**：
   - **时间线线条**：
     - 使用`::before`伪元素在`events` div上模拟线条，设置宽度和高度。
     - 设置`events` div为相对定位，以确保线条从容器顶部开始。
   - **事件标记**：
     - 使用flexbox使事件内容水平排列（圆圈在左，内容在右）。
     - 通过相对定位调整圆圈的位置，使其更好地对齐。
   - **垂直间距**：
     - 使用`row-gap`属性在事件之间添加间距，避免在最后一个事件下方添加不必要的空白。

5. **响应式设计**：
   - **大屏幕布局**：
     - 使用媒体查询（`@media`）在大屏幕上将线条居中，并将一些事件移到左侧，一些移到右侧。
     - 通过调整`flex-direction`和`text-align`属性实现左右对齐。

6. **总结**：
   - 使用flexbox可以相对简单地创建一个基本的时间线，这是作者最喜欢的CSS特性之一，因为它简化了过去非常复杂的问题。

7. **完整CSS代码**：
   - 包括时间线线条、事件标记、内容对齐、颜色样式等。
   - 使用媒体查询实现响应式布局，确保在大屏幕上时间线居中，事件左右对齐。
