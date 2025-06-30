Title: Agentic Coding: The Future of Software Development with Agents

URL Source: https://simonwillison.net/2025/Jun/29/agentic-coding/

Markdown Content:
**[Agentic Coding: The Future of Software Development with Agents](https://www.youtube.com/watch?v=nfOVgz_omlU)**. Armin Ronacher delivers a 37 minute YouTube talk describing his adventures so far with Claude Code and agentic coding methods.

> A friend called Claude Code catnip for programmers and it really feels like this. I haven't felt so energized and confused and just so willing to try so many new things... it is really incredibly addicting.

I picked up a bunch of useful tips from this video:

*   Armin runs Claude Code with the `--dangerously-skip-permissions` option, and says this unlocks a huge amount of productivity. I haven't been brave enough to do this yet but I'm going to start using that option while running in a Docker container to ensure nothing too bad can happen.
*   When your agentic coding tool can run commands in a terminal you can mostly avoid MCP - instead of adding a new MCP tool, write a script or add a Makefile command and tell the agent to use that instead. The only MCP Armin uses is [the Playwright one](https://github.com/microsoft/playwright-mcp).
*   Combined logs are a really good idea: have everything log to the same place and give the agent an easy tool to read the most recent N log lines.
*   While running Claude Code, use Gemini CLI to run sub-agents, to perform additional tasks without using up Claude Code's own context
*   Designing additional tools that provide very clear errors, so the agents can recover when something goes wrong.
*   Thanks to Playwright, Armin has Claude Code perform all sorts of automated operations via a signed in browser instance as well. "Claude can debug your CI... it can sign into a browser, click around, debug..." - he also has it use the `gh` GitHub CLI tool to interact with things like [GitHub Actions workflows](https://cli.github.com/manual/gh_workflow).

![Image 1: "Tip 1: Unified Logging" at top, followed by title "Forward Everything Into One Log File" and bullet points: "Combine console.log + server logs + everything else", "patch console.log in the browser -> forward to server via API call", "All output streams flow to a single, tailable log file", "Give it a way to log out SQL too!", "Provide a make tail-logs command for easy access". Bottom shows example: "# Example" and "make tail-logs  # Shows last 50 lines, follows new output".](https://static.simonwillison.net/static/2025/armin-logging.jpg)
