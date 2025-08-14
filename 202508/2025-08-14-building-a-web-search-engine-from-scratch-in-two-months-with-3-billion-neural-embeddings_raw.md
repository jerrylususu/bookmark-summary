Title: Building a web search engine from scratch in two months with 3 billion neural embeddings

URL Source: https://blog.wilsonl.in/search-engine/

Published Time: 2025-08-10T00:00:00.000Z

Markdown Content:
Published August 10, 2025 34 min read

[![Image 1: Screenshot of final SERP without AI features.](https://blog.wilsonl.in/search-engine/serp-rocksdb.png)](https://blog.wilsonl.in/search-engine/serp-rocksdb.png)
A while back, I decided to undertake a project to challenge myself: build a web search engine from scratch. Aside from the fun deep dive opportunity, there were two motivators:

*   Search engines seemed to be getting worse, with more SEO spam and less relevant quality content.
*   Transformer-based [text embedding models](https://huggingface.co/spaces/mteb/leaderboard) were taking off and showing amazing natural comprehension of language.

A simple question I had was: why couldn't a search engine _always_ result in top quality content? Such content may be rare, but the Internet's [tail is long](https://en.wikipedia.org/wiki/Long_tail), and better quality results should rank higher than the prolific inorganic content and engagement bait you see today.

Another pain point was that search engines often felt underpowered, closer to keyword matching than human-level intelligence. A reasonably complex or subtle query couldn't be answered by most search engines at all, but the ability to would be powerful:

[![Image 2: SERP result of paragraph-length query.](https://blog.wilsonl.in/search-engine/serp-paragraph-cropped.png)](https://blog.wilsonl.in/search-engine/serp-paragraph-cropped.png)
Search engines cover broad areas of computer science, linguistics, ontology, NLP, ML, distributed systems, performance engineering, and so on. I thought it'd be interesting to see how much I could learn and cover in a short period. Plus, it'd be cool to have my own search engine. Given all these points, I dived right in.

In this post, I go over the 2-month journey end-to-end, starting from no infra, bootstrapped data, or any experience around building a web search engine. Some highlights:

*   A cluster of 200 GPUs generated a combined 3 billion [SBERT](https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1) embeddings.
*   At peak, hundreds of crawlers ingested 50K pages per second, culminating in an index of 280 million.
*   End-to-end query latency landed around 500 ms.
*   RocksDB and HNSW were [sharded](https://blog.wilsonl.in/corenn/) across 200 cores, 4 TB of RAM, and 82 TB of SSDs.

You can play around with a deployed instance of this search engine as a [live demo](https://blog.wilsonl.in/search-engine/#live-demo). Here's a high-level architecture map of the system that will be covered in this post:

*   [Proving ground](https://blog.wilsonl.in/search-engine/#proving-ground)
*   [Normalization](https://blog.wilsonl.in/search-engine/#normalization)
*   [Chunking](https://blog.wilsonl.in/search-engine/#chunking)
    *   [Semantic context](https://blog.wilsonl.in/search-engine/#semantic-context)
    *   [Statement chaining](https://blog.wilsonl.in/search-engine/#statement-chaining)

*   [Initial results](https://blog.wilsonl.in/search-engine/#initial-results)
*   [Crawler](https://blog.wilsonl.in/search-engine/#crawler)
*   [Pipeline](https://blog.wilsonl.in/search-engine/#pipeline)
*   [Storage](https://blog.wilsonl.in/search-engine/#storage)
*   [Service mesh](https://blog.wilsonl.in/search-engine/#service-mesh)
*   [GPU buildout](https://blog.wilsonl.in/search-engine/#gpu-buildout)
*   [Sharded HNSW](https://blog.wilsonl.in/search-engine/#sharded-hnsw)
*   [Optimizing latency](https://blog.wilsonl.in/search-engine/#optimizing-latency)
*   [Knowledge graph](https://blog.wilsonl.in/search-engine/#knowledge-graph)
*   [SERP](https://blog.wilsonl.in/search-engine/#serp)
    *   [AI assistant](https://blog.wilsonl.in/search-engine/#ai-assistant)
    *   [State tracking](https://blog.wilsonl.in/search-engine/#state-tracking)

*   [Search quality](https://blog.wilsonl.in/search-engine/#search-quality)
*   [Live demo](https://blog.wilsonl.in/search-engine/#live-demo)
*   [Costs](https://blog.wilsonl.in/search-engine/#costs)
*   [Conclusion and what's next](https://blog.wilsonl.in/search-engine/#conclusion-and-what's-next)

Proving ground
--------------

I started off by creating a minimal playground to experiment if [neural embeddings](https://huggingface.co/spaces/mteb/leaderboard) were superior for search: take some web page, chunk it up, and see if I can answer complex indirect natural language queries with precision.

As an example, let's say I'm looking at the S3 documentation. Here are how some queries are answered by current systems, and how I envisioned they should be answered:

| Query | Traditional search | Neural search |
| --- | --- | --- |
| i want to use s3 instead of postgres but with databases i can tag some human comment with some file in another column | _Random results about Postgres, S3, files_ | You can also specify custom metadata at the time that the object is stored. |
| why does CORS still not work after allowing all? | _Random snippet about CORS, "S3 not working", object permissions_ | Bucket configurations have an eventual consistency model... |
| could files get lost or corrupted? | _(No result shown)_ | If a PUT request is successful, your data is safely stored. |
| can i use s3 from lua? | _(No result shown)_ | The architecture of Amazon S3 is designed to be programming language-neutral, ... With the REST API, you use standard HTTP requests to create, fetch, and delete buckets and objects. |

Basically, the search engine should understand _intent_, not _keywords_:

*   Queries are understood as a whole instead of broken down into keywords and phrases.
*   No need for query engineering: operators, format, right words to use.
*   "Tip of the tongue", implicit, and conceptual queries are mapped correctly to the right answer.
*   You can ask multi-concept, complex, nuanced queries and surface non-obvious relationships.
*   It should be far less susceptible to keyword spam and SEO tactics.

This is already great for searches in general. But it'd also be great for finding insights, unnoticed connections, and hidden gems. You can ask some very sophisticated specific query, and the search engine will surface a [one-line sentence](https://en.wiktionary.org/wiki/needle_in_a_haystack) in an obscure quality essay. You could write a paragraph of your thoughts and views, and find other writers and areas with similar perspectives. You could query with phrases that signal quality and depth, to find content and communities of similar values.

Here's the sandbox flywheel I initially created to prove the concept:

1.   Grow set of gathered diverse raw web pages.
2.   Parse, normalize, augment, and embed them into a queryable HNSW index.
3.   Build and expand the test dataset of queries as I crawl, debug, experiment, and eval.
4.   Create a UI to introspect data at each stage, see failure points, and tune.

Normalization
-------------

HTML represents content in tags which have various intents: layout, text, media, interactivity, metadata, and app programming. Since a search engine focuses on text content, the first step of any pipeline is to sanitize and regularize the noisy markup from a crawled page and extract out semantic text. [WHATWG](https://html.spec.whatwg.org/multipage/) already defines plenty of semantic elements and rules, which I subsetted into the following mini-spec:

*   Structures should be consistent: `table > (thead, tbody, tfoot) > tr > (th, td)`; `(ul, ol) > li`.
*   Only semantic text elements should be kept: `p, table, pre, blockquote, ul, ol, dl`.
*   Text is trimmed and collapsed; no loose or unexpected text nodes outside of `<p>`.
*   Flatten text trees so that retrieving and mutating text spans (which happens often) doesn't require traversing and reconciling trees.
*   Remove or unwrap as many nodes as possible: scripts, attributes, empty elements, `<head>`, comment nodes, foreign/layout elements.
*   If `main > article` exists, use it instead of whole page.

One goal is to remove all of the [chrome](https://www.nngroup.com/articles/browser-and-gui-chrome/) on a page as they're not part of the content, which pollute the context and distort meaning:

*   Menu bars, nav links, banners, footers, site information.
*   Comments sections, asides, links to other articles.
*   Interface elements, forms, controls, social media buttons.

These can get mixed up with the primary content and dilute the search engine's understanding of the page's actual content and intent, causing poor query results.

Removing these is straightforward if the page uses [semantic elements](https://developer.mozilla.org/en-US/curriculum/core/semantic-html/) like `<article>` or [ARIA roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles), but otherwise devolves into heuristics and NLP. Methods like pattern matching on classes and IDs is fraught, and removing content by accident is worse than keeping in noise. More advanced methods like [visually](https://developer.chrome.com/docs/chromium/headless) classifying DOM structure or training [statistical text models](https://fasttext.cc/) are possible given more time and resources.

Given HTML's laxness, many sites don't follow these rules rigorously, so you get undercoverage and overcoverage. Unfortunately, this even applies to some [big](https://en.wikipedia.org/) sites that could not be ignored, so I had to hard code some special rules for them ([much like a well-known browser](https://github.com/WebKit/WebKit/blob/main/Source/WebCore/page/Quirks.cpp)).

Example special rules for en.wikipedia.org
```
if re.match(r"^en\.wikipedia\.org/wiki/", url):
    if tag_name not in HEADING_ELEMS:
        last_heading = find_prev_sibling(child, lambda e: e.tagName in HEADING_ELEMS)
        if (
            last_heading
            and last_heading.tagName == "h2"
            and get_text_content(last_heading).replace("[edit]", "").strip()
            in ("Sources", "Further reading", "External links", "See also")
        ):
            # This is in a section we don't want to keep.
            continue

    classes = set(child.getAttribute("class").split(" "))
    if "hatnote" in classes: continue # Remove "meta" information about the Wikipedia article itself. See https://en.wikipedia.org/wiki/Wikipedia:Hatnote.
    if tag_name == "ol" and "references" in classes: continue # Remove section containing list of references.
    if tag_name == "table" and "sidebar" in classes: continue # Remove sidebar, which sometimes contains useful facts but often just contains "adjacent" information and links, and is hard to parse due to use of table for formatting (not semantics).
    if "thumb" in classes: continue # Remove figures.
    if "navbox" in classes: continue # Remove the navigation boxes at the bottom of the page.
    if "printfooter" in classes: continue # Remove the message "Retrieved from $url".
    if child.getAttribute("id") == "siteSub": continue # Remove the message "From Wikipedia, the free encyclopedia".

    if c.tagName == "sup" and "reference" in classes: continue # Remove numbered references around square brackets within body text.
    if "mw-jump-link" in classes: continue # Remove "Jump to content" link.
    if "mw-editsection" in classes: continue # Remove "[edit]" links.
    if "mw-ui-button" in classes: continue # Remove UI buttons.
    if "wb-langlinks-edit" in classes: continue # Remove "Edit links" link.
    if "mwe-math-fallback-image-display" in classes or "mwe-math-fallback-image-inline" in classes: continue # This is a fallback, we can remove it as we handle <math> elements.
```

There's a lot of rich structured data available on many pages. `<meta>` tags like [OpenGraph](https://ogp.me/) are well-known. There's also an entire [spec](https://schema.org/docs/gs.html) to representing [almost anything](https://schema.org/docs/full.html) in a web page for robots to consume. Search engines use these to power [enhanced rich results](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) and build their [knowledge graphs](https://en.wikipedia.org/wiki/Knowledge_Graph_(Google)). It's how they know something is mentioning a [movie](https://en.wikipedia.org/wiki/Steve_Jobs_(film)) and not a [book](https://en.wikipedia.org/wiki/Steve_Jobs_(book)) or [person](https://en.wikipedia.org/wiki/Steve_Jobs) to improve relevancy, discover new emerging [things](https://en.wikipedia.org/wiki/Ontology) in the world, and show fancy shopping, rating, carousel, and "near me" results.

Chunking
--------

Once the text is ready, the next step is to [chunk it](https://www.pinecone.io/learn/chunking-strategies/). Most embedding models can't take in whole-page inputs and tend to [lose representational power at such lengths](https://jina.ai/news/long-context-embedding-models-are-blind-beyond-4k-tokens/) anyway. Embedding at the page level is also too coarse, not helpful for pinpointing.

A common approach is to simply split at every _n_ characters or words. But this can crudely cut off words, grammar, and structure that destroy meaning. My approach was to break into sentences, a natural coherent boundary, using a trained [sentencizer](https://spacy.io/api/sentencizer). These models are trained on a large corpus of texts and have a good understanding of grammar and syntax for high accuracy. I found spaCy's model to work the best here, handling subtleties like abbreviations, decimals, URLs, and informal style grammar.

It seemed to me that breaking into sentences would be a good atomic unit of detail: enough to pinpoint the exact relevant part or answer to a query, useful for featured direct snippets or result highlights. This would also allow building larger embedding units (e.g. paragraph sized) with more control over length while still maintaining semantic coherence.

### Semantic context

But a big problem with chunking is context. A sentence builds on top of previous sentences, the containing paragraph, current section, actively discussed concepts, and so on. Indirect references ("it", "the", "then", etc.) lose meaning if chunk is broken off from establishing context.

An initial step was to leverage the normalized semantic document tree. For example:

*   Headings indicate nesting or splitting sections; the content under a `<h2>` is associated with that heading's text.
*   Table headings indicate labels for cells in each row; paragraphs indicate semantic text break points; `<dd>` is associated with its `<dt>`; and so on.
*   A "leading" sentence like _Here are the suggested values:_ before a list explains what that list is and so would be associated with that list.

Therefore, a page like:

> PostgreSQL Performance Tuning Guide
> -----------------------------------
> 
> 
> …
> 
> 
> Connection Settings
> -------------------
> 
> 
> …
> 
> 
> ### Maximum connections
> 
> 
> Each connection uses a new process. This is different to most other database systems. Therefore, the setting may have surprising performance impact. Due to this design, connections use more resources than in a thread-based system, and so require extra consideration. Here are some recommended values:
> 
> 
> *   If you are using version 16 or greater: | Environment | Recommended Setting | … |
> | --- | --- | --- |
> | Development | 100 | … |
> | Web Application | 200-400 | … |
> | Data Warehouse | 50-100 | … |
> | Microservices | 20-50 per service | … | 
> *   If you are using version 15: | Environment | Recommended Setting | … |
> | --- | --- | --- |
> | Development | 100 | … |
> | Web Application | 200-400 | … |
> | Data Warehouse | 50-100 | … |
> | Microservices | 20-50 per service | … | 
> 
> 
> …

would represent the first "Development" table row as

```
[
  "PostgreSQL Performance Tuning Guide", // (heading 1)
  "Connection Settings", // (heading 2)
  "Maximum connections", // (heading 3)
  "Here are some recommended values:", // (leading statement before list)
  "If you are using version 16 or greater:", // (leading statement before table)
  "Environment: Development | Recommended Setting: 100 | …", // denormalized row to provide column headings as context
].join("\n")
```

rather than

```
"Development | 100 | …"
```

which loses meaning due to lack of context.

This context also provides disambiguation and relevancy. In the above example, both tables are only differentiated by the version mention before each table.

### Statement chaining

This doesn't resolve the problem of nearby local context: follow on sentences, anaphora, etc. To tackle this further, I trained a [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) classifier model that would take a sentence and the preceding sentences, and label which one (if any) it depends upon in order to retain meaning. Therefore, when embedding a statement, I would follow the "chain" backwards to ensure all dependents were also provided in context.

This also had the benefit of labelling sentences that should never be matched, because they were not "leaf" sentences by themselves.

[![Image 3: Screenshot of the statement labeller UX.](https://blog.wilsonl.in/search-engine/statement-labeller.png)](https://blog.wilsonl.in/search-engine/statement-labeller.png)

 The built internal statement labeller UX for quick labelling with instructions. 

[![Image 4: Screenshot of the statement debug view.](https://blog.wilsonl.in/search-engine/admin-statement-chain-debug.png)](https://blog.wilsonl.in/search-engine/admin-statement-chain-debug.png)

 A statement with its semantic context and AI-labelled antecedent dependent statement. 

Using the previous web page, here is an example:

```
[
  "PostgreSQL Performance Tuning Guide", // heading 1
  "Connection Settings", // heading 2
  "Maximum connections", // heading 3,
  "Each connection uses a new process.", // necessary to understand the sentence
  // ...skipped unnecessary sentences
  "Due to this design, connections use more resources than in a thread-based system, and so require extra consideration.", // the target sentence
].join("\n")
```

Another example that has multiple hops:

```
[
  "PostgreSQL Performance Tuning Guide", // heading 1
  "Connection Settings", // heading 2
  "Maximum connections", // heading 3
  "Each connection uses a new process.", // to understand the next line
  "This is different to most other database systems.", // to understand the next line
  "Therefore, the setting may have surprising performance impact.", // the target sentence
].join("\n")
```

Chunking while preserving context is a hard problem. Anthropic has an interesting analysis and offer their own approach [here](https://www.anthropic.com/news/contextual-retrieval). Another approach that I would experiment with is [late chunking](https://jina.ai/news/late-chunking-in-long-context-embedding-models/).

Initial results
---------------

I built a UX to visualize and interact with pages in my sandbox and test out queries. The results seemed to be pretty good.

For example, on [this S3 documentation page](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html), using a natural language question gave multiple relevant direct answers, not just keyword matches, from disparate snippets that weren't simply in sections directly related to the query:

[![Image 5: Prototype search results for "when should i use multipart uploads?" over S3 documentation.](https://blog.wilsonl.in/search-engine/poc-when-should-i-use-multipart-uploads.png)](https://blog.wilsonl.in/search-engine/poc-when-should-i-use-multipart-uploads.png)
Here's another example, querying [this web page](https://www.psychologytoday.com/us/blog/understanding-the-anxious-mind/202303/are-you-a-life-optimizer-what-to-do-about-perfectionism), where the search engine matched against "It's not worth it", which is arguably the most relevant and direct response, but without context would not make sense and therefore not get matched. The other matches also provide more relevant perspectives to the query.

[![Image 6: Prototype search results for "is perfectionism worth it?" over a blog post on perfectionism.](https://blog.wilsonl.in/search-engine/poc-is-perfectionism-worth-it.png)](https://blog.wilsonl.in/search-engine/poc-is-perfectionism-worth-it.png)
Here are more examples, where the query has very different keywords to their answers, and don't directly refer to them, yet are good matches:

[![Image 7](https://blog.wilsonl.in/search-engine/poc-im-charged-for-invisible-space.png)](https://blog.wilsonl.in/search-engine/poc-im-charged-for-invisible-space.png)

I'm trying to figure out why my billed usage is higher than my actual usage. Without using words from the answer (which I don't know), the search engine finds me the relevant answer.

[![Image 8](https://blog.wilsonl.in/search-engine/poc-race-conditions.png)](https://blog.wilsonl.in/search-engine/poc-race-conditions.png)

The search engine is able to pick up information _related in concept_ to race conditions, despite the article not mentioning "race conditions".

[![Image 9](https://blog.wilsonl.in/search-engine/poc-can-i-use-lua.png)](https://blog.wilsonl.in/search-engine/poc-can-i-use-lua.png)

AWS doesn't have an SDK for Lua. Instead of just giving back no or nonsense results, it points out that I can use the REST API, accessible to all languages.

[![Image 10](https://blog.wilsonl.in/search-engine/poc-what-do-i-pay-for.png)](https://blog.wilsonl.in/search-engine/poc-what-do-i-pay-for.png)

What do I get charged? Without knowing the words and concepts around what S3 multipart upload charges for, and no article section called "what you pay", the search engine knows what to surface.

[![Image 11](https://blog.wilsonl.in/search-engine/poc-how-can-i-attach-some-human-english-comment-to-a-file.png)](https://blog.wilsonl.in/search-engine/poc-how-can-i-attach-some-human-english-comment-to-a-file.png)

The search engine explains what a file is in S3 and how I can achieve my goal. Note that the keywords in the query and results basically don't overlap.

More direct queries that have straightforward (but not exact keyword matching) answers are also matched well:

[![Image 12: Screenshot of first result of query "can i know upload without knowing size ahead of time".](https://blog.wilsonl.in/search-engine/poc-can-i-upload-without-knowing-size-ahead-of-time.png)](https://blog.wilsonl.in/search-engine/poc-can-i-upload-without-knowing-size-ahead-of-time.png)[![Image 13: Screenshot of first result of query "can uploads be interrupted".](https://blog.wilsonl.in/search-engine/poc-can-uploads-be-interrupted.png)](https://blog.wilsonl.in/search-engine/poc-can-uploads-be-interrupted.png)
Plenty of important snippets and statements lie within rich markup like nested table rows, lists, and definitions:

[![Image 14: Screenshot of query for "what permissions do i need to upload".](https://blog.wilsonl.in/search-engine/poc-what-permissions-do-i-need-to-upload.png)](https://blog.wilsonl.in/search-engine/poc-what-permissions-do-i-need-to-upload.png)
Crawler
-------

I felt confident that the pipeline and resulting embeddings deliver good results, so I moved on to building out the actual search engine, starting with a Node.js crawler. Some requirements:

*   A form of work stealing for distributing tasks is likely needed as how long requests take varies significantly.
*   Trust nothing: control and verify DNS resolution, URLs, redirects, headers, and [timers](https://en.wikipedia.org/wiki/Slowloris_(cyber_attack)).
*   Origins often rate limit by IP, so tasks should be distributed across crawlers and handle origin-specific rate limits.
*   Lots of requests = lots of potential memory leaks. Manage resources (sockets, keepalives, pools) strictly, and use streaming wherever possible to keep memory O(1).

The approach ended up being:

*   up to N-per-origin concurrent Promises, which are essentially green threads as primary workload is async I/O
*   self-imposed sliding window and concurrency rate limiting per origin, with jittered delays between requests and exponential backoff between failures
*   use Node.js streams to fetch, decompress, and ingest in fixed-sized buffers for memory usage stability

Each node grabs a diverse set of URLs from the DB across domains, which is then randomly work-stolen across green threads. This multi-level stochastic queues setup reduces contention from needing global coordination, frequent polling due to the high-throughput nature, and excessive hitting of any single origin, compared to simply ordered polling from a global crawl queue.

Origins that are rate limited get excluded when polling for more URLs, and existing polled tasks get sent back to global queue.

[![Image 15: Diagram of multi-level crawl queues.](https://blog.wilsonl.in/search-engine/multi-level-crawl-queues.png)](https://blog.wilsonl.in/search-engine/multi-level-crawl-queues.png)
A surprising failure point was DNS. EAI_AGAIN and SERVFAIL caused a non-insignificant amount of failures. DNS resolution for every crawl was done manually to verify that the resolved IP was not a private IP, to avoid leaking internal data.

There's a surprising amount of detail that I overlook normally. For example, URLs seem straightforward, but can actually be subtle to deal with. All URLs, before entering the system, were strictly processed as they were central to many systems and records:

*   They must have `https:` protocol, not `ftp:`, `data:`, `javascript:`, etc.
*   They must have a valid [eTLD](https://publicsuffix.org/list/) and [hostname](https://en.wikipedia.org/wiki/Hostname#Syntax), and can't have ports, usernames, or passwords.
*   Canonicalization is done to deduplicate. All components are percent-decoded then re-encoded with a minimal consistent charset. Query parameters are dropped or sorted. Origins are lowercased.
*   Some URLs are extremely long, and you can run into rare limits like HTTP headers and database index page sizes.
*   Some URLs also have [strange characters](https://en.wikipedia.org/wiki/C0_and_C1_control_codes) that you wouldn't think would be in a URL, but will get rejected downstream by systems like [PostgreSQL](https://www.postgresql.org/docs/current/datatype-character.html#:~:text=the%20character%20with%20code%20zero%20(sometimes%20called%20NUL)%20cannot%20be%20stored) and [SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html).

Pipeline
--------

[![Image 16: Search engine pipeline state and data flow diagram.](https://blog.wilsonl.in/search-engine/pipeline.png)](https://blog.wilsonl.in/search-engine/pipeline.png)
Each web page was stored in PostgreSQL with a state shown in the above diagram. Workers would poll from PostgreSQL directly using `SELECT ... FOR UPDATE SKIP LOCKED` transactions, transitioning the state once completed. However, lots of long transactions and single-row lock → read → update queries from many distant connections is not efficient with PostgreSQL, so a Rust coordinator service was introduced:

*   Kept entire queue state in memory, and efficiently tracked heartbeats and expiration.
*   Handled locking, state transitions, and integrity via faster in-memory state.
*   Used efficient RPC over multiplexed HTTP/2 with clients and only a few PostgreSQL connections to the DB with queued batched upserts.

This in-memory queue was designed for high throughput:

*   An `Arc<Mutex<Task>>` was shared between three data structures: 
    *   HashMap `task ID -> task` for fetching and mutating tasks.
    *   Binary heap over tasks, keyed by visibility timeouts, for making expired polled tasks available again.
    *   Grouped by origin (`origin` ->`list of tasks in that origin`) for fair scheduling across origins, with separate tracked list of available origins.
    *   Random polling within origin list, with O(1) [`swap_remove`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.swap_remove) of self-indexed position (which also means only one other self-indexed position needs updating, no mass shift-down-by-one).

*   Graceful drift handling was adopted over global locking: 
    *   Atomicity maintained via per-task locks.
    *   Changes in timeout (e.g. heartbeats) don't mutate heap; instead, the latest expiration is re-checked when background loop goes through timeout heap.
    *   An available origin that becomes empty isn't removed from available origins list until next access (poller), amortizing costs.
    *   `Arc<Mutex<Task>>` is source of truth; data structures are merely indices that may be stale (e.g. completed tasks in heap, empty origins in list, phantom polled task).

The result was efficient sublinear complexity for all operations:

| Operation | Time complexity | Process |
| --- | --- | --- |
| **Push task** | O(1) | HashMap insert + Vec push to origin list + update task's stored index |
| **Pop random** | O(k) average _k = excluded origins_ | O(1) random index into origins list → O(1) random index into origin's tasks → O(1) swap_remove using stored index → O(log n) heap push |
| **Complete task** | O(1) | HashMap lookup → lock task → state transition → O(1) swap_remove from origin list using stored index |
| **Heartbeat** | O(1) | HashMap lookup → update timeout in-place (no heap rebuild) |
| **Release timeouts** | O(log n) per task | Heap pop → check if expired → if yes: O(1) push to origin list; if no: O(log n) re-push to heap |
| **Find task** | O(1) | Direct HashMap lookup |

Each task only occupied around 100 bytes of memory, so despite being memory-bound in theory, in reality it was scalable to 1 billion active tasks on a typical 128 GB RAM server.

This also helped with the multi-level stochastic queue setup described previously. Thousands of crawlers all frequently polling a random set of URLs that avoid an arbitrary set of origins, as well as sending back rate limited origin URLs, is a hard database query to optimize for, but more straightforward if global state is kept in memory via a central coordinator.

An interesting optimization was to try and reduce the memory impact of buffering so many URLs in memory:

*   [Interning](https://en.wikipedia.org/wiki/String_interning): avoided copies, which was helpful.
*   [Zstd](https://en.wikipedia.org/wiki/Zstd): doesn't work well on small strings, even with custom trained dictionary.
*   [Trie](https://en.wikipedia.org/wiki/Trie): high memory usage in reality due to pointer widths, usize offsets, sparseness, node allocations.
*   Custom compression algorithm that tries to find patterns in URL components: UUIDs, enums, base64, etc. This was very CPU expensive.

Eventually, this in-memory system was retired in favor of a queue service. SQS had very low concurrent rate limits that could not keep up with the throughput of thousands of workers across the pipeline. SQS was also very expensive, [charging per message](https://aws.amazon.com/sqs/pricing/). I decided to write an [open source RocksDB-based queue](https://github.com/wilsonzlin/queued) that was as simple as SQS, while able to perform 300K operations per second from a single node.

In order to persist the multi-level random/fair scheduling, I appended crawl tasks with a random initial [visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) to approximate shuffling and therefore diversify origins in any sequence of polled tasks. Crawler nodes polled a very large batch rather than one-by-one to continue avoiding excessive global polling via the multi-level queues approach.

Storage
-------

I initially chose Oracle Cloud for infra needs due to their [very low egress costs](https://www.oracle.com/cloud/networking/virtual-cloud-network/pricing/) with 10 TB free per month. As I'd store terabytes of data, this was a good reassurance that if I ever needed to move or export data (e.g. processing, backups), I wouldn't have a hole in my wallet. Their compute was also [far cheaper](https://www.oracle.com/cloud/pricing/) than other clouds, while still being a reliable major provider.

Their object storage service was the initial place for storing raw pages and derived data, and it was similar to S3 in function and performance. However, that quickly ran into scaling issues due to frequency of large-sized writes, which was expected as services like S3 have quite low rate limits — there are [hard limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html), but also dynamic per-account/bucket quotas and hi