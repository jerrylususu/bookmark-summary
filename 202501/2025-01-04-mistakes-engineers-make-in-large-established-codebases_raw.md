Title: Mistakes engineers make in large established codebases

URL Source: https://www.seangoedecke.com/large-established-codebases/

Markdown Content:
Working in large established codebases is one of the hardest things to learn as a software engineer. You can’t practice it beforehand (no, open source does not give you the same experience). Personal projects can never teach you how to do it, because they’re necessarily small and from-scratch. For the record, when I say “large established codebases”, I mean:

*   Single-digit million lines of code (~5M, let’s say)
*   Somewhere between 100 and 1000 engineers working on the same codebase
*   The first working version of the codebase is at least ten years old

I’ve now spent a decade working in these codebases. Here’s what I wish I’d known at the start.

### The cardinal mistake is inconsistency

There’s one mistake I see more often than anything else, and it’s absolutely deadly: ignoring the rest of the codebase and just implementing your feature in the most sensible way. In other words, limiting your touch points with the existing codebase in order to keep your nice clean code uncontaminated by legacy junk. For engineers that have mainly worked on small codebases, this is very hard to resist. But you must resist it! In fact, you must sink as deeply into the legacy codebase as possible, **in order to maintain consistency.**

Why is consistency so important in large codebases? Because it protects you from nasty surprises, it slows down the codebase’s progression into a mess, and it allows you to take advantage of future improvements.

Suppose you’re building an API endpoint for a particular type of user. You could put some “return 403 if current user isn’t of that type” logic in your endpoint. But you should first go and look to see what other API endpoints in the codebase do for auth. If they use some specific set of helpers, you should also use that helper (even if it’s ugly, hard to integrate with, or seems like overkill for your use case). **You must resist the urge to make your little corner of the codebase nicer than the rest of it.**

The main reason to do this is because large codebases have a lot of landmines in them. For instance, you might not know that the codebase has a concept of “bots”, which are like users but not quite, and require special treatment for auth. You might not know that the internal support tooling in the codebase allows an engineer to sometimes authenticate on behalf of a user, which requires special treatment for auth. There’s definitely another hundred things you might not know. Existing functionality represents a safe path through the minefield. If you do your auth like other API endpoints that have stuck around for a long time, you can follow that path without having to know all the surprising things that the codebase does.

On top of that, lack of consistency is the primary long-term killer of large codebases, because it makes it impossible to make any general improvements. Sticking with our auth example, if you want to ever introduce a new type of user, a consistent codebase lets you update the existing set of auth helpers to accommodate that. In an inconsistent codebase, where some API endpoints are doing things differently, you’ll have to go and update and test every one of those implementations. In practice, that means that the general change does not happen, or that the hardest 5% of endpoints to update are just left out of scope - which in turn decreases consistency further, because now you have a user type that works for most-but-not-all API endpoints.

So when you sit down to implement anything in a large codebase, you should always first go and look around for prior art, and follow that if at all possible.

### Is anything else important?

Consistency is the most important thing. Let me quickly run through some other concerns as well, though:

You need to develop a good sense of how the service is used in practice (i.e. by users). Which endpoints are hit the most often? Which endpoints are the most crucial (i.e. are used by paying customers and cannot gracefully degrade)? What latency guarantees must the service obey, and what code gets run in the hot paths? One common large-codebase mistake is to make a “tiny tweak” that is unexpectedly in the hot path for a crucial flow, and thus causes a big problem.

You can’t rely on your ability to test the code in development like you can in a small project. Any large project accumulates state over time (for instance, how many kinds of user do you think GMail supports?) At a certain point, you can’t test every combination of states, even with automation. Instead, you have to test the crucial paths, code defensively, and rely on slow rollouts and monitoring to catch problems.

Be very, very reluctant to introduce new dependencies. In large codebases, code often lives forever. Dependencies introduce an ongoing cost in security vulnerabilities and package updates that will almost certainly outlive your tenure at the company. If you have to, make sure you pick dependencies that are widely-used and reliable, or that are easy to fork if needed.

For related reasons, if you ever get the chance to remove code, take it with both hands. This is some of the riskiest work in large codebases, so don’t half-ass it: first instrument the code to identify callers in production and drive them down to zero, so you can be absolutely certain it’s safe to remove. But it’s still worth doing. There are few things in a large codebase more worthwhile than safely removing code.

Work in small PRs and front-load the changes that affect other teams’ code. This one is important in small projects too, but it’s critical in large ones. That’s because you’ll often be relying on the domain experts in other teams to anticipate things you’ve missed (since large projects are just too complex to anticipate it all yourself). If you keep your changes to risky areas small and easy-to-read, those domain experts have a much better chance of noticing problems and saving you from an incident.

### Why bother?

Finally, I want to take a second to defend these codebases in general. One common take I’ve heard goes like this:

> Why would you ever decide to work in the legacy mess? Spending time knee-deep in spaghetti code might be hard, but it isn’t good engineering. When faced with a large established codebase, our job should be to shrink it by splitting out small elegant services instead of wading in and making the mess larger.

I think this is totally wrong-headed. The main reason is that, as a general rule, **large established codebases produce 90% of the value**. In any big tech company, the majority of the revenue-producing activity (i.e. the work that actually pays your engineering salary) comes from a large established codebase. If you work at a big tech company and don’t think this is true, maybe you’re right, but I’ll only take that opinion seriously if you’re deeply familiar with the large established codebase you think isn’t providing value. I’ve seen multiple cases where a small elegant service powers some core feature of a high-revenue product, but all the actual productizing code (settings, user management, billing, enterprise reporting, etc) still lives in the large established codebase.

So you should know how to work in the “legacy mess” because that’s what your company actually does. Good engineering or not, _it’s your job_.

The other reason is that **you cannot split up a large established codebase without first understanding it**. I have seen large codebases successfully split up, but I have never seen that done by a team that wasn’t already fluent at shipping features inside the large codebase. You simply cannot redesign any non-trivial project (i.e. a project that makes real money) from first-principles. There are too many accidental details that support tens of millions of dollars of revenue.

### Summary

*   Large codebases are worth working in because they usually pay your salary
*   By far the most important thing is consistency
*   Never start a feature without first researching prior art in the codebase
*   If you don’t follow existing patterns, you better have a very good reason for it
*   Understand the production footprint of the codebase
*   Don’t expect to be able to test every case - instead, rely on monitoring
*   Remove code any chance you get, but be very careful about it
*   Make it as easy as possible for domain experts to catch your mistakes
