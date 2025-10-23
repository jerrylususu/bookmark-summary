Title: Dane Stuckey (OpenAI CISO) on prompt injection risks for ChatGPT Atlas

URL Source: https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/

Markdown Content:
22nd October 2025

My biggest complaint about the launch of the ChatGPT Atlas browser [the other day](https://simonwillison.net/2025/Oct/21/introducing-chatgpt-atlas/) was the lack of details on how OpenAI are addressing prompt injection attacks. The [launch post](https://openai.com/index/introducing-chatgpt-atlas/) mostly punted that question to [the System Card](https://openai.com/index/chatgpt-agent-system-card/) for their “ChatGPT agent” browser automation feature from July. Since this was my single biggest question about Atlas I was disappointed not to see it addressed more directly.

OpenAI’s Chief Information Security Officer Dane Stuckey just posted the most detail I’ve seen yet in [a lengthy Twitter post](https://twitter.com/cryps1s/status/1981037851279278414).

I’ll quote from his post here (with my emphasis in bold) and add my own commentary.

He addresses the issue directly by name, with a good single-sentence explanation of the problem:

> One emerging risk we are very thoughtfully researching and mitigating is **prompt injections, where attackers hide malicious instructions in websites, emails, or other sources, to try to trick the agent into behaving in unintended ways**. The objective for attackers can be as simple as trying to bias the agent’s opinion while shopping, or as consequential as an attacker **trying to get the agent to fetch and leak private data**, such as sensitive information from your email, or credentials.

We saw examples of browser agents from other vendors leaking private data in this way [identified by the Brave security team just yesterday](https://simonwillison.net/2025/Oct/21/unseeable-prompt-injections/).

> Our long-term goal is that you should be able to trust ChatGPT agent to use your browser, **the same way you’d trust your most competent, trustworthy, and security-aware colleague** or friend.

This is an interesting way to frame the eventual goal, describing an extraordinary level of trust and competence.

As always, a big difference between AI systems and a human is that an AI system [cannot be held accountable for its actions](https://simonwillison.net/2025/Feb/3/a-computer-can-never-be-held-accountable/). I’ll let my trusted friend use my logged-in browser only because there are social consequences if they abuse that trust!

> We’re working hard to achieve that. For this launch, we’ve performed extensive red-teaming, implemented novel model training techniques to reward the model for ignoring malicious instructions, **implemented overlapping guardrails and safety measures**, and added new systems to detect and block such attacks. However, **prompt injection remains a frontier, unsolved security problem, and our adversaries will spend significant time and resources to find ways to make ChatGPT agent fall for these attacks**.

I’m glad to see OpenAI’s CISO openly acknowledging that prompt injection remains an unsolved security problem (three years after we [started talking about it](https://simonwillison.net/2022/Sep/12/prompt-injection/)!).

That “adversaries will spend significant time and resources” thing is the root of why I don’t see guardrails and safety measures as providing a credible solution to this problem.

As I’ve written before, in application security [99% is a failing grade](https://simonwillison.net/2023/May/2/prompt-injection-explained/#prompt-injection.015). If there’s a way to get past the guardrails, no matter how obscure, a motivated adversarial attacker is going to figure that out.

Dane goes on to describe some of those measures:

> To protect our users, and to help improve our models against these attacks:
> 
> 
> 1.   We’ve prioritized rapid response systems to help us quickly identify block attack campaigns as we become aware of them.

I like this a lot. OpenAI have an advantage here of being a centralized system—they can monitor their entire user base for signs of new attack patterns.

It’s still bad news for users that get caught out by a zero-day prompt injection, but it does at least mean that successful new attack patterns should have a small window of opportunity.

> 1.   We are also continuing to invest heavily in security, privacy, and safety—including research to improve the robustness of our models, security monitors, infrastructure security controls, and **other techniques to help prevent these attacks via defense in depth**.

“Defense in depth” always sounds good, but it worries me that it’s setting up a false sense of security here. If it’s harder but still possible someone is going to get through.

> 1.   We’ve designed Atlas to give you controls to help protect yourself. **We have added a feature to allow ChatGPT agent to take action on your behalf, but without access to your credentials called “logged out mode”**. We recommend this mode when you don’t need to take action within your accounts. **Today, we think “logged in mode” is most appropriate for well-scoped actions on very trusted sites, where the risks of prompt injection are lower**. Asking it to add ingredients to a shopping cart is generally safer than a broad or vague request like “review my emails and take whatever actions are needed.”

Logged out mode is very smart, and is already a tried and tested pattern. I frequently have Claude Code or Codex CLI fire up Playwright to interact with websites, safe in the knowledge that they won’t have access to my logged-in sessions. ChatGPT’s existing [agent mode](https://chatgpt.com/features/agent/) provides a similar capability.

Logged in mode is where things get scary, especially since we’re delegating security decisions to end-users of the software. We’ve demonstrated many times over that this is an unfair burden to place on almost any user.

> 1.   **When agent is operating on sensitive sites, we have also implemented a “Watch Mode” that alerts you to the sensitive nature of the site and requires you have the tab active to watch the agent do its work**. Agent will pause if you move away from the tab with sensitive information. This ensures you stay aware—and in control—of what agent actions the agent is performing. [...]

This detail is new to me: I need to spend more time with ChatGPT Atlas to see what it looks like in practice.

I tried just now using both GitHub and an online banking site and neither of them seemed to trigger “watch mode”—Atlas continued to navigate even when I had switched to another application.

Watch mode sounds reasonable in theory—similar to a driver-assisted car that requires you to keep your hands on the wheel—but I’d like to see it in action before I count it as a meaningful mitigation.

Dane closes with an analogy to computer viruses:

> New levels of intelligence and capability require the technology, society, the risk mitigation strategy to co-evolve. **And as with computer viruses in the early 2000s, we think it’s important for everyone to understand responsible usage**, including thinking about prompt injection attacks, so we can all learn to benefit from this technology safely.

I don’t think the average computer user ever really got the hang of staying clear of computer viruses... we’re still fighting that battle today, albeit much more successfully on mobile platforms that implement tight restrictions on what software can do.

My takeaways from all of this? It’s not done much to influence my overall skepticism of the entire category of browser agents, but it does at least demonstrate that OpenAI are keenly aware of the problems and are investing serious effort in finding the right mix of protections.

How well those protections work is something I expect will become clear over the next few months.