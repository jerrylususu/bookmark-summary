Title: Can small AI models think as well as large ones?

URL Source: https://www.seangoedecke.com/cognitive-core/

Markdown Content:
An AI trend that’s emerged in the last few months[1](https://www.seangoedecke.com/cognitive-core/#fn-1) is the idea of a “cognitive core”. Instead of trying to build the largest, most capable model we can, should we be trying to build a small model?

### The unreasonable effectiveness of small LLMs

In general, big models - models with higher parameter counts - are better models. Claude Opus 4 is better at everything than Claude Sonnet 4, and so on. It gives you more accurate answers, solves problems more elegantly, and can maintain coherence for longer when in an agentic tool loop. So far, the story of model development at AI labs has been producing increasingly larger and more capable models, with smaller distilled versions that are cheap and fast enough to serve at scale[2](https://www.seangoedecke.com/cognitive-core/#fn-2).

However, one surprising fact from the last few years of AI work has been how unreasonably effective small models can be. When you halve the size of a model, you don’t get a model that’s half as smart. If you do it right, you get a model that’s 90% as smart. As we learn how to make smarter big models, the smaller models get smarter too. The original GPT-3 was probably[3](https://www.seangoedecke.com/cognitive-core/#fn-3) 175B parameters. It got ~44% on the popular MMLU [benchmark](https://en.wikipedia.org/wiki/MMLU), which covers a mix of SAT-style language, mathematics, and general knowledge. Today, Gemma 3B (58 times smaller) [gets](https://llm-stats.com/) ~65% on the same benchmark.

Why can we make such good small models? One reason that might help your intuition: when you train a large model from scratch, the signal per piece of training data is very poor. You only train based on the next token in the sequence, so if the training sentence is “one plus one is five” the model is equally punished for finishing the sentence with “5” as it is for finishing it with “forty” or “sausage”. However, when you distil a small model from a large one, you aren’t training on the model token outputs but on the _logits themselves_: the full probability distribution across all possible tokens. That’s just way more information for the small model to learn from! On top of that, if it predicts “5” it won’t be punished as harshly (since presumably the big model would think “5” is pretty likely, even if it prefers “five”).

### What “cognitive core” can do

Now we can articulate why the “cognitive core” idea is so exciting. If tiny models are almost as good as big models, but they don’t have access to as many facts, couldn’t we just give a tiny model the tools it needs to go and look up facts (e.g. from the internet)? Is it possible to build a 3B parameter (or smaller!) model where all of those parameters are dedicated to knowing how to look things up and reason about them?

Right now, it is not practically possible to run a strong LLM locally. If you have multiple high-end graphics cards, you can run something that’s just below the frontier, but the best LLMs you can run on a regular phone or laptop are not powerful enough to be useful. That’s purely a function of the parameter count: you can’t run Claude Sonnet 4 on your phone because your phone simply cannot fit all of the parameters in-memory in its GPU. To run inference, your phone would be spending all its time moving weights in and out of the GPU, and you’d be waiting ~30 seconds for each token[4](https://www.seangoedecke.com/cognitive-core/#fn-4).

What are big models doing that small models aren’t? One thing they’re doing is encoding more facts about the world. It’s well-known that bigger models typically have much better recall of the facts from their training data, while small models don’t. This makes intuitive sense: the weights of a language model are a densely-encoded version of their entire training corpus, so the more weights (i.e. the more parameters) a language model has to play with, the more of that corpus it can compress and store.

But if you’re not specifically asking for those facts, it does seem like a waste to be matrix-multiplying through every single weight. When you ask “what’s the most important email in my inbox”, why are you multiplying through the weights that store the plot of Neon Genesis Evangelion, or the order of the Kings of England? Sure, sometimes you’ll be getting emails about those topics, where background knowledge would be helpful. But enriching the model with a brief summary pulled from search is much quicker and cheaper - by multiple orders of magnitude - than relying on the model to already know the relevant facts.

Imagine a language model that’s small enough to run on your phone without it heating up or draining your battery. You could run that model _all the time_ for basically free: researching topics for you, collating and summarizing your images and notifications, and so on. It would be a brand new engineering primitive - unlocking new features and capabilities that nobody has thought of yet.

### Reasons to be suspicious

Why _wouldn’t_ “cognitive core” work? What are the arguments against it? The main one is that **reasoning ability might require a lot of background knowledge**. It might turn out that we can’t create a model that’s as good as reasoning as Claude Sonnet 4 without knowing all the trivia that Claude Sonnet 4 knows, because “the ability to reason” turns out to be a complex relationship between many, many individual model weights. Humans learn reasoning techniques from concrete examples, and only develop the ability to apply those techniques more generally after applying them in practice many times. It’s possible that those examples are load-bearing: if you strip out all knowledge of those examples, the ability to use the technique goes away too.

Along the same lines, it might turn out that **reasoning ability requires many parameters**. One surprising result from Anthropic’s [AI interpretablity](https://www.seangoedecke.com/ai-interpretability) research is that larger models have better abstractions than smaller models. When you ask a small model questions about dogs, only the “dog” pattern of neurons lights up, but a large model has recognizable patterns for more abstract concepts like “animal” or “pet”. If good reasoning requires operating with broad abstractions, and you can’t fit broad abstractions into a small model, it might be impossible to produce a strong “cognitive core” model.

We might also think that **larger models will always be smarter**. Even if we could build a fairly-smart cognitive core with a 1B model, if the current state of the art much larger models are significantly smarter than that, it might not make any sense to build around the smaller cognitive core system. In the days of GPT-3.5, people were saying that GPT-3.5 on your phone would be transformative. Small models right now are stronger than GPT-3.5, but they remain mostly toys (or small components of larger systems), because for any given use case you get so much better results from hitting the Anthropic, OpenAI or Google inference APIs. This idea is kind of a [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox) for AI capabilities - as models get more capable, the demand for ever-more-capable models grows to meet supply.

### Final thoughts

Overall I’m excited to see just how strong small models can become. Of all the possible futures where AI succeeds, the grimmest one is the one where large models dominate and power is concentrated in the hands of a few giant AI labs. It would be much better if small models continue to get better at the same rate (or faster), and people are able to build all kinds of things more cheaply. And of course it’d be good news for people who worry about the environmental impact of AI.

Still, I’m skeptical that we’re ever going to get to a point where the most useful models are super-reasoners with almost no general knowledge at all. I think it’s going to be hard to disentangle “pure” reasoning ability from the web of concrete facts that are the objects of reasoning.

* * *

1.   The idea dates back to at least last year, but Sam Altman referenced it as an OpenAI goal in an [interview](https://www.reddit.com/r/singularity/comments/1l32s24/sam_altman_says_the_perfect_ai_is_a_very_tiny/) two months ago. More recently, a Andrej Karpathy [tweet](https://x.com/karpathy/status/1938626382248149433) has spurred some [discussion](https://x.com/swyx/status/1943073193083965852). And of course small on-device models are a big part of Apple’s AI strategy with the iPhone.

[↩](https://www.seangoedecke.com/cognitive-core/#fnref-1)
2.   A single large base model can spawn four or five different “sub-models” that are post-trained as assistants, or for reasoning, and so on. I wrote a lot more about this [here](https://www.seangoedecke.com/ai-lab-structure).

[↩](https://www.seangoedecke.com/cognitive-core/#fnref-2)
3.   See [here](https://papers.nips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf), section 7.3. If you believe this unsourced aside from a [Microsoft paper](https://arxiv.org/pdf/2412.19260v1) (section 5.1), Claude 3.5 Sonnet has the same parameter count!

[↩](https://www.seangoedecke.com/cognitive-core/#fnref-3)
4.   Rough estimate: you’re moving ~175GB of weights around per token, at ~3GB/s, so ~0.017 per token. Double that speed for a 4-bit quantization. Remember your phone is probably red-hot this whole time.

[↩](https://www.seangoedecke.com/cognitive-core/#fnref-4)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

July 27, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *
