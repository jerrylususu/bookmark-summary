Title: Anthropic’s Prompt Engineering Interactive Tutorial

URL Source: https://simonwillison.net/2024/Aug/30/anthropic-prompt-engineering-interactive-tutorial/

Markdown Content:
**[Anthropic's Prompt Engineering Interactive Tutorial](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial)** ([via](https://news.ycombinator.com/item?id=41395921 "Hacker News")) Anthropic continue their trend of offering the best documentation of any of the leading LLM vendors. This tutorial is delivered as a set of Jupyter notebooks - I used it as an excuse to try [uvx](https://docs.astral.sh/uv/guides/tools/) like this:

git clone https://github.com/anthropics/courses
uvx --from jupyter-core jupyter notebook courses

This installed a working Jupyter system, started the server and launched my browser within a few seconds.

The first few chapters are pretty basic, demonstrating simple prompts run through the Anthropic API. I used `%pip install anthropic` instead of `!pip install anthropic` to make sure the package was installed in the correct virtual environment, [then filed an issue and a PR](https://github.com/anthropics/courses/issues/30).

One new-to-me trick: in the first chapter the tutorial suggests running this:

API\_KEY \= "your\_api\_key\_here"
%store API\_KEY

This stashes your Anthropic API key in the [IPython store](https://ipython.readthedocs.io/en/stable/config/extensions/storemagic.html). In subsequent notebooks you can restore the `API_KEY` variable like this:

%store \-r API\_KEY

I poked around and on macOS those variables are stored in files of the same name in `~/.ipython/profile_default/db/autorestore`.

[Chapter 4: Separating Data and Instructions](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/Anthropic%201P/04_Separating_Data_and_Instructions.ipynb) included some interesting notes on Claude's support for content wrapped in XML-tag-style delimiters:

> **Note:** While Claude can recognize and work with a wide range of separators and delimeters, we recommend that you **use specifically XML tags as separators** for Claude, as Claude was trained specifically to recognize XML tags as a prompt organizing mechanism. Outside of function calling, **there are no special sauce XML tags that Claude has been trained on that you should use to maximally boost your performance**. We have purposefully made Claude very malleable and customizable this way.

Plus this note on the importance of avoiding typos, with a nod back to the [problem of sandbagging](https://simonwillison.net/2023/Apr/5/sycophancy-sandbagging/) where models match their intelligence and tone to that of their prompts:

> This is an important lesson about prompting: **small details matter**! It's always worth it to **scrub your prompts for typos and grammatical errors**. Claude is sensitive to patterns (in its early years, before finetuning, it was a raw text-prediction tool), and it's more likely to make mistakes when you make mistakes, smarter when you sound smart, sillier when you sound silly, and so on.

[Chapter 5: Formatting Output and Speaking for Claude](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/Anthropic%201P/05_Formatting_Output_and_Speaking_for_Claude.ipynb) includes notes on one of Claude's most interesting features: _prefill_, where you can tell it how to start its response:

client.messages.create(
    model\="claude-3-haiku-20240307",
    max\_tokens\=100,
    messages\=\[
        {"role": "user", "content": "JSON facts about cats"},
        {"role": "assistant", "content": "{"}
    \]
)

Things start to get really interesting in [Chapter 6: Precognition (Thinking Step by Step)](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/Anthropic%201P/06_Precognition_Thinking_Step_by_Step.ipynb), which suggests using XML tags to help the model consider different arguments prior to generating a final answer:

> `Is this review sentiment positive or negative? First, write the best arguments for each side in <positive-argument> and <negative-argument> XML tags, then answer.`

The tags make it easy to strip out the "thinking out loud" portions of the response.

It also warns about Claude's sensitivity to ordering. If you give Claude two options (e.g. for sentiment analysis):

> In most situations (but not all, confusingly enough), **Claude is more likely to choose the second of two options**, possibly because in its training data from the web, second options were more likely to be correct.

This effect can be reduced using the thinking out loud / brainstorming prompting techniques.

A related tip is proposed in [Chapter 8: Avoiding Hallucinations](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/Anthropic%201P/08_Avoiding_Hallucinations.ipynb):

> How do we fix this? Well, a great way to reduce hallucinations on long documents is to **make Claude gather evidence first.**
> 
> In this case, we **tell Claude to first extract relevant quotes, then base its answer on those quotes**. Telling Claude to do so here makes it correctly notice that the quote does not answer the question.

I really like the example prompt they provide here, for answering complex questions against a long document:

> `<question>What was Matterport's subscriber base on the precise date of May 31, 2020?</question>`
> 
> `Please read the below document. Then, in <scratchpad> tags, pull the most relevant quote from the document and consider whether it answers the user's question or whether it lacks sufficient detail. Then write a brief numerical answer in <answer> tags.`
