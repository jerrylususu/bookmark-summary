Title: Robin Hood Hashing should be your default Hash Table implementation

URL Source: https://www.sebastiansylvan.com/post/robin-hood-hashing-should-be-your-default-hash-table-implementation/

Markdown Content:
8/May 2013
There’s a neat variation on open-addressing based hash tables called [Robin Hood hashing](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&frm=1&source=web&cd=1&cad=rja&sqi=2&ved=0CDAQFjAA&url=https%3A%2F%2Fcs.uwaterloo.ca%2Fresearch%2Ftr%2F1986%2FCS-86-14.pdf&ei=RJqJUcHZH8HuigKGsoHQDw&usg=AFQjCNEyXJn73zNas94y_yK55dv--oMmbg&sig2=CRV_bivIwvFsw8c2wz5ZwQ&bvm=bv.46226182,d.cGE). This technique isn’t very well-known, but it makes a huge practical difference because it both improves performance and space utilization compared to other “standard” hash tables (e.g. [chaining](http://en.wikipedia.org/wiki/Hash_table)). It also eliminates the major downside of other open addressing hash tables.

Here are the benefits, summarized:

*   High load factors can be used without seriously affecting performance. 0.9 is perfectly reasonable as a default (0.95 or higher works too, it mainly affects insertion cost a bit).

*   No linked lists or other extra pointers. This reduces cache misses and storage overhead. Your underlying structure can be a simple flat array since it’s just open addressing under the hood.

*   Lookup and insertion logic is fast. Again, no linked lists to traverse or other complications, just a linear probe sequence with a few checks per element.

*   Unlike other open addressing schemes, looking for non-existent elements is still fast.

For a simple benchmark where I inserted 100k english words into a map, then deleted 10% of them, and then looked them all up again, the timings for my simple Robin Hood hash table was **23%**, **66%** and **25% **lower for insertions, deletions and lookups respectively compared to the VS 2012 std::unordered_map, it did this using **30%** less memory overall.

It’s all about the variance
---------------------------

So the basic idea is to take normal open addressing, but use one clever trick in order to drastically reduce the variance of the expected average and maximum probe lengths. We’ll se later why reducing variance is so important. To give you an idea how Robin Hood Hashing improves things, the probe length variance for a RH table at a load factor of 0.9 is 0.98, whereas for a normal open addressing scheme it’s 16.2. At a load factor of 0.99 it’s 1.87 and 194 respectively.

**The clever trick is just this**: when you probe for a position to insert a new element, if the probe length for the existing element is less than the current probe length for the element being inserted, swap the two elements and keep going.

That way elements that were inserted early and thus “lucked out” on their probe lengths, will gradually be moved away from their preferred slot as new elements come in that could make better use of that place in the table (hence the name - the insertion “takes from the rich”, i.e. the elements with low probe counts). It leads to an “evening out” of the probe lengths.

Why is low variance better? Well, with modern cache architectures a probe count of 1 isn’t really much faster than a probe count of 3, because the main cost is fetching the cache line, so the ideal scenario is for all elements to have the same probe count, and having that probe count fitting within one cache line.

It turns out that Robin Hood hashing has the same expected probe count as normal open addressing (about 2.55) - it just has substantially less variance, and therefore ends up with far fewer cache misses. Yes, there are fewer elements that can early out after 1 probe, but there also far fewer elements that end up needing to fetch multiple cache lines because of long probe lengths.

Furthermore, the expected value of the _longest_ probe sequence approaches about 6 for a load of 0.9 (it’s not actually constant, but grows very, very slowly - [see this paper](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&frm=1&source=web&cd=2&cad=rja&sqi=2&ved=0CDcQFjAB&url=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fsummary%3Fdoi%3D10.1.1.130.6339&ei=RJqJUcHZH8HuigKGsoHQDw&usg=AFQjCNFquQO-Wa7uCGLwFTdLKpEHDBGsig&sig2=DfIIJzRj2YXIRyLiHGCHUA&bvm=bv.46226182,d.cGE)), which is pretty reasonable.

What about failed lookups?
--------------------------

So now you’re probably thinking that this sounds good, but in the back of your mind you know that normal open addressing tables do pretty well too, but have a major downside in that searching for non-existing elements is troublesome to handle. To allay your fears I’ll first tell you a very simple (but totally practical) solution that is enabled by the low variance, and then we’ll see the even better version later.

First a recap. The usual problem is this: since the search algorithm terminates when you find an “empty” slot in the underlying array, it can take a very long time to determine that an element doesn’t exist in the array when the table grows full.

How does Robin Hood hashing solve this? Well the simplest solution is to exploit the fact that the expected longest probe count is low (~6). Just modify the standard search algorithm to ignore empty slots (rather than terminate the search) and keep going until you’ve probed longer than the known maximum probe length for the whole table. This maximum probe length will be small, with a very high probability, even for very loaded tables.

This solution would obviously be inefficient for the standard open addressing scheme, since the expected longest probe count is much higher (e.g. at a load of 0.9 and ~64K elems it is about 70).

The details
-----------

In order to know what the probe count of an existing element is (which is key to the algorithm) we could just re-hash the element to re-compute its “desired” slot index and then subtract this from its actual location. A faster way is to simply cache the hash value for each key.

Storing the hash value is generally a sensible strategy anyway, because it means you have a fast early-out for comparisons, so we take that approach here. In other words, the hash table elements consist of a 32 bit hash value, the key, and the value. For my implementation I stored the hash values in a separate array in order to get more hash probes per cache line (at the expense of a second mandatory cache miss to actually fetch the key). This gave a small speed-up for my test where the key size was large (sizeof(std::string)), but there’s a #define in the code to put the hash value alongside its key.

In order to indicate that a slot is unused, we modify the hash function to never return 0, and use a stored hash value of 0 to mean “uninitialized slot”.

First, let’s look at the insertion algorithm, since this is where the actual Robin Hood trick comes in.

`1 2 3 4 5 6 7 8 9101112131415161718192021222324252627282930313233````
void insert_helper(uint32_t hash, Key&& key, Value&& val)
{
	int pos = desired_pos(hash);
	int dist = 0;
	for(;;)
	{			
		if(elem_hash(pos) == 0)
		{			
			construct(pos, hash, move(key), move(val));
			return;
		}

		// If the existing elem has probed less than us, 
		// then swap places with existing
		// elem, and keep going to find another slot for that elem.
		int existing_dist = probe_distance(elem_hash(pos), pos);
		if (existing_dist < dist)
		{	
			if(is_deleted(elem_hash(pos)))
			{
				construct(pos, hash, move(key), move(val));
				return;
			}			
			swap(hash, elem_hash(pos));
			swap(key, buffer[pos].key);
			swap(val, buffer[pos].value);
			dist = existing_dist;
		}

		pos = (pos+1) & mask;
		++dist;			
	}
}
```

The algorithm is pretty simple. We simply loop until we’ve found an uninitialized slot (hash value == 0). If we found an existing slot whose probe distance is less than our current probe count (‘dist’), we swap places and continue. Note: using move semantics here matters (e.g. for efficient swapping).

In order to delete an element, we follow the same strategy as for normal open addressing and mark the slot as a tombstone. Tombstones are treated specially in the insert algorithm. We overwrite the tombstone only when we would’ve wanted to swap anyway (see the check for is_deleted above).

We must mark the tombstone using a whole bit rather than just reserving a single hash value (like we did for uninitialized slots), because we need to know the probe count of the tombstone.

`1 2 3 4 5 6 7 8 9101112````
bool erase(const Key& key)
{
	const uint32_t hash = hash_key(key);
	const int ix = lookup_index(key);

	if (ix == -1) return false;

	buffer[ix].~elem();
	elem_hash(ix) |= 0x80000000; // mark as deleted
	--num_elems;
	return true;
}
```

This is all pretty straightforward. We first find the element, then we call its destructor, and finally set the “tombstone” bit.

And lastly, the lookup algorithm:

`1 2 3 4 5 6 7 8 9101112131415161718````
int lookup_index(const Key& key) const
{
	const uint32_t hash = hash_key(key);
	int pos = desired_pos(hash);
	int dist = 0;
	for(;;)
	{							
		if (elem_hash(pos) == 0) 
			return -1;
		else if (dist > probe_distance(elem_hash(pos), pos)) 
			return -1;
		else if (elem_hash(pos) == hash && buffer[pos].key == key) 
			return pos;				

		pos = (pos+1) & mask;
		++dist;
	}
}
```

This just finds the desired position of the element using the hash, then probes linearly from there on in. There are two conditions to signify that the element doesn’t exist, and finally one check to see if we’ve found the element.

The first exit condition checks for completely uninitialized elements. This is because if the element we are looking for had probed an uninitialized slot during insertion, it would have simply been place there. So the existence of an uninitialized slot along our probe sequence means the element must not be in the table.

The second condition is more interesting. This is our replacement for simple checking the probe distance against a table-wide maximum probe count. We _know_ that when we probe an element during insertion, the one with the longer probe count of the two gets to keep the slot. So if we’re looking for an element that exists,we should expect to never see an existing element with a shorter probe count then our current count (if that _had_ happened, there would’ve been a swap during insertion!).

In other words, we early out as soon as our current probe count exceeds the probe count of the stored element. Since the average probe count for stored elements is 2.55, we can exit pretty quickly for non-existent elements (much earlier than stopping after a table-wide maximum probe count).

This second condition is why we need to maintain the hash value even for tomb stones. Imagine what would happen if we simply marked the slot as uninitialized when it was deleted - the next insertion that comes across it would simply occupy it thereby getting an unfairly low probe count, and more importantly messing up the second condition above. Instead, we just flag deleted elements as tombstones, and only reuse the slot in the insertion algorithm if a swap would’ve happened anyway.

Finally, the last condition simply compares the hashes and the keys and returns the found element.

Here’s a the full code for this blog post: [code](https://gist.github.com/ssylvan/5538011). I should note that I wrote this specific implementation for this blog post, so it hasn’t been extensively used or tested (or optimized). It’s quite likely that there are bugs.

More Reading
