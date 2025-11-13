Title: Scaling HNSWs - <antirez>

URL Source: https://antirez.com/news/156

Markdown Content:
[antirez](https://antirez.com/user/antirez) 2 days ago. 71676 views. I’m taking a few weeks of pause on my HNSWs developments (now working on some other data structure, news soon). At this point, the new type I added to Redis is stable and complete enough, it’s the perfect moment to reason about what I learned about HNSWs, and turn it into a blog post. That kind of brain dump that was so common pre-AI era, and now has become, maybe, a bit more rare. Well, after almost one year of thinking and implementing HNSWs and vector similarity stuff, it is time for some writing. However this is not going to be an intro on HNSWs: too many are present already. This is the “extra mile” instead. If you know HNSWs, I want to share with you my more “advanced” findings, especially in the context of making them fast enough to allow for a “Redis” experience: you know, Redis is designed for low latency and high performance, and HNSWs are kinda resistant to that, so there were challenges to expose HNSWs as an abstract data structure.

This blog post will be split into several sections. Think of them as pages of the same book, different chapters of the same experience. Oh and, by the way, I already wrote and subsequently lost this blog post :D [long, sad story about MacOS and bad habits – I hadn’t lost something like that since the 90s, during blackouts], so here most of the problem will be to recall what I wrote a few days ago and, while I’m at it, to better rephrase what I didn’t like very much.

## A few words about the state of HNSW

Before digging into the HNSWs internals and optimizations, I want to say a few things about HNSWs. The original paper introducing HNSWs is a great piece of computer science literature, and HNSWs are amazing data structures, but: I don’t believe they are the last word for searching, in a greedy way, for nearby vectors according to a distance function. The paper gives the feeling it lacks some “pieces”, almost like if the researchers, given six months more, had a lot more to explore and say. For instance, I modified the paper myself, extending it in order to support removal of entries, actual removals, not just tombstone deletions where the element is marked as gone and collected later: deleting items is totally missing from the paper. Similarly, there are, right now, efforts in order to really check if the “H” in the HNSWs is really needed, and if instead a flat data structure with just one layer would perform more or less the same (I hope I’ll cover more about this in the future: my feeling is that the truth is in the middle, and that it makes sense to modify the level selection function to just have levels greater than a given threshold).

All this to say that, if you are into data structures research, I believe that a great area is to imagine evolutions and refinements of HNSWs, without getting trapped within the idea that the evolutions are only in the sense of: let’s do it, but for disk (see Microsoft efforts), or the like. Ok, enough with the premise, let’s go to the actual low level stuff :)

## Scaling memory

Redis is an in-memory system, and both HNSWs and vectors have the unfortunate quality of being very space-hungry. There are three reasons for this: 1. HNSWs have a lot of pointers, like 16, 32 or more pointers (this is a tunable parameter of HNSWs) to neighbor nodes. 2. HNSWs have many levels, being a skiplist-alike data structure. This exacerbates the first problem. 3. HNSW’s satellite data is a vector of floating point numbers, so, in the vanilla case, 4 bytes per component, and normally you can have 300-3000 components, this is the usual range.

So, what are the lessons learned here? There are folks that compress pointers, since it is very likely that many pointers (8 bytes in 64 bit systems) will have the highest four bytes all the same. This is smart, I didn’t implement it yet, because in Redis I need to go fast, and this is a tradeoff between space and time: but maybe it is worth it, maybe not. I’ll dig more. 

However, if you do the math, the fact that there are many layers is not *so* terrible as it looks. On average, the multiple layers per node make the situation worse by just ~1.3x (if the probability of level increase is 0.25 in the level selection function), since many nodes will be just at layer 0. But still 1.3 is more than 1, and if that “H” in HNSWs really is not *so* useful… [Spoiler, what I found is that the seek time if you have everything at layer 0 is greater, the main loop for the greedy search will start from less optimal places and it will eventually reach the right cluster, but will take more computation time. However this is just early results.]

