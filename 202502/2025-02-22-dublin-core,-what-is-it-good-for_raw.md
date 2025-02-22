Title: Dublin Core, what is it good for?

URL Source: https://www.thisdaysportion.com/posts/dublin-core-what-is-it-good-for/

Published Time: 2024-09-01T00:00:00+00:00

Markdown Content:
…or Schema, microformats or Open Graph?

TLDR
----

There are several popular meta schemas out there. Open Graph may be the best supported, but if you want your meta data to be picked up by a particular service you might need to do a bit of research. Or support them all.

What’s a meta schema?
---------------------

Meta schemas enable us to embed structured information in web pages, such as articles, blog posts or book reviews. This can include fairly basic information, such as publication date and author, and extended information, such as the publisher, copyright, genre and keywords.

Although this information may seem self-evident – you can probably infer the publication date of this post because it sits under the title, for example – schemas make the data easily findable by computers. Furthermore, with some schema implementations, you can add information to your document that you don’t always want to display on the page, such as copyright.

How to add meta schema data to your posts
-----------------------------------------

There are a couple of basic ways to add information about your document to the HTML.

### Add the data to the document head

The first, naturally enough, is to add it to the document `head`. In fact, HTML already has an element made for the purpose – [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta). Add `name` and `content` pairs to set meta data. The three non-technical, standard items are `description`, `author` and `keywords`:

```
<title>The highest bestest powered rifle</title>
<meta name="author" content="Hunter S Thompson">
<meta name="description" content="An account of being fired into the stars upon one’s death.">
<meta name="keywords" content="Aspen">
```

Note: The `<title>` element is a special instance of HTML meta data.

