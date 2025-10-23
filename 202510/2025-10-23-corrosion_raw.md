Title: Corrosion

URL Source: https://fly.io/blog/corrosion/

Published Time: Wed, 22 Oct 2025 23:15:36 GMT

Markdown Content:
![Image 1](https://fly.io/blog/corrosion/assets/sqlite-cover.webp)

Image by[Annie Ruygt](https://annieruygtillustration.com/)

Fly.io transmogrifies Docker containers into Fly Machines: micro-VMs running on our own hardware all over the world. The hardest part of running this platform isn’t managing the servers, and it isn’t operating the network; it’s gluing those two things together.

Several times a second, as customer CI/CD pipelines tear up or bring down [Fly Machines](https://fly.io/machines), our state synchronization system blasts updates across our internal mesh, so that edge proxies from Tokyo to Amsterdam can keep the accurate routing table that allows them to route requests for applications to the nearest customer instances.

On September 1, 2024, at 3:30PM EST, a new Fly Machine came up with a new “virtual service” configuration option a developer had just shipped. Within a few seconds every proxy in our fleet had locked up hard. It was the worst outage we’ve experienced: a period during which no end-user requests could reach our customer apps at all.

Distributed systems are blast amplifiers. By propagating data across a network, they also propagate bugs in the systems that depend on that data. In the case of Corrosion, our state distribution system, those bugs propagate **quickly**. The proxy code that handled that Corrosion update had succumbed to a [notorious Rust concurrency footgun](https://news.ycombinator.com/item?id=42093551): an `if let` expression over an `RWLock` assumed (reasonably, but incorrectly) in its `else` branch that the lock had been released. Instant and virulently contagious deadlock.

A lesson we’ve learned the hard way: never trust a distributed system without an interesting failure story. If a distributed system hasn’t ruined a weekend or kept you up overnight, you don’t understand it yet. Which is why that’s how we’re introducing Corrosion, an unconventional service discovery system we built for our platform [and open sourced](https://github.com/superfly/corrosion).

[](https://fly.io/blog/corrosion/#our-face-seeking-rake)Our Face-Seeking Rake
-----------------------------------------------------------------------------

State synchronization is the hardest problem in running a platform like ours. So why build a risky new distributed system for it? Because no matter what we try, that rake is waiting for our foot. The reason is our orchestration model.

Virtually every mainstream orchestration system (including Kubernetes) relies on a centralized database to make decisions about where to place new workloads. Individual servers keep track of what they’re running, but that central database is the source of truth. At Fly.io, in order to scale across dozens of regions globally, [we flip that notion on its head](https://fly.io/blog/carving-the-scheduler-out-of-our-orchestrator/): individual servers are the source of truth for their workloads.

In our platform, our central API bids out work to what is in effect a global market of competing “worker” physical servers. By moving the authoritative source of information from a central scheduler to individual servers, we scale out without bottlenecking on a database that demands both responsiveness and consistency between São Paulo, Virginia, and Sydney.

The bidding model is elegant, but it’s insufficient to route network requests. To allow an HTTP request in Tokyo to find the nearest instance in Sydney, we really do need some kind of global map of every app we host.

For longer than we should have, we relied on [HashiCorp Consul](https://github.com/hashicorp/consul) to route traffic. Consul is fantastic software. Don’t build a global routing system on it. Then we [built SQLite caches of Consul](https://fly.io/blog/a-foolish-consistency/). SQLite: also fantastic. But don’t do this either.

Like an unattended turkey deep frying on the patio, truly global distributed consensus promises deliciousness while yielding only immolation. [Consensus protocols like Raft](https://raft.github.io/)break down over long distances. And they work against the architecture of our platform: our Consul cluster, running on the biggest iron we could buy, wasted time guaranteeing consensus for updates that couldn’t conflict in the first place.

[](https://fly.io/blog/corrosion/#corrosion)Corrosion
-----------------------------------------------------

To build a global routing database, we moved away from distributed consensus and took cues from actual routing protocols.

[A protocol like OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) has the same operating model and many of the same constraints we do. OSPF is a “[link-state routing protocol](https://en.wikipedia.org/wiki/Link-state_routing_protocol)”, which, conveniently for us, means that routers are sources of truth for their own links and responsible for quickly communicating changes to every other router, so the network can make forwarding decisions.

We have things easier than OSPF does. Its flooding algorithm can’t assume connectivity between arbitrary routers (solving that problem is the point of OSPF). But we run a global, fully connected WireGuard mesh between our servers. All we need to do is gossip efficiently.

[Corrosion is a Rust program](https://github.com/superfly/corrosion) that propagates a SQLite database with a gossip protocol.

Like Consul, our gossip protocol is [built on SWIM](https://fly.io/blog/building-clusters-with-serf#what-serf-is-doing). Start with the simplest, dumbest group membership protocol you can imagine: every node spams every node it learns about with heartbeats. Now, just two tweaks: first, each step of the protocol, spam a random subset of nodes, not the whole set. Then, instead of freaking out when a heartbeat fails, mark it “suspect” and ask another random subset of neighbors to ping it for you. SWIM converges on global membership very quickly.

Once membership worked out, we run QUIC between nodes in the cluster to broadcast changes and reconcile state for new nodes.

Corrosion looks like a globally synchronized database. You can open it with SQLite and just read things out of its tables. What makes it interesting is what it doesn’t do: no locking, no central servers, and no distributed consensus. Instead, we exploit our orchestration model: workers own their own state, so updates from different workers almost never conflict.

We do impose some order. Every node in a Corrosion cluster will eventually receive the same set of updates, in some order. To ensure every instance arrives at the same “working set” picture, we use [cr-sqlite, the CRDT SQLite extension](https://github.com/vlcn-io/cr-sqlite).

cr-sqlite works by marking specified SQLite tables as CRDT-managed. For these table, changes to any column of a row are logged in a special `crsql_changes`table. Updates to tables are applied last-write-wins using logical timestamps (that is, causal ordering rather than wall-clock ordering). [You can read much more about how that works here](https://github.com/superfly/corrosion/blob/main/doc/crdts.md).

As rows are updated in Corrosion’s ordinary SQL tables, the resulting changes are collected from `crsql_changes`. They’re bundled into batched update packets and gossiped.

When things are going smoothly, Corrosion is easy to reason about. Many customers of Corrosion’s data don’t even need to know it exists, just where the database is. We don’t fret over “leader elections” or bite our nails watching metrics for update backlogs. And it’s fast as all get-out.

[](https://fly.io/blog/corrosion/#shit-happens)Shit Happens
-----------------------------------------------------------

This is a story about how we made one good set of engineering decisions and [never experienced any problems](https://how.complexsystems.fail/). [Please clap](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/).

We told you already about the worst problem Corrosion was involved with: efficiently gossiping a deadlock bug to every proxy in our fleet, shutting our whole network down. Really, Corrosion was just a bystander for that outage. But it perpetrated others.

Take a classic ops problem: the unexpectedly expensive DDL change. You wrote a simple migration, tested it, merged it to main, and went to bed, wrongly assuming the migration wouldn’t cause an outage when it ran in prod. Happens to the best of us.

Now spice it up. You made a trivial-seeming schema change to a CRDT table hooked up to a global gossip system. Now, when the deploy runs, thousands of high-powered servers around the world join a chorus of database reconciliation messages that melts down the entire cluster.

That happened to us last year when a team member added a nullable column to a Corrosion table. New nullable columns are kryptonite to large Corrosion tables: `cr-sqlite` needs to backfill values for every row in the table. It played out as if every Fly Machine on our platform had suddenly changed state simultaneously, just to fuck us.

Gnarlier war story: for a long time we ran both Corrosion and Consul, because two distributed systems means twice the resiliency. One morning, a Consul mTLS certificate expired. Every worker in our fleet severed its connection to Consul.

We should have been fine. We had Corrosion running. Except: under the hood, every worker in the fleet is doing a backoff loop trying to reestablish connectivity to Consul. Each of those attempts re-invokes a code path to update Fly Machine state. That code path incurs a Corrosion write.

By the time we’ve figured out what the hell is happening, we’re literally saturating our uplinks almost everywhere in our fleet. We apologize to our uplink providers.

It’s been a long time since anything like this has happened at Fly.io, but preventing the next one is basically all we think about anymore.

[](https://fly.io/blog/corrosion/#iteration)Iteration
-----------------------------------------------------

In retrospect, our Corrosion rollout repeated a mistake we made with Consul: we built a single global state domain. Nothing about Corrosion’s design required us to do this, and we’re unwinding that decision now. Hold that thought. We got some big payoffs from some smaller lifts.

First, and most importantly, we watchdogged everything. We showed you a contagious deadlock bug, lethal because our risk model was missing “these Tokio programs might deadlock”. Not anymore. Our [Tokio programs](https://tokio.rs/) all have built-in watchdogs; an event-loop stall will bounce the service and make a king-hell alerting racket. Watchdogs have cancelled multiple outages. Minimal code, easy win. Do this in your own systems.

Then, we extensively tested Corrosion itself. We’ve written about [a bug we found in the Rust `parking_lot` library](https://fly.io/blog/parking-lot-ffffffffffffffff/). We spent months looking for similar bugs [with Antithesis](https://antithesis.com/product/how_antithesis_works/). Again: do recommend. It retraced our steps on the `parking_lot` bug easily; the bug wouldn’t have been worth the blog post if we’d been using Antithesis at the time. [Multiverse debugging](https://antithesis.com/docs/multiverse_debugging/overview/) is killer for distributed systems.

No amount of testing will make us trust a distributed system. So we’ve made it simpler to rebuild Corrosion’s database from our workers. We keep checkpoint backups of the Corrosion database on object storage. That was smart of us. When shit truly went haywire last year, we had the option to reboot the cluster, which is ultimately what we did. That eats some time (the database is large and propagating is expensive), but diagnosing and repairing distributed systems mishaps takes even longer.

We’ve also improved the way our workers feed Corrosion. Until recently, any time a worker updated its local database, we published the same incremental update to Corrosion. [But now we’ve eliminated partial updates.](https://community.fly.io/t/self-healing-machine-state-synchronization-and-service-discovery/26134) Instead, when a Fly Machine changes, we re-publish the entire data set for the Machine. Because of how Corrosion resolves changes to its own rows, the node receiving the re-published Fly Machine automatically filters out the no-op changes before gossiping them. Eliminating partial updates forecloses a bunch of bugs (and, we think, kills off a couple sneaky ones we’ve been chasing). We should have done it this way to begin with.

Finally, let’s revisit that global state problem. After the contagious deadlock bug, we concluded we need to evolve past a single cluster. So we took on a project we call “regionalization”, which creates a two-level database scheme. Each region we operate in runs a Corrosion cluster with fine-grained data about every Fly Machine in the region. The global cluster then maps applications to regions, which is sufficient to make forwarding decisions at our edge proxies.

Regionalization reduces the blast radius of state bugs. Most things we track don’t have to matter outside their region (importantly, most of the code changes to what we track are also region-local). We can roll out changes to this kind of code in ways that, worst case, threaten only a single region.

[](https://fly.io/blog/corrosion/#the-new-system-works)The New System Works
---------------------------------------------------------------------------

Most distributed systems have state synchronization challenges. Corrosion has a different “shape” than most of those systems:

*   It doesn’t rely on distributed consensus, like [Consul](https://github.com/hashicorp/consul), [Zookeeper](https://zookeeper.apache.org/), [Etcd](https://etcd.io/), [Raft](https://www.cockroachlabs.com/docs/stable/architecture/replication-layer), or [rqlite](https://rqlite.io/) (which we came very close to using). 
*   It doesn’t rely on a large-scale centralized data store, like [FoundationDB](https://www.foundationdb.org/) or databases backed by S3-style object storage. 
*   It’s nevertheless highly distributed (each of thousands of workers run nodes), converges quickly (in seconds), and presents as a simple SQLite database. Neat! 

It wasn’t easy getting here. Corrosion is a large part of what every engineer at Fly.io who writes Rust works on.

Part of what’s making Corrosion work is that we’re careful about what we put into it. Not every piece of state we manage needs gossip propagation. `tkdb`, the backend for [our Macaroon tokens](https://fly.io/blog/macaroons-escalated-quickly/), is a much simpler SQLite service backed by [Litestream](https://litestream.io/). So is Pet Sematary, the secret store we built to replace HashiCorp Vault.

Still, there are probably lots of distributed state problems that want something more like a link-state routing protocol and less like a distributed database. If you think you might have one of those, [feel free to take Corrosion for a spin](https://github.com/superfly/corrosion).

Corrosion is Jérôme Gravel-Niquet’s brainchild. For the last couple years, much of the iteration on it was led by Somtochi Onyekwere and Peter Cai. The work was alternately cortisol- and endorphin-inducing. We’re glad to finally get to talk about it in detail.