So here the *real* low hanging fruit is: vector quantization. What I found is that if you use 8 bit quantization what you get is an almost 4x speedup, a 4x reduction of your vectors (but not a 4x reduction of the whole node: the pointers are still there, and they take a lot of space), and a recall that is virtually the same in real world use cases. This is the reason why Redis Vector Sets use 8 bit quantization by default. You can specify, via VADD options, that you want full precision vectors or binary quantized vectors, where we just take the sign, but I’m skeptical about using both full size vectors and binary quantized vectors. Before talking about them, let’s see what kind of quantization I used for 8 bit.

What I do is to compute the maximum absolute value of the component of each vector (so quantization is per-vector), then I use signed 8 bit values to represent the quant from -127 to 127. This is not as good as storing both min and max value, but it is faster when computing cosine similarity, since I can do this:

    /* Each vector is quantized from [-max_abs, +max_abs] to [-127, 127]
     * where range = 2*max_abs. */
    const float scale_product = (range_a/127) * (range_b/127);

Then I multiply things together in the integer domain with (actually in the code the main loop is unrolled and uses multiple accumulators, to make modern CPUs more busy)

    for (; i < dim; i++) dot0 += ((int32_t)x[i]) * ((int32_t)y[i]);

And finally we can return back to the floating point distance with:

    float dotf = dot0 * scale_product;

Check the vectors_distance_q8() for more information, but I believe you got the idea: it is very simple to go from the integer quants domain to the unquantized dotproduct with trivial operations.

So, 8 bit quantization is a great deal, and full precision was a *needed* feature, because there will be people doing things with vectors generated in a way where each small amount makes a difference (no, with learned vectors this is not the case…) but, why binary quantization? Because I wanted users to have a simple way to not waste space when their *original* information is already binary. Imagine you have a set of users and they have yes/no properties, and you want to find similar users, items, whatever. Well: this is where binary quantization should be used, it’s just, again, an option of the VADD command.

## Scaling speed: threading and locality

Oh, you know, I have to tell you something about myself: I’m not a fan of threaded systems when it is possible to do a lot with a single core, and then use multiple cores in a shared-nothing architecture. But HNSWs are different. They are *slow*, and they are accessed almost always in read-only ways, at least in most use cases. For this reason, my Vector Sets implementation is fully threaded. Not just reads, even writes are partially threaded, and you may wonder how this is possible without it resulting in a mess, especially in a system like Redis, where keys can be accessed in different ways by the background saving process, the clients, and so forth.

Well, to start, let’s focus on reads. What happens is that as long as nobody is writing in the data structure, we can spawn threads that do the greedy collection of near vectors and return back the results to the blocked client. However, my implementation of HNSWs was written from scratch, I mean, from the empty C file opened with vim, it has 0% of shared code with the two implementations most other systems use, so there are a few “novelties”. One of such different things is that in order to avoid re-visiting already visited nodes, I use an integer stored in each node that is called “epoch”, instead of using another data structure to mark (like, in a hash table) nodes already visited. This is quite slow, I believe. The epoch instead is local to the node, and the global data structure increments the epoch for each search. So in the context of each search, we are sure that we can find epochs that are just <= the current epoch, and the current epoch can be used to mark visited nodes.

But with threads, there are multiple searches occurring at the same time! And, yep, what I needed was an array of epochs:

typedef struct hnswNode {
    uint32_t level;         /* Node's maximum level */
    … many other stuff …
    uint64_t visited_epoch[HNSW_MAX_THREADS];
}

That’s what you can read in hnsw.h. This is, again, a space-time tradeoff, and again time won against space.

So, how was it possible to have threaded writes? The trick is that in HNSW inserts, a lot of time is spent looking for neighbors candidates. So writes are split into a reading-half and commit-half, only the second needs a write lock, and there are a few tricks to make sure that the candidates we accumulated during the first part are discarded if the HNSW changed in the meantime, and some nodes may no longer be valid. There is, however, another problem. What about the user deleting the key, while background threads are working on the value? For this scenario, we have a function that waits for background operations to return before actually reclaiming the object. With these tricks, it is easy to get 50k ops/sec on real world vector workloads, and these are numbers I got from redis-benchmark itself, with all the overhead involved. The raw numbers of the flat HNSW library itself are much higher.

