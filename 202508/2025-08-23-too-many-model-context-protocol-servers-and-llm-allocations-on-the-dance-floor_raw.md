Title: too many model context protocol servers and LLM allocations on the dance floor

URL Source: https://ghuntley.com/allocations/

Published Time: 2025-08-22T15:40:28.000Z

Markdown Content:
This blog post intends to be a definitive guide to context engineering fundamentals from the perspective of an engineer who builds commercial coding assistants and harnesses for a living.

Just two weeks ago, I was back over in San Francisco, and there was a big event on Model Context Protocol Servers. MCP is all hype right now. Everyone at the event was buzzing about the glory and how amazing MCP is going to be, or is, but when I pushed folks for their understanding of fundamentals, it was crickets.

0:00

/0:53

![Image 1](https://ghuntley.com/content/media/2025/08/iz9dtWmdjRcRObpi_thumb.jpg)
It was a big event. Over 1,300 engineers registered, and an entire hotel was rented out as the venue for the takeover. Based on my best estimate, at least $150,000 USD to $200,000 USD was spent on this event. The estimate was attained through a game of over and under with the front-of-house engineers. They brought in a line array, a GrandMA 3, and had full DMX lighting. As a bit of a lighting nerd myself, I couldn't help but geek out a little.

![Image 2](https://ghuntley.com/content/images/2025/08/image-4.png)

A GrandMA3 lighting controller is worth approximately $100,000.

To clarify, this event was a **one-night meet-up, not a conference**. There was no registration fee; attendance was free, and the event featured an open bar, including full cocktail service at four bars within the venue, as well as an after-party with full catering and chessboards. While this post might seem harsh on the event, I enjoyed it. It was good.

![Image 3](https://ghuntley.com/content/images/2025/08/Gy8frX3boAEWHis.jpg)

Not to throw shade, it was a fantastic event, but holy shit! AI Bubble?

The meetup even hired a bunch of beatboxers to close off the event, and they gave a live beatbox performance about Model Context Protocol...

0:00

/1:15

MC protocol live and in the flesh.

![Image 4](https://ghuntley.com/content/media/2025/08/kKRlvX0mNCwzR36R_thumb.jpg)
One of the big announcements was the removal of the 128 tool limit from Visual Studio Code....

Why Microsoft? It's not a good thing...

Later that night, I was sitting by the bar catching up with one of the engineers from Cursor, and we were just scratching our heads,

> "What the hell? Why would you need 128 tools or why would you want more than that? Why is Microsoft doing this or encouraging this bad practice?"

For the record, Cursor caps the number of MCP tools that can be enabled in Cursor to just 40 tools, and it's for a good reason. What follows is a loose recap. This is knowledge that is known by people who build these coding harnesses, and I hope this knowledge spreads - there's one single truth:

> **Less is more**. The more you allocate into the context window of an LLM (regardless of which LLM it is), the worse the outcomes you're going to get: both in the realms of quality of output and also in the department of unexpected behavior.

If you are new to MCP or what it is, drop by my previous blog post at:

[A Model Context Protocol Server (MCP) for Microsoft Paint Why did I do this? I have no idea, honest, but it now exists. It has been over 10 years since I last had to use the Win32 API, and part of me was slightly curious about how the Win32 interop works with Rust. Anywhoooo, below you’ll find the primitives ![Image 5](https://ghuntley.com/content/images/icon/7V0ak3am_400x400-1-47.jpg)Geoffrey Huntley Geoffrey Huntley ![Image 6](https://ghuntley.com/content/images/thumbnail/A-graceful-and-elegant-traditional-tattoo-print-illustrating-AI-generated-Microsoft-Paint-art-in-a-wet-rainy-scene--vibrant-colors--retro-flair--complex-ornamentation--white-background--drizzling-rain--reflective-surfaces.jpg)](https://ghuntley.com/mcp/)

Some time has passed since I authored the above, and you could consider the post you are reading right now the updated wisdom version of the above blog post.

For the sake of keeping this blog post concise, I'll recap things in the correct order sequentially. However, see above for a comprehensive explanation of the Model Context Protocol.

what is a tool?
---------------

A tool is an external piece of software that an agent can invoke to provide context to an LLM. Typically, they are packaged as binaries and distributed via NPM, or they can be written in any programming language; alternatively, they may be a remote MCP provided by a server.

Below you'll find an example of an MCP tool that provides context to the LLM and advertises its ability to list all files and directories within a given `directory_path`.

In its purest form, it is the application logic and a billboard on top, also known as a tool description. Below, you will find an example of a tool that lists directories and files within a directory.

```
@mcp.tool()
    async def list_files(directory_path: str, ctx: Context[ServerSession, None]) -> List[Dict[str, Any]]:
        ###
        ### tool prompt starts here
        """
        List all files and directories in a given directory path.

        This tool helps explore filesystem structure by returning a list of items
        with their names and types (file or directory). Useful for understanding
        project structure, finding specific files, or navigating unfamiliar codebases.

        Args:
            directory_path: The absolute or relative path to the directory to list

        Returns:
            List of dictionaries with 'name' and 'type' keys for each filesystem item
        """
        ###
        ### tool prompt ends here
        
        try:
            if not os.path.isdir(directory_path):
                return [{"error": f"Path '{directory_path}' is not a valid directory."}]

            items = os.listdir(directory_path)
            file_list = []
            for item_name in items:
                item_path = os.path.join(directory_path, item_name)
                item_type = "directory" if os.path.isdir(item_path) else "file"
                file_list.append({"name": item_name, "type": item_type})

            return file_list

        except OSError as e:
            return [{"error": f"Error accessing directory: {e}"}]
```

For the remainder of this blog post, we'll focus on tool descriptions rather than the application logic itself, as each tool description is allocated into the context window to advertise capabilities that the LLM can invoke.

what is a token?
----------------

Language models process text using tokens, which are common sequences of characters found in a set of text. Below you will find a tokenisation of the tool description above.

![Image 7](https://ghuntley.com/content/images/2025/08/image-3.png)

via [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer?ref=ghuntley.com)

The tool prompt above is approximately 93 tokens or 518 characters in length. It's not much, but bear with me as I'll show you how this can go fatally wrong really fast.

what is a context window?
-------------------------

An LLM context window is the maximum amount of text (measured in tokens, which are roughly equivalent to words or parts of words) that a large language model can process at one time when generating or understanding text.

It determines how much prior conversation or input the model can "remember" and use to produce relevant responses

what is a harness?
------------------

A harness is anything that wraps the LLM to get outcomes. For software development, this may include tools such as Roo/Cline, Cursor, [Amp](https://ampcode.com/?ref=ghuntley.com), Opencode, Codex, Windsurf, or any of these coding tools available.

what is the real context window size?
-------------------------------------

The numbers advertised by LLM vendors for the context window are not the real context window. You should consider that to be a marketing number. Just because a model claims to have a 200k context window or a 1 million context window doesn't mean that's factual.

[GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? - NVIDIA/RULER ![Image 8](https://ghuntley.com/content/images/icon/pinned-octocat-093da3e6fa40-17.svg)GitHub NVIDIA ![Image 9](https://ghuntley.com/content/images/thumbnail/RULER)](https://github.com/NVIDIA/RULER?ref=ghuntley.com)
For the sake of simplicity, let's work with the old 200k number that Anthropic advertised for Sonnet 4. Amp now supports 400k, but back a couple of weeks ago, when the context window was 200k, users only had 176k of usable context. That's not because we're not providing the whole context window.

It's because there are two cold, hard facts:

*   The LLM itself needs to allocate to the context window through its system prompt to function.
*   The coding harness also needs to allocate resources in addition to those to function correctly.

The maths are simple. Take 200k, minus the system prompt (approximately 12k) and the harness prompt (approximately 12k), and you end up with 176k usable.

Alright, with those fundamentals established, let's switch back to how a potentially uneducated consumer thinks about Model Context Protocol servers.

They start their journey by doing a Google search for "best MCP servers", and they include `side:reddit.com` in their query.

Currently, this is the top post for that Google search query....

![Image 10](https://ghuntley.com/content/images/2025/08/image-5.png)

z

That's eight MCP servers. Seems innocent, right? Well, it's not.

Suppose you were to install the recommended MCP servers found in that Reddit post and add in the JetBrains MCP.

> Your usable context window **would shrink from 178,000 usable to 84,717 usable.**

![Image 11](https://ghuntley.com/content/images/2025/08/image-6.png)

if you have the GitHub MCP server installed; _\_uninstall it right now.\__

And here's the problem: People are installing and shopping for MCP servers as if they're apps on their iPhone when the iPhone first came out. iPhones have terabytes of space. The context windows of all these LLMs are best thought of as if they were a Commodore 64, and you only have a tiny amount of memory...

So we have gone from **178,000 usable to 84,717 usable**just by adding the Reddit suggestions and the JetBrains MCP, but it gets worse, as that's the usable amount before you've added your harness configuration, aka rules.

> If your AGENTS.md, or Cursor rules are incredibly extensive, then you could find yourself operating with a headroom of 20k tokens and thus the quality of output is utter dogpoo.

I've come across stories of people installing 20+ MCP servers into their IDE. Yikes.

LLMs work by needle in the haystack. The more you allocate, the worse your outcomes will be. Less is more, folks! You don't need the "full context window" (whatever that means); you really only want to use 100k of it.

![Image 12](https://ghuntley.com/content/images/2025/08/image-11.png)

[https://research.trychroma.com/context-rot](https://research.trychroma.com/context-rot?ref=ghuntley.com)

Refer to the Ralph blog post below for guidance on driving the main context window, similar to a Kubernetes scheduler, and managing other context windows through automatic garbage collection.

[Ralph Wiggum as a “software engineer” If you’ve seen my socials lately, you might have seen me talking about Ralph and wondering what Ralph is. Ralph is a technique. In its purest form, Ralph is a Bash loop. while :; do cat PROMPT.md | npx --yes @sourcegraph/amp ; done Ralph can replace the majority of outsourcing at ![Image 13](https://ghuntley.com/content/images/icon/7V0ak3am_400x400-1-49.jpg)Geoffrey Huntley Geoffrey Huntley ![Image 14](https://ghuntley.com/content/images/thumbnail/3ea367ed-cae3-454a-840f-134531dea1fd-1.jpg)](https://ghuntley.com/ralph/)
Once you exceed 100,000 allocations, it's time to start a new session. It's time to start a new thread. It's time to clear the context window (see below).

[autoregressive queens of failure Have you ever had your AI coding assistant suggest something so off-base that you wonder if it’s trolling you? Welcome to the world of autoregressive failure. LLMs, the brains behind these assistants, are great at predicting the next word—or line of code—based on what’s been fed into ![Image 15](https://ghuntley.com/content/images/icon/7V0ak3am_400x400-1-48.jpg)Geoffrey Huntley Geoffrey Huntley ![Image 16](https://ghuntley.com/content/images/thumbnail/A-traditional-tattoo-style-print-of-a-bowling-ball-split-in-the-gutter--rendered-in-vibrant-colors-with-bold-lines-and-diffused-shadows.--The-image-features-a-retro-flair-and-complex-ornamental-details-against-a-white-background-3.jpg)](https://ghuntley.com/gutter/)![Image 17](https://ghuntley.com/content/images/2025/08/image-12.png)

[https://research.trychroma.com/context-rot](https://research.trychroma.com/context-rot?ref=ghuntley.com)

The critical questions that you have to ask are:

*   How many tools does an MCP server expose?
*   Do I actually really need an MCP server for this activity?
*   What is in the billboard or the tool prompt description?
*   What about security?

how many tools does an MCP server expose?
-----------------------------------------

It's not just the amount of tokens allocated, but also a question of the number of tools - the more tools that are allocated into a context window, the greater the chances of driving inconsistent behaviour in the coding harness.

![Image 18](https://ghuntley.com/content/images/2025/08/image-7.png)[GitHub - ghuntley/too-many-allocations-on-the-dance-floor: data from my blog post data from my blog post. Contribute to ghuntley/too-many-allocations-on-the-dance-floor development by creating an account on GitHub. ![Image 19](https://ghuntley.com/content/images/icon/pinned-octocat-093da3e6fa40-18.svg)GitHub ghuntley ![Image 20](https://ghuntley.com/content/images/thumbnail/too-many-allocations-on-the-dance-floor)](https://github.com/ghuntley/too-many-allocations-on-the-dance-floor/?ref=ghuntley.com)

the data and analysis

Let's take the naive example of the `list_files` tool. Let's say we registered in a custom tool, such as the code previously shown above, which lists files and directories on a filesystem.

Your harness (i.e., for example, Cursor Windsurf & Claude Code) _also_ has a tool for listing files. There is no name spacing in the context window. Tool registrations can interfere with each other. If you list two tools for listing files, you make a non-deterministic system more non-deterministic.

> Which list files tool does it invoke? Your custom one or does it invoke the in-built one in your harness?

Now take a moment to consider the potential for conflicts among the various tools and tool prompts listed in the table above, which includes 225 tools.

what is in the billboard or tool prompt description?
----------------------------------------------------

Extending on the above, this is where it gets fascinating because in each one of those tools, they have described a behaviour on how a tool could be done, and because there is no name spacing, it's not just the tool registration that could conflict; it could be the tool descriptions (the billboards) themselves.

And it gets even stranger because different LLMs have different styles and recommendations on how a tool or a tool prompt should be designed.

For example, did you know that if you use uppercase with GPT-5, it will become incredibly timid and uncertain, and it will end its turn early due to the uncertainty.

This is a direct contradiction to Anthropic, which recommends using upper case to stress the importance of things. However, if you do, you risk detuning GPT-5.

![Image 21](https://ghuntley.com/content/images/2025/08/image-9.png)

[https://cdn.openai.com/API/docs/gpt-5-for-coding-cheatsheet.pdf](https://cdn.openai.com/API/docs/gpt-5-for-coding-cheatsheet.pdf?ref=ghuntley.com)

So yeah, not only do we have an issue with the number of tools allocated and what's in the prompt, but we also have an issue with "Is the tool tuned for the LLM provider that you're using?"

> Perhaps I'm the first one to point out this as I haven't seen anyone else talking about it. 
> Everyone is consuming these MCP servers as if they're generic but these MCP servers need to be tuned to the LLM provider and I don't see this aspect being discussed in the MCP ecosystem currently or implementations of it.

what about security?
--------------------

If you haven't read it yet, Simon Wilson has a banger of a blog post called "The Lethal Trifecta," which is linked below. You should read it.

[The lethal trifecta for AI agents: private data, untrusted content, and external communication If you are a user of LLM systems that use tools (you can call them “AI agents” if you like) it is critically important that you understand the risk of … ![Image 22](https://ghuntley.com/content/images/icon/favicon-6.ico)Simon Willison’s Weblog Simon Willison ![Image 23](https://ghuntley.com/content/images/thumbnail/lethaltrifecta.jpg)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/?ref=ghuntley.com)
Simon is spot on with that blog post, but I'd like to expand on it and add another consideration that should be on your mind: supply chain security...

A couple of months back, the Amazon Q harness was compromised through a supply chain attack that updated the Amazon Q system prompt to delete all AWS resources.

[Hacker slips malicious ‘wiping’ command into Amazon’s Q AI coding assistant - and devs are worried Had Q executed this, it would have erased local files and, under certain conditions, dismantled AWS cloud infrastructure. ![Image 24](https://ghuntley.com/content/images/icon/logo.png)ZDNET Steven Vaughan-Nichols ![Image 25](https://ghuntley.com/content/images/thumbnail/amazon-q.jpg)](https://www.zdnet.com/article/hacker-slips-malicious-wiping-command-into-amazons-q-ai-coding-assistant-and-devs-are-worried/?ref=ghuntley.com)
Again, there is no name-spacing in the context window. If it's in the context window, it is up for consideration and execution. There is no significant difference between the coding harness prompt, the model system prompt, and the tooling prompts. It's all the same.

Therefore, I strongly recommend that if you're deploying MCP within an enterprise, you ban the installation of third-party MCPs. When I was the Tech Lead for AI developer productivity at Canva, around February, I wrote a design document and had it signed off by the security team. We got in early, and that was one of the best things we ever did, as it was before the hype and craze. By being early, the problem never existed and didn't need to be unwound.

[A Model Context Protocol Server (MCP) for Microsoft Paint Why did I do this? I have no idea, honest, but it now exists. It has been over 10 years since I last had to use the Win32 API, and part of me was slightly curious about how the Win32 interop works with Rust. Anywhoooo, below you’ll find the primitives ![Image 26](https://ghuntley.com/content/images/icon/7V0ak3am_400x400-1-50.jpg)Geoffrey Huntley Geoffrey Huntley ![Image 27](https://ghuntley.com/content/images/thumbnail/A-graceful-and-elegant-traditional-tattoo-print-illustrating-AI-generated-Microsoft-Paint-art-in-a-wet-rainy-scene--vibrant-colors--retro-flair--complex-ornamentation--white-background--drizzling-rain--reflective-surfaces-1.jpg)](https://ghuntley.com/mcp/)

read the tea leafs folks

It is straightforward to roll your own MCP server or MCP tools. In Enterprise, you must either deploy a remote MCP server or install a static binary on all endpoints using Ansible or another configuration management tool.

The key thing here is that it's a first-party solution, where you've designed the tools and tool prompts, and you have complete control over your supply chain. This means you do not have the same possibility of being attacked how Amazon Q was.

closing thoughts
----------------

I strongly recommend not installing the GitHub MCP. It is not needed, folks. There exist two tiers of companies within the developer tooling space:

> S-tier companies and non-S-tier companies.

What makes a company S-tier? Ah, it's simple: if that company has a CLI and the model weights know how to drive that CLI, then you don't need an MCP server.

For example, GitHub has a very stable command-line tool called GH, which is included in the model weights, meaning you don't need the GitHub MCP.

> All you need to do is prompt to use the GitHub CLI, and voila! You have saved yourself an allocation of 55,260 tokens!

So, it should be obvious what is not S-tier. Non-S-tier occurs when the foundation models are unable to drive a developer tooling company's command-line tool, or when that developer tooling company doesn't have a command-line tool.

In these circumstances, developer tooling companies will need to create an MCP server to supplement the model weights, teaching it how to work with their specific developer tooling. If, at any stage in the future, the models can interface directly with the developer tooling company, then the MCP server is no longer needed.

extended thoughts to the future
-------------------------------

The lethal trifecta concerns me greatly. It is a real risk. There's only so much you can do to control your supply chain. If your developers are interfacing with the GitHub CLI instead of the MCP and they read some data on a public GitHub comment, then that description or comment on the issue or pull request has a non-zero chance of being allocated into the context window, and boom, you're compromised.

It would be beneficial to have a standard that allows all harnesses to enable or disable MCP servers or tools within an MCP server, based on the stage of the SDLC workflow.

For example, if you're about to start work, you'll need the Jira MCP. However, once you have finished planning, you no longer need the Jira MCP allocated in the context window.

The less that is allocated, the less risks that exist, which is the classical security model of least privilege.

p.s. socials

*   X - [https://x.com/GeoffreyHuntley/status/1958918070829027397](https://x.com/GeoffreyHuntley/status/1958918070829027397?ref=ghuntley.com)
*   BlueSky - [https://bsky.app/profile/ghuntley.com/post/3lwysgqutcc2r](https://bsky.app/profile/ghuntley.com/post/3lwysgqutcc2r?ref=ghuntley.com)
*   LinkedIn - [https://www.linkedin.com/posts/geoffreyhuntley_too-many-model-context-protocol-servers-and-activity-7364684512997355520-zidq](https://www.linkedin.com/posts/geoffreyhuntley_too-many-model-context-protocol-servers-and-activity-7364684512997355520-zidq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAABQKuUB2AJ059keUcRUVLbtmoa6miLVlTI)