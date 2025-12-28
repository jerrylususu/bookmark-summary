# 让你的 RSS/Atom feed 更好看
- URL: https://taxodium.ink/pretty-feed.html
- Added At: 2025-04-24 13:29:47

## TL;DR


通过Pretty-FEED-V3.XSL样式表文件可美化RSS/Atom订阅源显示。在XML文件头部添加关联指令，利用XSLT技术将数据转换为HTML模板，支持动态展现标题、作者等信息。RSS用户可直接使用原始版本，Atom需采用定制版（GitHub可获取），也可尝试替代工具RSS.Beauty。此方法实现订阅源页面的可视化设计，提升阅读体验并支持灵活自定义。

## Summary


1. 通过引入Pretty-FEED-V3.XSL文件美化订阅源显示：  
   - 在RSS XML开头添加`<?xml-stylesheet>`指令引用样式表，修改默认展示格式；  
   - Atom用户需先调整该XSL文件，参考作者实现或相关讨论，适配Atom的XML结构。  

2. 核心技术为XML样式表（xml-stylesheet）和XSLT：  
   - 类似HTML的CSS链接，通过XML处理指令关联样式文件；  
   - XSLT技术可将XML数据转换为HTML模板，支持直接编写HTML标签和CSS样式，动态提取标题、作者等内容。  

3. 提供两种现成方案：  
   - RSS用户可直接使用`genmon`的原始版本，Atom用户使用作者定制的修改版（附GitHub链接）；  
   - 提到替代工具RSS.Beauty，但推荐自行修改XSL便于充分定制。  

4. 总结：通过XSLT实现订阅源页面的可视化设计，提升易读性与美观度，可根据需求灵活调整。