## Scaling memory: reclaiming it properly

Before talking about how to scale HNSWs into big use cases with multiple instances involved, and why Redis Vector Sets expose the actual data structure in the face of the user (I believe programmers are smart and don’t need babysitting, but it’s not *just* that), I want to go back and talk again about memory, because there is an interesting story to tell about this specific aspect.

Most HNSWs implementations are not able to reclaim memory directly when you delete a node from the graph. I believe there are two main reasons for that:

1. People misunderstand the original HNSW paper in a specific way: they believe links can be NOT reciprocal among neighbors. And there is a specific reason why they think so.

2. The paper does not say anything about deletion of nodes and how to fix the graph after nodes go away and we get missing links in the “web” of connections.

The first problem is a combination (I believe) of lack of clarity in the paper and the fact that, while implementing HNSWs, people face a specific problem: when inserting a new node, and good neighbors are searched among existing nodes, often the candidates already have the maximum number of outgoing links. What to do, in this case? The issue is often resolved by linking unidirectionally from the new node we are inserting to the candidates that are already “full” of outgoing links. However, when you need to delete a node, you can no longer resolve all its incoming links, so you can’t really reclaim memory. You mark it as deleted with a flag, and later sometimes there is some rebuilding of the graph to “garbage collect” stale nodes, sometimes memory is just leaked.

So, to start, my implementation in Redis does things differently by forcing links to be bidirectional. If A links to B, B links to A. But, how to do so, given that A may be busy? Well, this gets into complicated territory but what happens is that heuristics are used in order to drop links from existing nodes, with other neighbors that are well connected, and if our node is a better candidate even for the target node, and if this is not true there are other ways to force a new node to have at least a minimal number of links, always trying to satisfy the small world property of the graph.

This way, when Redis deletes a node from a Vector Set, it always has a way to remove all the pointers to it. However, what to do with the remaining nodes that now are missing a link? What I do is to create a distance matrix among them, in order to try to link the old node neighbors among them, trying to minimize the average distance. Basically for each pair of i,j nodes in our matrix, we calculate how good is their connection (how similar their vectors are) and how badly linking them affects the *remaining* possible pairs (since there could be elements left without good pairs, if we link two specific nodes). After we build this matrix of scores, we then proceed with a greedy pairing step.

This works so well that you can build a large HNSW with millions of elements, later delete 95% of all your elements, and the remaining graph still has good recall and no isolated nodes and so forth.

That is what I mean when I say that there is space in HNSWs for new papers to continue the work.

## Scaling HNSWs to multiple processes

When I started to work at Redis Vector Sets, there was already a vector similarity implementation in Redis-land, specifically as an index type of RediSearch, and this is how most people think at HNSWs: a form of indexing of existing data.

Yet I wanted to provide Redis with a new HNSW implementation exposed in a completely different way. Guess how? As a data structure, of course. And this tells a story about how Redis-shaped is my head after so many years, or maybe it was Redis-shaped since the start, and it is Redis that is shaped after my head, since I immediately envisioned how to design a Redis data structure that exposed HNSWs to the users, directly, and I was puzzled that the work with vectors in Redis was not performed exactly like that.

At the same time, when I handed my design document to my colleagues at Redis, I can’t say that they immediately “saw” it as an obvious thing. My reasoning was: vectors are like scores in Redis Sorted Sets, except they are not scalar scores where you have a total order. Yet you can VADD, VREM, elements, and then you can call VSIM instead of ZRANGE in order to have *similar* elements. This made sense not just as an API, but I thought of HNSWs as strongly composable, and not linked to a specific use case (not specific to text embeddings, or image embeddings, or even *learned* embeddings necessarily). You do:

    VADD my_vector_set VALUES [… components …] my_element_string

So whatever is in your components, Redis doesn't care, when you call VSIM it will report similar elements.

