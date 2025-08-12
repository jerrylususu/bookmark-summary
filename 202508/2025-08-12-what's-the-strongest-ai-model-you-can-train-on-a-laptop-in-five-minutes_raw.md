Title: What's the strongest AI model you can train on a laptop in five minutes?

URL Source: https://www.seangoedecke.com/model-on-a-mbp/

Markdown Content:
What’s the strongest model I can train on my MacBook Pro in five minutes?

I’ll give the answer upfront: the best 5-minute model I could train was a ~1.8M-param GPT-style transformer trained on ~20M TinyStories tokens, reaching ~9.6 perplexity on a held-out split. Here’s an example of the output, with the prompt bolded:

> **Once upon a time**, there was a little boy named Tim. Tim had a small box that he liked to play with. He would push the box to open. One day, he found a big red ball in his yard. Tim was so happy. He picked it up and showed it to his friend, Jane. “Look at my bag! I need it!” she said. They played with the ball all day and had a great time.

OK, so it’s not _great_. But it’s not bad for five minutes!

### The challenge

I’ve been interested in this silly question for a few days. It’s a silly question for two reasons. First, anyone who can afford a MacBook can afford to rent half an hour on a H100 and train a model that’s several orders of magnitude more powerful. Second, if you were forced to train on a weaker device like a laptop, there’s no reason to limit yourself to five minutes (and no reason to think it would even be possible to train a strong model in that time).

