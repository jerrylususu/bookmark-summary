Title: Intermediate Developer

URL Source: https://dawranliou.com/blog/intermediate-dev/

Markdown Content:
Published: 2023-08-04

This is a story of an average intermediate software developer.

Being an intermediate developer, I cared a lot about my code. I spent a fair share of time weighing the pros and cons of my approaches to solving problems. Is this code too clever to be understood? Are there hidden invariants that weren't being explained? How easy is the code to be changed in the future? How aesthetic is the code, subjectively?

Being an intermediate developer, I empathize a lot with my PR reviewers. I spent my time in `git rebase --interactive` mode to organize the git history so it tells an appealing story from start to finish. I pick and choose chunks in Magit so commits are focused and avoid accidentally including unnecessary changes. Move up, move down, reword, fixup, and squash commits all came in handy. How easy can reviewers to understand the problem I'm solving when they need more context? Can I give them more visuals like diagrams or GIF animation so I can communicate my work better?

Being an intermediate developer, I read a lot of code and technical documentation. Libraries code is a great place to learn from the more experienced. Public technical documents like RFCs are resources. When modifying legacy code, always seek to understand before trying to be understood. Digging into git history to know why certain code was written and finding as much documentation as available is necessary. Never dismiss the code too quickly before understanding the history of a piece of code.

Being an intermediate developer, I document knowledge worth sharing with my colleagues. Not only do I write the technical documentation or submit bug tickets, but I also spend time crafting git commits, doc-strings, or even code comments. Those are good places to document "the why" behind the code. Clean code can communicate "what the code does" well. "Why the code does things" is better communicated in the other forms. Code comments are not code smells when used precisely.

As an intermediate developer, I don't shy away from learning our full application stack. Application front-end, backend, async job scheduler, and job workers are the obvious ones. When needed, optimizing PostgreSQL query with `EXPLAIN ANALYZE` can be done. Familiar myself with enough DevOps toolings so I can support the team when the Jenkins pipelines break. Occasionally digging into the ClojureScript compiler code so I can troubleshoot obscure advanced compilation bugs. I read a lot and learned a lot.

Being an intermediate developer, I write tests to improve coverage. "A problem well-stated is half-solved." I don't do very strict TDD, but writing tests beforehand gives me good targets. I can always do interactive rebases to fix the git history by amending the tests. Good tests can tell better stories than other forms of documentation.

As an intermediate developer, I greatly care about my team's success. I review others' code, give feedback on their work, and offer them help to unblock them. Despite the occasionally non-blocking nick-picks about others' work, my job here is to understand their work, not to be a human compiler to uncover bugs, nor to gate-keep codes that do not follow any superficial code style guides. As a reviewer, I learn from my teammates' code and make sure the knowledge is passed on.

Being an intermediate developer, I help my team to onboard new people. I share my workflow, REPL development tricks, Emacs lisp code specific to our working environment, documentation, and things not well-documented by the generations of developers that have worked on it.

Being an intermediate developer, I extend my help to other teams. I work closely with Designers and Quality Engineers to answer questions about features and help them flesh out the UI/UX inconsistencies. I spend hours digging into the DevOps pipelines to familiarize myself with the toolings to help DevOps team to investigate issues that touch both the Clojure domain and the Operations domain.

As an intermediate developer, I keep an eye on the wider programming community to learn from the thought leaders and the great open-source projects and bring what I know to our code base and technical discussions. [Common Lisp](https://lisp-lang.org/) is a very vibrant community and has so many great ideas. [Fennel](https://fennel-lang.org/) is a fun language that helps me to learn [Lua](https://www.lua.org/) better. [Janet](https://janet-lang.org/) and [CHICKEN Scheme](https://wiki.call-cc.org/) have taught me more about C and low level programming.

This is a story about an average intermediate Clojure developer.

—

****Epilogue****

This year marks my 10th year as a professional software engineer/developer. I've grown a lot over the years. Upon reflecting on my experiences and watching my colleagues, I have many thoughts to write about what seniority means to me. I'm a pretty well-rounded Clojure programmer. However, being an effective software developer is so much more than just programming. "Programs are meant to be read by humans and only incidentally for computers to execute." Communication is the essence of programming. The same is true of the other parts of my day-to-day work as an intermediate developer - reading/writing docs, reviewing PRs, discussing UI/UX with Designers and Quality Engineers, breaking down problems into predictable chunks of work, helping the customer support team to provide customer questions, etc.

I think this article is 90% the recording of what I've become as an intermediate developer and 10% as my praise for the Clojure language and its community. To this day, I'm still glad that I taught myself Clojure 5 years ago. I attribute a lot of my success today to Clojure because it kept me focused so I could develop the other areas much better. Also, the team I worked with in Kira Systems for the past 3.5 years has been highly supportive, and I've grown a lot since I joined.

This article is a reminder for my future self of what I've achieved as an intermediate developer. I hope I've grown even more when I look back at this article in the future.