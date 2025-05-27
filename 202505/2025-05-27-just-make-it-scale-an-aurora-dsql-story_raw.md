Title: Just make it scale: An Aurora DSQL story

URL Source: https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html

Published Time: 2025-05-27T04:30:00.00Z

Markdown Content:
* * *

May 27, 2025 • 3404 words

![Image 1: Aurora DSQL Team](https://www.allthingsdistributed.com/images/aurora-dsql-header.png)

At re:Invent we announced Aurora DSQL, and since then I’ve had many conversations with builders about what this means for database engineering. What’s particularly interesting isn’t just the technology itself, but the journey that got us here. I’ve been wanting to dive deeper into this story, to share not just the what, but the how and why behind DSQL’s development. Then, a few weeks ago, at our internal developer conference — DevCon — I watched a talk from two of our senior principal engineers (PEs) on building DSQL (a project that started 100% in JVM and finished 100% Rust). After the presentation, I asked [Niko Matsakis](https://www.linkedin.com/in/nicholas-matsakis-615614/) and [Marc Bowes](https://www.linkedin.com/in/marc-bowes-952b5518/) if they’d be willing to work with me to turn their insights into a deeper exploration of DSQL’s development. They not only agreed, but offered to help explain some of the more technically complex parts of the story.

In the blog that follows, Niko and Marc provide deep technical insights on Rust and how we’ve used it to build DSQL. It’s an interesting story on the pursuit of engineering efficiency and why it’s so important to question past decisions – even if they’ve worked very well in the past.

**Note from the author**

Before we get into it, a quick but important note. This was (and continues to be) an ambitious project that requires a tremendous amount of expertise in everything from storage to control plane engineering. Throughout this write-up we've incorporated the learnings and wisdom of many of the Principal and Sr. Principal Engineers that brought DSQL to life. I hope you enjoy reading this as much as I have.

Special thanks to: Marc Brooker, Marc Bowes, Niko Matsakis, James Morle, Mike Hershey, Zak van der Merwe, Gourav Roy, Matthys Styrdom.

A brief timeline of purpose-built databases at AWS [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#a-brief-timeline-of-purpose-built-databases-at-aws)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Since the early days of AWS, the needs of our customers have grown more varied — and in many cases, more urgent. What started with a push to make traditional relational databases easier to manage with the launch of Amazon RDS in 2009 quickly expanded into a portfolio of purpose-built options: DynamoDB for internet-scale NoSQL workloads, Redshift for fast analytical queries over massive datasets, Aurora for those looking to escape the cost and complexity of legacy commercial engines without sacrificing performance. These weren’t just incremental steps—they were answers to real constraints our customers were hitting in production. And time after time, what unlocked the right solution wasn’t a flash of genius, but listening closely and building iteratively, often with the customer in the loop.

Of course, speed and scale aren’t the only forces at play. In-memory caching with ElastiCache emerged from developers needing to squeeze more from their relational databases. Neptune came later, as graph-based workloads and relationship-heavy applications pushed the limits of traditional database approaches. What’s remarkable looking back isn’t just how the portfolio grew, but how it grew in tandem with new computing patterns—serverless, edge, real-time analytics. Behind each launch was a team willing to experiment, challenge prior assumptions, and work in close collaboration with product teams across Amazon. That’s the part that’s harder to see from the outside: innovation almost never happens overnight. It almost always comes from taking incremental steps forward. Building on successes and learning from (but not fearing) failures.

While each database service we’ve launched has solved critical problems for our customers, we kept encountering a persistent challenge: how do you build a relational database that requires no infrastructure management and which scales automatically with load? One that combines the familiarity and power of SQL with genuine serverless scalability, seamless multi-region deployment, and zero operational overhead? Our previous attempts had each moved us closer to this goal. Aurora brought cloud-optimized storage and simplified operations, Aurora Serverless automated vertical scaling, but we knew we needed to go further. This wasn’t just about adding features or improving performance - it was about fundamentally rethinking what a cloud database could be.

Which brings us to Aurora DSQL.

Aurora DSQL [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#aurora-dsql)
---------------------------------------------------------------------------------------------------------------------

The goal with Aurora DSQL’s design is to break up the database into bite-sized chunks with clear interfaces and explicit contracts. Each component follows the Unix mantra—do one thing, and do it well—but working together they are able to offer all the features users expect from a database (transactions, durability, queries, isolation, consistency, recovery, concurrency, performance, logging, and so on).

At a high-level, this is DSQL’s architecture.

![Image 2: Aurora DSQL Architecture Diagram](https://www.allthingsdistributed.com/images/aurora-dsql-architecture.png)
We had already worked out how to handle reads in 2021—what we didn’t have was a good way to scale writes horizontally. The conventional solution for scaling out writes to a database is [two-phase commit (2PC)](https://en.wikipedia.org/wiki/Two-phase_commit_protocol). Each journal would be responsible for a subset of the rows, just like storage. This all works great so long as transactions are only modifying nearby rows. But it gets really complicated when your transaction has to update rows across multiple journals. You end up in a complex dance of checks and locks, followed by an atomic commit. Sure, the happy path works fine in theory, but reality is messier. You have to account for timeouts, maintain liveness, handle rollbacks, and figure out what happens when your coordinator fails — the operational complexity compounds quickly. For DSQL, we felt we needed a new approach – a way to maintain availability and latency even under duress.

Scaling the Journal layer [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#scaling-the-journal-layer)
-------------------------------------------------------------------------------------------------------------------------------------------------

Instead of pre-assigning rows to specific journals, we made the architectural decision to write the entire commit into a single journal, no matter how many rows it modifies. This solved both the atomic and durable requirements of [ACID](https://en.wikipedia.org/wiki/ACID). The good news? This made scaling the write path straightforward. The challenge? It made the read path significantly more complex. If you want to know the latest value for a particular row, you now have to check all the journals, because any one of them might have a modification. Storage therefore needed to maintain connections to every journal because updates could come from anywhere. As we added more journals to increase transactions per second, we would inevitably hit network bandwidth limitations.

The solution was the Crossbar, which separates the scaling of the read path and write path. It offers a subscription API to storage, allowing storage nodes to subscribe to keys in a specific range. When transactions come through, the Crossbar routes the updates to the subscribed nodes. Conceptually, it’s quite simple, but challenging to implement efficiently. Each journal is ordered by transaction time, and the Crossbar has to follow each journal to create the total order.

![Image 3: Aurora DSQL Crossbar Diagram](https://www.allthingsdistributed.com/images/aurora-dsql-crossbar.png)

Adding to the complexity, each layer has to provide a high degree of fan out (we want to be efficient with our hardware), but in the real world, subscribers can fall behind for any number of reasons, so you end up with a bunch of buffering requirements. These problems made us worried about garbage collection, especially GC pauses.

The reality of distributed systems hit us hard here - when you need to read from every journal to provide total ordering, the probability of any host encountering tail latency events approaches 1 surprisingly quickly – something [Marc Brooker has spent some time writing about](https://brooker.co.za/blog/2021/04/19/latency.html).

To validate our concerns, we ran simulation testing of the system – specifically modeling how our crossbar architecture would perform when scaling up the number of hosts, while accounting for occasional 1-second stalls. The results were sobering: with 40 hosts, instead of achieving the expected million TPS in the crossbar simulation, we were only hitting about 6,000 TPS. Even worse, our tail latency had exploded from an acceptable 1 second to a catastrophic 10 seconds. This wasn’t just an edge case - it was fundamental to our architecture. Every transaction had to read from multiple hosts, which meant that as we scaled up, the likelihood of encountering at least one GC pause during a transaction approached 100%. In other words, at scale, nearly every transaction would be affected by the worst-case latency of any single host in the system.

Short term pain, long term gain [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#short-term-pain-long-term-gain)
------------------------------------------------------------------------------------------------------------------------------------------------------------

We found ourselves at a crossroads. The concerns about garbage collection, throughput, and stalls weren’t theoretical – they were very real problems we needed to solve. We had options: we could dive deep into JVM optimization and try to minimize garbage creation (a path many of our engineers knew well), we could consider C or C++ (and lose out on memory safety), or we could explore Rust. We chose Rust. The language offered us predictable performance without garbage collection overhead, memory safety without sacrificing control, and zero-cost abstractions that let us write high-level code that compiled down to efficient machine instructions.

The decision to switch programming languages isn’t something to take lightly. It’s often a [one-way door](https://www.youtube.com/watch?v=rxsdOQa_QkM) — once you’ve got a significant codebase, it’s extremely difficult to change course. These decisions can make or break a project. Not only does it impact your immediate team, but it influences how teams collaborate, share best practices, and move between projects.

Rather than tackle the complex Crossbar implementation, we chose to start with the Adjudicator – a relatively simple component that sits in front of the journal and ensures only one transaction wins when there are conflicts. This was our team’s first foray into Rust, and we picked the Adjudicator for a few reasons: it was less complex than the Crossbar, we already had a Rust client for the journal, and we had an existing JVM (Kotlin) implementation to compare against. This is the kind of pragmatic choice that has served us well for over two decades – start small, learn fast, and adjust course based on data.

We assigned two engineers to the project. They had never written C, C++, or Rust before. And yes, there were plenty of battles with the compiler. The Rust community has a saying, “[with Rust you have the hangover first](https://nostarch.com/blog/software-engineer-jon-gjengset-gets-nitty-gritty-rust).” We certainly felt that pain. We got used to the compiler telling us “no” a lot.

![Image 4: Compiler says “No” image](https://www.allthingsdistributed.com/images/aurora-dsql-compiler-no.jpeg)

(Image by Lee Baillie)

But after a few weeks, it compiled and the results surprised us. The code was 10x faster than our carefully tuned Kotlin implementation – despite no attempt to make it faster. To put this in perspective, we had spent years incrementally improving the Kotlin version from 2,000 to 3,000 transactions per second (TPS). The Rust version, written by Java developers who were new to the language, clocked 30,000 TPS.

This was one of those moments that fundamentally shifts your thinking. Suddenly, the couple of weeks spent learning Rust no longer looked like a big deal, when compared with how long it’d have taken us to get the same results on the JVM. We stopped asking, “Should we be using Rust?” and started asking “Where else could Rust help us solve our problems?”

Our conclusion was to rewrite our data plane entirely in Rust. We decided to keep the control plane in Kotlin. This seemed like the best of both worlds: high-level logic in a high-level, garbage collected language, do the latency sensitive parts in Rust. This logic didn’t turn out to be quite right, but we’ll get to that later in the story.

It’s easier to fix one hard problem then never write a memory safety bug [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#its-easier-to-fix-one-hard-problem-then-never-write-a-memory-safety-bug)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Making the decision to use Rust for the data plane was just the beginning. We had decided, after quite a bit of internal discussion, to build on PostgreSQL (which we’ll just call Postgres from here on). The modularity and extensibility of Postgres allowed us to use it for query processing (i.e., the parser and planner), while replacing replication, concurrency control, durability, storage, the way transaction sessions are managed.

But now we had to figure out how to go about making changes to a project that started in 1986, with over a million lines of C code, thousands of contributors, and continuous active development. The easy path would have been to hard fork it, but that would have meant missing out on new features and performance improvements. We’d seen this movie before - forks that start with the best intentions but slowly drift into maintenance nightmares.

Extension points seemed like the obvious answer. Postgres was designed from the beginning to be an extensible database system. These extension points are part of Postgres’ public API, allowing you to modify behavior without changing core code. Our extension code could run in the same process as Postgres but live in separate files and packages, making it much easier to maintain as Postgres evolved. Rather than creating a hard fork that would drift further from upstream with each change, we could build on top of Postgres while still benefiting from its ongoing development and improvements.

The question was, do we write these extensions in C or Rust? Initially, the team felt C was a better choice. We already had to read and understand C to work with Postgres, and it would offer a lower impedance mismatch. As the work progressed though, we realized a critical flaw in this thinking. The Postgres C code is reliable: it’s been thoroughly battled tested over the years. But our extensions were freshly written, and every new line of C code was a chance to add some kind of memory safety bug, like a use-after-free or buffer overrun. The “a-ha!” moment came during a code review when we found several memory safety issues in a seemingly simple data structure implementation. With Rust, we could have just grabbed a proven, memory-safe implementation from Crates.io.

Interestingly, the [Android team published research last September](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html) that confirmed our thinking. Their data showed that the vast majority of new bugs come from new code. This reinforced our belief that to prevent memory safety issues, we needed to stop introducing memory-unsafe code altogether.

![Image 5: New Memory Unsafe Code and Memory safety Vulns](https://www.allthingsdistributed.com/images/aurora-dsql-google-mem-safe-vulns.png)

(Research from the Android team shows that most new bugs come from new code. So if you pick a memory safe language – you prevent memory safety bugs.)

We decided to pivot and write the extensions in Rust. Given that the Rust code is interacting closely with Postgres APIs, it may seem like using Rust wouldn’t offer much of a memory safety advantage, but that turned out not to be true. The team was able to create abstractions that enforce safe patterns of memory access. For example, in C code it’s common to have two fields that need to be used together safely, like a `char*` and a `len` field. You end up relying on conventions or comments to explain the relationship between these fields and warn programmers not to access the string beyond len. In Rust, this is wrapped up behind a single String type that encapsulates the safety. We found many examples in the Postgres codebase where header files had to explain how to use a struct safely. With our Rust abstractions, we could encode those rules into the type system, making it impossible to break the invariants. Writing these abstractions had to be done very carefully, but the rest of the code could use them to avoid errors.

It’s a reminder that decisions about scalability, security, and resilience should be prioritized – even when they’re difficult. The investment in learning a new language is minuscule compared to the long-term cost of addressing memory safety vulnerabilities.

About the control plane [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#about-the-control-plane)
---------------------------------------------------------------------------------------------------------------------------------------------

Writing the control plane in Kotlin seemed like the obvious choice when we started. After all, services like Amazon’s Aurora and RDS had proven that JVM languages were a solid choice for control planes. The benefits we saw with Rust in the data plane – throughput, latency, memory safety – weren’t as critical here. We also needed internal libraries that weren’t yet available in Rust, and we had engineers that were already productive in Kotlin. It was a practical decision based on what we knew at the time. It also turned out to be the wrong one.

At first, things went well. We had both the data and control planes working as expected in isolation. However, once we started integrating them together, we started hitting problems. DSQL’s control plane does a lot more than CRUD operations, it’s the brain behind our hands-free operations and scaling, detecting when clusters get hot and orchestrating topology changes. To make all this work, the control plane has to share some amount of logic with the data plane. Best practice would be to create a shared library to avoid “[repeating ourselves](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)”. But we couldn’t do that, because we were using different languages, which meant that sometimes the Kotlin and Rust versions of the code were slightly different. We also couldn’t share testing platforms, which meant the team had to rely on documentation and whiteboard sessions to stay aligned. And every misunderstanding, even a small one, led to a costly debug-fix-deploy cycles. We had a hard decision to make. Do we spend the time rewriting our [simulation tools](https://brooker.co.za/blog/2022/04/11/simulation.html) to work with both Rust and Kotlin? Or do we rewrite the control plane in Rust?

The decision wasn’t as difficult this time around. A lot had changed in a year. Rust’s 2021 edition had addressed many of the pain points and paper cuts we’d encountered early on. Our internal library support had expanded considerably – in some cases, such as the AWS Authentication Runtime client, the Rust implementations were outperforming their Java counterparts. We’d also moved many integration concerns to API Gateway and Lambda, simplifying our architecture.

But perhaps most surprising was the team’s response. Rather than resistance to Rust, we saw enthusiasm. Our Kotlin developers weren’t asking “do we have to?” They were asking “when can we start?” They’d watched their colleagues working with Rust and wanted to be part of it.

A lot of this enthusiasm came from how we approached learning and development. Marc Brooker had written what we now call “The DSQL Book” – an internal guide that walks developers through everything from philosophy to design decisions, including the hard choices we had to defer. The team dedicated time each week to learning sessions on distributed computing, paper reviews, and deep architectural discussions. We brought in Rust experts like Niko who, true to our working backwards approach, helped us think through thorny problems before we wrote a single line of code. These investments didn’t just build technical knowledge – they gave the team confidence that they could tackle complex problems in a new language.

When we took everything into account, the choice was clear. It was Rust. We needed the control and data planes working together in simulation, and we couldn’t afford to maintain critical business logic in two different languages. We had observed significant throughput performance in the crossbar, and once we had the entire system written in Rust tail latencies were remarkably consistent. Our p99 latencies tracked very close to our p50 medians, meaning even our slowest operations maintained predictable, production-grade performance.

It’s so much more than just writing code [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#its-so-much-more-than-just-writing-code)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Rust turned out to be a great fit for DSQL. It gave us the control we needed to avoid tail latency in the core parts of the system, the flexibility to integrate with a C codebase like Postgres, and the high-level productivity we needed to stand up our control plane. We even wound up using Rust (via WebAssembly) to power our internal ops web page.

We assumed Rust would be lower productivity than a language like Java, but that turned out to be an illusion. There was definitely a learning curve, but once the team was ramped up, they moved just as fast as they ever had.

This doesn’t mean that Rust is right for every project. Modern Java implementations like JDK21 offer great performance that is more than enough for many services. The key is to make these decisions the same way you make other architectural choices: based on your specific requirements, your team’s capabilities, and your operational environment. If you’re building a service where tail latency is critical, Rust might be the right choice. But if you’re the only team using Rust in an organization standardized on Java, you need to carefully weigh that isolation cost. What matters is empowering your teams to make these choices thoughtfully, and supporting them as they learn, take risks, and occasionally need to revisit past decisions. That’s how you build for the long term.

Now, go build!

Recommended reading [](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html#recommended-reading)
-------------------------------------------------------------------------------------------------------------------------------------

If you’d like to learn more about DSQL and the thinking behind it, Marc Brooker has written an in-depth set of posts called DSQL Vignettes:

*   [Aurora DSQL, and A Personal Story](https://brooker.co.za/blog/2024/12/03/aurora-dsql.html)
*   [Reads and Compute](https://brooker.co.za/blog/2024/12/04/inside-dsql.html)
*   [Transactions and Durability](https://brooker.co.za/blog/2024/12/05/inside-dsql-writes.html)
*   [Wait! Isn’t That Impossible?](https://brooker.co.za/blog/2024/12/06/inside-dsql-cap.html)

* * *
