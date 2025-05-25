Title: In defense of shallow technical knowledge

URL Source: https://www.seangoedecke.com/shallow-technical-knowledge/

Markdown Content:
Whenever a new piece of technology comes out (these days, mostly AI) I go to some effort to understand it. Usually I end up writing [a post](https://www.seangoedecke.com/tags/explainers) about it, so I can be confident that I do understand[1](https://www.seangoedecke.com/shallow-technical-knowledge/#fn-1).

What’s the point of doing this? Obviously my explainers about [diffusion models](https://www.seangoedecke.com/diffusion-models-explained) are _shallow_: certainly they aren’t detailed enough to do useful research on diffusion models. What’s the point, then?

In my view, **good engineering requires having reliable shallow intuitions about how things work**. You don’t need a _full understanding_ of how things work, or even a good enough understanding to work usefully in that area of the stack. But it’s still useful to try to minimize the number of technologies in your stack that are purely black boxes.

### Database indexes

Let me give an example that isn’t about AI. If you’ve done any kind of web development, you rely heavily on database indexes. For some engineers, these are black boxes. All they know is _what they do_: specifically, that if you set up the right kind of index, you can turn very slow queries into very fast ones. Sometimes they’ve learned some more rules of thumb, such that you should avoid having too many unused indexes.

Instead of learning rules of thumb, you should instead learn at a very high level what an index is: essentially a large dictionary that maps some combination of column values to the location on-disk where the full record is stored. This is not good enough to let you _implement_ a database index. But it’s very useful when you’re _using_ a database index. From that definition, you can conclude:

1.   That without an index, the database is forced to iterate over every single record in the table to satisfy your query (unless your query explicitly sets a `LIMIT` on records returned)
2.   That an index is only useful if it matches the actual query your application is making. If you index on “name plus email” and then start querying on “name plus address”, your index won’t be used and you’re back to the full table scan described in (1)
3.   That indexes massively speed up reads, but must slow down database writes and updates, because each change must also be made again in the index “dictionary”

I don’t think it’s necessarily useful to go deeper than this, unless you’re actively maintaining a database. You _could_ learn about the data structures that represent the index, about how they’re stored on-disk and in-memory, about all the tricks that go into updating them efficiently, and so on. All that stuff is very interesting. But it will very rarely inform the database migration or query you’re writing.

### Large language models

At GitHub, I work with large language models every day. I’ve worked on the Copilot side of things, and now I work on [GitHub Models](https://docs.github.com/en/github-models), where we’re actually exposing language model inference directly via our API. It has been very useful to understand what language models actually are, and I’ve spent a lot of time doing that (coding LLM inference from scratch in [Javascript and Ruby](https://www.seangoedecke.com/porting-and-hacking-llama2), for instance).

As one example of how it’s been useful, some time ago I implemented a “json output” mode for the Models [playground](https://github.com/marketplace/models). It slightly surprised me to learn that although almost every model in the catalog technically supported json output, the smaller ones did not support it _well_. Specifically, when json mode was enabled, the smaller models would sometimes get stuck and endlessly output `\n` after a few characters of valid json.

However, that behavior is actually predictable. Language models do not directly output words (or tokens). Instead, they output the entire set of probabilities over all possible tokens every time, and a simple function (called a sampler) selects a token from that set - for instance, by picking the token with the highest probability. When a model supports json output, what that typically means is that **the _sampler_ can be told to only select tokens that continue a valid json string**.

For instance, when picking the first token in the model response, the sampler will only pick from `\n`, `{` or `[`. This works great for large models or models trained on a lot of json. After a few tokens, they “get the idea” that they’re outputting json and do most of the work themselves. But small models don’t really understand json, so they might think `\n` is more likely than a token like `[`. Once they’ve outputted a couple of `\n` characters, that makes them even more likely to output more. So you end up in a loop where the model prefers to keep spitting out new lines than to try and continue the json string.

It was useful to understand the problem at this level of detail, because it let me conclude:

1.   Some small models will just never be able to reliably output json unprompted - this isn’t a bug in the setup, but a feature of the actual technology
2.   Even so, you could probably get those small models to do it by prompting them with some sample json, so it’s in the context
3.   Just because a _sampler_ supports a strategy doesn’t mean it plays nicely with the actual model

We ended up supporting json mode for most models via the API, but not giving a UI option for it except for models that were smart enough to output json effectively. That way we don’t confuse people who aren’t familiar with the points above and just want to try the LLMs out, while still letting developers have control over what they’re building with the models.

### Where do you draw the line?

If a basic understanding of how technologies work is helpful when you’re writing software on top of them, would a full understanding be even more useful? Maybe! But I think there’s a limit to how deep you can go on everything. I would rather have a basic understanding of database indexes, sharding, HTTP, pre-forking web servers, Ruby on Rails (and the twelve other things that go into normal web dev work) than to have a full understanding of only one of those things.

This question probably resolves to the familiar “go broad or go deep” discussion: should a software engineer try to have broad knowledge about many things, or to have deep knowledge about one specialty? I think it’s fine to go either route. Personally, I’ve tried to go broad in my own career, and I’d give the same advice to people who ask. I think it makes you more versatile and puts you in a better spot to react to new trends (such as AI). But if you really like databases or networking or whatever, you can certainly spend a career diving deep into that.

### Tips for building intuitions

When I’m trying to figure out how something works, I aim **to be able to explain it to a smart junior engineer**. I think this is a pretty good imaginary person to target: technical enough that you’re not starting from scratch, but not so technical that you can handwave complicated areas with jargon. For instance, if you’re trying to understand diffusion models, you shouldn’t say “oh, then the model denoises and the quality gets better”. You should put enough effort in to understand what denoising is and why doing it would improve the quality of the output.

Paradoxically, I think going too deep into the mathematics can be harmful, not helpful. In computer science papers, a complex mathematical expression often covers a simple intuition. [SwiGLU](https://paperswithcode.com/method/swiglu) is just “allow the neural net to gate parts of the network on or off”. [Rotary position embedding](https://medium.com/@mlshark/rope-a-detailed-guide-to-rotary-position-embedding-in-modern-llms-fde71785f152) is just “pack relative-position information into a token embedding by rotating it into the complex plane”. The mathematical details are less useful than understanding why binary states are useful, or what information about relative position is for.

One way to tell that you’ve done it right is if you can automatically think through a bunch of specific consequences, like the ones I listed in the two example sections. The whole point of this process is to be able to have _useful intuitions_ about these technologies (e.g. “oh, [text diffusion](https://www.seangoedecke.com/limitations-of-text-diffusion-models) would be a good fit for the AI box in Google search results because it has to be very fast and has a mostly fixed size). If you’re not having any useful intuitions, that probably reflects a flaw in your understanding.

I don’t read through a lot of secondary sources, unless they’re unusually good. I try to read at least one original paper (e.g. the classic attention paper for transformers), and I chat a lot with language models. For most of the things I’m learning, the language model already knows all the details, so I don’t have to actually supply the paper in-context - for instance, the “Attention is all you need” paper is well-known enough that all current language models can answer questions about it from scratch.

I find language models to be also very useful for checking my results. When I write one of my [explainer](https://www.seangoedecke.com/tags/explainers) posts, I always copy-paste it into a model chat (usually o3) and ask for a careful fact-check. This is great for flushing out subtle misunderstandings. For this to work well, you have to actually write down some claims. I like to write down a bunch of the “consequences” I mentioned above. Doing that makes it easy for the language model to do fact-checking. For instance, when I was learning about diffusion models, I thought that they’d be faster than autoregressive models with a full context window, but I was wrong about that. Figuring out why I was wrong helped me fix a misunderstanding I had about how caching worked with the key-value attention matrix in transformers.

### Summary

*   Building a shallow understanding about how technologies you use work is very helpful, because it lets you have useful insights (about performance, quality, when the technology is a good fit, and so on)
*   You could instead go deep on one thing if you want, but my personal advice is to go broad
*   The kind of understanding I mean is the kind you could explain to someone who is a little technical but not an expert - no mathematics, no jargon
*   Writing down your understanding is very useful because it forces you to articulate things
*   It also allows you to fact-check with a language model, which I’ve found very useful 

* * *

1.   Partly because the act of writing is useful for clarifying my thoughts, and partly because producing a written artifact means I can trivially ask o3 “hey, what did I miss?“.

[↩](https://www.seangoedecke.com/shallow-technical-knowledge/#fnref-1)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

May 25, 2025│ Tags: [good engineers](https://www.seangoedecke.com/tags/good%20engineers/)

* * *
