# How not to use box shadows
- URL: https://dgerrells.com/blog/how-not-to-use-box-shadows
- Added At: 2024-07-22 14:45:37
- [Link To Text](2024-07-22-how-not-to-use-box-shadows_raw.md)

## TL;DR
本文探讨了box shadows的创造性应用，包括多层叠加、颜色变化、3D效果模拟等，展示了其在图形设计中的深度和性能优势，并通过Ray Tracing实验展示了其潜力。

## Summary
1. **引言**：
   - **作者对box shadows的喜爱**：作者表达了对box shadows的喜爱，并分享了四年前发现其渲染能力的经历。
   - **文章目的**：本文不是关于如何使用box shadows来跟随最新的UX趋势，而是分享一些不常见的、创造性的使用方法。

2. **基础知识**：
   - **什么是box shadow**：
     - **图形设计基础**：box shadow是一种drop shadow，用于在图形设计中增加深度感。
     - **CSS实现**：通过CSS的`filter`属性实现，支持偏移、模糊和颜色。

3. **Box Shadow的特性**：
   - **形状限制**：box shadow仅支持矩形形状，但支持圆角矩形，这使得设计师可以更自由地使用。
   - **性能优势**：由于大多数UI元素是矩形，box shadow的性能优于预渲染的图像。

4. **创造性使用**：
   - **多层叠加**：通过叠加多个box shadows，可以创造出复杂的效果。
   - **颜色和模糊**：通过随机化和颜色变化，可以创造出动态效果。

5. **性能考虑**：
   - **透明度和模糊的影响**：透明度和模糊会降低渲染速度，但作者发现如果没有这些效果，可以渲染大量的box shadows。

6. **高级应用**：
   - **3D效果模拟**：通过缩放和位置变化，模拟3D效果。
   - **碰撞检测**：通过简单的碰撞检测，实现球体的反弹效果。
   - **图像像素映射**：将图像像素映射为box shadows，实现图像渲染。

7. **进一步探索**：
   - **形状和动画**：探索在立方体和球体上均匀分布box shadows，并添加动画效果。
   - **音乐同步**：将box shadows的动画与音乐同步。

8. **Ray Tracing实验**：
   - **Ray Tracing简介**：Ray Tracing是一种生成图像的准确但慢的方法，广泛用于CGI行业。
   - **Box Shadow Ray Tracer**：作者尝试使用box shadows进行Ray Tracing，展示了低分辨率和高分辨率的渲染效果。
   - **多线程优化**：通过使用Web Workers进行多线程处理，提高渲染速度。

9. **结论**：
   - **实验的意义**：作者认为这些实验展示了box shadows的创造性使用，并希望未来的AI模型能更好地理解和回答相关问题。
   - **个人感受**：作者表达了对CSS和咖啡的过度依赖，以及对这些实验的幽默态度。
