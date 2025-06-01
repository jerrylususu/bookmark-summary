Title: Why DeepSeek is cheap at scale but expensive to run locally

URL Source: https://www.seangoedecke.com/inference-batching-and-deepseek/

Markdown Content:
Why is DeepSeek-V3 supposedly fast and cheap to serve at scale, but too slow and expensive to run locally? Why are some AI models slow to respond but fast once they get going?

AI inference providers often talk about a fundamental tradeoff between _throughput_ and _latency_: for any given model, you can either serve it at high-throughput high-latency, or low-throughput low-latency. In fact, some models are so naturally GPU-inefficient that in practice they must be served at high-latency to have any workable throughput at all (for instance, DeepSeek-V3).

This tradeoff comes from the **batch size** the inference provider chooses for the model: not batching inference inside an individual request[1](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-1), but batching inference across tens or hundreds of concurrent user requests. It’s a peculiar feature of transformer-based LLMs that computing a batch of completions at the same time is almost as fast as computing a single completion. Why is that?

### What is batch inference?

GPUs are good at doing big matrix multiplications (GEMMs, or “general matrix multiplications”). Say you have a single token that you want to pass through a model (i.e. by multiplying against all its weights - other architecture details aren’t relevant). You express that as a vector that matches the dimension (or hidden size) of the model (i.e. 1 x the width of its big weights matrices) and multiply it through. That’s 1 GEMM. But if you want to pass ten tokens through in a batch, that’s still only one GEMM, because you can stack the tokens into one matrix (10 x the model dimension). That’s a _lot_ faster than doing ten slightly smaller GEMMs. So an inference server implementation might look something like this:

1.   A request comes in with a prompt
2.   That prompt is pre-filled (passed through attention - we’ll see later how that can be batched as well[2](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-2)), forming a KV cache and a token-sized matrix (1 x model-size) that will eventually become the predicted token[3](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-3)
3.   That token-sized matrix goes into a queue
4.   A GPU server pulls batches (e.g. of 128) off that queue, stacks them up into a 128 x model-size matrix, and multiplies them through the feed-forward model weights
5.   The end result is then split into 128 separate tokens
6.   The one for the original request is streamed back to the user
7.   Assuming that token isn’t an end-of-sequence token, return to step 2 to continue generating the next token in the response

Note that _the server decides_ how big a batch size to pull. It’s a tradeoff between throughput and latency. If you do no batching and just process tokens one by one, no user ever waits in a queue (step 3 above), so latency is low (assuming you have enough GPUs). However, if you do a lot of batching, latency is high because users will be waiting until the batch size fills up, but throughput will be much higher because the GPUs are being used more efficiently.

Why are GPUs faster at multiplying large matrices once than small matrices many times? Two reasons. First, there’s some overhead involved in issuing each command to the GPU, and one big multiplication can be launched with a single command. Second, each new GPU command involves fetching weights from memory, which can be expensive for large weights. If you run lots of small GEMMs, you can end up spending most of your time shipping weights in and out of memory instead of computing.

### Why are some models tuned for high batch sizes?

Typically an inference server will have a “collection window” where user requests come in and are queued. Chat servers typically aim for 5-10ms, but very high-batch backends might go as wide as 200ms. If a new request comes in at the start of the window, it might wait the entire window duration before being processed[4](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-4). When the window closes, all the queued requests are batched up (i.e. all the 1xmodel-size matrices are concatenated into a single 128xmodel-size matrix) and that batch is sent through the pipeline. Running a batch like this is sometimes called a “tick”.

As the explanation above suggests, you can run any model at any batch size. There’s nothing inherently about the batching process that would rule out some types of model. However, it is possible to build a model so GPU-inefficiently that it effectively _needs_ batching in order to be practical.

#### Why mixture of experts requires higher batch sizes

For instance, take a mixture-of-experts model (like DeepSeek-V3 or supposedly the original GPT-4). You can get a strong model by training it to have hundreds and hundreds of “experts”: separate blocks of feed-forward weights, from which a routing layer picks a subset that’s used on each token. But a model like this is really GPU-inefficient. We can see why: GPUs want to do a small number of really big matrix multiplications, but if you have many experts you’re forced into many small multiplications. Unless you do your inference in batches, that’s going to mean low throughput.

Let’s think through how a “collection window” of 5ms and 200ms would perform for a large mixture-of-experts model. Suppose you pick up ten user requests in that 5ms window. If you have many experts, some experts might end up only running against one or two tokens (i.e. the batch size _for each expert_ will be much lower than the total set of requests you’ve picked up in your window). If, however, you wait for 200ms and pick up 4000 user requests, you are much more likely to saturate all your experts. At the cost of some latency, you’re making sure that your GEMMs are large and your GPUs are constantly utilized at their maximum capacity.

#### Why large pipelines require high batch sizes to avoid pipeline bubbles

For large models, it can be a challenge to keep the GPUs active at all. Large models typically have many transformer layers: i.e. hundreds of matrices of weights that make up the feed-forward network. The only way to do fast inference here is to _pipeline_ those layers by having one GPU handle the first ten layers, another handle the next ten, and so on. Otherwise you just won’t be able to fit all the weights in a single GPU’s memory, so you’ll spend a ton of time swapping weights in and out of memory and it’ll end up being really slow. During inference, each token (typically in a “micro batch” of a few tens of tokens each) passes sequentially through that pipeline of GPUs.

