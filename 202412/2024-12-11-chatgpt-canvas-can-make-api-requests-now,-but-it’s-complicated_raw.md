Title: ChatGPT Canvas can make API requests now, but it’s complicated

URL Source: https://simonwillison.net/2024/Dec/10/chatgpt-canvas/

Markdown Content:
10th December 2024

Today’s [12 Days of OpenAI](https://openai.com/12-days/?day=4) release concerned [ChatGPT Canvas](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it), a new ChatGPT feature that enables ChatGPT to pop open a side panel with a shared editor in it where you can collaborate with ChatGPT on editing a document or writing code.

I’m always excited to see a new form of UI on top of LLMs, and it’s great seeing OpenAI stretch out beyond pure chat for this. It’s definitely worth playing around with to get a feel for how a collaborative human+LLM interface can work. The feature where you can ask ChatGPT for “comments on my document” and it will attach them Google Docs style is particularly neat.

I wanted to focus in on one particular aspect of Canvas, because it illustrates a concept I’ve been talking about for a little while now: the increasing complexity of fully understanding the capabilities of core LLM tools.

#### Canvas runs Python via Pyodide

If a canvas editor contains Python code, ChatGPT adds a new “Run” button at the top of the editor.

ChatGPT has had the ability to run Python for a long time via the excellent [Code Interpreter](https://simonwillison.net/tags/code-interpreter/) feature, which executes Python server-side in a tightly locked down Kubernetes container managed by OpenAI.

The new Canvas run button is **not the same thing**—it’s an entirely new implementation of code execution that runs code directly in your browser using [Pyodide](https://pyodide.org/) (Python compiled to WebAssembly).

The first time I tried this button I got the following dialog:

![Image 5: Run Python code? Python in canvas can make network requests and interact with external systems. Please review your code carefully before proceeding.](https://static.simonwillison.net/static/2024/run-python-code.jpg)

“Python in canvas can make network requests”‽ This is a _very new_ capability. ChatGPT Code Interpreter has all network access blocked, but apparently ChatGPT Canvas Python does not share that limitation.

I tested this a little bit and it turns out it can make direct HTTP calls from your browser to anywhere online with compatible CORS headers.

(Understanding CORS is [a recurring theme](https://simonwillison.net/search/?q=cors&sort=date&tag=llms) in working with LLMs as a consumer, which I find deeply amusing because it remains a pretty obscure topic even among professional web developers.)

[Claude Artifacts](https://simonwillison.net/tags/claude-artifacts/) allow full JavaScript execution in a Canvas-like interface within Claude, but even those are severely restricted in terms of the endpoints they can access. OpenAI have apparently made the opposite decision, throwing everything wide open as far as allowed network request targets go.

I prompted ChatGPT like this:

> `use python to fetch "https://datasette.io/content.json?sql=select+*+from+stats++limit+10%0D%0A&_shape=array" and then display it nicely - the JSON looks like this:`
> 
> ```
> [
>   {
>     "package": "airtable-export",
>     "date": "2020-12-14",
>     "downloads": 2
>   },
> ```

I often find pasting the first few lines of a larger JSON example into an LLM gives it enough information to guess the rest.

Here’s the result. ChatGPT wrote the code and showed it in a canvas, then I clicked “Run” and had the resulting data displayed in a neat table below:

![Image 6: Two columns. On the left is my chat with my prompt. On the right Python code, with a table below showing the results of the API call.](https://static.simonwillison.net/static/2024/canvas-python.jpg)

What a neat and interesting thing! I can now get ChatGPT to write me Python code that fetches from external APIs and displays me the results.

It’s not yet as powerful as Claude Artifacts which allows for completely custom HTML+CSS+JavaScript interfaces, but it’s also _more_ powerful than Artifacts because those are not allowed to make outbound HTTP requests at all.

#### What this all means

With the introduction of Canvas, here are some new points that an expert user of ChatGPT now needs to understand:

*   ChatGPT can write and then execute code in Python, but there are two different ways it can do that:
    *   If run using Code Interpreter it can access files you upload to it and [a collection of built-in libraries](https://github.com/simonw/scrape-openai-code-interpreter/blob/main/packages.txt) but cannot make API requests.
    *   If run in a Canvas it uses Pyodide and can access API endpoints, but not files that you upload to it.
*   Code Interpreter cannot `pip install` additional packages, though you may be able to [upload them as wheels](https://til.simonwillison.net/llms/code-interpreter-expansions) and convince it to install them.
*   Canvas Python can install extra packages using [micropip](https://micropip.pyodide.org/en/stable/project/usage.html), but this will only work for pure Python wheels that are compatible with Pyodide.
*   Code interpreter is locked down: it cannot make API requests or communicate with the wider internet at all. If you want it to work on data you need to upload that data to it.
*   Canvas Python can fetch data via API requests (directly into your browser), but only from sources that implement an open CORS policy.
*   Both Canvas and Code Interpreter remain strictly limited in terms of the custom UI they can offer—but they both have access to the Pandas ecosystem of visualization tools so they can probably show you charts or tables.

#### This is really, really confusing

Do you find this all hopelessly confusing? I don’t blame you. I’m a professional web developer and a Python engineer of 20+ years and I can just about understand and internalize the above set of rules.

I don’t really have any suggestions for where we go from here. This stuff is _hard to use_. The more features and capabilities we pile onto these systems the harder it becomes to obtain true mastery of them and really understand what they can do and how best to put them into practice.

Maybe this doesn’t matter? I don’t know anyone with true mastery of Excel—to the point where they could compete in [last week’s Microsoft Excel World Championship](https://fmworldcup.com/microsoft-excel-world-championship/)—and yet plenty of people derive enormous value from Excel despite only scratching the surface of what it can do.

I do think it’s worth remembering this as a general theme though. Chatbots may sound easy to use, but they really aren’t—and they’re getting harder to use all the time.

#### A new data exfiltration vector

Thinking about this a little more, I think the most meaningful potential security impact from this could be opening up a new data exfiltration vector.

Data exfiltration attacks occur when an attacker tricks someone into pasting malicious instructions into their prompt (often via a [prompt injection attack](https://simonwillison.net/tags/prompt-injection/)) that cause ChatGPT to gather up any available private information from the current conversation and leak it to that attacker in some way.

I imagine it may be possible to construct a pretty gnarly attack that convinces ChatGPT to open up a Canvas and then run Python that leaks any gathered private data to the attacker via an API call.
