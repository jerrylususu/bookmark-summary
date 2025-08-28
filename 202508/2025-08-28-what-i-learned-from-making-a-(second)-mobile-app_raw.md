Title: What I learned from making a (second) mobile app

URL Source: https://pjonori.blog/posts/what-i-learned-making-a-second-mobile-app/

Markdown Content:
Every now and then I get an odd tendency to just go off and make something. It’s why I made [a typeface](https://pjonori.design/work/olivia-sans/). It’s why I made [a mobile music app](https://apps.apple.com/us/app/it-plays-music/id6475738719). And it’s why I made another mobile app, [It Makes Noise](https://apps.apple.com/us/app/it-makes-noise/id6749282237).

![Image 1: Screenshots of It Makes Noise](https://pjonori.blog/posts/what-i-learned-making-a-second-mobile-app/it-makes-noise.png#noshadow)_Yup, that’s what I made._

It Makes Noise is a mobile app that (you guessed it) makes noise. I wanted something to block out background sounds. Nothing on the market really did it for me–so I did it for myself.

I learn a lot through these projects. That’s primarily why I do them. It seems like it’d be worth outlining what those things were. Keep in mind, these are my experiences. No more, no less. I make no guarantees about their value for anyone other than me.

AI continues to be a real mixed bag
-----------------------------------

Yeah, I used AI to make my app. I tried to use it with my first mobile app, with little success. This time worked _better_, mainly due to better tooling. But to say it was effective would be a wholesale lie. This is solely based on my experience. I’ve used AI with some success on other projects. All those projects were significantly smaller than this one.

I thought it’d be interesting to get a first-hand take on vibe coding. I decided to throw caution and reason to the wind. I let an LLM build out the codebase with my involvement limited to prompts.

I will never, _ever_ do that again.

The appeal of AI to so many is how fast something real is made. That was exactly how this project played out. I had an app that would compile and function the way I had in my head (more or less). Mind you, it took some wild turns, but there was _something_ resembling an app in a short amount of time. I should have stopped there.

But I didn’t. I decided to just ride this out to the bitter end. And it was in fact bitter. The initial app was _fine_. But as I tried to shift functionality, fix bugs and iterate on features, the joy ride broke down.

![Image 2: A graph charting my productivity with AI-driven development over time](https://pjonori.blog/posts/what-i-learned-making-a-second-mobile-app/productivity-over-time.png)_A hyper-precise graph that charts my productivity with AI-driven development over time._

The innate problem with AI is that it can feel magical at first. So much in such a short amount of time. But that spike in productivity begins to slide over time. And in my experience, it eventually descends into madness. Do you enjoy tracking down a bug in tens of thousands lines of code that _you didn’t write?_ If so, you’re in for a treat.

The codebase got so convoluted and irrational that I had to step in and break the party up. The app required a full re-architecture that culminated in roughly 50% of the code removed.

Now, many are likely saying, “That’s not how you’re supposed to use AI.” To which I _very clearly_ understand. But like it or not, many people, especially designers, are attempting to use AI how I did. I’ve long held this approach to software development to be problematic, if not dangerous. But who am I to judge without having direct experience?

Now I do have experience. I hold this approach to software development to be problematic, if not dangerous.

AI can be like arrogance and overconfidence in a bottle. It can give people the perception that they can do things with no direct skill/experience. And that’s the problem. They have no skill/experience in the given subject. They have no way to judge the quality of what’s generated.

I know enough to know what I don’t know. That’s valuable in and of itself. I understand where I’m safe to tread and what I need to leave be. This experiment was enough to reaffirm I’d rather take the time to know what I’m making.

I’d still use AI though
-----------------------

I will never vibe code anything of even moderate complexity again. I tried it, despite my apprehensions. If anything, it was worse than I imagined.

But, there remains value. I use it for two different scenarios:

1.   Stub out a tightly scoped and narrowly defined set of functionality
2.   Help me with something I have no idea how to even start

Searching for answers to technical challenges can also be a mixed bag. Sometimes I don’t even know the terminology needed to seek out the answer. Also, the internet kind of sucks now. Even if the answer is out there, I have to fight with ads, SEO-riddled gobbledygook and paywalls.

AI has been a better solution in certain cases. To say otherwise would be disingenuous. I don’t plan to abandon AI. But I prefer to have it solve a problem outside of the main codebase. That can take two routes:

1.   Creating separate, self-contained demos to reverse-engineer
2.   Provide code recommendations that I manually copy into my code (or not)

I’ve found those approaches quite useful. But that is a very different reality than the promise of, “Hey AI, make me an app.”

Doing something creates respect for the people who do it well
-------------------------------------------------------------

This project also reaffirmed the value in doing something outside your own wheelhouse. And by doing, I mean _actually doing it_. Not sitting in the passenger seat pretending to drive. Really driving. That first-hand experience gives a new appreciation for those who are actually good at it.

That’s probably the thing that worries me the most about AI. I’m concerned it’ll erode our appreciation for the people who have put in the work. I see this harming society’s collective expertise in countless subjects. Not to mention how it devalues the very people who could counteract the harm.

From my view, that’s the insipid cost of vibe _whatevering_. It’s the ultimate means to an end. I’ll go to the grave believing the slog towards the end is what’s truly valuable. The things I’ve done have made me who I am. I have a comically meandering career. And, yes, it took a while, but those various off ramps I’ve taken have rounded out my thinking. I wouldn’t change anything. I pity those who will lose out at the chance to learn things the hard way.

All those meanderings helped me to pull the atrocity-of-a-codebase back into something usable. Your run of the mill designer won’t have the experience to do that. There are a lot of designers who are about to vibe code into in comedic humiliation.

It’s important to give a project time to breathe
------------------------------------------------

This app started a long, long way from where it ended. I’ll admit that the current version of the app came together pretty damned quickly. But that came after sitting with a janky-ass prototype for large amount of time. It was _barely good enough_ for just me. But it was good enough to clear things up.

I made something to scratch a personal itch. And it kind of worked. Barely. That time sitting in my metaphorical stink gave me a much better idea of what I actually wanted. I paused for a large amount of time to gain a much larger amount of clarity.

Yes, there were still plenty of minor course corrections once I restarted work. But they were minor. Sitting, stopping and evaluating saved a ton of design and development time.

In truth, that’s painting a rosier picture than what really happened. Many dumb ideas don’t start off dumb. They become dumb because context shifts around them. This app started off as a tool to procedurally generate binaural beats and white noise. The app at that time let you select your frequency and phase shift to create custom recipes. At some point, the app shifted to be simpler. But the underlying functionality did not.

I ended up with a frankenstein codebase. The app was juggling multiple audio controllers for different audio types. I didn’t take a moment to re-evaluate the situation. Instead I kept building on top of a shaky foundation to feed progress addiction. At some point it dawned on me that I could just use audio files for _everything_. I should have come to that conclusion _much sooner_. And I would have. If I would have stopped to think for a damned minute.

I still don’t understand iOS development
----------------------------------------

To be more specific, I don’t understand SwiftUI–not _really_. It still feels magical at times. Things seem to _happen_ and I don’t fully grasp why. I’ll admit there are many lines of code in the app that work for reasons beyond me.

That’s _obviously_ bad.

I can still make things work, but I know they’re not elegant. That bothers me, but I’ll live. I know enough to build something that more or less reflects what’s in my head. What has really been driven home is that anyone can make a native mobile app. Mind you, not _any_ mobile app. But, _something_ is possible assuming they’re willing to do the work and keep it simple/pragmatic.

I find building native apps equally exciting and maddening. I makes it clear how much my home is building for the web.

My favorite design tool (continues to be) the code editor
---------------------------------------------------------

I used Figma (or any other drawing tool) precisely zero times to design this app. Yes, I used it to create the App Icon–you got me. All other design iterations happened through code.

I’m one of the weird ones that’s considered the text editor to be their primary design tool for the past 20 years or so. That opinion was held with less conviction even 5 years ago. Now it’s cemented. I’ve come to actively avoid using traditional design tools. This project was one of my biggest projects that was made entirely from a text editor.

Now, I can’t say I enjoyed the editors used for this project, but that’s another story altogether…

I now directly understand why software is where it is.
------------------------------------------------------

It’s hilariously uncompetitive to charge for an app. This is the kind of thing you “know”, but don’t _really know_ until you experience it first-hand. Which sucks–and explains a lot.

Selling an app–for real, upfront money–is an uphill battle. I’m not arrogant enough to assume that’s the primary reason why my apps aren’t flying off the digital shelves. But it’s hard to ignore that $2.99 is infinitely more expensive than free. And, look I get it. Why pay for something that could very likely suck. Especially when there are hundreds of free options available. There’s no reason to believe my app is worth paying for, or even better than the free alternatives. It’s a leap most aren’t willing to take.

It’s not a coincidence that the overwhelming majority of apps made available are free. But they aren’t–which readers of this blog likely know. A lot of people in the world prefer to live under the belief that there’s such a thing as a free lunch. And perpetuating that belief to extract money is _really fucking complicated_. A lot of the software that we use on a daily basis is pretty simple. It’s the business angle that adds complexity.

It takes a certain kind of genius to develop the mainstream platforms we see today. But it’s resulted in a lot of unhappiness. When all the bullshit is set aside–when an app can just be an app instead of a service–things get simpler. Simple enough that a dumbass like yours truly can actually make something. Twice.

I’d rather be a good dumbass than an evil genius.