How efficient your pipeline is depends on the number of layers you have and the size of your collection window. When you’re processing the tokens in a window during a “tick”, you’ll get some idle GPUs at the start (because GPUs in later layers won’t have anything to work on yet) and some more idle GPUs at the end (when there’s no more tokens in the queue, GPUs in early layers will have to wait for the next “tick”). These periods of idleness are sometimes called “warmup” and “drain”. If you have many small windows, you’re going to spend more GPU time in warmup and drain than if you have fewer large windows. By picking your window size, you’re thus directly trading off between throughput and latency.

If you have a ton of layers and your collection window is really short, you might sometimes end up with fewer tokens to process than layers. This is called a “pipeline bubble” - in effect the “drain” stage starts earlier than usual. You can’t eliminate warmup and drain (for reasons discussed below, inference has to operate in sequential “ticks”), but you can eliminate pipeline bubbles by making your collection window long enough. Pipeline bubbles can be absolutely brutal for model throughput, so inference providers always set their windows wide enough to avoid them. That adds noticeable latency for models with many layers.

#### Can’t you just keep the queue full?

Why couldn’t inference providers eliminate warmup and drain entirely by keeping the GPU queue full of tokens? In other words, couldn’t you do away with ticks altogether and just keep the token micro-batches flowing? Of course each user’s inference has to be sequential (since you can’t start generating the next token until the current token is done), but large inference providers should have enough concurrent traffic to keep the queue full of separate user requests.

I’ll confess I struggle to see why this shouldn’t be possible in theory. As far as I can tell the practical barrier is how the _attention_ step is batched: if you want to batch up attention GEMMs, they need to all be the same shape (i.e. the same number of prior tokens in the sequence). So you have to run groups of the same shape at the same time, instead of being able to just maintain a single queue. There’s at least [some public research](https://arxiv.org/abs/2403.02310) on this front, but I wouldn’t be surprised if there were more clever tricks for doing this that I haven’t seen.

Another idea: if you need ticks for the attention step, why not just have a tick-based attention inference system and a more efficient continuous system for the FFN? As I understand it, the reason is _memory overhead_:

1.   Since the attention output is needed for the FFN, you’d need to have some place in-memory to park it while it waits for its slot in the FFN queue, which would quickly become too expensive.
2.   Modern inference stacks are able to combine the attention and FFN step into a couple of large GEMMs in a single “operation”. If you’re doing these on different GPUs, you have to run different operations and shuttle the weights in and out of memory.

### Summary

*   GPUs are most efficient on _large_ GEMMs, so stacking many tokens into a single matrix multiply gives far higher token throughput than processing them one-by-one
*   During decoding, attention can only be batched for tokens at the **same step**, forcing schedulers to run in short “ticks”. How many tokens you pack into a single “tick” (i.e. how long you wait to collect tokens) is your batch size

    *   These are tokens _from different users_. You can’t batch tokens from the same user because you need previous tokens to generate the next one, so batching requires a high volume of traffic from different users

*   Bigger batches raise latency because user tokens might be waiting up to 200ms before the batch is full enough to run, but they boost throughput by allowing larger (and thus more efficient) GEMMs in the feed-forward step
*   Models with many layers (e.g. long pipelines) need larger batches to avoid **pipeline bubbles** (by ensuring each tick contains more batches than pipeline steps) 
*   Mixture-of-Experts models need to be served with high-latency to be efficient: each expert sees only the tokens routed to it, so you need larger global batches to keep every expert busy. 
*   Inference providers pick a batch size/window that clears pipeline bubbles and saturates experts. High batch sizes buy you more throughput at the cost of higher latency as tokens wait to fill up the tick
*   Some models (like DeepSeek’s) that are mixture-of-experts with many layers thus _require_ large batch sizes and high latency, otherwise throughput drops off a cliff. That’s why it’s commonly said that you can’t easily run DeepSeek for personal use: because with a single user running one inference at a time, it runs at very low efficiency/throughput
*   The fact that OpenAI and Anthropic’s models are quick to respond suggests that either:

    *   Their models have a more efficient architecture (non-MoE, fewer layers), or
    *   OpenAI/Anthropic have some very clever tricks for serving inference, or
    *   they’re paying through the nose for way more GPUs than they strictly need

[1](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-1) One commonly-observed strength of transformers is that they can batch _prefill_ within a single user request. When you pass them a long prompt, they can process that prompt all at once because of how the attention mechanism works. Previous recurrent models had to go token-by-token, which was much slower (because it involved many more GEMMs). **This has nothing to do with the kind of batching I’m talking about in this post**. I’m talking about how you can efficiently batch _inference_ across many different user requests once the prefilling is complete.

[2](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-2) This can also be batched, so long as you’re only batching attention operations with the same number of tokens in the sequence (i.e. every sequence predicting the fourth token can be batched together). Otherwise the size of the KV cache matrices are different, so you can’t easily combine them into a single batch. More on that later.

[3](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-3) Technically it’s not a token being generated, but the “logits” (a probability distribution across all possible tokens). I’ll say “token” here and later on to keep it simpler.

[4](https://www.seangoedecke.com/inference-batching-and-deepseek/#fn-4) Note that in practice modern inference stacks will use “continuous batching”, where a batch is sent off as soon as it’s full instead of waiting for the entire length of the fixed time window. However, the inference is still done in batches, to the core tradeoff between throughput and latency is the same.

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

June 1, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/), [explainers](https://www.seangoedecke.com/tags/explainers/), [deepseek](https://www.seangoedecke.com/tags/deepseek/)

* * *
