Title: 连字（Ligature）那些事儿

URL Source: https://webzhao.me/posts/ligature/

Markdown Content:
连字（也称合字，英文为 Ligature）是字体和排版里面的一个概念，在 Web 页面上我们使用的并不多。因此，对于大多数前段开发者来说，这可能还是一个陌生的概念。

连字（Ligature）到底是什么？
------------------

我们在学校阅读 pdf 格式的英文论文时候，可能会注意到如果字母 f 如果和字母 i 出现在一块，会被“合体”显示成 ﬁ（注意：这是一个字符）。其实，不光 f 和 i 会这样，还有很多情况两个甚至三个字符会合体：

```
fl  → ﬂ
ff  → ﬀ
ffi → ﬃ
ffl → ﬄ
ae  → æ (音标)
```

还有两个我们很熟悉的字符，其实也是连字而来的：`&` 和 `W` 字母 W 则来源于两个 u 或 v 的组合。你想一下，W 的读音是不是很像 `double-u`。而在法语中，W 的读音则和 `double-v` 完全一致。

那么，为什么要将多个字母连起来成一个字符呢？这还要从公元前说起。在印刷出现之前，文字主要是用来手写的（当然也可能是雕刻什么的）。人们发现，在最早的楔形文字手写本中就已经含有很多连写字符。中世纪的拉丁文手写本中，誊写僧人为加快速度将字符连写，诞生了很多手写连字，如在哥特体中，带右圈的字母（b, o,和 p）和带左圈的字母（c, e, o, d, g 和 q）的圈部都被重叠书写。14 世纪的手写本中含有很多这种手写连字。

从视觉上，连字可以让整个排版更流畅一些，减少冲突感。比如字母 f 和 i 连在一起的时候，f 的右上角和 i 顶上的圆点会紧挨着，有一些冲突。而将它们合体成 ﬁ 之后，会自然一些。

