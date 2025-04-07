Title: Writing C for curl

URL Source: https://daniel.haxx.se/blog/2025/04/07/writing-c-for-curl/

Published Time: 2025-04-07T08:26:53+02:00

Markdown Content:
It is a somewhat common question to me: how do we write C in [curl](https://curl.se/) _to make it safe and secure for billions of installations_? Some precautions we take and decisions we make. There is no silver bullet, just guidelines. As I think you can see for yourself below they are also neither strange nor surprising.

The ‘c’ in curl does not and never did stand for the C programming language, it stands for _client_.

Disclaimer
----------

**This text does in no way mean that we don’t occasionally merge security related bugs.** We do. We are human. We do mistakes. Then we fix them.

Testing
-------

We write as many tests as we can. We run all the static code analyzer tools we can on the code – frequently. We run fuzzers on the code non-stop.

C is not memory-safe
--------------------

We are certainly not immune to memory related bugs, mistakes or vulnerabilities. We count about 40% of our security vulnerabilities to date to have been the direct result of us using C instead of a memory-safe language alternative. This is however a much lower number than the 60-70% that are commonly repeated, originating from a few big companies and projects. If this is because of a difference in counting or us actually having a lower amount of C problems, I cannot tell.

Over the last five years, we have received **no** reports identifying a _critical_ vulnerability and only two of them were rated at severity _high_. The rest ( 60 something) have been at severity _low_ or _medium_.

We currently have close to 180,000 lines of C89 production code (excluding blank lines). We stick to C89 for widest possible portability and because we believe in continuous non-stop iterating and polishing and never rewriting.

Readability
-----------

Code should be easy to read. It should be clear. No hiding code under clever constructs, fancy macros or overloading. Easy-to-read code is easy to review, easy to debug and easy to extend.

Smaller functions are easier to read and understand than longer ones, thus preferable.

Code should read as if it was written by a single human. There should be a consistent and uniform code style all over, as that helps us read code better. Wrong or inconsistent code style is a bug. We fix all bugs we find.

We have tooling that verify basic code style compliance.

Narrow code and short names
---------------------------

Code should be written narrow. It is hard on the eyes to read long lines, so we enforce a strict 80 column maximum line length. We use two-spaces indents to still allow us to do some amount of indent levels before the column limit becomes a problem. If the indent level becomes a problem, maybe it should be split up in several sub-functions instead?

Also related: (in particular local) identifiers and names should be short. Having long names make them hard to read, especially if there are multiple ones that are similar. Not to mention that they can get hard to fit within 80 columns after some amount of indents.

So many people will now joke and say something about wide screens being available and what not but the key here is readability. Wider code is harder to read. Period. The question could possibly be exactly where to draw the limit, and that’s a debate for every project to have.

Warning-free
------------

While it should be natural to everyone already, we of course build all curl code entirely without any compiler warning in any of the 220+ CI jobs we perform. We build curl with all the most picky compiler options that exist with the set of compilers we use, and we silence every warning that appear. We treat every compiler warning as an error.

Avoid “bad” functions
---------------------

There are some C functions that are just plain bad because of their lack of boundary controls or local state and we avoid them (gets, sprintf, strcat, strtok, localtime, etc).

There are some C functions that are complicated in other ways. They have too open ended functionality or do things that often end up problematic or just plain wrong; they easily lead us into doing mistakes. We avoid sscanf and strncpy for those reasons.

We have tooling that _bans_ the use of these functions in our code. Trying to introduce use of one of them in a pull request causes CI jobs to turn red and alert the author about their mistake.

Buffer functions
----------------

Years ago we found ourselves having done several mistakes in code that were dealing with different dynamic buffers. We had too many separate implementations working on dynamically growing memory areas. We unified this handling with a new set of internal help functions for growing buffers and now made sure we only use these. This drastically reduces the need for realloc(), which helps us avoid mistakes related to that function.

Each dynamic buffer also has its own maximum size set, which in its simplicity also helps catching mistakes. In the current libcurl code, we have 80 something different _dynamic buffers_.

Parsing functions
-----------------

I mentioned how we don’t like sscanf. It is a powerful function for parsing, but it often ends up parsing more than what the user wants (for example more than one space even if only one should be accepted) and it has weak (non-existing) handling of integer overflows. Lastly, it steers users into copying parsed results around unnecessarily, leading to superfluous uses of local stack buffers or short-lived heap allocations.

Instead we introduced another set of helper functions for string parsing, and over time we switch all parser code in curl over to using this set. It makes it easier to write strict parsers that only match exactly what we want them to match, avoid extra copies/mallocs and it does strict integer overflow and boundary checks better.

Monitor memory function use
---------------------------

Memory problems often involve a dynamic memory allocation followed by a copy of data into the allocated memory area. Or perhaps, if the allocation and the copy are both done correctly there is no problem but if either of them are wrong things can go bad. Therefor we aim toward minimizing that pattern. We rather favor strdup and memory duplication that allocates and copies data in the same call – or uses of the helper functions that may do these things behind their APIs. We run a daily updated graph in the curl dashboard that shows _memory function call density_ in curl. Ideally, this plot will keep falling over time.

![Image 1](https://daniel.haxx.se/blog/wp-content/uploads/2025/04/Screenshot-2025-04-06-at-13-01-34-curl-Project-status-dashboard.png)

Memory function call density in curl production code over time

It can perhaps also be added that we avoid superfluous memory allocations, in particular in hot paths. A large download does not need any more allocations than a small one.

Double-check multiplications
----------------------------

Integer overflows is another area for concern. Every arithmetic operation done needs to be done with a certainty that it does not overflow. This is unfortunately still mostly a manual labor, left for human reviews to detect.

64-bit support guaranteed
-------------------------

In early 2023 we dropped support for building curl on systems without a functional 64-bit integer type. This simplifies a lot of code and logic. Integer overflows are less likely to trigger and there is no risk that authors accidentally believe they do 64-bit arithmetic while it could end up being 32-bit in some rare builds like could happen in the past. Overflows and mistakes can still happen if using the wrong type of course.

Maximum string length
---------------------

To help us avoid mistakes on strings, in particular with integer overflows, but also with other logic, we have a general check of all string inputs to the library: they do not accept strings longer than a set limit. We deem that any string set that is longer is either just a blatant mistake or some kind of attempt (attack?) to trigger something weird inside the library. We return error on such calls. This maximum limit is right now eight megabytes, but we might adjust this in the future as the world and curl develop.

keep master golden
------------------

At no point in time is it allowed to break master. We only merge code into master that we believe is clean, fine and runs perfect. This still fails at time, but then we do our best at addressing the situation as quickly as possible.

Always check for and act on errors
----------------------------------

In curl we always check for errors and we bail out _without leaking any memory_ if (when!) they happen. This includes all memory operations, I/O, file operations and more. All calls.

Some developers are used to modern operating systems basically not being able to return error for some of those, but curl runs in many environments with varying behaviors. Also, a system library cannot _exit_ or _abort_ on errors, it needs to let the application take that decision.

APIs and ABIs
-------------

Every function and interface that is publicly accessible must **never** be changed in a way that risks breaking the API or ABI. For this reason and to make it easy to spot the functions that need this extra precautions, we have a strict rule: public functions are prefixed with “curl\_” and no other functions use that prefix.

Everyone can do it
------------------

Thanks to the process of human reviewers, plenty of automatic tools and an elaborate and extensive test suite, everyone can (attempt to) write curl code. Assuming you know C of course. The risk that something bad would go in undetected, is roughly equal no matter who the author of the code is. The responsibility is shared.

Go ahead. You can do it!