As there are not many useful meta name attributes beyond author and description, developers, search engines and academics have written more expressive schemas. I’ll go through these in a bit more detail, but one of them is [Dublin Core](https://www.dublincore.org/specifications/dublin-core/usageguide/elements/), which has 22 meta data items, which you can add to the document head in pretty much the same way as the original meta name attributes. In this example, we’ve added language and publication date to the author and description:

```
<link rel="schema.DC" href="http://purl.org/DC/elements/1.0/">
<meta name="DC.Title" content="The highest bestest powered rifle">
<meta name="DC.Description" content="An account of being fired into the stars upon one’s death.">
<meta name="DC.Creator" content="Thompson, Hunter S">
<meta name="DC.Date" content="2024-05-01T08:25:00+00:00">
<meta name="DC.Language" content="en">
<meta name="DC.Subject" content="Aspen">
```

Sometimes, we can also add meta data to the document head using `json` wrapped in a `<script>` element. [Schema.org](https://schema.org/) allows this method. In this example, we’re adding information about the publisher and an associated image:

```
<script type="application/ld+json">
{
"@context": "https://schema.org/",
"@type": "Blog",
"@id": "https://www.thisdaysportion.com/",
"mainEntityOfPage": "https://www.thisdaysportion.com/",
"name": "This day’s portion",
"description": "A blog about Aspen life.",
"publisher": {
"@type": "Organization",
"@id": "https://www.thisdaysportion.com/",
"name": "This day’s portion",
"logo": {
"@type": "ImageObject",
"@id": "https://www.thisdaysportion.com/images/faust-staves.jpg",
"url": "https://www.thisdaysportion.com/images/faust-staves.jpg",
"width": "600",
"height": "600"
}
},
"blogPost": [
{
"@type": "BlogPosting",
"@id": "https://moriarty.thisdaysportion.com/without.html",
"mainEntityOfPage": "https://www.moriarty.thisdaysportion.com/without.html",
"headline": "The highest bestest powered rifle (no article, no microformats)",
"name": "The highest bestest powered rifle (no article, no microformats)",
"description": "An account of being fired into the stars upon oneâ€™s death.",
"datePublished": "2024-05-01",
"dateModified": "2024-05-02",
"author": {
"@type": "Person",
"@id": "https://www.thisdaysportion.com/",
"name": "Hunter S Thompson"
},
"image": {
"@type": "ImageObject",
"@id": "https://www.thisdaysportion.com/images/faust-staves.jpg",
"url": "https://www.thisdaysportion.com/images/faust-staves.jpg",
"height": "600",
"width": "600"
},
"url": "https://moriarty.thisdaysportion.com/without.html",
"keywords": [
"Aspen",
"Guns",
"Wild Turkey"
]
}
]
}
</script>
```

### Add the data to the HTML, using attributes or classes

Another schema – there’s no easy to use w3 schema for HTML, unfortunately, just [XML](https://www.w3.org/XML/Schema) – is [Microformats](https://microformats.org/). You add microformat meta data by using a set of defined classes in your HTML. This time, we’re adding categories and identifying the actual content with the `e-content` class:

```
<main class="h-entry">

<h1 class="p-name">The highest bestest powered rifle (with microformats in the HTML)</h1>

<p>By <span class="p-author">Hunter S Thompson</span></p>

<p class="dt-published" datetime="2024-05-01">1 May 2024</p>

<div class="e-content">

…

</div>

<p><span class="p-category">Wild Turkey</span>, <span class="p-category">Guns</span>, <span class="p-category">Aspen</span>.</p>

</main>
```

Schema.org uses HTML `itemscope`, `itemtype` and `itemprop` attributes instead of classes. Note how the markup can get quite complex when you nest `itemtypes` – in this case the `Person` sits within the `BlogPosting`:

```
<main itemscope itemtype="https://schema.org/BlogPosting">

<h1 itemprop="name">The highest bestest powered rifle (Schema in markup)</h1>

<p><span itemprop="author" itemscope itemtype="https://schema.org/Person"><span itemprop="name" class="p-author h-card">Hunter S Thompson</span></span></p>

<p><time itemprop="datePublished">1 May 2024</time></p>

<div itemprop="articleBody">

…

</div>

<p>Keywords: <span itemprop="keywords">Guns, Wild Turkey, Aspen</span></p>

</main>
```

What schemas can I use and how should I add them?
-------------------------------------------------

As you can tell, you have choices here, whether you want them or not. The main schemas I’m aware of are:

*   [Schema.org](https://schema.org/)
*   [Microformats](https://micorformats.org/)
*   [Dublin Core](https://www.dublincore.org/specifications/dublin-core/usageguide/elements/)
*   [Open Graph](https://ogp.me/). This is Meta’s schema that originally enabled Facebook to automatically format any links you’d add to a post, displaying a thumbnail, title and a summary. It’s been adopted by most social media and beyond, and contains a good range of meta items.
*   The HTML defaults

The schema you choose will dictate how you add it. Dublin Core and Open Graph add data to the document `head` while you add microformats with HTML classes. Schema.org can be used in the `head` and the `body`.

Adding data to the `head` has the advantage of hiding it from the rendered page. I’d also argue it’s cleaner than mixing it with your HTML, although Schema.org’s `json` is fussy. Using classes instead of attributes strikes me as a failure to separate semantics from styling, although I appreciate this is a mainly hypothetical problem. Ideally, I’d just use Dublin Core as it’s placed in the head and is a simple list of names and content.

Unfortunately, your choice doesn’t have much to do with ease of use. Depending on what you want to achieve, you may have to use more than one schema.

Where are schemas used and how?
-------------------------------

This is where it gets complicated. So far, we’ve looked at how we add various schemas to our documents without considering how this meta data will actually be used.

Some popular uses for meta data are:

*   In read-it-later services, such as [Pocket](https://getpocket.com/), [Instapaper](https://instapaper.com/) and [Omnivore](https://omnivore.app/)
*   In Google search and social media link snippets
*   To enable [webmentions](https://indieweb.org/Webmention), a protocol that enables automated communication between independent websites and social media accounts. Webmentions require Microformats.
*   In academic services, such as [Zotero](https://zotero.org/), a reference and bibliography app. You can add a web page to Zotero and and it will use the schema meta data to create a bibliographic reference.

![Image 1: The Zotero app with a web article highlighted. In the right hand pane it displays meta data associated with the page, including document author and date.](https://www.thisdaysportion.com/images/zotero-2.jpg)

Because there are several schemas and no “official” version, these services are free to adopt whichever they want. To further muddy things, they can also choose _how_ they interpret meta data.

To get some insight into how schemas are used in the real world, I ran a few tests by feeding three of the above services different versions of the same document:

*   One with [no schemas beyond the basic HTML defaults](https://moriarty.thisdaysportion.com/main.html)
*   One marked up with [microformats in the HTML](https://moriarty.thisdaysportion.com/micro.html)
*   One with [Schema.org json](https://moriarty.thisdaysportion.com/schema-head.html) added to the `head`
*   One with [Schema.org itemprop attributes](https://moriarty.thisdaysportion.com/schema-body.html) in the HTML
*   One with [Dublin Core meta elements](https://moriarty.thisdaysportion.com/dc.html) in the `head`
*   One with [Open Graph meta elements](https://moriarty.thisdaysportion.com/og.html) in the `head`

Support across the services varied.

### Instapaper

| Schema | Support |
| --- | --- |
| Plain HTML | Partial. Just the title from the title element. |
| Microformats | No |
| Dublin Core | No |
| Open Graph | Partly. Just the title and the article listing image.  
 |
| Schema json | No |
| Schema HTML | Yes |

As you can see, Instapaper only has partial support for the various schemas. Interestingly, it takes the Open Graph title over the document’s `<title>`. Schema.org is supported, but only when it’s added to the HTML using `itemprop` attributes.

### Omnivore

| Schema | Support |
| --- | --- |
| Plain HTML | Partial. It is able to get the date from the raw HTML. Uses the title element. |
| Microformats | Yes |
| Dublin Core | Yes |
| Open Graph | Just the image.  
 |
| Schema json | Yes |
| Schema HTML | Yes |

Omnivore is a good meta data citizen, providing support for the main schemas, including Schema.org’s `json`.

### Zotero

| Schema | Support |
| --- | --- |
| Plain HTML | Partial. Just the title from the title element. |
| Microformats | No  
 |
| Dublin Core | Yes |
| Open Graph | Yes, including date  
 |
| Schema json | No |
| Schema HTML | No  
 |

I’d guess that Zotero’s choice of meta schemas is a reflection of its age and library background: Dublin Core’s development predates Schema.org and Microformats. It’s interesting that it has made a nod to modern developments (the meta data world turns reassuringly slowly) by supporting Open Graph.

### A note on social media and search results

I didn’t test extensively across social media as I don’t have Twitter, Facebook or Instagram accounts. Open Graph is the accepted meta data standard here, which you can use when linking to a page. Here’s an example of how Pinafore, a Mastodon app, creates a formatted link to a web page when you toot its URL:

![Image 2: Screenshot of a link to a BBC prom article, displaying a thumbnail image, the title and a summary.](https://www.thisdaysportion.com/images/meta-classical.png)

And the [BBC web page](https://www.bbc.co.uk/programmes/m0022npm) `head` Open Graph markup that Pinafore uses:

```
<meta property="og:description" content="The most intimate, star-studded of proms with Yo-Yo Ma, Leonidas Kavakos and Emanuel Ax.">
<meta property="og:title" content="BBC Radio 3 - BBC Proms, 2024, Beethoven for Three with Yo Yo Ma, Emanuel Ax and Leonidas Kavakos">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.bbc.co.uk/programmes/m0022npm">        <meta property="og:image" content="https://ichef.bbci.co.uk/images/ic/1200x675/p0jlgs4g.jpg">
```

Although Google purports to use its own Schema.org data to construct objects like cards in its search results, the only semi reliable meta items are the page `<title>` and the `<meta name="description">`, which are used in results snippets:

![Image 3: A Google search snippet. The title is “The highest bestest powered rile” and the summary is “An account of being fired into the stars upon one’s death.”](https://www.thisdaysportion.com/images/goog-snippet.png)

So what schema(s) should I use?
-------------------------------

Sorry to disappoint, but the answer is _it depends_.

Your document _will_ need a `<title>`.

Some services demand a particular schema. If you want to send webmentions, you have to use microformats. Zotero – which is widely used across universities – requires Dublin Core or Open Graph.

If you want a formatted link to your post on social media, you’ll need Open Graph. I was quite surprised by the extent to which Open Graph has been adopted by other services. If you were just going to choose one, this is maybe the one I’d suggest. For some semblance of control of search snippets, add a `<meta name="description">`.

If you’re supporting Schema.org and only want to implement it in one way, `itemprop` attributes in the `body` have better support in my small sample.

The problem is there are several schemas out there, and many services of varying ages. To cover everything you’d need to add a lot of meta data.
