Title: The fate of “small” open source

URL Source: https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/

Published Time: 2025-11-16T19:10:35+00:00

Markdown Content:
The fate of “small” open source | Read the Tea Leaves

===============

[Read the Tea Leaves](https://nolanlawson.com/)Software and other dark arts, by Nolan Lawson
============================================================================================

![Image 1: Search](https://s0.wp.com/wp-content/themes/pub/springloaded/images/search-btn.gif?m=1230136840i)

*   [Home](https://nolanlawson.com/)
*   [Apps](https://nolanlawson.com/apps/)
*   [Code](https://nolanlawson.com/code/)
*   [Talks](https://nolanlawson.com/talks/)
*   [About](https://nolanlawson.com/about/)

« [Why do browsers throttle JavaScript timers?](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)

16 Nov

The fate of “small” open source
-------------------------------

Posted November 16, 2025 by Nolan Lawson in [software engineering](https://nolanlawson.com/category/software-engineering/). Tagged: [LLMs](https://nolanlawson.com/tag/llms/). [6 Comments](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comments)

By far the most popular npm package I’ve ever written is [`blob-util`](https://www.npmjs.com/package/blob-util), which is ~10 years old and still gets 5+ million weekly downloads.

It’s a small collection of utilities for working with [`Blob`s](https://developer.mozilla.org/en-US/docs/Web/API/Blob) in JavaScript. I wrote it because I found that PouchDB users were endlessly confused about how to work with `Blob`s and how to convert them to strings, `ArrayBuffer`s, etc.

Given that [some 80% of developers](https://survey.stackoverflow.co/2025/ai#sentiment-and-usage) are now using AI in their regular work, `blob-util` is almost certainly the kind of thing that most developers would just happily have an LLM generate for them. Sure, you _could_ use `blob-util`, but then you’d be taking on an extra dependency, with unknown performance, maintenance, and supply-chain risks.

And sure enough, Claude will happily spit out whatever `Blob` utilities you need when prompted:

_> Write me a utility function in TypeScript to convert a Blob to an ArrayBuffer. It should return a Promise._

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19`function``blobToArrayBuffer(blob: Blob): Promise<ArrayBuffer> {`

```return``new``Promise((resolve, reject) => {`

```const reader =``new``FileReader();`

```reader.onload = () => {`

```if``(reader.result``instanceof``ArrayBuffer) {`

```resolve(reader.result);`

```}``else``{`

```reject(``new``Error(``'Failed to read Blob as ArrayBuffer'``));`

```}`

```};`

```reader.onerror = () => {`

```reject(reader.error);`

```};`

```reader.readAsArrayBuffer(blob);`

```});`

`}`

Claude’s version is pretty close to [the `blob-util` version](https://github.com/nolanlawson/blob-util/blob/99c06472d18329eda1421286692bd875d76d5c9c/src/blob-util.ts#L384-L394) (unsurprising, since it was probably trained on it!). Although it’s much more verbose, unnecessarily checking if `readAsArrayBuffer` actually gives you an `ArrayBuffer` (although this does make TypeScript happy). To be fair, it also improves on my implementation by directly `reject`ing with an error rather than the more awkward `onerror` event.

**Note:** for anyone wondering, yes Claude did suggest the new [`Blob.arrayBuffer()`](https://developer.mozilla.org/en-US/docs/Web/API/Blob/arrayBuffer) method, but it also generated the above for “older environments.”

I suppose some people would see this as progress: fewer dependencies, more robust code (even if it’s a bit more verbose), quicker turnaround time than the old “search npm, find a package, read the docs, install it” approach.

I don’t have any excessive pride in this library, and I don’t particularly care if the download numbers go up or down. But I do think something is lost with the AI approach. When I wrote `blob-util`, I took a teacher’s mentality: the README has [a cutesy and whimsical tutorial](https://www.npmjs.com/package/blob-util#tutorial) featuring Kirby, in all his blobby glory. (I had a thing for putting Nintendo characters in all my stuff at the time.)

The goal wasn’t just to give you a utility to solve your problem (although it does that) – the goal was also to _teach_ people how to use JavaScript effectively, so that you’d have an understanding of how to solve other problems in the future.

I don’t know which direction we’re going in with AI (well, ~80% of us; to the remaining holdouts, I salute you and wish you godspeed!), but I do think it’s a future where we prize instant answers over teaching and understanding. There’s less reason to use something like `blob-util`, which means there’s less reason to write it in the first place, and therefore less reason to educate people about the problem space.

Even now there’s a movement toward putting documentation in an [`llms.txt`](https://llmstxt.org/) file, so you can just point an agent at it and save your brain cells the effort of deciphering English prose. (Is this even documentation anymore? What _is_ documentation?)

Conclusion
----------

I still believe in open source, and I’m still doing it (in fits and starts). But one thing has become clear to me: the era of small, low-value libraries like `blob-util` is over. They were already on their way out thanks to Node.js and the browser taking on more and more of their functionality (see `node:glob`, `structuredClone`, etc.), but LLMs are the final nail in the coffin.

This does mean that there’s less opportunity to use these libraries as a springboard for user education (Underscore.js [also had this philosophy](https://underscorejs.org/docs/underscore-esm.html)), but maybe that’s okay. If there’s no need to find a library to, say, [group the items in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy), then maybe learning about the mechanics of such libraries is unnecessary. Many software developers will argue that asking a candidate to reverse a binary tree is pointless, since it never comes up in the day-to-day job, so maybe the same can be said for utility libraries.

I’m still trying to figure out what _kinds_ of open source are worth writing in this new era (hint: ones that an LLM can’t just spit out on command), and where education is the most lacking. My current thinking is that the most value is in bigger projects, more inventive projects, or in more niche topics not covered in an LLM’s training data. For example, I look back on my work on [`fuite`](https://github.com/nolanlawson/fuite) and various [memory-leak-hunting blog posts](https://nolanlawson.com/2022/01/05/memory-leaks-the-forgotten-side-of-web-performance/), and I’m pretty satisfied that an LLM couldn’t reproduce this, because it requires novel research and creative techniques. (Although who knows: maybe someday an agent will be able to just bang its head against Chrome heap snapshots until it finds the leak. I’ll believe it when I see it.)

There’s been a lot of hand-wringing lately about where open source fits in in a world of LLMs, but I still see people pushing the boundaries. For example, a lot of naysayers think there’s no point in writing a new JavaScript framework, since LLMs are so heavily trained on React, but then there goes the indefatigable [Dominic Gannaway](https://github.com/trueadm) writing [Ripple.js](https://www.ripplejs.com/), yet another JavaScript framework (and with [some new ideas](https://podrocket.logrocket.com/ripple-js-dominic-gannaway-logrocket-podrocket), to boot!). This is the kind of thing I like to see: humans laughing in the face of the machine, going on with their human thing.

So if there’s a conclusion to this meandering blog post (excuse my squishy human brain; I didn’t use an LLM to write this), it’s just that: yes, LLMs have made some kinds of open source obsolete, but there’s still plenty of open source left to write. I’m excited to see what kinds of novel and unexpected things you all come up with.

### _Related_

[The state of binary data in the browser](https://nolanlawson.com/2015/06/30/the-state-of-binary-data-in-the-browser/ "The state of binary data in the&nbsp;browser")June 30, 2015 In "Webapps"

[Introducing the Cordova SQLite Plugin 2](https://nolanlawson.com/2016/04/10/introducing-the-cordova-sqlite-plugin-2/ "Introducing the Cordova SQLite Plugin&nbsp;2")April 10, 2016 In "Webapps"

[Bugs I’ve filed on browsers](https://nolanlawson.com/2024/03/03/bugs-ive-filed-on-browsers/ "Bugs I&#8217;ve filed on&nbsp;browsers")March 3, 2024 In "Web"

### 6 responses to this post.

1.   ![Image 2: Ralph Haygood's avatar](https://2.gravatar.com/avatar/8835b386e2c474ab19e99505da23750db2fd6a307a418604937ffae4ac8a32c0?s=30&d=https%3A%2F%2F2.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D30&r=G) Posted by Ralph Haygood on [November 16, 2025 at 1:21 PM](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comment-238069) “but then you’d be taking on an extra dependency, with unknown performance, maintenance, and supply-chain risks”: So instead of a small JavaScript library that’s been used on millions of websites for around ten years, you’ll take on a gigantic, continually changing statistical model that has a known vulnerability of wide scope (prompt injection)? That’s preposterous. I doubt many people are klarna koding because they’re worried about performance, supply-chain risks, or, least of all, maintenance. I suspect they’re doing it because they’re afflicted with Shiny-Object Syndrome (to which programmers as a group are quite prone), they’re appallingly lazy*, or they have bosses threatening to fire them if they don’t.

I call it klarna koding rather than vibe coding because like Klarna, it’s buy now, pay later, in that if you’re doing a lot of it, technical debt is probably piling up in your codebase. You (Lawson) have provided a minor case in point: as you note, “Claude’s version is … much more verbose”, which makes it slightly harder, not easier, to understand. Unless you’re working at a fly-by-night start-up that plans to get bought or go bust before anyone has to worry about the godawful mess that is your hacked-together codebase, you should care about how easy it is for humans to understand your code, because sooner or later, somebody – like maybe you a year from now – may well need to do so, no matter what the marketing fodder from Anthropic or Anysphere may claim.

Oh well. All this means plenty of lucrative work for people willing to clean up the messes klarna koding makes:

[https://www.404media.co/the-software-engineers-paid-to-fix-vibe-coded-messes/](https://www.404media.co/the-software-engineers-paid-to-fix-vibe-coded-messes/)

See also:

[https://pivot-to-ai.com/2025/09/09/if-ai-coding-is-so-good-where-are-the-little-apps/](https://pivot-to-ai.com/2025/09/09/if-ai-coding-is-so-good-where-are-the-little-apps/)

*I’m unapologetically lazy myself, but not so lazy that I’m willing to sign my name to shitty work.

[Reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?replytocom=238069#respond)  
2.   ![Image 3: Tim McCormack's avatar](https://2.gravatar.com/avatar/5472dcc77fdaf0b551a34aa9d85f2371f22f331cf37a2044e23a22e0513d91f9?s=30&d=https%3A%2F%2F2.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D30&r=G) 

Posted by [Tim McCormack](https://www.brainonfire.net/) on [November 16, 2025 at 7:34 PM](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comment-238070) 

Holdout here. :-) Note that before LLMs, there was already the same choice: Write a utility function, or pull it in from a library. The utility functions often aren’t *that* hard to write, but just off the top of my head there were a bunch of reasons to avoid writing them that _didn’t_ involve the effort required:

    *   Smaller code base to maintain, search, and understand.
    *   Fewer unit tests to run.
    *   The library has probably shaken all the major bugs and corner cases out.
    *   Tighter boundaries for debugging (“probably don’t need to step into this function, it’s from a library”) as a result of the library probably being more solid.
    *   If it’s a popular library, then reading code that calls the utility functions becomes easier; you already know what that function call does.

There are cons as well, especially for the _really_ small or trivial libraries, but you see my point — there was value in utility libraries then, and for that reason there’s value in them now.

[Reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?replytocom=238070#respond)

3.   ![Image 4: Jim Shortz's avatar](https://2.gravatar.com/avatar/537a10a4f34d8c6c114594f78641d4d5f521f1cb48c52f5d0e68e72a9302dd32?s=30&d=https%3A%2F%2F2.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D30&r=G) Posted by Jim Shortz on [November 17, 2025 at 9:05 AM](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comment-238071) First off, thank you for contributing a valuable piece of open source to

the community. However, I have to respectfully disagree on the teaching

angle.

I have reluctantly begun to use AI LLMs, mostly for hobby projects

involving tech stacks I don’t use much (such as Node.js). When I ask it

to write something for me, I don’t just accept what it gives me. I read

through it and make sure I understand what every line is doing. If there

is a language construct or library function I’m not familiar with, I can

ask follow up questions to learn what it is.

Even though it’s just a machine (and sometimes gives me wrong answers),

I find the “conversational” style to be a great asset in helping me

learn the new thing.

In the end, I usually don’t use what it generated, or I use it as a

starting point and modify the heck out of it.

In contrast, I have taken dependencies on hundreds of open source

libraries and never look inside of them unless I’m having a problem.

[Reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?replytocom=238071#respond)  
4.   ![Image 5: Manuel Jasso's avatar](https://graph.facebook.com/v6.0/10162958391802442/picture?type=large) Posted by Manuel Jasso on [November 17, 2025 at 12:28 PM](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comment-238072) Nolan, fist of all: I miss you.

I’ve been writing code for about 40 years now, and even though this AI wave is impressive, I’ve seen enough impressive tech waves to say that in the end, only time will tell where this one will land. Everything we say today is just speculation.

I have a concern with this AI wave that you bring up: learning and understanding vs producing code.

My concern is that young programmers will grow up depending too much on something that is inherently not trustworthy, because I think trust is a human-to-human phenomenon. And yes, this is my perspective, it is not right or wrong, it is what I believe. Nobody can prove me right or wrong, only time will tell.

[Reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?replytocom=238072#respond)  
5.   ![Image 6: Unknown's avatar](https://hrbrmstrsdailydrop.files.wordpress.com/2023/12/site-logo.png?w=30) Posted by [Drop #732 (2025-11-17): Reliable Sources – hrbrmstr's Daily Drop](https://dailydrop.hrbrmstr.dev/2025/11/17/drop-732-2025-11-17-reliable-sources/) on [November 17, 2025 at 12:32 PM](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comment-238073) […] The referenced article questions the future of tiny npm packages like blob‑util in an AI‑driven development world, referencing Nolan Lawson’s post on small‑open‑source projects ([https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)) […]

[Reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?replytocom=238073#respond)  
6.   ![Image 7: Tim's avatar](https://0.gravatar.com/avatar/37102125b390509c367181cf5df2791502ea1cbfb484db8234d1392031c9a12b?s=30&d=https%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D30&r=G) Posted by Tim on [November 17, 2025 at 3:47 PM](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comment-238074) As this is the internet, I’m going to take one incidental remark you said and run off on a wild tangent.

“80% of developers are now using AI in their regular work”

80% _of StackOverflow users_. I would say that’s not terribly surprising, since people go there to find answers to small, self-contained questions, which is exactly what LLMs excel at. It’s also not at all representative of all developers.

Every non-web development field I’ve worked in (aerospace, embedded systems, databases outside of the major open-source relational and document-based, gaming, industrial, etc) is represented poorly or not at all on StackOverflow. For example, the “playstation4” tag has only 4 questions, and there is still no “playstation5” tag. Surely nobody believes that the entire global community of PlayStation developers hasn’t had a single question in 5 years!

There are also many languages/libraries which already had a great online community and never felt the need to move there. For example, the average Lisp question on StackOverflow is quite basic (there are a ton of questions about “hello world” and setting up an editor), while the serious Lisp programmers still meet elsewhere. Clearly, people still trying to figure out basic syntax in a new language for fun are going to massively over-represent LLM usage.

I think the more interesting aspect of your observation is: are the people writing the infotainment system in your car (for example) going to use an LLM to inline all their libraries, rather than take on actual dependencies? If so, how are they going to debug it later, when they don’t understand the code, and can’t upgrade it with a dependency manager? What if they write the code for your ECU this way?

We already thought it was bad that companies were mooching off volunteer maintainers (XKCD: 2347). It’s only going to get worse, because now they’re going to mooch off our source code without feeling the need to obey license terms, or even file a bug report when they discover a problem.

[Reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?replytocom=238074#respond)  

### Leave a comment [Cancel reply](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#respond)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

### Recent Posts

*   [The fate of “small” open source](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)
*   [Why do browsers throttle JavaScript timers?](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)
*   [Selfish reasons for building accessible UIs](https://nolanlawson.com/2025/06/16/selfish-reasons-for-building-accessible-uis/)
*   [AI ambivalence](https://nolanlawson.com/2025/04/02/ai-ambivalence/)
*   [Goodbye Salesforce, hello Socket](https://nolanlawson.com/2025/01/18/goodbye-salesforce-hello-socket/)

### About Me

![Image 8: Photo of Nolan Lawson, headshot](https://nolanlawson.com/wp-content/uploads/2023/01/profile_17.jpg?w=300)
I'm Nolan, a programmer from Seattle working at Socket. All opinions are my own. Photo by Cătălin Mariş.

### Archives

*   [November 2025](https://nolanlawson.com/2025/11/)(1)
*   [August 2025](https://nolanlawson.com/2025/08/)(1)
*   [June 2025](https://nolanlawson.com/2025/06/)(1)
*   [April 2025](https://nolanlawson.com/2025/04/)(1)
*   [January 2025](https://nolanlawson.com/2025/01/)(1)
*   [December 2024](https://nolanlawson.com/2024/12/)(2)
*   [October 2024](https://nolanlawson.com/2024/10/)(2)
*   [September 2024](https://nolanlawson.com/2024/09/)(3)
*   [August 2024](https://nolanlawson.com/2024/08/)(1)
*   [July 2024](https://nolanlawson.com/2024/07/)(1)
*   [March 2024](https://nolanlawson.com/2024/03/)(1)
*   [January 2024](https://nolanlawson.com/2024/01/)(1)
*   [December 2023](https://nolanlawson.com/2023/12/)(4)
*   [August 2023](https://nolanlawson.com/2023/08/)(2)
*   [January 2023](https://nolanlawson.com/2023/01/)(2)
*   [December 2022](https://nolanlawson.com/2022/12/)(1)
*   [November 2022](https://nolanlawson.com/2022/11/)(2)
*   [October 2022](https://nolanlawson.com/2022/10/)(2)
*   [June 2022](https://nolanlawson.com/2022/06/)(4)
*   [May 2022](https://nolanlawson.com/2022/05/)(3)
*   [April 2022](https://nolanlawson.com/2022/04/)(1)
*   [February 2022](https://nolanlawson.com/2022/02/)(1)
*   [January 2022](https://nolanlawson.com/2022/01/)(1)
*   [December 2021](https://nolanlawson.com/2021/12/)(3)
*   [September 2021](https://nolanlawson.com/2021/09/)(1)
*   [August 2021](https://nolanlawson.com/2021/08/)(6)
*   [February 2021](https://nolanlawson.com/2021/02/)(2)
*   [January 2021](https://nolanlawson.com/2021/01/)(2)
*   [December 2020](https://nolanlawson.com/2020/12/)(1)
*   [July 2020](https://nolanlawson.com/2020/07/)(1)
*   [June 2020](https://nolanlawson.com/2020/06/)(1)
*   [May 2020](https://nolanlawson.com/2020/05/)(2)
*   [February 2020](https://nolanlawson.com/2020/02/)(1)
*   [December 2019](https://nolanlawson.com/2019/12/)(1)
*   [November 2019](https://nolanlawson.com/2019/11/)(1)
*   [September 2019](https://nolanlawson.com/2019/09/)(1)
*   [August 2019](https://nolanlawson.com/2019/08/)(2)
*   [June 2019](https://nolanlawson.com/2019/06/)(4)
*   [May 2019](https://nolanlawson.com/2019/05/)(3)
*   [February 2019](https://nolanlawson.com/2019/02/)(2)
*   [January 2019](https://nolanlawson.com/2019/01/)(1)
*   [November 2018](https://nolanlawson.com/2018/11/)(1)
*   [September 2018](https://nolanlawson.com/2018/09/)(5)
*   [August 2018](https://nolanlawson.com/2018/08/)(1)
*   [May 2018](https://nolanlawson.com/2018/05/)(1)
*   [April 2018](https://nolanlawson.com/2018/04/)(1)
*   [March 2018](https://nolanlawson.com/2018/03/)(1)
*   [January 2018](https://nolanlawson.com/2018/01/)(1)
*   [December 2017](https://nolanlawson.com/2017/12/)(1)
*   [November 2017](https://nolanlawson.com/2017/11/)(2)
*   [October 2017](https://nolanlawson.com/2017/10/)(1)
*   [August 2017](https://nolanlawson.com/2017/08/)(1)
*   [May 2017](https://nolanlawson.com/2017/05/)(1)
*   [March 2017](https://nolanlawson.com/2017/03/)(1)
*   [January 2017](https://nolanlawson.com/2017/01/)(1)
*   [October 2016](https://nolanlawson.com/2016/10/)(1)
*   [August 2016](https://nolanlawson.com/2016/08/)(1)
*   [June 2016](https://nolanlawson.com/2016/06/)(1)
*   [April 2016](https://nolanlawson.com/2016/04/)(1)
*   [February 2016](https://nolanlawson.com/2016/02/)(2)
*   [December 2015](https://nolanlawson.com/2015/12/)(1)
*   [October 2015](https://nolanlawson.com/2015/10/)(1)
*   [September 2015](https://nolanlawson.com/2015/09/)(1)
*   [July 2015](https://nolanlawson.com/2015/07/)(1)
*   [June 2015](https://nolanlawson.com/2015/06/)(2)
*   [October 2014](https://nolanlawson.com/2014/10/)(1)
*   [September 2014](https://nolanlawson.com/2014/09/)(1)
*   [April 2014](https://nolanlawson.com/2014/04/)(1)
*   [March 2014](https://nolanlawson.com/2014/03/)(1)
*   [December 2013](https://nolanlawson.com/2013/12/)(2)
*   [November 2013](https://nolanlawson.com/2013/11/)(3)
*   [August 2013](https://nolanlawson.com/2013/08/)(1)
*   [May 2013](https://nolanlawson.com/2013/05/)(3)
*   [January 2013](https://nolanlawson.com/2013/01/)(1)
*   [December 2012](https://nolanlawson.com/2012/12/)(1)
*   [November 2012](https://nolanlawson.com/2012/11/)(1)
*   [October 2012](https://nolanlawson.com/2012/10/)(1)
*   [September 2012](https://nolanlawson.com/2012/09/)(3)
*   [June 2012](https://nolanlawson.com/2012/06/)(2)
*   [March 2012](https://nolanlawson.com/2012/03/)(3)
*   [February 2012](https://nolanlawson.com/2012/02/)(1)
*   [January 2012](https://nolanlawson.com/2012/01/)(1)
*   [November 2011](https://nolanlawson.com/2011/11/)(1)
*   [August 2011](https://nolanlawson.com/2011/08/)(1)
*   [July 2011](https://nolanlawson.com/2011/07/)(1)
*   [June 2011](https://nolanlawson.com/2011/06/)(3)
*   [May 2011](https://nolanlawson.com/2011/05/)(2)
*   [April 2011](https://nolanlawson.com/2011/04/)(4)
*   [March 2011](https://nolanlawson.com/2011/03/)(1)

### Tags

[accessibility](https://nolanlawson.com/tag/accessibility/)[alogcat](https://nolanlawson.com/tag/alogcat/)[android](https://nolanlawson.com/tag/android-2/)[android market](https://nolanlawson.com/tag/android-market/)[apple](https://nolanlawson.com/tag/apple/)[app tracker](https://nolanlawson.com/tag/app-tracker/)[benchmarking](https://nolanlawson.com/tag/benchmarking/)[blobs](https://nolanlawson.com/tag/blobs/)[boost](https://nolanlawson.com/tag/boost/)[bootstrap](https://nolanlawson.com/tag/bootstrap/)[browsers](https://nolanlawson.com/tag/browsers/)[bug reports](https://nolanlawson.com/tag/bug-reports/)[catlog](https://nolanlawson.com/tag/catlog/)[chord reader](https://nolanlawson.com/tag/chord-reader/)[code](https://nolanlawson.com/tag/code/)[contacts](https://nolanlawson.com/tag/contacts/)[continuous integration](https://nolanlawson.com/tag/continuous-integration/)[copyright](https://nolanlawson.com/tag/copyright/)[couch apps](https://nolanlawson.com/tag/couch-apps/)[couchdb](https://nolanlawson.com/tag/couchdb/)[couchdroid](https://nolanlawson.com/tag/couchdroid/)[developers](https://nolanlawson.com/tag/developers/)[development](https://nolanlawson.com/tag/development/)[emoji](https://nolanlawson.com/tag/emoji/)[grails](https://nolanlawson.com/tag/grails/)[html5](https://nolanlawson.com/tag/html5/)[indexeddb](https://nolanlawson.com/tag/indexeddb/)[information retrieval](https://nolanlawson.com/tag/information-retrieval/)[japanese name converter](https://nolanlawson.com/tag/japanese-name-converter/)[javascript](https://nolanlawson.com/tag/javascript/)[jenkins](https://nolanlawson.com/tag/jenkins/)[keepscore](https://nolanlawson.com/tag/keepscore/)[listview](https://nolanlawson.com/tag/listview/)[logcat](https://nolanlawson.com/tag/logcat/)[logviewer](https://nolanlawson.com/tag/logviewer/)[lucene](https://nolanlawson.com/tag/lucene/)[nginx](https://nolanlawson.com/tag/nginx/)[nlp](https://nolanlawson.com/tag/nlp/)[node](https://nolanlawson.com/tag/node/)[nodejs](https://nolanlawson.com/tag/nodejs/)[npm](https://nolanlawson.com/tag/npm/)[offline-first](https://nolanlawson.com/tag/offline-first/)[open source](https://nolanlawson.com/tag/open-source/)[passwords](https://nolanlawson.com/tag/passwords/)[performance](https://nolanlawson.com/tag/performance/)[pinafore](https://nolanlawson.com/tag/pinafore/)[pokedroid](https://nolanlawson.com/tag/pokedroid/)[pouchdb](https://nolanlawson.com/tag/pouchdb/)[pouchdroid](https://nolanlawson.com/tag/pouchdroid/)[query expansion](https://nolanlawson.com/tag/query-expansion/)[relatedness calculator](https://nolanlawson.com/tag/relatedness-calculator/)[relatedness coefficient](https://nolanlawson.com/tag/relatedness-coefficient/)[s3](https://nolanlawson.com/tag/s3/)[safari](https://nolanlawson.com/tag/safari/)[satire](https://nolanlawson.com/tag/satire/)[sectioned listview](https://nolanlawson.com/tag/sectioned-listview/)[security](https://nolanlawson.com/tag/security/)[semver](https://nolanlawson.com/tag/semver/)[shadow dom](https://nolanlawson.com/tag/shadow-dom/)[social media](https://nolanlawson.com/tag/social-media/)[socket.io](https://nolanlawson.com/tag/socket-io/)[software development](https://nolanlawson.com/tag/software-development/)[solr](https://nolanlawson.com/tag/solr/)[spas](https://nolanlawson.com/tag/spas/)[supersaiyanscrollview](https://nolanlawson.com/tag/supersaiyanscrollview/)[synonyms](https://nolanlawson.com/tag/synonyms/)[twitter](https://nolanlawson.com/tag/twitter/)[ui design](https://nolanlawson.com/tag/ui-design/)[ultimate crossword](https://nolanlawson.com/tag/ultimate-crossword/)[w3c](https://nolanlawson.com/tag/w3c/)[webapp](https://nolanlawson.com/tag/webapp/)[webapps](https://nolanlawson.com/tag/webapps-2/)[web platform](https://nolanlawson.com/tag/web-platform/)[web sockets](https://nolanlawson.com/tag/web-sockets/)[websql](https://nolanlawson.com/tag/websql/)

### Links

*   [Mastodon](https://toot.cafe/@nolan)
*   [GitHub](https://github.com/nolanlawson)
*   [npm](https://npmjs.com/~nolanlawson)

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

*   [Comment](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/#comments)
*   [Reblog](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)
*   [Subscribe](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)[Subscribed](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)

 

    *   [![Image 9](https://nolanlawson.com/wp-content/uploads/2025/01/favicon.png?w=32) Read the Tea Leaves](https://nolanlawson.com/)
    

Join 1,280 other subscribers

 Sign me up 

    *    Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fnolanlawson.com%252F2025%252F11%252F16%252Fthe-fate-of-small-open-source%252F) 

*   
 

    *   [![Image 10](https://nolanlawson.com/wp-content/uploads/2025/01/favicon.png?w=32) Read the Tea Leaves](https://nolanlawson.com/)
    *   [Subscribe](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)[Subscribed](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)
    *   [Sign up](https://wordpress.com/start/)
    *   [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fnolanlawson.com%252F2025%252F11%252F16%252Fthe-fate-of-small-open-source%252F)
    *   [Copy shortlink](https://wp.me/p1t8Ca-3VZ)
    *   [Report this content](https://wordpress.com/abuse/?report_url=https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)
    *   [View post in Reader](https://wordpress.com/reader/blogs/21720966/posts/15127)
    *   [Manage subscriptions](https://subscribe.wordpress.com/)
    *   [Collapse this bar](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/)

![Image 12](https://pixel.wp.com/g.gif?blog=21720966&v=wpcom&tz=-7&user_id=0&post=15127&subd=nolanwlawson&host=nolanlawson.com&ref=&rand=0.7888562540890868)