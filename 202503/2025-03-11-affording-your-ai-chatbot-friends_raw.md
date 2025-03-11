Title: Affording your AI chatbot friends

URL Source: https://xeiaso.net/talks/2025/ai-chatbot-friends/

Markdown Content:
Published on 03/10/2025, 5250 words, 20 minutes to read

Servers are expensive. Servers with GPUs are even more expensive. AI agents rely on servers with GPUs. If you don’t have control over what is happening at different parts of the stack, then things can change out from under you and your AI agent can change drastically without warning. Read: your AI chatbot friend can get massively depressed out of nowhere!

In this talk, I’ll cover all of the parts involved in a production-grade AI agent workload and how and where you can and should get control of them. This will cover the overall stack you’ll end up using, model management and the risks of models changing, cost-time tradeoffs and how to make educated decisions about them, as well as stories of my misadventures when things went wrong. You will leave this talk with practical strategies for maintaining control over their AI agent’s behavior and for controlling costs.

![Image 1: The title slide with the talk and speaker name.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/001.jpg)

The title slide with the talk and speaker name.

Hi, I’m Xe. Today I’m gonna talk with you about the wonders of AI agents and how you can run them with whatever model you want without breaking the bank.

![Image 2: An anime depiction of an absolutely incensed anime businessman pointing at a whiteboard labeled 'We need AI'.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/002.jpg)

An anime depiction of an absolutely incensed anime businessman pointing at a whiteboard labeled 'We need AI'.

Imagine this is you. You wake up one day and go to a meeting. Your boss is there absolutely insisting that your product needs to have AI. What does that mean? Well let’s assume it’s something sensible, but now the mandate has come in from above and you’re the one that actually goes to implement it.

You’re probably asking yourself questions like this:

*   What are the moving parts with AI?
*   When should I buy vs build?
*   What infrastructure can I use?
*   How can I run this without spending a lot of money?
*   What is an AI agent?

![Image 3: A slide explaining AI agents with a robotic blue tiger working on a car with a bunch of tools.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/004.jpg)

A slide explaining AI agents with a robotic blue tiger working on a car with a bunch of tools.

Thankfully that last question is the easiest to answer. An “AI Agent” is just a model with access to tools like “escalate ticket”, “run SQL query”, or “draw an image”. The rest of the hype comes from fitting it into existing workloads like ETL nonsense with MuleSoft or something banal like that. This is really what all the hype is about: hooking AI models up to existing infrastructure so that they can do “useful things”.

The moving parts of AI
----------------------

So, if an agent is just a model with access to tools, how do you make that happen? Let’s look over the moving parts of AI. To keep things simple, I’m going to break this into four parts.

1.  **Models**: The first part is the model. A model is a bunch of floating-point numbers that were trained on unimaginable sums of text. These models take input embeddings and use them to generate new tokens that just so happen to be words. There’s hundreds of models out there, but if you’re in doubt you should try Facebook’s Llama series of models, DeepSeek V3, or maybe one of OpenAI’s models. They’re usually good enough to start with.
2.  **The inference engine**: Next we have the inference engine. This is the thing that runs the model. There’s a few options on the market for inference engines, but usually you’ll use Ollama, llama.cpp, or vllm with an OpenAI API client. This is the part that needs the GPU to run. When you pay OpenAI for a model, they host the model and inference engine for you.
3.  **Your code**: Now we get to your code. Your code is going to be the thing that sits in the middle, wrapping your frontend around the AI model and doing whatever square peg round hole transformations you need. This is the part that’s the most diverse and opinionated, so I’m not going to cover it that much here.
4.  **The user interface**: Finally, there’s the user interface. This is the chat box that pops up when a user clicks on the sparkle emoji button, the tool that summarizes the meeting transcript for action items, or whatever your CEO wanted.

![Image 4: A slide showing all of those moving parts of AI agents.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/010.jpg)

A slide showing all of those moving parts of AI agents.

And that’s it really, the AI models get run by the inference engine. Your code calls the inference engine and then presents the results to the user interface. It’s basically the same as a database in the standard three tier webapp architecture.

### The stereotypical example app

![Image 5: A slide showing a diagram of the stereotypical example app.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/011.jpg)

A slide showing a diagram of the stereotypical example app.

