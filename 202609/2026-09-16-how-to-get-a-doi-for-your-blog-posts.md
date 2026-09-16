# How to get a DOI for your blog posts
- URL: https://shkspr.mobi/blog/2026/09/how-to-get-a-doi-for-your-blog-posts/
- Added At: 2026-09-16 14:07:47
- Tags: #read

## TL;DR
作者介绍为博客文章申请DOI的原因、方法与风险：用Rogue Scholar自动分配，但面临失控、追踪和删除等问题；结论是虽显自恋，却便于学术引用，值得尝试。

## Summary
这篇文章讲的是作者如何给自己的博客文章申请和使用 DOI，并解释为什么值得做、怎么做，以及有哪些风险。DOI 是“数字对象标识符”，可以理解成学术论文常用的持久链接。作者博客经常被论文、书籍、会议和新闻引用，而学术引用通常使用 DOI，所以即使以后域名变了、网站重排了，DOI 也能重定向到文章的新地址。

作者已经给博客申请过 ISSN，也有 ORCID。常规获取 DOI 的方式包括：学术机构代为申请、上传到 arXiv、使用付费服务。作者选择的是 Rogue Scholar。Rogue Scholar 是一个开放获取的科学博客存档和注册服务，会保存博客文章、给文章分配 DOI，并让它们更容易和正式学术文献一起被发现。它要求博客提供全文 feed，并且内容按 CC BY 授权。作者填表、进入 Slack 讨论、几天后获得批准，之后他的博客社区页面和 DOI 就能用了。

新文章是自动处理的。Rogue Scholar 会轮询博客 feed，抓取内容，并给每篇新文章铸造 DOI，作者不用手动操作，通常发布几分钟后 DOI 就会出现。旧文章比较麻烦：默认只会抓最近 40 篇，而且是最近“更新”过的 40 篇，并没有简单办法批量添加旧内容。作者正在写一个 WordPress 插件，想追溯性地给旧文章加 DOI。

获取 DOI 可以通过 Rogue Scholar 的 API，它基于 InvenioRDM。用文章 URL 或 GUID 查询后，会返回 JSON，DOI 在 `hits→hits→0→links→doi` 里。Rogue Scholar 会给每篇文章生成两个 DOI：一个指向文章本身，另一个指向特定版本。如果文章更新，应该产生新版本 DOI，这样别人可以引用你当时写下的版本，而不是后来修改过的版本。也可以用 CrossRef 搜索。短 DOI 服务 shortdoi.org 虽然存在，但不推荐使用。整个博客还有一个“虚荣 DOI”，比如作者的 `10.59350/shkspr`。

作者还介绍了自己生成 DOI 的方法：生成 0 到 1,099,511,627,775 之间的随机数，转成 Base32，加两个字符的校验和，再前缀 `10.59350/`。然后可以在 Atom feed 里用 `<id>https://doi.org/10.59350/12345-67890</id>` 声明，Rogue Scholar 看到后会代为注册。要让它对 HTML 引用管理器可见，可以加 Zotero 的 `<meta name=citation_doi content=10..../...>`，或 DublinCore 的 `<meta name=DC.Identifier content=doi:10..../...>`，或者用 Schema.org 的 `sameAs` 链接。

缺点也不少。第一是失去控制：DOI 系统比较中心化，`doi.org` 是中间守门人；如果它出问题，所有 `https://doi.org/10....` 链接都可能受影响。Rogue Scholar 也能重定向作者的 DOI，如果它被黑或变质，可能指向别处。归档还可能丢失 CSS 排版，只留下纯 HTML 或 PDF。第二是引用追踪：Google Scholar 按域名 `shkspr.mobi` 提醒，但如果别人用 DOI 引用，就不会触发提醒。Rogue Scholar 有引用追踪，但作者还不确定实际效果，也不确定会不会发邮件。第三是出版方元数据：CrossRef 里显示出版方是 Rogue Scholar 的母公司 Front Matter，不同引用管理器可能显示成博客名或 Front Matter。第四是许可：Rogue Scholar 硬性要求 CC BY，作者个人更喜欢 CC BY-SA；通过 Rogue Scholar 获取的内容是 CC BY，通过作者网站获取则是更严格的 CC BY-SA。第五是验证：DOI 持久，但不代表内容可验证，没有哈希或加密签名，无法确认归档文本是否准确。第六是排除内容：不想给 DOI 的文章需要从 feed 中排除，WordPress 可以用类似 `/feed/atom/?cat=-1234` 的方式，Rogue Scholar 也有过滤器。第七是删除：目前似乎无法删除或撤回内容，误发的东西可能永久存档。第八是隶属关系：ORCID 里的工作经历会被关联到任职期间写的博客文章，作者认为那些文章是个人身份写的，可以申请移除不准确关联。作者还试过生成带自己名字语义的 DOI，比如 `edent-00f47`，但即使校验和有效，也不应该使用带语义的字符串。

最后，作者也自问：是不是每篇博客都值得一个 DOI？他不知道哪篇“废话帖”会突然流行并被引用，所以觉得给所有文章都发 DOI 有点自恋和做作，但 DOI 系统并不缺空间。结论是：对他个人来说值得。他认为学术博客应该被正确引用，虽然并非所有文章都是前沿研究，但常有意想不到的文章进入论文或教材。他也好奇这会让博客在学术界更可见还是更不可见。文章本身就有一个 DOI：`https://doi.org/10.59350/5ck9b-kjv69`。
