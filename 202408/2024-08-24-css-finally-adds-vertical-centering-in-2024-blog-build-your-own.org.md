# CSS finally adds vertical centering in 2024 | Blog | build-your-own.org
- URL: https://build-your-own.org/blog/20240813_css_vertical_center/
- Added At: 2024-08-24 11:23:27
- [Link To Text](2024-08-24-css-finally-adds-vertical-centering-in-2024-|-blog-|-build-your-own.org_raw.md)

## TL;DR
2024年，CSS通过`align-content`属性实现默认布局中的垂直居中，支持Chrome、Firefox和Safari。新特性简化了垂直居中的实现，无需flexbox或grid布局。历史上有多种垂直居中方法，如表格单元格、绝对定位等。二维对齐涉及`align-content`、`justify-content`等属性，CSS轴术语解释了块轴和内联轴。CSS设计复杂，命名不佳，需额外努力掌握。

## Summary
1. **CSS垂直居中更新**：2024年，CSS终于通过`align-content`属性实现了默认布局中的垂直居中，只需一个CSS属性即可实现。

2. **支持情况**：
   - Chrome: 123
   - Firefox: 125
   - Safari: 17.4

3. **新特性**：
   - 不再需要使用flexbox或grid布局，只需一个CSS属性即可实现垂直居中。
   - 内容无需包裹在div中。

4. **垂直居中的历史**：
   - **方法1：表格单元格**：使用display: table和display: table-cell实现，但需要额外的CSS间接实现。
   - **方法2：绝对定位**：通过相对定位和绝对定位结合transform实现，但方法复杂且不易理解。
   - **方法3：行内内容**：利用伪元素和行内块元素实现，但存在零宽度“strut”字符的问题。
   - **方法4：单行flexbox**：使用flexbox的单行模式，通过align-items或justify-content实现。
   - **方法5：多行flexbox**：在多行flexbox中，使用align-content实现。
   - **方法6：网格内容**：使用grid布局，通过align-content实现。
   - **方法7：网格单元格**：通过align-items实现，注意与align-content的区别。
   - **方法8：自动外边距**：在flow布局中使用margin:auto实现水平居中，但不适用于垂直居中。
   - **方法9：2024年的新方法**：直接使用align-content实现垂直居中。

5. **二维对齐**：
   - **对齐属性对比**：
     - `align-content`：在不同布局中的作用不同，如flow布局中为块轴，flexbox中为交叉轴，grid中为块轴。
     - `justify-content`：在flow布局中无效果，flexbox中为主轴，grid中为内联轴。
     - `align-items`和`justify-items`：在不同布局中的作用不同。
   - **CSS轴术语**：解释了块轴和内联轴的概念，以及它们与文本方向的关系。
   - **命名问题**：讨论了`align-*`和`justify-*`属性的命名逻辑及其在不同布局中的应用。

6. **CSS设计的困惑**：
   - CSS有数百个命名不佳的属性，每个属性都可能以 unintuitive 的方式影响结果。
   - 对比了Unix的正交、可组合原语与CSS的复杂性。
   - 强调了掌握CSS需要额外努力，并推荐了一个视觉指南来帮助理解CSS的难点。
