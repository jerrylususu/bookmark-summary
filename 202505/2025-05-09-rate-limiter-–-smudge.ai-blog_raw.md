Title: rate limiter – smudge.ai blog

URL Source: https://smudge.ai/blog/ratelimit-algorithms

Markdown Content:
Visualizing algorithms for rate limiting
----------------------------------------

May 15, 2024

Why rate limit?
---------------

Imagine a Twitch chat with many active participants and just one spammer. Without rate limiting, the sole spammer can easily dominate the entire conversation. With rate limiting, each user has a fair chance to participate.

A rate limiter lets you control the rate of traffic that your service processes by blocking requests that exceed a set limit during a period of time. This is useful beyond just throttling spam in a chat. For instance, rate limiting a login form can deter brute force attacks while still allowing a small burst of incorrect guesses.

API endpoints are also frequently rate-limited to prevent any single user from monopolizing resources. Imagine that you want users to only be able to hit an expensive endpoint 100 times per minute. You could track hits with a counter that resets every minute. Any request after the 100th within that minute gets blocked. This is one of the simplest rate-limiting algorithms, called a **fixed window limiter**, and is a common way to control traffic to a service.

But it’s not always that simple.

When does each one-minute window begin and end? If I begin a burst of requests near the end of a window, can I exceed the limit? Is a window’s capacity restored one request at a time, or all at once?

In this post, we’ll explore the three most common algorithms to answer each of these questions.

