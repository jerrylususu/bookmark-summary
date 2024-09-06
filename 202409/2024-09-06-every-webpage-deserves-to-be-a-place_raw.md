Title: Every webpage deserves to be a place

URL Source: https://interconnected.org/home/2024/09/05/cursor-party

Markdown Content:
If you’ve visited my actual website, rather than reading by email or whatever, such as reading [this very post](https://interconnected.org/home/2024/09/05/cursor-party), you may notice somebody else’s cursor pass by as you’re reading.

![Image 1](https://interconnected.org/more/2024/09/cursor-party/two-cursors.png)

So that’s a feature I’ve added, part of something called **cursor party.**

I’ve blurred other people’s cursors as if you’re seeing them through frosted glass.

* * *

What’s the smallest thing that can help you realise that other people are here too?

Multiplayer cursors aren’t the most sophisticated way to share presence but they are super effective.

Anyway, here’s something that is a hidden feature: cursor chat.

Hit the / key then start typing, just like Figma.

I like to hang out on my own blog and surprise people by saying hi.

![Image 2](https://interconnected.org/more/2024/09/cursor-party/cursor-chat.png)

Sometimes they ignore me, and sometimes they say whoa and we have a little chat.

You’ll notice three things about that pic:

*   when somebody else speaks, their cursor pops out from the other side of the glass and pops into focus. Their message follows them around
*   a Type / to reply nudge follows _your_ cursor
*   a Quiet Mode toggle appears in the top right.

So there is a _reason_ for Quiet Mode, and is this.

_Mostly_ my blog is pretty quiet. I think of it like one of those always empty tiny galleries with like maximum three paintings that you get in some neighbourhoods (there’s one around the corner from where I live now in Peckham).

And if you’re in there - which is rare - and somebody else happens to step in at the exact same moment - which is _super_ rare - then you’re like, huh, that’s nice, and you feel the cosy glow of co-presence and finish looking at the pictures then wander out again.

But sometimes one of my posts will get so, so popular.

And then it looks like this:

![Image 3](https://interconnected.org/more/2024/09/cursor-party/busy.png)

Only that’s a static screenshot so you have to imagine it with all the cursors flying around and people yelling.

Which is not conducive to easy reading, I admit.

And also, when people encounter this from Hacker News, which is usually the source of all the traffic, makes some people REALLY CROSS.

> I don’t understand what the cursors and highlights are supposed to show us.
> 
> Maybe they could just put in flashing text plus a flashing background plus a microwave attack on the reader.

Lol

Actually that time got really funny…

Because it started with people saying the cursors were distracting them from reading the post.

And then next, check this out, people figured out the cursor chat, and decided that the post was distracting them from chatting to each other.

So they started swapping tips: just use inspector 2 delete article

![Image 4](https://interconnected.org/more/2024/09/cursor-party/takeover.png)

Which is exactly what should happen!!

On the web, you can’t tell when a website is busy until it gives a 500 error and falls over and becomes inaccessible.

But a real world location gets inaccessible because it’s too crowded with people and you simply can’t get through the door.

If your neighbourhood micro gallery was suddenly mobbed with people you’d be like, whoa, what’s going on? You want to know! That’s part of being part of a place! You can always come back later if it’s too busy.

And if that crowd of people get talking and decide to take over the place for their own party – well then that’s exactly what they should do.

So a webpage feeling jostlingly full is an ideal and necessary corollary of having cosy presence.

But yeah, it’s also possibly annoying.

Which is why the Quiet Mode toggle appears when a page starts getting busy or when somebody starts chatting.

* * *

Another cursor party feature is real-time shared text highlighting.

Here it is:

![Image 5](https://interconnected.org/more/2024/09/cursor-party/highlights.png)

I made the original version of this feature back in 2021: [Social Attention: a modest prototype in shared presence](https://interconnected.org/home/2021/03/22/social_attention).

It wasn’t reliable then. Now it is! Thank you new browser APIs.

Shared text highlighting is ephemeral and anonymous. Nothing is tracked on the server. You just sometimes see somebody else highlighting a word or a few as they read down a post. (I do it, you may do it, it’s a common tic.)

* * *

Ok it sounds weird for me to say that I hang out on my own blog and say hi to passers by.

But it shouldn’t sound weird?

Like, why not? Welcome into my front yard!

Sometimes I say hi to people and it turns out we know each other!

Sometimes I get a DM from someone to say that they met another cursor on my site and spent a few minutes dancing around each other.

Sometimes I’ll highlight some text, then somebody else does, then I do back, and so we go moving down the page, from top to bottom.

[It’s a miracle that we can feel togetherness over the internet.](https://interconnected.org/home/2021/09/22/togetherness)

And yet! And yet!

* * *

### Here’s the code

I built the first version of cursor party when I was working with PartyKit last year.

This was the launch post…

[Cursor party! Get multiplayer cursors on your own website](https://blog.partykit.io/posts/cursor-party) (2023):

> Yeah yeah you already know I’m obsessed with multiplayer cursors.
> 
> What if I said you could have them on your own website with just one line of code?

The magic of websockets and a deft framework with perfect abstractions. PartyKit is still my go-to for real-time multiplayer. So simple, so powerful.

Well, PartyKit got acquired by Cloudflare (huge congrats Sunil) and they’re still being developed as a framework but are no longer a client. HOWEVER…

cursor party is open source. So since then I’ve added a few bits.

And you can have it on your own site too haha

Here are the features now:

*   multiplayer cursors
*   cursor chat
*   live shared text highlighting (ephemeral, anonymous)
*   quiet mode
*   works even on static sites by adding a single line of code
*   surprise your homepage visitors by saying hi

There are instructions in the README about how to install it for your own site:

**[Get interconnected-cursor-party here.](https://github.com/genmon/interconnected-cursor-party)**

Yes it is still fairly technical.

If you want this and you’re not technical, or it doesn’t work on your platform, or there’s a multiplayer feature that you’d like that extends this, then drop me a note and we’ll figure something out. I would consider offering a hosted option.

* * *

What I like about multiplayer cursors, cursor chat, and shared highlighting is that it’s like the opposite of a _feature…_

It’s not differentiation. It wouldn’t dilute me if you did it too. (But it shouldn’t be a browser feature, it’s part of the site, it’s me designing the vibe for this particular place.)

It doesn’t stand out. If there’s nobody else on this site you wouldn’t even notice.

It should be everywhere. It’s how the web should be.
