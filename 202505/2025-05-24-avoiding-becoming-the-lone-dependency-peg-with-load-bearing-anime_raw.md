Title: Avoiding becoming the lone dependency peg with load-bearing anime

URL Source: https://xeiaso.net/blog/2025/avoiding-becoming-peg-dependency/

Markdown Content:
Published on 2025-05-23, 702 words, 3 minutes to read

While working on [Anubis](https://anubis.techaro.lol/) (a Web AI Firewall Utility designed to stop rampant scraping from taking out web services), one question in particular keeps coming up:

![Image 1: Aoi is wut](https://stickers.xeiaso.net/sticker/aoi/wut)

[Aoi](https://xeiaso.net/characters#aoi)

Why do you have an anime character in the challenge screen by default?

This is sometimes phrased politely. Other times people commenting on this display a measured lack of common courtesy.

The Anubis character is displayed by default as a way to ensure that I am not the lone unpaid dependency peg holding up a vast majority of the Internet.

[![Image 2: XKCD Comic 2347: Dependency by Randall Munroe](https://files.xeiaso.net/blog/2025/avoiding-becoming-peg-dependency/dependency_small.jpg)](https://files.xeiaso.net/blog/2025/avoiding-becoming-peg-dependency/dependency_small.jpg)

XKCD Comic 2347: Dependency by Randall Munroe

Of course, nothing is stopping you from forking the software to replace the art assets. Instead of doing that, I would rather you [support the project](https://github.com/sponsors/Xe) and purchase a license for the commercial variant of Anubis named [BotStopper](https://gist.within.lgbt/xe/ed3282f1cc064c56bcbb1a74f6a13be2). Doing this will make sure that the project is sustainable and that I don't burn myself out to a crisp in the process of keeping small internet websites open to the public.

At some level, I use the presence of the Anubis mascot as a ["shopping cart test"](https://en.wikipedia.org/wiki/Shopping_cart_theory). If you either pay me for the unbranded version or leave the character intact, I'm going to take any bug reports more seriously. It's a positive sign that you are willing to invest in the project's success and help make sure that people developing vital infrastructure are not neglected.

There's been some online venom and vitriol about the use of a cartoon that people only for about 3 seconds on average that make me wonder if I should have made this code open source in the first place. The anime image is load-bearing. It is there as a social cost. You are free to replace it, but I am also free to make parts of the program rely on the presence of the anime image in order to do more elaborate checks, such as checks that do not rely on JavaScript.

Amusingly, this has caused some issues with the education market because they want a solution NOW and their purchasing process is a very slow and onerous beast. I'm going to figure out a balance eventually, but who knew that the satirical tech startup I made up as a joke would end up having a solid foothold in the education market?

One of best side effects of the character being there is that it's functioned as a bit of a viral marketing campaign for the project. Who knows how many people learned that Anubis is there, functional, and works well enough for people to complain about because of someone getting incensed online about the fact that the software shows a human-authored work of art for a few seconds?

I want this project to be sustainable; and in the wake of rent, food prices, and computer hardware costs continuing to go up I kinda need money because our economy runs on money, not GitHub stars.

I have a no-JS solution that should be ready soon (I've been doing a lot of unpublishable reverse engineering of how browsers work), but I also need to figure out how to obfuscate it so that the scrapers can't just look at the code to fix their scrapers. So far I'm looking at WebAssembly on the server for this. I'll let y'all know more as I have it figured out on my end. There will be some fun things in the near future, including but not limited to [external services to help Anubis make better decisions on when to throw or not throw challenges](https://github.com/TecharoHQ/anubis/pull/533).

Hopefully the NLNet application I made goes through, funding to buy a few months of development time would go a long way. There has been venture capital interest in Anubis, so that's a potential route to go down too.

Thanks for following the development of Anubis! If you want to support the project, please throw me [some bucks on GitHub Sponsors](https://github.com/sponsors/Xe).

* * *

Facts and circumstances may have changed since publication. Please contact me before jumping to conclusions if something seems wrong or unclear.

Tags:

Copyright 2012-2025 Xe Iaso. Any and all opinions listed here are my own and not representative of any of my employers, past, future, and/or present.

Served by xesite v4 (/app/bin/xesite) with site version [fec22e70](https://github.com/Xe/site/commit/fec22e7034970edffd8e0c5c8c34884e2f9536bf) , source code available [here](https://github.com/Xe/site).
