Title: AI interpretability is further along than I thought

URL Source: https://www.seangoedecke.com/ai-interpretability/

Markdown Content:
It’s common to call AI language models “black boxes”. Unlike normal human-written programs, which we can examine line-by-line to see what they’re doing, AI models are _grown_. AI models make decisions based on the interactions of billions of their weights. We can list those interactions, but that doesn’t add up to an explanation for why the model did what it did, any more than “here’s the billion neurons that fired” would explain human decisions. That’s what makes them “black boxes”: we can see what they _do_ on the outside, but we can’t usefully look inside. Or can we?

As it turns out, we can say a surprising amount about how models think.

### Why interpretability matters

A lot of money and effort has gone into looking inside AI models in the last few years. It might not be immediately obvious why. Wouldn’t AI labs be incentivized to spend their limited money and compute on making the models smarter? There are a few reasons for that.

First, AI labs don’t just want to make smart models. They want to make _useful_ and _safe_ models. If you make the world’s smartest model, but half the time it doesn’t answer questions or it just lies for the fun of it, you haven’t made a model you can release. So some level of interpretability is necessary to confidently answer questions like “is this model safe?” and “does this model answer questions correctly?”

Second, AI labs are disproportionately full of the kind of people who think AI is going to take over the world (because those people are much more likely to go and work for AI labs). For those people, the question of “is this model safe?” is an _existential question_: getting it wrong dooms the entire human race. So for those people, interpretability is a higher priority than capability. It’s no surprise that Anthropic - the most AGI-pilled frontier lab - has done the most useful public work in interpretability.

Third, there’s good reason to believe that understanding models helps to make them more capable. A trained base model contains multitudes: it is good at predicting the next sequence of tokens in a huge variety of situations, including when it’s completing tokens from someone who isn’t very smart. Much of the training data is just regular text written by regular humans, not experts or geniuses. This is why a lot of system prompts start with “you are an expert” or “you are the world’s best” - they’re trying to guide the model away from “normal human” roleplay and into the part of its latent space that’s the smartest. If you can identify how the model ends up in one part of that spectrum, you can more effectively guide it towards the smarter end. In theory, you could substantially boost the performance of existing models.

### Features and neurons

The fundamental concept in interpretability is the _feature_. You can think of a feature as a set of neurons that fire at the same time when the model is engaged with some particular concept (e.g. if a set of neurons fires only when talking about dogs we might call those the “dog feature”).

