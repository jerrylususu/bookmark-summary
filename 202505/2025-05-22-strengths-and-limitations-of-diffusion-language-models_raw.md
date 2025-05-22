Title: Strengths and limitations of diffusion language models

URL Source: https://www.seangoedecke.com/limitations-of-text-diffusion-models/

Markdown Content:
Google recently released [Gemini Diffusion](https://deepmind.google/models/gemini-diffusion/), which is impressing everyone with its speed. Supposedly they even had to slow down the demo so people could see what was happening. What’s special about diffusion models that makes text generation so much faster? Should every text model be a diffusion model, going forward?

I previously wrote a simple explainer of diffusion models [here](https://www.seangoedecke.com/diffusion-models-explained). If you don’t have any intuitions about how diffusion models are different, I suggest starting with that. This post will go into more detail about how those differences affect performance and quality in model outputs.

### Why diffusion models are fast

The biggest difference between diffusion models and traditional autoregressive models (like 4o, Claude, and all current transformer-based models) is that diffusion models generate the entire output at each step. For an output like “abcd”, a autoregressive architecture will generate token-by-token: “a”, “ab”, “abc”, and finally “abcd”. A diffusion model will generate the whole thing, growing more accurate at each step: “xycz”, “aycd”, then “abcd”. This has two interesting consequences for speed:

1.   Unlike normal autoregressive models, diffusion models can generate correct parts of the final token sequence in parallel (e.g. the start and the end) during the same pass
2.   Unlike autoregressive models, diffusion models can be trained to make fewer passes (in exchange for producing a lower-quality output)

You can see the first point in the slowed-down Gemini Diffusion demo. The generation in the first frame is at least partially accurate (i.e. it’s generated a bunch of the “correct” tokens all in one go). And the second point is easy to imagine: just stop halfway through the demo and imagine that’s the output you get. Twice as fast, if you’re happy for there to be some errors in the final output.

### Fixed-length vs arbitrary length responses

The other main difference between diffusion and autoregressive models is that a diffusion model always generates a fixed-length output (say, 256 tokens)[1](https://www.seangoedecke.com/limitations-of-text-diffusion-models/#fn-1). Technically autoregressive models generate fixed length outputs as well (one token), but in practice they’re designed to generate a token sequences of varying lengths. This has implications both for speed and quality.

Diffusion models are _always_ going to be faster than autoregressive models at generating the number of tokens in their output set (or higher), for the reasons I laid out in the previous section. If a diffusion model needs to generate 512 tokens, it can do that in two chunks (24 passes) instead of needing 512 passes. **However, if you only need to generate a handful of tokens, autoregressive models might be faster.** If a diffusion model always makes 12 passes, it’s going to do twice as much work than an autoregressive model in order to generate a six-token response.

### Performance on long contexts

Because they generate output in blocks, **diffusion models are slower at ingesting long context windows**. The reason why is pretty technical. Consider how attention works in an autoregressive language model. Each token is “checked” against all previous tokens in the sequence in order to determine which previous tokens are most relevant. For instance, if the model is about to generate a name, the previous usages of that name in the sequence will all have high attention scores, because they’re being used to determine what name to generate now.

The reason this isn’t straightforwardly quadratic is the “key-value cache”: because autoregressive models generate token-by-token, attention scores for previously-generated tokens don’t have to be checked again.

Diffusion models can’t benefit from the key-value cache as easily, because the current block of tokens being generated can all change during each denoising pass, and thus can’t be cached. So diffusion models must re-calculate attention[2](https://www.seangoedecke.com/limitations-of-text-diffusion-models/#fn-2) against the entire context window for each token in the block of tokens being generated, _every denoising pass_. That adds up to many more flops than the equivalent autoregressive model would spend.

### Can diffusion models reason?

A striking recent development in autoregressive models has been the introduction of the “reasoning model”: an autoregressive model that’s been trained to produce a chain-of-thought internal monologue before producing a user-facing answer. It’s intuitive to understand why autoregressive models can do this: they think about each token they produce, so at any point they can “change their mind” and take a new position, usually by outputting a token like “But” or “Wait” or “Hold on”.

What about diffusion models? I don’t think it’s clear yet. Maybe we’ll see strong reasoning models built on diffusion. But if we don’t, it’ll be because the “changing your mind” reasoning paradigm doesn’t map nicely onto block-by-block generation. Why would a diffusion model generate a token block with “Wait, I was wrong” in the middle of it? Wouldn’t that get “edited out” in the denoising pass?

It’s possible that diffusion models could change their minds in a totally different way. When a diffusion model makes multiple passes over an output and updates tokens, is it changing its mind like a reasoning model would? How much reasoning work can be embedded into a denoising pass? There’s at least [some current research](https://arxiv.org/abs/2402.07754) exploring this direction.

One reason to be broadly skeptical about the potential of diffusion models to reason is precisely that they do much less work per-token than autoregressive models do. That’s just less space for the model to spend “thinking”. However, that’s not necessarily an integral feature of diffusion. Right now diffusion models are built for speed, but we could imagine a diffusion model built to make hundreds of thousands of passes over each generated block of tokens. A model like that could plausibly do quite a lot of reasoning.

### Yes, text diffusion models sometimes use transformers

One final technical point: it’s not completely correct to talk about “diffusion models” vs “transformer models”, like I did [here](https://www.seangoedecke.com/diffusion-models-explained). When diffusion models do that pass over the entire input, they use an internal model to predict which parts of the input are noise and should be removed. That internal model is often a transformer model, as in [Mercury Coder](https://www.inceptionlabs.ai/introducing-mercury). Unlike “normal” autoregressive transformer models, the transformer inside a diffusion model doesn’t predict token logits, but instead predicts where the noise is in the input.

However, from the perspective of an AI developer (instead of someone training models at an AI lab) this is kind of an academic distinction. The behavioral characteristics of a diffusion model are the same whether the underlying noise-predicting model is a transformer or not, because the overall diffusion architecture is different enough to dominate the differences in behavior.

### Summary

*   Diffusion models are fast because they can output multiple tokens “in parallel”, instead of going token-by-token
*   They’re easily tunable to do less editing (i.e. denoising) passes if you want more speed at the cost of quality
*   However, if you only want two or three tokens, autoregressive models will likely be faster, because a diffusion model needs to do all of its denoising passes no matter what
*   Diffusion models (at least ones using transformers) will be slower with lots of tokens in context, because outputting many tokens in parallel requires a lot of uncacheable attention work
*   It’s unclear how easy it is to build a reasoning model on top of diffusion. I bet there’s some really interesting private research going on here at AI labs. Intuitively, they won’t do chain-of-thought reasoning as nicely as autoregressive models, but there might be other approaches available to spend test-time-compute here
*   Diffusion models can and do use transformers, but it doesn’t make them operate like autoregressive models at all

* * *

1.   Of course, a diffusion model with a 256 token output size can output fewer tokens (e.g. by generating some real tokens and filling the rest of the output window with blank tokens). It can also generate more tokens by making multiple passes, each of which generates 256 tokens at a time.

[↩](https://www.seangoedecke.com/limitations-of-text-diffusion-models/#fnref-1)
2.   Here I’m assuming that the diffusion model is using a transformer as the denoising model. See a later section of this post for more detail on that.

[↩](https://www.seangoedecke.com/limitations-of-text-diffusion-models/#fnref-2)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

May 22, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/), [diffusion](https://www.seangoedecke.com/tags/diffusion/)

* * *
