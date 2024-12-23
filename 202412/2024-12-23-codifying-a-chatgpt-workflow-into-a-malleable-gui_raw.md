Title: Codifying a ChatGPT workflow into a malleable GUI

URL Source: https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms

Markdown Content:
Wouldn't it be neat if you could use LLMs to create little personal utility apps as the need arises? Here's a story where I did just that...

In my previous post, [Malleable software in the age of LLMs](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming), I laid out a theory for how LLMs might enable a new era of people creating their own personal software:

> I think it’s likely that soon all computer users will have the ability to develop small software tools from scratch, and to describe modifications they’d like made to software they’re already using.
> 
> In other words, LLMs will represent a step change in tool support for end-user programming: the ability of normal people to fully harness the general power of computers without resorting to the complexity of normal programming. Until now, that vision has been bottlenecked on turning fuzzy informal intent into formal, executable code; now that bottleneck is rapidly opening up thanks to LLMs.

Today I’ll **share a real example where I found it useful to build custom personal software with an LLM**. Earlier this week, I used GPT-4 to code an app that helps me draft text messages in English and translate them to Japanese. The basic idea: I paste in the context for the text thread and write my response in English; I get back a translation into Japanese. The app has a couple other neat features, too: I can drag a slider to tweak the formality of the language, and I can highlight any phrase to get a more detailed explanation.

The whole thing is ugly and thrown together in no time, but it has exactly the features I need, and I’ve found it quite useful for planning an upcoming trip to Japan.

