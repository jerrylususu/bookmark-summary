Title: My AI Skeptic Friends Are All Nuts

URL Source: https://fly.io/blog/youre-all-nuts/

Markdown Content:
![Image 1: A psychedelic landscape.](https://fly.io/blog/youre-all-nuts/assets/whoah.png)

Image by[Annie Ruygt](https://annieruygtillustration.com/)

A heartfelt provocation about AI-assisted programming.

Tech execs are mandating LLM adoption. That’s bad strategy. But I get where they’re coming from.

Some of the smartest people I know share a bone-deep belief that AI is a fad — the next iteration of NFT mania. I’ve been reluctant to push back on them, because, well, they’re smarter than me. But their arguments are unserious, and worth confronting. Extraordinarily talented people are doing work that LLMs already do better, out of spite.

All progress on LLMs could halt today, and LLMs would remain the 2nd most important thing to happen over the course of my career.

**Important caveat**: I’m discussing only the implications of LLMs for software development. For art, music, and writing? I got nothing. I’m inclined to believe the skeptics in those fields. I just don’t believe them about mine.

Bona fides: I’ve been shipping software since the mid-1990s. I started out in boxed, shrink-wrap C code. Survived an ill-advised [Alexandrescu](https://www.amazon.com/Modern-Design-Generic-Programming-Patterns/dp/0201704315) C++ phase. Lots of Ruby and Python tooling. Some kernel work. A whole lot of server-side C, Go, and Rust. However you define “serious developer”, I qualify. Even if only on one of your lower tiers.

### [](https://fly.io/blog/youre-all-nuts/#level-setting)level setting

† (or, God forbid, 2 years ago with Copilot)

First, we need to get on the same page. If you were trying and failing to use an LLM for code 6 months ago †, you’re not doing what most serious LLM-assisted coders are doing.

People coding with LLMs today use agents. Agents get to poke around your codebase on their own. They author files directly. They run tools. They compile code, run tests, and iterate on the results. They also:

*   pull in arbitrary code from the tree, or from other trees online, into their context windows, 
*   run standard Unix tools to navigate the tree and extract information, 
*   interact with Git, 
*   run existing tooling, like linters, formatters, and model checkers, and 
*   make essentially arbitrary tool calls (that you set up) through MCP. 

The code in an agent that actually “does stuff” with code is not, itself, AI. This should reassure you. It’s surprisingly simple systems code, wired to ground truth about programming in the same way a Makefile is. You could write an effective coding agent in a weekend. Its strengths would have more to do with how you think about and structure builds and linting and test harnesses than with how advanced o3 or Sonnet have become.

If you’re making requests on a ChatGPT page and then pasting the resulting (broken) code into your editor, you’re not doing what the AI boosters are doing. No wonder you’re talking past each other.

### [](https://fly.io/blog/youre-all-nuts/#the-positive-case)the positive case

![Image 2: four quadrants of tedium and importance](https://fly.io/blog/youre-all-nuts/assets/code-quad.png?2/3&center)

LLMs can write a large fraction of all the tedious code you’ll ever need to write. And most code on most projects is tedious. LLMs drastically reduce the number of things you’ll ever need to Google. They look things up themselves. Most importantly, they don’t get tired; they’re immune to inertia.

Think of anything you wanted to build but didn’t. You tried to home in on some first steps. If you’d been in the limerent phase of a new programming language, you’d have started writing. But you weren’t, so you put it off, for a day, a year, or your whole career.

I can feel my blood pressure rising thinking of all the bookkeeping and Googling and dependency drama of a new project. An LLM can be instructed to just figure all that shit out. Often, it will drop you precisely at that golden moment where shit almost works, and development means tweaking code and immediately seeing things work better. That dopamine hit is why I code.

There’s a downside. Sometimes, gnarly stuff needs doing. But you don’t wanna do it. So you refactor unit tests, soothing yourself with the lie that you’re doing real work. But an LLM can be told to go refactor all your unit tests. An agent can occupy itself for hours putzing with your tests in a VM and come back later with a PR. If you listen to me, you’ll know that. You’ll feel worse yak-shaving. You’ll end up doing… real work.

### [](https://fly.io/blog/youre-all-nuts/#but-you-have-no-idea-what-the-code-is)but you have no idea what the code is

Are you a vibe coding Youtuber? Can you not read code? If so: astute point. Otherwise: what the fuck is wrong with you?

You’ve always been responsible for what you merge to `main`. You were five years go. And you are tomorrow, whether or not you use an LLM.

If you build something with an LLM that people will depend on, read the code. In fact, you’ll probably do more than that. You’ll spend 5-10 minutes knocking it back into your own style. LLMs are [showing signs of adapting](https://github.com/PatrickJS/awesome-cursorrules) to local idiom, but we’re not there yet.

People complain about LLM-generated code being “probabilistic”. No it isn’t. It’s code. It’s not Yacc output. It’s knowable. The LLM might be stochastic. But the LLM doesn’t matter. What matters is whether you can make sense of the result, and whether your guardrails hold.

Reading other people’s code is part of the job. If you can’t metabolize the boring, repetitive code an LLM generates: skills issue! How are you handling the chaos human developers turn out on a deadline?

† (because it can hold 50-70kloc in its context window)

For the last month or so, Gemini 2.5 has been my go-to †. Almost nothing it spits out for me merges without edits. I’m sure there’s a skill to getting a SOTA model to one-shot a feature-plus-merge! But I don’t care. I like moving the code around and chuckling to myself while I delete all the stupid comments. I have to read the code line-by-line anyways.

### [](https://fly.io/blog/youre-all-nuts/#but-hallucination)but hallucination

If hallucination matters to you, your programming language has let you down.

Agents lint. They compile and run tests. If their LLM invents a new function signature, the agent sees the error. They feed it back to the LLM, which says “oh, right, I totally made that up” and then tries again.

You’ll only notice this happening if you watch the chain of thought log your agent generates. Don’t. This is why I like [Zed’s agent mode](https://zed.dev/agentic): it begs you to tab away and let it work, and pings you with a desktop notification when it’s done.

I’m sure there are still environments where hallucination matters. But “hallucination” is the first thing developers bring up when someone suggests using LLMs, despite it being (more or less) a solved problem.

### [](https://fly.io/blog/youre-all-nuts/#but-the-code-is-shitty-like-that-of-a-junior-developer)but the code is shitty, like that of a junior developer

Does an intern cost $20/month? Because that’s what Cursor.ai costs.

Part of being a senior developer is making less-able coders productive, be they fleshly or algebraic. Using agents well is both a both a skill and an engineering project all its own, of prompts, indices, [and (especially) tooling.](https://fly.io/blog/semgrep-but-for-real-now/) LLMs only produce shitty code if you let them.

† (Also: 100% of all the Bash code you should author ever again)

Maybe the current confusion is about who’s doing what work. Today, LLMs do a lot of typing, Googling, test cases †, and edit-compile-test-debug cycles. But even the most Claude-poisoned serious developers in the world still own curation, judgement, guidance, and direction.

Also: let’s stop kidding ourselves about how good our human first cuts really are.

### [](https://fly.io/blog/youre-all-nuts/#but-its-bad-at-rust)but it’s bad at rust

It’s hard to get a good toolchain for Brainfuck, too. Life’s tough in the aluminum siding business.

† (and they surely will; the Rust community takes tooling seriously)

A lot of LLM skepticism probably isn’t really about LLMs. It’s projection. People say “LLMs can’t code” when what they really mean is “LLMs can’t write Rust”. Fair enough! But people select languages in part based on how well LLMs work with them, so Rust people should get on that †.

I work mostly in Go. I’m confident the designers of the Go programming language didn’t set out to produce the most LLM-legible language in the industry. They succeeded nonetheless Go has just enough type safety, an extensive standard library, and a culture that prizes (often repetitive) idiom. LLMs kick ass generating it.

All this is to say: I write some Rust. I like it fine. If LLMs and Rust aren’t working for you, I feel you. But if that’s your whole thing, we’re not having the same argument.

### [](https://fly.io/blog/youre-all-nuts/#but-the-craft)but the craft

Do you like fine Japanese woodworking? All hand tools and sashimono joinery? Me too. Do it on your own time.

† (I’m a piker compared to my woodworking friends)

I have a basic wood shop in my basement †. I could get a lot of satisfaction from building a table. And, if that table is a workbench or a grill table, sure, I’ll build it. But if I need, like, a table? For people to sit at? In my office? I buy a fucking table.

Professional software developers are in the business of solving practical problems for people with code. We are not, in our day jobs, artisans. Steve Jobs was wrong: we do not need to carve the unseen feet in the sculpture. Nobody cares if the logic board traces are pleasingly routed. If anything we build endures, it won’t be because the codebase was beautiful.

Besides, that’s not really what happens. If you’re taking time carefully golfing functions down into graceful, fluent, minimal functional expressions, alarm bells should ring. You’re yak-shaving. The real work has depleted your focus. You’re not building: you’re self-soothing.

Which, wait for it, is something LLMs are good for. They devour schlep, and clear a path to the important stuff, where your judgement and values really matter.

### [](https://fly.io/blog/youre-all-nuts/#but-the-mediocrity)but the mediocrity

As a mid-late career coder, I’ve come to appreciate mediocrity. You should be so lucky as to have it flowing almost effortlessly from a tap.

We all write mediocre code. Mediocre code: often fine. Not all code is equally important. Some code should be mediocre. Maximum effort on a random unit test? You’re doing something wrong. Your team lead should correct you.

Developers all love to preen about code. They worry LLMs lower the “ceiling” for quality. Maybe. But they also raise the “floor”.

Gemini’s floor is higher than my own. My code looks nice. But it’s not as thorough. LLM code is repetitive. But mine includes dumb contortions where I got too clever trying to DRY things up.

And LLMs aren’t mediocre on every axis. They almost certainly have a bigger bag of algorithmic tricks than you do: radix tries, topological sorts, graph reductions, and LDPC codes. Humans romanticize `rsync` ([Andrew Tridgell](https://www.andrew.cmu.edu/course/15-749/READINGS/required/cas/tridgell96.pdf) wrote a paper about it!). To an LLM it might not be that much more interesting than a SQL join.

But I’m getting ahead of myself. It doesn’t matter. If truly mediocre code is all we ever get from LLM, that’s still huge. It’s that much less mediocre code humans have to write.

### [](https://fly.io/blog/youre-all-nuts/#but-itll-never-be-agi)but it’ll never be AGI

I don’t give a shit.

Smart practitioners get wound up by the AI/VC hype cycle. I can’t blame them. But it’s not an argument. Things either work or they don’t, no matter what Jensen Huang has to say about it.

### [](https://fly.io/blog/youre-all-nuts/#but-they-take-rr-jerbs)but they take-rr jerbs

[So does open source.](https://news.ycombinator.com/item?id=43776612) We used to pay good money for databases.

We’re a field premised on automating other people’s jobs away. “Productivity gains,” say the economists. You get what that means, right? Fewer people doing the same stuff. Talked to a travel agent lately? Or a floor broker? Or a record store clerk? Or a darkroom tech?

When this argument comes up, libertarian-leaning VCs start the chant: lamplighters, creative destruction, new kinds of work. Maybe. But I’m not hypnotized. I have no fucking clue whether we’re going to be better off after LLMs. Things could get a lot worse for us.

LLMs really might displace many software developers. That’s not a high horse we get to ride. Our jobs are just as much in tech’s line of fire as everybody else’s have been for the last 3 decades. We’re not [East Coast dockworkers](https://en.wikipedia.org/wiki/2024_United_States_port_strike); we won’t stop progress on our own.

### [](https://fly.io/blog/youre-all-nuts/#but-the-plagiarism)but the plagiarism

Artificial intelligence is profoundly — and probably unfairly — threatening to visual artists in ways that might be hard to appreciate if you don’t work in the arts.

We imagine artists spending their working hours pushing the limits of expression. But the median artist isn’t producing gallery pieces. They produce on brief: turning out competent illustrations and compositions for magazine covers, museum displays, motion graphics, and game assets.

LLMs easily — alarmingly — clear industry quality bars . Gallingly, one of the things they’re best at is churning out just-good-enough facsimiles of human creative work. I have family in visual arts. I can’t talk to them about LLMs. I don’t blame them. They’re probably not wrong.

Meanwhile, software developers spot code fragments [seemingly lifted](https://arxiv.org/abs/2311.17035) from public repositories on Github and lose their shit. What about the licensing? If you’re a lawyer, I defer. But if you’re a software developer playing this card? Cut me a little slack as I ask you to shove this concern up your ass. No profession has demonstrated more contempt for intellectual property.

The median dev thinks Star Wars and Daft Punk are a public commons. The great cultural project of developers has been opposing any protection that might inconvenience a monetizable media-sharing site. When they fail at policy, they route around it with coercion. They stand up global-scale piracy networks and sneer at anybody who so much as tries to preserve a new-release window for a TV show.

Call any of this out if you want to watch a TED talk about how hard it is to stream _The Expanse_ on LibreWolf. Yeah, we get it. You don’t believe in IPR. Then shut the fuck up about IPR. Reap the whirlwind.

It’s all special pleading anyways. LLMs digest code further than you do. If you don’t believe a typeface designer can stake a moral claim on the terminals and counters of a letterform, you sure as hell can’t be possessive about a red-black tree.

### [](https://fly.io/blog/youre-all-nuts/#positive-case-redux)positive case redux

When I started writing a couple days ago, I wrote a section to “level set” to the state of the art of LLM-assisted programming. A bluefish filet has a longer shelf life than an LLM take. In the time it took you to read this, everything changed.

Kids today don’t just use agents; they use asynchronous agents. They wake up, free-associate 13 different things for their LLMs to work on, make coffee, fill out a TPS report, drive to the Mars Cheese Castle, and then check their notifications. They’ve got 13 PRs to review. Three get tossed and re-prompted. Five of them get the same feedback a junior dev gets. And five get merged.

_“I’m sipping rocket fuel right now,”_ a friend tells me. _“The folks on my team who aren’t embracing AI? It’s like they’re standing still.”_ He’s not bullshitting me. He doesn’t work in SFBA. He’s got no reason to lie.

There’s plenty of things I can’t trust an LLM with. No LLM has any of access to prod here. But I’ve been first responder on an incident and fed 4o — not o4-mini, 4o — log transcripts, and watched it in seconds spot LVM metadata corruption issues on a host we’ve been complaining about for months. Am I better than an LLM agent at interrogating OpenSearch logs and Honeycomb traces? No. No, I am not.

To the consternation of many of my friends, I’m not a radical or a futurist. I’m a statist. I believe in the haphazard perseverance of complex systems, of institutions, of reversions to the mean. I write Go and Python code. I’m not a Kool-aid drinker.

But something real is happening. My smartest friends are blowing it off. Maybe I persuade you. Probably I don’t. But we need to be done making space for bad arguments.

### [](https://fly.io/blog/youre-all-nuts/#but-im-tired-of-hearing-about-it)but i’m tired of hearing about it

And here I rejoin your company. I read [Simon Willison](https://simonwillison.net/), and that’s all I really need. But all day, every day, a sizable chunk of the front page of HN is allocated to LLMs: incremental model updates, startups doing things with LLMs, LLM tutorials, screeds against LLMs. It’s annoying!

But AI is also incredibly — a word I use advisedly — important. It’s getting the same kind of attention that smart phones got in 2008, and not as much as the Internet got. That seems about right.

I think this is going to get clearer over the next year. The cool kid haughtiness about “stochastic parrots” and “vibe coding” can’t survive much more contact with reality. I’m snarking about these people, but I meant what I said: they’re smarter than me. And when they get over this affectation, they’re going to make coding agents profoundly more effective than they are today.
