Title: 让你的 RSS/Atom feed 更好看

URL Source: https://taxodium.ink/pretty-feed.html

Markdown Content:
如果你是 RSS feed，只要在你的 XML 文件开头引入 [pretty-feed-v3.xsl](https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl)，你就可以得到一个好看的 HTML feed 页面了。[3](https://taxodium.ink/pretty-feed.html#fn.3)

<?xml version="1.0" encoding="UTF-8"?\>
<!-- 添加这行 XML 样式表，引用 pretty-feed-v3.xsl --\>
<?xml-stylesheet href="/home/static/styles/pretty-feed-v3.xsl" type="text/xsl"?\>
<!-- 你原来的 RSS 内容 --\>
<rss xmlns:atom\="http://www.w3.org/2005/Atom" xmlns:content\="http://purl.org/rss/1.0/modules/content/" version\="2.0"\></rss\>

如果你是 Atom feed，你需要修改一下 [pretty-feed-v3.xsl](https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl)，你可以参考 [我的实现](https://github.com/Spike-Leung/taxodium/blob/org-publish/publish/styles/pretty-feed-v3.xsl)，或者看看 [相关 issue](https://github.com/genmon/aboutfeeds/issues/26)。

用到的技术是 [xml-stylesheet](https://www.w3.org/TR/xml-stylesheet/) 和 [XSLT(eXtensible Stylesheet Language/Transform)](https://developer.mozilla.org/en-US/docs/Web/XML/XSLT/Guides/Transforming_XML_with_XSLT/An_Overview)。

如果你熟悉 HTML，我们可以做一个类比。

`<?xml-stylesheet href="some.xsl" type="text/xsl"?>` 就相当于 `<link rel="stylesheet" href="some.css">` , 作用是引用一个样式表。

[xml-stylesheet](https://www.w3.org/TR/xml-stylesheet/) 引用的样式表有自己的规则，但整体来说它很像 HTML，你也可以在里面写 HTML 标签，用 <style\> 写样式。

它也像一个模版，用 HTML 写模版，而数据则通过 [XSLT](https://developer.mozilla.org/en-US/docs/Web/XML/XSLT/Guides/Transforming_XML_with_XSLT/An_Overview) 从你的 RSS / Atom feed 的 XML 中读取，例如读取标题，作者，文章标题，发布时间，文章总结等。

如果你只是想美化一下，你基于现有的文件修改就好了：[4](https://taxodium.ink/pretty-feed.html#fn.4)

*   适用 RSS feed： [Matt Webb's pretty-feed-v3.xsl](https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl)
*   使用 Atom feed：[Spike Leung's pretty-feed-v3.xsl](https://github.com/Spike-Leung/taxodium/blob/org-publish/publish/styles/pretty-feed-v3.xsl)

如果你嫌麻烦，也可以用 [RSS.Beauty](https://github.com/ccbikai/RSS.Beauty)，但自己写的话，定制化会更高，如果你还有更好的方法欢迎分享。