When you get started, you’ll almost certainly see a setup like this. The example code will almost certainly call OpenAI’s API, pass input and context there, maybe spin in a loop to handle tool calls depending on how it’s set up, It’ll have a chat UI like the ChatGPT UI and you pay per million tokens of output.

Let’s be real for a second. This will absolutely work for a vast majority of usecases, especially where confidentiality doesn’t matter. OpenAI’s SRE team is one of the best in the market. It’s super easy to set up, all you need is a corporate card and an API key. It works on any laptop or server with an internet connection. It’s easy to think about, and easy to compartmentalize. You get access to some of the best models in the market and it works out pretty well.

Depending on what model you choose, the needs of your product, and how much people use the AI features, you can easily get away with paying a few thousand dollars per month on the extreme edge. The best results come from making sure that you balance output quality with cost, which is more of an art than a science.

![Image 6: 'The problems of doing this' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/015.jpg)

'The problems of doing this' in rather large text.

However, roses have thorns, and there’s some pretty insidious ones that may make you think otherwise for this:

The biggest problem is actually one of the biggest advantages: you’re relying on OpenAI to keep the model up. This means you don’t need to purchase GPUs or worry about uptime (let’s face it, OpenAI being down means that more than just you is down and there’s a huge GDP impact), but you’re relying on them to keep your product functional. This is a huge position of power for OpenAI. They’re selling their products at a loss so people will adopt them, and some day the financial cows will come home along with massive price hikes.

OpenAI and other providers can and will deprecate that one model that your production workloads depend on. Sure you can just change over to another model, but sometimes that can have massive consequences on your app. One time I switched a model over in one of my chatbots and she went from a happy bubbly little thing to showing symptoms of a full blown depressive episode. That was just from changing one variable in the code. Imagine how much your app’s behavior could change if the entire model was changed out but you thought you were fine because you asked for GPT-4o in your code.

And then that deprecation warning inevitably gets ignored (because let’s face it, who actually reads the deprecation warning emails these days), then suddenly it’s your emergency and you get to start learning about hyperparameters or having to tell your boss “sorry, it’s out of our hands”.

Do you really want to give the keys to the kingdom to someone else?

### Self-host all the things

So then you’re inevitably temped to want to self host all the things! After all, if your code is calling your server, deprecations are on your schedule, right? This is a nice idea and sounds really good to the ear. Let’s take a look at what the stack looks like:

![Image 7: A diagram of what that example looks like with a self-hosted setup.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/017.jpg)

A diagram of what that example looks like with a self-hosted setup.

This looks basically the same, but it’s slightly different.

Instead of asking OpenAI’s API, you ask your own pool of GPU servers to run the model with the question and context. The API endpoint in the inference server translates your requests into tokens, the GPU mangles the tokens a bit according to the model weights and then returns a de-token-ified response to the user.

The other main difference is that there’s a model storage server in the equation because let’s face it, you’re going to have more models around than your GPU servers have space for them. In practice you’ll probably end up storing your models in object storage like Tigris and then cache them to the inference servers so they load fast.

Otherwise, your app shouldn’t really notice or care that there’s another model in the equation. The behavior will be different, sure, but you can pretty easily correct for that in your prompt and code.

![Image 8: 'The upsides of doing this' in rather large text with the list of the upsides to the left.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/021.jpg)

'The upsides of doing this' in rather large text with the list of the upsides to the left.

This is a lot more complicated than relying on a third party, but this strategy has significant upsides that can make up for it in some circumstances.

The biggest advantage is the most obvious one. When you’re calling models on your servers, you own the stack. You get to choose what models are available. You get to choose when a model becomes deprecated. You get to mix and match models at will.

When you use a provider like OpenAI, you’re limited to the models that OpenAI has available. The OpenAI models are usually good enough, but what if you want to finetune a model for your exact usecase or experiment with models that are using things that OpenAI just doesn’t support? What if you need to see the reasoning output in your reasoning flows? OpenAI doesn’t let you do that, but self hosted models do.

Finally, the last big advantage of using a self hosting workflow is that you don’t send data to a random third party. OpenAI doesn’t see or filter what you do. This can make self-hosting more than worth it in some cases, such as using AI models to analyze trends in medical records. Nobody is going to even imagine allowing you to pipe all that data to OpenAI, no matter what acronyms OpenAI is compliant with.

