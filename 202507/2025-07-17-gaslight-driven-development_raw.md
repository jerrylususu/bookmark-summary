Title: Gaslight-driven development

URL Source: https://tonsky.me/blog/gaslight-driven-development/

Published Time: 2025-07-16

Markdown Content:
Any person who has used a computer in the past ten years knows that doing meaningless tasks is just part of the experience. Millions of people create accounts, confirm emails, dismiss notifications, solve captchas, reject cookies, and accept terms and conditions—not because they particularly want to or even need to. They do it because that’s what the computer told them to do. Like it or not, we are already serving the machines.

Well, now there is a new way to serve our silicon overlords. LLMs started to have opinions on how your API _should_ look, and since 90% of all code will be written by AI [comes September](https://www.businessinsider.com/anthropic-ceo-ai-90-percent-code-3-to-6-months-2025-3), we have no choice but to oblige.

You might’ve heard a story of Soundslice [adding a feature because ChatGPT kept telling people it exists](https://www.holovaty.com/writing/chatgpt-fake-feature/). We see the same at Instant: for example, we used `tx.update` for both inserting and updating entities, but LLMs kept writing `tx.create` instead. Guess what: we now have `tx.create`, too.

Is it good or is it bad? It definitely feels strange. In a sense, it’s helpful: LLMs here have seen millions of other APIs and are suggesting the most obvious thing, something every developer would think of first, too.

It’s also a unique testing device: if developers use your API wrong, they blame themselves, read the documentation, and fix their code. In the end, you might never learn that they even had the problem. But with ChatGPT, you yourself can experience “newbie’s POV” at any time.

Of course, this approach doesn’t work if you are trying to do something new and unique. LLMs just won’t “get it”. But how many of us are doing something new and unique? Maybe, API is not the place to get clever? Maybe, for most cases, it’s truly best if you did the most obvious thing?

So welcome to the new era. AI is not just using tools we gave it. It now has opinions about how these tools should’ve been made. And instead of asking nicely, it gaslights everybody into thinking that’s how it’s always been.
