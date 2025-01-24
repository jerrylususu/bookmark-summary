Title: Why are big tech companies so slow?

URL Source: https://www.seangoedecke.com/difficulty-in-big-tech/

Markdown Content:
Big tech companies spend a lot of time and money building things that a single, motivated engineer could build in a weekend. This fact puzzles a lot of people who don’t work in big tech. Often those people share theories about why this is true:

1.  Big tech engineers are incompetent and unproductive, and big tech routinely wastes billions of dollars in salary on bad hires
2.  Big tech companies use processes, like Agile, that are so inherently inefficient as to slow down work by 100x for no good reason
3.  Big tech engineers are lazy and are stealing time from their employers
4.  Big tech companies are dominated by coordination problems that sap much of the value of each extra engineer
5.  Big tech operates at web scale, so comparing weekend features to big tech features is like comparing a diecast toy car to a Ferrari

The first theory - that their engineers are incompetent - is widely held by game devs and hackers, who have a particular disdain for how slow and inefficient big company code often is. You’ll see these people doing back-of-envelope estimates for how fast it “should” be to serve a HTTP request, and scoffing at big company web apps that are 10x or 100x slower than that. The second, third, and fourth theories are typically held by startup grinders, who believe that operating with low process and hiring people dedicated to the mission is their comparative advantage against big tech companies. The fifth theory is held by big tech employees themselves (or engineers who are temporarily-embarassed big tech employees). The idea here is that big tech companies just work on a different level than your personal projects or lowly startups, so you couldn’t even begin to understand what it takes to build a CRUD form in that environment.

All of these theories are wrong. Many big tech engineers are lazy or incompetent, or slowed down by bad process, but big tech companies are not stupid: they still keep hiring engineers because it’s fabulously profitable to do so.

### Balancing features

So why do big tech companies find it so much harder to build? It’s the scale of the app itself: not the number of traffic or users, but the number of _features_. As that number grows, it becomes more and more difficult to build and ship new features. The reason is straightforwardly mathematical. Each new feature potentially interacts with all the features before it. You have to check to make sure it doesn’t interfere with an existing feature, and if it does, you have make some kind of balancing change to keep both features working.

Features can interfere with each other in many different ways. Sometimes it’s a simple design problem: we want to add an export button, but we already have a save button in that spot. Sometimes it’s a conceptual problem: we allow users to delete their saved data, but now we’re building a way for users to extend other users’ public data - does that count as the original user’s data or the new user’s? Sometimes it’s a scale problem: a previous feature involves an expensive computation that will be caused to execute thousands of times a second by a new feature. Sometimes it’s a pure organization-of-the-codebase problem, or a legal problem, or a problem with GDPR, and so on. I could list examples of these forever.

To someone without a lot of big tech experience, this can look like a problem with the codebase. It just seems so awkward and complicated - if it were correctly factored, all of this would be so much easier. But this is an error. First, you’ll never get around the mathematics of adding new features, no matter how nice the code is. Second, big tech codebases are awkward _because_ balancing features is difficult, not the other way around. An ungainly big tech codebase is the agglomeration of millions of small feature-balancing decisions (i.e. edge cases) over many years. That’s where all the value comes from! You can build any of the individual features in a weekend. But the next feature will take four days, and the one after that a whole week, and pretty soon you’ll be operating at the speed of big tech.

### Wicked features

Much of the complexity is produced by a small set of what I call “wicked features”, which interfere with _every other_ feature. For instance, adding a whole new user type: once you do that, you have to ask “can this user type access this feature” for every feature for the rest of the company’s life. Adding a new deployment environment is a popular example of this (for instance, offering your cloud-based SaaS as an on-premise deployment). Unfortunately, these features are often the most lucrative by far, because they unlock huge enterprise customers. So big tech companies often have multiple wicked features.

Incidentally, this is why the quality of big tech engineering is sometimes worse than you would expect. The cognitive load of operating in this environment is pretty intense. Delivering anything at all is [really, really difficult](https://www.seangoedecke.com/how-to-ship). So really obvious balls sometimes get dropped because the engineer in question was trying to thread a path between ten other features.

### Why not just build less features?

The obvious solution - obvious enough that every big tech leader is well aware of it - is to _limit features_. This is a big reason why internal projects fail: they grow complex enough that the potential benefits are outweighed by the ongoing cost, and the executive sponsor gets cold feet. Ironically, despite being good for speed in the long run, this makes big tech companies seem even slower from the outside. Six months spent working on a feature that is (correctly) axed before shipping makes it look like the next feature took an extra six months to build.

To state another obvious point: features also make money. In big tech companies, features that seem trivial often make a lot of money. Dan Luu makes this point better than anyone I’ve seen [here](https://danluu.com/sounds-easy/):

> Features also matter: when I talk to engineers working on basically any product at any company, they’ll often find that there are seemingly trivial individual features that can add integer percentage points to revenue. Just as with performance, people underestimate how many engineers you can add to a product before engineers stop paying for themselves.

Startups don’t care about marginal features because their success is entirely dominated by finding a single successful feature that anybody wants to pay for. Big companies by definition have at least one successful feature that’s already driving lots of revenue, so they care a _lot_ about marginal features. 1% of Google Ads or AWS S3 revenue is a lot of money. Big companies are thus incentivized to keep adding complexity until it’s literally impossible to add any more.

### Summary

Why are big tech companies slow? Because they’ve packed in as many features as possible in order to make more money, and the interaction of existing features adds an unimaginable amount of cognitive load. Some hackers are revolted by this, because they love simple tools that do one thing well. That’s a fair reaction. But don’t let your revulsion fool you into thinking that big tech companies are full of stupid people.

Capturing value at the margin is really difficult to do well. That’s why big tech pays big tech salaries for it!
