Title: Should LLMs just treat text content as an image?

URL Source: https://www.seangoedecke.com/text-tokens-as-image-tokens/

Markdown Content:
Several days ago, DeepSeek released a new [OCR paper](https://github.com/deepseek-ai/DeepSeek-OCR/blob/main/DeepSeek_OCR_paper.pdf). OCR, or “optical character recognition”, is the process of converting an image of text - say, a scanned page of a book - into actual text content. Better OCR is obviously relevant to AI because it unlocks more text data to train language models on[1](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fn-1). But there’s a more subtle reason why really good OCR might have deep implications for AI models.

### Optical compression

According to the DeepSeek paper, you can pull out 10 text tokens from a single image token with near-100% accuracy. In other words, a model’s internal representation of an image is ten times as efficient as its internal representation of text. Does this mean that models shouldn’t consume text at all? When I paste a few paragraphs into ChatGPT, would it be more efficient to convert that into an image of text before sending it to the model? **Can we supply 10x or 20x more data to a model at inference time by supplying it as an image of text instead of text itself?**

This is called “optical compression”. It reminds me of a [funny idea](https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/) from June of this year to save money on OpenAI transcriptions: before uploading the audio, run it through ffmpeg to speed it up by 2x. The model is smart enough to still pull out the text, and with one simple trick you’ve cut your inference costs and time by half. Optical compression is the same kind of idea: before uploading a big block of text, take a screenshot of it (and optionally downscale the quality) and upload the screenshot instead.

Some people are already sort-of doing this with existing multimodal LLMs. There’s a company [selling this as a service](https://www.morphik.ai/blog/stop-parsing-docs), an [open-source](https://github.com/jolibrain/colette) project, and even a [benchmark](https://getomni.ai/blog/ocr-benchmark). It seems to work okay! Bear in mind that this is not an intended use case for existing models, so it’s plausible that it could get a lot better if AI labs start actually focusing on it.

The DeepSeek paper suggests an interesting way[2](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fn-2) to use tighter optical compression for long-form text contexts. As the context grows, you could decrease the resolution of the oldest images so they’re cheaper to store, but are also literally blurrier. The paper suggests an analogy between this and human memory, where fresh memories are quite vivid but older ones are vaguer and have less detail.

### Why would this work?

Optical compression is pretty unintuitive to many software engineers. **Why on earth would an image of text be expressible in fewer tokens than the text itself?**

In terms of raw information density, an image obviously contains more information than its equivalent text. You can test this for yourself by creating a text file, screenshotting the page, and comparing the size of the image with the size of the text file: the image is about 200x larger. Intuitively, the word “dog” only contains a single word’s worth of information, while an image of the word “dog” contains information about the font, the background and text color, kerning, margins, and so on. How, then, could it be possible that a single image token can contain ten tokens worth of text?

The first explanation is that **text tokens are discrete while image tokens are continuous**. Each model has a finite number of text tokens - say, around 50,000. Each of those tokens corresponds to an embedding of, say, 1000 floating-point numbers. Text tokens thus only occupy a scattering of single points in the space of all possible embeddings. By contrast, the embedding of an image token can be sequence of those 1000 numbers. So an image token can be far more expressive than a series of text tokens.

Another way of looking at the same intuition is that **text tokens are a really inefficient way of expressing information**. This is often obscured by the fact that text tokens are a reasonably efficient way of _sharing_ information, so long as the sender and receiver both know the list of all possible tokens. When you send a LLM a stream of tokens and it outputs the next one, you’re not passing around slices of a thousand numbers for each token - you’re passing a single integer that represents the token ID. But _inside the model_ this is expanded into a much more inefficient representation (inefficient because it encodes some amount of information about the meaning and use of the token)[3](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fn-3). So it’s not that surprising that you could do better than text tokens.

Zooming out a bit, it’s plausible to me that **processing text as images is closer to how the human brain works**. To state the obvious, humans don’t consume text as textual content; we consume it as image content (or sometimes as audio). Maybe treating text as a sub-category of image content could unlock ways of processing text that are unavailable when you’re just consuming text content. As a toy example, emoji like :) are easily-understandable as image content but require you to “already know the trick” as text content[4](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fn-4).

### Final thoughts

Of course, AI research is full of ideas that sounds promising but just don’t work that well. It sounds like you should be able to do this trick on current multimodal LLMs - particularly since many people just use them for OCR purposes anyway - but it hasn’t worked well enough to become common practice.

Could you train a new large language model on text represented as image content? It might be tricky. Training on text tokens is easy - you can simply take a string of text and ask the model to predict the next token. How do you train on an image of text?

You could break up the image into word chunks and ask the model to generate an image of the next word. But that seems to me like it’d be really slow, and tricky to check if the model was correct or not (e.g. how do you quickly break a file into per-word chunks, how do you match the next word in the image, etc). Alternatively, you could ask the model to output the next word as a token. But then you probably have to train the model on enough tokens so it knows how to manipulate text tokens. At some point you’re just training a normal LLM with no special “text as image” superpowers.

* * *

1.   AI labs are desperate for high-quality text, but only around 30% of written books have been digitized. It’s really hard to find recent data on this, but as a very rough estimate [Google Books](https://blog.google/products/search/google-books-library-project/?utm_source=chatgpt.com) had ~40M books in 2023, but Google [estimates](https://www.wired.com/2010/08/how-google-counted-the-worlds-129-million-books?utm_source=chatgpt.com) there to have been ~130M books in 2010. That comes out to 30%.

[↩](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fnref-1)
2.   See Figure 13.

[↩](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fnref-2)
3.   Not to skip too far ahead, but this is one reason to think that representing a block of text tokens in a single image might not be such a great idea.

[↩](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fnref-3)
4.   Of course current LLMs can interpret these emojis. Less-toy examples: image-based LLMs might have a better feel for paragraph breaks and headings, might be better able to take a big picture view of a single page of text, and might find it easier to “skip through” large documents by skimming the start of each paragraph. Or they might not! We won’t know until somebody tries.

[↩](https://www.seangoedecke.com/text-tokens-as-image-tokens/#fnref-4)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/text-tokens-as-image-tokens/&t=Should%20LLMs%20just%20treat%20text%20content%20as%20an%20image?).

October 21, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *