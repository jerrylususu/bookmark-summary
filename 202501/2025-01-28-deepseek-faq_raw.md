Title: DeepSeek FAQ

URL Source: https://stratechery.com/2025/deepseek-faq/

Published Time: 2025-01-27T14:05:14+00:00

Markdown Content:
**It’s Monday, January 27. Why haven’t you written about DeepSeek yet?**

I did! I wrote about `R1` [last Tuesday](https://stratechery.com/2025/stratechery-updates-deepseek-r1-deepseek-implications/).

**I totally forgot about that.**

I take responsibility. I stand by the post, including the two biggest takeaways that I highlighted (emergent chain-of-thought via pure reinforcement learning, and the power of distillation), and I mentioned the low cost (which I expanded on in [Sharp Tech](https://sharptech.fm/member/episode/the-end-of-open-ai-and-microsoft-risks-and-rationale-of-the-stargate-project-deep-seek-r-1-and-bitter-lessons-for-the-future)) and chip ban implications, but those observations were too localized to the current state of the art in AI. What I totally failed to anticipate were the broader implications this news would have to the overall meta-discussion, particularly in terms of the U.S. and China.

**Is there precedent for such a miss?**

There is. In September 2023 Huawei announced the Mate 60 Pro with a SMIC-manufactured 7nm chip. The existence of this chip wasn’t a surprise for those paying close attention: SMIC had made a 7nm chip [a year earlier](https://www.semianalysis.com/p/chinas-smic-is-shipping-7nm-foundry) (the existence of which I had noted [even earlier than that](https://stratechery.com/2022/tech-and-war/)), and TSMC had shipped 7nm chips in volume using nothing but DUV lithography (later iterations of 7nm were the first to use EUV). Intel had also made 10nm (TSMC 7nm equivalent) chips years earlier using nothing but DUV, but couldn’t do so with profitable yields; the idea that SMIC could ship 7nm chips using their existing equipment, particularly if they didn’t care about yields, wasn’t remotely surprising — to me, anyways.

What I totally failed to anticipate was the overwrought reaction in Washington D.C. The dramatic expansion in the chip ban that culminated in [the Biden administration transforming chip sales to a permission-based structure](https://stratechery.com/2025/ai-diffusion-regulations-closing-loopholes-the-objections/) was downstream from people not understanding the intricacies of chip production, and being totally blindsided by the Huawei Mate 60 Pro. I get the sense that something similar has happened over the last 72 hours: the details of what DeepSeek has accomplished — and what they have not — are less important than the reaction and what that reaction says about people’s pre-existing assumptions.

**So what did DeepSeek announce?**

The most proximate announcement to this weekend’s meltdown was `R1`, a reasoning model that is similar to OpenAI’s `o1`. However, many of the revelations that contributed to the meltdown — including DeepSeek’s training costs — actually accompanied the `V3` announcement over Christmas. Moreover, many of the breakthroughs that undergirded `V3` were actually revealed with the release of the `V2` model last January.

**Is this model naming convention the greatest crime that OpenAI has committed?**

Second greatest; we’ll get to the greatest momentarily.

**Let’s work backwards: what was the V2 model, and why was it important?**

The DeepSeek-`V2` model introduced two important breakthroughs: DeepSeekMoE and DeepSeekMLA. The “MoE” in DeepSeekMoE refers to “mixture of experts”. Some models, like GPT-3.5, activate the entire model during both training and inference; it turns out, however, that not every part of the model is necessary for the topic at hand. MoE splits the model into multiple “experts” and only activates the ones that are necessary; GPT-4 was a MoE model that was believed to have 16 experts with approximately 110 billion parameters each.

DeepSeekMoE, as implemented in `V2`, introduced important innovations on this concept, including differentiating between more finely-grained specialized experts, and shared experts with more generalized capabilities. Critically, DeepSeekMoE also introduced new approaches to load-balancing and routing during training; traditionally MoE increased communications overhead in training in exchange for efficient inference, but DeepSeek’s approach made training more efficient as well.

DeepSeekMLA was an even bigger breakthrough. One of the biggest limitations on inference is the sheer amount of memory required: you both need to load the model into memory and also load the entire context window. Context windows are particularly expensive in terms of memory, as every token requires both a key and corresponding value; DeepSeekMLA, or multi-head latent attention, makes it possible to compress the key-value store, dramatically decreasing memory usage during inference.

**I’m not sure I understood any of that.**

The key implications of these breakthroughs — and the part you need to understand — only became apparent with `V3`, which added a new approach to load balancing (further reducing communications overhead) and multi-token prediction in training (further densifying each training step, again reducing overhead): `V3` was shockingly cheap to train. DeepSeek claimed the model training took 2,788 thousand H800 GPU hours, which, at a cost of $2/GPU hour, comes out to a mere $5.576 million.

**That seems impossibly low.**

DeepSeek is clear that these costs are only for the final training run, and exclude all other expenses; from [the `V3` paper](https://arxiv.org/html/2412.19437v1):

> Lastly, we emphasize again the economical training costs of DeepSeek-V3, summarized in Table 1, achieved through our optimized co-design of algorithms, frameworks, and hardware. During the pre-training stage, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, i.e., 3.7 days on our cluster with 2048 H800 GPUs. Consequently, our pre- training stage is completed in less than two months and costs 2664K GPU hours. Combined with 119K GPU hours for the context length extension and 5K GPU hours for post-training, DeepSeek-V3 costs only 2.788M GPU hours for its full training. Assuming the rental price of the H800 GPU is $2 per GPU hour, our total training costs amount to only $5.576M. Note that the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments on architectures, algorithms, or data.

So no, you can’t replicate DeepSeek the company for $5.576 million.

**I still don’t believe that number.**

Actually, the burden of proof is on the doubters, at least once you understand the `V3` architecture. Remember that bit about DeepSeekMoE: V3 has 671 billion parameters, but only 37 billion parameters in the active expert are computed per token; this equates to 333.3 billion FLOPs of compute per token. Here I should mention another DeepSeek innovation: while parameters were stored with BF16 or FP32 precision, they were reduced to FP8 precision for calculations; 2048 H800 GPUs have a capacity of 3.97 exoflops, i.e. 3.97 billion billion FLOPS. The training set, meanwhile, consisted of 14.8 trillion tokens; once you do all of the math it becomes apparent that 2.8 million H800 hours is sufficient for training `V3`. Again, this was just the final run, not the total cost, but it’s a plausible number.

**Scale AI CEO Alexandr Wang [said they have 50,000 H100s](https://x.com/kimmonismus/status/1882824571281436713)**.

I don’t know where Wang got his information; I’m guessing he’s referring to [this November 2024 tweet from Dylan Patel](https://x.com/dylan522p/status/1859302712803807696), which says that DeepSeek had “over 50k Hopper GPUs”. H800s, however, are Hopper GPUs, they just have much more constrained memory bandwidth than H100s because of [U.S. sanctions](https://stratechery.com/2022/china-chip-ban-clarifications-nvidias-a800-china-intel-and-tower/).

Here’s the thing: a huge number of the innovations I explained above are about overcoming the lack of memory bandwidth implied in using H800s instead of H100s. Moreover, if you actually did the math on the previous question, you would realize that DeepSeek actually had an excess of computing; that’s because DeepSeek actually programmed 20 of the 132 processing units on each H800 specifically to manage cross-chip communications. _This is actually impossible to do in CUDA._ DeepSeek engineers had to drop down to PTX, a low-level instruction set for Nvidia GPUs that is basically like assembly language. This is an insane level of optimization that only makes sense if you are using H800s.

Meanwhile, DeepSeek also makes their models available for inference: that requires a whole bunch of GPUs above-and-beyond whatever was used for training.

**So was this a violation of the chip ban?**

Nope. H100s were prohibited by the chip ban, but not H800s. Everyone assumed that training leading edge models required more interchip memory bandwidth, but that is exactly what DeepSeek optimized both their model structure and infrastructure around.

Again, just to emphasize this point, all of the decisions DeepSeek made in the design of this model only make sense if you are constrained to the H800; if DeepSeek had access to H100s, they probably would have used a larger training cluster with much fewer optimizations specifically focused on overcoming the lack of bandwidth.

**So `V3` is a leading edge model?**

It’s definitely competitive with OpenAI’s `4o` and Anthropic’s Sonnet-3.5, and appears to be better than Llama’s biggest model. What does seem likely is that DeepSeek was able to distill those models to give `V3` high quality tokens to train on.

**What is distillation?**

Distillation is a means of extracting understanding from another model; you can send inputs to the teacher model and record the outputs, and use that to train the student model. This is how you get models like GPT-4 Turbo from GPT-4. Distillation is easier for a company to do on its own models, because they have full access, but you can still do distillation in a somewhat more unwieldy way via API, or even, if you get creative, via chat clients.

Distillation obviously violates the terms of service of various models, but the only way to stop it is to actually cut off access, via IP banning, rate limiting, etc. It’s assumed to be widespread in terms of model training, and is why there are an ever-increasing number of models converging on GPT-`4o` quality. This doesn’t mean that we know for a fact that DeepSeek distilled `4o` or Claude, but frankly, it would be odd if they didn’t.

**Distillation seems terrible for leading edge models.**

It is! On the positive side, OpenAI and Anthropic and Google are almost certainly using distillation to optimize the models they use for inference for their consumer-facing apps; on the negative side, they are effectively bearing the entire cost of training the leading edge, while everyone else is free-riding on their investment.

Indeed, this is probably the core economic factor undergirding [the slow divorce of Microsoft and OpenAI](https://stratechery.com/2025/stargate-the-end-of-microsoft-and-openai/). Microsoft is interested in providing inference to its customers, but much less enthused about funding $100 billion data centers to train leading edge models that are likely to be commoditized long before that $100 billion is depreciated.

**Is this why all of the Big Tech stock prices are down?**

In the long run, model commoditization and cheaper inference — which DeepSeek has also demonstrated — is great for Big Tech. A world where Microsoft gets to provide inference to its customers for a fraction of the cost means that Microsoft has to spend less on data centers and GPUs, or, just as likely, sees dramatically higher usage given that inference is so much cheaper. Another big winner is Amazon: AWS has by-and-large failed to make their own quality model, but that doesn’t matter if there are very high quality open source models that they can serve at far lower costs than expected.

Apple is also a big winner. Dramatically decreased memory requirements for inference make edge inference much more viable, and Apple has the best hardware for exactly that. Apple Silicon uses unified memory, which means that the CPU, GPU, and NPU (neural processing unit) have access to a shared pool of memory; this means that Apple’s high-end hardware actually has the best consumer chip for inference (Nvidia gaming GPUs max out at 32GB of VRAM, while Apple’s chips go up to 192 GB of RAM).

Meta, meanwhile, is the biggest winner of all. [I already laid out last fall](https://stratechery.com/2024/metas-ai-abundance/) how every aspect of Meta’s business benefits from AI; a big barrier to realizing that vision is the cost of inference, which means that dramatically cheaper inference — and dramatically cheaper training, given the need for Meta to stay on the cutting edge — makes that vision much more achievable.

Google, meanwhile, is probably in worse shape: a world of decreased hardware requirements lessens the relative advantage they have from TPUs. More importantly, a world of zero-cost inference increases the viability and likelihood of products that displace search; granted, Google gets lower costs as well, but any change from the status quo is probably a net negative.

**I asked why the stock prices are down; you just painted a positive picture!**

My picture is of the long run; today is the short run, and it seems likely the market is working through the shock of R1’s existence.

**Wait, you haven’t even talked about `R1` yet.**

`R1` is a reasoning model like OpenAI’s `o1`. It has the ability to think through a problem, producing much higher quality results, particularly in areas like coding, math, and logic (but I repeat myself).

**Is this more impressive than `V3`?**

Actually, the reason why I spent so much time on `V3` is that that was the model that actually demonstrated a lot of the dynamics that seem to be generating so much surprise and controversy. `R1` is notable, however, because `o1` stood alone as the only reasoning model on the market, and the clearest sign that OpenAI was the market leader.

`R1` undoes the `o1` mythology in a couple of important ways. First, there is the fact that it exists. OpenAI does not have some sort of special sauce that can’t be replicated. Second, `R1` — like all of DeepSeek’s models — has open weights (the problem with saying “open source” is that we don’t have the data that went into creating it). This means that instead of paying OpenAI to get reasoning, you can run `R1` on the server of your choice, or even locally, at dramatically lower cost.

**How did DeepSeek make `R1`?**

DeepSeek actually made two models: `R1` and `R1`\-Zero. I actually think that `R1`\-Zero is the bigger deal; as I noted above, it was my biggest focus in [last Tuesday’s Update](https://stratechery.com/2025/stratechery-updates-deepseek-r1-deepseek-implications/):

> `R1`\-Zero, though, is the bigger deal in my mind. [From the paper](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf):
> 
> > In this paper, we take the first step toward improving language model reasoning capabilities using pure reinforcement learning (RL). Our goal is to explore the potential of LLMs to develop reasoning capabilities without any supervised data, focusing on their self-evolution through a pure RL process. Specifically, we use DeepSeek-`V3`\-Base as the base model and employ GRPO as the RL framework to improve model performance in reasoning. During training, DeepSeek-`R1`\-Zero naturally emerged with numerous powerful and interesting reasoning behaviors. After thousands of RL steps, DeepSeek-`R1`\-Zero exhibits super performance on reasoning benchmarks. For instance, the pass@1 score on AIME 2024 increases from 15.6% to 71.0%, and with majority voting, the score further improves to 86.7%, matching the performance of OpenAI-`o1`\-0912.
> 
> Reinforcement learning is a technique where a machine learning model is given a bunch of data and a reward function. The classic example is AlphaGo, where DeepMind gave the model the rules of Go with the reward function of winning the game, and then let the model figure everything else on its own. This famously ended up working better than other more human-guided techniques.
> 
> LLMs to date, however, have relied on reinforcement learning with human feedback; humans are in the loop to help guide the model, navigate difficult choices where rewards aren’t obvious, etc. RLHF was the key innovation in transforming GPT-3 into ChatGPT, with well-formed paragraphs, answers that were concise and didn’t trail off into gibberish, etc.
> 
> `R1`\-Zero, however, drops the HF part — it’s just reinforcement learning. DeepSeek gave the model a set of math, code, and logic questions, and set two reward functions: one for the right answer, and one for the right format that utilized a thinking process. Moreover, the technique was a simple one: instead of trying to evaluate step-by-step (process supervision), or doing a search of all possible answers (a la AlphaGo), DeepSeek encouraged the model to try several different answers at a time and then graded them according to the two reward functions.
> 
> What emerged is a model that developed reasoning and chains-of-thought on its own, including what DeepSeek called “Aha Moments”:
> 
> > A particularly intriguing phenomenon observed during the training of DeepSeek-`R1`\-Zero is the occurrence of an “aha moment”. This moment, as illustrated in Table 3, occurs in an intermediate version of the model. During this phase, DeepSeek-`R1`\-Zero learns to allocate more thinking time to a problem by reevaluating its initial approach. This behavior is not only a testament to the model’s growing reasoning abilities but also a captivating example of how reinforcement learning can lead to unexpected and sophisticated outcomes.
> > 
> > This moment is not only an “aha moment” for the model but also for the researchers observing its behavior. It underscores the power and beauty of reinforcement learning: rather than explicitly teaching the model on how to solve a problem, we simply provide it with the right incentives, and it autonomously develops advanced problem-solving strategies. The “aha moment” serves as a powerful reminder of the potential of RL to unlock new levels of intelligence in artificial systems, paving the way for more autonomous and adaptive models in the future.
> 
> This is one of the most powerful affirmations yet of [The Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf): you don’t need to teach the AI how to reason, you can just give it enough compute and data and it will teach itself!
> 
> Well, almost: `R1`\-Zero reasons, but in a way that humans have trouble understanding. Back to the introduction:
> 
> > However, DeepSeek-`R1`\-Zero encounters challenges such as poor readability, and language mixing. To address these issues and further enhance reasoning performance, we introduce DeepSeek-`R1`, which incorporates a small amount of cold-start data and a multi-stage training pipeline. Specifically, we begin by collecting thousands of cold-start data to fine-tune the DeepSeek-`V3`\-Base model. Following this, we perform reasoning-oriented RL like DeepSeek-`R1`\-Zero. Upon nearing convergence in the RL process, we create new SFT data through rejection sampling on the RL checkpoint, combined with supervised data from DeepSeek-`V3` in domains such as writing, factual QA, and self-cognition, and then retrain the DeepSeek-`V3`\-Base model. After fine-tuning with the new data, the checkpoint undergoes an additional RL process, taking into account prompts from all scenarios. After these steps, we obtained a checkpoint referred to as DeepSeek-`R1`, which achieves performance on par with OpenAI-`o1`\-1217.
> 
> This sounds a lot like what [OpenAI did for `o1`](https://stratechery.com/2024/openais-new-model-how-o1-works-scaling-inference/): DeepSeek started the model out with a bunch of examples of chain-of-thought thinking so it could learn the proper format for human consumption, and then did the reinforcement learning to enhance its reasoning, along with a number of editing and refinement steps; the output is a model that appears to be very competitive with `o1`.

Here again it seems plausible that DeepSeek benefited from distillation, particularly in terms of training `R1`. That, though, is itself an important takeaway: we have a situation where AI models are teaching AI models, and where AI models are teaching themselves. We are watching the assembly of an AI takeoff scenario in realtime.

**So are we close to AGI?**

It definitely seems like it. This also explains why Softbank (and whatever investors Masayoshi Son brings together) would provide the funding for OpenAI that Microsoft will not: the belief that we are reaching a takeoff point where there will in fact be real returns towards being first.

**But isn’t `R1` now in the lead?**

I don’t think so; this has been overstated. `R1` is competitive with `o1`, although there do seem to be some holes in its capability that point towards some amount of distillation from `o1`\-Pro. OpenAI, meanwhile, has demonstrated `o3`, a far more powerful reasoning model. DeepSeek is absolutely the leader in efficiency, but that is different than being the leader overall.

**So why is everyone freaking out?**

I think there are multiple factors. First, there is the shock that China has caught up to the leading U.S. labs, despite the widespread assumption that China isn’t as good at software as the U.S.. This is probably the biggest thing I missed in my surprise over the reaction. The reality is that China has an extremely proficient software industry generally, and a very good track record in AI model building specifically.

Second is the low training cost for `V3`, and DeepSeek’s low inference costs. This part was a big surprise for me as well, to be sure, but the numbers are plausible. This, by extension, probably has everyone nervous about Nvidia, which obviously has a big impact on the market.

Third is the fact that DeepSeek pulled this off despite the chip ban. Again, though, while there are big loopholes in the chip ban, it seems likely to me that DeepSeek accomplished this with legal chips.

**I own Nvidia! Am I screwed?**

There are real challenges this news presents to the Nvidia story. Nvidia has two big moats:

*   CUDA is the language of choice for anyone programming these models, and CUDA only works on Nvidia chips.
*   Nvidia has a massive lead in terms of its ability to combine multiple chips together into one large virtual GPU.

These two moats work together. I noted above that if DeepSeek had access to H100s they probably would have used a larger cluster to train their model, simply because that would have been the easier option; the fact they didn’t, and were bandwidth constrained, drove a lot of their decisions in terms of both model architecture and their training infrastructure. Just look at the U.S. labs: they haven’t spent much time on optimization because Nvidia has been aggressively shipping ever more capable systems that accommodate their needs. The route of least resistance has simply been to pay Nvidia. DeepSeek, however, just demonstrated that another route is available: heavy optimization can produce remarkable results on weaker hardware and with lower memory bandwidth; simply paying Nvidia more isn’t the only way to make better models.

That noted, there are three factors still in Nvidia’s favor. First, how capable might DeepSeek’s approach be if applied to H100s, or upcoming GB100s? Just because they found a more efficient way to use compute doesn’t mean that more compute wouldn’t be useful. Second, lower inference costs should, in the long run, drive greater usage. Microsoft CEO Satya Nadella, in a late night tweet almost assuredly directed at the market, said exactly that:

> Jevons paradox strikes again! As AI gets more efficient and accessible, we will see its use skyrocket, turning it into a commodity we just can't get enough of. [https://t.co/omEcOPhdIz](https://t.co/omEcOPhdIz)
> 
> — Satya Nadella (@satyanadella) [January 27, 2025](https://twitter.com/satyanadella/status/1883753899255046301?ref_src=twsrc%5Etfw)

Third, reasoning models like `R1` and `o1` derive their superior performance from using more compute. To the extent that increasing the power and capabilities of AI depend on more compute is the extent that Nvidia stands to benefit!

Still, it’s not all rosy. At a minimum DeepSeek’s efficiency and broad availability cast significant doubt on the most optimistic Nvidia growth story, at least in the near term. The payoffs from both model and infrastructure optimization also suggest there are significant gains to be had from exploring alternative approaches to inference in particular. For example, it might be much more plausible to run inference on a standalone AMD GPU, completely sidestepping AMD’s inferior chip-to-chip communications capability. Reasoning models also increase the payoff for inference-only chips that are even more specialized than Nvidia’s GPUs.

In short, Nvidia isn’t going anywhere; the Nvidia stock, however, is suddenly facing a lot more uncertainty that hasn’t been priced in. And that, by extension, is going to drag everyone down.

**So what about the chip ban?**

The easiest argument to make is that the importance of the chip ban has only been accentuated given the U.S.’s rapidly evaporating lead in software. Software and knowhow can’t be embargoed — we’ve had these debates and realizations before — but chips are physical objects and the U.S. is justified in keeping them away from China.

At the same time, there should be some humility about the fact that earlier iterations of the chip ban seem to have directly led to DeepSeek’s innovations. Those innovations, moreover, would extend to not just smuggled Nvidia chips or nerfed ones like the H800, but to Huawei’s Ascend chips as well. Indeed, you can very much make the case that the primary outcome of the chip ban is today’s crash in Nvidia’s stock price.

What concerns me is the mindset undergirding something like the chip ban: instead of competing through innovation in the future the U.S. is competing through the denial of innovation in the past. Yes, this may help in the short term — again, DeepSeek would be even more effective with more computing — but in the long run it simply sews the seeds for competition in an industry — chips and semiconductor equipment — over which the U.S. has a dominant position.

**Like AI models?**

AI models are a great example. I mentioned above I would get to OpenAI’s greatest crime, which I consider to be the [2023 Biden Executive Order on AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/). I wrote in [Attenuating Innovation](https://stratechery.com/2023/attenuating-innovation-ai/):

> The point is this: if you accept the premise that regulation locks in incumbents, then it sure is notable that the early AI winners seem the most invested in generating alarm in Washington, D.C. about AI. This despite the fact that their concern is apparently not sufficiently high to, you know, stop their work. No, they are the responsible ones, the ones who care enough to call for regulation; all the better if concerns about imagined harms kneecap inevitable competitors.

That paragraph was about OpenAI specifically, and the broader San Francisco AI community generally. For years now we have been subject to hand-wringing about the dangers of AI by the exact same people committed to building it — and controlling it. These alleged dangers were the impetus for OpenAI becoming closed [back in 2019 with the release of GPT-2](https://openai.com/index/better-language-models/):

> Due to concerns about large language models being used to generate deceptive, biased, or abusive language at scale, we are only releasing a much smaller version of GPT-2 along with sampling code⁠(opens in a new window). We are not releasing the dataset, training code, or GPT-2 model weights…We are aware that some researchers have the technical capacity to reproduce and open source our results. We believe our release strategy limits the initial set of organizations who may choose to do this, and gives the AI community more time to have a discussion about the implications of such systems.
> 
> We also think governments should consider expanding or commencing initiatives to more systematically monitor the societal impact and diffusion of AI technologies, and to measure the progression in the capabilities of such systems. If pursued, these efforts could yield a better evidence base for decisions by AI labs and governments regarding publication decisions and AI policy more broadly.

The arrogance in this statement is only surpassed by the futility: here we are six years later, and the entire world has access to the weights of a dramatically superior model. OpenAI’s gambit for control — enforced by the U.S. government — has utterly failed. In the meantime, how much innovation has been foregone by virtue of leading edge models not having open weights? More generally, how much time and energy has been spent lobbying for a government-enforced moat that DeepSeek just obliterated, that would have been better devoted to actual innovation?

**So you’re not worried about AI doom scenarios?**

I definitely understand the concern, and just noted above that we are reaching the stage where AIs are training AIs and learning reasoning on their own. I recognize, though, that there is no stopping this train. More than that, this is exactly why openness is so important: we need more AIs in the world, not an unaccountable board ruling all of us.

**Wait, why is China open-sourcing their model?**

Well DeepSeek is, to be clear; CEO Liang Wenfeng said in [a must-read interview](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas) that open source is key to attracting talent:

> In the face of disruptive technologies, moats created by closed source are temporary. Even OpenAI’s closed source approach can’t prevent others from catching up. So we anchor our value in our team — our colleagues grow through this process, accumulate know-how, and form an organization and culture capable of innovation. That’s our moat.
> 
> Open source, publishing papers, in fact, do not cost us anything. For technical talent, having others follow your innovation gives a great sense of accomplishment. In fact, open source is more of a cultural behavior than a commercial one, and contributing to it earns us respect. There is also a cultural attraction for a company to do this.

The interviewer asked if this would change:

> **DeepSeek, right now, has a kind of idealistic aura reminiscent of the early days of OpenAI, and it’s open source. Will you change to closed source later on? Both OpenAI and Mistral moved from open-source to closed-source.**
> 
> We will not change to closed source. We believe having a strong technical ecosystem first is more important.

This actually makes sense beyond idealism. If models are commodities — and they are certainly looking that way — then long-term differentiation comes from having a superior cost structure; that is exactly what DeepSeek has delivered, which itself is resonant of how China has come to dominate other industries. This is also contrary to how most U.S. companies think about differentiation, which is through having differentiated products that can sustain larger margins.

**So is OpenAI screwed?**

Not necessarily. [ChatGPT made OpenAI the accidental consumer tech company](https://stratechery.com/2023/the-accidental-consumer-tech-company-chatgpt-meta-and-product-market-fit-aggregation-and-apis/), which is to say a product company; there is a route to building a sustainable consumer business on commoditizable models through some combination of subscriptions and advertisements. And, of course, there is the bet on winning the race to AI take-off.

Anthropic, on the other hand, is probably the biggest loser of the weekend. DeepSeek made it to number one in the App Store, simply highlighting how Claude, in contrast, hasn’t gotten any traction outside of San Francisco. The API business is doing better, but API businesses in general are the most susceptible to the commoditization trends that seem inevitable (and do note that OpenAI and Anthropic’s inference costs look a lot higher than DeepSeek because they w