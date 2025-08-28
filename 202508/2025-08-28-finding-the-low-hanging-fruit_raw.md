Title: Finding the low-hanging fruit

URL Source: https://www.seangoedecke.com/low-hanging-fruit/

Markdown Content:
Suppose your job is to pick fruit in a giant orchard. The orchard covers several hills and valleys, and is big enough that you’d need a few weeks to walk all the way around the edge. What should you do first?

### What is low-hanging fruit?

Like a good engineer, you might reduce this to an optimization problem: in order to harvest the most fruit possible, you should maximise the quantity of fruit you get from each individual tree. Just by walking up to a tree, you estimate you can get about thirty percent of the fruit by standing on your tiptoes, but most of the fruit is higher than you can reach. You start by building a tall ladder so you can pick fruit from the highest branches, which ups your yield percentage to ninety percent. But some fruit is out wide as well as high up, on branches too flimsy to lean a ladder against. So you design a picker arm that lets you reach out sideways to pick more fruit. This ups your yield to ninety-five percent, but the arm isn’t perfect - there’s fruit that’s awkward to reach, or that clings to the tree too tightly for the arm to pluck it off. You tweak your picker arm design, incrementally improving your yield. After a lot of work you triumphantly achieve ninety-eight percent.

Meanwhile, some other joker has wandered off into a nearby valley, where the trees have ten times as much fruit on them, and has come out with three times as much fruit as you just by mindlessly picking what they could reach.

The obvious moral is that **you should try to pick the low-hanging fruit**. Setting aside the metaphor, you should try to spend your time doing the kind of work that delivers the most value for the least amount of effort. At a tech company, the value of work is highly variable[1](https://www.seangoedecke.com/low-hanging-fruit/#fn-1). Some engineers spend weeks of hard work for the same amount of value as other engineers deliver in half an hour. This is not an exaggeration - I have seen this happen more times than I can count.

I’m mostly going to talk about performance optimization here, since it’s what I have experience in, but the same principles apply for other kinds of work. If you’re looking to improve awful design or UX, or to catch easy-to-fix bugs, you can get an order of magnitude more value for your effort by getting better at identifying low-hanging fruit.

### Low-hanging fruit at tech companies

But how do you actually do that? The easiest way is to **listen for what the company is telling you**. Companies usually have a small set of active priorities at any given time. Working on those priorities is typically very highly leveraged, because you have the entire momentum of the company behind you. As a concrete example: shipping some polish on an old established feature might at best deliver some incremental value, but shipping the same polish on a brand-new high-profile feature might determine whether the feature succeeds or fails.

However, there’s also lots of low-hanging fruit from a technical perspective. I have spent a lot of time in my career speeding up endpoints and page loads. It’s one of my favourite things to do[2](https://www.seangoedecke.com/low-hanging-fruit/#fn-2). The same principle applies here: many engineers spend a lot of time shaving 5ms off a page load by micro-optimizing asset sizes or extracting logic into a cached code path, when another page (or even the same page) spends 200ms in an un-indexed database query, or a completely avoidable N+1 query loop.

**When you’re trying to optimize, you should take as wide a view as possible.** Don’t stop when you see the first thing that looks slow. Scan through the whole thing, taking notes as you go, in case you see something that looks even worse later on. Most code paths (more on this later) will have multiple areas you could optimize if you wanted to. Picking the low-hanging fruit means starting with the worst bit.

### Profiling and metrics

If you can, **profile before optimizing**. I like to use [flamegraphs](https://www.brendangregg.com/flamegraphs.html) where possible: visualizations of the call stack where the initial caller sits at the bottom and the stack extends vertically.

![Image 1: cpu](https://www.seangoedecke.com/e2e7d0e8b092db6d25db6c3e92077bbf/cpu-mysql-updated.svg)

The huge benefit of this approach is that you can just see which operations are taking the most time. When you can generate a flamegraph, low-hanging-fruit optimization becomes almost a mechanical process: take the longest span that originates from your own code (i.e. not from libraries or frameworks), see how much quicker you can make it, then move to the next longest span and repeat.

However, bear in mind that flamegraphs can be misleading. They only give you the data for a single request. Sometimes the lowest-hanging fruit only occurs in a subset of requests (i.e. for customers with lots of records in your system, or when a cache miss occurs for a particular internal API). To catch cases like these, **you should pay attention to metrics**. Specifically, p95 and p99 request duration metrics, which means metrics that track how slow your slowest 5% or 1% of requests are.

If you’re just looking at averages, you might miss that your snappy 100ms API request actually takes five seconds for some cohort of users. Optimizing that away won’t have a significant impact on the average duration (maybe it’ll take it from 100ms to 99ms), but it’ll have a significant impact on those users. This is more important than it sounds, because your slowest 1% of users are probably your _biggest_ 1% of users, which means they’re probably paying you the most money and are your most important set of customers.

### Where is the low-hanging fruit?

Suppose you’re not looking at a single API endpoint. Instead, you’re looking at an entire API, or an entire service, or even an entire company. How do you know where to look for low-hanging fruit? The best trick I know is to think through the problem backwards. **What areas are likely to have already been aggressively optimized?**

The very highest-traffic or most visible endpoints are probably in this category. If I joined Facebook, I would not expect to be able to find easy performance wins on the facebook.com page load. It’s just been too visible for too long - engineers will have already paid them enough attention to catch the really obvious problems. Likewise, if there’s already been an optimization effort in a particular area, you probably won’t find much low-hanging fruit there. Finally, if the code is brand-new, it’s probably been acceptably optimized. In a technically competent company, the worst problems tend to build up over time as layers of cruft.

The other principle is that **code that is easy to optimize will typically get optimized**. If you’re part of a large group looking for someone’s dropped keys at night, don’t look under the streetlights - someone else will probably notice the keys if they’re in a well-lit spot. Look in the dark or dirty spots where other searchers might pay less attention. Code that is easy to read, well-factored, and in a language familiar to the company is likely to get optimized. Gnarly legacy code or code that’s in an unfamiliar language will get ignored. This goes double when changes to the code are dangerous (as is the case for billing code).

So if you’re looking for low-hanging fruit, look for:

1.   Endpoints or pages that are in the second or third tier of visibility - important enough to optimize, but not so important that they’ve already been optimized
2.   Old code. The older the better
3.   Code that’s hard to read or not in the main language the company uses
4.   Code that’s scary to touch

Of course, it’s possible to improve code that’s not in this category. But you’re far more likely to find the kind of “add one line of code to improve p95 latency by 500ms” easy wins in code that fits these conditions.

* * *

1.   For much more on that, see my posts [_What is Important_](https://www.seangoedecke.com/what-is-important), [_The Spotlight_](https://www.seangoedecke.com/the-spotlight), and [_Crushing JIRA tickets is a party trick, not a path to impact_](https://www.seangoedecke.com/party-tricks). Of course “value” here is a bit subjective - I mean value _to the company_, or more specifically shareholder value. But I think this also applies to “value for customers”, or whatever other definition of value you prefer.

[↩](https://www.seangoedecke.com/low-hanging-fruit/#fnref-1)
2.   That’s what I regret most about the [industry turn](https://www.seangoedecke.com/good-times-are-over) in ~2023: you used to be able to spend most of your time doing this kind of optimization work, but now you have to deliver shareholder value more directly. I miss it.

[↩](https://www.seangoedecke.com/low-hanging-fruit/#fnref-2)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/low-hanging-fruit/&t=Finding%20the%20low-hanging%20fruit).

August 26, 2025│ Tags: [tech companies](https://www.seangoedecke.com/tags/tech%20companies/)

* * *