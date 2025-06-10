Title: crawshaw - 2025-06-08

URL Source: https://crawshaw.io/blog/programming-with-agents

Markdown Content:
How I program with Agents
-------------------------

_2025-06-08_

This is the second part of my ongoing self-education in how to adapt my programming experience to a world with computers that talk. The first part, [How I program with LLMs](https://sketch.dev/blog/programming-with-llms), covered ways LLMs can be adapted into our existing tools (basically, autocomplete) and how careful prompting can replace traditional web search. Now I want to talk about the harder, and more rewarding act of using agents to program.

Define Agent
------------

It is worthwhile starting with a definition of the word “agent” in the context of LLMs. The “AI” hype cycle has been throwing this very generic word around longer than agents have actually been useful constructs. As a result there is a bit of smoke and mirrors marketing and general mysticism to dig through to find any value in the word. For someone with an engineering background there is now a straightforward definition: [an agent is 9 lines of code](https://sketch.dev/blog/agent-loop). That is, an agent is a for loop which contains an LLM call. The LLM can execute commands and see their output without a human in the loop.

That’s it. Like all simple things your instinct, quite reasonably, could be to say “so what?” It is a for loop. But the results are an astonishing improvement on the power of a raw large language model.

Whiteboard programming
----------------------

Consider yourself in front of a whiteboard, writing a function in C with a marker designed to test if a UTF-8 string is valid. (This has actually happened to me, it is a standard interview technique. The stakes were high, this interview changed the course of my career!) How well you do at this task depends on your experience as a programmer, and your ability to fudge your inability to use external resources. You need to remember the encoding of UTF-8. You need to not confuse your C grammar with all the other C-like programming languages you have used over your career (is it name-then-type or type-then-name?). In daily life you get feedback from a compiler if you make a mistake, you can look up a specification of UTF-8, and best of all you can write your program and sprinkle some printfs in it to see what you got wrong.

Asking an agentless LLM to write code is equivalent to asking you to write code on a whiteboard. It is an exercise in dredging up half-forgotten memories, executing a parser on an extraordinarily inefficient substrate, attempting to avoid hallucinating an actually-useful programming interface. The fact LLMs can invent programs out of whole cloth is an astonishing technical achievement that I consider myself blessed to have lived to see, but it is also not a huge shock that attaching a GPU to a virtual whiteboard is not going to do a significant amount of useful programming.

But what happens if we give an LLM more than a virtual whiteboard? What if it could call the compiler, see the compiler errors, and get a chance to fix them before we see the result? What if it could use `grep` and `cat` to read existing files in a project? What if it could patch multiple existing files, including the unit tests and repeatedly run the tests? Agents are feedback-driven LLMs.

Agents are LLMs with environmental feedback
-------------------------------------------

Just as humans thrive in environments with feedback, LLMs go from nice demos to useful programmers when given a surprisingly small core set of tools that are very familiar to programmers:

*   `bash(cmd)`
*   `patch(hunks)`
*   `todo(tasks)`
*   `web_nav(url), web_eval(script), web_logs(), web_screenshot(), etc`
*   `keyword_search(keywords)`
*   `codereview()`

Agents are very good at navigating code bases using the bash tool: find, cat, grep -R, just the way those of us who predate IDEs tend to navigate code bases. Upfront it is instructed to commit changes to git, which it does by using the bash tool to run git add, git commit, etc.

The result, compared to an LLM generating code without these tools available is significantly different. Of note:

*   API use is greatly improved because the agent can web search for documentation and `curl` the docs into its context window.

*   Compiler feedback reduces syntax errors and hallucinated interfaces.

*   The compiler in a full development environment also improves dependency management, by helping the LLM understand features of the particular version of a dependency that a project uses. (This is an ongoing weakness of LLMs though, they will use documentation from a newer API version or make assumptions that apply only to older versions of a dependency. We have plans to address with this sketch.dev)

*   Test failures help find errors in generated code, and have a positive reinforcing effect of getting the LLM to write tests for new code.

*   LLMs can handle larger code bases than fit in the context window because they selectively choose which pieces of the codebase to read.

*   Agents can try the end product themselves: run the code, take a screenshot of a page from the browser, feed it back into the model and keep tweaking the CSS based on the end-to-end rendering. When things go really wrong, read the server logs, find the panic, fix it and add a test.

The downside of agents is time. A single sentence request that would have required a 200 token response can now generate tens of thousands of intermediate tokens driving tools, some web searching, and many runs of a project test suite. This takes several minutes and there are only so many cups of coffee we can healthily brew in one day.

Today it may also appear costly (my last significant agent-driven commit cost me $1.15 in API credits!) but the cost will rapidly disappear as the chips driving the models continue to improve. GPUs are not nearly as restricted in their future progress as CPUs which are far more constrained in how they can physically improve (compiler-driven [ILP](https://en.wikipedia.org/wiki/Instruction-level_parallelism) only goes so far). The fact that we still call LLM chips “graphics” chips shows the economic machine underneath software has a lot of restructuring to do before it is fully focused on LLM performance-per-watt.

Ultimately, agents spend CPU and GPU cycles doing intermediary work so that humans do not need to. Any time I can mechanise my labor I get more done, so agents are a huge step forward for me. I only end up writing a tiny fraction of the programs I want to due to a shortage of hours in the day, and with agent support I get a little further into the list of programs I wish I could write. May we all be so lucky as I have been this last year. As such, I am thoroughly convinced that agents are worth significant engineering investment addressing their limitations.

It is relatively easy to see an example of an agent producing useful work. Drop one into your project, break off a small task and type it in, see what it does. Let me give you two examples.

Example: Github App auth
------------------------

Let me talk you through an example of where I used an agent to do a significant amount of work on a project. I implemented the first pass of Github App auth for the hosted sketch.dev using sketch. It did the whole thing with 3-4 pieces of feedback as I clicked around the interface finding errors. That is an astonishing achievement. It is easy for the haughty to disregard the work of gluing well-known APIs together as “not real” programming, but it has been the practical experience of my career that for every hour of truly interesting programming I can do, I have had to do 10 or more hours of dreary work with APIs, libraries, dysfunctional compilers, build systems, or obtuse package managers to actually make that hour useful. Having a tool that lets me do 30 minutes of “not real” programming by writing a few carefully constructed sentences, and lets me vacuum the kids' room while it works, **preserves momentum**.

But now comes the work. It implemented the GitHub app auth flow I wanted. It even met the stringent requirement I put on it: I asked it if it could avoid saving a token per user, and instead use the global private credentials of the app to drive everything to keep the database simple. It did it! In the process of doing it, it wrote some very bad code.

First, is the huge security vulnerability it created. Because it let anyone who had authorized the app work with any repository authorized with the app, even if they did not have access to it. Disaster. Fortunately it is so bad that if we had got to testing with others on the team we would have spotted it quickly when our own private repos started appearing on each other’s repository lists. (And was such an obvious problem I caught it even before that.)

 A quick explanation of the problem to sketch.dev got it to fix it, it implemented authorization checks for users and got it right. Another amazing achievement, I wrote one sentence and got a reworked functioning commit on a branch.

The next problem was performance. While the new code worked, it would have been unworkably slow as soon as it had several users. It generated a list of repositories the user had access to by:

```
for install := range allAppInstallations {  
	for r := range install.Repositories() {  
		if r.IsCollaborator(user) {  
			// add to available repositories  
		}  
	}  
}
```

This meant that every time I wanted to display to the user a list of repositories they had authorized, I had to, for each GitHub org that had allowed the use of Sketch, do an API call to fetch their repository list, and then for every single repository do another API call to check if this person is a user. This means the number of API calls grows with the total number of product users, which is not going to work.

It turns out, the problem was my original naive requirement to avoid storing per-user tokens from GitHub. It turns out they do not have any efficient app-auth-level API calls to determine what a user can access, the only way to do it efficiently is to ask what access the auth token has, and use an auth token for the user.

Once I realized this I told sketch to go back and remove my original requirement: save per-user auth tokens and use them for everything. It quickly came up with efficient API calls.

Telling this story took more words than I typed in total into Sketch to generate the GitHub auth code I wanted, and writing it took more effort than the code reviews that caught all the issues. I need to emphasize that because it is so easy to take a part of an anecdote like this and use the limits and mistakes of these tools to declare them “useless” or “dangerous”, while my experience is not that at all. What we have today can clearly not replace me as a programmer, but it did let me get done in a day a dreary task that I would have struggled to traditionally complete in a week. And I vacuumed the kid’s room while I was at it.

Example: SQL conventions around JSON
------------------------------------

Here is an example of something my agent needs to do regularly that it struggled with until I found a way to help it (and I believe captures a typical limitation people run into when first trying to work with LLMs).

I learned an odd way of using SQL at Tailscale (from Brad and Maisem): make every table a JSON object. In particular, have only one “real” column and the rest generated from the JSON. So the typical table looks like:

```
CREATE TABLE IF NOT EXISTS Cookie (  
  Cookie   TEXT    NOT NULL AS (Data->>'cookie')  STORED UNIQUE, -- PK
  UserID   INTEGER NOT NULL AS (Data->>'user_id') STORED REFERENCES User (UserID),  
  Created  INTEGER NOT NULL AS (unixepoch(Data->>'created')) STORED,  
  LastUsed INTEGER AS (unixepoch(Data->>'last_used')) CHECK (LastUsed>0),  
  Data     JSONB   NOT NULL  
);
```

This has many pros and many cons. It acts as a poor man’s ORM as each table has an “obvious” data type matching each record. It makes adding to the schema trivial. You can choose to ADD COLUMN if you like but you do not have to. The SQL column constraints act as good dynamic checks on the quality of your JSON. It greatly increases the amount of stored data per row. You have to structure all your INSERT and UPDATEs in terms of JSON. Half a foot in the document database world, but I can still write an old fashioned JOIN. Etc.

Pros and cons aside (that can be a fun blog post for the future), our agent often tripped over this style. When creating new tables and columns, it would sometimes, but not always, follow the generated column pattern. The very first time we added a table that did not use this all-generated-column style it got further confused, and would choose almost at random it seemed between styles.

It turned out to be really easy to fix the agent’s behavior. At the top of the SQL schema file I tried adding a three sentence description of this. The key line seems to be “each table has a single concrete Data JSON column, all other columns are generated from it” and then a comment on the tables that did not follow this pattern explaining they were an exception to the norm, and the behavior improved dramatically.

This is slightly counter-intuitive. My lived experience of instructions like this is that engineers heavily discount them. It may be ad(-like) blindness, it may be the challenge of keeping comments up to date, or it may be that most comments are not worth much attention.. Instead the industry norm for communicating this kind of knowledge is an unpleasant routine of engineers who do not know writing a PR that does it the wrong way, then receiving comments on it and telling them to do more work. LLMs seem to give the comments more work, hopefully for the better.

“Asset” and “debt” models of code
---------------------------------

One of the arguments against LLM as a code generation tool is that generating code is only a small fraction of the overall cost of code. The ongoing work of dealing with existing code is the vast majority of the cost, goes the argument. There are code bases where this statement is clearly true. In heavily used products with a growing user base adding new ways of using programs, engineers do spend most of their time navigating the unwritten misunderstood interdependencies of existing code. To someone whose job is that, a computer you can talk to that produces a usable result for “implement bubble sort in fortran” sits somewhere between a toy and nuisance. Sometimes attempts to compare this to financial concepts such as “assets” and “debts” are used, but I will skip them as they never seem to quite fit.

Whether this understanding of engineering, which is correct for some projects, is correct for engineering as a whole is questionable. Very few programs ever reach the point that they are heavily used and long-lived. Almost everything has few users, or is short-lived, or both. Let’s not extrapolate from the experiences of engineers who only take jobs maintaining large existing products to the entire industry.

Fortunately we do not have to answer the question of what the entirety of programming looks like to say if agents are valuable, because agents are potentially useful even in the maintenance of existing products. An agent is not just code generation. It is an LLM with a series of tools that reads code, and changes code by editing files.

Agents are as happy removing code as adding it.

The result is change. Yes, the change is “more work” because the person driving an agent has to understand the change being made. Yes, the agent may not have sufficient understanding to change large products yet. But change is the ultimate goal of the engineer driving the tool, and agents are demonstrating the ability to edit moderately large projects with some care. That makes them potentially useful tools everywhere in the programming industry. If agents are not good enough yet (and that’s a big if, it is well worth testing), they are on the right track and now have all the fundamentals to get there.

A related, but tricker topic is one of the quieter arguments passed around for harder-to-use programming tools (for example, programming languages like C with few amenities and convoluted build systems) is that these tools act as gatekeepers on a project, stopping low-quality mediocre development. You cannot have sprawling dependencies on a project if no-one can figure out how to add a dependency. If you believe in an argument like this, then anything that makes it easier to write code: type safety, garbage collection, package management, and LLM-driven agents make things worse. If your goal is to decelerate and avoid change then an agent is not useful.

Why are we seeing agents now?
-----------------------------

Unlike somewhat mysterious ideas like the transformer architecture that underpins LLMs, mechanical feedback into an LLM seems “obvious.” It is clear to those of us who think about developer tools: I have been working on it for over a year now, but our first revision of sketch.dev in January, despite having go tooling wired into an LLM, hardly counts as an agent by the standards of what we can use today. (The difference in utility between the first revision of sketch and the current [sketch](https://github.com/boldsoftware/sketch) open source project is astonishing.) The utility of feedback is also clear to everyone who works in the ML field, as [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) has been one of the core tenants of the field for 50 years.

The answer is a critical chunk of the work for making agents useful is in the training process of the underlying models. **The LLMs of 2023 could not drive agents, the LLMs of 2025 are optimized for it.** Models have to robustly call the tools they are given and make good use of them. We are only now starting to see frontier models that are good at this. And while our goal is to eventually work entirely with open models, the open models are trailing the frontier models in our tool calling evals. We are confident the story will change in six months, but for now, useful repeated tool calling is a new feature for the underlying models.

What is next
------------

It is challenging to think about what is next in a fast-moving field where most engineers today are not even using these tools yet. But those of us building these tools need to think about it.

Most use of agents today is either in the IDE or in a checked out repository on a development machine. This is an easy way to get started, it’s easy to install a vscode fork or a command line tool and run it. But it has two significant limits.

The first major limit is that agents need a lot of safeguards built into them to avoid them running amok. One of my machines has production credentials squirreled away on it I can use to do deployments. As part of running commands is the agent going to grab those credentials and run my deploy script for its uncommitted changes? Avoiding this, if your agent runs directly on your real computer, involves a lot of asking the programmer to babysit the tool calls and give the agent permission to run commands. And even then, there are dangers. I can say “yes to all” to running curl, only to forget a web server I’m developing that’s running on localhost doesn’t have any auth yet and can read arbitrary files off disk. Oops, my production credentials are exposed again.

The second major limit is requiring developers to use their bespoke manually-configured development environments to run an agent means we are effectively serializing execution of an agent. As mentioned earlier, one of the major weaknesses of agents is they take several minutes per turn to produce good results (and probably will for the foreseeable future). One way to make better use of our time is for an engineer to be driving several agents simultaneously, but this sort of agent deployment makes that impractical.

We are exploring solving both of these issues in [sketch.dev](https://sketch.dev/) using containers. By default sketch creates a little development environment in a container with a copy of the source code and the runner has the ability to extract git commits from the container. This lets you run many simultaneously. (Other agents are also exploring this space, agents in general are a very busy space!)

To give you an example of how this parallelism can work in practice, while I was working on the GitHub auth mentioned in the above example, I was about to complain in a group chat about how ugly a form I made is. Instead, I opened a second copy of Sketch and pasted in a screenshot of the form and wrote “this is ugly, please make it less ugly.” I went back to thinking about auth, and when I remembered I had typed that a half hour later I looked at the results and decided yes, it is an improvement. So I asked it to rebase, it resolved the merge conflict (one of my least favorite programming tasks!), and I pushed the update. It was not nearly the quality a real designer can produce, but it was certainly better than the awful unstyled form I had created during testing. In a past life I would have created an issue in the issue tracker, by which I mean I would have made a note in my personal to-do.txt file to create an issue, because issues are visible to other programmers and require typing something more coherent and constructive than pasting a screenshot and saying “this is ugly, please fix.” One of the great things about talking to an agent is if you only have a tiny bit of mental energy left you have a good chance of getting something of value out of 30 seconds work. The likelihood I would have ever turned the to-do.txt entry into a real issue is, honestly, pretty low.

So our takeaway from exploring the UX of agents for the past six months is that we may finally have a good use for “development” containers.

What does the IDE become?
-------------------------

An open question that we are spending a lot of time exploring is: what does the IDE become in this environment? Let us say we start work by talking to an agent. The execution container can be completely derived from GitHub, the changes shown as a diff and pushed as a branch (or PR). Is that the actual workflow?

In practice, many of the commits generated by sketch, or any other agent we have tried, require some human cleanup afterwards. (Our experience is, when programmers first use an agent most commits need manual intervention, but practice writing prompts reduces the number of necessary intervention.) It could be as simple as editing a comment or changing a variable name. It can be more significant. How do we make that work with a containerized world?

So far we have several workflows that we quite like that other agents have not yet explored. One is making the diff view editable. You can type in the right-hand-side of Sketch’s diff view and it ends up in the commit and pushed for you. It is great for one-line edits.

For the sorts of fixups where you want to run sed, or grep through the changes, or run the tests in an interesting way, we have had great success with giving the user ssh access to the container. Not only can you shell in (and we have a little web terminal in the UI too), it is easy to turn this into a vscode:// URL that can be opened directly in a traditional IDE, which is sometimes exactly what we want.

Finally, we let you write “code review” style comments on the diff view in sketch.dev and send them back to the agent as feedback. Commenting directly on a line of a diff can greatly reduce the amount we have to type (and is very familiar from our long practice in the code review process).

Overall, we are convinced that containers can be useful and warranted for programming. The idea has been around for a long time but I have never personally wanted to start programming in a container. But cleaning up a diff that an agent wrote for me in a container is far more interesting.

A final note
------------

The process of learning and experimenting with LLM-derived technology has been an exercise in humility. In general I love learning new things when the art of programming changes: dealing with the switch to multi-core programming, rethinking software design when SSDs replaced HDDs and dropped seek latencies, when everything was suddenly reachable on the same inter-network, these sorts of shifts in the industry are a joy to deal with. (Not to be confused with useless makework like the latest JavaScript framework, the latest cloud provider service, or the latest cluster orchestration software.) These sorts of challenges affected how my programs work: the choice of algorithms, languages, libraries, etc. But LLMs, and more specifically Agents, affect the process of writing programs in a new and confusing way. Absolutely every fundamental assumption about how I work has to be questioned, and it ripples through all the experience I have accumulated. There are days when it feels like I would be better off if I did not know anything about programming and started from scratch. And it is still changing.

The way this all works today is very different than six months ago, and I do not believe we are at a stable point yet. I believe a lot of norms around team interactions will also be changing. For example, **the mostly-broken process of half-hearted code review that has been adopted across the industry no longer solves the problems it barely solved before**. It needs to be reinvented. The “IDE”, which has never been nearly as integrated as it has claimed to be, needs to be torn up and repurposed. The industry now seems aware of this, but has not taken an agent-first approach yet. There is a lot to do, and I suspect in six months things will be very different again. Curiosity and humility will get us through it, but even more than usual I would suggest turning away from internet forums where people talk in circles about this technology. That is a job for an agent.

_This post also appears on the [sketch blog](https://sketch.dev/blog/programming-with-agents)._

_Thanks to Sean McCullough, Philip Zeyliger, and Thomas Ptacek for reviewing this post._