1.  [Fixed windows](https://smudge.ai/blog/ratelimit-algorithms#fixed-windows)
2.  [Sliding windows](https://smudge.ai/blog/ratelimit-algorithms#sliding-windows)
3.  [Token buckets](https://smudge.ai/blog/ratelimit-algorithms#token-buckets)

Fixed windows
-------------

A set number of requests can be made within a predefined time window. Requests increment a counter that’s reset to zero at the start of each window.

_Allow 6 requests per day (24-hour windows)_

> Each green dot  represents an allowed request while  is a request blocked by the rate limiter. You can add more requests with the Hit button, which pauses the automatic stream.

*   Pros
    *   Simple to implement and understand
    *   Predictable for users
*   Cons
    *   Allows bursts up to 2x the `limit` when requests begin near the end of a window
*   Real-world example
    *   GitHub’s API uses a fixed window rate limiter with `limit = 5000`, `windowDuration = 1h`, and `windowStart` set to the start of each wall clock hour, allowing users 5,000 requests per hour.

**A brief tangent on 24-hour fixed windows**

There is a subtle issue with the 24-hour limiter above. Its windows reset every day at midnight—but midnight according to _which time zone_? A standard fixed window might reset its counter according to your server’s midnight or a standard timezone offset such as UTC. A user in a different timezone who just ran out of requests might retry just after midnight and be surprised if the limit hasn’t been lifted—since, to them, it is a new calendar day.

For these applications, you need to offset your window starts according to the user’s time zone, which has some potential for abuse as users can manually adjust their timezone once they’ve run out of requests to gain up to 1 full window of additional requests. Worse yet, users traveling west to east might incorrectly have more requests limited, while those traveling east to west might incorrectly have more requests allowed. If a rate limit resets based on local midnight and a user moves to an earlier time zone, they encounter earlier local midnights. This can allow them to reset their request count sooner by being in a new “day” earlier than expected, potentially increasing their total allowable requests within a 24-hour period as measured by real time. Yikes. And we still haven’t dealt with DST.

This use case is already a bit of a tangent, so for now I’ll leave it at this: handling time zones correctly, accounting for users relocating as well as daylight savings, is difficult to get right—so if you’re considering going down that painful path, I’ll just [point](https://stackoverflow.com/questions/2532729/daylight-saving-time-and-time-zone-best-practices/3269325#3269325) [you](https://www.creativedeletion.com/2015/01/28/falsehoods-programmers-date-time-zones.html) [to](https://www.youtube.com/watch?v=-5wpm-gesOY) [these](https://2ality.com/2021/06/temporal-api.html#time-zones-vs.-time-offsets) [resources](https://tech.bluesmoon.info/2013/08/dont-guess-at-timezones-in-javascript.html) instead. If you can sidestep this problem by using any other approach at all, you should!

#### Fixed window with user-defined start

Instead of fixing the start times to a set interval, each window can be created at the time of the user’s first request within that window.

With this approach, it’s especially important to show users the time remaining until the next window once they’re limited since there’s no set time that aligns each window.

Sliding windows
---------------

Instead of refreshing the capacity all at once, sliding windows refill one request at a time.

*   Pros
    *   Smooths the distribution of request traffic
    *   Well-suited for high loads
*   Cons
    *   Less predictable for users than fixed windows
    *   Storing timestamps for each request is resource-intensive

Because sliding windows tend to be most useful in high-traffic scenarios, the fact that the naive algorithm is resource-intensive is counterproductive. Shouldn’t a high-traffic rate limiter use an efficient algorithm? For this reason, most real-world sliding window rate limiters, such as those provided by [Upstash](https://upstash.com/docs/oss/sdks/ts/ratelimit/algorithms#sliding-window) or [Cloudflare](https://www.cloudflare.com/application-services/products/rate-limiting/), use an approximation, often called a floating window. Using this approximation, we have all the same pros but can remove the “resource-intensive” point from the cons. Here’s how it works:

1.  Count the number of allowed requests in the previous fixed window.
2.  Count the number of allowed requests in the current fixed window.
3.  Weight the previous window’s allowed requests proportional to that window’s overlap with a floating window ending at the current time.
4.  Add the weighted requests from (3) to the unweighted requests from (2).

In other words, this is the computation:

```
approximation = (prevWindowCount * prevWindowWeight) + currentWindowCount
```

  
In practice, this approximation limits requests at roughly the same proportion but is far more efficient than tracking all the requests’ timestamps. While the two algorithms will end up blocking different requests, the long term average number of blocked requests should be very close. See for yourself how it compares:

Precise window: limited 0

Approximated: limited 0

*   Real-world example
    *   Cloudflare’s configurable rate limiter uses an [approximated sliding window](https://blog.cloudflare.com/counting-things-a-lot-of-different-things).

Token buckets
-------------

Instead of thinking in terms of windows with durations, picture a bucket that fills up with “tokens” at a constant rate. Each request withdraws one token from this bucket, and when the bucket is empty the next request will be blocked. This _token bucket_ approach has some useful properties.

1.  The capacity of the bucket is the maximum number of requests that a burst can support (not counting tokens that are replenished mid-burst).
2.  The refill interval represents the long-term average allowed request interval.

Having distinct burst and average capacities without the need for multiple rate limiters is one of the main benefits to this algorithm.

*   Pros
    
    *   Allows bursts of high traffic, but enforces a long-term average rate of requests
    *   More flexible for users, allowing for traffic spikes within an acceptable range
*   Cons
    
    *   More difficult to convey limits and refill times to users than with fixed windows
*   Real-world examples
    
    *   Stripe [uses a token bucket](https://stripe.com/blog/rate-limiters) in which each user gets a bucket with `limit = 500`, `refillInterval = 0.01s`, allowing for sustained activity of 100 requests per second, but bursts of up to 500 requests. ([Implementation details](https://gist.github.com/ptarjan/e38f45f2dfe601419ca3af937fff574d).)
    *   OpenAI’s free tier for GPT-3.5 is limited to 200 [requests per day](https://platform.openai.com/docs/guides/rate-limits) using a token bucket with `limit = 200` and `refillInterval = 86400s / 200`, replenishing the bucket such that at the end of a day (86,400 seconds) an empty bucket will be 100% filled. They refill the bucket one token at a time.
    
    The Twitch chat demo above is rate-limited using a token bucket with a bucket size of 3, allowing bursts of up to 3 requests, and a refill interval of 4 seconds, which creates a long-term average allowed rate of 1 message every 4 seconds.
    
    Thanks to their flexibility, token buckets can also mimic the properties of some of the other algorithms. For example, set the `refillRate` equal to the `limit` and you have an equivalent to a fixed window rate limiter with a user-defined start.
    

Other considerations
--------------------

If you decide to add rate limiting to your application or endpoint, in addition to selecting an appropriate algorithm there are a few other things you should keep in mind.

*   **Create a persisted store for the rate limiter.** If you ever intend to horizontally scale your server (or even just restart it, or use serverless) your rate limiter data store can’t be in-memory. A popular option is to save rate limiting data to a key-value store like Redis, which has built-in functions for expiring keys, on a separate machine from your application. You can, however, use an ephemeral in-memory cache to block requests without hitting Redis while the limiter is hot.
*   **Fail open.** If your server’s connection to the persisted store fails, make sure to allow all requests rather than blocking access to your service altogether.
*   **Optionally throttle bursts.** Throttling can be used in combination with rate limiting to reduce the impact of burst traffic.
*   **Choose sensible keys.** In general, rate limiting is done on a per-user level. For most apps, this means keying on the user ID. For APIs, key on an API key. To rate limit unauthenticated users, the options aren’t great, but popular methods include using the request’s IP address, a device fingerprint, a unique installation ID, or just a shared limiter.
*   **Surface useful rate limiting errors.** Let users know how long they have to wait for their next request. For APIs, use the 429 HTTP status code when a request is blocked and include the relevant `x-ratelimit-*` response headers. [GitHub](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#checking-the-status-of-your-rate-limit) has good examples of the headers for their fixed-window limiter and [OpenAI](https://platform.openai.com/docs/guides/rate-limits/rate-limits-in-headers) has some for their token-bucket limiter.

Wrapping up
-----------

*   If you need a simple rate limiter or predictable window start times, use a [fixed window](https://smudge.ai/blog/ratelimit-algorithms#fixed-windows).
*   If you need traffic smoothing for a high volume of requests, consider using an [approximated sliding window](https://smudge.ai/blog/ratelimit-algorithms#sliding-windows).
*   If you need to support bursts of traffic while enforcing a lower average long-term rate for requests, use a [token bucket](https://smudge.ai/blog/ratelimit-algorithms#token-buckets).

* * *

Playground
----------

* * *

_This post was inspired by the amazing load balancing visualizations at [samwho.dev](https://samwho.dev/load-balancing/). Also, a huge thank you to [@onsclom](https://github.com/onsclom) for pairing with me on the canvas visualizations. Lastly, shoutout to Upstash for their [docs](https://upstash.com/docs/oss/sdks/ts/ratelimit/costs) and implementation [scripts](https://github.com/upstash/ratelimit/blob/main/src/lua-scripts/single.ts), which served as an excellent reference for each algorithm._

_There’s a discussion about this post on [Hacker News](https://news.ycombinator.com/item?id=40384421) as well._

_Feel free to send corrections, ideas, and feedback my way at [feedback@smudge.ai](mailto:feedback@smudge.ai)!_

* * *

> This post is the second in a [series](https://smudge.ai/blog) where I document some of the things I’ve learned while building smudge.ai. If you’re new here, [smudge.ai](https://smudge.ai/) is a Chrome extension that lets you save custom ChatGPT commands into your right-click menu. It’s a (mostly) solo project and an extension I rely on almost every day. If you think it could be a useful tool for you, too, then you can always try smudge.ai for free with no account using the rate-limited free tier, which happens to have been implemented as a fixed window with a user-defined start. Cheers!
