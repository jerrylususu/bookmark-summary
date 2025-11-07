Title: How I use AI (Oct 2025)

URL Source: https://ben.stolovitz.com/posts/how_use_ai_oct_2025/

Published Time: 2025-10-31T00:00:00.000Z

Markdown Content:
I want to take stock of how I’m currently using AI — at least, the cool stuff like LLMs that we _call_ “AI.” I’m curious to see this evolve in the coming years.

![Image 1: A person wonders at a group of eager robots](https://ben.stolovitz.com/_astro/cover-dark.CwT1zN4s_dqtF0.png)![Image 2: A person wonders at a group of eager robots](https://ben.stolovitz.com/_astro/cover.BUA-tVJ__Z2oAxeN.png)
Background
----------

I believe I use AI fairly typically for a software engineer, if slightly more than average. I’ve been working in the AI space since slightly before the announcement of GPT-3 in 2020.

I use AI in a few particular ways:

*   Coding
*   Research & search
*   Summarization & transcription
*   Writing
*   Art & music

This is, of course, purely my opinion & speculation. If you have different ways of using AI, I’d love to know!

Coding
------

Coding is the part of my life most changed with AI, by far.

I started using Copilot very early: Microsoft quickly deployed access to Github Copilot internally, so I’ve used that since nearly Day 1. I’m a **huge** fan. Its suggestions are incredible and save me (hundreds of?) keystrokes every day. I expect other tools, like Claude Code, are just as good.

![Image 3: Code with a line of about 50 chars italicized](https://ben.stolovitz.com/_astro/autocomplete.DIDqaQT6_Z1KHl8P.webp)

Copilot autocomplete correctly predicting an entire line of code (the italic line)

I mainly use **autocomplete**:

*   It completes stuff _I already know how to do_. It’s very good at predicting my next line, so I simply tab-complete much of my code. Google reported in 2024 that [50% of code characters written internally](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/#:~:text=assisting%20in%20the%20completion%20of%2050%25%20of%20code%20characters) were from AI tab completion — it simply _is_ that good.

*   It helps me _discover idiomatic patterns & syntax_. It reliably predicts how to deserialize JSON in C#, which I’d otherwise need to look up.

*   (It’s mediocre at _writing complicated algorithms_. It tends to spew pages of incorrect code. I’m still finding the balance, but it often takes me longer to validate its code than to write it myself).

Altogether, it’s good enough that I’ll frequently _wait for a suggestion to appear_, even if it takes thirty seconds. In these respects, it’s a beefed-up [IntelliSense](https://code.visualstudio.com/docs/editing/intellisense), and it’s magical. 10 out of 10.

I’ve also started using **agent mode**, where it plans & writes complicated changes on its own. It’s been less “magically good” and less mind-blowingly useful. But its quality often surprises me.

I like to tag these AI commits with `(AI)` so I can find them later: here’s [a commit improving logging](https://github.com/citelao/systray-doom/commit/ccb889ff2ff1ec4a00f92f5f7d581564ddad5581) in a project, and a subsequent [commit making the output prettier](https://github.com/citelao/systray-doom/commit/aa1c3c7bf5191eab887a0a12c5eb333d944e2ee7). These commits took about ~10min to generate; writing the code manually would have taken much longer since I’m unfamiliar with logging in .NET. I’ve tried before, but documentation was so dense that I failed multiple times. Agents are helping me understand idioms that ASP.NET developers understand implicitly.

Despite that, I still need to babysit agents. They tend to get lost when doing unconventional things, like using opaquely-documented Win32 APIs or calling PowerShell from C#. The logging commits exemplify what agents excel at: implementing a common idiom that has lots of training data, so AI knows it well.

This is why I’m still tepid on **agentic pull requests**. In my experience, agents still need a human in the loop to validate changes & unblock errors. PRs lengthen that loop, which slows you down (you now must check out a branch & build it to validate any changes). I was able to use Codex to [add GitHub actions](https://github.com/citelao/systray-doom/pull/4) to a project of mine, but I gave up on [a subsequent PR](https://github.com/citelao/systray-doom/pull/6/files) auto-incrementing versions in favor of [a manual PR](https://github.com/citelao/systray-doom/pull/7) I wrote with agents locally. The agentic PR simply had too many errors to be worth fixing.

AI **code review** is a bit better. I’ve worked with agents that leave tedious, harmful comments (like “consider catching exceptions” in code where doing so would mask larger problems). But Codex caught a _severe_ potential use-after-free bug [in some of my hand-written code](https://github.com/citelao/systray-doom/pull/8#discussion_r2461845675). That’s pretty cool.

![Image 4: Codex review comment: 'Built menu items hold unpinned string pointers'](https://ben.stolovitz.com/_astro/code-review.BoGuvG2z_Zddpfs.webp)

AI code review points out a potentially big issue

I only rarely use **inline editing** (I usually use autocomplete instead), and agent mode has fully replaced the old one-shot **code mode** in GitHub Copilot (code mode rarely had enough context to be useful).

In short:

|  | Usefulness | Notes |
| --- | --- | --- |
| **Autocomplete** | 👍👍👍 | Industry-changing! |
| **Agent mode** | 👍 | Increasingly useful. Needs documentation & testability to be successful |
| **Agentic PRs** | 🤔 | Validation loop too slow to be productive |
| **Code review** | 🤔 | Need to sort out signal from noise |
| **Inline editing** | ❌ | Slower to use than autocomplete |
| **Code mode** | ❌ | Usurped by agent mode |

Research & search
-----------------

Research & search are a close second in "life changiness": they’re the most frequent reason I use ChatGPT.

I find LLMs mediocre at **traditional search**. They’re not search engines: when I ask ChatGPT (or Claude) to find good Italian food, it reliably hallucinates restaurants that closed in 2023. When I ask the LLMs to “cite your sources,” they perform much better (which makes sense: they are trained on old data, so asking them to search the web helps). Even with citations, though, LLMs have been terrible at **product searches** like [finding a new USB hub](https://chatgpt.com/share/68f03caf-9194-8013-ac56-611a79c50e5f). I suspect that’s because searching for products _without_ AI is also similarly frustrating: results are filled with advertisements and SEO spam, most large reviewers recommend the same few products, and Redditors flock to faddy, niche, expensive stuff ([relevant ProZD](https://www.youtube.com/watch?v=4ZK8Z8hulFg)). I’m not surprised LLMs offer vague and uninspired advice.

Instead I use LLMs for **pub facts**—stuff I’d ask my partner at a pub. “Who’s that guy who was in that movie where he did that thing?” They are incredible at this. Finding that one Reddit thread, that one article, or that one book. ChatGPT was able to [find an article I saw on Hacker News](https://chatgpt.com/share/68f03bcb-ba24-8013-9fa9-f14b2c79ae6f), despite me telling it an incorrect date, and it [one-shotted a book](https://chatgpt.com/share/68f03bfe-ad40-8013-ade6-87e7cfccd00c) that I could not find after several manual searches. (Notably, Claude was [unable to find the same article](https://claude.ai/share/779988a5-8950-4182-abf4-1f7dfd9596c1). Unsure why).

![Image 5: ChatGPT: 'Do you mean Trust[...]?'](https://ben.stolovitz.com/_astro/trust-one-shot.BN9zCZbU_1isU60.webp)

ChatGPT finds a book

I also enjoy using LLMs to **explain well-known concepts**. I’ll ask them things an industry expert would instantly know. I’ve used them to help me [use command-line tools](https://chatgpt.com/share/68fed6b3-bca0-8013-9996-067816baee88) I don’t frequently use, guess at syntax [when writing a plugin](https://chatgpt.com/share/68fee21c-0918-8013-b880-8b5c11be3283) and [when using an unfamiliar markup language](https://chatgpt.com/share/68fee290-e10c-8013-811b-8345d1ca1cb8), and even [find the right airport terminal](https://chatgpt.com/share/68fee271-a098-8013-a374-ab2babfbbeef) for a flight. It’s… kinda nice to search [“superman after credits scene”](https://www.google.com/search?q=superman+after+credits+scene) and actually get an answer in the [AI overview](https://search.google/ways-to-search/ai-overviews/) at the top.

However, I don’t trust LLM answers much. ChatGPT confidently claimed a Switch 2 could use Switch 1 docks ([it cannot](https://en-americas-support.nintendo.com/app/answers/detail/a_id/68426/~/compatibility-of-nintendo-switch-with-nintendo-switch%26nbsp%3B2#s1q2)). It was [simply incorrect about an obscure .NET API](https://chatgpt.com/share/68fee9c8-1cf8-8013-9b28-d26c53adc8bd). And I don’t have to write much about how Google’s overviews [are](https://mashable.com/article/google-ai-search-memes-mistakes)[very](https://mashable.com/article/google-ai-overviews-2025-review)[frequently](https://www.ktvq.com/news/local-news/billings-police-dont-trust-google-ai-for-local-emergency-phone-numbers)[wrong](https://bsky.app/profile/gregjenner.bsky.social/post/3lnhxkdywzc2m). I’m not as gloomy as many, but it’s clear that these machines are not human experts. [Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing) is an expert, and his [2-sentence comment](https://stackoverflow.com/questions/61601132/what-is-the-use-of-a-process-with-no-threads-in-windows#comment108965999_61601132) on an old StackOverflow question of mine is better than the, uh, [mediocre answers](https://chatgpt.com/share/68f040d8-9a60-8013-8bc2-ef3676b9a0a2) that [LLMs give](https://chatgpt.com/share/68f040fa-6d18-8013-9bef-531ea72509e8). They’ve had plenty of time to index his answer.

![Image 6: ChatGPT claims 'the Switch 1 dock should work perfectly fine with the Switch 2.'](https://ben.stolovitz.com/_astro/switch-compat.DhiwUrUW_Z2mbjeY.webp)

ChatGPT is wrong about Nintendo Switch docks

My trepidation extends to complex **literature searches**. I use LLMs as secondary librarians when I’m doing research. They reliably find primary sources (articles, papers, etc.) that I miss in my initial searches.

But these searches are _dangerous_. I distrust LLM librarians. There is so much data in the world: you can (in good faith!) find evidence to support almost any position or conclusion. ChatGPT is not a human, and, unlike teachers & librarians & scholars, ChatGPT does not have a consistent, legible worldview. In my experience, it readily agrees with any premise you hand it — and brings citations. It may have read every article that can be read, but it has no real opinion — so it is not a credible expert.

![Image 7: ChatGPT chat: How fast is human latency detection in interaction loops](https://ben.stolovitz.com/_astro/latency-detection.-ap5jazP_Z102OI7.webp)

ChatGPT does not have a worldview: how much of [this answer](https://chatgpt.com/share/6906475e-8ee0-8013-b56b-311b4d669408) is right? How much is sycophancy?

For example, ChatGPT was able to find lots of citations regarding [human latency thresholds](https://chatgpt.com/share/6906475e-8ee0-8013-b56b-311b4d669408) and [some keyboarding topics I’m researching](https://chatgpt.com/share/68f041e0-2070-8013-b6d8-511c77bff30d). But many of its quotes were out-of-date (or hallucinations)! In this case, _I_ am the expert, wondering if there are additional sources worth citing; I can audit AI output. But AI has [almost fooled](https://arstechnica.com/tech-policy/2025/05/judge-initially-fooled-by-fake-ai-citations-nearly-put-them-in-a-ruling/#:~:text=%20It%20almost%20led%20to%20the%20scarier%20outcome%20(from%20my%20perspective)%20of%20including%20those%20bogus%20materials%20in%20a%20judicial%20order.) expert judges and lawyers already! Woe to any perplexed student seeking guidance.

|  | Usefulness | Notes |
| --- | --- | --- |
| **Traditional search** | ❌ | Worse than just using Google |
| **Product search** | ❌ | Poisoned by the Internet |
| **Pub facts** | 👍👍 | Makes me more annoying at parties! |
| **Explaining well-known concepts** | 👍 | Sometimes better than the docs. Mostly correct. |
| **Literature searches** | ⚠️👍 | ChatGPT finds evidence to support any claim, and that’s scary |

Summarization & transcription
-----------------------------

Perhaps it’s odd to emphasize **summarization** and **transcription**, but LLMs are _so dang good at it_.

LLMs care not about tedium. They’ll read hundreds of pages & spit out a perfect summary in less than a minute. For example, Microsoft Teams can automatically summarize meetings, and its summaries are incredible. It’s humbling to see an hour of discussion reduced to 5 bullet points.

I’ve heard concerns that LLMs [are inattentive to stuff in the middle of long documents](https://arxiv.org/abs/2307.03172), but I haven’t experimented enough to notice firsthand. I do know that LLMs need _lots_ of prompting to produce short-enough, clear summaries. They otherwise tend to ramble.

|  | Usefulness | Notes |
| --- | --- | --- |
| **Summarization** | 👍👍 | So good that it’s no longer magical, but not super necessary day-to-day |
| **Transcription** | 👍👍 | Ditto |

Writing
-------

I do not use AI to **write from scratch**. Nor do I use it as an outlining aid.

That’s partly selfishness: clear communication is a rare skill among software engineers. Why cede an opportunity to practice?

But it’s also practicality: every document relies on context that LLMs have no access to (because it’s in emails or from a meeting or on paper or in your brain). So a generated document is guaranteed to be hallucinated pablum. Why would I want to hallucinate a dev spec — the document I use to get feedback on & plan months of work?

At work, my goal is to communicate _my_ most important ideas. Not AI’s. I want my words to be purposeful & apt. I want to build lovely things. That is not served by filling my colleagues’ inboxes with vomit.

![Image 8: A perplexed person attempts to read a ream of documents provided by a business-like robot](https://ben.stolovitz.com/_astro/vomit-dark.xhlY2zul_Z11n2g5.png)![Image 9: A perplexed person attempts to read a ream of documents provided by a business-like robot](https://ben.stolovitz.com/_astro/vomit.CFeZeYMp_rqroy.png)

That is not served by filling my colleagues’ inboxes with vomit

Likewise, this blog is art to me. I am a [happy little rat of NIMH, making my art](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/#:~:text=you%20live%20an%20idyllic%20life%20lounging%20about%2C%20eating%2C%20and%20composing%20great%20works%20of%20art), and I have no desire to cede that art to a machine. I’m fine using them to help me **find good words** (e.g. [finding a word](https://chatgpt.com/share/6902d18b-036c-8013-bdb4-09a6a50c7fdc) for [TikTok will always be temporary](https://ben.stolovitz.com/posts/tiktok_will_always_be_temporary#:~:text=stuff%20hardens%2C-,calcifies,-.%20One%20day%2C%20it)), but I believe I communicate effectively & clearly. I have my friends edit: that is a joyous process (my editors enjoy it, right?). Interfacing with a machine is not.

So I don’t ask the machines to write for me.

AI is an _uncanny_**editor** though. I recently asked both Claude and ChatGPT for feedback on some formal documents I was writing, and they were great! These documents had multiple pages of guidelines; I pasted my draft, I pasted the guidelines, and I asked for suggestions. The LLMs identified critical gaps in my responses & punched up the prose.

It’s scary how good they can be. I’ve taken to _avoiding AI’s verbatim suggestions_ and rewriting on my own — it often rephrases things _so well_ that I worry it will usurp my voice. So I don’t edit with AI on this blog or in my personal writing, although I wonder if my opinion here will ever change.

Luckily, LLMs still need good grounding to write well. Without clear human ideas, their writing is verbose and insipid. And I’ve seen Claude miss rhetorical patterns that would have been obvious to a human reader. But when I have a good idea, these machines can make it _so_ much better. It’s terrifying.

|  | Usefulness | Notes |
| --- | --- | --- |
| **Writing from scratch** | ❌ | Ew. Why? |
| **Finding good words** | 👍👍 | Good, clean fun |
| **Editing** | ⚠️👍👍👍 | Scary good. |

Art & music
-----------

Lastly, art. I have not found a great use for **image generation**. I used Bing to generate playlist art for my Spotify playlists & a few email memes, but I’ve stopped. I don’t find it valuable. Plus, I dislike any AI art I notice. Cover photos on blogs, bad comics on social media, ew. It _is_ useful, but in a stupid way: it’s a signal that accompanying text will also be AI-generated.

![Image 10: My Bing-generated art on my Spotify playlist](https://ben.stolovitz.com/_astro/spotify.CQcebfdZ_Z2hGmbU.webp)

My AI playlist art

I’m certain of this distaste now that I’ve started seeing AI art in the physical world. There’s a clothing store near me with an AI-generated mural, and I believe I saw AI-designed merchandise at a museum gift shop. Gross! It’s off-putting to see those humanless pictures in real life.

Why would I add to the slop?

I think **music generation** is headed down the same path. I don’t generate or plan to generate any music with AI myself, but I’ve already heard several _lovely_ AI-generated songs this year. One in particular — a song about [transporting steel coils](https://www.instagram.com/p/DPFMae9Eq-y/) ("I’ve been curious/​why steel coils are transported on their side/​instead of flat…")—inspired me to start writing my own music again. But I think I’ll get tired of it quickly.

Perhaps the best that can be said of AI art is that it lowers the bar to create. At its best, it empowers us to invent beyond art’s typical cliches. Producing a song takes hundreds of hours — so if you asked me to record a rhymeless, tuneless song about steel coil transportation (or a perhaps-copyright-infringey [song about Warhammer characters](https://www.youtube.com/watch?v=MXZrp_NaozI)) I’d laugh at you. I’d be wrong.

![Image 11: learningwithlyrics' Instagram steel coils post](https://ben.stolovitz.com/_astro/steel-coils.Dpw94cJe_ApIuX.webp)

The [steel coils song](https://www.instagram.com/p/DPFMae9Eq-y/) is silly and nonsensical… and delightful

But in practice, I think AI art gets suborned for laziness, stinginess, and grift. It is a shame that these songs are not voiced by human session singers, laughing at the lyrics in their recording booths. Art should increase human connection, not obsolete it. I do not want to use a faux-Ghibli portrait as my profile picture. And if you ask me: would I like AI to generate some art today?

I’d rather doodle.

|  | Usefulness | Notes |
| --- | --- | --- |
| **Image generation** | ❌ | Unpleasant when I detect it. Less fun than drawing a stick figure. |
| **Music generation** | 🤔 | I bet I’ll dislike it soon |

Conclusion (and “boring” AI)
----------------------------

Overall, this new wave of AI has transformed how I work. Autocompletion for my coding & human-like chat for random tip-of-my-tongue questions — awesome.

I’m confident we’re just starting to see what AI can achieve. Even if models stay the same, I _know_ we haven’t fully explored what they can do. LLMs are still in their “wondrous” phase; compare that to all the AI we take for granted. Good search, good recommendations, spellcheck, autocomplete. I simply expect to talk to my phone while I drive, and I rely on Siri to schedule my reminders.

The new AI will become normal, too. It will become pedestrian. There’s lots of good in what we have now, lots of mediocre, lots of bad, lots of _scary_. I hope it’s useful to document what this feels like, when it’s all new.

When it’s normal, I hope it’s mostly good.

* * *

_Thanks to Atherai Maran for editing._