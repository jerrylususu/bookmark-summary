Title: microsoft/vscode-copilot-chat

URL Source: https://simonwillison.net/2025/Jun/30/vscode-copilot-chat/

Published Time: Tue, 01 Jul 2025 13:13:27 GMT

Markdown Content:
**[microsoft/vscode-copilot-chat](https://github.com/microsoft/vscode-copilot-chat)** ([via](https://twitter.com/ashtom/status/1939724483448717369 "@ashtom")) As [promised](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot) at Build 2025 in May, Microsoft have released the GitHub Copilot Chat client for VS Code under an open source (MIT) license.

So far this is just the extension that provides the chat component of Copilot, but [the launch announcement](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone) promises that Copilot autocomplete will be coming in the near future:

> Next, we will carefully refactor the relevant components of the extension into VS Code core. The [original GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) that provides inline completions remains closed source -- but in the following months we plan to have that functionality be provided by the open sourced [GitHub Copilot Chat extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat).

I've started spelunking around looking for the all-important prompts. So far the most interesting I've found are in [prompts/node/agent/agentInstructions.tsx](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx), with a `<Tag name='instructions'>` block that [starts like this](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx#L39):

> `You are a highly sophisticated automated coding agent with expert-level knowledge across many different programming languages and frameworks. The user will ask a question, or ask you to perform a task, and it may require lots of research to answer correctly. There is a selection of tools that let you perform actions or retrieve helpful context to answer the user's question.`

There are [tool use instructions](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx#L54) - some edited highlights from those:

> *   `When using the ReadFile tool, prefer reading a large section over calling the ReadFile tool many times in sequence. You can also think of all the pieces you may be interested in and read them in parallel. Read large enough context to ensure you get what you need.`
> *   `You can use the FindTextInFiles to get an overview of a file by searching for a string within that one file, instead of using ReadFile many times.`
> *   `Don't call the RunInTerminal tool multiple times in parallel. Instead, run one command and wait for the output before running the next command.`
> *   `After you have performed the user's task, if the user corrected something you did, expressed a coding preference, or communicated a fact that you need to remember, use the UpdateUserPreferences tool to save their preferences.`
> *   `NEVER try to edit a file by running terminal commands unless the user specifically asks for it.`
> *   `Use the ReplaceString tool to replace a string in a file, but only if you are sure that the string is unique enough to not cause any issues. You can use this tool multiple times per file.`

That file also has separate [CodesearchModeInstructions](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx#L127), as well as a [SweBenchAgentPrompt](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx#L160) class with a comment saying that it is "used for some evals with swebench".

Elsewhere in the code, [prompt/node/summarizer.ts](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompt/node/summarizer.ts) illustrates one of their approaches to [Context Summarization](https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/), with a prompt that looks like this:

> `You are an expert at summarizing chat conversations.`
> 
> 
> `You will be provided:`
> 
> 
> `- A series of user/assistant message pairs in chronological order`
> 
> `- A final user message indicating the user's intent.`
> 
> 
> `[...]`
> 
> 
> `Structure your summary using the following format:`
> 
> 
> `TITLE: A brief title for the summary`
> 
> `USER INTENT: The user's goal or intent for the conversation`
> 
> `TASK DESCRIPTION: Main technical goals and user requirements`
> 
> `EXISTING: What has already been accomplished. Include file paths and other direct references.`
> 
> `PENDING: What still needs to be done. Include file paths and other direct references.`
> 
> `CODE STATE: A list of all files discussed or modified. Provide code snippets or diffs that illustrate important context.`
> 
> `RELEVANT CODE/DOCUMENTATION SNIPPETS: Key code or documentation snippets from referenced files or discussions.`
> 
> `OTHER NOTES: Any additional context or information that may be relevant.`

[prompts/node/panel/terminalQuickFix.tsx](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/panel/terminalQuickFix.tsx) looks interesting too, with prompts to help users fix problems they are having in the terminal:

> `You are a programmer who specializes in using the command line. Your task is to help the user fix a command that was run in the terminal by providing a list of fixed command suggestions. Carefully consider the command line, output and current working directory in your response. [...]`

That file also has [a PythonModuleError prompt](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/panel/terminalQuickFix.tsx#L201):

> `Follow these guidelines for python:`
> 
> `- NEVER recommend using "pip install" directly, always recommend "python -m pip install"`
> 
> `- The following are pypi modules: ruff, pylint, black, autopep8, etc`
> 
> `- If the error is module not found, recommend installing the module using "python -m pip install" command.`
> 
> `- If activate is not available create an environment using "python -m venv .venv".`

There's so much more to explore in here. [xtab/common/promptCrafting.ts](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/xtab/common/promptCrafting.ts#L34) looks like it may be part of the code that's intended to replace Copilot autocomplete, for example.

The way it handles evals is really interesting too. The code for that lives [in the test/](https://github.com/microsoft/vscode-copilot-chat/tree/v0.29.2025063001/test) directory. There's a _lot_ of it, so I engaged Gemini 2.5 Pro to help figure out how it worked:

```
git clone https://github.com/microsoft/vscode-copilot-chat
cd vscode-copilot-chat/chat
files-to-prompt -e ts -c . | llm -m gemini-2.5-pro -s \
  'Output detailed markdown architectural documentation explaining how this test suite works, with a focus on how it tests LLM prompts'
```

Here's [the resulting generated documentation](https://github.com/simonw/public-notes/blob/main/vs-code-copilot-evals.md), which even includes a Mermaid chart (I had to save the Markdown in a regular GitHub repository to get that to render - Gists still don't handle Mermaid.)

The neatest trick is the way it uses [a SQLite-based caching mechanism](https://github.com/simonw/public-notes/blob/main/vs-code-copilot-evals.md#the-golden-standard-cached-responses) to cache the results of prompts from the LLM, which allows the test suite to be run deterministically even though LLMs themselves are famously non-deterministic.
