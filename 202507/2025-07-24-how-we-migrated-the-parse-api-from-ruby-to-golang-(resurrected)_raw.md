Title: How We Migrated the Parse API From Ruby to Golang (Resurrected)

URL Source: https://charity.wtf/2025/07/24/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected/

Published Time: 2025-07-24T02:14:45+00:00

Markdown Content:
I wrote a lot of blog posts over my time at Parse, but they all evaporated after [Facebook killed the product](https://charity.wtf/2016/02/03/how-to-survive-an-acquisition/). Most of them I didn’t care about (there were, ahem, a lot of “service reliability updates”), but I was mad about losing one specific piece, a deceptively casual retrospective of the grueling, murderous two-year rewrite of our entire API from Ruby on Rails to Golang..

I could have sworn I’d looked for it before, but someone asked me a question about migrations this morning, which spurred me to pull up the Wayback Machine again and dig in harder, and … ✨I FOUND IT!!✨

Honestly, it is entirely possible that if we had not done this rewrite, there might be no Honeycomb. In the early days of the rewrite, we would ship something in Go and the world would break, over and over and over. As I said,

> Rails HTTP processing is built on a philosophy of “be liberal in what you accept”. So developers end up inadvertently sending API requests that are undocumented or even non-RFC compliant … but Rails middleware cleans them up and handles it fine.

Rails would accept any old trash, Go would not. Breakage ensues. Tests couldn’t catch what we didn’t know to look for. Eventually we lit upon a workflow where we would split incoming production traffic, run each request against a Go API server and a Ruby API server, each backed by its own set of MongoDB replicas, and diff the responses. This is when we first got turned on to how incredibly powerful Scuba was, in its ability to compare individual responses, field by field, line by line.

Once you’ve used a tool like that, you’re hooked.. you can’t possibly go back to metrics and aggregates. The rest, as they say, is history.

The whole thing is still pretty fun to read, even if I can still smell the blood and viscera a decade later. Enjoy.

* * *

“How We Moved Our API From Ruby to Go and Saved Our Sanity”
-----------------------------------------------------------

_Originally posted on blog.parse.com on June 10th, 2015._

The first lines of Parse code were written nearly four years ago. In 2011 Parse was a crazy little idea to solve the problem of building mobile apps.

Those first few lines were written in Ruby on Rails.

* * *

Ruby on Rails
-------------

Ruby let us get the first versions of Parse out the door quickly. It let a small team of engineers iterate on it and add functionality very fast. There was a deep bench of library support, gems, deploy tooling, and best practices available, so we didn’t have to reinvent very many wheels.

We used Unicorn as our HTTP server, Capistrano to deploy code, RVM to manage the environment, and a zillion open source gems to handle things like YAML parsing, oauth, JSON parsing, MongoDB, and MySQL. We also used Chef which is Ruby-based to manage our infrastructure so everything played together nicely. For a while.

The first signs of trouble bubbled up in the deploy process. As our code base grew, it took longer and longer to deploy, and the “graceful” unicorn restarts really weren’t very graceful. So, we monkeypatched rolling deploy groups in to Capistrano.

“Monkeypatch” quickly became a key technical term that we learned to associate with our Ruby codebase.

A year and a half in, at the end of 2012, we had 200 API servers running on[m1.xlarge](https://web.archive.org/web/20150611004347/http://ec2instances.info/)instance types with 24 unicorn workers per instance. This was to serve 3000 requests per second for 60,000 mobile apps. It took 20 minutes to do a full deploy or rollback, and we had to do a bunch of complicated load balancer shuffling and pre-warming to prevent the API from being impacted during a deploy.

Then, Parse really started to take off and experience hockey-stick growth.

* * *

Problems
--------

When our API traffic and number of apps started growing faster, we started having to rapidly spin up more database machines to handle the new request traffic. That is when the “one process per request” part of the Rails model started to fall apart.

With a typical Ruby on Rails setup, you have a fixed pool of worker processes, and each worker can handle only one request at a time. So any time you have a type of request that is particularly slow, your worker pool can rapidly fill up with that type of request. This happens too fast for things like auto-scaling groups to react. It’s also wasteful because the vast majority of these workers are just waiting on another service. In the beginning, this happened pretty rarely and we could manage the problem by paging a human and doing whatever was necessary to keep the API up. But as we started growing faster and adding more databases and workers, we added more points of failure and more ways for performance to get degraded.

We started looking ahead to when Parse would 10x its size, and realized that the one-process-per-request model just wouldn’t scale. We had to move to an async model that was fundamentally different from the Rails way. Yeah, rewrites are hard, and yeah they always take longer than anyone ever anticipates, but we just didn’t see how we could make the Rails codebase scale while it was tied to one process per request.

* * *

What next?
----------

We knew we needed asynchronous operations. We considered a bunch of options:

### EventMachine

We already had some of our push notification service using EventMachine, but our experience was not great as it too was scaling. We had constant trouble with accidentally introducing synchronous behavior or parallelism bugs. The vast majority of Ruby gems are not asynchronous, and many are not threadsafe, so it was often hard to find a library that did some common task asynchronously.

### JRuby

This might seem like the obvious solution – after all, Java has threads and can handle massive concurrency. Plus it’s Ruby already, right?[This is the solution Twitter investigated before settling on Scala](https://web.archive.org/web/20150611004347/http://www.infoq.com/articles/twitter-java-use). But since JRuby is still basically Ruby, it still has the problem of asynchronous library support. We were concerned about needing a second rewrite later, from JRuby to Java. And literally nobody at all on our backend or ops teams wanted to deal with deploying and tuning the JVM. The groans were audible from outer space.

### C++

We had a lot of experienced C++ developers on our team. We also already had some C++ in our stack, in our Cloud Code servers that ran embedded V8. However, C++ didn’t seem like a great choice. Our C++ code was harder to debug and maintain. It seemed clear that C++ development was generally less productive than more modern alternatives. It was missing a lot of library support for things we knew were important to us, like HTTP request handling. Asynchronous operation was possible but often awkward. And nobody really _wanted_ to write a lot of C++ code.

### C#

C# was a strong contender. It arguably had the best concurrency model with Async and Await. The real problem was that C# development on Linux always felt like a second-class citizen. Libraries that interoperate with common open source tools are often unavailable on C#, and our toolchain would have to change a lot.

### Go

Go and C# both have asynchronous operation built into the language at a low level, making it easy for large groups of people to write asynchronous code. The MongoDB Go driver is probably the best MongoDB driver in existence, and complex interaction with MongoDB is core to Parse. Goroutines were much more lightweight than threads. And frankly we were most excited about writing Go code. We thought it would be a lot easier to recruit great engineers to write Go code than any of the other solid async languages.

In the end, the choice boiled down to C# vs Go, and we chose Go.

* * *

Wherein we rewrite the world
----------------------------

We started out rewriting our EventMachine push backend from Ruby to Go. We did some preliminary benchmarking with Go concurrency and found that each network connection ate up only 4kb of RAM. After rewriting the EventMachine push backend to Go we went from 250k connections per node to 1.5 million connections per node without even touching things like kernel tuning. Plus it seemed really fun. So, Go it was.

We rewrote some other minor services and starting building new services in Go. The main challenge, though, was to rewrite the core API server that handles requests to[api.parse.com](https://web.archive.org/web/20150611004347/http://api.parse.com/)while seamlessly maintaining backward compatibility. We rewrote this endpoint by endpoint, using a live shadowing system to avoid impacting production, and monitored the differential metrics to make sure the behaviors matched.

During this time, Parse 10x’d the number of apps on our backend and more than 10x’d our request traffic. We also 10x’d the number of storage systems backed by Ruby. We were chasing a rapidly moving target.

The hardest part of the rewrite was dealing with all the undocumented behaviors and magical mystery bits that you get with Rails middleware. Parse exposes a REST API, and Rails HTTP processing is built on a philosophy of “be liberal in what you accept”. So developers end up inadvertently sending API requests that are undocumented or even non-RFC compliant … but Rails middleware cleans them up and handles it fine.

So we had to port a lot of delightful behavior from the Ruby API to the Go API, to make sure we kept handling the weird requests that Rails handled. Stuff like doubly encoded URLs, weird content-length requirements, bodies in HTTP requests that shouldn’t have bodies, horrible oauth misuse, horrible mis-encoded Unicode.

Our Go code is now peppered with fun, cranky comments like these:

```
// Note: an unset cache version is treated by ruby as “”.
// Because of this, dirtying this isn’t as simple as deleting it – we need to
// actually set a new value.

// This byte sequence is what ruby expects.
// yes that’s a paren after the second 180, per ruby.

// Inserting and having an op is kinda weird: We already know
// state zero. But ruby supports it, so go does too.

// single geo query, don’t do anything. stupid and does not make sense
// but ruby does it. Changing this will break a lot of client tests.
// just be nice and fix it here.

// Ruby sets various defaults directly in the structure and expects them to appear in cache.
// For consistency, we’ll do the same thing.
```

### Results

Was the rewrite worth it? Hell yes it was.**Our reliability improved by an order of magnitude**. More importantly, our API is not getting more and more fragile as we spin up more databases and backing services. Our codebase got cleaned up and we got rid of a ton of magical gems and implicit assumptions. Co-tenancy issues improved for customers across the board. Our ops team stopped getting massively burned out from getting paged and trying to track down and manually remediate Ruby API outages multiple times a week. And needless to say, our customers were happier too.

We now almost never have reliability-impacting events that can be tracked back to the API layer – a massive shift from a year ago. Now when we have timeouts or errors, it’s usually constrained to a single app – because one app is issuing a very inefficient query that causes timeouts or full table scans for their app, or it’s a database-related co-tenancy problem that we can resolve by automatically rebalancing or filtering bad actors.

An asynchronous model had many other benefits. We were also able to instrument everything the API was doing with counters and metrics, because these were no longer blocking operations that interfered with communicating to other services. We could downsize our provisioned API server pool by about 90%. And we were also able to remove silos of isolated Rails API servers from our stack, drastically simplifying our architecture.

As if that weren’t enough, the time it takes to run our full integration test suite dropped from 25 minutes to 2 minutes, and the time to do a full API server deploy with rolling restarts dropped from 30 minutes to 3 minutes. The go API server[restarts gracefully](https://web.archive.org/web/20150611004347/https://github.com/facebookgo/grace)so no load balancer juggling and prewarming is necessary.

We love Go. We’ve found it really fast to deploy, really easy to instrument, really lightweight and inexpensive in terms of resources. It’s taken a while to get here, but the journey was more than worth it.

### Credits/Blames

Credits/Blames go to Shyam Jayaraman for driving the initial decision to use Go, Ittai Golde for shepherding the bulk of the API server rewrite from start to finish, Naitik Shah for writing and open sourcing a ton of[libraries and infrastructure](https://web.archive.org/web/20150611004347/https://github.com/facebookgo)underpinning our Go code base, and the rest of the amazing Parse backend SWE team who performed the rewrite.

![Image 1](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/07/Screenshot-2025-07-23-at-18.46.47.png?resize=300%2C161&ssl=1)
