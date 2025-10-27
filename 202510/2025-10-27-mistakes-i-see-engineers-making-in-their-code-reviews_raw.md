Title: Mistakes I see engineers making in their code reviews

URL Source: https://www.seangoedecke.com/good-code-reviews/

Markdown Content:
In the last two years, code review has gotten much more important. Code is now easy to generate using LLMs, but it’s still just as hard to review[1](https://www.seangoedecke.com/good-code-reviews/#fn-1). Many software engineers now spend as much (or more) time reviewing the output of their own AI tools than their colleagues’ code.

I think a lot of engineers don’t do code review correctly. Of course, there are lots of different ways to do code review, so this is largely a statement of my [engineering taste](https://www.seangoedecke.com/taste).

### Don’t just review the diff

The biggest mistake I see is **doing a review that focuses solely on the diff**[2](https://www.seangoedecke.com/good-code-reviews/#fn-2). Most of the highest-impact code review comments have very little to do with the diff at all, but instead come from your understanding of the rest of the system.

For instance, one of the most straightforwardly useful comments is “you don’t have to add this method here, since it already exists in this other place”. The diff itself won’t help you produce a comment like this. You have to already be familiar with other parts of the codebase that the diff author doesn’t know about.

Likewise, comments like “this code should probably live in this other file” are very helpful for maintaining the long-term quality of a codebase. The cardinal value when working in large codebases is _consistency_ (I write about this more in [_Mistakes engineers make in large established codebases_](https://www.seangoedecke.com/large-established-codebases)). Of course, you cannot judge consistency from the diff alone.

Reviewing the diff by itself is much easier than considering how it fits into the codebase as a whole. You can rapidly skim a diff and leave line comments (like “rename this variable” or “this function should flow differently”). Those comments might even be useful! But you’ll miss out on a lot of value by only leaving this kind of review.

### Don’t leave too many comments

Probably my most controversial belief about code review is that **a good code review shouldn’t contain more than five or six comments**. Most engineers leave too many comments. When you receive a review with a hundred comments, it’s very hard to engage with that review on anything other than a trivial level. Any really important comments get lost in the noise[2.5](https://www.seangoedecke.com/good-code-reviews/#fn-2.5).

What do you do when there are twenty places in the diff that you’d like to see updated - for instance, twenty instances of `camelCase` variables instead of `snake_case`? Instead of leaving twenty comments, I’d suggest leaving a single comment explaining the stylistic change you’d like to make, and asking the engineer you’re reviewing to make the correct line-level changes themselves.

There’s at least one exception to this rule. When you’re onboarding a new engineer to the team, it can be helpful to leave a flurry of stylistic comments to help them understand the specific dialect that your team uses in this codebase. But even in this case, you should bear in mind that any “real” comments you leave are likely to be buried by these other comments. You may still be better off leaving a general “we don’t do early returns in this codebase” comment than leaving a line comment on every single early return in the diff.

### Don’t review with a “how would I write it?” filter

One reason engineers leave too many comments is that they review code like this:

1.   Look at a hunk of the diff
2.   Ask themselves “how would I write this, if I were writing this code?”
3.   Leave a comment with each difference between how they would write it and the actual diff

This is a good way to end up with hundreds of comments on a pull request: an endless stream of “I would have done these two operations in a different order”, or “I would have factored this function slightly differently”, and so on.

I’m not saying that these minor comments are always bad. Sometimes the order of operations really does matter, or functions really are factored badly. But one of my strongest opinions about software engineering is that **there are multiple acceptable approaches to any software problem**, and that which one you choose often comes down to [taste](https://www.seangoedecke.com/taste).

As a reviewer, when you come across cases where you would have done it differently, you must be able to approve those cases without comment, so long as either way is acceptable. Otherwise you’re putting your colleagues in an awkward position. They can either accept all your comments to avoid conflict, adding needless time and setting you up as the _de facto_ gatekeeper for all changes to the codebase, or they can push back and argue on each trivial point, which will take even more time. **Code review is not the time for you to impose your personal taste on a colleague.**

### If you do not want a change to be merged, leave a blocking review

So far I’ve only talked about review comments. But the “high-order bit” of a code review is not the content of the comments, but the _status_ of the review: whether it’s an approval, just a set of comments, or a blocking review. The status of the review colors all the comments in the review. Comments in an approval read like “this is great, just some tweaks if you want”. Comments in a blocking review read like “here’s why I don’t want you to merge this in”.

**If you want to block, leave a blocking review.** Many engineers seem to think it’s rude to leave a blocking review even if they see big problems, so they instead just leave comments describing the problems. Don’t do this. It creates a culture where nobody is sure whether it’s okay to merge their change or not. An approval should mean “I’m happy for you to merge, even if you ignore my comments”. Just leaving comments should mean “I’m happy for you to merge if someone else approves, even if you ignore my comments.” If you would be upset if a change were merged, you should leave a blocking review on it. That way the person writing the change knows for sure whether they can merge or not, and they don’t have to go and chase up everyone who’s left a comment to get their informal approval.

### Most reviews should be approvals

I should start with a caveat: this depends a lot on what kind of codebase we’re talking about. For instance, I think it’s fine if PRs against something like [SQLite](https://github.com/sqlite/sqlite) get mostly blocking reviews. But a standard SaaS codebase, where teams are actively developing new features, ought to have mostly approvals. I go into a lot more detail about the distinction between these two types of codebase in [_Pure and Impure Engineering_](https://www.seangoedecke.com/pure-and-impure-engineering).

If tons of PRs are being blocked, it’s usually a sign that **there’s too much gatekeeping going on**. One dynamic I’ve seen play out a lot is where one team owns a bottleneck for many other teams’ features - for instance, maybe they own the edge network configuration where new public-facing routes must be defined, or the database structure that new features will need to modify. That team is typically more reliability-focused than a typical feature team. Engineers on that team may have a different title, like SRE, or even belong to a different organization. Their incentives are thus misaligned with the feature teams they’re nominally supporting.

Suppose the feature team wants to update the public-facing ingress routes in order to ship some important project. But the edge networking team doesn’t care about that project - it doesn’t affect their or their boss’s review cycles. What does affect their reviews is any production problem the change might cause. That means they’re motivated to block _any_ potentially-risky change for as long as possible. This can be very frustrating for the feature team, who is willing to accept some amount of risk for the sake of delivering new features[3](https://www.seangoedecke.com/good-code-reviews/#fn-3).

Of course, there are other reasons why many PRs might be getting blocking reviews. Maybe the company just hired a bunch of incompetent engineers, who ought to be prevented from merging their changes. Maybe the company has had a recent high-profile incident, and all risky changes should be blocked for a couple of weeks until their users forget about it. But in normal circumstances, **a high rate of blocked reviews represents a structural problem**.

For many engineers - including me - it feels good to leave a blocking review, for the same reasons that it feels good to gatekeep in general. It feels like you’re single-handedly protecting the quality of the codebase, or averting some production incident. It’s also a way to indulge a common vice among engineers: flexing your own technical knowledge on some less-competent engineer. Oh, looks like you didn’t know that your code would have caused an N+1 query! Well, _I_ knew about it. Aren’t you lucky _I_ took the time to read through your code?

This principle - that **you should bias towards approving changes** - is important enough that Google’s own [guide to code review](https://google.github.io/eng-practices/review/) begins with it, calling it ”_the_ senior principle among all of the code review guidelines”[4](https://www.seangoedecke.com/good-code-reviews/#fn-4).

### Final thoughts

I’m quite confident that many competent engineers will disagree with most or all of the points in this post. That’s fine! I also believe many obviously true things about code review, but I didn’t include them here.

In my experience, it’s a good idea to:

*   Consider what code _isn’t_ being written in the PR instead of just reviewing the diff
*   Leave a small number of well-thought-out comments, instead of dashing off line comments as you go and ending up with a hundred of them
*   Review with a “will this work” filter, not with a “is this exactly how I would have done it” filter
*   If you don’t want the change to be merged, leave a blocking review
*   Unless there are very serious problems, approve the change

This all more or less applies to reviewing code from agentic LLM systems. They are particularly prone to missing code that they ought to be writing, they also get a bit lost if you feed them a hundred comments at once, and they have their own style. The one point that does _not_ apply to LLMs is the “bias towards approving” point. You can and should gatekeep AI-generated PRs as much as you want.

I do want to close by saying that **there are many different ways to do code review**. Here’s a non-exhaustive set of values that a code review practice might be trying to satisfy: making sure multiple people on the team are familiar with every part of the codebase, letting the team discuss the software design of each change, catching subtle bugs that a single person might not see, transmitting knowledge horizontally across the team, increasing perceived ownership of each change, enforcing code style and format rules across the codebase, and satisfying SOC2 “no one person can change the system alone” constraints. I’ve listed these in the order I care about them, but engineers who would order these differently will have a very different approach to code review.

edit: This post got some mostly-positive comments on both [lobste.rs](https://lobste.rs/s/ngei5p/mistakes_i_see_engineers_making_their) and [Hacker News](https://news.ycombinator.com/item?id=45701404). Several people didn’t like the “camel case vs snake case” example, because they thought it should be caught by tooling - fair enough, but the principle holds for changes that can’t be as easily caught by tooling, like “log with certain tags before write operations”. This [chain of comments](https://news.ycombinator.com/item?id=45702780) is an interesting discussion on the norms around leaving blocking reviews. Finally, the top lobste.rs [comment](https://lobste.rs/c/bsnn0w) thinks I’m misrepresenting Google’s guidelines by paraphrasing it as “bias for approval”. It seems really clear to me that the Google principle is aimed to convince smart, nitpicky engineers that they ought to be approving more changes - but that’s definitely an interpretation on my part.

* * *

1.   Of course there are LLM-based reviewing tools. They’re even pretty useful! But at least right now they’re not as good as human reviewers, because they can’t bring to bear the amount of general context that a competent human engineer can.

[↩](https://www.seangoedecke.com/good-code-reviews/#fnref-1)
2.   For readers who aren’t software engineers, “diff” here means the difference between the existing code and the proposed new code, showing what lines are deleted, added, or edited.

[↩](https://www.seangoedecke.com/good-code-reviews/#fnref-2)
3.   This is a special instance of a general truth about communication: if you tell someone one thing, they’ll likely remember it; if you tell them twenty things, they will probably forget it all.

[↩](https://www.seangoedecke.com/good-code-reviews/#fnref-2.5)
4.   In the end, these impasses are typically resolved by the feature team complaining to their director or VP, who complains to the edge networking team’s director or VP, who tells them to just unblock the damn change already. But this is a pretty crude way to resolve the incentive mismatch, and it only really works for features that are high-profile enough to receive air cover from a very senior manager.

[↩](https://www.seangoedecke.com/good-code-reviews/#fnref-3)
5.   Google’s principle is much more explicit, stating that you should approve a change if it’s even a minor improvement, not when it’s perfect. But I take the underlying message here to be “I know it feels good, but don’t be a nitpicky gatekeeper - approve the damn PR!”

[↩](https://www.seangoedecke.com/good-code-reviews/#fnref-4)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/good-code-reviews/&t=Mistakes%20I%20see%20engineers%20making%20in%20their%20code%20reviews).

October 25, 2025│ Tags: [good engineers](https://www.seangoedecke.com/tags/good%20engineers/), [software design](https://www.seangoedecke.com/tags/software%20design/), [explainers](https://www.seangoedecke.com/tags/explainers/), [ai](https://www.seangoedecke.com/tags/ai/)

* * *