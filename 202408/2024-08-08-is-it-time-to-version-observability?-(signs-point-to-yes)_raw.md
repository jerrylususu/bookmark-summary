Title: Is It Time To Version Observability? (Signs Point To Yes)

URL Source: https://charity.wtf/2024/08/07/is-it-time-to-version-observability-signs-point-to-yes/

Published Time: 2024-08-07T22:57:19+00:00

Markdown Content:
Augh! I am _so behind_ on _so much writing_, I’m even behind on writing shit that I need to reference in order to write other pieces of writing. Like this one. So we’re just gonna do this quick and dirty on the personal blog, and not bother bringing it up to the editorial standards of…anyone else’s sites. 😬

If you’d rather consume these ideas in other ways:

*   I gave a [keynote at SRECon](https://www.usenix.org/conference/srecon24americas/presentation/majors-plenary) in March
*   Here is a slide deck of [my slides from CTO Craft Con London](https://speakerdeck.com/charity/cto-craft-con-keynote-observability-is-due-for-a-version-change-are-you-ready-for-it) in May
*   A [Screaming In The Cloud podcast](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/shifting-from-observability-1-0-to-2-0-with-charity-majors/) with Corey Quinn in April
*   My piece earlier in the year on the [Cost Crisis in Observability Tooling](https://www.honeycomb.io/blog/cost-crisis-observability-tooling) touched on some of the concepts too
*   [Matt Sanabria](http://twitter.com/sudomateo) wrote a great piece [comparing us and a bunch of other observability vendors](https://matthewsanabria.dev/posts/observability-companies-to-watch-in-2024/) in 2024.

What does observability mean? No one knows
------------------------------------------

In 2016, we first borrowed the term “observability” from the wikipedia entry for [control systems observability](https://en.m.wikipedia.org/wiki/Observability), where it is a measure of your ability to understand internal system states just by observing its outputs. We ([Honeycomb](http://honeycomb.io/)) then spent a couple of years trying to work out how that definition might apply to software systems. Many twitter threads, podcasts, [blog](https://charity.wtf/2020/03/03/observability-is-a-many-splendored-thing/) [posts](https://www.honeycomb.io/blog/observability-a-manifesto) and lengthy [laundry lists](https://thenewstack.io/observability-a-3-year-retrospective/) of [technical criteria](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool) [emerged from](https://www.honeycomb.io/blog/why-observability-requires-distributed-column-store) that work, including a [whole ass book](https://www.amazon.com/Observability-Engineering-Charity-Majors-ebook/dp/B09ZQ6FHTT).

![Image 1: Metrics, logs, tracing, drama](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-44.jpeg?resize=204%2C189&ssl=1)

In 2018, Peter Bourgon wrote a [blog post](https://peter.bourgon.org/blog/2017/02/21/metrics-tracing-and-logging.html) proposing that “observability has three pillars: metrics, logs and traces. Ben Sigelman did a masterful job of unpacking why [metrics, logs and traces are just telemetry](https://softwareengineeringdaily.com/2021/02/04/debunking-the-three-pillars-of-observability-myth/). However, lots of people latched on to the three pillars language: vendors because they (coincidentally!) had metrics products, logging products, and tracing products to sell, engineers because it described their daily reality.

Since then the industry has been stuck in kind of a weird space, where the language used to describe the problems and solutions has evolved, but the solutions themselves are largely the same ones as five years ago, or ten years ago. They’ve improved, of course — _massively_ improved — but structurally they’re variations on the same old pre-aggregated metrics.

It has gotten harder and harder to speak clearly about different philosophical approaches and technical solutions without wading deep into the weeds, where no one but experts should reasonably have to go.

This is what semantic versioning was made for
---------------------------------------------

Look, I am not here to be the language police. I stopped correcting people on twitter back in 2019. We all do observability! One big happy family. 👍

I AM here to help engineers think clearly and crisply about the problems in front of them. So here we go. Let’s call the metrics, logs and traces crowd — the “three pillars” generation of tooling — that’s “**Observability 1.0**“. Tools that honeycomb that are built based on [arbitrarily-wide](https://www.honeycomb.io/blog/structured-events-basis-observability) [structured log](https://www.honeycomb.io/blog/how-are-structured-logs-different-from-events) [events](https://charity.wtf/2019/02/05/logs-vs-structured-events/), a [single source of truth](https://charity.wtf/2022/08/15/live-your-best-life-with-structured-events/) — that’s “**Observability 2.0**“.

Here is the twitter thread where I first teased out the differences between these generations of tooling (all the way back in December, yes, that’s how long I’ve been meaning to write this 😅).

> About two months ago I wrote this thread about how we lost the battle to define ✨observability✨ -- to give it a real, specific, falsifiable technical definition, distinct from monitoring or telemetry.
> 
> I complained, I argued, I grieved...and now I'm over it. SO over it. 🙄 [https://t.co/QH3U0iZZ8G](https://t.co/QH3U0iZZ8G)
> 
> — Charity Majors (@mipsytipsy) [December 22, 2023](https://twitter.com/mipsytipsy/status/1738048200630792245?ref_src=twsrc%5Etfw)

This is literally the problem that semantic versioning was designed to solve, by the way. Major version bumps are reserved for _backwards-incompatible, breaking changes,_ and that’s what this is. **You cannot simultaneously store your data across both multiple pillars _and_ a single source of truth.**

Incompatible. Breaking change. O11y 1.0, meet O11y 2.0.

small technical changes can unlock waves of powerful sociotechnical transformation
----------------------------------------------------------------------------------

There are a LOT of ramifications and consequences that flow from this one small change in how your data gets stored. I don’t have the time or space to go into all of them here, but I will do a quick overview of the most important ones.

![Image 2: The Cloud: A Cautionary Tale](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-43.jpeg?resize=199%2C200&ssl=1)

The historical analogue that keeps coming to mind for me is virtualization. VMs are old technology, they’ve been around since the 70s. But it wasn’t until the late 90s that VMware productized it, unlocking wave after wave of change, from cloud computing and SaaS to the very DevOps movement itself.

I believe the shift to observability 2.0 holds a similarly massive potential for change, based on what I see happening today, with teams who have already made the leap. Why?  In a word, precision. O11y 1.0 _can only ever give you_ _aggregates and random exemplars._ O11y 2.0, on the other hand, can tell you _precisely_ what happened when you flipped a flag, deployed to a canary, or made any other change in production.

Will these waves of sociotechnical transformation ever be realized? Who knows. The changes that get unlocked will depend to some extent on us (Honeycomb), and to an even greater extent on engineers like you. Anyway, I’ll talk about this more some other time. Right now, I just want to establish a baseline for this vocabulary.

1.0 vs 2.0: How does the data get stored?
-----------------------------------------

**1.0💙** O11y 1.0 has many sources of truth, in many different formats. Typically, you end up storing your data across metrics, logs, traces, APM, RUM, profiling, and possibly other tools as well. Some folks even find themselves falling back to B.I. (business intelligence) tools like Tableau in a pinch to understand what’s happening on their systems.

Each of these tools are siloed, with no connective tissue, or only a few, predefined connective links that connect e.g. a specific metric to a specific log line. Aggregation is done at write time, so you have to decide up front which data points to collect and which questions you want to be able to ask. You may find yourself eyeballing graph shapes and assuming they must be the same data, or copy-pasting IDs around from logging to tracing tools and back.

![Image 3: Wide Events are Kenough](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-47.jpeg?resize=227%2C141&ssl=1)

**2.0 💚** Data gets stored in [arbitrarily-wide structured](https://brandur.org/nanoglyphs/025-logs) [log events](https://x.com/mipsytipsy/status/1042817542648082432) (often [called](https://baselime.io/blog/canonical-log-lines) “[canonical logs](https://stripe.com/blog/canonical-log-lines)“), often with trace and span IDs appended. You can visualize the events over time as a

trace, or slice and dice your data to zoom in to individual events, or zoom out to a birds-eye view. You can interact with your data by group by, break down, etc.

You aggregate at read time, and preserve raw events for ad hoc querying. Hopefully, you derive your SLO data from the same data you query! Think of it as B.I. for systems/app/business data, all in one place. You can derive metrics, or logs, or traces, but it’s all the same data.

1.0 vs 2.0: on metrics vs logs
------------------------------

**1.0** 💙 The [workhorse of o11y 1.0 is metrics](https://www.honeycomb.io/resources/cost-crisis-metrics-tooling). RUM tools are built on metrics to understand browser user sessions. APM tools are built using metrics to understand application performance. Long ago, the decision was made to use metrics as the source of truth  for telemetry because they are cheap and fast, and hardware used to be incredibly expensive.

The more complex our systems get, the worse of a tradeoff this becomes. Metrics are a terrible building block for understanding rich data, because you have to discard all that![Image 4: To live is to suffer, to survive is to impose a post-hoc narrative](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-42.jpeg?resize=238%2C138&ssl=1) valuable context at write time, and they don’t support high (or even medium!) cardinality data. All you can do to enrich the data is via tags.

Metrics are a great tool for _cheaply_ _summarizing_ vast quantities of data. They are not equipped to help you introspect or understand complex systems. You will go broke and go mad if you try.

**2.0** 💚 The building block of o11y 2.0 is wide, structured log events. Logs are infinitely more powerful, useful and cost-effective than metrics are because they preserve context and relationships between data, and data is _made valuable_ by context. Logs also allow you to capture high cardinality data and data relationships/structures, which give you the ability to compute outliers and identify related events.

1.0 vs 2.0: Who uses it, and how?
---------------------------------

**1.0** 💙 Observability 1.0 is predominantly about how you _operate_ your code. It centers around errors, incidents, crashes, bugs, user reports and problems. MTTR, MTTD, and reliability are top concerns.

O11y 1.0 is typically consumed using static dashboards — lots and lots of static dashboards. “Single pane of glass” is often mentioned as a holy grail. It’s easy to find something once you know what you’re looking for, but you need to know to look for it before you can find it.

**2.0** 💚 If o11y 1.0 is about how you operate your code, o11y 2.0 is about how you _develop_ your code. O11y 2.0 is what underpins the entire software development lifecycle, enabling engineers to connect feedback loops end to end so they get fast feedback on the changes they make, while it’s still fresh in their heads. **This is the foundation of your team’s![Image 5: This Span Could Have Been An Attribute](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-56.jpeg?resize=200%2C201&ssl=1) ability to move swiftly, with confidence.** It isn’t just about understanding bugs and outages, it’s about proactively understanding your software and how your users are experiencing it.

Thus, o11y 2.0 has a much more exploratory, open-ended interface. Any dashboards should be dynamic, allowing you to drill down into a question or follow a trail of breadcrumbs as part of the debugging/understanding process. The canonical question of o11y 2.0 is “here’s a thing I care about … _why_ do I care about it? What are all of the ways it is different from all the other things I _don’t_ care for?”

When it comes to understanding your software, it’s often harder to identify the question than the answer. Once you know what the question is, you probably know the answer too. With o11y 1.0, it’s very easy to find something once _you know what you’re looking for_. With o11y 2.0, that constraint is removed.

1.0 vs 2.0: How do you interact with production?
------------------------------------------------

**1.0** 💙 You deploy your code and wait to get paged. 🤞 Your job is done as a developer when you commit your code and tests pass.

**2.0** 💚 You practice observability-driven development: as you write your code, you instrument it. You deploy to production, then inspect your code through the lens of the instrumentation you just wrote. Is it behaving the way you expected it to? Does anything else look … weird?

Your job as a developer isn’t done until you know it’s working in production. Deploying to production is the _beginning_ of gaining confidence in your code, not the denouement.

1.0 vs 2.0: How do you debug?
-----------------------------

**1.0** 💙 You flip from dashboard to dashboard, pattern-matching and looking for similar shapes with your eyeballs.

You lean heavily on intuition, educated guesses, past experience, and a mental model of the![Image 6: Observability: high cardinality, high dimensionality, explorability](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-39.jpeg?resize=195%2C200&ssl=1) system. This means that the best debuggers are ALWAYS the engineers who have been there the longest and seen the most.

Your debugging sessions are [_search-first_](https://www.honeycomb.io/blog/the-true-cost-of-search-first-problem-solving-on-your-production-systems): you start by searching for something you know should exist.

**2.0** 💚 You check your instrumentation, or you watch your SLOs. If something looks off, you see what all the mysterious events have in common, or you start forming hypotheses, asking a question, considering the result, and forming another one based on the answer. You interrogate your systems, following the trail of breadcrumbs to the answer, every time.

You don’t have to guess or rely on elaborate, inevitably out-of-date mental models. The data is right there in front of your eyes. The best debuggers are the people who are the most curious.

Your debugging questions are [_analysis-first_](https://www.honeycomb.io/blog/the-true-cost-of-search-first-problem-solving-on-your-production-systems): you start with your user’s experience.

1.0 vs 2.0: The cost model
--------------------------

**1.0** 💙 You pay to store your data again and again and again and again, multiplied by all the different formats and tool types you are paying to store it in. Cost goes up at a multiplier of your traffic increase. I wrote a whole piece earlier this year on the [cost crisis in observability tooling](https://www.honeycomb.io/blog/cost-crisis-observability-tooling), so I won’t go into it in depth here.

As your costs increase, the value you get out of your tools actually _decreases_.

If you are using metrics-based products, your costs go up based on cardinality. “Custom metrics” is a euphemism for “cardinality”; “100 free custom metrics” actually means “100 free cardinality”, aka unique values.

**2.0** 💚 You pay to store your data once. As your costs go up, the value you get out goes up too. You have powerful, surgical options for controlling costs via head-based or tail-based dynamic sampling.![Image 7: Every Pillar Has Its Price](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-35.jpeg?resize=200%2C200&ssl=1)

You can have infinite cardinality. You are encouraged to pack hundreds or thousands of dimensions in per event, and any or all of those dimensions can be any data type you want. This luxurious approach to cardinality and data is one of the least well understood aspects of the switch from o11y 1.0 to 2.0.

Many observability engineering teams have spent their entire careers massaging cardinality to control costs. What if you just .. didn’t have to do that? What would you do with your lives? If you could just store and query on all the crazy strings you want, forever? 🌈

Metrics are a bridge to our past
--------------------------------

Why are observability 1.0 tools so unbelievably, eyebleedingly expensive? As anyone who works with data can tell you, this is always what happens when you use the wrong tool for the job. Once again, metrics are a great tool for _summarizing_ vast quantities of data. When it comes to understanding complex systems, they flail.

I wrote a [whole whitepaper earlier this year](https://www.honeycomb.io/resources/cost-crisis-metrics-tooling) that did a deep dive into exactly why tools built on top of metrics are so unavoidably costly. If you want the gnarly detail, download that.

The TLDR is this: tools built on metrics — whether RUM, APM, dashboards, etc — are a bridge to our past. If there’s one thing I’m certain of, it’s that **tools built on top of wide, structured logs are the bridge to our future.**

Wide, structured log events are the bridge to our future
--------------------------------------------------------

Five years from now, I predict that the center of gravity will have swung dramatically; all modern engineering teams will be powering their telemetry off of tools backed by wide, structured log events, not metrics. It’s getting harder and harder and harder to try and wring relevant insights out of metrics-based observability tools. The end of the ZIRP era is bringing unprecedented cost pressure to bear, and it’s simply a matter of time.

**The future belongs to tools built on wide, structured log events — a single source of truth that you can trace over time, or zoom in, zoom out, derive SLOs from, etc.![Image 8: Unstructured Logs Go Here (Trash)](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-8.jpeg?resize=205%2C179&ssl=1)**

It’s the _only_ way to understand our systems in all their skyrocketing complexity. This constant dance with cost vs cardinality consumes entire teams worth of engineers and adds zero value. It adds _negative_ value.

And here’s the weirdest part. The main thing holding most teams back psychologically from embracing o11y 2.0 seems to be the entrenched difficulties they have grappling with o11y 1.0, and their sense that they can’t adopt 2.0 until they get a handle on 1.0. Which gets things exactly backwards.

Because observability 2.0 is so much easier, simpler, and more cost effective than 1.0.

observability 1.0 \*is\* the hard way
-------------------------------------

It’s _so fucking hard_. We’ve been doing it so long that we are blind to just how HARD it is. But trying to teach teams of engineers to wrangle metrics, to squeeze the questions they want to ask into multiple abstract formats scattered across many different tools, with no visibility into what they’re doing until it comes out eventually in form of a giant bill… it’s fucking _hard_.

Observability 2.0 is so much simpler. You want data, you just toss it in. Format? don’t care. Cardinality? don’t care.

You want to ask the question, you just ask it. Format? don’t care.

Teams are beating themselves up trying to master an archaic, unmasterable set of technical tradeoffs based on data types from the 80s. It’s an unwinnable war. We can’t understand today’s complex systems without context-rich, explorable data.

We need more options for observability 2.0 tooling
--------------------------------------------------

My hope is that by sketching out these technical differences between o11y 1.0 and 2.0, we can begin to collect and build up a vendor-neutral library of o11y 2.0 options for folks. The world needs more options for understanding complex systems besides just [Honeycomb](http://honeycomb.io/) and [Baselime](http://baselime.io/).

The world _desperately_ needs an open source analogue to Honeycomb — something built for wide structured events, stored in a [columnar store](https://www.honeycomb.io/blog/why-observability-requires-distributed-column-store/) (or even just Clickhouse), with an interactive interface. Even just a written piece on how you solved it at your company would help move the industry forward.![Image 9: Reinstrument my code with opentelemetry ... or go fuck myself??](https://i0.wp.com/charity.wtf/wp-content/uploads/2024/08/newpix-36.jpeg?resize=287%2C121&ssl=1)

My other hope is that people will **stop building new observability startups built on metrics**. Y’all, Datadog and Prometheus are the last, best metrics-backed tools that will ever be built. You can’t catch up to them or beat them at that; no one can. Do something different. Build for the next generation of software problems, not the last generation.

If anyone knows of anything along these lines, please send me links? I will happily collect them and signal boost. Honeycomb is a great, lifechanging tool (and we have a generous free tier, hint hint) but one option does not a movement make.

<3 charity

P.S. Here’s a great piece written by [Ivan Burmistrov](http://twitter.com/isburmistrov) on his experience using observability 2.0 type tooling at Facebook — namely [Scuba](https://research.facebook.com/publications/scuba-diving-into-data-at-facebook/), which was the inspiration for Honeycomb. [It’s a terrific piece and you should read it.](https://isburmistrov.substack.com/p/all-you-need-is-wide-events-not-metrics)

P.P.S. And if you’re curious, here’s the long twitter thread I wrote in October of 2023 on how we lost the battle to define observability:

> So, we lost the battle to define observability. You know it, I know it. Observability was supposed to \*mean\* something, and in the early days, it did.
> 
> "Observability" once meant the kind of exploratory, open ended investigation our systems increasingly demand.
> 
> — Charity Majors (@mipsytipsy) [October 30, 2023](https://twitter.com/mipsytipsy/status/1719066099973849590?ref_src=twsrc%5Etfw)
