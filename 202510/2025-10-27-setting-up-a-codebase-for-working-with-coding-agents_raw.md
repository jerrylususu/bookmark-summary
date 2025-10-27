Title: Setting up a codebase for working with coding agents

URL Source: https://simonwillison.net/2025/Oct/25/coding-agent-tips/

Markdown Content:
Someone on Hacker News [asked for tips](https://news.ycombinator.com/item?id=45695621#45704966) on setting up a codebase to be more productive with AI coding tools. Here's my reply:

*   Good automated tests which the coding agent can run. I love pytest for this - one of my projects has 1500 tests and Claude Code is really good at selectively executing just tests relevant to the change it is making, and then running the whole suite at the end.
*   Give them the ability to interactively test the code they are writing too. Notes on how to start a development server (for web projects) are useful, then you can have them use Playwright or curl to try things out.
*   I'm having great results from maintaining a GitHub issues collection for projects and pasting URLs to issues directly into Claude Code.
*   I actually don't think documentation is too important: LLMs can read the code a lot faster than you to figure out how to use it. I have comprehensive documentation across all of my projects but I don't think it's that helpful for the coding agents, though they are good at helping me spot if it needs updating.
*   Linters, type checkers, auto-formatters - give coding agents helpful tools to run and they'll use them.

For the most part anything that makes a codebase easier for humans to maintain turns out to help agents as well.

**Update**: Thought of another one: detailed error messages! If a manual or automated test fails the more information you can return back to the model the better, and stuffing extra data in the error message or assertion is a very inexpensive way to do that.