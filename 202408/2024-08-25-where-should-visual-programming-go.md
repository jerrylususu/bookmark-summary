# Where Should Visual Programming Go?
- URL: https://tonsky.me/blog/diagrams/
- Added At: 2024-08-25 06:32:27
- [Link To Text](2024-08-25-where-should-visual-programming-go?_raw.md)

## TL;DR
文章讨论了图表在编程中的应用，提出不应完全替代代码，而应在适当的地方添加图形以增强理解和代码清晰化。通过不同级别的图表与代码关系（从独立存在到图表即代码），探讨了图表与代码的最佳结合方式。最终建议图表应作为与文本并存的独立工具，而不是替代品，并强调某些情况下图表比代码更有用。

## Summary
1. **引言**：
   - 引用Sebastian Bensusan的文章“We need visual programming. No, not like that.”，强调不应完全替代代码，而应在适当的地方添加图形。
   - 作者分享个人对图表的喜爱，认为图表有助于理解和代码的清晰化。

2. **图表示例**：
   - 按钮状态图：展示按钮状态和转换的复杂性。
   - 图片上传组件图：说明错误处理的重要性。

3. **图表与代码的关系**：
   - **级别0**：图表独立存在
     - 图表在单独的工具中绘制，用于辅助代码编写，可能存放在wiki上供他人查看。
     - 缺点：难以发现，容易过时。
   - **级别1**：图表与代码并存
     - 提出将图像嵌入文本文件的想法，当前最佳实践是将图表以文本形式描述。
     - 缺点：仍可能过时，且在终端环境中不适用。
   - **级别2**：图表由代码生成
     - 代码和图表共存，图表由代码生成，IDE可以实现这一点。
     - 优点：始终更新，不侵入代码存储。
     - 缺点：可能不够直观，自动布局困难。
   - **级别3**：图表即代码
     - 认为某些事物用文本表示更好，某些则用图形，应根据具体情况混合使用。
     - 举例Luna语言，尝试双表示法，即一切既是代码也是图表。
     - 认为文本编码应保持文本形式，但应能跳转到图表工具绘制状态机并执行。

4. **结论**：
   - 图表不应替代或“增强”文本，而应作为与文本并存的独立工具。
   - 提出类似Godot或Unity的游戏引擎概念，可以在其中编写正常文本代码，也可以创建和编辑场景。
   - 强调不是要图形化编码，而是要思考哪些类型的图表比代码更有用，并能直接执行。

5. **非目标**：
   - 不是要图形化编码或使用无代码平台，有时代码本身更好。
   - 建议在wiki上放置图表，以帮助队友理解。
