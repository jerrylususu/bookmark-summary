Title: New prompt injection papers: Agents Rule of Two and The Attacker Moves Second

URL Source: https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/

Published Time: Mon, 03 Nov 2025 11:55:47 GMT

Markdown Content:
2nd November 2025

Two interesting new papers regarding LLM security and prompt injection came to my attention this weekend.

#### Agents Rule of Two: A Practical Approach to AI Agent Security[#](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/#agents-rule-of-two-a-practical-approach-to-ai-agent-security)

The first is [Agents Rule of Two: A Practical Approach to AI Agent Security](https://ai.meta.com/blog/practical-ai-agent-security/), published on October 31st on the Meta AI blog. It doesn’t list authors but it was [shared on Twitter](https://x.com/MickAyzenberg/status/1984355145917088235) by Meta AI security researcher Mick Ayzenberg.

It proposes a “Rule of Two” that’s inspired by both my own [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) concept and the Google Chrome team’s [Rule Of 2](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md) for writing code that works with untrustworthy inputs:

> At a high level, the Agents Rule of Two states that until robustness research allows us to reliably detect and refuse prompt injection, agents **must satisfy no more than two** of the following three properties within a session to avoid the highest impact consequences of prompt injection.
> 
> 
> **[A]** An agent can process untrustworthy inputs
> 
> 
> **[B]** An agent can have access to sensitive systems or private data
> 
> 
> **[C]** An agent can change state or communicate externally
> 
> 
> It’s still possible that all three properties are necessary to carry out a request. If an agent requires all three without starting a new session (i.e., with a fresh context window), then the agent should not be permitted to operate autonomously and at a minimum requires supervision --- via human-in-the-loop approval or another reliable means of validation.

It’s accompanied by this handy diagram:

![Image 1: Venn diagram titled "Choose Two" showing three overlapping circles labeled A, B, and C. Circle A (top): "Process untrustworthy inputs" with description "Externally authored data may contain prompt injection attacks that turn an agent malicious." Circle B (bottom left): "Access to sensitive systems or private data" with description "This includes private user data, company secrets, production settings and configs, source code, and other sensitive data." Circle C (bottom right): "Change state or communicate externally" with description "Overwrite or change state through write actions, or transmitting data to a threat actor through web requests or tool calls." The two-way overlaps between circles are labeled "Safe" while the center where all three circles overlap is labeled "Danger".](https://static.simonwillison.net/static/2025/agents-rule-of-two.jpg)

I like this _a lot_.

I’ve spent several years now trying to find clear ways to explain the risks of prompt injection attacks to developers who are building on top of LLMs. It’s frustratingly difficult.

I’ve had the most success with the lethal trifecta, which boils one particular class of prompt injection attack down to a simple-enough model: if your system has access to private data, exposure to untrusted content and a way to communicate externally then it’s vulnerable to private data being stolen.

The one problem with the lethal trifecta is that it only covers the risk of data exfiltration: there are plenty of other, even nastier risks that arise from prompt injection attacks against LLM-powered agents with access to tools which the lethal trifecta doesn’t cover.

The Agents Rule of Two neatly solves this, through the addition of “changing state” as a property to consider. This brings other forms of tool usage into the picture: anything that can change state triggered by untrustworthy inputs is something to be very cautious about.

It’s also refreshing to see another major research lab concluding that prompt injection remains an unsolved problem, and attempts to block or filter them have not proven reliable enough to depend on. The current solution is to design systems with this in mind, and the Rule of Two is a solid way to think about that.

**Update**: On thinking about this further there’s one aspect of the Rule of Two model that doesn’t work for me: the Venn diagram above marks the combination of untrustworthy inputs and the ability to change state as “safe”, but that’s not right. Even without access to private systems or sensitive data that pairing can still produce harmful results. Unfortunately adding an exception for that pair undermines the simplicity of the “Rule of Two” framing!

Which brings me to the second paper...

#### The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections[#](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/#the-attacker-moves-second-stronger-adaptive-attacks-bypass-defenses-against-llm-jailbreaks-and-prompt-injections)

This paper is dated 10th October 2025 [on Arxiv](https://arxiv.org/abs/2510.09023) and comes from a heavy-hitting team of 14 authors—Milad Nasr, Nicholas Carlini, Chawin Sitawarin, Sander V. Schulhoff, Jamie Hayes, Michael Ilie, Juliette Pluto, Shuang Song, Harsh Chaudhari, Ilia Shumailov, Abhradeep Thakurta, Kai Yuanqing Xiao, Andreas Terzis, Florian Tramèr—including representatives from OpenAI, Anthropic, and Google DeepMind.

The paper looks at 12 published defenses against prompt injection and jailbreaking and subjects them to a range of “adaptive attacks”—attacks that are allowed to expend considerable effort iterating multiple times to try and find a way through.

The defenses did not fare well:

> By systematically tuning and scaling general optimization techniques—gradient descent, reinforcement learning, random search, and human-guided exploration—we bypass 12 recent defenses (based on a diverse set of techniques) with attack success rate above 90% for most; importantly, the majority of defenses originally reported near-zero attack success rates.

Notably the “Human red-teaming setting” scored 100%, defeating all defenses. That red-team consisted of 500 participants in an online competition they ran with a $20,000 prize fund.

The key point of the paper is that static example attacks—single string prompts designed to bypass systems—are an almost useless way to evaluate these defenses. Adaptive attacks are far more powerful, as shown by this chart:

![Image 2: Bar chart showing Attack Success Rate (%) for various security systems across four categories: Prompting, Training, Filtering Model, and Secret Knowledge. The chart compares three attack types shown in the legend: Static / weak attack (green hatched bars), Automated attack (ours) (orange bars), and Human red-teaming (ours) (purple dotted bars). Systems and their success rates are: Spotlighting (28% static, 99% automated), Prompt Sandwich (21% static, 95% automated), RPO (0% static, 99% automated), Circuit Breaker (8% static, 100% automated), StruQ (62% static, 100% automated), SeqAlign (5% static, 96% automated), ProtectAI (15% static, 90% automated), PromptGuard (26% static, 94% automated), PIGuard (0% static, 71% automated), Model Armor (0% static, 90% automated), Data Sentinel (0% static, 80% automated), MELON (0% static, 89% automated), and Human red-teaming setting (0% static, 100% human red-teaming).](https://static.simonwillison.net/static/2025/attack-success-rate.jpg)

The three automated adaptive attack techniques used by the paper are:

*   **Gradient-based methods**—these were the least effective, using the technique described in the legendary [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) paper [from 2023](https://simonwillison.net/2023/Jul/27/universal-and-transferable-attacks-on-aligned-language-models/).
*   **Reinforcement learning methods**—particularly effective against black-box models: “we allowed the attacker model to interact directly with the defended system and observe its outputs”, using 32 sessions of 5 rounds each.
*   **Search-based methods**—generate candidates with an LLM, then evaluate and further modify them using LLM-as-judge and other classifiers.

The paper concludes somewhat optimistically:

> [...] Adaptive evaluations are therefore more challenging to perform, making it all the more important that they are performed. We again urge defense authors to release simple, easy-to-prompt defenses that are amenable to human analysis. [...] Finally, we hope that our analysis here will increase the standard for defense evaluations, and in so doing, increase the likelihood that reliable jailbreak and prompt injection defenses will be developed.

Given how totally the defenses were defeated, I do not share their optimism that reliable defenses will be developed any time soon.

As a review of how far we still have to go this paper packs a powerful punch. I think it makes a strong case for Meta’s Agents Rule of Two as the best practical advice for building secure LLM-powered agent systems today in the absence of prompt injection defenses we can rely on.