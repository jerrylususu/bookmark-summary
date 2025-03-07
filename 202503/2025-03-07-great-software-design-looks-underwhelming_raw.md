Title: Great software design looks underwhelming

URL Source: https://www.seangoedecke.com/great-software-design/

Markdown Content:
Years ago I spent a lot of time reviewing coding challenges. The challenge itself was very straightforward - building a CLI tool that hit an API and allowed the user to page through and inspect the data. We allowed any language, so I saw all kinds of approaches[1](https://www.seangoedecke.com/great-software-design/#fn-1). At one point I came across a challenge I thought was literally perfect. It was a single Python file (maybe thirty lines of code in total), written in a very workmanlike style: the simplest, most straightforward way to meet the challenge requirements.

When I sent it to another reviewer, suggesting that we use this as a reference point for what a 10/10 looked like, I was genuinely shocked to hear from them that they wouldn’t have passed that challenge through to an interview. According to them, it didn’t demonstrate enough understanding of sophisticated language features. It was _too_ simple.

Years later, I’m even more convinced that I was right and that reviewer was wrong. **Great software design is supposed to be too simple.** I think now I can finally begin to articulate why.

### Eliminating risk

Every software system has a lot of things that can go wrong. Sometimes these are called “failure modes” of the system. Here’s a sample:

*   SSL certificates expire and aren’t renewed
*   Database fills up and becomes too slow or out of memory
*   User data gets overwritten or corrupted
*   Users see a broken UI experience
*   Core user flows (e.g. saving records) fail to work

There are two ways of designing around a potential failure mode. The first is to be reactive: adding rescue clauses around risky blocks of code, making sure failed API requests are retried, setting up graceful degradation so errors don’t blow up the whole experience, adding logging and metrics so bugs can be easily identified, and so on. This is worth doing. In fact, I believe this kind of (frankly paranoid) attitude is the mark of an experienced software engineer. But working like this is not a mark of good design. It’s often a signal that you’re papering over flaws in a bad design.

The second way to handle potential failure modes is to **design them out of existence**. What does that mean in practice?

### Protecting the hot paths

Sometimes it means **moving components out of the hot path**. I once worked on a catalog endpoint that (due to other design choices) was extremely inefficient, in the order of ~200ms per record. This exposed us to a few nasty failure modes: resource starvation for the rest of the app, proxy timeouts on index requests, and users just giving up after waiting ten seconds for a response. We ended up moving the endpoint construction code into a cron job, sticking the results in blob storage, and having the catalog endpoint serve the blob. We still had the nasty 200ms-per-record code, but it was now under our control: it couldn’t be triggered by user actions, and if it failed the worst-case scenario is we’d just serve a stale blob.

### Removing components

Sometimes it means **using fewer components altogether**. Another service I worked on was a documentation CRM that had a really bespoke system for pulling various bits of docs out of different repositories and stitching them together into database entries (sometimes pulling docs directly out of code comments). This was originally a good decision - at the time, it was hard to get teams to write any kind of docs at all, so the system had to be maximally flexible. But as the company grew, it was very much showing its age. The sync job stored some state in the database and some state on disk, and often triggered strange git errors when the state on disk got out of sync or the underlying host ran out of memory. We ended up removing the database entirely, shifting all the docs into a central repository, and reworking the documentation page as a normal static site[2](https://www.seangoedecke.com/great-software-design/#fn-2). All kinds of possible runtime and operational bugs were removed, just like that.

### Centralizing state

Sometimes it means **normalizing your state**. One of the worst kinds of failure mode are bugs that leave your state (e.g. your database rows) in an inconsistent or corrupted state: one table says one thing, but another table says differently. This is bad because fixing the bug is only the start of the work. You have to go in and repair all the damaged records, which can involve some detective work to figure out what the right value ought to be (or in the worst case, guessing). Designing so that the crucial parts of your state have a single source of truth is often worth taking on a lot of other pain.

### Using robust systems

Sometimes it means **relying on battle-tested systems**. My favourite example for this is the Ruby webserver Unicorn. It’s the most straightforward, unsophisticated way you could possibly build a webserver on top of Linux. First, you take a server process that listens on a socket and handles one request at a time. Handling one request at a time won’t scale: incoming requests will queue up on the socket faster than the server can clear them. So what do you do? You fork that server process a bunch. Because of the way fork works, each child process is already listening on the original socket, so standard Linux socket logic handles spreading requests evenly between your server processes. If anything goes wrong, you can kill the child process and instantly fork off another one.

Some people think it’s a bit silly to like Unicorn so much because it’s obviously less scalable than a threaded server. But I love it for two reasons. First, because it hands off so much work to the process and socket Linux primitives. That’s smart because they’re ultra-reliable. Second, because it’s really, really hard for a Unicorn worker to do anything nasty to another Unicorn worker. Process isolation is a lot more reliable than thread isolation. That’s why Unicorn is the chosen webserver for most big Rails companies: Shopify, GitHub, Zendesk, and so on. Great software design doesn’t mean that your software is ultra-performant. It means that it’s a good fit for the task[3](https://www.seangoedecke.com/great-software-design/#fn-3).

### Summary

**Great software design looks simple because it eliminates as many failure modes as possible during the design stage.** The best way to eliminate a failure mode is to _not_ do something exciting (or if you can, not do anything at all).

Not all failure modes are created equal. You want to try hardest to eliminate the really scary ones (like data inconsistency), even if it means making slightly clunky choices elsewhere.

These are all relatively boring, unsexy ideas. But great software design is boring and unsexy. It’s easy to get excited about big ideas like CQRS or microservices or service meshes. Great software design doesn’t look like big exciting ideas. Most of the time it doesn’t look like anything at all.

March 7, 2025

* * *
