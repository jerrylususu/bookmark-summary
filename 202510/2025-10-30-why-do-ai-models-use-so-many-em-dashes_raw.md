Title: Why do AI models use so many em-dashes?

URL Source: https://www.seangoedecke.com/em-dashes/

Markdown Content:
If you asked most people to name a defining feature of AI-generated writing, they’d probably say the em-dash — like this. Language models use em-dashes so much that real humans who like em-dashes have [stopped using them](https://www.reddit.com/r/OpenAI/comments/1mk62b1/comment/n7gnqpb/) out of fear of being confused with AI. It’s also surprisingly hard to prompt models to avoid em-dashes: take this [thread](https://community.openai.com/t/cannot-get-responses-to-not-include-dashes-and-em-dashes/1023216/7) from the OpenAI forums where users share their unsuccessful attempts. Given all that, it’s kind of weird that **we don’t really know why language models use the em-dash so much**.

### Explanations I don’t find convincing

One common explanation is that normal English text contains a lot of em-dashes, so it’s just learned behavior from the training data. I find this fairly unconvincing, for the reason that _everyone thinks AI uses a lot of em-dashes_. If em-dashes were as common in AI prose as human prose, they would be as unremarkable as the use of other punctuation marks.

Another explanation I’m not convinced by is that AI models like em-dashes because they’re so versatile. When the model is trying to predict the next token, an em-dash keeps its options open: it could either continue on the same point or make a brand new point. Since models are just trying to pick the next most likely token, could they just be “playing it safe” by using em-dashes? I don’t think so. First, other punctuation marks are similarly flexible. Second, I’m not sure that “playing it safe” is a good idiom for thinking about how models generate text.

Other people have [argued](https://msukhareva.substack.com/p/the-mystery-of-emdashes-part-two?) that AI models use em-dashes because model training explicitly biases for brevity, and em-dashes are very token-efficient. From what I can tell by playing with the OpenAI [tokenizer](https://platform.openai.com/tokenizer), the em-dash itself isn’t inherently more efficient, but plausibly without it you’d have to write some connective tissue like ”, therefore”. Still, I don’t buy this. Many em-dashes (e.g. the common “it’s not X - it’s Y” pattern) could simply be replaced with a comma, which is equally brief[0](https://www.seangoedecke.com/em-dashes/#fn-0). I also don’t think GPT-4o is so brevity-focused that it’s doing micro-optimizations around punctuation like this: if it wanted to use fewer tokens, it could simply waffle less[0.5](https://www.seangoedecke.com/em-dashes/#fn-0.5).

### Could em-dash use be RLHF-ed in from African English?

One theory I spent more time looking into was that **em-dash use could reflect the local English dialect of the RLHF workers**. The final stage of training a language model[1](https://www.seangoedecke.com/em-dashes/#fn-1) involves RLHF: reinforcement learning with human feedback. Essentially, hundreds of human testers are paid to interact with the model and grade model outputs, which are then fed back into the model to make it more helpful and friendly.

The AI company paying for this work is incentivized to do it in countries that are low cost-of-living but have many fluent English speakers. For OpenAI, this meant African countries like Kenya and Nigeria. But one interesting consequence of this decision is that African English is subtly different from American or British English. For instance, African English uses the word “delve” more liberally, which is the [explanation](https://www.theguardian.com/technology/2024/apr/16/techscape-ai-gadgest-humane-ai-pin-chatgpt) for why GPT-4o really likes the word “delve” (and other flowery words like “explore” and “tapestry”)[2](https://www.seangoedecke.com/em-dashes/#fn-2).

Does African English use a lot of em-dashes, causing African RLHF workers to rate responses with em-dashes highly? This would be a neat explanation, but I don’t think it’s true. I pulled a [dataset](https://varieng.helsinki.fi/CoRD/corpora/ICE-NIG/) of Nigerian English text and measured the frequency of em-dashes per-word. Out of all words in the dataset, 0.022% of them were em-dashes. This [paper](https://www.researchgate.net/profile/Kun-Sun-5/publication/328512136_Frequency_Distributions_of_Punctuation_Marks_in_English_Evidence_from_Large-scale_Corpora/links/5f803541a6fdccfd7b521aac/Frequency-Distributions-of-Punctuation-Marks-in-English-Evidence-from-Large-scale-Corpora.pdf) about the frequency of punctuation marks in English text in general estimates general em-dash rates as between 0.25% and 0.275%:

> The use of the dash increased after 1750, then reached its peak (about 0.35%) in 1860, but afterwards continued to drop up until the 1950s before starting to fluctuate between 0.25% and 0.275%. The frequency of punctuation marks calculated in the current study is relative to word count in corpora.

Remember that point about em-dash rates peaking in 1860 for later. But for now, it seems like Nigerian English, which is a good-enough stand-in for punctuation rates in African English, is actually _less_ prone to use em-dashes. For that reason, I don’t think the overuse of em-dashes and “delve” are caused by the same mechanism.

### Digitization of print media

One interesting observation about em-dashes is that _GPT-3.5 did not use them_. GPT-4o used ~10x more em-dashes than its predecessor, and GPT-4.1 was even worse. However, Anthropic and Google’s models do use em-dashes. Even the open-source Chinese models use em-dashes[3](https://www.seangoedecke.com/em-dashes/#fn-3). What changed between November 2022 and July 2024?

One thing that changed was the makeup of the training data. In 2022, OpenAI was almost certainly training on a mix of public internet data and pirated books from sites like LibGen. However, once the power of language models became apparent, AI labs quickly realized that they needed more high-quality training data, which meant scanning a lot of print books. Only OpenAI employees know when or if OpenAI started scanning books, but [court filings](https://www.publishersweekly.com/pw/by-topic/digital/copyright/article/98089-federal-judge-rules-ai-training-is-fair-use-in-anthropic-copyright-case.html?utm_source=chatgpt.com) have revealed that Anthropic started their process in February 2024. I think it’s reasonable to assume that OpenAI did something similar. In other words, **between 2022 and 2024 the training data changed to include a lot of print books**.

Remember the punctuation rates study above that showed em-dash rates peaking in 1860? I think it’s a plausible theory that the books AI labs digitized skewed closer to 1860 than the pirated books. Intuitively, pirated content biases towards contemporary and popular literature, because that’s what people want to download. If AI labs wanted to go beyond that, they’d have to go and buy older books, which would probably have more em-dashes. We now arrive at what I think is the most plausible explanation for why AI models include so many em-dashes:

**State-of-the-art models rely on late-1800s and early-1900s print books for high-quality training data, and those books use ~30% more em-dashes than contemporary English prose. That’s why it’s so hard to get models to stop using em-dashes: because they learned English from texts that were full of them.**

I want to thank [this blog](https://msukhareva.substack.com/p/the-mystery-of-emdashes-part-two) from Maria Sukhareva for putting me onto this point. I disagree with her that em-dashes are structurally preferred, for reasons I’ve briefly covered above, but I think it’s very plausible that she’s correct about digitization driving em-dash usage. For some more specific examples and a similar point, you can also check out [this post](https://medium.com/ghost-channel/the-em-dash-debate-is-broken-heres-what-the-data-actually-shows-023fffd5cd06), which shows just how many em-dashes some classic works have. My favorite book, _Moby-Dick_, has a staggering 1728 em-dashes!

### Final thoughts

This is still largely based on speculation. Maybe I’m wrong about when OpenAI started digitizing written text. If they did it before GPT-3.5, then it couldn’t be the cause of em-dashes. Certainly models trained today are at least in part infected with em-dashes by training on the output of other AI models. Either they’re deliberately trained on synthetic data, or they just can’t avoid vacuuming in a host of AI-generated content along with other internet texts.

One thing I’m still a bit confused about: if em-dashes are common because they’re a feature of late-1800s/early-1900s writing, **why doesn’t AI prose read more like Moby-Dick?** Is it plausible that the models are picking up fragments of older English prose stylings, like punctuation, but are still producing contemporary-sounding text?

I also might be wrong that newly-digitized content would have older publication dates. It’s plausible to me that pirated books would skew more contemporary, but could that be outweighed by the number of older books that are in the public domain?

There also might be a simpler explanation for em-dash prevalence: for instance, maybe em-dashes just read more conversational, so they were preferred by RLHF-ers, and this created a vicious cycle that biased towards more and more em-dashes. This would kind of line up with a Sam Altman [interview clip](https://www.linkedin.com/posts/curtwoodward_chatgpt-em-dash-deathwatch-sam-altman-activity-7355259218972557312-RH4j/) where he says they added more em-dashes because people liked them. I don’t know how you’d go about proving or disproving this.

In general, I’m still surprised that there’s no widespread consensus about the cause of one of the most identifiable features of AI prose. I do think I’m probably right that digitizing late-1800s/early-1900s works is the cause - but it would be really nice if someone who was at OpenAI between GPT-3.5 and GPT-4o (or who’s in a position to know for some other reason) could confirm that this is what happened.

* * *

1.   The linked blog post tries to experimentally show that em-dashes save tokens by asking models to paraphrase em-dash sentences and noting that those paraphrased sentences are longer. To be convinced by this, I would like to see if paraphrased non-em-dash sentences are typically the same length or shorter. I suspect that paraphrasing adds tokens no matter what.

[↩](https://www.seangoedecke.com/em-dashes/#fnref-0)
2.   Incidentally, I _do_ think that GPT-5’s overuse of semicolons probably is a brevity bias, because GPT-5 is noticeably less verbose than its predecessors.

[↩](https://www.seangoedecke.com/em-dashes/#fnref-0.5)
3.   At least, in the era of GPT-4o.

[↩](https://www.seangoedecke.com/em-dashes/#fnref-1)
4.   Cultural differences in English is a deep rabbit-hole to go down, which I encountered for the first time via Paul Graham’s [tweet](https://x.com/paulg/status/1777030573220933716) about “delve”, subsequent [tweet](https://x.com/paulg/status/1778887559474495624) about good writing, and the [torrent of criticism](https://medium.com/@moyosoreale/the-paul-graham-vs-nigerian-twitter-saga-lexical-racism-and-language-bias-masked-as-chatgpt-53ee9f6459aa) from Nigerians, Indians, and other post-colonial countries that see a willingness to use flowery language as part of competency with language in general.

[↩](https://www.seangoedecke.com/em-dashes/#fnref-2)
5.   Maybe some of this can be explained by those models training on the output from American labs’ models, but I doubt it. By now it seems pretty clear that the Chinese labs can train pretty strong models on their own.

[↩](https://www.seangoedecke.com/em-dashes/#fnref-3)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/em-dashes/&t=Why%20do%20AI%20models%20use%20so%20many%20em-dashes?).

October 30, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *