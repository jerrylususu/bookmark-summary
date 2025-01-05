Title: What we learned copying all the best code assistants

URL Source: https://blog.val.town/blog/fast-follow/

Markdown Content:
![Image 7: Steve Krouse](https://blog.val.town/_astro/steve.X7ylcW9k_ZMjRK9.webp) on Jan 3, 2025

Since the beginning of Val Town, our users have been clamouring for the state-of-the-art LLM code generation experience. When we launched our code hosting service in 2022, the state-of-the-art was GitHub Copilot. But soon it was ChatGPT, then Claude Artifacts, and now [Bolt](https://bolt.new/), [Cursor](https://www.cursor.com/), and [Windsurf](https://codeium.com/windsurf). We’ve been trying our best to keep up. Looking back over 2024, our efforts have mostly been a series of _fast-follows_, copying the innovation of others. Some have been successful, and others false-starts. This article is a historical account of our efforts, giving credit where it is due.

### [GitHub Copilot Completions](https://blog.val.town/blog/fast-follow/#github-copilot-completions)

The story starts, of course, with GitHub Copilot. From day 1, Val Town users asked for a GitHub-Copilot-like completions experience.

We were wary of building this ourselves, but one day we stumbled upon Asad Memon’s [codemirror-copilot](https://github.com/asadm/codemirror-copilot), and hooked it up. That gave us our first taste of LLM-driven autocomplete, but behind the scenes, it was using ChatGPT. The prompt essentially asked ChatGPT to cosplay as an autocomplete service and fill in the text at the user’s cursor. So it was fairly slow, occasionally the model would forget its role and do something unexpected, and it didn’t have the accuracy of a purpose-built autocomplete model.

We wanted a faster, more accurate autocomplete sytem, one that used a model trained for the task - which is technically called [‘Fill in the Middle’](https://arxiv.org/abs/2207.14255). Finding an option that we could use within a product like Val Town was tricky – Copilot and most of its competitors lack documented or open APIs. But [Codeium](https://codeium.com/) did, and they also had very good accuracy and performance. We [launched Codeium completions](https://blog.val.town/blog/val-town-newsletter-16/#-codeium-completions) in April 2024 and open-sourced our [codemirror-codeium](https://github.com/val-town/codemirror-codeium) component. It’s been pretty great. It’s enabled by default for new users.

![Image 8: Codeium](https://blog.val.town/_astro/codeium.DmWVlUN2_ZSR3s9.webp)

### [ChatGPT](https://blog.val.town/blog/fast-follow/#chatgpt)

Then came ChatGPT. We found our users asking it to write Val Town code, and copying and pasting it back into Val Town. We figured we could automate that process for our users: provide an interface with a pre-filled system prompt and a one-click way to save the generated code as a val. The [first version of Townie](https://blog.val.town/blog/val-town-newsletter-18/#-townie) was born: a simple chat interface, very much inspired by ChatGPT, powered by GPT-3.5.

![Image 9: Townie](https://blog.val.town/_astro/townie.B_9WgDMi_Z1eUctW.webp)

It was just ok. It didn’t get much use, mostly because it was hard to iterate on its results. Getting good results from an LLM usually requires a conversation because programming-via-English is pretty imprecise, and you need follow-up requests to clarify your needs.

### [ChatGPT Tool Use](https://blog.val.town/blog/fast-follow/#chatgpt-tool-use)

Earlier this year, ChatGPT Function Calling, now called ‘tool-use’, was seen as the next big thing. The promise was that with a good OpenAPI spec, AI would be able to do just about anything on Val Town. So we dutifully cleaned up our OpenAPI spec, and [rebuilt Townie around it](https://blog.val.town/blog/openapi/#our-ai-townie-can-now-call-our-rest-api).

It was, ahem, fine. Function calling was a disappointment. You do all the work to provide the LLM with a strict definition of what functions it can call and with which arguments. But even with all of that, the LLM would hallucinate functions that didn’t exist. Function calling has improved since, with the introduction of [Structured Outputs](https://platform.openai.com/docs/guides/function-calling#structured-outputs).

But for us, the issue was that the interface was too generic. In theory, it was capable of doing anything (editing your blobs or sqlite data), but it wasn’t very useful at any specific thing. Most notably, it wasn’t a good interface for iterating on code. It could write a first version of code, but it wasn’t optimized to let you run that code, see the output, debug it, let you ask the AI for more help. In other words, the feedback loop was bad.

### [Claude Artifacts](https://blog.val.town/blog/fast-follow/#claude-artifacts)

We had begun to see the potential of Claude for code generation with the amazing results produced by [Websim](https://websim.ai/). But it was the [launch of Claude 3.5 Sonnet and Claude Artifacts](https://www.anthropic.com/news/claude-3-5-sonnet) that really got our attention. Claude 3.5 Sonnet was dramatically better at generating code than anything we’d seen before. It blew all of our minds. And Claude Artifacts solved the tight feedback loop problem that we saw with our ChatGPT tool-use version. And thus after about a month of prototyping and building, the [current version of Townie](https://blog.val.town/blog/codegen/) was born in August 2024.

For a couple weeks there, it felt like we had one of the best tools in the space. Townie can generate a fullstack app, with a frontend, backend, and database, in minutes, and fully deployed. The space has since gotten crowded. Live by the fast follow; die by the fast follow.

### [Our Contributions](https://blog.val.town/blog/fast-follow/#our-contributions)

While we were out in front, we invested in trying to stay there, and we made some contributions of our own that have since found there way into other tools in the space.

#### [Speed](https://blog.val.town/blog/fast-follow/#speed)

The biggest problem with all current codegen systems is the speed of generation. It takes minutes to generate just a couple hundred lines of code. If you regenerate the whole file every time – which is how most systems work – that means minutes between every feedback loop. (Not to mention the cost of regenerating the whole file every time, even when you are making a small change.)

We worked hard to get the LLM producing diffs, based on [work we saw in Aider](https://aider.chat/docs/unified-diffs.html). We were able to get it working most of the time, but not reliably enough. It’s now off by default, but you can ask Townie to “reply in diff” if you’d like to try your luck with it.

Our system prompt has always been open (you can view it in your Townie settings), so you can see how we’re doing that. Here’s the relevant section:

```
Follow the requirements above and respond by generating code in a format based on whether or not the user explicitly requests diff format in their most recent prompt:- If the user does not explicitly request diff format in their prompt, generate the entire val:  Use <existing_code> as the basis for generating code if it is provided.  Write code that is complete and directly runnable.  DO NOT omit code or use comments such as "more content here" or "code remains unchanged."  Write the code in `val code fences.Include the val type as metadata on the code fence, e.g.: `val type=script  If this is a new val, decide what val type is appropriate based on the user's prompt. Default to choosing http type vals unless the user has requested specific functionality that requires a different type.- If the user requests diff format in their prompt, follow these steps:  Write a valid unified diff with change hunk headers. The file headers can be omitted.  Base the diff off of the <existing_code> tags below.  Use the ```diff language code fence.
```

We’ve gotten scared off of investing more time in diffs right now, but I expect it may have been solved by others in the space already, or will be shortly. Anthropic’s long-rumored “fast-edit mode” solve this problem in one fell swoop. OpenAI launched their own [Predicted Outputs](https://platform.openai.com/docs/guides/predicted-outputs), which is also compelling, but then we’d have to switch to OpenAI. Or maybe the solution is simply faster models, smaller, mini-models, or faster chips, like Groq or Cerebras. A couple weeks ago I built [Cerebras Coder](https://cerebrascoder.com/) to demonstrate how powerful an instant feedback loop is for code generation. [Try it out yourself](https://cerebrascoder.com/) or [fork it here](https://www.val.town/v/stevekrouse/cerebras_coder).

DeepSeek [recently open-sourced an almost-Sonnet-3.5-level model that’s twice as fast and trained for only $6m](https://x.com/deepseek_ai/status/1872242657348710721). A boy can dream of a world where Sonnet-3.5-level codegen (or even smarter!) is available on a chip like Cerebras at a fraction of Anthropic’s cost. I think that would unleash a whole new class of innovation here.

#### [Autodetecting errors](https://blog.val.town/blog/fast-follow/#autodetecting-errors)

We did contribute one possibly-novel UI interaction, where the LLM automatically detects errors and asks you if you’d like it to try to solve them. We detect server-side errors by polling our backend for 500 errors in your logs. We detect client-side errors in the iframe by prompting Townie to import [this client-side library](https://www.val.town/v/std/catch), which pushes errors up to the parent window.

It’s not _particularly_ novel (in that others would have thought of this if we didn’t), but maybe the folks at [Anthropic](https://support.anthropic.com/en/articles/9949260-try-fixing-with-claude-for-artifact-errors) or Bolt saw our implementation and it inspired their own. I’d like to think we’re not _only_ free-riding in this space.

### [Hosted runtime and included APIs](https://blog.val.town/blog/fast-follow/#hosted-runtime-and-included-apis)

Maybe some of our UI ideas made it into GitHub Spark too, including deployment-free hosting, persistent data storage, and the ability to use LLMs in your apps without a your own API key – their versions of [@std/sqlite](https://docs.val.town/std/sqlite/) and [@std/openai](https://docs.val.town/std/openai/), respectively. In other words, you can say, “make me a ChatGPT clone with persistent thread history”, and in about 30 seconds, you’ll have a deployed app that does exactly that.

But we’re not the first hosting company to provide an LLM tool; that honor likely goes to Vercel’s [v0](https://v0.dev/).

### [Cursor](https://blog.val.town/blog/fast-follow/#cursor)

The next big thing was [Cursor](https://www.cursor.com/). I must admit that I never personally fell in love with it, but given how many people I respect love it, I think that’s a me-problem. I think Cursor is best for development in larger codebases, but recently my work has been on making vals in Val Town which are usually under 1,000 lines of code. (Our upcoming launch of multi-file Projects, now in private beta, will change this.) However Cursor is a real pioneer in the space, and has some UI interactions there that we have an eye to copy.

### [Windsurf](https://blog.val.town/blog/fast-follow/#windsurf)

Over the holiday, I fell in love with [Windsurf](https://codeium.com/windsurf) by the folks at Codeium. Its Cascade feature is a chat interface, which has tool use and multi-turn agentic capabilities, to search through your codebase and edit multiple files. It feels a bit like we’re coming full-circle back to when we did our tool-use version of Townie. However, I think we now all understand that you can’t simply give your OpenAPI spec to an LLM and expect good results. The magic of Windsurf is that they carefully crafted what actions their agent can take, and that it can take multiple actions in a row without your input.

I am salivating at the idea of giving Townie some of these capabilities. Imagine if Townie could search through all public vals, and maybe even npm, or the public internet, to find code, docs, and other resources to help you.

### [Devin](https://blog.val.town/blog/fast-follow/#devin)

Watching Windsurf take multiple actions on my behalf without my input is very inspirational. I’m dreaming of a world where Townie not only detects errors, but also automatically tries to fix them, possibly multiple times, possibly in parallel across different branches, without any human interaction. Here, of course, we’d be getting into territory mostly explored by the folks at [Devin](https://devin.ai/).

For starters, we could feed back screenshots of the generated website back to the LLM. But soon you’d want to give the LLM access to a full web browser so it can itself poke around the app, like a human would, to see what features work and which ones don’t. Maybe then it’d even write some tests, also like a human would, to make sure things don’t break as it continues to iterate.

I have a vague sense by the end of this year that you’ll be able to tell Townie to “make a fully realistic Hacker News Clone, with user accounts, nested comments, upvotes, downvotes” and it could iterate for potentially hours on your behalf. You could even go to bed and wake up with it done.

### [Collaboration and competition](https://blog.val.town/blog/fast-follow/#collaboration-and-competition)

Is this fast-following competitive or is it collaborative? So far it’s been feeling mostly collaborative. The pie is so freaking large — there are millions and maybe billions who are jumping at the chance to code — that we’re all happy to help each other scramble to keep up with the demand. I love that, and hope it remains this way. We at Val Town certainly don’t keep (m)any secrets. Our system prompt is open, and we blog about all our interesting technical choices. This very post is a case in point.

### [Should we bow out?](https://blog.val.town/blog/fast-follow/#should-we-bow-out)

All this copying, and how fast everything is moving begs the question: Should we get out of this race entirely? How can we hope to compete against better funded competitors? Should we instead focus on improving our core differentiator, and do a better job integrating with AI editors like VSCode, Cursor, Windsurf, and Bolt? Maybe! We’re planning to dip our toes into integrating: we plan to improve our local development experience, which would allow editors like VSCode, Cursor, and Windsurf to directly edit files in Val Town. We also plan to improve our API, so tools like Bolt could “deploy to Val Town”, like they currently deploy to Netlify.

However, it still feels like there’s a lot to be gained with a fully-integrated web AI code editor experience in Val Town – even if we can only get 80% of the features that the big dogs have, and a couple months later. It doesn’t take _that_ much work to copy the best features we see in other tools. The benefits to a fully integrated experience seems well worth that cost. In short, we’ve had a lot of success fast-following so far, and think it’s worth continuing to do so.

### [Townie](https://blog.val.town/blog/fast-follow/#townie)

If you’ve made it this far in the article, you should really [try out Townie](https://www.val.town/townie). It’s still is one of the best tools to create fullstack web apps. Make yourself a [‘what did I work on today’ app that pulls from Linear and GitHub](https://www.val.town/v/danphilibin/what_did_i_work_on_today) or [a tool to extract dominant colors from an image](https://x.com/destroytoday/status/1856709997737984089) or [an AI clone for your personality](https://deeperfates.com/). Your imagination is the limit. And if you do, please let me know ([steve@val.town](mailto:steve@val.town)) what features from other tools you’d like to see in Townie. We’re eager to learn from you.

_Thanks [Tom MacWright](https://macwright.com/), [JP Posma](https://janpaulposma.nl/), and [Simon Willison](https://simonwillison.net/) for feedback on drafts of this article._

[Edit this page](https://github.com/val-town/val-town-blog/edit/main/src/content/blog/fast-follow.mdx)