Other training challenges like [BabyLM](https://arxiv.org/html/2412.05149v1#S6) restrict the training data, which makes sense - some domains might have very little data, so it’s useful to know how you can most effectively train a model when data is scarce. It’s also a popular research goal to try and train the smallest strong model, which also makes sense, since you can run small models on phones and portable devices. But I can use as much training data as I want, and as large of a model as I want. My main limitation is _time_.

In five minutes, you just can’t push that many tokens through a model. That means that large models are out of the question, since it takes longer per-token to train a larger model. Better to train a 1M param model on 4M tokens than a 1B param model on 4,000 tokens. But of course you can’t go too small. In five minutes I can move a _lot_ of tokens through a tiny 10k param model, but that model is just not large enough to learn English grammar. The training loss plateaus in the first thirty seconds and doesn’t move after that, and the model just outputs gibberish.

### Pushing more tokens-per-second

My first goal was to figure out what performance optimizations would actually be helpful at this tiny scale. My first textbook GPT-2-style transformer trained at ~3000 tokens per second (using Apple’s MPS). Interestingly, math-based optimizations either slowed me down or had no meaningful effect: using `torch.compile` on the model, switching to `float16`, and so on.

I tried [gradient accumulation](https://huggingface.co/docs/accelerate/en/usage_guides/gradient_accumulation) - updating model weights in multiple batches - on the principle that I was also memory-constrained, but as you might expect it slowed me down by an order of magnitude. It turns out that the biggest bottleneck for training on a MacBook is just “launches” (i.e. telling the GPU to go and do something). The kind of model you can train on a laptop should be able to run the weight-updating step in-memory.

Interestingly, switching from PyTorch to MLX didn’t meaningfully improve performance. I was kind of hoping for a 2x boost, but I didn’t get one. So overall, my recommendations for speed are: use MPS (obviously), don’t worry about compiling or quantizing, don’t do gradient accumulation, and pick the smallest possible model.

### Choosing the right dataset

If you only have around ten million tokens to train on, what dataset do you pull them from? That’s around 50MB of text data: nowhere near enough to be a representative sample of all English text. If 10MB of that data is Shakespeare, and another 10MB of it is physics textbooks, and so on, there just won’t be enough consistent patterns for the model.

I started with a dataset pulled from the [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Simple_English_Wikipedia), which seemed sensible: using straightforward grammar and vocabulary means less for the model to learn. This worked okay, but there was another problem. Here’s an example of the output I got (bolded text is my prompt):

> **Paris, France is a city** in North Carolina. It is the capital of North Carolina, which is officially major people in Bhugh and Pennhy. The American Council Mastlandan, is the city of Retrea. There are different islands, and the city of Hawkeler: Law is the most famous city in The Confederate. The country is Guate.

I think this is kind of impressive for five minutes of training. It knows that a city is in some place, and that a city can also be a capital of that same place. It degrades a bit after that, but the English grammar is correct and the text it generates is still about cities and countries. However, it’s clearly not generating coherent _content_, because it’s obsessed with proper nouns. Every sentence is about Noun X being in Noun Y. That’s the downside of training a model on an encyclopaedia: it’s hard to produce impressive content when you’re reciting a list of made-up facts.

Like most small-model experiments, I ended up using [TinyStories](https://arxiv.org/abs/2305.07759): a synthetic dataset of one-paragraph short stories, written at a 4-year-old reading level. This has a lot of advantages for training small language models. The stories are all coherent, with cause-and-effect and even usually a moral. There are very few proper nouns for the model to remember, and the language is even simpler than Simple English Wikipedia. The TinyStories paper shows that you can train a 1M language model to produce stories like this pretty well (although they didn’t do it in five minutes). That size model is definitely small enough to train on my laptop!

### Tokenization

A note on tokenization. I didn’t include the time spent training the tokenizer in my five-minute budget, but for a model this size it really doesn’t matter. No matter how carefully you optimize, you simply can’t push more than a few hundred megabytes of data through the training process in a five-minute window, so as long as you don’t do anything silly - like tokenizing the entire TinyStories dataset ahead of time, even though you’re only going to use a fraction - tokenization takes a handful of seconds.

For this reason, I didn’t spend a lot of time optimizing the tokenization step. I could have tried training on raw characters instead of multi-byte tokens, for instance, but multi-byte tokens are very likely easier for a model to learn.

### Architecture

What kind of model architecture works the best for a five-minute training run? I tried a bunch of different things, more or less at random.

#### Transformers and LSTMs

The obvious choice for a model architecture is a GPT-2 style transformer. It’s simple to implement, very well-supported, and works at low parameter counts. I didn’t bother trying a mixture-of-experts - it seemed silly doing that for a 1M parameter model. I didn’t use any dropout, since I wasn’t worried about overfitting and I would have been happy to see any kind of fitting at all.

I spent most of my time tweaking transformer hyperparameters (though as you’ll see I did try some other types of model). In terms of the actual model structure, I found that [SwiGLU](https://medium.com/@s_boudefel/exploring-swiglu-the-activation-function-powering-modern-llms-9697f88221e7) made a noticeable difference, and that I had the best results from two or three layer models. I tried a bunch of different learning rates and anything around 0.001 to 0.002 seemed good enough: pretty high, but when you’re racing to converge in five minutes that’s what you want. I also experimented with curriculum learning - where you start with smaller sequences and up the size as the model learns simpler patterns - but as you might expect five minutes was too short to really make it worthwhile. In terms of attention, I tried both with RoPE and with learned positional embeddings, and positional embeddings seemed noticeably better.

I also tried training a few LSTM (long short-term memory) models of around the same size, but didn’t see great results. It was pretty similar to my transformer experiments - as you’d expect - but the perplexity didn’t get quite as low as transformers of the same size.

### Diffusion

Just for the hell of it I trained a few small language diffusion models with D3PM. Diffusion language models [are hard](https://www.seangoedecke.com/limitations-of-text-diffusion-models) because language tokens are discrete, unlike pixel values in an image, so any amount of noise can turn a valid token into an invalid one. D3PM attempts to solve this problem by applying “structured” noise (e.g. replacing a token with a `[MASK]` token or a different token).

I had absolutely no success with this approach. Here’s an example of the kind of output I got:

> upon made The and a Now Tom wore.” and boy.”, see my small burn Max’. from day mouth a. saw. brought pink blew very was b she box a, Max day a and clothes Lily Max Spot put flew. yellow ” rece They ma

As you can see, it’s just random tokens. The de-noising process hasn’t produced any kind of meaningful structure at all. I didn’t expect this to be competitive - intuitively, learning to construct a sentence one randomly-placed word at a time is more difficult than learning to construct it in-order - but I’m still a little surprised it was this bad. Transformers and LSTMs were producing grammatically-plausible output after the first minute of training.

#### Model size

Finally, the most important question: how big a model can you usefully train in five minutes? I tried a bunch of different sizes[1](https://www.seangoedecke.com/model-on-a-mbp/#fn-1):

[![Image 1: models](https://www.seangoedecke.com/static/24d64b5a3307cf5e8100129eac1eb532/fcda8/models.png)](https://www.seangoedecke.com/static/24d64b5a3307cf5e8100129eac1eb532/5496c/models.png)

You can see that the sweet spot is around 2M parameters: any larger and the model is too slow to converge in five minutes, any smaller and it stops improving at all after the first minute (presumably because there aren’t enough parameters to encode the patterns in the training data).

Interestingly, this more or less coincides with the well-known Chinchilla [scaling laws](https://arxiv.org/pdf/2203.15556) paper, which says your optimal model size is your total number of training tokens divided by 20[2](https://www.seangoedecke.com/model-on-a-mbp/#fn-2). For this challenge, the number of training tokens also depends on the model size (because you can push more tokens through a smaller model in five minutes). For a 2.6M param model, I can train at 56k tokens per second, which over five minutes works out to an ideal model size of 0.84M: so the Chinchilla model predicts that it’s overkill, which matches my experience. For a 1M model, I can train at 100k tokens per second, which works out to an ideal model size of 1.5M - much closer to optimal, and indeed my results are better. I haven’t done the maths to work out the exact optimal size where my tokens-per-second matches the actual model size, but it’s clearly somewhere between 1M and 1.5M parameters.

It was cool to see well-known real scaling laws apply to this challenge!

### Final thoughts

It was a lot of fun doing this. I learned a lot about training very small models for very short amounts of time. I tried to understand every line of code I wrote (and have previously written transformers [from scratch](https://www.seangoedecke.com/porting-and-hacking-llama2)), but I definitely would not have tried things like the diffusion models without LLM assistance.

I don’t think this challenge is particularly useful for training strong models in general. Most of the interesting behaviour happens after the first five minutes of training. But I was still pleasantly surprised at how easily I was able to train a broadly-coherent storytelling model. As architectures (and laptop GPUs) improve, I wonder what kind of models we will eventually be able to train in five minutes.

* * *

1.   Not pictured is a 8M transformer I trained that had perplexity so bad that it made the rest of the dots hard to read. Also not pictured are the diffusion models, because (a) they sucked and (b) perplexity isn’t easily comparable between them and transformers/LSTMs.

[↩](https://www.seangoedecke.com/model-on-a-mbp/#fnref-1)
2.   Section 3.4, table 3.

[↩](https://www.seangoedecke.com/model-on-a-mbp/#fnref-2)