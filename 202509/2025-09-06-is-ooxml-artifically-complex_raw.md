Title: Is OOXML Artifically Complex?

URL Source: https://hsu.cy/2025/09/is-ooxml-artificially-complex/

Published Time: 2025-09-05T00:00:00+00:00

Markdown Content:
Sep. 5, 2025

*   [OOXML as a Sloppy Standard](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#ooxml-as-a-sloppy-standard)
*   [Why Microsoft’s Motive Wasn’t Deliberate Sabotage](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#why-microsofts-motive-wasnt-deliberate-sabotage)
*   [Conclusion](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#conclusion)

*   [引言](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#%E5%BC%95%E8%A8%80)
*   [为什么说 OOXML 是一个潦草的标准](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%AF%B4-ooxml-%E6%98%AF%E4%B8%80%E4%B8%AA%E6%BD%A6%E8%8D%89%E7%9A%84%E6%A0%87%E5%87%86)
*   [为什么说微软的动机并非蓄意破坏竞争](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%AF%B4%E5%BE%AE%E8%BD%AF%E7%9A%84%E5%8A%A8%E6%9C%BA%E5%B9%B6%E9%9D%9E%E8%93%84%E6%84%8F%E7%A0%B4%E5%9D%8F%E7%AB%9E%E4%BA%89)
*   [结语](https://hsu.cy/2025/09/is-ooxml-artificially-complex/#%E7%BB%93%E8%AF%AD)

* * *

A while ago, the official blog of LibreOffice published a provocative [article](https://blog.documentfoundation.org/blog/2025/07/18/artificially-complex-xml-schema-as-lock-in-tool/): “An artificially complex XML schema as a lock-in tool.” Its target is Microsoft’s XML-based file formats — the Office Open XML (OOXML).

The article alleges that, although Microsoft put its Office formats through standardization, the spec is engineered to be so complex that it obstructs interoperability with third-party software. Moreover, the complexity is allegedly gratuitous and disconnected from real-world needs; it’s like advertising an “open” railway system while designing the signaling so only one manufacturer can run trains. Users, the argument continues, often accept proprietary technology uncritically, which makes it easy for Microsoft to lock people into its ecosystem.

A quick refresher: historically, Office used binary formats (`.doc`, `.xls`, and `.ppt`) whose contents weren’t human-readable. Starting with Office 2007, Microsoft switched the defaults to `.docx`, `.xlsx`, and `.pptx`, where the “x” stands for XML. These files are ZIP containers holding a set of XML parts and resources such as images. Both the XML structure and the packaging follow a published spec — OOXML.

With Microsoft’s backing, OOXML was adopted by international standards bodies, first as [ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/) and later as [ISO/IEC 29500](https://www.iso.org/standard/71691.html). Microsoft also put it under the [Open Specification Promise (OSP)](https://docs.microsoft.com/en-us/openspecs/dev_center/ms-devcentlp/1c24c7c8-28b0-4ce1-a47d-95fe1ff504bc), committing not to assert certain patent claims against compliant implementations.

On paper, then, anyone can parse, create, and edit OOXML to be compatible with Microsoft Office, which sounds great. But the LibreOffice article calls this premise into question, arguing that OOXML’s deliberate complexity turns this supposed openness into a trap, a tool for maintaining a monopoly.

Let’s be honest: few people would describe their experience with Microsoft Office as satisfying, which is part of why this article resonated widely. In my past life doing legal grunt work, battling convoluted Word documents was a daily ritual. I also authored the Word section of an Office tutorial series, where my main approach was to explain Word’s quirks by digging into the underlying OOXML format. Thus, I’m intimately familiar with what makes Office and OOXML painful.

Despite this, I disagree with the LibreOffice’s framing and conclusion. Aiming for mass appeal, the post is heavy on emotion and accusation but light on factual analysis, missing a solid educational opportunity. (LibreOffice later [published](https://blog.documentfoundation.org/blog/2025/06/28/a-technical-dive-into-odf/) a more technical comparison, but it still jumped straight from code snippets to conclusions.)

In my view, OOXML is indeed complex, convoluted, and obscure. But that’s likely less about a plot to block third-party compatibility and more about a self-interested negligence: Microsoft prioritized the convenience of its own implementation and neglected the qualities of clarity, simplicity, and universality that a general-purpose standard should have. Yes, that neglect has anticompetitive effects in practice, but the motive is different from deliberate sabotage and thus warrants a different judgment. (A detailed legal analysis is beyond the scope of this article.)

In other words, LibreOffice identified the right problem, it may have reached the wrong conclusion. Here’s why.

OOXML as a Sloppy Standard
--------------------------

The LibreOffice article criticizes how “a simple sentence such as ‘To be, or not to be, that is the question’ becomes an inextricable sequence of tags that users cannot access.” Let’s use this very example to see what happens.

Create a Word document containing

> **To be**, or not to be, that is the question.

(with “To be” in bold), save, and peek at `word/document.xml` inside the resulting `.docx`:

```
<w:p w14:paraId="6F3ED131" w14:textId="46C90999" w:rsidR="00BF5D1D"
    w:rsidRDefault="004249FF">
    <w:r w:rsidRPr="00D41C8D">
        <w:rPr>
            <w:b />
            <w:bCs />
        </w:rPr>
        <w:t>To be</w:t>
    </w:r>
    <w:r w:rsidRPr="004249FF">
        <w:t>, or not to be, that is the question</w:t>
    </w:r>
    <w:r>
        <w:t>.</w:t>
    </w:r>
</w:p>
```

(line breaks added for readability.)

Take a breath — The core structure is a paragraph (`<w:p>`) containing three runs (`<w:r>`). A _run_ is a contiguous span of text sharing the same formatting. In OOXML, every paragraph comprises one or more runs.

Breaking it further down:

*   The outer `<w:p>` element represents the paragraph. The attributes like `w14:paraId` and `w:rsidR` are internal identifiers Word uses for features like collaborative editing and tracking revisions.
*   The first `<w:r>` represents the bolded text _To be_. It contains a `<w:rPr>` (Run Properties) element to define its formatting. Inside, `<w:b/>` and `<w:bCs/>` set the font to bold for Western and complex scripts, respectively (even though there are no complex scripts here). Only after all that does the `<w:t>` element hold the actual text.
*   The second `<w:r>` contains the rest of the text up to the period. Since it uses the default formatting, it lacks a `<w:rPr>` element.
*   The third `<w:r>` contains only the final period. There’s no formatting difference, and it’s split off the prior run simply because I pasted the sentence but typed the period, exactly the kind of “surprise” OOXML happily encodes.

Contrast that with the same content saved as ODF (`content.xml`):

```
<text:p text:style-name="Standard">
    <text:span text:style-name="T1">To be</text:span>
    , or not to be, that is the question.
</text:p>
```

Even at a glance it’s more intelligible. Strip the `text:` namespaces and it’s nearly valid HTML.

The only thing that needs explaining is that ODF doesn’t wrap _To be_ with a dedicated “bold” tag. Instead, it applies an auto-style named `T1` to a `<text:span>`, an act of separating content and presentation that mirrors established web practices.

In short, if you have a basic understanding of the web stack, you can largely make sense of ODF’s XML. On the other hand, OOXML, with its abstruse tag names, feels like it requires a PhD to decipher.

And this is just for simple text formatting. When you get into complex elements like tables and lists — a shared nightmare for every heavy Word user — OOXML’s complexity only skyrockets. That thousand-page specification isn’t just for show.

Beyond its formal complexity, the quality of OOXML as a standard is also questionable. Contemporary critiques of the submission [catalogued](https://noooxml.wdfiles.com/local--files/arguments/ODF-vs-OOXML-v1.2.pdf) technical defects, for example:

*   Canonizing known bugs and compromises from Office (_e.g._, maintaining two separate date systems starting in 1900 or 1904, and incorrectly [“treating 1900 as a leap year”](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/wrongly-assumes-1900-is-leap-year));
*   Conflicting with established standards for language codes (ISO 639), vector graphics (W3C SVG), and mathematical notation (W3C MathML);
*   Using vaguely defined and inconsistent units of measurement; and
*   Lacking clear and consistent naming conventions for elements and attributes (_e.g._, inconsistent ccase rules).

[The process of OOXML becoming an ISO standard](https://en.wikipedia.org/wiki/Standardization_of_Office_Open_XML) was itself highly dramatic. First, Microsoft chose to submit it via the “fast track,” a path intended for mature, widely implemented, and stable specifications. OOXML in 2006 met none of these criteria: it was new; its only complete implementation was the not-yet-released Office 2007; and nobody could plausibly review thousands of pages on that timetable. Organizations like Google and the Free Software Foundation Europe (FSFE), along with many technical experts, raised objections.

The voting that followed was among ISO’s most contentious: several national bodies abruptly swelled with new members, many Microsoft partners, who then voted in favor. Sweden’s initial approval was voided after incentives linked to support came to light.

In the end, OOXML squeaked through after two rounds, but Brazil, India, South Africa, Venezuela, and others filed formal appeals alleging procedural defects. Although these appeals failed to overturn the result, they underscored the divisive and chaotic nature of the standardization.

Why Microsoft’s Motive Wasn’t Deliberate Sabotage
-------------------------------------------------

So far, the evidence seems to support LibreOffice’s claim: OOXML is a sloppy standard, both technically and procedurally. But facts don’t directly prove intent. If we dig into the context of OOXML’s creation, it can be argued that harming competitors was not Microsoft’s _primary_ aim.

First, OOXML was, in material part, a defensive posture under intensifying antitrust and “open standards” pressure. Microsoft [announced](https://news.microsoft.com/2005/11/21/qa-microsoft-co-sponsors-submission-of-office-open-xml-document-formats-to-ecma-international-for-standardization/) OOXML in late 2005 while appealing an adverse European Commission [judgment](https://en.wikipedia.org/wiki/Microsoft_Corp._v_European_Commission#Judgment) centered on interoperability disclosures. Thus, it was only a matter of time before Office file compatibility came under the regulatory microscope. (The Commission indeed opened a [probe](https://competition-cases.ec.europa.eu/cases/AT.39294) in 2008.)

Meanwhile, the rival ODF matured and became an ISO standard in May 2006. Governments, especially in Europe, began to mandate open standards in public procurement. If Microsoft did nothing, Office risked exclusion from government deals.

Given that context, the sensible inference about Microsoft’s goal is to create a format that it controlled but also carried the “international standard” seal of approval, which would be both a shield against potential regulation and a weapon against the challenge from ODF. Thus, the primary goal for this new format wasn’t to be elegant, universal, or easy to implement; it was to placate regulators while preserving Microsoft’s technological and commercial advantages. The easiest, cheapest way to do that, of course, is to package its existing complexity as the new “standard.”

To support this, it’s worth noting a more fundamental difference between OOXML and ODF. Look again at the XML snippets, but this time, pay attention to where the actual text content appears:

```
<!-- OOXML -->
<w:p ...><w:r ...><w:rPr>...</w:rPr><w:t>To be</w:t></w:r><w:r ...><w:t>, or not to be...</w:t></w:r><w:r><w:t>.</w:t></w:r></w:p>

<!-- ODF -->
<text:p ...><text:span ...>To be</text:span>, or not to be...</text:p>
```

In ODF, the text content interleaves with XML tags, just like in HTML, while in OOXML, text is always buried inside `<w:t>` at the leaves, and never appears as a peer of structural elements.

That reflects two opposed uses of XML:

*   ODF uses XML as markup. Text is first-class; tags annotate spans with structure and styling. This matches XML’s [original design goal](https://en.wikipedia.org/wiki/XML#History) for information presentation.
*   OOXML uses XML as a serialization format. In other words, OOXML isn’t so much describing the document content as it is describing the abstract data structures that the Office application “sees.” Our example above serializes a “paragraph” object, which is an ordered array of “run” objects; some of these run objects have style properties, and each has a string property containing the actual text.

You can corroborate this by comparing OOXML to Office’s VBA object model. For instance, the child elements allowed within OOXML’s paragraph properties tag (`<w:pPr>`, specified in ECMA-376 Part 1, § 17.3.2.28) map almost one-for-one to the properties of VBA’s [`Paragraph` object](https://learn.microsoft.com/en-us/office/vba/api/word.paragraph). Many other OOXML–VBA pairings align the same way.

This explains the root of OOXML’s complexity: it mirrors Office’s sprawling features and legacy. To ensure fidelity and backward compatibility, Microsoft didn’t design a format that describes a document’s appearance; instead, it’s much closer to a dump of the application’s state. In this sense, OOXML is less of a standard and more of a projection of the Office application itself.

In fact, Office’s legacy is so heavy that even Microsoft doesn’t fully implement OOXML as standardized. ECMA-376 defines Strict and Transitional variants, with Transitional intended to preserve behaviors needed for old Office versions (e.g., `footnoteLayoutLikeWW8`, `autoSpaceLikeWord9`, `useWord97LineBreakRules`). To this day, Office saves Transitional by default. Microsoft even maintains a lengthy [document](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/21b45168-16f9-466d-9445-1992a02c517a) detailing the ways in which Office deviates from the ECMA-376 standard, including different interpretations of default values and non-standard extensions.

Furthermore, binding the format tightly to program state is not a novel, muddy-the-water trick, but merely how Office has long worked. Joel Spolsky, in a [famous blog post](https://www.joelonsoftware.com/2008/02/19/why-are-the-microsoft-office-file-formats-so-complicated-and-some-workarounds/), analyzed the complexity of the old binary Office formats, showing that they were even more akin to a direct memory dump, and was also of the opinion that this design was driven more by performance and practical constraints than by malice or incompetence.

Nor did OOXML spring from nowhere. Even before it, Microsoft had already been exploring a transition from binary to XML. Office XP and 2003 supported more primitive XML formats like [Excel XML](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-xp/aa140066(v=office.10)) and [Word XML](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-2003/aa174023(v=office.11)), just without ZIP packaging and with all parts mashed into a single XML file (binary resources base64-encoded). This provides further evidence that OOXML is less an act of sabotage than the continuation of a flawed, inelegant lineage.

Conclusion
----------

The argument of this article is not to let Microsoft off the hook; they could have done much better. Faced with demands for openness, Microsoft could have produced a clean, modern spec and keep the mass pile of legacy inside the application. Instead, it poured all that baggage into an XML container, pushed it to the world with market power, and shifted the comprehension cost onto everyone else. While this article argues for distinguishing this from the deliberate sabotage that LibreOffice alleges, a broken, low-quality standard is damaging to the ecosystem, whether born of negligence or conspiracy.

On the other hand, the LibreOffice post reflects a counterproductive reflex that’s common in open-source circles: scolding users for accepting proprietary tech. But users aren’t foolish. Elegance and openness are virtues, but they are only a few of the factors most people weigh, and often not the decisive ones. LibreOffice itself, as ODF’s flagship, still suffers from rough edges in design, interaction, and performance. As a result, even as Office hobble itself with bloat, most people still find it _easier_. Without a clear-eyed, systematic push to improve those fundamentals, cheerleading for open software and open formats will remain slogan and self-pity, an approach that is unlikely to win a broader audience or to dent an incumbent’s dominance.

中文版
---

引言
--

前段时间，开源办公软件 LibreOffice 的官方博客[发表](https://blog.documentfoundation.org/blog/2025/07/18/artificially-complex-xml-schema-as-lock-in-tool/)了一篇颇具话题性的文章：《刻意复杂化的 XML 规范是一种锁定用户的工具》（An artificially complex XML schema as a lock-in tool）。

这篇文章把批判的矛头指向了微软基于 XML 的文件格式——Office Open XML（简称 OOXML）。文章指控，微软虽然表面上开放了 Office 文件格式标准，但通过将其设计得极为复杂，实际上阻碍了与第三方软件的互操作性。文章认为，这种复杂性是刻意为之，与实际需求脱节。这就好比运营一条名义上开放的轨道，却将控制系统设计得只有一家制造商才能运营，从而形成事实垄断。同时，用户往往不加批判地接受这些专有技术，这使得微软能轻易将用户锁定在自己的生态系统中。

为不太熟悉这个话题的朋友补充一些背景。Office 办公软件历史上经历过一次重要的文件格式变化。Office 2003 及更早版本的默认格式（`.doc`、`.xls`、`.ppt`等）是所谓的「二进制格式」，其内容并非人类可直接阅读的文本。从 Office 2007 开始，微软切换到新的默认格式`.docx`、`.xlsx`和`.pptx`，其中的`x`就代表 XML。这些新格式的文件本质上是一个 ZIP 压缩包，里面包含了一系列 XML 文件和图片等资源。从 XML 的结构到打包方式，都遵循一套公开的标准，也就是 OOXML。

在微软的推动下，OOXML 先后被国际标准组织采纳为[ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/)和[ISO/IEC 29500](https://www.iso.org/standard/71691.html)。微软也将其纳入所谓「[开放规范承诺](https://docs.microsoft.com/en-us/openspecs/dev_center/ms-devcentlp/1c24c7c8-28b0-4ce1-a47d-95fe1ff504bc)」，保证不会对实现该标准的行为提出专利权主张。

因此，理论上，任何个人或第三方软件都可以自由地解析、创建和修改 OOXML 文件，实现与 Microsoft Office 的兼容。这听起来很美好，但 LibreOffice 的文章正是对此提出质疑，认为 OOXML 刻意的复杂性使所谓的「开放」变成了一个只进不出的陷阱，是微软维护垄断的工具。

如何看待这种观点？坦白地说，相信没有几个人对 Office 的使用体验印象完美，这也是此文颇具传播力的原因。在我过去的一段法律民工生涯中，跟复杂的 Word 文档斗争是每天的必修课。我还负责编写过一份[Office 教程](https://sspai.com/series/226)的 Word 部分，当时的主要思路就是通过介绍 OOXML 格式，来解释 Word 的一些怪癖和相应的最佳实践。因此，我对 Office 和 OOXML 的难用之处也算深有体会。

但即使如此，我并不赞同 LibreOffice 此文的写法和结论：可能是为了大众传播效果，这篇文章情绪、指控过多，而分析、事实太少，实际上错过了一次很好的科普机会。（LibreOffice 后来又[发布](https://blog.documentfoundation.org/blog/2025/06/28/a-technical-dive-into-odf/)了一篇更技术性的对比，但仍然直接从代码跳到了结论。）

在我看来，OOXML 格式确实复杂、繁琐、晦涩。但这很可能不是因为微软蓄意阻止第三方兼容，而更多是出于一种不作为的自私心态：在制定标准时，只考虑自身实现的便利，而忽略了一个通用标准应有的质量、简洁和普适。当然，这种不作为客观上也造成了阻碍竞争的结果，但这在动机上与蓄意破坏有别，因此也应受到不同的评价。（具体的法律分析超出了本文的讨论范围。）

为此，本文将基于 OOXML 的语法和制定背景，论证为什么 LibreOffice 的文章指出了正确的问题，却可能得出了错误的结论。

为什么说 OOXML 是一个潦草的标准
-------------------

LibreOffice 的文章中批评说，「简单如『生存还是毁灭，这是个问题』的句子，都会变成用户无法解读的相互纠缠的标签组合」。我们不妨就以此为例，新建一个 Word 文档，输入

> To be or not to be.

（其中 _To be_ 加粗），然后保存，看看都会存储出什么样的结果。

用任意压缩工具解压这个`.docx`文件，从所得的`word/document.xml`文件中就能看到如下内容：

```
<w:p w14:paraId="6F3ED131" w14:textId="46C90999" w:rsidR="00BF5D1D"
    w:rsidRDefault="004249FF">
    <w:r w:rsidRPr="00D41C8D">
        <w:rPr>
            <w:b />
            <w:bCs />
        </w:rPr>
        <w:t>To be</w:t>
    </w:r>
    <w:r w:rsidRPr="004249FF">
        <w:t>, or not to be, that is the question</w:t>
    </w:r>
    <w:r>
        <w:t>.</w:t>
    </w:r>
</w:p>
```

（有节选，额外添加了换行和缩进以便阅读；后同。）

可能你已经晕了……但让我们强打精神来分析一下。这段 XML 的核心结构是一个段落（`<w:p>`），它包含了三个「文本块」（run，用`<w:r>`元素来代表）。所谓「文本块」，是指一段具有相同格式的连续文本。在 OOXML 中，每个段落都由一个或多个文本块组成。

具体而言——

*   外层`<w:p>`元素代表整个段落。其中的`w14:paraId`、`w14:textId`和`w:rsidR`等属性是 Word 内部用于协同编辑、追踪修订历史的标识符；
*   第一个`<w:r>`元素代表加粗的 _To be_。它包含一个`<w:rPr>` (Run Properties) 元素来定义格式。其中，`<w:b/>`和`<w:bCs/>`分别将西文和中文等复杂书写系统（complex script，尽管这里没有）的字体设置为粗体。之后，`<w:t>`元素才包含实际的文本内容；
*   第二个`<w:r>`元素包含了后面直到句号前的所有文本。由于这段文本使用默认格式，所以没有`<w:rPr>`元素；
*   第三个`<w:r>`元素只包含最后的句号，与前面的文本在格式上并无差异。之所以被单独分割出来，仅仅是因为……前面的文字是我粘贴的，而这个句号是我手动输入的。是的，OOXML 就是会因为各种意想不到的原因，给你制造类似的「惊喜」。

作为对比，相同内容若使用 LibreOffice 的 OpenDocument 格式（ODF）存储，其对应的 XML 文件 (`content.xml`) 则要好懂得多：

```
<text:p text:style-name="Standard">
    <text:span text:style-name="T1">To be</text:span>
    , or not to be, that is the question.
</text:p>
```

你可能一眼就觉得这是一种更简明的格式。事实上，如果去掉标签和属性开头的命名空间`text:`，它几乎就是一段合法的 HTML。唯一需要解释的是粗体文本的处理方式：ODF 没有用一个「粗体」标签直接包裹 _To be_，而是创建了一个名为`T1`的自动样式，并将其应用到包裹文本的`<text:span>`元素上。这种做法也体现了 Web 中受推崇的「内容与样式分离」原则。

总的来说，只要你略懂 Web 基础，就能大致看懂 ODF 的 XML。相比之下，OOXML 中那些晦涩的标签名，大概都需要博士后学位才能猜出来是什么意思。

以上分析的还只是最简单的文本格式。如果涉及表格、列表等复杂元素（相信这是每个重度 Word 用户共享的噩梦），OOXML 的复杂程度只会让你更加挠头——几千页的文档不是吃干饭的。

除了形式上的复杂，OOXML 作为一个标准的质量也令人堪忧。在 OOXML 的制定阶段，就有大量文章指出微软提交的规范文档存在[诸多技术缺陷](https://noooxml.wdfiles.com/local--files/arguments/ODF-vs-OOXML-v1.2.pdf)，例如——

*   将 Office 中已知的错误或者妥协纳入标准（例如同时保留 1900 或 1904 年为起始点的两套日期系统，并且错误地[将 1900 年视为闰年](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/wrongly-assumes-1900-is-leap-year)）；
*   与语言区域代码（ISO 639）、矢量图形（W3C SVG）、数学符号（W3C MathML）等已确立的现存标准存在冲突；
*   使用定义不明确的计量单位，并且前后矛盾；以及
*   对元素和属性的命名约定（例如大小写规则）既不清晰也不一致。

[OOXML 成为 ISO 标准的过程](https://en.wikipedia.org/wiki/Standardization_of_Office_Open_XML)也极富戏剧性。首先，微软选择通过「快速通道」提交标准。这条通道本是为那些技术成熟、业界广泛实施的稳定规范所设。显然，OOXML 在 2006 年被提交时完全不符合这些条件：它是一个全新的规范，唯一的完整实现是尚未正式发布的 Office 2007，其几千页的规范文档更是根本不可能在短时间内完成审阅。谷歌、自由软件基金会欧洲分部（FSFE）等组织和众多技术专家都对此提出了异议。

其后的 ISO 投票过程更是该组织历史上争议最大的一次。例如，在投票期间，美国、意大利等国的标准委员会成员数量激增，新成员大多是微软的商业伙伴，并一致投票支持 OOXML。瑞典标准机构最初投了赞成票，但随后因曝出微软向合作伙伴提供报酬以换取支持的丑闻，该投票被宣布无效。

最终，ISO 经历了艰难的两轮投票才让 OOXML 得以通过。但这一结果并未平息争议，巴西、印度、南非、委内瑞拉等国正式向 ISO 提出上诉，认为整个过程存在程序瑕疵。虽然这些程序最终未能推翻结果，但足以表明这次标准化过程的分裂与混乱。

为什么说微软的动机并非蓄意破坏竞争
-----------------

到目前为止，证据似乎都支持 LibreOffice 的观点：OOXML 作为一个标准，无论在技术层面还是制定程序层面都是相当潦草的。但事实并不能直接推出意图和动机。如果进一步了解 OOXML 的制定背景，就会发现破坏竞争至少并不是微软的首要目的。

首先应当看到，OOXML 在某种程度上是微软在日益严格的反垄断审查和开放标准竞争压力下，采取的一种防御性姿态。OOXML 格式于 2005 年底[宣布](https://news.microsoft.com/2005/11/21/qa-microsoft-co-sponsors-submission-of-office-open-xml-document-formats-to-ecma-international-for-standardization/)。当时，微软正在上诉欧盟委员会前一年对其做出的[反垄断判决](https://en.wikipedia.org/wiki/Microsoft_Corp._v_European_Commission#Judgment)。该案的一个核心问题就是微软拒绝向 Sun 公司提供必要的协议规范，阻碍了跨系统兼容。不难想见，Office 的文件兼容性成为下一个监管焦点只是时间问题。（事实也的确如此，欧盟在 2008 年对 Office 等产品的兼容性问题展开了[调查](https://competition-cases.ec.europa.eu/cases/AT.39294)。）

与此同时，竞争标准 ODF 逐渐成型，并于 2006 年 5 月被正式批准为 ISO 国际标准。全球多国、特别是欧洲国家政府，开始倾向于在政府文件中强制采用开放标准。如果微软不采取行动，Office 就可能因不符合采购要求而被排除在政府订单之外。

基于此，我们可以对微软的动机做出合理推测：它迫切需要一个由自己主导、且带有「国际标准」光环的格式，以应对潜在的监管审查，并对抗 ODF 的挑战。这个新格式的首要目标不是简洁、通用或易于实现，而是「安抚」监管机构，同时最大限度地保留自身的技术优势和商业利益。要实现这一点，最便捷、成本最低的路径，就是将自己现有的复杂生态直接打包成一个所谓的「标准」。

为了说明这一点，值得指出 OOXML 和 ODF 还存在一个更加本质的不同。为此，再次观察前面给出的 XML 代码片段，并且注意两种格式中文本内容的出现位置。

```
<!-- OOXML -->
<w:p w14:paraId="6F3ED131" w14:textId="46C90999" w:rsidR="00BF5D1D"w:rsidRDefault="004249FF"><w:r w:rsidRPr="00D41C8D"><w:rPr><w:b /><w:bCs /></w:rPr><w:t>To be</w:t></w:r><w:r w:rsidRPr="004249FF"><w:t>, or not to be, that is the question</w:t></w:r><w:r><w:t>.</w:t></w:r></w:p>

<!-- ODF -->
<text:p text:style-name="Standard"><text:span text:style-name="T1">To be</text:span>, or not to be, that is the question.</text:p>
```

可以看到，在 ODF 中，文本内容可以与 XML 标签穿插出现，就像在 HTML 中一样。而在 OOXML 中，文本内容永远被包裹在最底层的`<w:t>`元素里，绝不会与其他结构化标签平级。

这种差异反映出两种格式使用 XML 的方式完全不同——

*   ODF 的语法是将 XML 作为一种标记语言（markup language）使用的。换句话说，文本内容是这种语法中的主角，尖括号括起的 XML 标签环绕在文本片段周围，标记其内部文本的外观、位置、层级等特征。这其实也是 XML 的[设计初衷](https://en.wikipedia.org/wiki/XML#History)——促进数字媒体中的信息展示；
*   OOXML 则将 XML 挪用为了一种序列化（serialization）格式。所谓「序列化」，是指将程序内存中的数据结构或对象转化为一串可存储或传输的文本。换句话说，OOXML 与其说是在描述文档内容，不如说是在描述 Office 软件「看到」的抽象结构。例如，上文例子就序列化了一个段落类型对象，它是由多个文本片段类型对象组成的有序集合。其中，有的文本片段对象具有样式属性，并且每个文本对象都有一个字符串属性用来记录文字内容。

这个结论可以通过比较 OOXML 标准和 Office 的编程语言 Visual Basic for Applications (VBA) 得到印证。例如，OOXML 中段落属性`<w:pPr>`所允许的子元素（ECMA-376 Part 1, § 17.3.2.28），与 VBA 中[段落对象 (`Paragraph`)](https://learn.microsoft.com/en-us/office/vba/api/word.paragraph)的属性几乎一一对应。其他许多 OOXML 元素和对应的 VBA 对象也有这种对应关系。

这就解释了 OOXML 复杂性的成因：它原封不动地反映了 Office 软件的繁复功能和历史包袱。为了保证存储格式的还原度和兼容性，微软没有选择在文件中描述文档的外观，然后用程序来解析和还原这些描述，而更像是直接把程序的运行状态转储到文件中。从这个意义上说，OOXML 与其说是一个「标准」，不如说就是应用程序本身，是 Office 软件的射影。

事实上，由于 Office 的历史包袱过于沉重，微软自己到现在都没有做到完全遵循 OOXML 标准。ECMA-376 将 OOXML 分为「严格」（Strict）和「过渡」（Transitional）两个版本。所谓「过渡」，就是为了兼容旧版 Office 的各种特殊行为而保留的功能，记录在标准的第四部分，例如`footnoteLayoutLikeWW8`、`autoSpaceLikeWord9`、`useWord97LineBreakRules`等等。时至今日，Office 默认保存的仍然是这种「过渡」格式。微软还有一份冗长的[文档](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/21b45168-16f9-466d-9445-1992a02c517a)说明 Office 在哪些方面违反了 ECMA-376 标准，例如对许多默认值的不同诠释和处理、自定义部件和扩展性等。

此外，将文件格式与程序状态高度绑定，也不是一种故意「搅浑水」的新发明，而是 Office 的「祖传」思路。知名软件工程博主 Joel Spolsky 在[一篇经典文章](https://www.joelonsoftware.com/2008/02/19/why-are-the-microsoft-office-file-formats-so-complicated-and-some-workarounds/)中分析过旧版 Office 二进制格式的复杂性，其中表明这些旧格式还要更类似于内存的直接转储，并且也认为这种设计更多是出于性能和现实的考量，而非恶意或无能。

其实，早在 OOXML 之前，微软就已经在探索从二进制格式向 XML 转型，并且在 Office XP 和 2003 中分别支持了一种更「原始」的[Excel XML](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-xp/aa140066(v=office.10))和[Word XML](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-2003/aa174023(v=office.11))格式。这些格式的语法已经体现出 OOXML 的雏形，但没有采用 ZIP 打包，而是将所有组件和资源文件（编码为二进制数据）都堆放在单个 XML 文件中。这也从侧面表明，OOXML 并不是微软为了「搞乱」竞争而定制的，而是一些已有思路和成果的延续——尽管并不是特别优雅的思路和成果。

结语
--

本文的目的并不是为微软开脱；它本可以做得更好。当面临「开放」的外部要求时，微软本可以推出一个更干净和现代的标准，将庞杂、充满矛盾的「遗产」保留在程序内部自行消化。相反，它选择将这些遗产统统打包，扔进一个 XML 容器，然后利用其市场力量推向世界，并迫使其他人来承担理解和消化的成本。尽管本文主张将这与 LibreOffice 所指控的「蓄意破坏竞争」作出区分，但显然，一个破碎、低质量的标准，无论其形成是源于阴谋还是疏忽，都是会对生态系统造成损害的。

但另一方面，LibreOffice 文章所反映出的某些思维也不值得鼓励。它像许多开源拥趸的常见论调一样，「恨铁不成钢」地指责用户不加批判地接受微软的封闭技术。但用户并不傻。技术的优雅、授权的开放固然是优点，但对大多数用户来说，这只是决策的众多考量之一，甚至不是最主要的因素。作为 ODF 格式的「旗舰」软件，LibreOffice 自身从设计到交互再到性能，都存在许多粗糙之处。以至于即使 Office 不断用臃肿的功能自废武功，在多数人眼中它依然比 LibreOffice 更「易用」。如果不能正视并系统地改善这些问题，那么对开源软件和开放格式的鼓吹，就只能停留在喊口号和顾影自怜的层面，既无法让其声音被更广泛的人群接纳，也难以对垄断市场构成实质性的挑战。