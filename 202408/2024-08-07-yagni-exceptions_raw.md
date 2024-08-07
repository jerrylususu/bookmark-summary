Title: YAGNI exceptions

URL Source: https://lukeplant.me.uk/blog/posts/yagni-exceptions/

Published Time: 2021-06-29T09:42:00+01:00

Markdown Content:
I'm essentially a believer in [You Aren't Gonna Need It](https://martinfowler.com/bliki/Yagni.html) – the principle that you should add features to your software – including generality and abstraction – when it becomes clear that you need them, and not before.

However, there are some things which really are easier to do earlier than later, and where natural tendencies or a ruthless application of YAGNI might neglect them. This is my collection so far:

*   Applications of [Zero One Many](http://wiki.c2.com/?ZeroOneInfinityRule). If the requirements go from saying “we need to be able to store an address for each user”, to “we need to be able to store two addresses for each user”, 9 times out of 10 you should go straight to “we can store many addresses for each user”, with a soft limit of two for the user interface only, because there is a very high chance you will need more than two. You will almost certainly win significantly by making that assumption, and even if you lose it won't be by much.
    
*   Versioning. This can apply to protocols, APIs, file formats etc. It is good to think about how, for example, a client/server system will detect and respond to different versions ahead of time (i.e. even when there is only one version), especially when you don't control both ends or can't change them together, because it is too late to think about this when you find you need a version 2 after all. This is really an application of [Embrace Change](http://wiki.c2.com/?EmbraceChange), which is a principle at the heart of YAGNI.
    
*   Logging. Especially for after-the-fact debugging, and in non-deterministic or hard to reproduce situations, where it is often too late to add it after you become aware of a problem.
    
*   Timestamps.
    
    For example, creation timestamps, as [Simon Willison tweeted](https://twitter.com/simonw/status/1384580075329179650):
    
    > A lesson I re-learn on every project: always have an automatically populated "created\_at" column on every single database table. Any time you think "I won't need it here" you're guaranteed to want to use it for debugging something a few weeks later.
    
    More generally, instead of a boolean flag, e.g. `completed`, a nullable timestamp of when the state was entered, `completed_at`, can be much more useful.
    
*   Generalising from the “logging” and “timestamps” points, collecting a bit more data than you need right now is usually not a problem (unless it is personal or otherwise sensitive data), because you can always throw it away. But if you never collected it, it's gone forever. I have won significantly when I've anticipated the need for auditing which wasn't completely explicit in the requirements, and I've lost significantly when I've gone for data minimalism which lost key information and limited what I could do with the data later.
    
*   A relational database.
    
    By this I mean, if you need a database at all, you should jump to having a relational one straight away, and default to a relational schema, even if your earliest set of requirements could be served by a “document database” or some basic flat-file system. Most data is relational by nature, and a non-relational database is a very bad default for almost all applications.
    
    If you choose a relational database like PostgreSQL, and it later turns out a lot of your data is “document like”, you can use its [excellent support for JSON](https://www.postgresql.org/docs/current/datatype-json.html).
    
    However, if you choose a non-rel DB like MongoDB, even when it seems like you've got a perfect fit in terms of current schema needs, most likely a new, “simple” requirement will cause you a lot of pain, and [prompt a rewrite in Postgres](http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/) (see sections “How MongoDB Stores Data” and “Epilogue” in that article).
    
    I thought [a comment on Lobsters](https://lobste.rs/s/63eb9g/when_rewrite#c_7gwj71) I read the other day was insightful here:
    
    > I wonder if the reason that “don’t plan, don’t abstract, don’t engineer for the future” is such good advice is that most people are already building on top of highly-abstracted and featureful platforms, which don’t need to be abstracted further?
    
    We can afford to do YAGNI only when the systems we are working with are malleable and featureful. Relational databases are extremely flexible systems that provide insurance against future requirements changes. For example, my advice in the previous section implicitly depends on the fact that removing data you don't need can be as simple as "DROP COLUMN", which is [almost free](https://stackoverflow.com/questions/15699989/dropping-column-in-postgres-on-a-large-dataset) (well, sometimes…).
    

That's my list so far, I'll probably add to it over time. Do you agree? What did I miss?

Links
-----

*   [Discussion of this post on Lobsters](https://lobste.rs/s/quywfp/yagni_exceptions_2021)
    
*   [Discussion of this post on Twitter](https://twitter.com/spookylukey/status/1409967250426281984).
    
*   [Simon Willison's response post on PAGNIs](https://simonwillison.net/2021/Jul/1/pagnis/) with [Twitter discussion](https://twitter.com/simonw/status/1410678459756552198) and [Lobsters discussion](https://lobste.rs/s/nokjr0/pagnis_probably_are_gonna_need_its).
    
*   [Jacob Kaplan-Moss's response post on security PAGNIs](https://jacobian.org/2021/jul/8/appsec-pagnis/), and [Twitter discussion](https://twitter.com/jacobian/status/1413157068375302146).