![Image 1: typography of coffin](https://webzhao.me/assets/ligature/coffin.png)

在活字印刷出现后，很多手写的连字被直接制造在一个铅字模上。

![Image 2: sort](https://webzhao.me/assets/ligature/sort.jpg)

从 20 世纪 50 年代起，随着 [瑞士设计风格](https://en.wikipedia.org/wiki/International_Typographic_Style) 的盛行以及 [无衬线体](https://zh.wikipedia.org/wiki/%E6%97%A0%E8%A1%AC%E7%BA%BF%E4%BD%93) 的广泛使用，以及照排技术的出现，连字逐渐很少被使用。早期的电脑排版也都没有支持连字，字体也不支持（TeX 是个例外）。因为当时的电脑主要是英文系统，不支持连字也没有什么影响。

随着电脑多语言的支持以及现代字体技术的发展，连字也逐渐恢复了使用。

在电脑上支持连字
--------

在电脑上，将多个字母合体成一个是如何实现的呢？在早期的排版软件（比如 TeX）里面，程序会自动把可以连字的组合（比如 f 和 l）替换成单个的连字（ﬂ）。在 [OpenType](https://zh.wikipedia.org/wiki/OpenType) 字体格式出现后，字体开发者可以在字体中定义连字。OpenType 格式的字体可以设置一个 [字符替换表（GSUB - The Glyph Substitution Table）](https://www.microsoft.com/typography/otspec/gsub.htm) 来指定哪些字符的组合会被替换成其它字符。

当然，使用 OpenType 字体的程序需要支持 ligature 特性并开启它之后才能看到效果。

下图是 Apple Pages 软件的截图，左边文字使用默认配置开启了连字，而右边的没有。请注意对比一下字母 T 和 h 结合处的不同。

![Image 3: apple pages](https://webzhao.me/assets/ligature/pages.png)

其它文字编辑、排版或设计软件也大多支持连字。Microsoft Office 从 2010 版本开始也支持这个特性，只不过没有默认开启，需要你自己 [设置一下](https://support.office.com/zh-cn/article/-%E5%AD%97%E4%BD%93-%E5%AF%B9%E8%AF%9D%E6%A1%86%E4%B8%AD%E7%9A%84-OpenType-%E9%80%89%E9%A1%B9-1033d3a7-511a-4d77-a2e2-d10d32889e28)。

CSS 中的 Ligature
---------------

在网页上启用连字，需要在最新版本的浏览器中才能实现。`font-variant-ligatures` 是 [CSS Fonts Module Level 3](https://drafts.csswg.org/css-fonts-3/) 草案中新增加的一个 CSS 属性，它可以控制内容是否启用连字以及启用哪些类型的连字。

在详细介绍 `font-variant-ligatures` 属性之前，我们先要了解一下 OpenType 中定义的连字类型。

**标准连字（common）**

常用连字或者标准连字就是我们最常见的 f 和 l、i 等字母的连字。当然，不同的字体定义的标准连字也不完全一样。在 OpenType 中，使用 `liga` 这个特性标记表示标准连字。

**上下文连字（contextual）**

也称为上下文替换字。当某个字母和其它特定字母相邻时，它会被替换成另一种书写形式，以便看起来使书写线条更连贯。对比下图中的两行文字，其中第二行开启了上下文替换：

![Image 4: contextual](https://webzhao.me/assets/ligature/clig.png)

我们可以看到，单独的字母 o 是只有一个圈的形状。在开启了上下文替换时，它被显示成另外一种书写形式，即头上多了一个向右的线条。

**自由连字（discretionary）**

自由连字有时候也翻译为酌情连字，比标准连字风格更强，更具有装饰性。`Th`、`ck`、`ct`、`st`等字母的组合形成的连字经常被划分为自由连字。

![Image 5: discretionary](https://webzhao.me/assets/ligature/dlig.png)

**历史连字（historical）**

历史连字是那些在曾经使用过，但现在已经很少使用了的连字。比如德语中的 `tz` 曾被书写为 `ß`。

![Image 6: tz](https://webzhao.me/assets/ligature/hlig.png)

在了解连字的类型之后，CSS3 中的 `font-variant-ligatures` 属性就很容易理解了。它可以有如下的取值：

*   `normal`：默认值，开启标准连字和上下文连字。
*   `none`：不开启任何连字。
*   `common-ligatures` / `common-ligatures`：开启或关闭标准连字。
*   `discretionary-ligatures` / `no-discretionary-ligatures`：开启或关闭自由连字。
*   `historical-ligatures` / `no-historical-ligatures`：开启或关闭历史连字。
*   `contextual` / `no-contextual`：开启或关闭上下文连字（替换）。

`font-variant-ligatures` 属性可以同时指定以上两个或多个值，比如：

```
p {
  font-variant-ligatures: common-ligatures discretionary-ligatures;
}
```

除了 `font-variant-ligatures`，也可以通过 `font-feature-settings` 属性来设置连字以及其它 OpenType 特性。不过这个属性比较底层，可以设置一些不常用的高级特性。W3C 的规范也是建议开发者尽量避免使用 `font-feature-settings`，而使用 `font-variant` 系列的属性代替。

`font-variant-ligatures` 属性在浏览器支持程度方面还是不错的，Chrome 31、Firefox 34 和 IE 10 以上版本都可以很好地支持。当然，在浏览器中展示连字的前提是你使用的字体是支持 OpenType 的连字特性的。

连字和图标字体
-------

图标字体的使用现在已经非常普遍了。尤其是 [FontAwesome](http://fontawesome.io/) 这样的图标库，使用起来那是相当的方便。但是图标字体有两个小问题：

1.  一般的图标字体使用一个空标签来代替图标，语义性差一些。比如使用 FontAwesome 显示一个“编辑”图标，需要写一个无意义的 `<i class="fa fa-pencil-square-o" aria-hidden="true"></i>`。
2.  用来渲染成图标的字符，一般都是超出正常文字编码范围的 UTF8 字符。当图标所使用的字体不能被正确加载时，会显示空白或乱码。

其实，连字可以和图标字体完美结合起来。想象一下，你在 HTML 中书写 `<i class="icon">edit</i>`，而它使用的字体把 `edit` 四个字母连字成一个字符，而这个字符渲染出来就是一个编辑图标。这样你的 HTML 不再是无意义的，而且字体加载失败时，文字会展示出来。

Google 有一套图标库 [Material Icons](https://google.github.io/material-design-icons/) 就是按照这个思路实现的：

![Image 7: material icons](https://webzhao.me/assets/ligature/md.png)

编程字体中的连字
--------

连字除了能在网页上使用，用它来展示代码也挺不错的。在编程语言中，`==`、`!===` 、`=>` 这些符号组合可以使用连字更形象、简洁地展示出来。对比下图中左右两段代码，右边代码的阅读起来是不是更容易呢？

![Image 8: code](https://webzhao.me/assets/ligature/code.png)

右边一段代码使用了 [FiraCode](https://github.com/tonsky/FiraCode) 字体，并且编辑器也支持连字功能。类似的字体还有 [Monoid](http://larsenwork.com/monoid/)、[Hasklig](https://github.com/i-tu/Hasklig) 等。

总结
--

连字（Ligature）是为了书写的方便及阅读的流畅而把多个字符连成了一个字符。在互联网时代，我们不仅可以使用连字提高（英文）网页的可读性，还可以用它来做字体图标等有意思的事情。

在中文领域，连字虽然现在没什么实际应用，但是仔细想想，很多汉字的产生本身就是几个字合体的结果，比如「圕」字。

参考链接：

*   [https://helpx.adobe.com/typekit/using/open-type-syntax.html](https://helpx.adobe.com/typekit/using/open-type-syntax.html)
*   [http://blog.justfont.com/2013/10/why-stick-together/](http://blog.justfont.com/2013/10/why-stick-together/)
*   [https://zh.wikipedia.org/zh-cn/%E5%90%88%E5%AD%97](https://zh.wikipedia.org/zh-cn/%E5%90%88%E5%AD%97)