![Image 9: An edit of 'the myth of consensual sex' meme but with AI and OpenAI over Jesus.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/022.jpg)

An edit of 'the myth of consensual sex' meme but with AI and OpenAI over Jesus.

What if your app touches LGBTQ issues, menstruation schedules, or something else that the current political zeitgeist will label wrongthink? OpenAI could just turn off answering questions like “I don’t feel like my body is right, is there something I can do to fix it?” and then you’d be totally out of luck. Your self-hosted models would be totally unaffected.

![Image 10: 'The problems of doing this' in rather large text with a list of the problems to the right side.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/026.jpg)

'The problems of doing this' in rather large text with a list of the problems to the right side.

Of course, doing this isn’t free puppies, rainbows, and the like. There’s some significant downsides in self hosting your AI workflows and they can be subtle and insidious.

The nvidia drivers will become the bane of your existence. They’re normally stable, but they can and will fall over without notice. Always at 3am. Never during work hours, because why would they? You’ll have to deal with the nvidia drivers that you have no introspection into deciding that uptime is for cowards. You can make up for this with a worker pool and redundancy, but that makes your projects expensive. It’s a tradeoff.

Another downside is that you have to choose what models you use for your products. There’s so many options out there that it can be paralyzing. Like I said earlier, the Facebook Llama models are a good place to start, but you have to know enough about what you want out of the AI models to know which model is right for you. This is a skill you can learn, but it sucks having to learn it in anger.

There’s a few inference engine options like Ollama, llama.cpp, and vllm, but you’ll find out that they all suck in different, mutually incompatible ways. Eventually you’ll end up having opinions about which runtime is right for you, but again you have to spend the time to have those opinions.

![Image 11: An anime depiction of an absolutely incensed salaryman pointing at a whiteboard with unreadable text and kira-kira emoji.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/027.jpg)

An anime depiction of an absolutely incensed salaryman pointing at a whiteboard with unreadable text and kira-kira emoji.

This is time that you really don’t have when your boss is breathing down your neck wanting to show the investors a sparkle emoji button. However, there’s one huge downside that isn’t as easy to work around.

Nvidia GPUs are essential to your setup. Sure you can hurt yourself trying another provider and everyone has to learn somehow, but realistically you’re going to use nvidia GPUs because that is the path of least resistance.

The only problem is that the lead time for buying them is measured in months. And when you do get them, they’re stupidly expensive. We’re talking somewhere on the order of 40,000 per card. You can only buy them in packs of 8 with servers that cost $200,000 in total. Not to mention the power they need and the datacenter technician time to handle the inevitable hardware failure.

![Image 12: A line of startup workers in front of a whiteboard labeled 'Kidney donations for AI servers'.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/029.jpg)

A line of startup workers in front of a whiteboard labeled 'Kidney donations for AI servers'.

Sure you can get the cards you need off of ebay, taobao, alibaba, or that one shady guy on craigslist. But sooner or later your employees are going to run out of spare kidneys and you’ll run out of budget for the pizza parties to make up for all the kidney donations.

Even more fun: when you do get those GPUs, they only have a service life of 1-3 years. This means you have to do the whole rigamarole again! I’m kind of amazed that any companies are able to put up with this, but that’s the real cost of AI.

I don’t really know if it’s worth it. I did the self hosting flow for my chatbot in my homelab and it did work, but nvidia seems dead set on starving consumer GPUs for video memory, meaning that as I wanted to experiment with bigger and better models, I had to start branching out into the cloud.

Nomadic compute
---------------

![Image 13: Noah from Xenoblade Chronicles 3 standing between a fork in the path with each side labeled 'Hosted APIs' and 'Self-Hosting'.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/032.jpg)

Noah from Xenoblade Chronicles 3 standing between a fork in the path with each side labeled 'Hosted APIs' and 'Self-Hosting'.

There’s gotta be some middle path between these two extremes, right? Both of these sides have just so much suffering in different ways.

![Image 14: N from Xenoblade Chronicles 3 walking down a middle path labeled 'Nomadic Compute'.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/033.jpg)

N from Xenoblade Chronicles 3 walking down a middle path labeled 'Nomadic Compute'.