![Image 12](https://www.geoffreylitt.com/images/article_images/texting-app-teaser.png?1734903615)

The app uses the GPT-4 API to do the actual translations. So there are two usages of LLMs going on here: I used an LLM to code the app, and then the app also uses an LLM when it runs to do the translations. Sorry if that’s confusing, 2023 is weird.

You may ask: why bother making an app for this? Why not just ask ChatGPT to do the translations? I’m glad you asked—that’s what this post is all about! In fact, I started out doing these translations in ChatGPT, but **I ended up finding this GUI nicer to use than raw ChatGPT for several reasons**:

*   It encodes a prescriptive workflow so I don’t need to fuss with prompts as much.
*   It offers convenient direct manipulation affordances like text boxes and sliders.
*   It makes it easier to share a workflow with other people.

(Interestingly, these are similar to the reasons that so many startups are building products wrapping LLM prompts—the difference here is that I’m just building the tool for myself, and not trying to make a product.)

A key point is that making this personal GUI is only worth it because **GPT also lowers the cost of making and iterating on the GUI!** Even though I’m a programmer, I wouldn’t have made this tool without LLM support. It’s not only the time savings, it’s also the fact that I don’t need to turn on my “programmer brain” to make these tools; I can think at a higher level and let the LLM handle the details.

There are also tradeoffs to consider when moving from ChatGPT into a GUI tool: the resulting workflow is more rigid and less open-ended than a ChatGPT session. In a sense this is the whole point of a GUI. But the GUI isn’t necessarily as limiting as it might seem, because remember, it’s _malleable_—I built it myself using GPT and can quickly make further edits. This is a very different situation that using a fixed app that someone else made! Below I’ll share one example of how I edited this tool on the fly as I was using it.

Overall I think this experience suggests an intriguing workflow of **codifying a ChatGPT workflow into a malleable GUI**: starting out with ChatGPT, exploring the most useful way to solve a task, and then once you’ve landed on a good approach, codifying that approach in a GUI tool that you can use in a repeatable way going forward.

Alright, on to the story of how this app came about.

* * *

ChatGPT is a good translator (usually 🙃)[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#chatgpt-is-a-good-translator-usually)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

I’m going on a trip to Japan soon and have been on some text threads where I need to communicate in Japanese. I grew up in Japan but my writing is rusty and painfully slow these days. One particular challenge for me is using the appropriate level of formality with extended family and other family acquaintances—I have fluent schoolyard Japanese but the nuances of formal grown-up Japanese can be tricky.

I started using ChatGPT to make this process faster by asking it to produce draft messages in Japanese based on my English input. I quickly realized **there are some neat benefits to ChatGPT vs. a traditional translation app**. I can give it the full context of the text thread so it can incorporate that into its translation. I can steer it with prompting: asking it to tweak the formality or do a less word-for-word translation. I can ask follow-up questions about the meaning of a word. These capabilities were all gamechangers for this task; they really show why smart chatbots can be so useful!

You may be wondering: how good were the translations? I’d say: good enough to be spectacularly useful to me, _given that I can verify and edit_. Often they were basically perfect. Sometimes they were wrong in huge, hilarious ways—flipping the meaning of a sentence, or swapping the name of a train station for another one (sigh, LLMs…).

In practice these mistakes didn’t matter too much though. I’m slow at writing in Japanese but can read basic messages easily, so I just fix the errors and they aren’t dealbreakers. **When creation is slow and verification is fast, it’s a sweet spot for using an LLM.**

Honing the workflow[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#honing-the-workflow)
-------------------------------------------------------------------------------------------------------------------------------

As I translated more messages and saw ways that the model failed, I developed some little prompting tricks that seemed to produce better translations. Things like this:

> Below is some context for a text message thread:
> 
> …paste thread…
> 
> Now translate my message below to japanese. make it sound natural in the flow of this conversation. don’t translate word for word, translate the general meaning.
> 
> …write message…

I also learned some typical follow-up requests I would often make after receiving the initial translation: things like asking to adjust the formality level up or down.

Once I had landed on these specific prompt patterns, it made my interactions more scripted. Each time I would need to dig up my prompt text for this task, copy-paste it in, and fill in the blanks for this particular translation. When asking follow-up questions I’d also copy-paste phrasings from previous chats that had proven successful. **At this point it didn’t feel like an open-ended conversation anymore; it felt like I was tediously executing a workflow made up of specific chat prompts.**

I also found myself wanting to have more of a feeling of a solid tool that I could return to. ChatGPT chats feels a bit amorphous and hard to return to: where do I store my prompts? How do I even remember what useful workflows I’ve come up with? I basically wanted a window I could pop open and get a quick translation.

Making a GUI with GPT[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#making-a-gui-with-gpt)
-----------------------------------------------------------------------------------------------------------------------------------

So, I asked GPT-4 to build me a GUI codifying this workflow. The app is a frontend-only React.js web app. It’s hosted on [Replit](https://replit.com/), which makes it easy to spin up a new project in one click and then share a link with people. (You can see the current code [here](https://replit.com/@GeoffreyLitt/TextMessageTranslator#src/App.jsx) if you’re curious.) I just copy-pasted the GPT-generated code into Replit.

![Image 13](https://www.geoffreylitt.com/images/article_images/texting-replit.png?1734903615)

The initial version of the app was very simple: it basically just accepted a text input and then made a request to the GPT-4 API asking for a natural-sounding translation. The early designs generated by ChatGPT were super primitive:

![Image 14](https://www.geoffreylitt.com/images/article_images/early-designs.png?1734903615)

Asking it for a “professional and modern” redesign helped get the design looking passable. I then asked GPT to add a _formality slider_ to the app. The new app requests three translations of varying formality, and then lets the user drag a slider to instantly choose between them 😎

GPT-4 did most of the coding of the UI. I didn’t measure how long it took, but subjectively, the whole thing felt pretty effortless; **it felt more like asking a friend to build an app for me than building it myself**, and I never engaged my detailed programmer brain. I still haven’t looked very closely at the code. GPT generally produced good results on every iteration. At one point it got confused about how to call the OpenAI API, but pasting in some recent documentation got it sorted out. I’ve included some of the coding prompts I used at the [bottom of this post](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#appendix) if you’re curious about the details.

At the same time, it’s important to note that **my programming background did substantially help the process along** and I don’t think it would have gone that well if I didn’t know how to make React UIs. I was able to give the LLM a detailed spec, which was natural for me to write. For example: I suggested storing the OpenAI key as a user-provided setting in the app UI rather than putting it in the code, because that would let us keep the app frontend-only. I also helped fix some minor bugs.

I do believe it’s possible to get to the point where an LLM can support non-programmers in building custom GUIs (and that’s in fact one of my main research goals at the moment). But it’s a much harder goal than supporting programmers, and will require a lot more work on tooling. More on this later.

Iterating on the fly[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#iterating-on-the-fly)
---------------------------------------------------------------------------------------------------------------------------------

A few times I noticed that the Japanese translations included phrases I didn’t understand. Once this need came up a few times, I decided to add it as a feature in my GUI. **I asked GPT to modify the code so that I can select a phrase and click a button to get an explanation in context:**

![Image 15](https://www.geoffreylitt.com/images/article_images/explain-phrase.png?1734903615)

This tight iteration loop felt awesome. Going from wanting the feature to having it in my app was accomplished in minutes with very little effort. This shows the benefit of having a _malleable GUI_ which I control and I can quickly edit using an LLM. My feature requests aren’t trapped in a feedback queue, I can just build them for myself. It’s not the best-designed interaction ever, but it gets the job done.

I’ve found that having the button there encourages me to ask for explanations more often. Before, when I was doing the translations in ChatGPT, I would need to explicitly think to write a follow-up message asking for an explanation. Now I have a button reminding me to do it, and the button also uses a high-quality prompt that I’ve developed.

My brother asked me to try the tool. I sent him the Replit link and he was able to use it.

I think sharing a GUI is probably way more effective than trying to share a complex ChatGPT workflow with various prompts patched together. The UI encodes what I’ve learned about doing this particular task effectively, and provides clear affordances that anyone can pick up quickly.

From chatbot to GUI[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#from-chatbot-to-gui)
-------------------------------------------------------------------------------------------------------------------------------

What general lessons can we take away from my experience here? I think it gestures at two big ideas.

The first one is that **chatbots are not always the best interface for a task**, even one like translation that involves lots of natural language and text. Amelia Wattenberger wrote a [great piece](https://wattenberger.com/thoughts/boo-chatbots) explaining some of the reasons. It’s worth reading the whole thing, but here’s a key excerpt about the value of affordances:

> Good tools make it clear how they should be used. And more importantly, how they should not be used. If we think about a good pair of gloves, it’s immediately obvious how we should use them. They’re hand-shaped! We put them on our hands. And the specific material tells us more: metal mesh gloves are for preventing physical harm, rubber gloves are for preventing chemical harm, and leather gloves are for looking cool on a motorcycle.
> 
> Compare that to looking at a typical chat interface. The only clue we receive is that we should type characters into the textbox. The interface looks the same as a Google search box, a login form, and a credit card field.

This principle clearly holds when designing a product that other people are going to use. But perhaps surprisingly, in my experience, **affordances are actually useful even when designing a tool for myself!** Good affordances can help my future self remember how to use the tool. The “explain phrase” button reminds me that I should ask about words I don’t know.

I also find that making a UI makes a tool more memorable. My custom GUI is a visually distinctive artifact that lives at a URL; this helps me remember that I have the tool and can use it. Having a UI makes my tool feel more like a reusable artifact than a ChatGPT prompt.

Now, it’s not quite as simple as “GUI good, chatbot bad"—there are tradeoffs. For my translation use case, I found ChatGPT super helpful for my initial explorations. The open-endedness of the chatbot gave it a huge leg up over Google Translate, a more traditional application with more limited capabilities and clearer affordances. I was able to explore a wide space of useful features and find the ones that I wanted to keep using.

I think this suggests a natural workflow: **start in chat, and then codify a UI if it’s getting annoying doing the same chat workflow repeatedly.**

By the way, one more thing: there are obviously many other visual affordances to consider besides the ones I used in this particular example. For example, here’s another example of a GPT-powered GUI tool I built a couple months ago, where I can drag-and-drop in a file and see useful conversions of that file into different formats:

> I wanted to convert a JSON file of a chat transcript into nice markdown text for sharing w/ people…
> 
> so I had GPT generate an ephemeral React UI where I can drag in the JSON file and it outputs the markdown🤓
> 
> reflections on the process: [pic.twitter.com/WGwBBtEGiT](https://t.co/WGwBBtEGiT)
> 
> — Geoffrey Litt (@geoffreylitt) [May 4, 2023](https://twitter.com/geoffreylitt/status/1654246096212992004?ref_src=twsrc%5Etfw)

Another takeaway: **it feels great to use a tiny GUI made just for my own needs**. It does only what I want it to do, nothing more. The design isn’t going to win any awards or get VC funding, but it’s good enough for what I want. When I come across more things that the app needs to do, I can add them.

Robin Sloan has this delightful idea that [an app can be a home-cooked meal](https://www.robinsloan.com/notes/home-cooked-app/):

> When you liberate programming from the requirement to be professional and scalable, it becomes a different activity altogether, just as cooking at home is really nothing like cooking in a commercial kitchen. I can report to you: not only is this different activity rewarding in almost exactly the same way that cooking for someone you love is rewarding, there’s another feeling, too, specific to this realm. I have struggled to find words for this, but/and I think it might be the crux of the whole thing:
> 
> This messaging app I built for, and with, my family, it won’t change unless we want it to change. There will be no sudden redesign, no flood of ads, no pivot to chase a userbase inscrutable to us. It might go away at some point, but that will be our decision. What is this feeling? Independence? Security? Sovereignty?
> 
> Is it simply … the feeling of being home?

Software doesn’t always need to be mass-produced like restaurant food, it can be produced intimately at small scale. My translator app feels this way to me.

In this example, using GPT-4 to code and edit the app is what enabled the feeling of malleability for me. It feels magical describing an app and having it appear on-screen within seconds. Little React apps seem to be the kind of simple code that GPT-4 is good at producing. You could even argue that it’s "just regurgitating other code it’s already seen”, but I don’t care—it made me the tool that I wanted.

I’m a programmer and I could have built this app manually myself without too much trouble. And yet, I don’t think I would have. The LLM is an order of magnitude faster than me at getting the first draft out and producing new iterations, this makes me much more likely to just give it a shot. This reminds me of how Simon Willison says that [AI-enhanced development makes him more ambitious with his projects](https://simonwillison.net/2023/Mar/27/ai-enhanced-development/):

> In the past I’ve had plenty of ideas for projects which I’ve ruled out because they would take a day—or days—of work to get to a point where they’re useful. I have enough other stuff to build already!
> 
> But if ChatGPT can drop that down to an hour or less, those projects can suddenly become viable.
> 
> Which means I’m building all sorts of weird and interesting little things that previously I wouldn’t have invested the time in.

Simon’s description applies perfectly to my example.

It’s not just about the initial creation, it’s also about the fast iteration loop. I discussed the possibility of LLMs updating a GUI app in my [previous post](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming):

> Next, consider LLMs applied to the app model. **What if we started with an interactive analytics application, but this time we had a team of LLM developers at our disposal?** As a start, we could ask the LLM questions about how to use the application, which could be easier than reading documentation.
> 
> But more profoundly than that, the LLM developers could go beyond that and _update_ the application. When we give feedback about adding a new feature, our request wouldn’t get lost in an infinite queue. They would respond immediately, and we’d have some back and forth to get the feature implemented. Of course, the new functionality doesn’t need to be shipped to everyone; it can just be enabled for our team. This is economically viable now because we’re not relying on a centralized team of human developers to make the change.
> 
> ![Image 16](https://www.geoffreylitt.com/images/article_images/llm-eup/llm-app.png?1734903615)

It simply feels good to be using a GUI app, have an idea for how it could be different, and then have that new version running within seconds.

There’s a caveat worth acknowleding here: the story I shared in this post only worked under specific conditions. The app I made is extremely simple in functionality; a more complex app would be much harder to modify.

And I’m pretty confident that the coding workflow I shared in this post only worked because I’m a programmer. The LLM makes me much, much faster at building these simple kinds of utilities, but my programming knowledge still feels essential to keeping the process running. I’m writing fairly detailed technical specs, I’m making architectural choices, I’m occasionally directly editing the code or fixing a bug. The app is so small and simple that it’s easy for me to keep up with what’s going on.

I yearn for non-programmers to also experience software this way, as a malleable artifact they can change in the natural course of use. LLMs are clearly a big leap forward on this dimension, but there’s also a lot of work ahead. We’ll need to find ways for LLMs to work with non-programmers to specify intent, to help them understand what’s going on, and to fix things when they go wrong.

I’m optimistic that a combination of better tooling and improved models can get us there, at least for simpler use cases like my translator tool. I guess there’s only one way to find out 🤓 ([Subscribe to my email newsletter](https://buttondown.email/geoffreylitt) if you want to follow along with my research in this area.)

* * *

Recently…[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#recently)
----------------------------------------------------------------------------------------------------------

In the past few months I’ve given a couple talks relevant to the themes in this post.

In April I spoke at [Causal Islands](https://www.causalislands.com/) about [Potluck](https://www.inkandswitch.com/potluck/), a programmable notes prototype I worked on with Max Schoening, Paul Shen, and Paul Sonnentag at Ink & Switch. In my talk I share a bunch of demos from our published essay, but I also show some newer demos of integrating LLMs to help author spreadsheets. (The embed below will jump you right to the LLM demos)

Also: a couple weeks ago, I presented my PhD thesis defense at MIT! I gave a talk called Building Personal Software with Reactive Databases. I talk about what makes spreadsheets great, and show a few projects I’ve worked on that aim to make it easier to build software using techniques from spreadsheets and databases.

* * *

If you’re interested in diving deeper into ways of interacting with LLMs besides chatbots, I strongly recommend the following readings:

*   [Agency plus automation: Designing artificial intelligence into interactive systems](https://idl.cs.washington.edu/files/2019-AgencyPlusAutomation-PNAS.pdf) by Jeffrey Heer
*   [Unpredictable Black Boxes are Terrible Interfaces](https://magrawala.substack.com/p/unpredictable-black-boxes-are-terrible) by Maneesh Agrawala
*   [Direct manipulation vs. interface agents](https://dl.acm.org/doi/10.1145/267505.267514), a 1997 debate between Ben Shneiderman and Pattie Maes

And for a more abstract angle on the example in this post, check out my previous post, [Malleable software in the age of LLMs](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming)!

* * *

Appendix: prompts[](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms#appendix-prompts)
--------------------------------------------------------------------------------------------------------------------------

Here are some of the prompts I used to make the translator app.

First, my general system prompt for UI coding:

> You are a helpful AI coding assistant. Make sure to follow the user’s instructions precisely and to the letter. Always reason aloud about your plans before writing the final code.
> 
> Write code in ReactJS. Keep the whole app in one file. Only write a frontend, no backend.
> 
> If the specification is clear, you can generate code immediately. If there are ambiguities, ask key clarifying questions before proceeding.
> 
> When the user asks you to make edits, suggest minimal edits to the code, don’t regenerate the whole file.

Initial prompt for the texting app:

> I’d like you to make me an app that helps me participate in a text message conversation in Japanese by using an LLM to translate. Here’s the basic idea:
> 
> *   I paste in a transcript of a text message thread into a box
> *   I write the message I want to reply with (in english) into a different box
> *   I click a button
> *   the app shows me a Japanese translation of my message as output; there’s a copy button so i can copy-paste it easily.
> *   the app talks to openai gpt-4 to do the translation. the prompt can be something like “here’s a text thread in japanese: . now translate my new message below to japanese. make it sound natural in the flow of this conversation. don’t translate word for word, translate the general meaning.” use the openai js library, some sample code pasted below.
> *   the user can paste in their openai key in a settings pane, it gets stored in localstorage

One of the iterative edits for the texting app:

> make the following edits and output new code:
> 
> *   write a css file and style the app to look professional and modern.
> *   arrange the text thread in a tall box on the left, and then the new message and translation vertically stacked to the right
> *   give the app a title: Japanese Texting Helper
> *   hide the openai key behind a settings section that gets toggled open/closed at the bottom of the app