But this also means that, if you have different vectors about the same use case split in different instances / keys, you can ask VSIM for the same query vector into all the instances, and add the WITHSCORES option (that returns the cosine distance) and merge the results client-side, and you have magically scaled your hundred of millions of vectors into multiple instances, splitting your dataset N times [One interesting thing about such a use case is that you can query the N instances in parallel using multiplexing, if your client library is smart enough].

Another very notable thing about HNSWs exposed in this raw way, is that you can finally scale writes very easily. Just hash your element modulo N, and target the resulting Redis key/instance. Multiple instances can absorb the (slow, but still fast for HNSW standards) writes at the same time, parallelizing an otherwise very slow process.

This way of exposing HNSWs also scales down in a very significant way: sometimes you want an HNSW for each user / item / product / whatever you are working with. This is very hard to model if you have an index on top of something, but it is trivial if your HNSWs are data structures. You just can have a Vector Set key for each of your items, with just a handful of elements. And of course, like with any other Redis key, you can set an expiration time on the key, so that it will be removed automatically later.

All this can be condensed into a rule that I believe should be more present in our industry: many programmers are smart, and if instead of creating a magic system they have no access to, you show them the data structure, the tradeoffs, they can build more things, and model their use cases in specific ways. And your system will be simpler, too.

## Scaling loading times

If I don’t use threading, my HNSW library can add word2vec (300 components for each vector) into an HNSW at 5000 elements/second if I use a single thread, and can query the resulting HNSW at 90k queries per second. As you can see there is a large gap.

This means that loading back an HNSW with many millions of elements from a Redis dump file into memory would take a lot of time. And this time would impact replication as well. Not great. But, this is true only if we add elements from the disk to the memory in the most trivial way, that is storing “element,vector” on disk and then trying to rebuild the HNSW in memory. There is another lesson to learn here. When you use HNSWs, you need to serialize the nodes and the neighbors as they are, so you can rebuild everything in memory just allocating stuff and turning neighbors IDs into pointers. This resulted in a 100x speedup.

But do you really believe the story ends here? Hehe. Recently Redis has stronger security features and avoids doing bad things even when the RDB file is corrupted by an attacker. So what I needed to do was to make sure the HNSW is valid after loading, regardless of the errors and corruption in the serialized data structure. This involved many tricks, but I want to take the freedom to just dump one comment I wrote here, as I believe the reciprocal check is particularly cool:

    /* Second pass: fix pointers of all the neighbors links.
     * As we scan and fix the links, we also compute the accumulator
     * register "reciprocal", that is used in order to guarantee that all
     * the links are reciprocal.
     *
     * This is how it works, we hash (using a strong hash function) the
     * following key for each link that we see from A to B (or vice versa):
     *
     *      hash(salt || A || B || link-level)
     *
     * We always sort A and B, so the same link from A to B and from B to A
     * will hash the same. Then we xor the result into the 128 bit accumulator.
     * If each link has its own backlink, the accumulator is guaranteed to
     * be zero at the end.
     *
     * Collisions are extremely unlikely to happen, and an external attacker
     * can't easily control the hash function output, since the salt is
     * unknown, and also there would be to control the pointers.
     *
     * This algorithm is O(1) for each node so it is basically free for
     * us, as we scan the list of nodes, and runs on constant and very
     * small memory. */

## Scaling use cases: JSON filters

I remember the day when the first working implementation of Vector Sets felt complete. Everything worked as expected and it was the starting point to start with the refinements and the extra features.

However in the past weeks and months I internally received the feedback that most use cases need some form of mixed search: you want near vectors to a given query vector (like most similar movies to something) but also with some kind of filtering (only released between 2000 and 2010). My feeling is that you need to query for different parameters less often than product people believe, and that most of the time you can obtain this more efficiently by adding, in this specific case, each year to a different vector set key (this is another instance of the composability of HNSWs expressed as data structures versus a kind of index).

However I was thinking about the main loop of the HNSW greedy search, that is something like this:

