Title: The surprising way to save memory with BytesIO

URL Source: https://pythonspeed.com/articles/bytesio-reduce-memory-usage/

Published Time: 2025-01-30T00:00:00+00:00

Markdown Content:
If you need a file-like object that stores bytes in memory in Python, chances are you you’re using Pytho’s built-in `io.BytesIO()`. And since you’re already using an in-memory object, if your data is big enough you probably should try to save memory when reading that data back out. After all, it’s better not to have two copies of all the data in memory when only one will suffice.

In this article we’ll cover:

*   A quick intro to `BytesIO`.
*   The memory usage impacts of `BytesIO.read()`.
*   The two alternatives for accessing `BytesIO` data efficiently, and the tradeoffs between them.

So what’s a `BytesIO`?
----------------------

Python’s [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO) allows you to create a file-like object that stores bytes in memory:

```
from io import BytesIO

f = BytesIO()
f.write(b"hello ")
f.write(b"world")
f.seek(0)
assert f.read() == b"hello world"
```

The problem with `BytesIO.read()`
---------------------------------

At some point you might want to access the data in the `BytesIO` directly, as a `bytes` or `memoryview` object. We’ll talk about what a `memoryview` is and why you might want it a bit later.

As we saw above, since `BytesIO` is a file-like object we can just use its `read()` method to extract `bytes`. Unfortunately, this comes at the cost of doubling the amount of memory used.

To demonstrate the problem, we’ll write a utility function that measures how much extra memory we’ve allocated:

```
import gc
import tracemalloc
from contextlib import contextmanager
tracemalloc.start()

@contextmanager
def report_allocated(action: str):
    print(action + ":")
    gc.collect()
    _, current = tracemalloc.get_traced_memory()
    try:
        yield
    finally:
        gc.collect()
        _, new_current = tracemalloc.get_traced_memory()
        print(
            "  Allocated additional",
            round((new_current - current) / (1024 * 1024)),
            "MiB\n",
        )
```

We can then measure memory usage from creating a `BytesIO` and then calling `read()`:

```
with report_allocated("Creating BytesIO"):
    f = BytesIO()
    chunk = b"X" * (1024 * 1024)
    for _ in range(50):
        f.write(chunk)
    f.seek(0)

with report_allocated("BytesIO.read()"):
    data : bytes = f.read()
```

Here’s the output:

```
Creating BytesIO:
  Allocated additional 57 MiB

BytesIO.read():
  Allocated additional 50 MiB
```

As you can see, `read()` creates a whole new copy of the data, using a lot more memory. Can we do better?

`BytesIO.getbuffer()`: getting a `memoryview` of the data
---------------------------------------------------------

One useful method `BytesIO` has that regular files don’t is [`BytesIO.getbuffer()`](https://docs.python.org/3/library/io.html#io.BytesIO.getbuffer): it returns a `memoryview` of the underlying data. Unlike `bytes` objects, a `memoryview` is a view into existing memory, so using it doesn’t allocate any new memory:

```
with report_allocated("Creating BytesIO"):
    # ... same as above ...

with report_allocated("BytesIO.getbuffer()"):
    data : memoryview = f.getbuffer()
```

When we run this, we get:

```
Creating BytesIO:
  Allocated additional 57 MiB

BytesIO.getbuffer():
  Allocated additional 0 MiB
```

Problem solved! In some cases, anyway; you can write a `memoryview` to a regular file, for example. But sometimes a `memoryview` isn’t what you want.

### Some limitations of `memoryview`

One problem with `memoryview` is that it lacks many of the methods that `bytes` has. For example, we can’t do `memoryview.find()`:

```
>>> data = b"abcd"
>>> data.find(b"c")
2
>>> data_view = memoryview(data)
>>> data_view.find(b"c")
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    data_view.find(b"c")
    ^^^^^^^^^^^^^^
AttributeError: 'memoryview' object has no attribute 'find'
>>>
```

A more obscure but still real problem is accessing `memoryview` objects from compiled extensions. Access has to happen using the Python [buffer protocol](https://docs.python.org/3/c-api/buffer.html). These are part of the stable C ABI only starting in CPython version 3.11.

At the time of writing, most open source projects are also supporting Python 3.10 and 3.9. If you’re working on such a project, and it’s compiling a single extension using the 3.9 or 3.10 versions of the ABI (i.e. `abi3` wheels), you can’t use the buffer protocol yet. Which means you can’t access `memoryview` objects. This problem will go away in October 2027 when 3.10 is end-of-life and open source projects drop support for anything before 3.11.

### From `memoryview` to `bytes`

You can deal with both these limitations by creating a new `bytes` object out of a `memoryview`, e.g.:

```
>>> new_data = bytes(data_view)
```

But that copies the data, allocating memory and undoing all the memory-saving benefits of using `BytesIO.getbuffer()`. In other words, `bytes(my_bytesio.getbuffer())` uses the same amount of memory as `my_bytesio.read()`. So that’s not helpful.

`BytesIO.getvalue()`: surprisingly efficient
--------------------------------------------

Another options is [`BytesIO.getvalue()`](https://docs.python.org/3/library/io.html#io.BytesIO.getvalue), which returns the contents of the `BytesIO` as a `bytes` object. My assumption has always been that this creates a copy of the underlying data.

I was wrong! The CPython developers are actually much smarter than that.

```
with report_allocated("Creating BytesIO"):
    # ... same as above ...

with report_allocated("BytesIO.getvalue()"):
    data : bytes = f.getvalue()
```

When run, we get:

```
Creating BytesIO:
  Allocated additional 57 MiB

BytesIO.getvalue():
  Allocated additional 0 MiB
```

This is magic. We’re getting a new `bytes` object, without allocating any memory.

How does this work? `BytesIO` is using copy-on-write. Internally, it keeps a reference to the new `bytes` object returned from `getvalue()`. So long as you don’t write to the `BytesIO`, any reads can happen off the same memory. But when you write to the `BytesIO`, it knows it can’t modify the current memory anymore (since `bytes` are supposed to be read-only) and only at this point will it allocate new memory.

```
with report_allocated("Creating BytesIO"):
    # ... same as above ...

with report_allocated("BytesIO.getvalue()"):
    data : bytes = f.getvalue()

with report_allocated("write to BytesIO"):
    f.seek(0, 2)  # go to the end of the file
    f.write(b"hello")

```

When we run this we get:

```
Creating BytesIO:
  Allocated additional 57 MiB

BytesIO.getvalue():
  Allocated additional 0 MiB

write to BytesIO:
  Allocated additional 50 MiB
```

This allows `BytesIO.getvalue()` to allocate no memory in the common case where you only read from the `BytesIO` after you’re done writing.

> To see some real-world impacts of switching from `read()` to `getvalue()`, see this [pull request I opened against Polars](https://github.com/pola-rs/polars/pull/20649); the work was sponsored by [G-Research’s open source program office](https://www.gresearch.com/teams/open-source-software/).
> 
> Does your company need help maintaining or contributing to open source projects? [Send me an email](mailto:itamar@pythonspeed.com) to see if I have availability.

`getvalue()` or `getbuffer()`?
------------------------------

To summarize, if you want to minimize memory usage when extracting data from `BytesIO`:

*   Avoid `BytesIO.read()`.
*   If you need the contents as `bytes`, use `BytesIO.getvalue()`.
*   If you can use `memoryview`, use `BytesIO.getbuffer()`.
