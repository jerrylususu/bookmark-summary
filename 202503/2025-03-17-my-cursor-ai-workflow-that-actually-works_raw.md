Title: My Cursor AI Workflow That Actually Works

URL Source: https://nmn.gl/blog/cursor-guide

Published Time: 2025-03-12T00:00:00+00:00

Markdown Content:
_Using AI for coding isn’t perfect, but it definitely makes me faster._

I’ve been coding with Cursor AI since it was launched now while building my SaaS, and I’ve got some thoughts.

The internet seems split between “AI coding is a miracle” and “AI coding is garbage.” Honestly, it’s somewhere in between.

Some days Cursor helps me compelte tasks in record times. Other days I waste hours fighting its suggestions.

After learning from my mistakes, I wanted to share what actually works for me as a solo developer.

Setting Up a `.cursorrules` File That Actually Helps
----------------------------------------------------

The biggest game-changer for me was creating a `.cursorrules` file. It’s basically a set of instructions that tells Cursor how to generate code for your specific project.

Mine core file is pretty simple — just about 10 lines covering the most common issues I’ve encountered. For example, Cursor kept giving comments rather than writing the actual code. One line in my rules file fixed it forever.

Here’s what the start of my file looks like:

```
- Only modify code directly relevant to the specific request. Avoid changing unrelated functionality.
- Never replace code with placeholders like `// ... rest of the processing ...`. Always include complete code.
- Break problems into smaller steps. Think through each step separately before implementing.
- Always provide a complete PLAN with REASONING based on evidence from code and logs before making changes.
- Explain your OBSERVATIONS clearly, then provide REASONING to identify the exact issue. Add console logs when needed to gather more information.
```

Don’t overthink your rules file. Start small and add to it whenever you notice Cursor making the same mistake twice. You don’t need any long or complicated rules, Cursor is using state of the art models and already knows most of what there is to know.

I continue the rest of the “rules” file with a detailed technical overview of my project. I describe what the project is for, how it works, what important files are there, what are the core algorithms used, and any other details depending on the project. I used to do that manually, but now I just [use my own tool to generate it](https://gigamind.dev/). You can do it using Cursor itself, but I just find it faster to have it done for me with one click.

Giving Cursor the Context It Needs
----------------------------------

My biggest “aha moment” came when I realized Cursor works way better when it can see similar code I’ve already written.

Now instead of just asking “Make a dropdown menu component,” I say “Make a dropdown menu component similar to the Select component in `@components/Select.tsx.`”

This tiny change made the quality of suggestions way better. The AI suddenly “gets” my coding style and project patterns. I don’t even have to tell it exactly what to reference — just pointing it to similar components helps a ton.

For larger projects, you need to start giving it more context. Ask it to create rules files inside `.cursor/rules` folder that explain the code from different angles like backend, frontend, etc. This is such a powerful technique that I created a [Cursor extension to do it automatically](https://gigamind.dev/).

In the morning when I’m sharp, I plan out complex features with [minimal AI help](https://nmn.gl/blog/ai-illiterate-programmers). This ensures critical code is solid.

I then work with the Agent mode to actually write them one by one, in order of most difficulty. I make sure to use the “Review” button to read all the code, and keep changes small and test them live to see if they actually work.

For tedious tasks like creating standard components or writing tests, I lean heavily on Cursor. Fortunately, such boring tasks in software development are now history.

For tasks more involved with security, payment, or auth; I make sure to test fully manually and also get Cursor to write automated unit tests, because those are places where I want full peace of mind.

When Cursor suggests something, I often ask “Can you explain why you did it this way?” This has caught numerous subtle issues before they entered my codebase.

Avoiding the Mistakes I Made
----------------------------

If you’re trying Cursor for the first time, here’s what I wish I’d known:

*   Be super cautious with AI suggestions for authentication, payment processing, or security features. I manually review these character by character.
*   When debugging with Cursor, always ask it to explain its reasoning. I’ve had it confidently “fix” bugs by introducing even worse ones.
*   Keep your questions specific. “Fix this component” won’t work. “Update the onClick handler to prevent form submission” works much better.
*   Take breaks from AI assistance. I often code without Cursor and came back with a better sense of when to use it.

Despite the frustrations, I’m still using Cursor daily. It’s like having a sometimes-helpful junior developer on your team who works really fast but needs supervision.

I’ve found that being specific, [providing context](https://gigamind.dev/), and always reviewing suggestions has transformed Cursor from a risky tool into a genuine productivity booster for my solo project.

The key for me has been setting boundaries. Cursor helps me write code faster, but I’m still the one responsible for making sure that code works correctly.

What about you? If you’re using Cursor or similar AI tools, I’d love to hear what’s working or not working in your workflow.
