Title: The three great virtues of an AI-assisted programmer

URL Source: https://www.seangoedecke.com/llm-user-virtues/

Markdown Content:
In 1991, Larry Wall famously [wrote](https://wiki.c2.com/?LazinessImpatienceHubris) that the three great virtues of a programmer were “laziness, impatience, and hubris”. A programmer should be lazy enough that they go to great effort to automate away manual work, impatient enough to write fast software, and have enough hubris that they believe they can write software other people will love. I write a lot about [virtue](https://www.seangoedecke.com/character-in-software-engineering) in software engineering, and in general I agree with Larry Wall’s three virtues. In particular, I think hubris is critical. A software engineer often needs to have the completely unreasonable confidence that they can fix any problem they encounter. I have seen many technically-strong engineers struggle because they lack this confidence. However, I worry that the three virtues are somewhat obsolete in the age of AI.

### Agentic coding and the three vices

Laziness, impatience and hubris are some of the strongest reasons to try and use agentic AI tools for programming (like Cursor, Copilot Agent, or Cline). Laziness and impatience are obvious: I can’t be bothered to sit down and write this myself, so I’ll throw it at the LLM. Anyone who’s seen the breathless hype surrounding these tools - engineers claiming to be 10x or 1000x more productive - can attest to the hubris. Some people truly believe that with a smart enough AI model they can do anything without needing to understand the solution themselves.

But these traits make it hard to _stop_ using AI. Taken together, they create a pattern of usage that I like to call “slot-machine coding”: continuously pulling the “solve this problem” lever in the hopes that this time the perfect solution will fall out. As Quentin Anthony [said](https://x.com/QuentinAnthon15/status/1943948796414898370) on Twitter, it’s more fun to press tab in Cursor for five hours than to spend one hour carefully debugging. This is a very plausible explanation for the recent surprising result in the [METR study](https://www.seangoedecke.com/impact-of-ai-study), where engineers felt like they were ~20% faster when they used AI, but were actually ~20% _slower_. It’s often faster to dig in and spend the time figuring out the problem - but what if slightly tweaking the prompt would get Copilot to instantly solve it for you this time? Just one more run.

The slow cycle-time of agentic AI tooling also invites quick distractions. Quentin also [tweeted](https://x.com/QuentinAnthon15/status/1943948803348082850) about this, but it’s a pattern I’ve observed in myself: if your development cycle involves a lot of 5-30 second wait times, it’s very tempting to spend that time (or longer) scrolling on your phone or in a browser tab. This is secretly one of the hardest things about programming with agentic AI: finding a useful way to spend the time while you’re waiting for the LLM agent to spin away.

### Agentic coding virtues

Given all that, I’d say that the first virtue of AI-assisted programming is **the obsession to keep your own mind working at the problem**. Instead of mindlessly letting the agent run, you should be actively tracking what it’s doing, or failing that, thinking about the original problem and trying to come to a deep understanding of what a solution should look like. Definitely don’t just sit on your phone! You should not start thinking when the AI agent has some output for you to look at - that’s far too late. Instead, you should incorporate the AI agent output into your ongoing stream of thought about the problem.

The second virtue of AI-assisted programming is **the impatience to eject and work it out yourself**. If the AI solution is almost but not quite there, much of the time you should fix it yourself instead of trying to prompt the agent to fix it. When you can see what needs doing, it’s usually faster to just do it. More importantly, when the AI solution gets stuck, you should be willing to jump in and solve the remainder of the problem on your own. Don’t get trapped in the slot-machine loop where you hope that one more run will figure it out! Be willing to say “well, looks like this problem isn’t a great fit for AI” and do it yourself. Try to be an active coworker with the LLM instead of just someone who gives it tasks.

The third virtue of AI-assisted programming is **suspicion of what the AI is doing**. Instead of being dazzled by AI-generated solutions, your default attitude should be that the LLM has probably screwed something up that you have to fix by hand. It’s a mistake to treat AI like you would treat a human coworker - a human coworker who had the strengths of AI would be very strong indeed, and would have earned a fair amount of trust. But AI doesn’t deserve that trust, because it will cheerfully make mistakes that an equivalently-competent human would never make. If you’re accepting AI-generated solutions, you must double and triple-check.

### Summary

If laziness, impatience and hubris were the cardinal virtues of programming by hand, obsession, impatience and suspicion are the virtues of AI-assisted programming. Impatience appears in both lists, but in a very different form: the first is about software in general, while the second is about being unwilling to wait for the AI to solve a problem that you can easily solve yourself.

To borrow a term from computer-assisted chess, we’re in the era of _centaurs_: computer assistance is good enough that it can make a human much stronger, but not yet good enough that it can completely outclass any human attempt to help. The best AI-assisted programmers are thus the ones who can push their own programming ability back into the agentic workflow: by continuing to think about the problem, by being willing to do parts of it on their own, and by distrusting any purely AI-generated output until they’ve worked through it themselves.

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

July 14, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *
