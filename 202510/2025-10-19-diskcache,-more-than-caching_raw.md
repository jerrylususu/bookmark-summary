Title: Diskcache, more than caching

URL Source: https://www.bitecode.dev/p/diskcache-more-than-caching

Published Time: 2025-10-19T08:46:52+00:00

Markdown Content:
_I adore SQLite, and I like caching a lot. If you mix the two, you get [diskcache](https://grantjenks.com/docs/diskcache/api.html#diskcache.Lock), a Python local key/value store that can act like a small local subset of Redis. It stores Python values, expires them, has queues, mappings, and deques._

_But it can do more than that: transactions, tagging, locking, thundering herd mitigation… There is a lot to unpack from this little utility._

_And all that can be accessed from several processes concurrently, even when writing, thanks to sharding._

I love [diskcache](https://grantjenks.com/docs/diskcache/api.html#diskcache.Lock), I wish it came with Python. [Kinda](https://www.bitecode.dev/p/python-libs-that-i-wish-were-part). On paper, it’s a Python local cache-oriented lib backed by SQLite, and therefore fast and robust. It features most things you expect from cache: automatic serialization, key/value syntax, expiration system with transparent key evictions...

Using it looks like this:

```
>>> from diskcache import Cache
... import time
... cache = Cache(’/tmp/mycache’)
... # expires after 2 seconds
... cache.set(’frog’, ‘frinos’, expire=2)
True
>>> print(cache.get(’frog’))
frinos
>>> time.sleep(3); print(cache.get(’frog’))
None
```

Simple... and efficient! Access time is in µs:

```
>> %timeit cache.set(’frog’, ‘frinos’)
39.9 μs ± 271 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
>>> %timeit cache.get(’frog’)
5.01 μs ± 80.4 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
```

It’s a sweet little piece of software that is really nice to have in your toolbox. You can use it in quick and dirty scripts, and even in small to medium websites. In fact, it comes with a Django cache backend out of the box.

But it can do much more than caching!

Being based on SQLite means you get atomic and thread-safe operations, sweet, sweet, SOLID semantics, and with that, you get a lot of things for free.

One thing diskcache can provide that a lot of caching systems don’t, is a transaction, meaning a way to write or read a bunch of stuff as if it were one unit:

```
with cache.transact():
     value = cache.get(’counter’, 0)
     value += 1
     cache.set(’counter’, value)
```

Because the cache can be written from several processes, this is very valuable. Consider this script:

```
from diskcache import Cache
from multiprocessing import Process
import sys

cache = Cache(’/tmp/mycache’)

def increment(use_transaction: bool):
    for _ in range(100):
        if use_transaction:
            with cache.transact():  # atomic read-modify-write
                value = cache.get(’counter’, 0)
                cache.set(’counter’, value + 1)
        else:
            # No transaction — race conditions likely under concurrency
            value = cache.get(’counter’, 0)
            cache.set(’counter’, value + 1)

if __name__ == “__main__”:
    use_transaction = “--with-transaction” in sys.argv

    cache.set(’counter’, 0)

    print(f”Running with{’out’ if not use_transaction else ‘’} transactions...”)

    # Launch 4 processes doing increments concurrently
    procs = [Process(target=increment, args=(use_transaction,)) for _ in range(4)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print(’Final counter:’, cache.get(’counter’))
```

It runs 4 processes, within each, a loop of 100 steps, incrementing the counter, so we should reach 400. But without a transaction, we do not, because sometimes several processes read the old value together, and increment this value, each of them saving the same number in the cache:

```
python increment.py
Running without transactions...
Final counter: 165
```

But with transactions, we get 400, because each pair read and write is guaranteed to happen as a whole:

```
python increment.py --with-transaction
Running with transactions...
Final counter: 400
```

Although keep transactions as short as possible because, during a transaction, no other writes occur to the cache.

Another SQLite goodness is the fact under the hood, it’s a full-featured relational database. Diskcache takes advantage of that in several ways.

It can add metadata to cache keys. E.G, it can add tags:

```
for num in range(100):
    _ = cache.set(num, num, tag=’odd’ if num % 2 else ‘even’)
```

And then perform operations, like key eviction, based on those tags:

`cache.evict(’even’)`
It can also let you iterate on keys in either insertion order or sorted keys:

```
for key in ‘cab’:
    cache[key] = None

list(cache)
[’c’, ‘a’, ‘b’]

list(cache.iterkeys())
[’a’, ‘b’, ‘c’]
```

And can look up the first and last item:

```
cache.peekitem()
(’comment:1’, "FIIIIIIIIIIIRST")

cache.peekitem(last=False)
(’comment:8908098’, "Pics or didn't happen")
```

In fact, if all you need is a queue, keys can be generated automatically, and values pushed and pulled, like in a list:

```
>>> key = cache.push(’first’)
>>> cache[key]
‘first’
>>> _ = cache.push(’second’)
>>> _ = cache.push(’zeroth’, side=’front’)
>>> _, value = cache.peek()
>>> value
‘zeroth’
>>> key, value = cache.pull()
>>> print(key)
499999999999999
>>> value
‘zeroth’
```

There is even a wrapper for that: [Deque](https://grantjenks.com/docs/diskcache/api.html#diskcache.Deque), an ordered collection with optimized access at its start and end. It features a `.rotate()` methods that take the last item and put it back as the first one, very quickly, so you can cycle the whole thing, like Python’s `collections.deque`.

Diskcache also comes with an (opt-in) sharding system to allow writing from several processes, so you can use it from your typical FastAPI, Flask, or Django application with multiple workers and not encounter the dreaded SQLITE `sqlite3.OperationalError: database is locked`:

```
from diskcache import FanoutCache
# 4 shards, so at 4 concurrent possible writes, and a 1 second timeout
cache = FanoutCache(shards=4, timeout=1)
```

So there is no reason to create only one instance of diskcache. You can have many, each being specialized and dedicated to something. One cache can be used as a general cache. Another one can be a queue. A last one can be a poor man’s DB.

Making multiple concurrent actors play nicely is really hard. E.G: how do you avoid duplicating your `functools.lru_cache` ? How do you avoid your cache eviction from triggering several calculations at the same time? How do you avoid concurrent access to resources?

Diskcache comes with plenty of utilities for that, with sane defaults, and they will work even if you are not the one starting the processes (like with a WSGI server).

It can cache the value of a function:

```
>>> @cache.memoize()
... def slow_add(a, b):
...     print(f”Computing {a} + {b}”)
...     return a + b
... 
... print(slow_add(2, 3))  # Computes
... print(slow_add(2, 3))  # Cached result, no print
Computing 2 + 3
5
5
```

But what if the function takes 5 seconds, and then 4 processes call it at the same time? They will all trigger the cache regeneration at the same time. Well, you can ask for an early optimistic run:

```
from diskcache import memoize_stampede
@memoize_stampede(cache, 5)
def expensive_compute(x):
    import time
    print(f”Computing {x}”)
    time.sleep(2)
    return x * x

print(expensive_compute(5))
```

The first run will perform the function, but no subsequent call will. Instead, they will always return the cached result, but also perform a probabilistic calculation about the need to update the cache. If it’s time, it may run the function in a thread. The closer to the expiration, the more chance to run the function.

Of course, you also have various types of locks, the simplest being:

```
from diskcache import Lock
name = ‘stock and two smocking barrels’
lock = Lock(cache, name)
with lock:
    print(”Critical section: only one process/thread at a time”)
```

A much better solution than creating a lock file. There are also reentrant locks, bounded semaphores, and a decorator to lock a function:

```
@cache.barrier(cache, Lock)
def compute():
    with barrier:
        print(”Computing...”)
        import time; time.sleep(2)

compute()  # Only one computes; others wait and reuse result
```

Or throttle one (limit to one call every x seconds):

```
@diskcache.throttle(’mykey’, expire=3)
def myfunc():
    print(”Executed!”)
    return “done”

myfunc()  # Executes
myfunc()  # Skipped if within 3 seconds
```

You can mix and max, and get creative. If you pair multi-processing with a lock and a Deque, you get a cheap task queue. If you use `.incr` on IP+UA+URL key with a daily expiration time, you get an approximate page visit count. Add a bloom filter on top, and you get a sloppy but working deny list for abusers.

Once you get a few basics that compose well, you can get pretty far until you need big-boy solutions.