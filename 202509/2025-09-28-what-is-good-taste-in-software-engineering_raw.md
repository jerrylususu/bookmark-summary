Title: What is "good taste" in software engineering?

URL Source: https://www.seangoedecke.com/taste/

Markdown Content:
Technical taste is different from technical skill. You can be technically strong but have bad taste, or technically weak with good taste. Like taste in general, technical taste sometimes runs ahead of your ability: just like you can tell good food from bad without being able to cook, you can know what kind of software you like before you’ve got the ability to build it. You can develop technical ability by study and repetition, but good taste is developed in a more mysterious way.

Here are some indicators of software taste:

*   What kind of code “looks good” to you? What kind of code “looks ugly”?
*   Which design decisions you feel really good about, and which ones are just fine?
*   Which software problems really bother you, to the point where you’re worrying about them outside of work? Which problems can you just brush off?

I think taste is **the ability to adopt the set of engineering values that fit your current project**.

### Why taste is different from skill

Aren’t the indicators above just a part of skill? For instance, doesn’t code look good _if it’s good code_? I don’t think so.

Let’s take an example. Personally, I feel like code that uses map and filter looks nicer than using a for loop. It’s tempting to think that this is a case of me being straightforwardly correct about a point of engineering. For instance, map and filter typically involve pure functions, which are easier to reason about, and they avoid an entire class of off-by-one iterator bugs. It feels to me like this isn’t a matter of taste, but a case where I’m right and other engineers are wrong.

But of course it’s more complicated than that. Languages like Golang don’t contain map and filter at all, for principled reasons. Iterating with a for loop is easier to reason about from a performance perspective, and is more straightforward to extend to other iteration strategies (like taking two items at a time). I don’t care about these reasons as much as I care about the reasons in favour of map and filter - that’s why I don’t write a lot of for loops - but it would be far too arrogant for me to say that engineers who prefer for loops are simply less skilled. In many cases, they have technical capabilites that I don’t have. They just care about different things.

