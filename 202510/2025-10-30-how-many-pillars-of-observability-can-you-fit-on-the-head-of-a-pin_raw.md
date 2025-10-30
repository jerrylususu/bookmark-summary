Title: How many pillars of observability can you fit on the head of a pin?

URL Source: https://charity.wtf/2025/10/30/the-pillar-is-a-lie/

Published Time: 2025-10-30T05:27:38+00:00

Markdown Content:
My day started off with an innocent question, from an innocent soul.

“Hey Charity, is profiling a pillar?”

I hadn’t even had my coffee yet.

“Someone was just telling me that profiling is the fourth pillar of observability now. I said I think profiling is a great tool, but I don’t know if it quite rises to the level of _pillar_. What do you think?”

_What….do.. I think._

What I think is, **there are no pillars**. I think the pillars are a fucking lie, dude. I think the language of pillars does a lot of work to keep good engineers trapped inside a mental model from the 1980s, paying outrageous sums of money for tooling that can’t keep up with the chaos and complexity of modern systems.

Here is a list of things I have recently heard people refer to as the “fourth pillar of observability”:

*   Profiling
*   Tokens (as in LLMs)
*   Errors, exceptions
*   Analytics
*   Cost

Is it a pillar, is it not a pillar? Are they all pillars? How many pillars are there?? How many pillars CAN there be? Gaahhh!