// Simplified HNSW greedy search algorithm. Don’t trust it too much.
while(candidates.len() > 0) {
    c = candidates.pop_nearest(query);
    worst_distance = results.get_worst_dist(query);
    if (distance(query,c) > worst_distance) break;
    foreach (neighbor from c) {
        if (neighbor.already_visited()) continue;
        neighbor.mark_as_visited();
        if (results.has_space() OR neighbor.distance(query) < worst_distance) {
            candidates.add(neighbor);
            results.add(neighbor);
        }
    }
}
return results;

So I started to play with the idea of adding a JSON set of metadata for each node. What if, once I have things like {“year”: 1999}, this was enough to filter while I perform the greedy search? Sure, the search needed to be bound, but there is a key insight here: I want, to start, elements that are *near* to the query vector, so I don’t really need to explore the whole graph if the condition on the JSON attributes is not satisfied by many nodes. I’ll let the user specify the effort, and anyway very far away results that match the filter are useless.

So that’s yet another way how my HNSW differs: it supports filtering by expressions similar to the ones you could write inside an “if” statement of a programming language. And your elements in the Vector Set can be associated with JSON blobs, expressing their properties. Then you can do things like:

    VSIM movies VALUES … your vector components here… FILTER '.year >= 1980 and .year < 1990'

## A few words on memory usage

HNSW’s fatal issue is — in theory — that they are normally served from memory. Actually, you can implement HNSWs on disk, even if there are better data structures from the point of view of disk access latencies. However, in the specific case of Redis and Vector Sets the idea is to provide something that is very fast, easy to work with: the flexibility of in-memory data structures help with that. So the question boils down to: is the memory usage really so bad?

Loading the 3 million Word2Vec entries into Redis with the default int8 quantization takes 3GB of RAM, 1kb for each entry. Many use cases have just a few tens of million of entries, or a lot less. And what you get back from HNSWs, if well implemented, and in memory, is very good performance, which is crucial in a data structure and in a workload that is in itself slow by definition. In my MacBook I get 48k ops per second with redis-benchmark and VSIM against this key (holding the word2vec dataset). My feeling is that the memory usage of in-memory HNSWs is very acceptable for many use cases. And even in the use cases where you want the bulk of your vectors on disk, even if there is to pay for slower performance, your hot set should likely be served from RAM.

This is one of the reasons why I believe that, to be active in HNSW research is a good idea: I don’t think they will be replaced anytime soon for most use cases. It seems more likely that we will continue to have different data structures that are ideal for RAM and for disk depending on the use cases and data size. Moreover, what I saw recently, even just scanning the Hacker News front page, is people with a few millions of items fighting with systems that are slower or more complicated than needed. HNSWs and carefully exposing them in the right way can avoid all that.

## Conclusions

I like HNSWs, and working and implementing them was a real pleasure. I believe vectors are a great fit for Redis, even in an AI-less world (for instance, a few months ago I used them in order to fingerprint Hacker News users, replicating an old work published on HN in the past). HNSWs are simply too cool and powerful for a number of use cases, and with AI, and learned embeddings, all this escalates to a myriad of potential use cases. However, like most features in Redis, I expect that a lot of time will pass before people realize they are useful and powerful and how to use them (no, it’s not just a matter of RAG). This happened also with Streams: finally there is mass adoption, after so many years.

If instead you are more interested in HNSW and the implementation I wrote, I believe the code is quite accessible, and heavily commented:

[https://github.com/redis/redis/blob/unstable/modules/vector-sets/hnsw.c](https://github.com/redis/redis/blob/unstable/modules/vector-sets/hnsw.c)

If you want to learn more about Redis Vector Sets, please feel free to read the README file I wrote myself. There is also the official Redis documentation, but I suggest you start from here:

[https://github.com/redis/redis/tree/unstable/modules/vector-sets](https://github.com/redis/redis/tree/unstable/modules/vector-sets)

Thanks for reading such a long blog post! And have a nice day.

References. This is the paper about the "H" in HNSW and how useful it is -> [https://arxiv.org/abs/2412.01940](https://arxiv.org/abs/2412.01940)