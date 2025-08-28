Title: Do the simplest thing that could possibly work

URL Source: https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/

Markdown Content:
When designing software systems, do the simplest thing that could possibly work.

It’s surprising how far you can take this piece of advice. I genuinely think you can do this _all the time_. You can follow this approach for fixing bugs, for maintaining existing systems, and for architecting new ones.

A lot of engineers design by trying to think of the “ideal” system: something well-factored, near-infinitely scalable, elegantly distributed, and so on. I think this is entirely the wrong way to go about software design. Instead, spend that time understanding the current system deeply, then do the simplest thing that could possibly work.

### Simple can be underwhelming

[System design](https://www.seangoedecke.com/good-system-design) requires competence with a lot of different tools: app servers, proxies, databases, caches, queues, and so on. As they gain familiarity with these tools, junior engineers naturally want to use them. It’s fun to construct systems out of many different components! And it feels very satisfying to draw boxes and arrows on a whiteboard - like you’re doing real engineering.

However, as with many skills, real mastery often involves learning when to do less, not more. The fight between an ambitious novice and an old master is a well-worn cliche in martial arts movies: the novice is a blur of motion, flipping and spinning. The master is mostly still. But somehow the novice’s attacks never seem to quite connect, and the master’s eventual attack is decisive.

In software, this means that [great software design looks underwhelming](https://www.seangoedecke.com/great-software-design). It doesn’t look like anything much is happening at all. You can tell you’re in the presence of great software design because you start having thoughts like “oh, I didn’t realise the problem was that easy” or “oh nice, you don’t actually have to do anything difficult”.

[Unicorn](https://github.com/defunkt/unicorn) is great software design, because it delivers all the most important guarantees in a web server (request isolation, horizontal scaling, crash recovery) by leaning on Unix primitives[1](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fn-1). The industry-standard Rails REST API is great software design, because it gives you exactly what you need for a CRUD app in the most boring way possible. I don’t think any of these are impressive _software_. But they’re impressive feats of _design_, because **they do the simplest thing that could possibly work**.

You should do that too! Suppose you’ve got a Golang application that you want to add some kind of rate limiting to. What’s the simplest thing that could possibly work? Your first idea might be to add some kind of persistent storage (say, Redis) to track per-user request counts with a leaky-bucket algorithm. That would work! But do you need a whole new piece of infrastructure? What if instead you kept those per-user request counts in-memory? Sure, you’d lose some rate limiting data when the application is restarted, but does that matter? Actually, are you sure your edge proxy[2](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fn-2) doesn’t support rate limiting already? Could you just write a couple of lines in a config file instead of implementing the feature at all?

Maybe your edge proxy doesn’t support rate limiting. Maybe you can’t track it in-memory because you have too many server instances running in parallel, so the tightest rate limit you could enforce that way is too wide. Maybe it’s a dealbreaker if you ever lose rate limiting data, because people are hammering your service _that_ hard. In that case, the simplest thing that could possibly work is adding persistent storage, so you should go and do that. But if you could do one of the easier approaches, wouldn’t you want to?

You really can build a whole application from scratch this way: start with the absolute simplest thing, and then only extend it when you have new requirements that force you to. It sounds silly, but it works. Think of it as taking [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) as the ultimate design principle: above single-responsibility, above choosing the best tool for the job, and above “good design”.

### What’s wrong with doing the simplest thing?

Of course, there are three big problems with always doing the simplest thing that could possibly work. The first is that, by not anticipating future requirements, you end up with an inflexible system or a [big ball of mud](http://laputan.org/mud/). The second is that it’s not clear what “simplest” means, so at worst I’m saying “to design well, always do good design”. The third is that you ought to be building systems that can _scale_, not systems that just work right now. Let’s take those objections in order.

#### Big balls of mud

To some engineers, “do the simplest thing that could possibly work” sounds like I’m telling them to stop doing engineering. If the simplest thing is usually a quick kludge, does that mean this advice will inevitably lead to a complete mess? We’ve all seen codebases with hacks stacked on top of hacks, and they definitely don’t look like good design.

But are hacks simple? I actually don’t think so. The problem with a hack or a kludge is precisely that it _isn’t_ simple: that it adds complexity to the codebase by introducing another thing you have to always remember. Hacks are just _easier to think of_. Figuring out the proper fix is hard because it requires having to understand the entire codebase (or large sections of it). In fact, the proper fix is almost always much simpler than the hack.

It is not easy to do the simplest thing that could possibly work. When you’re looking at a problem, the first few solutions that come to mind are unlikely to be the simplest ones. Figuring out the simplest solution requires considering many different approaches. In other words, it requires doing engineering.

#### What is simplicity?

Engineers disagree a lot about what constitutes simple code. If “simplest” already means “with good design”, is it just a tautology to say “you should do the simplest thing that could possibly work?” In other words, is Unicorn really simpler than [Puma](https://github.com/puma/puma)[3](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fn-3)? Is adding in-memory rate limiting really simpler than using Redis? Here’s a rough, intuitive definition of simplicity[4](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fn-4):

1.   Simple systems have fewer “moving pieces”: fewer things you have to think about when you’re working with them
2.   Simple systems are less _internally-connected_. They are composed from components with clear, straightforward interfaces

Unix processes are simpler than threads (and thus Unicorn is simpler than Puma) because processes are less connected: they do not share memory. This makes a lot of sense to me! But I don’t think it gives you the tools to figure out what’s simpler in every case.

What about in-memory rate limiting vs Redis? On the one hand, in-memory is simpler because you don’t have to think about all the things involved in standing up a separate service with persistent memory. On the other hand, Redis is simpler because the rate limiting guarantees it offers are more straightforward - you don’t have to worry about the case where one server instance thinks a user is rate limited and another one doesn’t.

When I’m not sure what “seems” simpler to me, I like to use this tiebreaker: **simple systems are stable**. If you’re comparing two states of a software system, and one will require more ongoing work _if no requirements change_, the other one is simpler. Redis must be deployed and maintained, it can have its own incidents, it requires its own monitoring, it requires a separate deployment in any new environments the service finds itself in, and so on. Thus in-memory rate limiting is simpler than Redis[5](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fn-5).

#### Why wouldn’t you want to be scalable?

A certain type of engineer is now screaming to themselves “but in-memory rate limiting won’t scale!” Doing the simplest thing that could possibly work will emphatically not deliver the most web-scale system. It will deliver a system that works well at the current scale. Is this irresponsible engineering?

No. In my view, the cardinal sin of big tech SaaS engineering is an obsession with scale. I’ve seen so much unavoidable pain caused by over-engineering systems to prepare for several orders of magnitude more than the current scale.

The main reason to not try this is that **it doesn’t work**. In my experience, for any non-trivial codebase, you can’t anticipate how it will behave at several orders of magnitude more traffic, because you don’t know ahead of time where all the bottlenecks are going to be. At most you can try to make sure you’re ready for 2x or 5x the current traffic, and then stand by to deal with problems as they come in.

The other reason not to try this is that **it makes your codebase inflexible**. It’s fun to decouple your service into two pieces so they can be scaled independently (I have seen this happen maybe ten times, and I have seen them _actually be usefully scaled independently_ maybe once). But that makes certain features very hard to implement, because they now require coordination over the wire. In the worst case, they require _transactions_ over the wire, which is a genuinely hard engineering problem. Most of the time you just don’t have to do any of this!

### Final thoughts

The longer I spend working in tech, the less optimistic I become about our collective ability to predict where a system is going. It’s hard enough to get your head around where a system currently is. And in fact, that’s the main practical difficulty in doing good design: getting an accurate big-picture understanding of the system. Most design is done without that understanding, and most design is thus pretty bad.

There are, broadly speaking, two ways to develop software. The first is to predict what your requirements might look like six months or a year from now, and then design the best system for that purpose. The second is to design the best system for what your requirements actually look like right now: in other words, to do the simplest thing that could possibly work.

* * *

1.   It’s just Unix sockets and forked processes! I _love_ Unicorn.

[↩](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fnref-1)
2.   Every tech company has some kind of edge proxy.

[↩](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fnref-2)
3.   I do like Puma and think it’s a good web server. There are definitely use cases where you’d pick it over Unicorn (though in those cases I would personally think hard about using a different language than Ruby).

[↩](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fnref-3)
4.   I’m influenced here by Rich Hickey’s great talk [Simple Made Easy](https://www.infoq.com/presentations/Simple-Made-Easy/). I don’t agree with all of it (I think familiarity does in fact contribute to simplicity in practice) but it’s definitely worth watching.

[↩](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fnref-4)
5.   Of course, if the system has to scale horizontally more than a little bit, in-memory rate limiting won’t work and must be replaced with something like Redis. But in my experience a Golang service can scale _a lot_ without having to scale horizontally to more than a handful of replicas.

[↩](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/#fnref-5)