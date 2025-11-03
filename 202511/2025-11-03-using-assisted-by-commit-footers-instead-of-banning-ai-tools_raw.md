Title: Using Assisted-by commit footers instead of banning AI tools

URL Source: https://xeiaso.net/notes/2025/assisted-by-footer/

Markdown Content:
Published on 2025-11-02, 463 words, 2 minutes to read

It sounds like ceding ground to the pro-AI crowd, however if you get people to be honest about it then everyone benefits.

Something I've seen around the internet is that many projects want [a blanket policy of no AI tools being allowed](https://wiki.gentoo.org/wiki/Project:Council/AI_policy) for contributors. As much as I agree with the sentiment of policies like this, I don't think it's entirely realistic because it's trivial to lie about not using them when you actually do.

I think a better middle ground is something like [Fedora's AI-Assisted Contributions Policy](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/). This demands that you include a commit footer that discloses what AI tools you've used in your process, such as this:

```
Assisted-by: GPT-OSS 120b via OpenAI Codex (locally hosted)
```

Amusingly, you can actually tell AI agents to write this commit footer and they'll happily do it. Consider this part of [this repo's AGENTS.md file](https://github.com/Xe/site/blob/main/AGENTS.md) (AGENTS.md is a set of instructions for AI agents to know how to best contribute to the policy):

> **Attribution Requirements**
> 
> 
> AI agents must disclose what tool and model they are using in the "Assisted-by" commit footer:
> 
> 
> ```
> Assisted-by: [Model Name] via [Tool Name]
> ```
> 
> Example:
> 
> 
> ```
> Assisted-by: GLM 4.6 via Claude Code
> ```

Not only does this make it trivial for automation to detect when AI tools are being used (and add appropriate tagging so reviewers can be more particular), it lets you know which AI tools cause more issues in the longer run. This can help guide policy and assist contributors that want to use AI tooling into picking the best tools for the job.

Anyways, at a high level if you ask people to disclose what AI tools they are using and make it so that the default configuration of most AI tooling will just add that disclosure for you, people are much more likely to comply with that policy. I think that this is a better middle ground than having witch hunts trying to figure out who used what tool and letting it become a free ground for noisy, low‑quality contributions.

I want to see a future where people are allowed to experiment with fancy new tools. However, given the risks involved with low‑effort contributions causing issues, I think it's better for everyone to simply require an easy machine‑readable footer.

Also, if you want to put `Assisted-by: GNU Emacs`, I won't stop you.

This post was edited with help from GPT-OSS 120b on a DGX Spark, a device which only consumes 150 watts at maximum load. While I was writing this, I had Final Fantasy 14 open in the background to listen to bards perform in Limsa Lominsa. This made my workstation's RTX 4080 pull 150 watts of power constantly.

* * *

Facts and circumstances may have changed since publication. Please contact me before jumping to conclusions if something seems wrong or unclear.

Tags:

Copyright 2012-2025 Xe Iaso. Any and all opinions listed here are my own and not representative of any of my employers, past, future, and/or present.

Served by xesite v4 (/app/bin/xesite) with site version [73daac0f](https://github.com/Xe/site/commit/73daac0f489a092969a65dee2112a2789687079d) , source code available [here](https://github.com/Xe/site).