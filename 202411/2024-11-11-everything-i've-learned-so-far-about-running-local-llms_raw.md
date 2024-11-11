Title: Everything I've learned so far about running local LLMs

URL Source: https://nullprogram.com/blog/2024/11/10/

Markdown Content:
November 10, 2024nullprogram.com/blog/2024/11/10/

_This article was discussed [on Hacker News](https://news.ycombinator.com/item?id=42100560)._

Over the past month I’ve been exploring the rapidly evolving world of Large Language Models (LLM). It’s now accessible enough to run a LLM on a Raspberry Pi smarter than the original ChatGPT (November 2022). A modest desktop or laptop supports even smarter AI. It’s also private, offline, unlimited, and registration-free. The technology is improving at breakneck speed, and information is outdated in a matter of months. This article snapshots my practical, hands-on knowledge and experiences — information I wish I had when starting. Keep in mind that I’m a LLM layman, I have no novel insights to share, and it’s likely I’ve misunderstood certain aspects. In a year this article will mostly be a historical footnote, which is simultaneously exciting and scary.

In case you’ve been living under a rock — as an under-the-rock inhabitant myself, welcome! — LLMs are neural networks that underwent a breakthrough in 2022 when trained for conversational “chat.” Through it, users converse with a wickedly creative artificial intelligence indistinguishable from a human, which smashes the Turing test and can be wickedly creative. Interacting with one for the first time is unsettling, a feeling which will last for days. When you bought your most recent home computer, you probably did not expect to have a meaningful conversation with it.

I’ve found this experience reminiscent of the desktop computing revolution of the 1990s, where your newly purchased computer seemed obsolete by the time you got it home from the store. There are new developments each week, and as a rule I ignore almost any information more than a year old. The best way to keep up has been [r/LocalLLaMa](https://old.reddit.com/r/LocalLLaMA). Everything is hyped to the stratosphere, so take claims with a grain of salt.

I’m wary of vendor lock-in, having experienced the rug pulled out from under me by services shutting down, changing, or otherwise dropping my use case. I want the option to continue, even if it means changing providers. So for a couple of years I’d ignored LLMs. The “closed” models, accessibly only as a service, have the classic lock-in problem, including [silent degradation](https://arxiv.org/pdf/2307.09009). That changed when I learned I can run models close to the state-of-the-art on my own hardware — the exact opposite of vendor lock-in.

This article is about running LLMs, not fine-tuning, and definitely not training. It’s also only about _text_, and not vision, voice, or other “multimodal” capabilities, which aren’t nearly so useful to me personally.

To run a LLM on your own hardware you need **software** and a **model**.

### The software

I’ve exclusively used the _astounding_ [llama.cpp](https://github.com/ggerganov/llama.cpp). Other options exist, but for basic CPU inference — that is, generating tokens using a CPU rather than a GPU — llama.cpp requires nothing beyond a C++ toolchain. In particular, no Python fiddling that plagues much of the ecosystem. On Windows it will be a 5MB `llama-server.exe` with no runtime dependencies. From just two files, EXE and GGUF (model), both designed to [load via memory map](https://justine.lol/mmap/), you could likely still run the same LLM 25 years from now, in exactly the same way, out-of-the-box on some future Windows OS.

Full disclosure: I’m biased because [the official Windows build process is w64devkit](https://github.com/ggerganov/llama.cpp/blob/ec450d3b/docs/build.md). What can I say? These folks have good taste! That being said, you should only do CPU inference if GPU inference is impractical. It works reasonably up to ~10B parameter models on a desktop or laptop, but it’s slower. My primary use case is not built with w64devkit because I’m using CUDA for inference, which requires a MSVC toolchain. Just for fun, I ported llama.cpp to Windows XP and ran [a 360M model](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) on a 2008-era laptop. It was magical to load that old laptop with technology that, at the time it was new, would have been worth billions of dollars.

The bottleneck for GPU inference is video RAM, or VRAM. These models are, well, _large_. The more RAM you have, the larger the model and the longer the context window. Larger models are smarter, and longer contexts let you process more information at once. **GPU inference is not worth it below 8GB of VRAM**. If [“GPU poor”](https://huggingface.co/spaces/k-mktr/gpu-poor-llm-arena), stick with CPU inference. On the plus side, it’s simpler and easier to get started with CPU inference.

There are many utilities in llama.cpp, but this article is concerned with just one: **`llama-server` is the program you want to run.** It’s an HTTP server (default port 8080) with a chat UI at its root, and [APIs for use by programs](https://github.com/ggerganov/llama.cpp/blob/ec450d3b/examples/server/README.md#api-endpoints), including other user interfaces. A typical invocation:

```
$ llama-server --flash-attn --ctx-size 0 --model MODEL.gguf
```

The context size is the largest number of tokens the LLM can handle at once, input plus output. Contexts typically range from 8K to 128K tokens, and depending on the model’s tokenizer, normal English text is ~1.6 tokens per word as counted by `wc -w`. If the model supports a large context you may run out of memory. If so, set a smaller context size, like ```
--ctx-size
$((1<<13))
``` (i.e. 8K tokens).

I do not yet understand what flash attention is about, and I don’t know why `--flash-attn`/`-fa` is not the default (lower accuracy?), but you should always request it because it reduces memory requirements when active and is well worth the cost.

If the server started successfully, visit it ([http://localhost:8080/](http://localhost:8080/)) to try it out. Though of course you’ll need a model first.

### The models

[Hugging Face](https://huggingface.co/) (HF) is “the GitHub of LLMs.” It’s an incredible service that has earned that title. “Small” models are around a few GBs, large models are hundreds of GBs, and HF _hosts it all for free_. With a few exceptions that do not matter in practice, you don’t even need to sign up to download models! (I’ve been so impressed that after a few days they got a penny-pincher like me to pay for pro account.) That means you can immediately download and try any of the stuff I’m about to discuss.

If you look now, you’ll wonder, “There’s a lot of stuff here, so what the heck am I supposed to download?” That was me one month ago. For llama.cpp, the answer is [GGUF](https://github.com/ggerganov/ggml/blob/8a3d7994/docs/gguf.md). None of the models are natively in GGUF. Instead GGUFs are in a repository with “GGUF” in the name, usually by a third party: one of the heroic, prolific GGUF quantizers.

(Note how nowhere does the official documentation define what “GGUF” stands for. Get used that. This is a technological frontier, and if the information exists at all, it’s not in the obvious place. If you’re considering asking your LLM about this once it’s running: Sweet summer child, we’ll soon talk about why that doesn’t work. As far as I can tell, “GGUF” has no authoritative definition (**update**: [the U stands for “Unified”](https://github.com/ggerganov/ggml/issues/220), but the rest is still ambiguous).)

Since llama.cpp is named after the Meta’s flagship model, their model is a reasonable start, though it’s not my personal favorite. The latest is Llama 3.2, but at the moment only the 1B and 3B models — that is, ~1 billion and ~3 billion parameters — work in Llama.cpp. Those are a little _too_ small to be of much use, and your computer can likely to better if it’s not a Raspberry Pi, even with CPU inference. Llama 3.1 8B is a better option. (If you’ve got at least 24GB of VRAM then maybe you can even do Llama 3.1 70B.)

If you search for Llama 3.1 8B you’ll find two options, one qualified “instruct” and one with no qualifier. Instruct means it was trained to follow instructions, i.e. to chat, and that’s nearly always what you want. The other is the “base” model which can only continue a text. (Technically the instruct model is still just completion, but we’ll get to that later.) It would be great if base models were qualified “Base” but, for dumb path dependency reasons, they’re usually not.

You will not find GGUF in the “Files” for the instruct model, nor can you download the model without signing up in order to agree to the community license. Go back to the search, add GGUF, and look for the matching GGUF model: [bartowski/Meta-Llama-3.1-8B-Instruct-GGUF](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF). bartowski is one of the prolific and well-regarded GGUF quantizers. Not only will this be in the right format for llama.cpp, you won’t need to sign up.

In “Files” you will now see many GGUFs. These are different quantizations of the same model. The original model has [bfloat16](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format) tensors, but for merely running the model we can throw away most of that precision with minimal damage. It will be a tiny bit dumber and less knowledgeable, but will require substantially fewer resources. **The general recommendation, which fits my experience, is to use `Q4_K_M`**, a 4-bit quantization. In general, better to run a 4-bit quant of a larger model than an 8-bit quant of a smaller model. Once you’ve got the basics understood, experiment with different quants and see what you like!

### My favorite models

Models are trained for different trade-offs and differ in strengths and weaknesses, so no model is best at everything — especially on “GPU-poor” configurations. My desktop system has an RTX 3050 Ti with 8GB VRAM, and its limitations have shaped my choices. I can comfortably run ~10B models, and ~30B models just barely enough to test their capabilities. For ~70B I rely on third-party hosts. My “t/s” numbers are all on this system running 4-bit quants.

This list omits “instruct” from the model name, but assume the instruct model unless I say otherwise. A few are _bona fide_ open source, at least as far as LLMs practically can be, and I’ve noted the license when that’s the case. The rest place restrictions on both use and distribution.

*   Mistral-Nemo-2407 (12B) \[Apache 2.0\]
    
    A collaboration between [Mistral AI](https://mistral.ai/) and Nvidia (“Nemo”), the most well-rounded ~10B model I’ve used, and my default. Inference starts at a comfortable 30 t/s. It’s strengths are writing and proofreading, and it can review code nearly as well as ~70B models. It was trained for a context length of 128K, but its [effective context length is closer to 16K](https://github.com/NVIDIA/RULER) — a limitation I’ve personally observed.
    
    The “2407” is a date (July 2024) as version number, a versioning scheme I wholeheartedly support. A date tells you about its knowledge cut-off and tech level. It sorts well. Otherwise LLM versioning is a mess. Just as open source is bad with naming, AI companies do not comprehend versioning.
    
*   Qwen2.5-14B and Qwen2.5-72B
    
    Qwen models, by Alibaba Cloud, impressively punch above their weight at all sizes. 14B inference starts at 11 t/s, with capabilities on par with Mistral Nemo. If I could run 72B on my own hardware, it would probably be my default. I’ve been trying it through Hugging Face’s inference API. There’s a 32B model, but it’s impractical for my hardware, so I haven’t spent much time with it.
    
*   Gemma-2-2B
    
    Google’s model is popular, perhaps due to its playful demeanor. For me, the 2B model [is great for fast translation](https://github.com/skeeto/scratch/blob/master/userscript/reddit-llm-translate.user.js). It’s amazing that LLMs have nearly obsoleted Google Translate, and you can run it on your home computer. Though it’s more resource-intensive, and refuses to translate texts it finds offensive, which sounds like a plot element from a sci-fi story. In my translation script, I send it text marked up with HTML. Simply _asking_ Gemma to preserve the markup Just Works! The 9B model is even better, but slower, and I’d use it instead of 2B for translating my own messages into another language.
    
*   Phi3.5-Mini (4B) \[MIT\]
    
    Microsoft’s niche is training on synthetic data. The result is a model that does well in tests, but doesn’t work so well in practice. For me, its strength is document evaluation. I’ve loaded the context with up to 40K-token documents — it helps that it’s a 4B model — and successfully queried accurate summaries and data listings.
    
*   SmolLM2-360M \[Apache 2.0\]
    
    Hugging Face doesn’t just host models; their 360M model is unusually good for its size. It fits on my 2008-era, 1G RAM, Celeron, and 32-bit operating system laptop. It also runs well on older Raspberry Pis. It’s creative, fast, converses competently, can write poetry, and a fun toy in cramped spaces.
    
*   Mixtral-8x7B (48B) \[Apache 2.0\]
    
    Another Mistral AI model, and more of a runner up. 48B seems too large, but this is a [Mixture of Experts](https://mistral.ai/news/mixtral-of-experts/) (MoE) model. Inference uses only 13B parameters at a time. It’s reasonably-suited to CPU inference on a machine with at least 32G of RAM. The model retains more of its training inputs, more like a database, but for reasons we’ll see soon, it isn’t as useful as it might seem.
    
*   Llama-3.1-70B and Llama-3.1-Nemotron-70B
    
    More models I cannot run myself, but which I access remotely. The latter bears “Nemo” because it’s an Nvidia fine-tune. If I could run 70B models myself, Nemotron might just be my default. I’d need to spent more time evaluating it against Qwen2.5-72B.
    

Most of these models have [abliterated](https://huggingface.co/blog/mlabonne/abliteration) or “uncensored” versions, in which refusal is partially fine-tuned out at a cost of model degradation. Refusals are annoying — such as Gemma refusing to translate texts it dislikes — but doesn’t happen enough for me to make that trade-off. Maybe I’m just boring. Also refusals seem to decrease with larger contexts, as though “in for a penny, in for a pound.”

The next group are “coder” models trained for programming. In particular, they have _fill-in-the-middle_ (FIM) training for generating code inside an existing program. I’ll discuss what that entails in a moment. As far as I can tell, they’re no better at code review nor other instruct-oriented tasks. It’s the opposite: FIM training is done in the base model, with instruct training applied later on top, so instruct works _against_ FIM! In other words, you get better FIM results from base models, though you lose the ability to converse with them.

There will be a section on evaluation later, but I want to note now that _LLMs still produce poor code_, even at the state-of-the-art. The rankings here are relative to other models, not about overall capability.

*   DeepSeek-Coder-V2-Lite (16B)
    
    A self-titled MoE model from [DeepSeek](https://www.deepseek.com/). It uses 2B parameters during inference, making it as fast as Gemma 2 2B but as smart as Mistral Nemo, striking a great balance, especially because it out-competes ~30B models at code generation. If I’m playing around with FIM, this is my default choice.
    
*   Qwen2.5-Coder-7B
    
    Qwen Coder is a close second. It works about as well, but slightly slower since it’s not MoE. It’s a better choice than DeepSeek if you’re memory-constrained, or, similarly, if your choices are GPU inference Qwen versus CPU inference DeepSeek. While writing this article, Alibaba Cloud released a new Qwen2.5-Coder-7B that’s reported to be better. They failed to increment the version number, which is horribly confusing. The community has taken to calling it Qwen2.5.1. (Remember what I said about AI companies and versions?)
    
*   Granite-8B-Code \[Apache 2.0\]
    
    IBM’s line of models is named Granite. In general Granite models are disappointing, _except_ that they’re unusually good at FIM. It’s tied in second place with Qwen2.5 7B in my experience.
    

I also evaluated CodeLlama, CodeGemma, Codestral, and StarCoder. Their FIM outputs were so poor as to be effectively worthless at that task, and I found no reason to use these models. The negative effects of instruct training were most pronounced for CodeLlama.

### The user interfaces

I pointed out Llama.cpp’s built-in UI, and I’d used similar UIs with other LLM software. As is typical, no UI is to my liking, especially in matters of productivity, so I built my own, **[Illume](https://github.com/skeeto/illume)**. This command line program converts standard input into an API query, makes the query, and streams the response to standard output. Should be simple enough to integrate into any extensible text editor, but I only needed it for Vim. Vimscript is miserable, probably the second worst programming language I’ve ever touched, so my goal was to write as little as possible.

I created Illume to scratch my own itch, to support my exploration of the LLM ecosystem. I actively break things and add features as needed, and I make no promises about interface stability. _You probably don’t want to use it._

Lines that begin with `!` are directives interpreted by Illume, chosen because it’s unlikely to appear in normal text. A conversation alternates between `!user` and `!assistant` in a buffer.

```
!user
Write a Haiku about time travelers disguised as frogs.

!assistant
Green, leaping through time,
Frog tongues lick the future's rim,
Disguised in pond's guise.
```

It’s still a text editor buffer, so I can edit the assistant response, reword my original request, etc. before continuing the conversation. For composing fiction, I can request it to continue some text (which does not require instruct training):

```
!completion
Din the Wizard stalked the dim castle
```

I can stop it, make changes, add my own writing, and keep going. I ought to spend more time practicing with it. If you introduce out-of-story note syntax, the LLM will pick up on it, and then you can use notes to guide the LLM’s writing.

While the main target is llama.cpp, I query different APIs, implemented by different LLM software, with incompatibilities across APIs (a parameter required by one API is forbidden by another), so directives must be flexible and powerful. So directives can set arbitrary HTTP and JSON parameters. Illume doesn’t try to abstract the API, but exposes it at a low level, so effective use requires knowing the remote API. For example, the “profile” for talking to llama.cpp looks like this:

```
!api http://localhost:8080/v1
!:cache_prompt true
```

Where `cache_prompt` is a llama.cpp-specific JSON parameter (`!:`). Prompt cache nearly always better enabled, yet for some reason it’s disabled by default. Other APIs refuse requests with this parameter, so then I must omit or otherwise disable it. The Hugging Face “profile” looks like this:

```
!api https://api-inference.huggingface.co/models/{model}/v1
!:model Qwen/Qwen2.5-72B-Instruct
!>x-use-cache false
```

For the sake of HF, Illume can interpolate JSON parameters into the URL. The HF API caches also aggressively caches. I never want this, so I supply an HTTP parameter (`!>`) to turn it off.

Unique to llama.cpp is an `/infill` endpoint for FIM. It requires a model with extra metadata, trained a certain way, but this is usually not the case. So while Illume can use `/infill`, I also added FIM configuration so, after reading the model’s documentation and configuring Illume for that model’s FIM behavior, I can do FIM completion through the normal completion API on any FIM-trained model, even on non-llama.cpp APIs.

### Fill-in-the-Middle (FIM) tokens

It’s time to discuss FIM. To get to the bottom of FIM I needed to go to the source of truth, the original FIM paper: [Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/abs/2207.14255). This allowed me to understand how these models are FIM-trained, at least enough to put that training to use. Even so, model documentation tends to be thin on FIM because they expect you to run their code.

Ultimately an LLM can only predict the next token. So pick some special tokens that don’t appear in inputs, use them to delimit a prefix and suffix, and middle (PSM) — or sometimes ordered suffix-prefix-middle (SPM) — in a large training corpus. Later in inference we can use those tokens to provide a prefix, suffix, and let it “predict” the middle. Crazy, but _this actually works!_

```
<PRE>{prefix}<SUF>{suffix}<MID>
```

For example when filling the parentheses of `dist = sqrt(x*x + y*y)`:

```
<PRE>dist = sqrt(<SUF>)<MID>x*x + y*y
```

To have the LLM fill in the parentheses, we’d stop at `<MID>` and let the LLM predict from there. Note how `<SUF>` is essentially the cursor. By the way, this is basically how instruct training works, but instead of prefix and suffix, special tokens delimit instructions and conversation.

Some LLM folks interpret the paper quite literally and use `<PRE>`, etc. for their FIM tokens, although these look nothing like their other special tokens. More thoughtful trainers picked `<|fim_prefix|>`, etc. Illume accepts FIM templates, and I wrote templates for the popular models. For example, here’s Qwen (PSM):

```
<|fim_prefix|>{prefix}<|fim_suffix|>{suffix}<|fim_middle|>
```

Mistral AI prefers square brackets, SPM, and no “middle” token:

```
[SUFFIX]{suffix}[PREFIX]{prefix}
```

With these templates I could access the FIM training in models unsupported by llama.cpp’s `/infill` API.

Besides just failing the prompt, the biggest problem I’ve had with FIM is LLMs not know when to stop. For example, if I ask it to fill out this function (i.e. assign something `r`):

```
def norm(x: float, y: float) -> float):
    return r
```

(Side note: Static types, including the hints here, produce better results from LLMs, acting as guardrails.) It’s not unusual to get something like:

```
def norm(x: float, y: float) -> float):
    r = sqrt(x*x + y*y)
    return r

def norm3(x: float, y: float, z: float) -> float):
    r = sqrt(x*x + y*y + z*z)
    return r

def norm4(x: float, y: float, z: float, w: float) -> float):
    r = sqrt(x*x + y*y + z*z + w*w)
    return r
```

Where the original `return r` became the return for `norm4`. Technically it fits the prompt, but it’s obviously not what I want. So be ready to mash the “stop” button when it gets out of control. The three coder models I recommended exhibit this behavior less often. It might be more robust to combine it with a non-LLM system that understands the code semantically and automatically stops generation when the LLM begins generating tokens in a higher scope. That would make more coder models viable, but this goes beyond my own fiddling.

Figuring out FIM and putting it into action revealed to me that FIM is still in its early stages, and hardly anyone is generating code via FIM. I guess everyone’s just using plain old completion?

### So what are LLMs good for?

LLMs are fun, but what the productive uses do they have? That’s a question I’ve been trying to answer this past month, and it’s come up shorter than I hoped. It might be useful to establish boundaries — tasks that LLMs definitely cannot do.

First, **LLMs are no good if correctness cannot be readily verified**. They are untrustworthy hallucinators. Often if you’re in position to verify LLM output, you didn’t need it in the first place. This is why Mixtral, with its large “database” of knowledge, isn’t so useful. It also means it’s _reckless and irresponsible to inject LLM output into search results_ — just shameful.

LLM enthusiasts, who ought to know better, fall into this trap anyway and propagate hallucinations. It makes discourse around LLMs less trustworthy than normal, and I need to approach LLM information with extra skepticism. Case in point: Recall how “GGUF” doesn’t have an authoritative definition. Search for one and you’ll find an obvious hallucination that made it all the way into official IBM documentation. I won’t repeat it hear as to not make things worse.

Second, **LLMs have goldfish-sized working memory**. That is, they’re held back by small context lengths. Some models are trained on larger contexts, but their [effective context length](https://github.com/NVIDIA/RULER) is usually much smaller. In practice, an LLM can hold several book chapters worth of comprehension “in its head” at a time. For code it’s 2k or 3k lines (code is token-dense). That’s the most you can work with at once. Compared to a human, it’s tiny. There are tools like [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) and fine-tuning to mitigate it… _slightly_.

Third, **LLMs are poor programmers**. At best they write code at maybe an undergraduate student level who’s read a lot of documentation. That sounds better than it is. The typical fresh graduate enters the workforce knowing practically nothing about software engineering. Day one on the job is the first day of their real education. In that sense, LLMs today haven’t even begun their real education.

_Writing new code is the easy part_. The hard part is maintaining code, and writing new code with that maintenance in mind. Even when an LLM produces code that works, there’s no thought to maintenance, nor could there be. In general the reliability of generate code follows the inverse square law by length, and generating more than a dozen lines at a time is fraught. I really tried, but never saw LLM output beyond 2–3 lines of code which I would consider acceptable.

Quality varies substantially by language. LLMs are better at Python than C, and better at C than assembly. I suspect it’s related to the difficulty of the language and the quality of the input. It’s trained on lots of terrible C — the internet is loaded with it after all — and probably the only labeled x86 assembly it’s seen is crummy beginner tutorials. Ask it to use SDL2 and it [reliably produces the common mistakes](https://nullprogram.com/blog/2023/01/08/) because it’s been trained to do so.

What about boilerplate? That’s something an LLM could probably do with a low error rate, and perhaps there’s merit to it. Though the fastest way to deal with boilerplate is to not write it at all. Change your problem to not require boilerplate.

Without taking my word for it, consider how it show up in the economics: If AI companies could deliver the productivity gains they claim, they wouldn’t sell AI. They’d keep it to themselves and gobble up the software industry. Or consider the software products produced by companies on the bleeding edge of AI. It’s still the same old, bloated web garbage everyone else is building. (My LLM research has involved navigating their awful web sites, and it’s made be bitter.)

In code generation, hallucinations are less concerning. You already knew what you wanted when you asked, so you can review it, and your compiler will help catch problems you miss (e.g. calling a hallucinated method). However, small context and poor code generation remain roadblocks, and I haven’t yet made this work effectively.

So then, what can I do with LLMs? A list is apt because LLMs love lists:

*   Proofreading has been most useful for me. I give it a document such as an email or this article (~8,000 tokens), tell it to look over grammar, call out passive voice, and so on, and suggest changes. I accept or reject its suggestions and move on. Most suggestions will be poor, and this very article was long enough that even ~70B models suggested changes to hallucinated sentences. Regardless, there’s signal in the noise, and it fits within the limitations outlined above. I’m still trying to apply this technique (“find bugs, please”) to code review, but so far success is elusive.
    
*   Writing short fiction. Hallucinations are not a problem; they’re a feature! Context lengths are the limiting factor, though perhaps you can stretch it by supplying chapter summaries, also written by LLM. I’m still exploring this. If you’re feeling lazy, tell it to offer you three possible story branches at each turn, and you pick the most interesting. Or even tell it to combine two of them! LLMs are clever and will figure it out. Some genres work better than others, and concrete works better than abstract. (I wonder if professional writers judge its writing as poor as I judge its programming.)
    
*   Generative fun. Have an argument with Benjamin Franklin (note: this probably violates the [Acceptable Use Policy](https://ai.meta.com/llama/use-policy/) of some models), hang out with a character from your favorite book, or generate a new scene of [Falstaff’s blustering antics](https://nullprogram.com/blog/2023/06/22/#76-henry-iv). Talking to historical figures has been educational: The character says something unexpected, I look it up the old-fashioned way to see what it’s about, then learn something new.
    
*   Language translation. I’ve been browsing foreign language subreddits through Gemma-2-2B translation, and it’s been insightful. (I had no idea German speakers were so distrustful of artificial sweeteners.)
    

Despite the short list of useful applications, this is the most excited I’ve been about a new technology in years!
