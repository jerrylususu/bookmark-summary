# Smarter than 'Ctrl+F': Linking Directly to Web Page Content
- URL: https://alfy.blog/2024/10/19/linking-directly-to-web-page-content.html
- Added At: 2024-12-14 13:51:15
- [Link To Text](2024-12-14-smarter-than-'ctrl+f'-linking-directly-to-web-page-content_raw.md)

## TL;DR
文本片段允许精确链接到网页中的特定文本，无需ID。通过特殊URL语法，浏览器可解析并高亮显示目标文本。该功能在主流浏览器中支持，但样式和行为略有差异。未来期待更多AI系统使用此功能，并希望浏览器提供更便捷的生成方式。

## Summary
1. **历史背景**：
   - 过去，链接网页的特定部分需要该部分具有ID，并通过URL的片段标识符（ID）进行链接。

2. **文本片段的引入**：
   - 文本片段（Text fragments）是一项现代Web平台功能，允许精确链接到网页中的特定文本，无需添加锚点。
   - 该功能通过`::target-text` CSS伪元素提供样式支持。

3. **文本片段的工作原理**：
   - 通过在URL末尾附加特殊语法，浏览器解析并搜索指定文本，滚动到该文本并高亮显示。
   - 如果用户按Tab键导航文档，焦点将移动到文本片段后的下一个可聚焦元素。

4. **文本片段的语法**：
   - 基本语法：`https://example.com/page.html#:~:text=[prefix-,]textStart[,textEnd][,-suffix]`
   - 包含前缀、文本开始、文本结束和后缀，帮助浏览器在多个匹配中找到正确的文本。

5. **示例**：
   - 单个文本片段：链接到“without relying on the presence of IDs”。
   - 文本范围：链接到“using particular”到“don’t control”之间的文本。
   - 多个文本片段：通过使用`&`符号链接多个文本片段。

6. **隐藏内容的行为**：
   - 如果链接的文本片段位于隐藏内容中（如`until-found`属性的元素或关闭的`<details>`元素），内容将自动显示。
   - 该功能目前仅在Google Chrome中支持。

7. **样式化高亮片段**：
   - 使用`::target-text`伪元素可以自定义高亮文本的样式，支持颜色、背景色、文本装饰等属性。

8. **浏览器支持与回退行为**：
   - 文本片段在所有主流浏览器中支持，`::target-text`伪元素在Safari中尚未完全支持。
   - 如果不支持该功能，页面将正常加载，但不进行高亮或滚动。

9. **浏览器高亮样式的差异**：
   - 不同浏览器的高亮颜色和样式有所不同，Safari的高亮区域更大，覆盖整个行高。

10. **功能检测**：
    - 使用`document.fragmentDirective`检测浏览器是否支持文本片段功能。

11. **个人见解**：
    - 作者最初通过Google搜索结果了解到文本片段，认为它是Chrome的专属功能，后来发现它是开放的Web标准。
    - 希望该功能能被更多生成式AI系统使用，提供精确的上下文链接。
    - 期待浏览器提供内置功能，使非技术人员也能轻松生成文本片段链接。

12. **更新**：
    - 2024年10月20日，发现Chromium浏览器已内置生成文本片段链接的功能，用户可以通过右键菜单的“复制高亮链接”选项实现。

13. **附加资源**：
    - 提供了多个与文本片段相关的技术文档和资源链接，包括W3C草案、MDN文档、CSSWG草案和CanIUse支持情况。
