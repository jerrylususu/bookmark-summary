Title: Why Decentralised Applications Don’t Work

URL Source: https://ingrids.space/posts/why-distributed-systems-dont-work/

Markdown Content:
Why Decentralised Applications Don’t Work | Ingrid's Space

1.   [My history with decentralised applications](https://ingrids.space/posts/why-distributed-systems-dont-work/#my-history-with-decentralised-applications)
2.   [Case studies](https://ingrids.space/posts/why-distributed-systems-dont-work/#case-studies)
    1.   [Blockchain](https://ingrids.space/posts/why-distributed-systems-dont-work/#blockchain)
    2.   [The web](https://ingrids.space/posts/why-distributed-systems-dont-work/#the-web)
    3.   [Email](https://ingrids.space/posts/why-distributed-systems-dont-work/#email)
    4.   [IRC/XMPP/Matrix](https://ingrids.space/posts/why-distributed-systems-dont-work/#ircxmppmatrix)
    5.   [RSS/Atom](https://ingrids.space/posts/why-distributed-systems-dont-work/#rssatom)
    6.   [Git](https://ingrids.space/posts/why-distributed-systems-dont-work/#git)
    7.   [BitTorrent](https://ingrids.space/posts/why-distributed-systems-dont-work/#bittorrent)

3.   [Why?](https://ingrids.space/posts/why-distributed-systems-dont-work/#why)
4.   [That was depressing… What now?](https://ingrids.space/posts/why-distributed-systems-dont-work/#that-was-depressing-what-now)

**TL;DR: Misaligned profit motives.**

This has been on my mind for a while, and with a couple of things lately stoking my ire (the NFT resurgence, and Signal integrating MobileCoin), I’ve finally pushed myself to put it into words.

Before I get started, I want to make one thing clear: although I’m starting from a perspective of cryptocurrency and use some associated language, this post is not about cryptocurrency. The scope is much larger, crypto just provides a nice stepping off point since it’s a poignant and timely example.

To clarify what I mean by decentralised: applications whose main purpose is fulfilled as part of a network, where that network is not reliant on any preordained nodes. Decentralised applications are also known as “federated”. There is also a more specific term “distributed”, also known as “peer to peer”. I won’t cover the distinction with the more specific terms because it’s not relevant here. I use the word application in a looser sense, to also cover protocols and specifications.

A practical example of a decentralised application would be email, in contrast to Slack. Although email has some rather dominant nodes (I’m looking at you, Google), I can send an email with my own custom mail client, an email address at my own domain, and a mail server I host myself, to a friend with a similar setup. No Google involved. With Slack, I must use the proprietary Slack client, signed into a Slack account, through Slack’s servers.

### My history with decentralised applications

I was still a child when the original Bitcoin paper[1](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:1) was released. I remember growing up starry-eyed, immersed in the fantastical ideas floating around in its wake. I also grew up with BitTorrent, email, and the web.

Shortly after leaving university, I took a job at a “fintech” (financial technology) company, for a blockchain based project. I was young, we all make mistakes.

Nowadays, I’m a prolific user of git, I use Matrix for some of my messaging needs, email for others, this blog makes use of the decentralised web, I follow several dozen RSS feeds (and publish one here), and of course, I still use BitTorrent.

### Case studies

Before I get to the underlying reasons of why these systems do not work, I want to justify that assertion with some examples. If you get bored, feel free to skip this section.

#### Blockchain

Bitcoin launched with the stated goal of providing an alternative financial system,[2](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:2) and other blockchain projects followed with all manner of lavish promises. Bitcoin failed at the stated goal (unless you count the dark net markets). It has instead defaulted to pyramid scheme, with the added externality of wasting a stupefying amount of energy.

As for the rest of the projects, all I can find is an endless pile of “get rich quick” schemes. It’s sad that I now see the word “blockchain” and immediately begin looking for the scam that’s inevitably there. Signal’s MobileCoin partnership is the latest betrayal here, and the one that hurts the most.

Since I’ve worked in “blockchain”, I’ve got to see this happen firsthand. It’s a common story. You get given a problem spec. You design a decentralised system to solve it neatly. You get told “This doesn’t work, `$COMPANY` doesn’t have any way to monetise it”. You go back to the drawing board, and design a centralised system. You get told, “Hey, this is good and all, but it doesn’t have blockchain”. Eventually you end up with the worst of both: a centralised system wrapping a phony pretense of blockchain. All of the energy waste, and none of the decentralisation.

#### The web

It feels a little strange to count the decentralised web as a failure, given that I’m out here publishing a blog post on my own domain and server. The decentralised web does still work, but I feel it’s important to acknowledge that this isn’t how most people use the web. It is in many ways impractical, and even in the best case it has some glaring flaws.

For starters, setting up your own website like this one is not a trivial task unless you’re already inclined to it like I was. Wrangling with domain registration, DNS configuration, hosting, building the actual damn site, and deployment, that is **a lot**. It’s even worse if yours isn’t a simple static site like this one. Not to mention that for much of the world’s population, the costs of hosting and domain registration are prohibitive. Furthermore, once you’ve got all that working, how do you let anyone else know about it? RSS and aggregators like lobste.rs and Hacker News work for little tech blogs, they don’t work for everyone else.

And so it is that most of us are trapped in an abusive relationship with platforms like Medium, Twitter, and Instagram.

All of the above hasn’t even touched on the fact that there’s a near monopoly on client side web rendering.

Chrome and its derivatives hold an overwhelming majority of the browser market share,[3](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:3) and thus, Google gets to decide how the web works. There’s a pretense of deference shown to standards organisations, but at the end of the day when Google decides on a standard, everyone else must implement it or die. Almost all the front-end web developers I know develop for Chrome. Compatibility with other browsers is an afterthought, if they’re even considered at all.

Bringing fresh competition against Chrome isn’t really an option either. Modern browser rendering engines are so complex (especially when you have to implement all of Chrome’s undocumented quirks too), that even Microsoft gave up trying. And if you’re thinking of making your own system that eschews the web standards, good luck trying to bootstrap the entire web’s worth of content.

#### Email

I used email as my flagship example above because I think it’s the most familiar and clear among these, but I made it sound a lot better than the reality. While hosting your own email is still possible, anyone capable enough to get that far is probably going to realise how bad an idea it is.

My statement that email can be used without involving Google is technically true, but anyone they blacklist will quickly realise that they’re largely locked out of the global email network. Not to mention that, in the same way Chrome’s market share gives Google de-facto control over web standards, Gmail’s gives them control over email standards.

#### IRC/XMPP/Matrix

IRC has been there since time immemorial, and we’ve seen modern takes on it come and go. Yet, the only people I know using IRC and Matrix are programmers and censorship victims.

Proprietary centralised services like Slack, Discord, WhatsApp, etc. dominate, most likely because they have the marketing budget for it. Open systems call for interoperability, but the centralised services are disincentivised to partake, because their lock-in allows them to abuse their users.

Some of the people behind Matrix seem to be of the belief that getting venture capital involved in their own system is the solution here,[4](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:4) I’m not convinced.

Google gets to be a villain here too; RSS has truly been done dirty. From its heyday in the blogging bubble powered by Google AdWords, to its vicious murder with the discontinuation of Google Reader, Google was at the centre. Now there’s talk of it’s use in a Chrome integration? We’ll see what comes of that.

RSS has, however, had unprecedented (and somewhat invisible) success in the form of podcasts. That too is in grave danger though, with Spotify sinking an absurd quantity of money into trying to make its closed system of not-actually-podcasts dominant. Even Apple, whose good stewardship has long been key to keeping podcasts open, has been making dubious moves. A recent update to the iTunes podcast directory made RSS feeds default to private, and their new “podcast subscription” system is not compatible with open podcasting.

#### Git

Git itself is largely ok; It seems that having programmers as the target demographic works out. Even here though, we see signs of corruption.

Git was originally intended to be used in conjunction with email to coordinate development. Many still use it this way. For most users, however, GitHub has entirely replaced email.

It’s one thing for git hosting to be quite centralised, that doesn’t afford the host much power over its users. If a host starts to play foul, one can simply

```
git remote set-url origin <repo url @ new host>
```

and take all the relevant data with them. Even providing a nice UI to wrap the email workflow is alright in my view, emailing patches isn’t for everyone.

What GitHub does though, is rather more sinister. They tweak the actual development workflow away from email with features like pull requests, and and they lock project data in with features like their issue system. When these changes are combined with GitHub’s marketing, they become dangerous. Almost all the university students and new grads I meet don’t know the difference between git and GitHub, and to them, there is no method of collaborative development other than pull-requests.

The network effects discussed with the web apply here too. I have a GitHub profile, because I know no-one will look at my code if I don’t.

#### BitTorrent

Like crypto, the only real use BitTorrent has ended up with has been outside the law. The only people I know using it for anything other than copyright evasion[5](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:5) are Linux distributions sharing their ISOs.

Copyright holders have made BitTorrent so synonymous with piracy, that even non-pirate use is regarded scornfully.

And honestly, it’s sad. Whenever someone wants to send me a file, they either link me to some awful proprietary service like Dropbox, or we fumble about with email. In another timeline, they could just send me a magnet link.

### Why?

At this point, even if you didn’t read the TL;DR, I bet you’ve spotted the trend. In every case there’s someone who stands to make a large profit (or avoid losing their large profit) from ensuring decentralised systems fail.

### That was depressing… What now?

Whenever this topic comes up, I’m used to seeing other programmers declare that the solution is simply to make something _better_.[6](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:6) I understand where this thought comes from; when you have a hammer, everything looks like a nail, and it’s comforting to think that your primary skill and passion is exactly what the problem needs. Making better tools doesn’t do anything about the backwards profit motive though, and besides, have you tried using any of the centralised alternatives lately? They’re all terrible. Quality of tools really isn’t what we’re losing on.

No, the solution has to be **political**. That’s uncomfortable for me, as it probably is for you too. Software I can do, politics though? That’s hard. Something needs to change about these profit motives though. I’m not arrogant enough to declare that I know the one true answer here, I doubt there even is one true answer. I can share some ideas though.

The current system of profit motives, one might call it a market, was designed to optimise the process of extracting, refining, and transforming physical resources. It seems to be pretty good at that, though one may question whether its externalities are worth it, or whether that goal should be the top priority.

What we’re dealing with here is far removed from physical resources, however, and the system has not been adapted at all. Although some like to idealise the aforementioned market as a free and unregulated system, the truth is that it optimises rather poorly under those circumstances, and needs heavy regulation to align profit motives in the direction of efficient processing and distribution of resources. _If_ we are to keep these profit motives at all,[7](https://ingrids.space/posts/why-distributed-systems-dont-work/#fn:7) we need new regulation to align them toward creating software that better serves our society.

* * *

1.   This reads a little differently over a decade later: [https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:1)

2.   Given its deflationary nature and the huge hoard of bitcoin controlled by Satoshi, one might be forgiven for suspecting this wasn’t the true motive, or at wasn’t least the only motive. If those suspicions are true though, there’s some satisfaction in knowing that Satoshi probably can’t get away with using/selling those coins, as there’s a now huge target painted on their back.[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:2)

3.   The next largest competitor is Firefox, whose development is entirely dependent on financial support from Google.[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:3)

4.   [https://www.matrix.org/blog/2019/10/10/new-vector-raises-8-5-m-to-accelerate-matrix-riot-modular](https://www.matrix.org/blog/2019/10/10/new-vector-raises-8-5-m-to-accelerate-matrix-riot-modular)[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:4)

5.   I’ll leave my views on copyright for another time[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:5)

6.   This post by Drew Devault is a good example. No shade intended, I otherwise largely agree with him: [https://drewdevault.com/2021/04/07/The-next-chat-app.html](https://drewdevault.com/2021/04/07/The-next-chat-app.html)[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:6)

7.   I’m not convinced we should[↩︎](https://ingrids.space/posts/why-distributed-systems-dont-work/#fnref:7)