What does it mean for a neuron to fire, in the context of a language model? Simplifying a lot: a model represents user input as an array of numbers (say, 100[1](https://www.seangoedecke.com/ai-interpretability/#fn-1)), then multiplies that array through a series of large weights matrices (say, of size 100x100). So as you’re doing that, after each matrix multiplication, you have an array of 100 numbers that will get multiplied through the next matrix (eventually becoming the final predicted token). Each element of each of those arrays is a “neuron”, and if the value is above some number (say, 0) we can say that the neuron has “fired”.

### Superposition

Is interpretability as simple as looking at all of the neurons and keeping track of which ones light up when you talk about which subjects? Unfortunately not. In 2022, Anthropic[2](https://www.seangoedecke.com/ai-interpretability/#fn-2) released a [paper](https://transformer-circuits.pub/2022/toy_model/index.html) showing that models engage in _superposition_: in other words, they can handle more features than they have individual neurons. The same individual neuron might fire for a whole host of different features (math, the front of cars, human feet). The technical word for this is “polysemanticity”, which just means “meaning many things”.

This makes a lot of intuitive sense, when you think about it. Even the largest models can obviously talk about more topics than they have neurons, so they must be somehow internally representing topics in a more compressed way than “one neuron per feature”.

### Identifying features with sparse autoencoders

How do you figure out which features a a model knows about? Probably the most impactful AI interpretability paper was [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html), which figured out how to pull out individual features from these large, highly-compressed language models. The rough approach is to train a separate model - a “sparse autoencoder” - that is trained to predict features based on neuron activations:

1.   Take a ton of normal model text training data and feed it through your language model, recording the neuron activations at some set layer[3](https://www.seangoedecke.com/ai-interpretability/#fn-3)
2.   Then use that dataset of “text plus neuron activation” pairs to train your sparse autoencoder
3.   What you end up with is a list of repeated neuron patterns and the texts that are associated with them
4.   Get a human labeler or an assistant LLM to review each group of text and assign a feature label to it

This is the first AI interpretability approach that has had real, tangible consequences for working with models. You can see the concepts that the model is using to think. And once you see them, you can change them. Anthropic showed that by boosting or dampening a particular feature (e.g. by artificially lowering or raising the values of the neurons at that layer) you could change the model behavior in predictable ways.

The best example of this was [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude). If you never got to try this, it was an amazing demonstration of the power of feature boosting. Golden Gate Claude was a version of Claude 3 Sonnet that had its “Golden Gate Bridge” feature artificially boosted. The result was a model that would not stop talking about the Golden Gate Bridge: it would use it for every analogy, suggest it for every example, and sometimes just segue into talking about it.

Golden Gate Claude (and feature-boosting in general) is why I think AI interpretability has such potential. It’s a common prompting trick to reference a human paragon: “write this code like John Carmack”, or “write this email like Patrick McKenzie”. Imagine being able to boost the “John Carmack” group of features by selecting a checkbox in your chat UI!

### Circuits and replacement models

So far we’ve got some (pretty rough) tools for identifying what concepts a model might be thinking about. But that doesn’t tell you _what a model is thinking_, in the same way that “I’m thinking about cars” doesn’t tell you anything about the content of those thoughts. To figure that out, you have to look at the _sequence_ of features between layers. If a layer of weights represents a “step” of thought, then by watching how one feature impacts subsequent features, you can get a sense of how the model is reasoning.

Anthropic’s paper [On the Biology of a LLM](https://transformer-circuits.pub/2025/attribution-graphs/biology.html), and their previous [Circuit Tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) paper, are all about doing this with **replacement models**.

The idea is to generalize the sparse auto-encoder idea to the entire original model. Sparse auto-encoders “blow up” a dense, polysemantic, superposition-y activation vector into a much larger monosemantic activation vector where each value represents a feature. Replacement models do this process for the entire original model - in theory it’s the same model, with the same knowledge and reasoning ability, but working from a much larger uncompressed representation (so much slower and less efficient). As an analogy, it’s kind of like converting a dense .mp3 sound file into a much larger (and simpler) .wav so it can be studied better.

Sequences of features in the replacement model are called **circuits**. Here’s some interesting examples:

*   When asked “what’s the capital of the state containing Dallas”, the model goes “Dallas -> Texas -> capital city -> Austin”, so you can see it “thinking through” the answer
*   When composing rhyming poetry, the model activates features corresponding to candidate rhyming words before it even starts on the line, so it can set itself up for the rhyme
*   When asked for a medical diagnosis, you can see the model going from symptoms to possible diagnoses to possible tests that might confirm them
*   Models are able to abstract concepts separate from language - i.e. the same “dog” concept fires when talking about dogs in multiple languages

### Surprising results from all of this

In one sense, we already knew all this. It wasn’t really plausible that you could get a model as smart as GPT-4 (let alone later frontier models) without some ability to internally plan or consider the relationships between concepts. But seeing it work in practice throws up some surprising results. For example:

Larger models don’t just encode more information, they abstract better. This is evidence against the “tiny reasoning model + giant context window” paradigm that Sam Altman has [suggested](https://www.reddit.com/r/singularity/comments/1l32s24/sam_altman_says_the_perfect_ai_is_a_very_tiny/) might be the perfect AI.

When models are making stuff up, you can see it in their circuits (for instance, you can see them jumping to a conclusion and then backfilling reasoning steps to justify it). If this is true, hallucinations may not be an unavoidable feature of large language models. That would be pretty surprising to me.

Also about hallucinations: models have features that seem to be about _what the model itself knows_. This doesn’t mean the model is _correct_ about this, but having the concepts available means it’s at least possible that you could eventually tweak a model to know the limits of its own knowledge.

### Summary

*   AI models are commonly understood to be black boxes, but we can actually say a surprising amount about what’s going on inside them
*   We can approximate a subset of the concepts the model is thinking in - called “features” - and how the model connects those concepts in a particular response - called “circuits”
*   Internally, models represent features as a complex combination of many individual “neurons” (intermediate weight activations), so to effectively analyze them they must be expanded into a much larger model where one feature maps to one neuron

I don’t want to overstate how much we know about AI models. The concepts and circuits we can identify are a fraction of the total processing that’s going on, and even how we label the concepts is a human guess - the model could be drawing much subtler distinctions than we realize. But as someone whose mental picture of all this was “we don’t know anything, neural networks are always black boxes”, it’s exciting to learn that we can at least peer (through a glass, darkly) into the mind of the model.

[3](https://www.seangoedecke.com/ai-interpretability/#fn-3) In theory you could record every layer in one model, but features would look different in each one, so you may as well train a different SAE per-layer.

* * *

1.   Of course this is a couple of orders of magnitude off what real frontier models would have.

[↩](https://www.seangoedecke.com/ai-interpretability/#fnref-1)
2.   I’m only going to talk about the [research](https://transformer-circuits.pub/) by Anthropic. There are other AI researchers and other papers, but it seems to me that Anthropic are doing by far the most successful work in this space.

[↩](https://www.seangoedecke.com/ai-interpretability/#fnref-2)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.
