Title: MCP: An (Accidentally) Universal Plugin System

URL Source: https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin

Published Time: 2025-06-28T14:09:30+00:00

Markdown Content:
There's this thing about USB-C that nobody really talks about. Not the part where we all had to buy new dongles (RIP my dongle drawer, 2010-2023). The other part.

See, we all thought USB-C was just going to be about charging things and moving files around like the other USBs. Very serious. Very purposeful. But because of the way it is it can do... other things.

[![Image 1](https://substackcdn.com/image/fetch/$s_!kwfs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01350f9f-9ecd-4cb2-a28d-103a9ccc9027_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!kwfs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01350f9f-9ecd-4cb2-a28d-103a9ccc9027_1024x1024.png)

My friend Rex connected his toaster to his monitor last week. I don't know why. The toaster doesn't know why. But it _worked_, and now Rex's toast has HDMI output.

Remember car cigarette lighters? Nobody uses them for cigarettes anymore. They're just universal power outlets that happen to be shaped like something from 1952. Your car doesn't care if you're charging a phone or running a personal pizza oven. The hole is the same size. The power is there.

_The protocol doesn't judge your life choices._

This brings me to something I discovered about MCP (Model Context Protocol) while trying to make my calendar app order takeout. Stay with me here.

Everyone thinks MCP is for making AI assistants smarter. You know, "Claude, please read my files and understand my soul." And sure, it does that. But here's what they put in the documentation that made me spit out my morning tea:

> "MCP provides a standardized way to connect AI models to different data sources and tools."

Okay but. _But_. What if you just... removed the AI part?

What if it's just "a standardized way to connect ~~AI models~~**literally anything** to different data sources and tools"?

[![Image 2](https://substackcdn.com/image/fetch/$s_!MBI9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca785d13-391f-42fa-8109-7ae384ec5e99_1836x1203.png)](https://substackcdn.com/image/fetch/$s_!MBI9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca785d13-391f-42fa-8109-7ae384ec5e99_1836x1203.png)

Or remember when someone looked at NFTs—which were supposed to just _point_ at images—and thought "what if the pointer... WAS the image?"

[![Image 3](https://substackcdn.com/image/fetch/$s_!C2qU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77d811eb-b5b3-44be-9a9d-e88ba57c7b38_3072x1002.png)](https://substackcdn.com/image/fetch/$s_!C2qU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77d811eb-b5b3-44be-9a9d-e88ba57c7b38_3072x1002.png)

For those of you who don’t get the idea, copy and paste this into your url bar: data:application/json;base64,eyJuYW1lIjogIkJhZyAjNzQ4IiwgImRlc2NyaXB0aW9uIjogIkxvb3QgaXMgcmFuZG9taXplZCBhZHZlbnR1cmVyIGdlYXIgZ2VuZXJhdGVkIGFuZCBzdG9yZWQgb24gY2hhaW4uIFN0YXRzLCBpbWFnZXMsIGFuZCBvdGhlciBmdW5jdGlvbmFsaXR5IGFyZSBpbnRlbnRpb25hbGx5IG9taXR0ZWQgZm9yIG90aGVycyB0byBpbnRlcnByZXQuIEZlZWwgZnJlZSB0byB1c2UgTG9vdCBpbiBhbnkgd2F5IHlvdSB3YW50LiIsICJpbWFnZSI6ICJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUI0Yld4dWN6MGlhSFIwY0RvdkwzZDNkeTUzTXk1dmNtY3ZNakF3TUM5emRtY2lJSEJ5WlhObGNuWmxRWE53WldOMFVtRjBhVzg5SW5oTmFXNVpUV2x1SUcxbFpYUWlJSFpwWlhkQ2IzZzlJakFnTUNBek5UQWdNelV3SWo0OGMzUjViR1UrTG1KaGMyVWdleUJtYVd4c09pQjNhR2wwWlRzZ1ptOXVkQzFtWVcxcGJIazZJSE5sY21sbU95Qm1iMjUwTFhOcGVtVTZJREUwY0hnN0lIMDhMM04wZVd4bFBqeHlaV04wSUhkcFpIUm9QU0l4TURBbElpQm9aV2xuYUhROUlqRXdNQ1VpSUdacGJHdzlJbUpzWVdOcklpQXZQangwWlhoMElIZzlJakV3SWlCNVBTSXlNQ0lnWTJ4aGMzTTlJbUpoYzJVaVBsTm9iM0owSUZOM2IzSmtQQzkwWlhoMFBqeDBaWGgwSUhnOUlqRXdJaUI1UFNJME1DSWdZMnhoYzNNOUltSmhjMlVpUGtScGRtbHVaU0JTYjJKbElHOW1JSFJvWlNCR2IzZzhMM1JsZUhRK1BIUmxlSFFnZUQwaU1UQWlJSGs5SWpZd0lpQmpiR0Z6Y3owaVltRnpaU0krU0c5dlpEd3ZkR1Y0ZEQ0OGRHVjRkQ0I0UFNJeE1DSWdlVDBpT0RBaUlHTnNZWE56UFNKaVlYTmxJajVRYkdGMFpXUWdRbVZzZER3dmRHVjRkRDQ4ZEdWNGRDQjRQU0l4TUNJZ2VUMGlNVEF3SWlCamJHRnpjejBpWW1GelpTSStSR2wyYVc1bElGTnNhWEJ3WlhKelBDOTBaWGgwUGp4MFpYaDBJSGc5SWpFd0lpQjVQU0l4TWpBaUlHTnNZWE56UFNKaVlYTmxJajVEYUdGcGJpQkhiRzkyWlhNOEwzUmxlSFErUEhSbGVIUWdlRDBpTVRBaUlIazlJakUwTUNJZ1kyeGhjM005SW1KaGMyVWlQazVsWTJ0c1lXTmxQQzkwWlhoMFBqeDBaWGgwSUhnOUlqRXdJaUI1UFNJeE5qQWlJR05zWVhOelBTSmlZWE5sSWo1VWFYUmhibWwxYlNCU2FXNW5QQzkwWlhoMFBqd3ZjM1puUGc9PSJ9

The protocol meant for storing references became a protocol for storing reality. It's like using a library card as the actual book.

Here's where it gets even better. The more MCP servers people build for AI, the more capabilities _every_ app can have. It's like:

1.   Someone builds an MCP server for their AI to access Spotify

2.   Your workout app can now generate playlists

3.   You didn't write any Spotify code

4.   The Spotify MCP developer doesn't know your app exists

5.   Everyone wins?

It's like a potluck where everyone brings their specialty dish, but instead of food, it's functionality. And instead of eating, you're... actually, this metaphor is falling apart. But you get it.

[![Image 4](https://substackcdn.com/image/fetch/$s_!Laga!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fea5180-6f0c-4642-8a2f-9c2f6ab5e6ab_1980x1539.png)](https://substackcdn.com/image/fetch/$s_!Laga!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fea5180-6f0c-4642-8a2f-9c2f6ab5e6ab_1980x1539.png)

The beautiful chaos is that every MCP server built for Claude or ChatGPT or whatever becomes a free plugin for _anything_ that speaks MCP. It's accidentally creating a universal plugin ecosystem. Nobody planned this (I don’t think). It's just happening.

They keep saying MCP is like USB-C for AI. But what does that actually mean?

USB-C isn't special because it's a port. It's special because it's a _possibility space_. It's a hole that says "put something here and we'll figure it out." Power? Sure. Data? Why not. Video? Apparently yes. Toaster control protocols? Rex says absolutely.

MCP is the same thing but for functionality. It's not saying "I'm for AI." It's saying "I'm a well-designed hole. Put something here."

So we’re building this thing called **APM** ([Actions Per Minute](https://actionsperminute.io/)). On paper, it's a task management app. In reality? It's a shape-shifter that becomes whatever you plug into it.

The entire plugin system? Just MCP servers.

Want spell check? MCP server.

Want it to order coffee when you complete 10 tasks? MCP server.

Want your AI agents to respond like peons from Warcraft 3 when you assign them a task? Of course you do, and that MCP server is already written and ready to use.

[![Image 5](https://substackcdn.com/image/fetch/$s_!cfIp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3871464-0023-4b56-8235-fad217a9a232_3045x3018.png)](https://substackcdn.com/image/fetch/$s_!cfIp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3871464-0023-4b56-8235-fad217a9a232_3045x3018.png)

Every great protocol gets used for something its creators never imagined:

*   HTTP was for academic papers. Now it runs civilization.

*   Bluetooth was for hands-free calling. Now it unlocks your front door.

*   USB was for keyboards and mice. Now it charges your emotional support portable fan.

MCP thinks it's for giving context to AI models.

But really? It's just a really good protocol for making things talk to other things.

And in a world where Rex's toast has HDMI output, maybe that's exactly what we need.

---

**P.S.** If you build an MCP server that makes your computer emit the smell of fresh bread, we need to talk.

**P.P.S.** We’ve just opened up early access for APM. Build something weird. Build something useful. Build something that makes us question our life choices. I believe in you.

_(Somewhere, a protocol is being used exactly as intended. This is deeply suspicious.)_