There is a way forward: Nomadic compute. Nomadic compute means cheating, but knowing exactly how and when you should cheat. It all revolves around taking advantage of your user patterns and the fundamental constants of the infrastructure we’re all working on top of. In a nomadic compute setup, your runtime hunts down deals between providers around your well-defined workloads, spinning up more of them when you need more and slaying off the excess when you have too many.

The biggest key to how nomadic compute works is by taking advantage of one fundamental constant between every provider: they all have nvidia GPUs. Any nvidia GPU is fungible for another one.

![Image 15: 'Everyone has GPUs' in the middle of a smattering of cloud provider logos for platforms with GPU support.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/035.jpg)

'Everyone has GPUs' in the middle of a smattering of cloud provider logos for platforms with GPU support.

Not to mention, every cloud provider and their mom has GPUs these days. I’ve even seen single person VPS companies have GPUs available. GPUs are absolutely everywhere and because there’s so much competition, you can almost always get a really good deal.

![Image 16: Title: 'The only specs that matter'](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/036.jpg)

Title: 'The only specs that matter'

To make this even more convenient from a nomadic compute setup: there’s only three specifications you care about when running AI workloads:

1.  The model year of the GPU
2.  The amount of vram it has
3.  The amount of memory bandwidth it has

More model year number? More fast. More vram amount? You can use bigger models More memory bandwidth? The model can respond faster.

These are fundamentally the only specs that really matter.

You don’t always need the newest possible cards either! Most of my AI workloads use the Nvidia A100, which is now three generations out of date but still way more than sufficient for my needs. They also get cheaper over time, so I pay even less for fundamentally the same experience!

