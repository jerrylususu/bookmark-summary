Title: Everything I know about good system design

URL Source: https://www.seangoedecke.com/good-system-design/

Markdown Content:
I see a lot of bad system design advice. One classic is the LinkedIn-optimized “bet you never heard of _queues_” style of post, presumably aimed at people who are new to the industry. Another is the Twitter-optimized “you’re a terrible engineer if you ever store booleans in a database” clever trick[1](https://www.seangoedecke.com/good-system-design/#fn-1). Even good system design advice can be kind of bad. I love _Designing Data-Intensive Applications_, but I don’t think it’s particularly useful for most system design problems engineers will run into.

What is system design? In my view, if software design is how you assemble lines of code, system design is how you assemble _services_. The primitives of software design are variables, functions, classes, and so on. The primitives of system design are app servers, databases, caches, queues, event buses, proxies, and so on.

This post is my attempt to write down, in broad strokes, everything I know about good system design. A lot of the concrete judgment calls do come down to experience, which I can’t convey in this post. But I’m trying to write down what I can.

### Recognizing good design

What does good system design look like? I’ve written before that it [looks underwhelming](https://www.seangoedecke.com/great-software-design). In practice, it looks like nothing going wrong for a long time. You can tell that you’re in the presence of good design if you have thoughts like “huh, this ended up being easier than I expected”, or “I never have to think about this part of the system, it’s fine”. Paradoxically, good design is self-effacing: bad design is often more impressive than good. I’m always suspicious of impressive-looking systems. If a system has distributed-consensus mechanisms, many different forms of event-driven communication, CQRS, and other clever tricks, I wonder if there’s some fundamental bad decision that’s being compensated for (or if the system is just straightforwardly over-designed).

I’m often alone on this. Engineers look at complex systems with many interesting parts and think “wow, a lot of system design is happening here!” In fact, a complex system usually reflects an absence of good design. I say “usually” because sometimes you do need complex systems. I’ve worked on many systems that earned their complexity. However, a complex system that works always evolves from a simple system that works. Beginning from scratch with a complex system is a really bad idea.

### State and statelessness

The hard part about software design is state. If you’re storing any kind of information for any amount of time, you have a lot of tricky decisions to make about how you save, store and serve it. If you’re not storing information[2](https://www.seangoedecke.com/good-system-design/#fn-2), your app is “stateless”. As a non-trivial example, GitHub has an internal API that takes a PDF file and returns a HTML rendering of it. That’s a real stateless service. Anything that writes to a database is stateful.

You should try and minimize the amount of stateful components in any system. (In a sense this is trivially true, because you should try to minimize the amount of _all_ components in a system, but stateful components are particularly dangerous.) The reason you should do this is that **stateful components can get into a bad state**. Our stateless PDF-rendering service will safely run forever, as long as you’re doing broadly sensible things: e.g. running it in a restartable container so that if anything goes wrong it can be automatically killed and restored to working order. A stateful service can’t be automatically repaired like this. If your database gets a bad entry in it (for instance, an entry with a format that triggers a crash in your application), you have to manually go in and fix it up. If your database runs out of room, you have to figure out some way to prune unneeded data or expand it.

What this means in practice is having one service that knows about the state - i.e. it talks to a database - and other services that do stateless things. Avoid having five different services all write to the same table. Instead, have four of them send API requests (or emit events) to the first service, and keep the writing logic in that one service. If you can, it’s worth doing this for the read logic as well, although I’m less absolutist about this. It’s _sometimes_ better for services to do a quick read of the `user_sessions` table than to make a 2x slower HTTP request to an internal sessions service.

### Databases

Since managing state is the most important part of system design, the most important component is usually where that state lives: the database. I’ve spent most of my time working with SQL databases (MySQL and PostgreSQL), so that’s what I’m going to talk about.

#### Schemas and indexes

If you need to store something in a database, the first thing to do is define a table with the schema you need. Schema design should be flexible, because once you have thousands or millions of records, it can be an enormous pain to change the schema. However, if you make it too flexible (e.g. by sticking everything in a “value” JSON column, or using “keys” and “values” tables to track arbitrary data) you load a ton of complexity into the application code (and likely buy some very awkward performance constraints). Drawing the line here is a judgment call and depends on specifics, but in general I aim to have my tables be human-readable: you should be able to go through the database schema and get a rough idea of what the application is storing and why.

If you expect your table to ever be more than a few rows, you should put indexes on it. Try to make your indexes match the most common queries you’re sending (e.g. if you query by `email` and `type`, create an index with those two fields). Don’t index on every single thing you can think of, since each index adds write overhead.

#### Bottlenecks

Accessing the database is often the bottleneck in high-traffic applications. This is true even when the compute side of things is relatively inefficient (e.g. Ruby on Rails running on a preforking server like Unicorn). That’s because complex applications need to make a _lot_ of database calls - hundreds and hundreds for every single request, often sequentially (because you don’t know if you need to check whether a user is part of an organization until after you’ve confirmed they’re not abusive, and so on). How can you avoid getting bottlenecked?

When querying the database, _query the database_. It’s almost always more efficient to get the database to do the work than to do it yourself. For instance, if you need data from multiple tables, `JOIN` them instead of making separate queries and stitching them together in-memory. Particularly if you’re using an ORM, beware accidentally making queries in an inner loop. That’s an easy way to turn a `select id, name from table` to a `select id from table` and a hundred `select name from table where id = ?`.

Every so often you do want to break queries apart. It doesn’t happen often, but I’ve run into queries that were ugly enough that it was easier on the database to split them up than to try to run them as a single query. I’m sure it’s always possible to construct indexes and hints such that the database can do it better, but the occasional tactical query-split is a tool worth having in your toolbox.

Send as many read queries as you can to database replicas. A typical database setup will have one write node and a bunch of read-replicas. The more you can avoid reading from the write node, the better - that write node is already busy enough doing all the writes. The exception is when you really, really can’t tolerate any replication lag (since read-replicas are always running at least a handful of ms behind the write node). But in most cases replication lag can be worked around with simple tricks: for instance, when you update a record but need to use it right after, you can fill in the updated details in-memory instead of immediately re-reading after a write.

Beware spikes of queries (particularly write queries, and _particularly_ transactions). Once a database gets overloaded, it gets slow, which makes it more overloaded. Transactions and writes are good at overloading databases, because they require a lot of database work for each query. If you’re designing a service that might generate massive query spikes (e.g. some kind of bulk-import API), consider throttling your queries.

### Slow operations, fast operations

A service has to do some things fast. If a user is interacting with something (say, an API or a web page), they should see a response within a few hundred ms[3](https://www.seangoedecke.com/good-system-design/#fn-3). But a service has to do other things that are slow. Some operations just take a long time (converting a very large PDF to HTML, for instance). The general pattern for this is splitting out **the minimum amount of work needed to do something useful for the user** and doing the rest of the work in the background. In the PDF-to-HTML example, you might render the first page to HTML immediately and queue up the rest in a background job.

What’s a background job? It’s worth answering this in detail, because “background jobs” are a core system design primitive. Every tech company will have some kind of system for running background jobs. There will be two main components: a collection of queues, e.g. in Redis, and a job runner service that will pick up items from the queues and execute them. You enqueue a background job by putting an item like `{job_name, params}` on the queue. It’s also possible to schedule background jobs to run at a set time (which is useful for periodic cleanups or summary rollups). Background jobs should be your first choice for slow operations, because they’re typically such a well-trodden path.

Sometimes you want to roll your own queue system. For instance, if you want to enqueue a job to run in a month, you probably shouldn’t put an item on the Redis queue. Redis persistence is typically not guaranteed over that period of time (and even if it is, you likely want to be able to query for those far-future enqueued jobs in a way that would be tricky with the Redis job queue). In this case, I typically create a database table for the pending operation with columns for each param plus a `scheduled_at` column. I then use a daily job to check for these items with `scheduled_at <= today`, and either delete them or mark them as complete once the job has finished.

### Caching

Sometimes an operation is slow because it needs to do an expensive (i.e. slow) task that’s the same between users. For instance, if you’re calculating how much to charge a user in a billing service, you might need to do an API call to look up the current prices. If you’re charging users per-use (like OpenAI does per-token), that could (a) be unacceptably slow and (b) cause a lot of traffic for whatever service is serving the prices. The classic solution here is **caching**: only looking up the prices every five minutes, and storing the value in the meantime. It’s easiest to cache in-memory, but using some fast external key-value store like Redis or Memcached is also popular (since it means you can share one cache across a bunch of app servers).

The typical pattern is that junior engineers learn about caching and want to cache _everything_, while senior engineers want to cache as little as possible. Why is that? It comes down to the first point I made about the danger of statefulness. A cache is a source of state. It can get weird data in it, or get out-of-sync with the actual truth, or cause mysterious bugs by serving stale data, and so on. You should never cache something without first making a serious effort to speed it up. For instance, it’s silly to cache an expensive SQL query that isn’t covered by a database index. You should just add the database index!

I use caching a lot. One useful caching trick to have in the toolbox is using a scheduled job and a document storage like S3 or Azure Blob Storage as a large-scale persistent cache. If you need to cache the result of a _really_ expensive operation (say, a weekly usage report for a large customer), you might not be able to fit the result in Redis or Memcached. Instead, stick a timestamped blob of the results in your document storage and serve the file directly from there. Like the database-backed long-term queue I mentioned above, this is an example of using the caching _idea_ without using a specific cache technology.

### Events

As well as some kind of caching infrastructure and background job system, tech companies will typically have an _event hub_. The most common implementation of this is Kafka. An event hub is just a queue - like the one for background jobs - but instead of putting “run this job with these params” on the queue, you put “this thing happened” on the queue. One classic example is firing off a “new account created” event for each new account, and then having multiple services consume that event and take some action: a “send a welcome email” service, a “scan for abuse” service, a “set up per-account infrastructure” service, and so on.

You shouldn’t overuse events. Much of the time it’s better to just have one service make an API request to another service: all the logs are in the same place, it’s easier to reason about, and you can immediately see what the other service responded with. Events are good for when the code sending the event doesn’t necessarily care what the consumers do with the event, or when the events are high-volume and not particularly time-sensitive (e.g. abuse scanning on each new Twitter post).

### Pushing and pulling

When you need data to flow from one place to a lot of other places, there are two options. The simplest is to _pull_. This is how most websites work: you have a server that owns some data, and when a user wants it they make a request (via their browser) to the server to pull that data down to them. The problem here is that users might do a lot of pulling down the same data - e.g. refreshing their email inbox to see if they have any new emails, which will pull down and reload the entire web application instead of just the data about the emails.

The alternative is to _push_. Instead of allowing users to ask for the data, you allow them to register as clients, and then when the data changes, the server pushes the data down to each client. This is how GMail works: you don’t have to refresh the page to get new emails, because they’ll just appear when they arrive.

If we’re talking about background services instead of users with web browsers, it’s easy to see why pushing can be a good idea. Even in a very large system, you might only have a hundred or so services that need the same data. For data that doesn’t change much, it’s much easier to make a hundred HTTP requests (or RPC, or whatever) whenever the data changes than to serve up the same data a thousand times a second.

Suppose you did need to serve up-to-date data to a million clients (like GMail, does). Should those clients be pushing or pulling? It depends. Either way, you won’t be able to run it all from a single server, so you’ll need to farm it out to other components of the system. If you’re pushing, that will likely mean sticking each push on an event queue and having a horde of event processors each pulling from the queue and sending out your pushes. If you’re pulling, that will mean standing up a bunch (say, a hundred) of fast[4](https://www.seangoedecke.com/good-system-design/#fn-4) read-replica cache servers that will sit in front of your main application and handle all the read traffic[5](https://www.seangoedecke.com/good-system-design/#fn-5).

### Hot paths

When you’re designing a system, there are lots of different ways users can interact with it or data can flow through it. It can get a bit overwhelming. The trick is to mainly focus on the “hot paths”: the part of the system that is most critically important, and the part of the system that is going to handle the most data. For instance, in a metered billing system, those pieces might be the part that decides whether or not a customer gets charged, and the part that needs to hook into all user actions on the platform to identify how much to charge.

Hot paths are important because they have fewer possible solutions than other design areas. There are a thousand ways you can build a billing settings page and they’ll all mainly work. But there might be only a handful of ways that you can sensibly consume the firehose of user actions. Hot paths also go wrong more spectacularly. You have to really screw up a settings page to take down the entire product, but any code you write that’s triggered on all user actions can easily cause huge problems.

### Logging and metrics

How do you know if you’ve got problems? One thing I’ve learned from my most paranoid colleagues is to log aggressively during unhappy paths. If you’re writing a function that checks a bunch of conditions to see if a user-facing endpoint should respond 422, you should log out the condition that was hit. If you’re writing billing code, you should log every decision made (e.g. “we’re not billing for this event because of X”). Many engineers don’t do this because it adds a bunch of logging boilerplate and makes it hard to write beautifully elegant code, but you should do it anyway. You’ll be happy you did when an important customer is complaining that they’re getting a 422 - even if that customer did something wrong, you still need to figure out _what they did wrong_ for them.

You should also have basic observability into the operational parts of the system. That means CPU/memory on the hosts or containers, queue sizes, average time per-request or per-job, and so on. For user-facing metrics like time per-request, you also need to watch the p95 and p99 (i.e. how slow your slowest requests are). Even one or two very slow requests are scary, because they’re disproportionately from your largest and most important users. If you’re just looking at averages, it’s easy to miss the fact that some users are finding your service unusable.

### Killswitches, retries, and failing gracefully

I wrote a [whole post](https://www.seangoedecke.com/killswitches) about killswitches that I won’t repeat here, but the gist is that you should think carefully about what happens when the system fails badly.

Retries are not a magic bullet. You need to make sure you’re not putting extra load on other services by blindly retrying failed requests. If you can, put high-volume API calls inside a “circuit breaker”: if you get too many 5xx responses in a row, stop sending requests for a while to let the service recover. You also need to make sure you’re not retrying write events that may or may not have succeeded (for instance, if you send a “bill this user” request and get back a 5xx, _you don’t know_ if the user has been billed or not). The classic solution to this is to use an “idempotency key”, which is a special UUID in the request that the other service uses to avoid re-running old requests: every time they do something, they save the idempotency key, and if they get another request with the same key, they silently ignore it.

It’s also important to decide what happens when part of your system fails. For instance, say you have some rate limiting code that checks a Redis bucket to see if a user has made too many requests in the current window. What happens when that Redis bucket is unavailable? You have two options: fail _open_ and let the request through, or fail _closed_ and block the request with a 429.

Whether you should fail open or closed depends on the specific feature. In my view, a rate limiting system should almost always fail open. That means that a problem with the rate limiting code isn’t necessarily a big user-facing incident. However, auth should (obviously) always fail closed: it’s better to deny a user access to their own data than to give a user access to some other user’s data. There are a lot of cases where it’s not clear what the right behavior is. It’s often a difficult tradeoff.

### Final thoughts

There are some topics I’m deliberately not covering here. For instance, whether or when to split your monolith out into different services, when to use containers or VMs, tracing, good API design. Partly this is because I don’t think it matters that much (in my experience, monoliths are fine), or because I think it’s too obvious to talk about (you should use tracing), or because I just don’t have the time (API design is complicated).

The main point I’m trying to make is what I said at the start of this post: good system design is not about clever tricks, it’s about knowing how to use boring, well-tested components in the right place. I’m not a plumber, but I imagine good plumbing is similar: if you’re doing something too exciting, you’re probably going to end up with crap all over yourself.

Especially at large tech companies, where these components already exist off the shelf (i.e. your company already has some kind of event bus, caching service, etc), good system design is going to look like nothing. There are very, very few areas where you want to do the kind of system design you could talk about at a conference. They do exist! I have seen hand-rolled data structures make features possible that wouldn’t have been possible otherwise. But I’ve only seen that happen once or twice in ten years. I see boring system design every single day.

* * *

1.   You’re supposed to store timestamps instead, and treat the presence of a timestamp as `true`. I do this sometimes but not always - in my view there’s some value in keeping a database schema immediately-readable.

[↩](https://www.seangoedecke.com/good-system-design/#fnref-1)
2.   Technically any service stores information of some kind for some duration, at least in-memory. Typically what’s meant here is storing information outside of the request-response lifecycle (e.g. persistently on-disk somewhere, such as in a database). If you can stand up a new version of the app by simply spinning up the application server, that’s a stateless app.

[↩](https://www.seangoedecke.com/good-system-design/#fnref-2)
3.   Gamedevs on Twitter will say that anything slower than 10ms is unacceptable. Whether that ought to be the case, it’s just factually not true about successful tech products - users will accept slower responses if the app is doing something that’s useful to them.

[↩](https://www.seangoedecke.com/good-system-design/#fnref-3)
4.   They’re fast because they don’t have to talk to a database in the way the main server does. In theory, this could just be a static file on-disk that they serve up when asked, or even data held in-memory.

[↩](https://www.seangoedecke.com/good-system-design/#fnref-4)
5.   Incidentally, those cache servers will either poll your main server (i.e. pulling) or your main server will send the new data to them (i.e. pushing). I don’t think it matters too much which you do. Pushing will give you more up-to-date data but pulling is simpler.

[↩](https://www.seangoedecke.com/good-system-design/#fnref-5)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

June 21, 2025│ Tags: [good engineers](https://www.seangoedecke.com/tags/good%20engineers/), [software design](https://www.seangoedecke.com/tags/software%20design/)

* * *
