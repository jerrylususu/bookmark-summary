Title: What I think about when I think about Claude Code

URL Source: https://interconnected.org/home/2025/09/12/claude

Markdown Content:
Writing code with [Claude Code](https://www.anthropic.com/claude-code) doesn’t feel the same as any other way of writing code.

Quick background: it’s an AI tool that you install and run in your terminal in a code repository. It’s a _little_ like a chat interface on the command line, but mainly you type what you want, and then Claude churns away for a few minutes, looking up docs on the web, checking through your files, making a to-do list, writing code, running tests and so on, until it’s done.

This is _not_ the same as other AI code-writing tools such as Github Copilot ([as previously discussed](https://interconnected.org/home/2023/01/27/copilot) (2023)) which is a joy, and you stride along 20 auto-generated lines at a go, but is ultimately just very very good auto-complete.

No, spending a morning coding with Claude Code is different.

You just loop one minute composing a thoughtful paragraph to the agent, and three minutes waiting, gazing out the window contemplating the gentle breeze on the leaves, the distant hum of traffic, the slow steady unrelenting approach of that which comes for us all.

* * *

Yes yes other terminal-based coding agents are available. Claude Code made it work first and it’s the one I’ve used most.

* * *

Writing that “thoughtful paragraph”…

The trick with Claude Code is to give it large, but not too large, extremely well defined problems.

(If the problems are too large then you are now vibe coding… which (a) frequently goes wrong, and (b) is a one-way street: once vibes enter your app, you end up with tangled, write-only code which functions perfectly but can no longer be edited by humans. Great for prototyping, bad for foundations.)

So the experience is that, before you write, you gaze into space, building castles in the imagination, visualising in great detail the exact contours of the palisades and battlements, the colours of the fluttering flags, turning it round in your head, exploring how it all fits together. Then you have to narrate it all in clear paragraphs, anticipating Claude’s potential misunderstandings, stating precisely the future that you want.

You can and should think hard about your exact intent: [here’s a wonderful (and long) case study](https://taylor.town/diggit-000)_(taylor.town)_ and you can see there are pages and pages and pages of careful design and specification documents, before Claude is even allowed to touch code.

Claude Code didn’t work well for me the first few times I used it. I asked for too much or too little. It takes a while to calibrate your [seven-league boots](https://en.wikipedia.org/wiki/Seven-league_boots).

* * *

So the rhythm is slower versus the regular way.

I’m interested in the [subjective feeling of coding](https://interconnected.org/home/2023/12/05/code) (2023) because (to me) firmware feels like precision needlework, nested parentheses feel like being high up, etc.

I think a lot of this is about _breath?_

Conventionally: I’m sure I hold my breath when I’m midway through typing a conditional, just a little. The rhythm of my breath takes on the rhythm of writing code.

Many years ago, [Linda Stone observed email apnea](https://lindastone.net/2014/11/24/are-you-breathing-do-you-have-email-apnea/) (2014):

> I noticed, almost immediately, that once I started to work on email, I was either shallow breathing or holding my breath.

She studied it. 80% of people experienced compromised breathing working on email (the 20% who didn’t had, in their regular lives, been taught breathing techniques, and were unconsciously managing it).

BUT, cumulative breath holding contributes to stress-related diseases. The body becomes acidic – there’s feedback; when you shorten your breath, even if the cause was not initially stress, _you become stressed._

WHEREAS:

With Claude Code, I don’t have that metronome shortening my breath. I do not subject myself to “code apnea.”

So it becomes calm, contemplative.

* * *

New job concept: a hold music composer for the 3 minute waits while Claude Code is _Thinking…_

Analogy: elevator music.

I’ve been reading about the company Muzak, the subscription music company founded by George Owen Squier in 1934. [The History of Muzak](https://us.moodmedia.com/blog/history-of-muzak/):

> In the early 1920s, Squier discovered a method of transmitting information via electrical wires and realized that this new method could be used to distribute music.

But:

> Even in the 1930s, music licensing was a difficult beast to tame. At the time, music played on the radio was broadcast live, while recorded music was only licensed for personal use at home on gramophones.

And so Muzak boiled the ocean and simply recorded their own music, hundreds of musicians over the 1930s, sometimes capturing as many as twelve tracks in a day.

And then piped music into:

*   factories
*   restaurants
*   hotels
*   elevators: It was a fairly common practice to play music in elevators to both soothe passengers and pass the time since elevators were not as smooth or as fast as they are today.

Music has a psychological effect, promoted by Muzak in the 1950s:

> The basic concept of Stimulus Progression is the idea of changing the styles and tempos of music to counterbalance and influence the natural rhythms of the human body. Studies showed that employee production would dip during certain times of the day; before and after lunch, for example. Muzak playlists were then programmed against those patterns by playing more upbeat music during the slower times of the day, and vice versa.

_Anyway._

Muzak, elevator music, has a reputation for being bland and beige.

But it is _functional:_ Stimulus Progression, see. (Calm shoppers buy more.)

And it conceives of the elevator as _a space to be filled with music;_ for all its liminality it is a space which we inhabit and do not simply pass across.

And so: when Claude Code is elevating my code, we should not be waiting… we should fill the space!

[ChatGPT now has the ability to change the accent colour of the chat UI](https://help.openai.com/en/articles/11958281-updating-your-visual-experience-on-chatgpt). Same same. Give me light! Give me sound!

* * *

[A Social History of Background Music](http://passport2dreams.blogspot.com/2017/10/a-social-history-of-background-music.html?m=1) (2017):

> In the 70s, Brian Eno sat in an airport for a few hours waiting for a flight and was annoyed by the canned background music. In 1978 he produced _Ambient 1: Music For Airports,_ a mellow, experimental soundscape intended to relax listeners.

Who will be the Brian Eno of coding agent hold music?

_Music for Claude Coding._

* * *

I also use Claude Code in the process of writing normal words.

Code is text, words are text. So they built it for code but it can work just the same.

As you can see in my [colophon](https://interconnected.org/home/2024/10/28/colophon) I keep a lot of notes going back a couple decades, and these notes are a big folder of Markdown text documents. (I use [iA Writer](https://ia.net/writer) these days.)

So I pop open the root directory in the terminal and init Claude Code.

Then I say: please look over the 30-40 most recent files in the blog posts folder and - concentrating on the ones that _aren’t_ like finished posts (because I will have published those) - give me half a dozen ideas of what to write a blog post about today

I don’t use it to do any actual writing. I prefer my words to be my own. But it’s neat to riff over my own notes like this.

* * *

So you don’t _actually_ sit and do nothing for 3-4 minutes.

While it works, Claude runs commands on your computer which do anything from editing code and searching the web to, uh, deleting all files in your home directory (it can make mistakes). Fortunately it asks each time for permission. And you respond each time from a menu:

*   Yes
*   Yes and don’t even ask me next time
*   No but here’s what to try instead

So your inner loop interaction with Claude Code is approval, course correction, and Claude accelerating in autonomy and power as your approvals accrete.

It’s a loop built around positive reinforcement and forward motion. And, because of this, you personally end up building a lot of trust in Claude and its ability to plan and execute.

What you _want_ to do but absolutely MUST NOT do is start Claude Code with the flag `--dangerously-skip-permissions` which slams it into yolo mode.

Don’t do it! But you know you want to.

* * *

Then of course you want to put Claude Code in control of everything else.

e.g. [Claude on the web can now deal with spreadsheets](https://www.anthropic.com/news/create-files).

So could we give it a [Hugging Face robot arm](https://huggingface.co/docs/lerobot/so101) and stick the arm on Roomba and let it loose in my front room?

`claude "tidy my house" --dangerously-skip-permissions`

Claude Code [when pls](https://interconnected.org/home/2024/09/20/filtered)