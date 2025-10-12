Title: How I provide technical clarity to non-technical leaders

URL Source: https://www.seangoedecke.com/clarity/

Markdown Content:
My mission as a staff engineer is to provide technical clarity to the organization.

Of course, I do other stuff too. I run projects, I ship code, I review PRs, and so on. But the most important thing I do - what I’m _for_ - is to provide technical clarity.

### What is technical clarity?

**In an organization, technical clarity is when non-technical decision makers have a good-enough practical understanding of what changes they can make to their software systems.**

The people in charge of your software organization[1](https://www.seangoedecke.com/clarity/#fn-1) have to make a lot of decisions about software. Even if they’re not setting the overall strategy, they’re still probably deciding which kinds of users get which features, which updates are most important to roll out, whether projects should be delayed or rushed, and so on.

These people may have been technical once. They may even have fine technical minds now. But they’re still “non-technical” in the sense I mean, because they simply don’t have the time or the context to build an accurate mental model of the system. Instead, they rely on a vague mental model, supplemented by advice from engineers they trust.

To the extent that their vague mental model is accurate and the advice they get is good - in other words, to the extent that they have technical clarity - they’ll make sensible decisions. The stakes are therefore very high. **Technical clarity in an organization can be the difference between a functional engineering group and a completely dysfunctional one.**

### Why technical clarity is so rare

The default quantity of technical clarity in an organization is very low. In other words, **decision-makers at tech companies are often hopelessly confused about the technology in question**. This is not a statement about their competence. Software is _really complicated_, and even the engineers on the relevant team spend much of their time hopelessly confused about the systems they own.

In my experience, this is surprising to non-engineers. But it’s true! For large established codebases, it’s completely normal for very senior engineers to be unable to definitively answer even very basic questions about how their own system works, like “can a user of type X do operation Y”, or “if we perform operation Z, what will it look like for users of type W?” Engineers often[2](https://www.seangoedecke.com/clarity/#fn-2) answer these questions with “I’ll have to go and check”.

Suppose a VP at a tech company wants to offer an existing paid feature to a subset of free-tier users. Of course, most of the technical questions involved in this project are irrelevant to the VP. But there is a set of technical questions that they _will_ need to know the answers to:

1.   Can the paid feature be safely delivered to free users in its current state?
2.   Can the feature be rolled out gradually?
3.   If something goes wrong, can the feature be reverted without breaking user accounts?
4.   Can a subset of users be granted early access for testing (and other) purposes?
5.   Can paid users be prioritized in case of capacity problems?

**Finding out the answer to these questions is a complex technical process.** It takes a deep understanding of the entire system, and usually requires you to also carefully re-read the relevant code. You can’t simply try the change out in a developer environment or on a test account, because you’re likely to miss edge cases. Maybe it works for your test account, but it doesn’t work for users who are part of an “organization”, or who are on a trial plan, and so on.

**Sometimes they can only be answered by actually performing the task.** I wrote about why this happens in [_Wicked features_](https://www.seangoedecke.com/wicked-features): as software systems grow, they build marginal-but-profitable features that interact with each other in surprising ways, until the system becomes _almost_ - but not quite - impossible to understand. Good software design can tame this complexity, but never eliminate it. Experienced software engineers are thus always suspicious that they’re missing some interaction that will turn into a problem in production.

### Official and unofficial technical advisors

For a VP or product leader, it’s an enormous relief to work with an engineer who can be relied on to help them navigate the complexities of the software system. In my experience, this “technical advisor” role is usually filled by staff engineers, or by senior engineers who are rapidly on the path to a staff role. Senior engineers who are good at providing technical clarity sometimes get promoted to staff without even trying, in order to make them a more useful tool for the non-technical leaders who they’re used to helping.

Of course, you can be an impactful engineer without doing the work of providing technical clarity to the organization. Many engineers - even staff engineers - deliver most of their value by shipping projects, identifying tricky bugs, doing good [systems design](https://www.seangoedecke.com/good-system-design), and so on. But those engineers will rarely be as valued as the ones providing technical clarity. That’s partly because senior leadership at the company will remember who was helping them, and partly because technical clarity is just much higher-leverage than almost any single project.

Non-technical leaders need to make decisions, whether they’re clear or not. They are thus highly motivated to maintain a mental list of the engineers who can help them make those decisions, and to position those engineers in the most important teams and projects.

From the perspective of non-technical leaders, **those engineers are an abstraction around technical complexity**. In the same way that engineers use garbage-collected languages so they don’t have to care about memory management, VPs use engineers so they don’t have to care about the details of software.

### Tolerating uncertainty

But what does it feel like _inside the abstraction_? Internally, engineers do have to worry about all the awkward technical details, even if their non-technical leaders don’t have to. If I say “no problem, we’ll be able to roll back safely”, I’m not as confident as I appear. When I’m giving my opinion on a technical topic, I top out at 95% confidence - there’s always a 5% chance that I missed something important - and am usually lower than that. I’m always at least a little bit worried.

Why am I worried if I’m 95% sure I’m right? Because I’m worrying about the things I don’t know to look for. When I’ve been spectacularly wrong in my career, it’s usually not about risks that I anticipated. Instead, it’s about the “unknown unknowns”: risks that I didn’t even contemplate, because my understanding of the overall system was missing a piece. That’s why I say that [shipping a project takes your full attention](https://www.seangoedecke.com/how-to-ship). When I lead technical projects, I spend a lot of time sitting and wondering about what I haven’t thought of yet.

In other words, even when I’m quite confident in my understanding of the system, I still have a background level of internal paranoia. **To provide technical clarity to the organization, I have to keep that paranoia to myself.** There’s a careful balance to be struck between verbalizing all my worries - more on that later - and between being so overconfident that I fail to surface risks that I ought to have mentioned.

Like good engineers, good VPs understand that [all abstractions are sometimes leaky](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/). They don’t blame their engineers for the occasional technical mistake, so long as those engineers are doing their duty as a useful abstraction the rest of the time[3](https://www.seangoedecke.com/clarity/#fn-3). What they won’t tolerate in a technical advisor is **the lack of a clear opinion at all**. An engineer who answers most questions with “well, I can’t be sure, it’s really hard to say” is useless as an advisor. They may still be able to write code and deliver projects, but they will not increase the amount of technical clarity in the organization.

### Isn’t hiding your uncertainty just lying?

When I’ve [written about communicating confidently](https://www.seangoedecke.com/taking-a-position) in the past, some readers think I’m advising engineers to act unethically. They think that careful, technically-sound engineers should communicate the exact truth, in all its detail, and that appearing more confident than you are is a con man’s trick: of _course_ if you pretend to be certain, leadership will think you’re a better engineer than the engineer who honestly says they’re not sure. Once one engineer starts keeping their worries to themself, other engineers have to follow or be sidelined, and pretty soon all the fast-talking blowhards are in positions of influence while the honest engineers are relegated to just working on projects.

In other words, when I say “no problem, we’ll be able to roll back”, even though I might have missed something, **isn’t that just lying?** Shouldn’t I just communicate my level of confidence accurately? For instance, could I instead say “I _think_ we’ll be able to roll back safely, though I can’t be sure, since my understanding of the system isn’t perfect - there could be all kinds of potential bugs”? I don’t think so.

**Saying that engineers should strive for maximum technical accuracy betrays a misunderstanding of what clarity _is_**. At the top of this article, I said that clarity is when _non-technical decision makers_ have a good enough working understanding of the system. That necessarily means a _simplified_ understanding. When engineers are communicating to non-technical leadership, they must therefore simplify their communication (in other words, allow some degree of inaccuracy in the service of being understood).

**Most of my worries are not relevant information to non-technical decision makers**. When I’m asked “can we deliver this today”, or “is it safe to roll this feature out”, the person asking is looking for a “yes” or “no”. If I also give them a stream of vague technical caveats, they will have to consciously filter that out in order to figure out if I mean “yes” or “no”. Why would they care about any of the details? They know that I’m better positioned to evaluate the technical risk than them - that’s why they’re asking me in the first place!

I want to be really clear that I’m not advising engineers to always say “yes” even to bad or unacceptably risky decisions. Sometimes you need to say “we won’t be able to roll back safely, so we’d better be sure about the change”, or “no, we can’t ship the feature to this class of users yet”. My point is that when you’re talking to the company’s decision-makers, **you should commit to a recommendation one way or the other**, and only give caveats when the potential risk is extreme or the chances are genuinely high.

At the end of the day, a VP only has so many mental bits to spare on understanding the technical details. If you’re a senior engineer communicating with a VP, you should make sure you fill those bits with the most important pieces: what’s possible, what’s impossible, and what’s risky. Don’t make them parse those pieces out of a long stream of irrelevant (to them) technical information.

### Summary

The highest-leverage work I do is to provide technical clarity to the organization: communicating up to non-technical decision makers to give them context about the software system. This is hard for two reasons. First, even competent engineers find it difficult to answer simple questions definitively about large codebases. Second, non-technical decision makers cannot absorb the same level of technical nuance as a competent engineer, so communicating to them requires _simplification_.

Effectively simplifying complex technical topics requires three things:

1.   Good taste - knowing which risks or context to mention and which to omit[4](https://www.seangoedecke.com/clarity/#fn-4).
2.   A deep technical understanding of the system. In order to communicate effectively, I need to also be shipping code and delivering projects. If I lose direct contact with the codebase, I will eventually lose my ability to communicate about it (as the codebase changes and my memory of the concrete details fades).
3.   The confidence to present a simplified picture to upper management. Many engineers either feel that it’s dishonest, or lack the courage to commit to claims where they’re only 80% or 90% confident. In my view, these engineers are abdicating their responsibility to help the organization make good technical decisions. I write about this a lot more in [_Engineers who won’t commit_](https://www.seangoedecke.com/taking-a-position).

* * *

1.   In a large tech company, this is usually a director or VP. However, depending on the scope we’re talking about, this could even be a manager or product manager - the same principles apply.

[↩](https://www.seangoedecke.com/clarity/#fnref-1)
2.   Sometimes you know the answer off the top of your head, but usually that’s when you’ve been recently working on the relevant part of the codebase (and even then you may want to go and make sure you’re right).

[↩](https://www.seangoedecke.com/clarity/#fnref-2)
3.   You do still have to be right a lot. I wrote about this in [_Good engineers are right, a lot_](https://www.seangoedecke.com/being-right-a-lot).

[↩](https://www.seangoedecke.com/clarity/#fnref-3)
4.   Despite this being very important, I don’t have a lot to say about it. You just have to feel it out based on your relationship with the decision-maker in question.

[↩](https://www.seangoedecke.com/clarity/#fnref-4)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/clarity/&t=How%20I%20provide%20technical%20clarity%20to%20non-technical%20leaders).

October 12, 2025│ Tags: [tech companies](https://www.seangoedecke.com/tags/tech%20companies/)

* * *