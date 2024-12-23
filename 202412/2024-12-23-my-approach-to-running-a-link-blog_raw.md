Title: My approach to running a link blog

URL Source: https://simonwillison.net/2024/Dec/22/link-blog/

Markdown Content:
22nd December 2024

I started running a basic link blog on this domain [back in November 2003](https://simonwillison.net/2003/Nov/24/blogmarks/)—publishing links (which I called “blogmarks”) with a title, URL, short snippet of commentary and a “via” links where appropriate.

So far I’ve published [7,607 link blog posts](https://simonwillison.net/search/?type=blogmark) and counting.

In April of this year I finally [upgraded my link blog to support Markdown](https://simonwillison.net/2024/Apr/25/blogmarks-that-use-markdown/), allowing me to expand my link blog into something with a lot more room.

The way I use my link blog has evolved substantially in the eight months since then. I’m going to describe the informal set of guidelines I’ve set myself for how I link blog, in the hope that it might encourage other people to give this a try themselves.

*   [Writing about things I’ve found](https://simonwillison.net/2024/Dec/22/link-blog/#writing-about-things-i-ve-found)
*   [Trying to add something extra](https://simonwillison.net/2024/Dec/22/link-blog/#trying-to-add-something-extra)
*   [The technology](https://simonwillison.net/2024/Dec/22/link-blog/#the-technology)
*   [More people should do this](https://simonwillison.net/2024/Dec/22/link-blog/#more-people-should-do-this)

#### Writing about things I’ve found

Back in November 2022 I wrote [What to blog about](https://simonwillison.net/2022/Nov/6/what-to-blog-about/), which started with this:

> You should start a blog. Having your own little corner of the internet is good for the soul!

The point of that article was to emphasize that blogging doesn’t have to be about unique insights. The value is in writing frequently and having something to show for it over time—worthwhile even if you don’t attract much of an audience (or any audience at all).

In that article I proposed two categories of content that are low stakes and high value: **things I learned** and **descriptions of my projects**.

I realize now that link blogging deserves to be included a third category of low stakes, high value writing. We could think of that category as **things I’ve found**.

That’s the purpose of my link blog: it’s an ongoing log of things I’ve found—effectively a combination of public bookmarks and my own thoughts and commentary on why those things are interesting.

When I first started link blogging I would often post a link with a one sentence summary of the linked content, and maybe a tiny piece of opinionated commentary.

After I upgraded my link blog to support additional markup (links, images, quotations) I decided to be more ambitious. Here are some of the things I try to do:

*   I always include **the names of the people** who created the content I a linking to, if I can figure that out. Credit is really important, and it’s also useful for myself because I can later search for someone’s name and find other interesting things they have created that I linked to in the past. If I’ve linked to someone’s work three or more times I also try to notice and upgrade them to [a dedicated tag](https://simonwillison.net/tags/).
*   I try to **add something extra**. My goal with any link blog post is that if you read both my post and the source material you’ll have an enhanced experience over if you read just the source material itself.
    *   Ideally I’d like you to take something useful away even if you don’t follow the link itself. This can be a slightly tricky balance: I don’t wont to steal attention from the authors and plagiarize their message. Generally I’ll try to find some key idea that’s worth emphasizing. Slightly cynically, I may try to capture that idea as backup against the original source vanishing from the internet. Link rot is real!
    *   My most basic version of this is trying to provide context as to why I think this particular thing is worth reading—especially important for longer content. A good recent example is my post about Anthropic’s [Building effective agents](https://simonwillison.net/2024/Dec/20/building-effective-agents/) essay the other day.
    *   I might tie it together to other similar concepts, including things I’ve written about in the past, for example linking [Prompt caching with Claude](https://simonwillison.net/2024/Aug/14/prompt-caching-with-claude/) to my coverage of [Context caching for Google Gemini](https://simonwillison.net/2024/May/14/context-caching-for-google-gemini/).
    *   If part of the material is a video, I might **quote a snippet of the transcript** (often extracted using MacWhisper) like I did in [this post about Anthropic’s Clio](https://simonwillison.net/2024/Dec/12/clio/).
    *   A lot of stuff I link to involves programming. I’ll often include a **direct link to relevant code**, using the GitHub feature where I can link to a snippet as-of a particular commit. One example is the [fetch-rss.py link in this post](https://simonwillison.net/2024/Oct/5/uv-with-github-actions-to-run-an-rss-to-readme-project/).
*   I’m liberal with **quotations**. Finding and quoting a paragraph that captures the key theme of a post is a very quick and effective way to summarize it and help people decide if it’s worth reading the whole thing. My post on [François Chollet’s o3 ARC-AGI analysis](https://simonwillison.net/2024/Dec/20/openai-o3-breakthrough/) is an example of that.
*   If the original author reads my post, I want them to **feel good about it**. I know from my own experience that often when you publish something online the silence can be deafening. Knowing that someone else read, appreciated, understood and then shared your work can be very pleasant.
*   A slightly self-involved concern I have is that I like to **prove that I’ve read it**. This is more for me than for anyone else: I don’t like to recommend something if I’ve not read that thing myself, and sticking in a detail that shows I read past the first paragraph helps keep me honest about that.
*   I’ve started leaning more into **screenshots** and even short video or audio clips. A screenshot can be considered a visual quotation—I’ll sometimes snap these from interesting frames in a YouTube video or live demo associated with the content I’m linking to. I used a screenshot of the Clay debugger in [my post about Clay](https://simonwillison.net/2024/Dec/21/clay-ui-library/).
There are a lot of great link blogs out there, but the one that has influenced me the most in how I approach my own is John Gruber’s [Daring Fireball](https://daringfireball.net/). I really like the way he mixes commentary, quotations and value-added relevant information.

#### The technology

The technology behind my link blog is probably the least interesting thing about it. It’s part of my [simonwillisonblog](https://github.com/simonw/simonwillisonblog) Django application—the main model is called [Blogmark](https://github.com/simonw/simonwillisonblog/blob/c781a1a42ab0a0237f75c7790f069bacc2d70d3f/blog/models.py#L328-L337) and it inherits from a [BaseModel](https://github.com/simonw/simonwillisonblog/blob/c781a1a42ab0a0237f75c7790f069bacc2d70d3f/blog/models.py#L172-L203) defining things like tags and draft modes that are shared across my other types of content (entries and quotations).

I use the Django Admin to create and edit entries, [configured here](https://github.com/simonw/simonwillisonblog/blob/c781a1a42ab0a0237f75c7790f069bacc2d70d3f/blog/admin.py#L73-L76).

The most cumbersome part of link blogging for me right now is images. I convert these into smaller JPEGs using a [tiny custom tool](https://tools.simonwillison.net/image-resize-quality) I built ([with Claude](https://gist.github.com/simonw/58a06a8028515999e5949a0166cd4c4f)), then upload them to my `static.simonwillison.net` S3 bucket using Transmit and drop them into my posts using a Markdown image reference. I generate a first draft of the alt text using a Claude Project with [these custom instructions](https://gist.github.com/simonw/1fa7e4e3dcb18fdeca2b3d6ac2c6c628), then usually make a few changes before including that in the markup. At some point I’ll wire together a UI that makes this process a little smoother.

That `static.simonwillison.net` buckt is then served via Cloudflare’s free tier, which means I effectively never have to think about the cost of serving up those image files.

I wrote up a TIL about [Building a blog in Django](https://til.simonwillison.net/django/building-a-blog-in-django) a while ago which describes a similar setup to the one I’m using for my link blog, including how the RSS feed works (using [Django’s syndication framework](https://docs.djangoproject.com/en/4.2/ref/contrib/syndication/)).

The most technically interesting component is my [search feature](https://simonwillison.net/search/?type=blogmark). I wrote about how that works in [Implementing faceted search with Django and PostgreSQL](https://simonwillison.net/2017/Oct/5/django-postgresql-faceted-search/)—the most recent code for that can be found in [blog/search.py](https://github.com/simonw/simonwillisonblog/blob/main/blog/search.py) on GitHub.

One of the most useful small enhancements I added was [draft mode](https://github.com/simonw/simonwillisonblog/issues/488), which lets me assign a URL to an item and preview it in my browser without publishing it to the world. This really helps when I am editing posts on my mobile phone as it gives me a reliable preview so I can check for any markup mistakes.

I also send out an approximately weekly [email newsletter](https://simonw.substack.com/) version of my blog, for people who want to subscribe in their inbox. This is a straight copy of content from my blog—Substack doesn’t have an API for this but their editor does accept copy and paste, so I have a delightful digital duct tape solution for assembling the newsletter which I described in [Semi-automating a Substack newsletter with an Observable notebook](https://simonwillison.net/2023/Apr/4/substack-observable/).

#### More people should do this

I posted this on Bluesky [last night](https://bsky.app/profile/simonwillison.net/post/3ldu6jywnos2j):

> I wish people would post more links to interesting things
> 
> I feel like Twitter and LinkedIn and Instagram and TikTok have pushed a lot of people out of the habit of doing that, by penalizing shared links in the various “algorithms”
> 
> Bluesky doesn’t have that misfeature, thankfully!
> 
> (In my ideal world everyone would get their own link blog too, but sharing links on Bluesky and Mastodon is almost as good)

Sharing interesting links with commentary is a low effort, high value way to contribute to internet life at large.
