Title: To get better at technical writing, lower your expectations

URL Source: https://www.seangoedecke.com/technical-communication/

Markdown Content:
Technical writing is a big part of a software engineer’s job. This is more true the more senior you get. In the limit case, a principal or distinguished engineer might only write technical documents, but even brand-new junior engineers need to write: commit messages, code comments, PR descriptions and comments, Slack threads, internal announcements, documentation, runbooks, and so on. **Whether you write well or badly matters a lot.**

### Keep it as short as possible

The primary rule about technical writing is that **almost none of your readers will pay much attention**. Your readers will typically read the first sentence, skim the next one, and then either skim the rest or stop reading entirely. You should thus write as little as possible. If you can communicate your idea in a single sentence, do that - there’s a high chance that people will actually read it.

What if you can’t communicate all the details in so few words? In fact, this is a feature not a bug. **You should deliberately omit many subtle details**.

This is the biggest difference between technical writing and code. Each line of code you write is as important to the computer as any other. The compiler or interpreter will methodically go through every single detail you put into your codebase and incorporate it into the final product. If there’s a subtle point you want to make - say, that prorated monthly billing should account for the fact that some months are longer than others - you can and should spend a paragraph of code articulating it. But each point you make when talking to humans consumes a limited attention budget[1](https://www.seangoedecke.com/technical-communication/#fn-1). Because of that, it’s usually wise to leave out subtle points entirely.

One consequence of this is that **you should frontload all important information**. If you spend a paragraph providing context and throat-clearing, many of your readers will have stopped reading (or started skimming) by the time you make your actual point. Try to get to your point in the very first sentence. It’s even better to get your point into the _title_, like an academic paper does.

### Lower your expectations

Many engineers refuse to deliberately leave out information, because they think they shouldn’t need to. They believe their technical colleagues are thoughtful, conscientious people who will pay careful attention to everything they read and attempt to come to a full understanding of it. In other words, **many engineers have far too high expectations of what their technical writing can accomplish.**

For instance, your technical writing is not going to transplant your understanding of a system into somebody else’s head. It simply does not work like that. **Understanding of technical systems is won only through painstaking concrete effort**: you have to interact with the system, read the code, make changes to it, and so on. At best, good technical writing will give someone enough rough context to get a fuzzy understanding of what you’re suggesting. At worst, good technical writing will convey to the reader that at least _you_ know what you’re talking about, so they may as well trust you even if they’re still confused.

Your technical writing is also not going to get everybody on the same page. Disagreement and confusion in large organizations is not dysfunction but function: it is the normal baseline of operation, just like some constant degree of failure is part of the normal baseline of a complex distributed system. **You should not expect your technical writing to fix this problem.**

### What can good technical writing do?

So what can good technical writing do? It can communicate a _very_ simple technical point to a broad audience. For instance, you can explain “adding new settings requires a database migration, so it cannot be done dynamically” to your Product org, and thus prevent them from suggesting impossible things[2](https://www.seangoedecke.com/technical-communication/#fn-2). However, be aware that the actual point being communicated is probably even simpler than that: something like “adding new settings is hard”, or even “settings are complicated”.

This is a fairly pessimistic view about the usefulness of technical writing. But I do think that even this limited goal is surprisingly important in a large organization. **The baseline level of technical confusion is so high that communicating even obvious things is high-leverage.** I wrote about this in [_Providing technical clarity to non-technical leaders_](https://www.seangoedecke.com/clarity): even the people _leading_ engineering organizations are often operating on a really low level of technical context, because they simply have so many other things to worry about.

Good technical writing can also communicate a reasonably complex technical point to a _tiny_ audience. For instance, you can write [an ADR](https://adr.github.io/) that goes into many subtle details about a planned piece of work. This is a great way to get excellent feedback on a plan, but **the effective audience for writing like this can be in the single digits**. Sometimes the effective audience for an ADR is _two_: you, the writer, and one other engineer who has the requisite context to understand it.

### Thinking clearly

Of course, to write clearly you first must think clearly. I haven’t written about this here because it’s an entirely separate topic (and one I have less concrete advice for). For some engineers, this is the main obstacle to condensing their point into a key sentence or two: they simply do not have a clear enough understanding to do that, and must instead express a series of related ideas and hope the reader gets the overall message.

I did write about this almost a year ago in [_Thinking clearly about software_](https://www.seangoedecke.com/thinking-clearly). I stand by most of that, particularly the parts about sitting with your uncertainty and focusing on what you can say for sure, but I think there’s probably much more to be said on this topic.

### Summary

The biggest mistake engineers make in their technical writing is **setting their expectations too high**. They try to communicate in too much detail and end up failing to communicate anything at all: either because readers are checked out by the time they arrive at the key point, or because they’ve simply assumed too much background technical knowledge and the reader is hopelessly confused.

When you are doing technical writing, **you are almost always communicating to people with less technical context than you**. You may have a crystal-clear understanding of what you’re talking about, but your reader will not. They likely won’t even be as interested as you in the topic: if you’re writing a paragraph to try and ask some other team to do something, that something is your project that you (presumably) care about, but the other team has their own projects and will probably only skim what you wrote.

If you can say what you want to say in one sentence - even if it means leaving out some nuance - you should almost always do that. If you have to write a paragraph, make it as short a paragraph as you can. If you have to write a page, make sure the first paragraph contains as much key information as possible, because many readers won’t make it any further than that.

The good news is that even if you’re overestimating how much you can successfully convey, you’re likely underestimating how useful it is to convey even a tiny amount of technical content. In large organizations, many technical decisions are made by people with effectively zero technical context[3](https://www.seangoedecke.com/technical-communication/#fn-3). Going from that to even a very rough “lay of the land” is a massive improvement.

* * *

1.   In this sense, it’s similar to talking with LLMs.

[↩](https://www.seangoedecke.com/technical-communication/#fnref-1)
2.   Of course settings (however implemented) don’t _need_ to require a database migration. You can rearchitect the system to make almost any architectural impossibility possible. But “we’d need to redesign settings to do this” is pretty similar to “this is impossible” for many one-off low-priority asks.

[↩](https://www.seangoedecke.com/technical-communication/#fnref-2)
3.   Even if the decision-makers have technical context on some of the system, they’ll likely still be often making decisions about other parts of the system that are black boxes to them.

[↩](https://www.seangoedecke.com/technical-communication/#fnref-3)

If you liked this post, consider[subscribing](https://buttondown.com/seangoedecke)to email updates about my new posts, or[sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/technical-communication/&t=To%20get%20better%20at%20technical%20writing,%20lower%20your%20expectations). Here's a preview of a related post that shares tags with this one.