Title: Enough AI copilots! We need AI HUDs

URL Source: https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds

Markdown Content:
In my opinion, one of the best critiques of modern AI design comes from [a 1992 talk](https://cgi.csc.liv.ac.uk/~coopes/comp319/2016/papers/UbiquitousComputingAndInterfaceAgents-Weiser.pdf) by the researcher [Mark Weiser](https://en.wikipedia.org/wiki/Mark_Weiser) where he ranted against “copilot” as a metaphor for AI.

This was 33 years ago, but it’s still incredibly relevant for anyone designing with AI.

Weiser’s rant[](https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds#weisers-rant)
--------------------------------------------------------------------------------------------------------

Weiser was speaking at an [MIT Media Lab event](https://www.dropbox.com/scl/fo/axpzd925tcsnkc9x5nd51/AJMdLqxafEYFun4Ns6fqMHo?dl=0&e=1&preview=frames_1992_014_Nov.pdf&rlkey=znit21hyth8w24m6gm02rq2y7) on “interface agents”. They were grappling with many of the same issues we’re discussing in 2025: how to make a personal assistant that automates tasks for you and knows your full context. They even had a human “butler” on stage representing an AI agent.

Everyone was super excited about this… except Weiser. He was opposed to the whole idea of agents! He gave this example: how should a computer help you fly a plane and avoid collisions?

**The agentic option is a “copilot” — a virtual human who you talk with to get help flying the plane.** If you’re about to run into another plane it might yell at you “collision, go right and down!”

Weiser offered a different option: **design the cockpit so that the human pilot is naturally aware of their surroundings.** In his words: “You’ll no more run into another airplane than you would try to walk through a wall.”

Weiser’s goal was an “invisible computer"—not an assistant that grabs your attention, but a computer that fades into the background and becomes "an extension of [your] body”.

![Image 1](https://www.geoffreylitt.com/images/article_images/weiser-slide.png?1753652074)

Weiser’s 1992 slide on airplane interfaces

HUDs[](https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds#huds)
---------------------------------------------------------------------------------------

There’s a tool in modern planes that I think nicely illustrates Weiser’s philosophy: **the Head-Up Display (HUD), which overlays flight info like the horizon and altitude on a transparent display directly in the pilot’s field of view.**

A HUD feels completely different from a copilot! You don’t talk to it. It’s literally part invisible—you just become naturally aware of more things, as if you had magic eyes.

![Image 2](https://www.geoffreylitt.com/images/article_images/copilot-hud.png?1753652074)

Designing HUDs[](https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds#designing-huds)
-----------------------------------------------------------------------------------------------------------

OK enough analogies. What might a HUD feel like in modern software design?

One familiar example is spellcheck. Think about it: **spellcheck isn’t designed as a “virtual collaborator” talking to you about your spelling.** It just instantly adds red squigglies when you misspell something! You now have a new sense you didn’t have before. It’s a HUD.

(This example comes from Jeffrey Heer’s excellent [Agency plus Automation](https://idl.cs.washington.edu/files/2019-AgencyPlusAutomation-PNAS.pdf) paper. We may not consider spellcheck an AI feature today, but it’s still a fuzzy algorithm under the hood.)

![Image 3](https://www.geoffreylitt.com/images/article_images/spellcheck.png?1753652074)

Spellcheck makes you aware of misspelled words without an “assistant” interface.

Here’s another personal example from AI coding. Let’s say you want to fix a bug. The obvious “copilot” way is to open an agent chat and ask it to do the fix.

But there’s another approach I’ve found more powerful at times: **use AI to build a custom debugger UI which visualizes the behavior of my program!** In one example, I [built a hacker-themed debug view of a Prolog interpreter](https://www.geoffreylitt.com/2024/12/22/making-programming-more-fun-with-an-ai-generated-debugger).

With the debugger, I have a HUD! I have new senses, I can see how my program runs. The HUD extends beyond the narrow task of fixing the bug. I can ambiently build up my own understanding, spotting new problems and opportunities.

Both the spellchecker and custom debuggers show that automation / “virtual assistant” isn’t the only possible UI. We can instead use tech to build better HUDs that enhance our human senses.

Tradeoffs[](https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds#tradeoffs)
-------------------------------------------------------------------------------------------------

I don’t believe HUDs are universally better than copilots! But I do believe **anyone serious about designing for AI should consider non-copilot form factors that more directly extend the human mind.**

So when should we use one or the other? I think it’s quite tricky to answer that, but we can try to use the airplane analogy for some intuition:

When pilots just want the plane to fly straight and level, they fully delegate that task to an autopilot, which is close to a “virtual copilot”. But if the plane just hit a flock of birds and needs to land in the Hudson, the pilot is going to take manual control, and we better hope they have great instruments that help them understand the situation.

In other words: routine predictable work might make sense to delegate to a virtual copilot / assistant. But when you’re shooting for extraordinary outcomes, perhaps the best bet is to equip human experts with new superpowers.

* * *

Further reading[](https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds#further-reading)
-------------------------------------------------------------------------------------------------------------

*   A nice discussion of one approach to this idea can be found in [Using Artificial Intelligence to Augment Human Intelligence](https://distill.pub/2017/aia/) by Michael Nielsen and Shan Carter.
*   A more cryptic take on the same topic: [Is chat a good UI for AI? A Socratic dialogue](https://www.geoffreylitt.com/2025/06/29/chat-ai-dialogue)
*   A discussion of how the the HUD philosophy intersects with on-demand software creation: [Malleable software in the age of LLMs](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming)