![Image 17: A green-haired anime woman in cyberpunk Seattle starbucks desperately trying to hack with a laptop and getting angry. The coffee isn't helping.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/037.jpg)

A green-haired anime woman in cyberpunk Seattle starbucks desperately trying to hack with a laptop and getting angry. The coffee isn't helping.

But then if you try to switch between providers and handle all the corner cases of their APIs and runtimes, you end up like this. Overcaffenated hacking late nights trying to cram yet another square peg into an uncooperative round hole. Luckily though, it’s the future and we have Skypilot:

![Image 18: A screenshot of the SkyPilot website.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/038.jpg)

A screenshot of the SkyPilot website.

[SkyPilot](https://docs.skypilot.co/en/latest/docs/index.html) lets you specify what hardware you need, the providers it can pick between, and what you want the job to do. It’ll figure out what to spin up for you and just make it work.

Load it with API keys for every provider you can, set the requirements wide, and it’ll just figure it all out. You can even have it autoscale workers based on HTTP request pressure, meaning that you can just sit back and let your app go viral because the infrastructure layer will just figure it out for you.

### Fundamentals

![Image 19: The fundamentals of nomadic compute, detailed list on the side.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/042.jpg)

The fundamentals of nomadic compute, detailed list on the side.

When you’re making nomadic compute work for you, keep these ideas in mind:

Build on top of boring tools. Sure you may want to use that fancy database that one provider offers, but don’t. Pick super boring and battle-tested tools like Postgres. Use Tigris or S3 instead of the filesystem. Make your application function anywhere that has an internet connection and an nvidia GPU. You can run WireGuard in userspace, take advantage of this!

In your three tier webapp diagrams, put your AI infrastructure in the same tier as databases. Your AI service is an ancillary support service. Make it act like one. A database is just an internal facing server with a weird API, right? Your AI services should be the same.

Finally, scale down your AI services when nobody is using them. Why should you have to pay for compute time that sits there doing nothing useful?

Cold starts can suck, but if you really cheat by putting the model weights into the docker image for the service, you can shunt a lot of the cold start cost to before you’re paying for the compute time. If your app allows you to, you can even go as far as making all of your AI workloads happen en masse in batch processing instead of spinning up and down workers on demand!

Take advantage of the product design and how people use it to your advantage. Autoscaling is love. Autoscaling is life.

Mimi, the chatbot
-----------------

![Image 20: A slide introducing the chatbot Mimi.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/043.jpg)

A slide introducing the chatbot Mimi.

As an example, let’s take a look at my chatbot Mimi. Mimi is one of the characters in the xe iaso dot net cinematic universe and when I made her into a chatbot I wanted to make something to amuse people and help them laugh. Like any good AI project, Mimi is actually pretty complicated under the hood:

![Image 21: A diagram of Mimi's architecture.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/044.jpg)

A diagram of Mimi's architecture.

Mimi gets chat messages from Discord and then if she’s interested in them passes them to the GPU over Glaceon. Glaceon connects to Fly where the copy of Ollama I use for inference lives. It sends API requests over and gets API responses back so that the bot can decide what to do next.

If the AI wants to draw an image, it sends a request to Falin and Falin sends it over to fal. Falin makes a copy of the image in Tigris and then sends that URL back to the bot, which posts it to Discord.

Mimi remembers things long term with pgvector. Rather, she should, but she’s kinda bad at remembering things right now. Maybe I’ll fix that eventually.

![Image 22: A self-host all the things meme with Mimi placed over the stick figure](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/045.jpg)

A self-host all the things meme with Mimi placed over the stick figure

When I started out, I genuinely wanted to self host all the things so that I could have Mimi be one of the only AI chatbots I know that did it. I wanted to run everything on computers that I could look at, but reality soon got in the way.

![Image 23: A diagram of Mimi's old architecture.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/046.jpg)

A diagram of Mimi's old architecture.

Mimi used to run across three nodes in my homelab: logos, ontos, and pneuma. Logos ran Ollama, and that’s what generated Mimi’s responses. When Mimi wanted to draw an image, she sent a request to ComfyUI on Ontos. ComfyUI generated the image from Mimi’s prompt, uploaded the image to Tigris, and spat back a URL that Mimi used to upload the image to Discord. It worked really well, but then a new model came out:

Facebook released Llama 3 with a 70 billion parameter version. The benchmarks said it was good. My testing on my MacBook said it was really good. I wanted to use it with Mimi, but there was a small problem: it was too big to fit on the GPU in Logos. It was actually bigger than any individual machine in my homelab. This is when I had to compromise, and this compromise is actually what inspired me to make the idea of nomadic compute in the first place.

![Image 24: It's okay to use the cloud, just make sure you have an exit strategy](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/048.jpg)

It's okay to use the cloud, just make sure you have an exit strategy

I put the part of Mimi that generates AI responses into the cloud. I reach out to it over a private network and it scales down when it’s not in use. Should I need to, I can move Mimi’s models and inference engine around again. It’d be inconvenient, sure, but it would be only a mild annoyance instead of a showstopper. GPUs are fungible, and as long as you have easy access to them in the cloud, it’s more than okay to ship parts of your AI apps out.

The image drawing tool had a similar set of compromises. Originally I was using Stable Diffusion 1.5. That model works really well (and sometimes can actually generate better images than newer models), but it’s kinda cumbersome to use and Mimi’s tool use was giving ComfyUI prompts that had biblically accurate results. To spare your sanity, I’m not going to show you the worst, but trust me when I say that it could end up really badly.

Then Flux came out and it could actually handle the prompts that Mimi was using. Again, Flux was too big for my GPUs. It’s only 12 billion parameters, but even with quantization it barely fit on my gaming tower’s GPU. I wanted to use that gaming GPU for…well gaming, and GPUs are super expensive where I live in Canada. Then I found out about fal:

[Fal](https://fal.ai/) could just run Flux for me and I’d pay for the output per image. With the exact model I picked for Mimi, it’s three tenths of a penny per image. That’s less than I’d pay in power to run the model locally. It just made sense to pick fal for my needs. Worst case, I could figure out a way to run the model elsewhere thanks to nomadic compute.

![Image 25: The same diagram of Mimi's architecture.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/044.jpg)

The same diagram of Mimi's architecture.

And as a result, Mimi’s infrastructure looks something like this. Everything that can scale down to zero does. I’d get Mimi to scale down when she’s not in use, but she needs to stay connected to Discord and IRC. It’s pretty nice in practice, I end up paying about $5 a month on Mimi and for what’s going on under the hood I think that’s pretty darn neat.

Lessons I've learned running AI workloads
-----------------------------------------

Before we finish this out, lemme cover some of the biggest lessons I’ve learned running AI workloads that will save you time and money as you implement the sparkle emoji for your boss.

### Every input matters

Every input to the AI model matters. Even small changes to prompts or user inputs can drastically alter the outputs and behavior of your product.

![Image 26: A diagram showing input pointing to the XKCD comic about machine learning pointing to output.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/055.jpg)

A diagram showing input pointing to the XKCD comic about machine learning pointing to output.

Generally when you think about AI systems, it’s easy to think about it like this. You take in the prompt, send it to a pile of linear algebra or whatever that mangles the language the right way and then you get an output. Usually this is the case. Usually.

Not always though! Sometimes there’s hidden inputs that seem pretty banal, such as the date and time of the user making the requests. This can have any number of strange effects from Claude getting lazier around August when Europe goes on holiday to ChatGPT getting noticeably worse output in December when Americans ritualistically give up for the year.

If your app doesn’t need a given bit of input, don’t supply it. This will make your models way more deterministic.

Most platforms and inference engines also let you set the seed value that the model uses to randomly select tokens or for seeding the diffusion space. Pick either a set seed for everyone (such as 3407) or a set seed per user. This will make your model way more predictable in practice.

### Set the temperature as low as you can

One of the other main parameters to AI models is the temperature. This controls how random the output is. Higher temperatures can cause more amusing results, but higher temperatures can also cause the model to become wildly unpredictable and go off the rails. Set the temperature as low as you can.

| Task | Temperature |
| --- | --- |
| Amusement chatbot | 1 |
| Summarization of meeting transcript | 0 |
| Analysis of financial documents | 0.25 or 0.5 |

If you need things to be strictly factual for data entry, summarization, or other cases where the details matter, set the temperature as low as zero. Otherwise, you can set the temperature to whatever feels right with testing.

My chatbot Mimi uses a temperature of 1 because nobody is going to be negatively affected if she’s wrong. I’m pointing this out because some runtimes like Ollama set the temperature to 1 by default, which can have implications for using it in more complicated flows.

### Use filter models

As we all know, user input is difficult to trust. What if your user asks your AI product how to make a pipe bomb? You don’t want your AI product telling people how to do that, that could get you in trouble. Thankfully, Facebook, Google, and other companies have created filter models.

![Image 27: A diagram showing a filter model in the middle of the AI model and the user input.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/062.jpg)

A diagram showing a filter model in the middle of the AI model and the user input.

A filter model is something that sits in the middle of your AI model. If user input passes the filter, it goes to the model. If it fails, the user gets a reason why it failed.

The output of the model is also passed to the filter to make sure that the user didn’t manage to smuggle an input that makes the model generate an unsafe reply. This can help you make sure that user inputs are passing muster as well as making sure that your AI model doesn’t advocate for horrible things under your nose.

The two most popular filter models are Llama guard from Facebook and ShieldGemma from Google. Both of them come in a few different sizes, but something of note is that filter models are almost always smaller than general purpose models.

These models won’t be able to write poetry, tell you how to make a pie, or the recipe for pancakes. They are finetuned specifically to make sure that input and output meets quality standards. Finetuned models for a specific task can always be smaller than general purpose models. You can even get access to hosted copies of these models via services like OpenRouter.

![Image 28: A screenshot of Mimi thinking some random innocuous Discord message was election interference.](https://cdn.xeiaso.net/file/christine-static/talks/2025/ai-chatbot-friends/064.jpg)

A screenshot of Mimi thinking some random innocuous Discord message was election interference.

These models have gotten a lot better than they used to be. One of the funniest ways Llama guard backfired on me was that one day that Mimi decided that everything was election interference. Advances in language models have really made this better, I’d love to see what a reasoning filter model would act like in practice.

Conclusion
----------

In conclusion, AI stuff isn’t scary or expensive. The devil is in the details of how you balance the complexity around.

*   Tools like Skypilot and philosophies like nomadic compute can absolutely help you make sure that your workloads are sustainable. OpenAI can’t deprecate the models that you host yourself.
*   Host what you’re the most comfortable with. Buy the things you’re less comfortable with. This will mean that you’re going to spread your workloads between clouds, but it will mean that you’re less beholden to any individual platform in particular. If one platform tries to jack up the prices, others certainly will welcome you with open arms.
*   Cheat when you can. Take advantage of user behavior. You don’t need to pay for idle workloads, so spin them down when they’re not in use.
*   If you can’t self host a model because it’s too big for your local hardware, make sure that you can self host it at all. This means that you have an ex