In other words, our disagreement comes down to a difference in _values_. I wrote about this point in [_I don’t know how to build software and you don’t either_](https://www.seangoedecke.com/confidence). Even if the big technical debates do have definite answers, no working software engineer is ever in a position to know what those answers are, because you can only fit so much experience into one career. We are all at least partly relying on our own personal experience: on our particular set of engineering values.

### What engineering taste actually is

Almost every decision in software engineering is a tradeoff. You’re rarely picking between two options where one is strictly better. Instead, each option has its own benefits and downsides. Often you have to make hard tradeoffs between engineering _values_: past a certain point, you cannot easily increase performance without harming readability, for instance[1](https://www.seangoedecke.com/taste/#fn-1).

Really understanding this point is (in my view) the biggest indicator of maturity in software engineering. Immature engineers are rigid about their decisions. They think it’s always better to do X or Y. Mature engineers are usually willing to consider both sides of a decision, because they know that both sides come with different benefits. The trick is not deciding if technology X is better than Y, but whether the benefits of X outweigh Y _in this particular case_.

In other words, **immature engineers are too inflexible about their taste**. They know what they like, but they mistake that liking for a principled engineering position. What defines a particular engineer’s taste?

In my view, **your engineering taste is composed of the set of engineering values you find most important**. For instance:

**Resiliency**. If an infrastructure component fails (a service dies, a network connection becomes unavailable), does the system remain functional? Can it recover without human intervention?

**Speed**. How fast is the software, compared to the theoretical limit? Is work being done in the hot path that isn’t strictly necessary?

**Readability**. Is the software easy to take in at a glance and to onboard new engineers to? Are functions relatively short and named well? Is the system well-documented?

**Correctness**. Is it possible to represent an invalid state in the system? How locked-down is the system with tests, types, and asserts? Do the tests use techniques like fuzzing? In the extreme case, has the program been proven correct by formal methods like [Alloy](https://en.wikipedia.org/wiki/Alloy_(specification_language))?

**Flexibility**. Can the system be trivially extended? How easy is it to make a change? If I need to change something, how many different parts of the program do I need to touch in order to do so?

**Portability**. Is the system tied down to a particular operational environment (say, Microsoft Windows, or AWS)? If the system needs to be redeployed elsewhere, can that happen without a lot of engineering work?

**Scalability**. If traffic goes up 10x, will the system fall over? What about 100x? Does the system have to be over-provisioned or can it scale automatically? What bottlenecks will require engineering intervention?

**Development speed**. If I need to extend the system, how fast can it be done? Can most engineers work on it, or does it require a domain expert?

There are many other engineering values: elegance, modern-ness, use of open source, monetary cost of keeping the system running, and so on. All of these are important, but **no engineer cares equally about all of these things.** Your taste is determined by which of these values you rank highest. For instance, if you value speed and correctness more than development speed, you are likely to prefer Rust over Python. If you value scalability over portability, you are likely to argue for a heavy investment in your host’s (e.g. AWS) particular quirks and tooling. If you value resiliency over speed, you are likely to want to split your traffic between different regions. And so on[2](https://www.seangoedecke.com/taste/#fn-2).

It’s possible to break these values down in a more fine-grained way. Two engineers who both deeply care about readability could disagree because one values short functions and the other values short call-stacks. Two engineers who both care about correctness could disagree because one values exhaustive test suites and the other values formal methods. But the principle is the same - there are lots of possible engineering values to care about, and because they are often in tension, each engineer is forced to take some more seriously than others.

### How to identify bad taste

I’ve said that all of these values are important. Despite that, it’s possible to have _bad_ taste. In the context of software engineering, bad taste means that **your preferred values are not a good fit for the project you’re working on**.

Most of us have worked with engineers like this. They come onto your project evangelizing about something - formal methods, rewriting in Golang, Ruby meta-programming, cross-region deployment, or whatever - because it’s worked well for them in the past. Whether it’s a good fit for your project or not, they’re going to argue for it, because it’s what they like. Before you know it, you’re making sure your internal metrics dashboard has five nines of reliability, at the cost of making it impossible for any junior engineer to understand.

In other words, most bad taste comes from **inflexibility**. I will always distrust engineers who justify decisions by saying “it’s best practice”. No engineering decision is “best practice” in all contexts! You have to make the right decision for the specific problem you’re facing.

One interesting consequence of this is that engineers with bad taste are like broken compasses. If you’re in the right spot, a broken compass will still point north. It’s only when you start moving around that the broken compass will steer you wrong. Likewise, many engineers with bad taste can be quite effective in the particular niche where their preferences line up with what the project needs. But when they’re moved between projects or jobs, or when the nature of the project changes, the wheels immediately come off. No job stays the same for long, particularly [in these troubled post-2021 times](https://www.seangoedecke.com/good-times-are-over).

### How to identify good taste

Good taste is a lot more elusive than technical ability. That’s because, unlike technical ability, good taste is the ability to select the right set of engineering values **for the particular technical problem you’re facing**. It’s thus much harder to identify if someone has good taste: you can’t test it with toy problems, or by asking about technical facts. You need there to be a real problem, with all of its messy real-world context.

You can tell you have good taste if the projects you’re working on succeed. If you’re not meaningfully contributing to the design of a project (maybe you’re just doing ticket-work), you can tell you have good taste if the projects where you agree with the design decisions succeed, and the projects where you disagree are rocky. Importantly, you need a set of different kinds of projects. If it’s just the one project, or the same kind of project over again, you might just be a good fit for that. Even if you go through many different kinds of projects, that’s no guarantee that you have good taste in domains you’re less familiar with[3](https://www.seangoedecke.com/taste/#fn-3).

How do you develop good taste? It’s hard to say, but I’d recommend working on a variety of things, paying close attention to which projects (or which parts of the project) are easy and which parts are hard. You should focus on **flexibility**: try not to acquire strong universal opinions about the right way to write software. What good taste I have I acquired pretty slowly. Still, I don’t see why you couldn’t acquire it fast. I’m sure there are prodigies with taste beyond their experience in programming, just as there are prodigies in other domains.

* * *

1.   Of course this isn’t always true. There are win-win changes where you can improve several usually-opposing values at the same time. But mostly we’re not in that position.

[↩](https://www.seangoedecke.com/taste/#fnref-1)
2.   Like I said above, different projects will obviously demand a different set of values. But the engineers working on those projects will still have to draw the line somewhere, and they’ll rely on their own taste to do that.

[↩](https://www.seangoedecke.com/taste/#fnref-2)
3.   That said, I do think good taste is somewhat transferable. I don’t have much personal experience with this so I’m leaving it in a footnote, but if you’re flexible and attentive to the details in domain A, you’ll probably be flexible and attentive to the details in domain B.

[↩](https://www.seangoedecke.com/taste/#fnref-3)