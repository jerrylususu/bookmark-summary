Title: My failed attempt to shrink all npm packages by 5%

URL Source: https://evanhahn.com/my-failed-attempt-to-shrink-all-npm-packages-by-5-percent/

Published Time: 2025-01-27T00:00:00+00:00

Markdown Content:
In 2022, I had an idea that could decrease the size of all newly-published npm packages by about 5%, and it was completely backwards compatible. This would have improved performance and reduced storage costs.

I eagerly pitched this idea to the npm maintainers, convinced it was a clear win. But after a few months, my proposal was rejected. To be clear: _I think this was the right call!_

Here’s what happened. I hope this story will be useful to others.

Technical background
--------------------

Two things to know before diving in: how npm packages are distributed, and about the Zopfli compressor.

### npm packages are just gzipped tarballs

First thing to know: npm packages are distributed as tar archives compressed with gzip. In other words, they’re just `.tar.gz` or `.tgz` files.

You can download these archives using `npm pack $PACKAGE_NAME`:

```
npm pack express && ls
# => express-4.21.2.tgz
```

If you [extract this tarball](https://evanhahn.com/mnemonic-to-remember-tar-commands/), you’ll see all of the package’s files, such as `package.json`.

### Zopfli, a gzip-compatible compressor

The second thing to know about: [Zopfli](https://github.com/google/zopfli).

Zopfli can create gzip-compatible data that’s smaller than other tools can. For example, compare the `zopfli` command to the `gzip` command:

```
gzip -9 romeo_and_juliet.txt
du -h romeo_and_juliet.txt.gz
# => 64K     romeo_and_juliet.txt.gz

zopfli romeo_and_juliet.txt
du -h romeo_and_juliet.txt.gz
# => 60K     romeo_and_juliet.txt.gz
```

As you can see, `zopfli` produces smaller files than `gzip`.

If Zopfli produces smaller sizes than gzip, why not use it everywhere? Unfortunately, Zopfli is great but it’s _much_ slower than regular gzip.

```
time gzip -9 romeo_and_juliet.txt
# => real   0m0.016s

time zopfli romeo_and_juliet.txt
# => real   0m0.462s
```

In this simple test, Zopfli is about _28 times slower_! That means it’s bad for content that changes a lot, but good for content that doesn’t.

In my opinion, Zopfli’s killer feature is that it creates files that are backwards compatible with existing decompressors. Other compression algorithms, like LZMA, can be better than gzip, but you can’t decompress their results with `gunzip` or equivalent. With Zopfli, you can!

```
cat my_file.txt
# => Hello world

lzma -c my_file.txt | gunzip -c
# => gunzip: unknown compression format

zopfli -c my_file.txt | gunzip -c
# => Hello world
```

So I wondered: if npm packages are compressed with gzip, **could npm packages be compressed better with Zopfli?** The answer is “yes”.

Proof of concept
----------------

To see if this would work, I tried it on one of my own npm packages.

I did something like this:

1.  Get the file that is published by default. I used [HumanizeDuration.js](https://www.npmjs.com/package/humanize-duration), one of my more popular packages, as a test.
    
    ```
    cd HumanizeDuration.js
    npm pack
    # ...
    # => humanize-duration-3.32.1.tgz
    ```
    
    This created `humanize-duration-3.32.1.tgz`, which was ~17 kibibytes large. I could `npm publish` this right now, but let’s try shrinking it.
    
2.  Decompress (but don’t unarchive) the file.
    
    ```
    gunzip humanize-duration-3.32.1.tgz
    ```
    
    This leaves us with an uncompressed tarball, `humanize-duration-3.32.1.tar`.
    
3.  Re-compress it with Zopfli.
    
    ```
    zopfli humanize-duration-3.32.1.tar
    ```
    
    As expected, this produced a slightly smaller file by over a kilobyte. That’s promising!
    
4.  Make sure I could still install it. I installed the tarball, and tried to use it.
    
    ```
    cd "$(mktemp -d)"
    
    npm install /path/to/recompressed/humanize-duration-3.32.1.tar.gz
    # => added 1 package in 123ms
    
    node -p 'require("humanize-duration")(1234)'
    # => 1.234 seconds
    ```
    
    It worked!
    

This saved 1114 bytes for a ~6.2% reduction. And this is completely backwards-compatible. That made sense; this is what Zopfli is supposed to do!

I also tried it on a few of my other packages. Everything seemed to work and offered a ~5% size reduction. Great!

I published one of my modules this way, and nobody complained. I later did this for [Helmet](https://helmetjs.github.io/), my [most popular module](https://evanhahn.com/lessons-learned-maintaining-a-sorta-popular-open-source-package/)—again, without issue.

This was, and still is, a minor success. This is a small optimization that saves about 2 gigabytes of bandwidth per year across all installations. I doubt many individual installs were perceptibly faster after this change…but it’s nice to do a tiny amount of work for a 5% improvement!

Now that I’d proved it’d work for my modules, I wondered: _could this be done on a wider scale?_

2022-05-27: asking for feedback
-------------------------------

Given that this worked fine for my packages, could this be done for the _entire npm registry_?

On May 27, I asked my [Signal](https://signal.org/) colleagues for feedback on an idea. Here’s what I asked (reformatted slightly):

> Here is something I would like feedback on:
> 
> npm packages are just gzipped tarballs (try it yourself with `npm pack $PACKAGE_NAME`).
> 
> Zopfli does a better job at gzipping files than `gzip -9`.
> 
> Therefore, the npm registry and developers could save bandwidth if they compressed new (or re-compressed existing) packages with Zopfli.
> 
> With React as an example:
> 
> *   The latest version of React is 81,166 bytes, compressed with the equivalent of `gzip -9`
> *   Re-compressing it with Zopfli saves 4019 bytes; about a 5% reduction
> *   React was downloaded ~562M times last year
> *   That would save ~2 TiB of bandwidth just for React
> 
> To be clear, this is completely backwards compatible as far as I understand.

I got two important pieces of feedback:

*   [Jordan Rose](https://belkadan.com/about) pointed out that decompression time could be significant. I hadn’t checked this! I ran some quick tests and found that this wasn’t an issue.
*   [Fedor Indutny](https://fosstodon.org/@indutny) pointed out that npm’s lockfile, `package-lock.json`, contains a checksum of the package file. The npm people couldn’t easily re-compress existing packages without breaking things. It would only work for newly-published files; new packages or new versions of existing ones.

Armed with that feedback, I brought the idea to the npm folks.

2022-05-29: RFC time
--------------------

I learned that the npm CLI people have [a formal proposal process](https://evanhahn.com/my-failed-attempt-to-shrink-all-npm-packages-by-5-percent/#TODO) where you write up a document and submit a patch.

I spent a few days writing and editing my proposal, [“Improving tarball compression while maintaining backwards compatibility”](https://github.com/npm/rfcs/pull/595). It was 708 words. I tried to make it sound compelling with things like this:

> Even a small savings, like 5%, would reduce the registry’s bandwidth usage by multiple terabytes. For example: React [was downloaded 561,743,096 times in 2021](https://npm-stat.com/charts.html?package=react&from=2021-01-01&to=2021-12-31). If we assume that each of these downloads shrunk from 81,166 bytes to 77,147 bytes, the registry would have saved more than 2 terabytes in bandwidth for React alone.

On May 29, I finally submitted my RFC. I was nervous!

2022-06-01: they discussed it
-----------------------------

A few days later, the npm CLI people had [a meeting where they discussed a bunch of stuff, including my RFC](https://github.com/npm/rfcs/issues/596). I wasn’t able to attend but watched the recording. Overall, they felt it was worth evaluating further but were cautious. From their notes:

> Overall sentiment is that the compression improvement is welcome but it looks like it would take a proof of concept and challenge some of the edge cases to see if there are any unintended consequences, etc

I built a [little proof of concept web app](https://evanhahn.github.io/npm-repack-with-zopfli-proof-of-concept/) that used a WebAssembly port of Zopfli to recompress npm packages and [posted about it on the RFC](https://github.com/npm/rfcs/pull/595#issuecomment-1145168973).

I attended the next meeting a couple of weeks later.

2022-06-15: the meeting
-----------------------

I attended a call on June 15.

I did the bad thing where I wasn’t really listening until it was my turn because I was thinking about what I was going to say. When it was finally my turn, I stammered.

Watching it back, I cringe a bit. I was wordy, unclear, and unconvincing. But I think I did an _okay_ job making my point: npm packages could become ~5% smaller if we could figure out how to run Zopfli at publish time.

You can [watch my mumbling in the recording](https://www.youtube.com/live/l8ob4j_KOR4?t=853), as well as the npm maintainers’ feedback.

_“Who benefits from this?”_ was probably the biggest question. It was discussed that the npm registry folks, paying storage costs, might care about this. But “literally no one’s noticed” some other recent performance improvements, so they wanted to see more data. Was this just something I thought was neat (a “performance romantic”, as one person called it), or did this solve a real problem for users?

There were also concerns about including WebAssembly, the performance implications at install time, and Zopfli licensing issues.

I was tasked with some investigation on the topics above, and I got digging.

2022-07-31: giving up
---------------------

After a bunch of thinking and feedback, what once seemed like an obviously great idea now seemed…well, less great.

On July 31, after doing a bunch of research, I posted [a comment on the RFC](https://github.com/npm/rfcs/pull/595#issuecomment-1200480148).

I wrote up some pros and cons. The pros:

*   The top 250 npm packages would shrink by about 4.5% with this change.
*   This compression would be backwards compatible, and would require no changes from anyone else.

But the cons were substantial:

*   Integrating Zopfli into the npm CLI would be difficult.
*   Publishing would be slower—in some cases, _much_ slower.
*   This wouldn’t retroactively apply to existing packages.

After this discussion and thinking about the tradeoffs, I felt that it was not worth it, and I closed my RFC.

And that was that!

Lessons learned
---------------

I learned a lot during this process.

It was a bit nerve-wracking, but I learned how to make proposals like this. I’d written internal proposals at work, but I’d never made a semi-official RFC like this before.

I also think I did a pretty bad job in my verbal communication during the meeting. Perhaps it was because I was nervous. I could have done a better job communicating about the tradeoffs—good and bad—of the proposal. And I could have been less wordy!

I also learned that things that seem like obvious wins aren’t always obvious wins, either because the motivation isn’t there or because there are trade-offs I minimized.

Overall, even though my proposal was denied, I’m glad I did this. I think I’m a better engineer for it! I hope this story was interesting and useful to you, dear reader.

(Oh, and I’m still [compressing my own modules with Zopfli](https://github.com/helmetjs/helmet/blob/632e629b08de04bbd7188934641f3535af21685d/build/build-package.ts#L341).)