This is not a new argument. Take this [ranty little tweet thread of mine from way back in 2018](https://x.com/mipsytipsy/status/1044666259898593282?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1044666259898593282%7Ctwgr%5E9396190927fee8616723684a3fef9c05a8a1edb6%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext2Fhtmlkey%3Da19fcc184b9711e1b4764040d3dc5c07schema%3Dtwitterurl%3Dhttps3A%2F%2Ftwitter.com%2Fmipsytipsy%2Fstatus%2F1044666259898593282image%3Dhttps3A%2F%2Fi.embed.ly%2F1%2Fimage3Furl3Dhttps253A252F252Fabs.twimg.com252Ferrors252Flogo46x38.png26key3Da19fcc184b9711e1b4764040d3dc5c07), for starters.

> ✨THERE ARE NO✨
> 
> ✨THREE PILLARS OF✨
> 
>  ✨OBSERVABILITY.✨
> 
> 
> and the fact that everybody keeps blindly repeating this mantra (and cargo culting these primitives) is probably why our observability tooling is 10 years behind the rest of our software tool chain. [https://t.co/94yDBPuDRv](https://t.co/94yDBPuDRv)
> 
> — Charity Majors (@mipsytipsy) [September 25, 2018](https://twitter.com/mipsytipsy/status/1044666259898593282?ref_src=twsrc%5Etfw)

Or perhaps you have heard of TEMPLE: Traces, Events, Metrics, Profiles, Logs, and Exceptions?

Or the [“braid” of observability data](https://thenewstack.io/modern-observability-is-a-single-braid-of-data/), or “[They Aren’t Pillars, They’re Lenses](https://www.honeycomb.io/blog/they-arent-pillars-theyre-lenses)”, or the Lightstep version: “[Three Pillars, Zero Answers](https://medium.com/lightstephq/three-pillars-with-zero-answers-2a98b36358b8)” (that title is a personal favorite).

Alright, alright. Yes, this has been going on for a long time. I’m older now and I’m tireder now, so here’s how I’ll sum it up.

**Pillar** is a marketing term.

**Signal** is a technical term.

So “is profiling a pillar?” is a valid question, but it’s not a _technical_ question. It’s a question about the marketing claims being made by a given company. Some companies are building a profiling product right now, so yes, to them, it is vitally important to establish profiling as a “pillar” of observability, because you can charge a _hell_ of a lot more for a “pillar” than you can charge for a mere “feature”. And more power to them. But it doesn’t mean anything from a technical point of view.

On the other hand, “signal” is absolutely a technical term. [The OpenTelemetry Signals documentation](https://opentelemetry.io/docs/concepts/signals/), which I consider canon, says that OTel currently supports Traces, Metrics, Logs, and Baggage as signal types, with Events and Profiles at the proposal/development stage. So yes, profiling is a type of signal.

The OTel docs define a telemetry signal as “a type of data transmitted remotely for monitoring and analysis”, and they define a pillar as … oh, they don’t even mention pillars? like at all??

I guess there’s your answer.

And this is probably where I should end my piece. (Why am I still typing…. 🤔)

Pillars vs signals
------------------

First of all, I want to stress that _it does not bother me_ when engineers go around talking about pillars. Nobody needs to look at me guiltily and apologize for using the term ‘pillar’ at![Image 1: Bunnies Addendum (For the Buffy Fans) - En Tequila Es Verdad](https://i0.wp.com/i.pinimg.com/564x/74/e3/91/74e3912b5482dedb363516d9944c6dad.jpg?resize=172%2C224&ssl=1)the bar after a conference because they think I’m mad at them. I am not the language police, it is not my job to go around enforcing correct use of technical terms. (I used to, I know, and I’m sorry! 😆)

When engineers talk about pillars of observability, they’re just talking about signals and signal types, and “pillar” is a perfectly acceptable colloquialism for “signal”.

When a _vendor_ starts talking about pillars, though — as in the example above! — it means they are gearing up to sell you something: another type of signal, siloed off from all the other signals you send them. Your [cost multiplier](https://www.honeycomb.io/blog/cost-crisis-observability-tooling) is about to [increment again](https://www.honeycomb.io/blog/how-much-should-i-spend-on-observability-pt1), and then they’re going to start talking about how Important it is that you buy a product for each and every one of the Pillars they happen to have.

As a refresher: there are [two basic architecture models](https://charity.wtf/2024/08/07/is-it-time-to-version-observability-signs-point-to-yes/) used by observability companies, the multiple pillars model and the unified storage model (aka o11y 2.0). The [multiple pillars model](https://www.honeycomb.io/blog/one-key-difference-observability1dot0-2dot0) is to store every type of signal in a different siloed storage location — metrics, logs, traces, profiling, exceptions, etc, _everybody_ gets a database! The [unified storage model](https://charity.wtf/2024/12/20/on-versioning-observabilities-1-0-2-0-3-0-10-0/) is to store all signals together in ONE database, preserving context and relationships, so you can treat data like data: slice and dice, zoom in, zoom out, etc.

Most of the industry giants were built using the pillars model, but Honeycomb (and every other observability company founded post-2019) has built using the unified storage model, building [wide, structured log events on a columnar storage engine](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool) with high cardinality support, and so on.

Bunny-hopping from pillar to pillar
-----------------------------------

When you use each signal type as a standalone pillar, this leads to an experience I think of as “bunny products” 🐇 where the user is always hopping from pillar to pillar. You see something on your metrics dashboard that looks scary? hop-hop to your logs and try to find it there, using grep and search and matching by timestamps. If you can find the right logs, then you need to trace it, so you hop-hop-hop to your traces and repeat your search there. With profiling as a pillar, maybe you can hop over to that dataset too.🐇🐰

The amount of data duplication involved in this model is _mind boggling_. You are literally storing the same information in your metrics TSDB as you are in your logs and your traces, just formatted![Image 2: The 30 Best Bunny Rabbit Memes - Hop to Pop](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ07ZmfJNJ8rDyWebCj3utRbXWxeJKT7brJVw&s)differently. (I never miss an opportunity to link to [Jeremy Morrell’s masterful doc on instrumenting your code for wide events](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/), which also happens to illustrate this nicely.) This is insanely expensive. Every request that enters your system gets stored _how many times,_ in _how many signals_? Count it up; that’s your cost multiplier.

Worse, much of the data that connects each “pillar” exists only in the heads of the most senior engineers, so they can guess or intuit their way around the system, but anyone who relies on actual data is screwed. Some vendors have added an ability to construct little rickety bridges post hoc between pillars, e.g. “this metric is derived from this value in this log line or trace”, but now you’re paying for each of those little bridges in addition to each place you store the data (and it goes without saying, you can only do this for things you can predict or hook up in the first place).

The multiple pillars model (formerly known as observability 1.0) relies on you believing that each signal type must be stored separately and treated differently. That’s what the pillars language is there to reinforce. Is it a Pillar or not?? It doesn’t matter because pillars don’t exist. Just know that if your vendor is calling it a P illar, you are definitely going to have to P ay for it. 😉

Zooming in and out
------------------

But all this data is just.. data. There is no good reason to silo signals off from each other, and lots of good reasons not to. You can derive metrics from rich, structured data blobs, or append your metrics to wide, structured log events. You can add span IDs and visualize them as a trace. The unified storage model (“o11y 2.0”) says you should store your data once, and do all the signal processing in the collection or analysis stages. Like civilized folks.

![Image 3: Anya Bunny Quote - Etsy](https://i0.wp.com/i.etsystatic.com/10147996/r/il/da4dfe/708169568/il_300x300.708169568_rykv.jpg?resize=232%2C232&ssl=1)

All along, Anya was right

From the perspective of the developer, not much changes. It just gets easier (a LOT easier), because nobody is harping on you about whether this nit of data should be a metric, a log, a trace, or all of the above, or if it’s low cardinality or high cardinality, or whether the cardinality of the data COULD someday blow up, or whether it’s a counter, a gauge, a heatmap, or some other type of metric, or when the counter is going to get reset, or whether your heatmap buckets are defined at useful intervals, or…or…

Instead, it’s just a blob of json. Structured data.. If you think it might be interesting to you someday, you dump it in, and if not, you don’t. That’s all. Cognitive load drops way down..

On the backend side, we store it once, retaining all the signal type information and connective tissue.

It’s the user interface where things change most dramatically. No more bunny hopping around from pillar to pillar, guessing and copy-pasting IDs and crossing your fingers. Instead, it works more like the zoom function on PDFs or Google maps.

You start with SLOs, maybe, or a familiar-looking metrics dashboard. But instead of hopping, you just.. zoom in. The SLOs and metrics are derived from the data you need to debug with, so you’re just like.. “Ah what’s my SLO violation about? Oh, it’s because of these events.” Want to trace one of them? Just click on it. No hopping, no guessing, no pasting IDs around, no lining up time stamps.

Zoom in, zoom out, it’s all connected. Same fucking data.

“But OpenTelemetry FORCES you to use three pillars”
---------------------------------------------------

There’s a misconception out there that OpenTelemetry is very pro-three pillars, and very anti o11y 2.0. This is a) not true and b) actually the opposite. Austin Parker has written a [voluminous amount of material](https://www.honeycomb.io/resources/whitepapers/opentelemetry-semantic-telemetry-reshape-observability) explaining that actually, under the hood, OTel treats everything like one big wide structured event log.![Image 4](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/10/srebunny.png?resize=200%2C300&ssl=1)

[As Austin puts it](https://www.honeycomb.io/blog/opentelemetry-is-not-three-pillars), “OpenTelemetry, fundamentally, unifies telemetry signals through shared, distributed context.” However:

“The project doesn’t _require_ you to do this. Each signal is usable more or less independently of the other. If you want to use OpenTelemetry data to feed a traditional ‘three pillars’ system where your data is stored in different places, with different query semantics, you can. Heck, quite a few very successful observability tools let you do that today!”

“This isn’t just ‘three pillars but with some standards on top,’ it’s a radical departure from the traditional ‘log everything and let god sort it out’ approach that’s driven observability practices over the past couple of decades.”

You _can_ use OTel to reinforce a three pillars mindset, but you don’t _have_ to. Most vendors have _chosen_ to implement three pillarsy crap on top of it, which you can’t really hold OTel responsible for. One[1] might even argue that OTel is doing as much as it can to influence you in the opposite direction, while still meeting Pillaristas where they’re at.

A postscript on profiling
-------------------------

What will profiling mean in a unified storage world? It just means you’ll be able to zoom in to even finer and lower-level resolution, down to syscalls and kernel operations instead of function calls. Like when Google Maps got good enough that you could read license plates instead of just rooftops.

Admittedly, we don’t have profiling yet at [Honeycomb](http://honeycomb.io/). When we did some research into the profiling space, what we learned was that most of the people who think they’re in desperate need of a profiling tool are actually in need of a good **tracing tool**. Either they didn’t have distributed tracing or their tracing tools just weren’t cutting it, for reasons that are not germane in a Honeycomb tracing world.

We’ll get to profiling, hopefully in the near-ish future, but for the most part, if you don’t need syscall level data, you probably don’t need profiling data either. Just good traces.

Also… I did not make this site or have any say whatsoever in the building of it, but I did sign the manifesto[2] and every day that I remember it exists is a day I delight in the joy and fullness of being alive:[kill3pill.com](http://kill3pill.com/) 📈

[![Image 5: Kill Three Pillars](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/10/Screenshot-2025-10-29-at-22.02.55.png?resize=493%2C115&ssl=1)](https://charity.wtf/2025/10/30/the-pillar-is-a-lie/kill3pill.com)

Hop hop, little friends,

 ~charity

[1] _Austin_ argues this. I’m talking about Austin, if not clear enough.

 [2] Thank you, [John Gallagher](https://www.linkedin.com/in/synapticmishap/)!!