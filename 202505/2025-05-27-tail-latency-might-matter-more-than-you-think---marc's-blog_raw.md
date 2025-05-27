Title: Tail Latency Might Matter More Than You Think

URL Source: https://brooker.co.za/blog/2021/04/19/latency.html

Markdown Content:
A frustratingly qualitative approach.

Tail latency, also known as _high-percentile_ latency, refers to high latencies that clients see fairly infrequently. Things like: “my service mostly responds in around 10ms, but sometimes takes around 100ms”. There are many causes of tail latency in the world, including contention, garbage collection, packet loss, host failure, and weird stuff operating systems do in the background. It’s tempting to look at the 99.9th percentile, and feel that it doesn’t matter. After all, 999 of 1000 calls are seeing lower latency than that.

Unfortunately, it’s not that simple. One reason is that modern architectures (like microservices and SoA) tend to have a lot of components, so one user interaction can translate into many, many, service calls. A common pattern in these systems is that there’s some _frontend_, which could be a service or some Javascript or an app, which calls a number of backend services to do what it needs to do. Those services then call other services, and so on. This forms two kinds of interactions: parallel fan-out, where the service calls many backends in parallel and waits for them all to complete, and serial chains where one service calls another, which calls another, and so on.

![Image 1: Service call graph showing fan-out and serial chains](https://mbrooker-blog-images.s3.amazonaws.com/call_graph.png)

These patterns make tail latency more important than you may think.

To understand why, let’s do a simple numerical experiment. Let’s simplify the world so that all services respond with the same latency, and that latency follows a very simple bimodal distribution: 99% of the time with a mean of 10ms (normally distributed with a standard deviation of 2ms), and 1% of the time with a mean of 100ms (and SD of 10ms). In the real world, service latencies are almost always multi-modal like this, but typically not just a sum of normal distributions (but that doesn’t matter here).

**Parallel Calls**

First, let’s consider parallel calls. The logic here is simple: we call N services in parallel, and wait for the slowest one. Applying our intuition suggests that as N increases, it becomes more and more likely that we’ll wait for a ~100ms _slow_ call. With N=1, that’ll happen around 1% of the time. With N=10, around 10% of the time. In this simple model, that basic intuition is right. This is what it looks like:

The tail mode, which used to be quite rare, starts to dominate as N increases. What was a rare occurrence is now normal. Nearly everybody is having a bad time.

**Serial Chains**

Serial chains are a little bit more interesting. In this model, services call services, down a chain. The final latency is the sum of all of the service latencies down the chain, and so there are a lot more cases to think about: 1 _slow_ service, 2 slow services, etc. That means that we can expect the overall shape of the distribution to change as N increases. Thanks to the central limit theorem we could work out what that looks like as N gets large, but the journey there is interesting too.

Here, we’re simulating the effects of chain length on the latency of two different worlds. One _Tail_ world which has the bimodal distribution we describe above, and one _No Tail_ world which only has the primary distribution around 10ms.

Again, the tail latency becomes more prominent here. That relatively rare tail increases the variance of the distribution we’re converging on by a factor of 25. That’s a huge difference, caused by something that didn’t seem too important to start with.

**Choosing Summary Statistics** One way that this should influence your thinking is in how you choose which latency statistics to monitor. The truth is that no summary statistic is going to give you the full picture. Looking at histograms is cool, but tends to miss the time component. You could look at some kind of windowed histogram heat map, but probably won’t. Instead, make sure you’re aware of the high percentiles of service latency, and consider monitoring common customer or client use-cases and monitoring their end-to-end latency experience.

Trimmed means, winsorized means, truncated means, interquartile ranges, and other statistics which trim off some of the tail of the distribution seem to be gaining in popularity. There’s a lot to like about the trimmed mean and friends, but cutting off the right tail will cause you to miss effects where that tail is very important, and may become dominant depending on how clients call your service.

I continue to believe that if you’re going to measure just one thing, make it [the mean](https://brooker.co.za/blog/2017/12/28/mean.html). However, you probably want to measure more than one thing.
