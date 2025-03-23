Title: Building SaaS Products with AI: What Actually Works

URL Source: https://nmn.gl/blog/building-with-ai

Published Time: 2025-03-22T00:00:00+00:00

Markdown Content:
As a software engineer experimenting with AI for the past 2 years, I’ve tested nearly every AI coding assistant on the market and developed a workflow that consistently delivers results.

Here’s my tried-and-tested method for solo developers looking to leverage AI to make SaaS products.

_Disclaimer: While my approach requires minimal manual coding, you’ll still need a basic understanding of concepts to be able to deliver quality results. Always work with a learning mindset, and don’t do things without understanding what’s going on._

A Beautiful UI
--------------

I begin with [Lovable](https://lovable.dev/) to generate a beautiful user interface. This AI builder excels at creating clean, professional UIs and comes with a well-structured tech stack.

First, focus solely on building static screens — no databases or authentication yet.

Starting with a tool like Lovable rather than coding from scratch offers two significant advantages:

*   You can test and refine the UI before adding complexity
*   The dependencies and stack configuration are professionally handled, eliminating the version conflicts

Once satisfied with your interface, connect the project to GitHub and clone the repository to your local machine using [GitHub Desktop](https://github.com/apps/desktop).

Build Feature by Feature
------------------------

Next, I open the repository in an AI coding assistant like [Cursor](https://www.cursor.com/) (more affordable) or [Roo Code](https://github.com/RooVetGit/Roo-Code) (higher quality, but more expensive and complex). After installing:

1.  Provide a detailed explanation of my app’s purpose
2.  Have the AI generate comprehensive documentation in a /docs/ folder
3.  Build features one by one, always asking the AI to implement error handling and console logging

For authentication and databases, I typically use Supabase and have the AI assist with integration, being careful not to expose API keys.

Debugging Strategically
-----------------------

Errors are inevitable when building with AI. I’ve found it’s best to expect a 50% error rate and develop debugging strategies accordingly:

For simple errors:

*   Test each feature individually
*   Use console logs to identify issues
*   Feed error messages back to the AI for fixes

For complex errors:

*   Use [RepoMix](https://repomix.com/) (I use the [Cursor extension](https://repomix.com/guide/installation#vscode-extension)) to copy crucial parts of the codebase
*   Paste the code into a more powerful reasoning model like OpenAI’s O1-Pro or DeepSeek R1
*   Ask the model to create a detailed technical breakdown of the bug and specific actions to fix it
*   Have your coding assistant implement these fixes

This approach not only resolves errors but also helps you understand how your code works, improving your ability to manage the project over time.

Security and Deployment
-----------------------

Before deploying, use RepoMix and upload the entire repository to Claude to find security vulnerabilities, especially checking for accidentally exposed API keys or other sensitive information. This is arguably the most crucial step, and I will write a detailed post about this soon.

Tips for Success
----------------

*   Progress incrementally with small, testable features
*   Implement thorough console logging to aid debugging
*   When stuck, escalate to more powerful models rather than struggling with the same tool
*   Read and understand the fixes proposed by AI to build your own knowledge
*   Document everything as you go, ensuring your AI assistants maintain context

Looking Forward
---------------

The current generation of AI tools [won’t replace professional software engineers](https://nmn.gl/blog/ai-illiterate-programmers) anytime soon, especially for enterprise software with complex business logic and compliance requirements. However, for developers with basic knowledge, these tools serve as powerful amplifiers that can dramatically accelerate development.

As someone building AI tools for code generation myself, I’m constantly amazed by how far this technology has come. Now is the perfect time to experiment with these capabilities and discover how they can enhance your development workflow.
