Title: 

URL Source: https://xeiaso.net/talks/2025/opsec-and-you/

Markdown Content:
Opsec and you: how to navigate having things to hide - Xe Iaso
===============           

[Xe](https://xeiaso.net/)

[Blog](https://xeiaso.net/blog/)

[Contact](https://xeiaso.net/contact/)

[Resume](https://xeiaso.net/resume/)

[Talks](https://xeiaso.net/talks/)

[Xecast](https://xeiaso.net/xecast/)

[Signalboost](https://xeiaso.net/signalboost/)

Opsec and you: how to navigate having things to hide
====================================================

Published on 03/13/2025, 6432 words, 24 minutes to read

It feels like privacy has become "impossible", hasn't it? What does it mean to actually be "private" these days? Who are you defending against? What do you want to do in order to mitigate it? And more importantly, how do you do this without giving up the conveniences of modern life?

In this talk, I'll be covering the finer points of operational security (opsec), knowing your threat model, building your own infrastructure to self-host things that are important to you with discarded hardware, and how to "blend in" when traveling or even at home. It's all about balance and figuring out what your needs are. My needs are certainly a lot different than yours are. This is a nuanced topic and I am not going to pretend there isn't any.

Want to watch this in your video player of choice? Take this:  
[https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/index.m3u8](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/index.m3u8)

![Image 1: The title slide with the title 'Opsec and you: how to navigate having something to hide' and speaker information.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/001.jpg)

The title slide with the title 'Opsec and you: how to navigate having something to hide' and speaker information.

Hi, I'm Xe. You probably know me from my blog. Today, I'm gonna give a talk that I really wish I didn't have to give. In a sane or just world, I wouldn't need to have this talk exist; however, we know what world we got and I'm here, so today I'm gonna talk about operational security or opsec.

![Image 2: Opsec in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/002.jpg)

Opsec in rather large text.

Opsec is a somewhat multifaceted topic, but it really boils down to making sure you keep yourself safe online.

It’s really easy to go down the online privacy rabbit hole and way past Narnia. This is fundamentally a game of balancing your authentic expression with how much information you share. Again, it sucks that we have to have this conversation, but I’d really much rather y’all have the tools to protect yourselves.

![Image 3: The agenda slide for the talk.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/004.jpg)

The agenda slide for the talk.

Today, I’m gonna cover the basics of what opsec is, give you practical tips on how to protect yourself online, how to control what you can, be aware of the things you can’t, show you the tools you can use today to keep yourself safe, and give you tips on how you can set up your own online infrastructure so that you can have real privacy online.

![Image 4: About the speaker slide.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/005.jpg)

About the speaker slide.

Before we get into all that though, I’m Xe. I’m the CEO of Techaro, which is a totally real company that actually exists. I’ve written god knows how many articles and I’ve worked at a smattering of companies. Some of them you know, most of them you don’t. I live in Ottawa with my husband and my 6 homelab servers.

![Image 5: 'Opsec 101' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/006.jpg)

'Opsec 101' in rather large text.

So, let’s talk about opsec. Today I’ll start out with what it means. Perfect security is impossible. Any actions you take are compromises. Sure in theory you can just become a hermit and live away from society, but that makes it difficult to do things like attend conference talks or post on social media. Like I said, it’s all about compromises and balance. Unless you're a citizen of Germany, in which case you can actually have real privacy online, asterisk.

Another thing to keep in mind is that it’s a lot easier to be one of the people out there in the audience watching this talk than it is to be me, the person giving it. There are completely different security implications at play. The trick is to figure out the right balance of information you share vs information you don’t share.

![Image 6: 'You're gonna fuck it up' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/011.jpg)

'You're gonna fuck it up' in rather large text.

Also, you’re gonna fuck it up. You will accidentally leak something. You are going to make an error and it will be okay. The other trick with opsec is to balance things out such that when you do inevitably make that error you minimize the consequences. You will fall for a phishing link. The trick is when you inevitably fuck it up, the consequences are minimized as much as possible.

### Threat modeling

The heart of operational security is the threat model. A threat model is the list of things and people you care about and what you are protecting against. This is probably one of the most personal parts of this. Your threat model is going to differ vastly from mine. Here’s an example threat model for a guy I just made up:

![Image 7: An example threat model for Sleve McDichael](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/013.jpg)

An example threat model for Sleve McDichael

Let’s imagine a guy named Sleve McDichael. He’s a straight white dude that posts cooking videos to TikTok. He doesn’t really have any enemies and works as a car mechanic. He’s civilly involved and sometimes posts about US politics. He used to play baseball and probably peaked in high school.

Let’s say the worst thing that could happen to Sleve is that someone gets angry about one of his cooking videos. He doesn’t mention his employer in his cooking videos, maybe he’ll say “oh yeah I’m a car mechanic” at some point, but overall he doesn’t mention where he works. Just to be safe, he let his employer know about the cooking TikTok videos. Their reaction was “oh cool I’ll follow and make the good recipes”. Imagine how simple Sleve’s life is. This is the dream.

Sleve has random internet strangers in scope for his threat model. Random internet strangers aren’t the most predictable, but generally they have limits as to what they can do. Individuals can only really do small scale actions.

The other thing to keep in mind with Sleve’s threat model is that there’s things that are out of scope. Usually most threat models end where the government begins. Sure hope that’s not an ominous thing to say in Anno Dominium Two Thousand And Twenty Five _fake laugh_.

![Image 8: The list of things Sleve can control.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/017.jpg)

The list of things Sleve can control.

In terms of things that can impact his threat model, here’s the low hanging fruit that Sleve can control. He can control what he posts, such as by not mentioning that he works at Jiffy Lube. He can control what social media apps he uses, such as TikTok or Bluesky. He can control when he posts because you can figure out where someone lives by when you post (you usually don’t post while you’re asleep!). He can also control what he shows in any photos or videos he posts.

![Image 9: The list of things Sleve cannot control.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/018.jpg)

The list of things Sleve cannot control.

Now let’s take a look at the things Sleve can’t control. Generally, Sleve can control the things he does, but he can’t control what other people do in response to them. He can’t control what other people do, and he has even less control over what the government does. Sure, he votes, but I vote too.

![Image 10: The list of things Sleve cannot easily control.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/019.jpg)

The list of things Sleve cannot easily control.

There’s also a bunch of things in the middle between things Sleve can and can’t control. In theory he can control his writing style so that people can’t identify him by his “writeprint”, but changing your writeprint (or even being cognizant of it) is difficult for most people. If he’s really worried, he can use an AI tool to rewrite what he posts so that it’ll hide his writeprint. Yes, this is something that works, and every AI model has its own writeprint. Even models that run on your local device are good enough to hide it -- fun fact, the Torment Nexus has a use.

In theory, Sleve also has control of how he speaks (voice training is a thing that does exist), but it’s difficult to control for most people. These are things that he needs to keep in mind as he writes posts or makes cooking videos.

Opsec behaviors
---------------

Despite everything, Sleve still manages to keep himself safe online. In order to keep yourself safe like Sleve does, there’s a few behaviors you can follow and they’re mostly low-hanging fruit:

*   Don’t follow out those viral online quizzes or install apps you don’t need to. Who knows what the publishers of those quizzes or viral apps are doing with your data. Remember [Cambridge Analytica](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal)? That started with online quizzes. Once it's off your device, God knows.
*   Another strategy is to google your name or usernames to see what comes up. Think like an attacker. What can you dig up about yourself from your online footprint?
*   Be aware of phishing. This is statistically the thing that you are inevitably going to fuck up. Attackers only have to be lucky once, you have to be lucky every time. I’ve fallen for phishing before and because I set things up to lessen the consequences, nothing bad happened. I didn’t even lose control of that Discord account that got temporarily yoinked. I even got control back without contacting support.
*   Use HTTPS. Browsers used to be more vocal about using HTTPS, but the s in HTTPS means “secure”. When you connect over HTTPS, it’s encrypted on the wire. Attackers may be able to see what domain names you are visiting, but they won’t see much more than that. Any contents of webpages or the paths you are visiting aren’t visible, even over public insecure wifi. The page you're visiting, the contents, or the paths are secure, even over public Wi-Fi.

![Image 11: Numa is concern](https://stickers.xeiaso.net/sticker/numa/concern)

[Numa](https://xeiaso.net/characters#numa)

![Image 12: What the 'not secure' mark looks like in Chrome, Firefox, and Safari.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/browser-not-secure-comparison.jpg)

What the 'not secure' mark looks like in Chrome, Firefox, and Safari.

Most browsers won’t let you know if the website you’re connected to is over HTTPS. Browsers will want you to assume HTTPS is the default. They will show you a “NOT SECURE” warning when you are not using HTTPS. Look for “Not Secure” in the address bar. If it’s there? Browse away to somewhere else. They probably don't need your traffic.

*   Use multi-factor authentication. It’s free. Passkeys are built into every major OS and are immune to phishing. Use 6 digit two factor authentication codes if you have to, but if you can avoid it never use SMS authentication codes. Your bank may not let you disable SMS authentication though. Your password manager will have support for two-factor auth stuff; I'll get into password managers later.
*   Before you post something, take a moment to think about what you’re about to do. Is it really worth posting? Once you post something, even if you delete it, it’s really hard to un-post it. It’s much easier to just not post it in the first place. I have a thing set up to let me think I’m posting things but it just deletes them. Best thing I’ve set up in a while. One of the things I have set up for myself is a website that looks like Twitter, so I can type things and hit "post", and it just gets sent to /dev/null. It's great, one of the best things I've ever set up.
*   Use full disk encryption on your machines. If you use a Mac, it’s on by default. If you use Windows, look for BitLocker in your settings. If you use Linux, look for LUKS in your distribution’s documentation. Full disk encryption is especially important for laptops because laptops can and will inevitably be left behind at the coffee shop. If the disk is encrypted, the machine is worthless to attackers.

### Nyms

![Image 13: 'Nyms' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/028.jpg)

'Nyms' in rather large text.

One of the things you can do to keep yourself anonymous online is to use pseudonyms, also known as nyms. These are names that don’t match the name on your passport. If you’re part of the furry community, you probably know your best friends by names like Soatok, Cendyne, or Framebuffer instead of whatever their passport names are. Pseudonyms are really easy to adopt and can be a great way to add personality to your online presence.

![Image 14: Xe's GitHub profile.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/029.jpg)

Xe's GitHub profile.

Fun fact: the name I use professionally is a pseudonym! I don’t use my passport name professionally so that I can brand myself better. Xe Iaso is three syllables instead of the longer name that I use on my passport that people constantly misspell and mispronounce. It's also three syllables, and I thought it would be less easy to typo, but I've also had to buy the domain xeLaso.net because someone at Apple decided that the serifs on lowercase L were too ugly.

If you are going to adopt pseudonyms, make sure that you only use two or three separate nyms at once. If you use more than that, you’ll run into the risk of confusing them with each other. If you’re plural, you may be able to get away with more, your mileage may vary, less is more. You’ve probably run into something I’ve published under a pseudonym and never known. Someone you know has published under a pseudonym and you've never known.

If you’re going to use pseudonyms longer term, make sure to make their social media accounts in advance and “age” them. New accounts look more suspicious than older accounts do. Brand new accounts have things that stand out in the UI of most social platforms to make them look fishy, because most phishing comes from brand new accounts. Accounts that recently became active after being idle also look suspicious for super-intense scrutiny, but you can automate posting to prevent a lot of the worst effects. Don’t feel bad about aging your nyms for a few months or even a year.

Pro tip: use AI models to help anonymize your writing. I use obscure locally hosted models to do this so that people can't place why they think the text looks familiar. This is a great way to keep your writing style from being used to identify you.

![Image 15: Aoi is wut](https://stickers.xeiaso.net/sticker/aoi/wut)

[Aoi](https://xeiaso.net/characters#aoi)

Really? Are you sure? That seems a bit unbelievable.

![Image 16: Cadey is aha](https://stickers.xeiaso.net/sticker/cadey/aha)

[Cadey](https://xeiaso.net/characters#cadey)

Yep! The really neat part is that this extends to very small local models too. Here's an example of Apple Intelligence (one of the worst models out there) rewriting the abstract for this talk (you can see it at the top of the page).

![Image 17: Mimi is happy](https://stickers.xeiaso.net/sticker/mimi/happy)

[Mimi](https://xeiaso.net/characters#mimi)

In today’s digital landscape, privacy has become increasingly challenging. This presentation will delve into the intricacies of operational security (opsec), elucidating the concept of true privacy in the modern world. It will explore the identification of potential threats, the establishment of self-hosted infrastructure utilizing discarded hardware, and strategies for blending in during travel or at home. The key takeaway is the importance of striking a balance between privacy and convenience. While the specific requirements may vary, this presentation aims to provide a comprehensive understanding of the nuances involved.

Generated by Apple Intelligence (macOS)

![Image 18: Cadey is enby](https://stickers.xeiaso.net/sticker/cadey/enby)

[Cadey](https://xeiaso.net/characters#cadey)

The really cool part is that this effect works with _every_ single language model on the market. Each of them have their own writeprint, meaning that if you consistently stick to one, you can be theoretically tracked that way. This will be a way to keep your writing style from identifying you in particular, but people can and will track the writing style of the model. Everything's a tradeoff.

### Metadata

![Image 19: 'Metadata' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/032.jpg)

'Metadata' in rather large text.

One of the other big things to think about with regards to opsec is metadata. Metadata is data about data. One of the best examples of metadata is the data attached to photos. Here’s an example with a photo I took on my iPhone:

![Image 20: A picture of a sign in Brooklyn that says 'No standing'.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/033.jpg)

A picture of a sign in Brooklyn that says 'No standing'.

This is a photo I took in New York City in order to communicate how strange the sign was to me. I still think it’s kinda strange, but here’s the metadata that my iPhone attached: It says "no standing," referring to stopped cars.

![Image 21: The same picture with a window to the side showing the photo metadata.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/034.jpg)

The same picture with a window to the side showing the photo metadata.

Wow, that’s a lot of info! It says I used an iPhone 15 Pro Max with the telephoto lens at ISO 50, f/2.8, a shutter speed of 1/125 seconds, and has the exact GPS coordinates the photo was taken at. Let's break this down. The telephoto lens is about 120mm equivalent, has an aperture of f2.8, shutter speed of 1/125 seconds, and has the _exact_ GPS coordinates of where I hit the capture button. This is a shocking amount of metadata at first glance. It makes you wonder, how much information are you really sharing when you upload a picture to the internet?

The good news is that online platforms know about this and take steps to prevent you from doxxing yourself with picture metadata. Most of this data is stored as EXIF data. Modern platforms will scrub this data before sharing any photos users upload. I’ve even seen some mobile phone OSes strip EXIF data when you use the photo picker tool. I've seen some mobile OSes, like CalyxOS and GrapheneOS, strip that at the photo picker level. But your mileage may vary; you may be more or less paranoid.

![Image 22: A screenshot of the GPSDetect extension.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/036.jpg)

A screenshot of the GPSDetect extension.

If you use Firefox, you can install the [GPSDetect](https://addons.mozilla.org/en-US/firefox/addon/gpsdetect/) extension and you’ll get a notification every time someone leaves GPS metadata in their photos. The link to the extension will be in a resource list at the end. Here’s an example of what it looks like in action:

![Image 23: A screenshot of the GPSDetect extension in action. Three notifications showing GPS coordinates of photos.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/037.jpg)

A screenshot of the GPSDetect extension in action. Three notifications showing GPS coordinates of photos.

You’ll get notifications like this every time someone didn’t strip the GPS metadata from their photos. When I encounter these in the wild, I usually send an email to the people that published those photos to help them out. They’re almost always thankful.

Other bit of metadata you may not think about: pictures of the sky can be used to figure out where the photo was taken. This requires more complicated attacks, but try to avoid posting pictures of the sky the same day you are taking them. If they're posted within about five minutes of when you took them, a dedicated attacker can figure out where you are.

Some people vary, but most people have a 24 hour sleep cycle. About 8 hours of the day are going to be spent sleeping. Usually when people are asleep, they aren’t posting. Here’s an example based on my Reddit account:

![Image 24: A screenshot of my active times on Reddit based on public account actions like comments and story posts.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/040.jpg)

A screenshot of my active times on Reddit based on public account actions like comments and story posts.

I live in eastern time. My most active hours on reddit align with the morning and evening eastern time. This is my Reddit account's peak activity time: right after work, and right after I wake up. If you were looking at my Reddit account history, you could probably figure out that I live in eastern time just from the metadata of when I post. This is something to keep in mind.

Tools
-----

![Image 25: 'Tools' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/041.jpg)

'Tools' in rather large text.

Now that we covered metadata, let’s branch into the more practical part of this talk: what tools you should use.

### Browsers

![Image 26: The old Google Chrome and Mozilla Firefox logos.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/042.jpg)

The old Google Chrome and Mozilla Firefox logos.

As far as browsers go: use very common browsers. Pick either Firefox or Chrome. They are very boring browsers, but they’re used by a lot of people. If someone hacks Chrome or Firefox, it’s almost certainly not to hack you in particular. They both suck, but they are used by so many people that nobody is going to attack _you_ in particular via Chrome or Firefox, because there are way more high-value targets like governments and banks. Common browsers also mean that you blend into the crowd and are harder to attack. Common browsers also mean your metadata blends in better and is harder to uniquely identify.

### VPNs

![Image 27: 'VPN' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/043.jpg)

'VPN' in rather large text.

One of the things that you’re gonna want to do is shove all your traffic into a VPN. This is what the YouTubers suggest after all, it sounds like it’s a good idea, and it’s not that expensive, right? It encrypts your IP address, right? It stops the hackers from getting your information! It's what the YouTubers suggest with the NordVPN and ProtonVPN ads, and advertising hasn't lied to you, has it? It's not that expensive, it's like three Starbucks drinks in 2019.

![Image 28: 'VPN' in rather large text with a 'no' symbol over it.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/044.jpg)

'VPN' in rather large text with a 'no' symbol over it.

Don’t.

Don’t use VPN services unless you have a very good reason to. Privacy VPNs are the security snake oil of our day. You should only use a VPN service as your default route if you have a very good reason to, such as to make sure that your very legal Linux ISOs are able to be downloaded without getting love letters.

![Image 29: A screenshot of the HTTPS metadata for the website xeiaso.net.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/045.jpg)

A screenshot of the HTTPS metadata for the website xeiaso.net.

Remember that bit about HTTPS? HTTPS is already encrypted. You don’t need to encrypt it again with a VPN. I mean, you _can_ if you want, but you don't need to.

![Image 30: A screenshot of the Tor browser.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/046.jpg)

A screenshot of the Tor browser.

Use the Tor browser for any browsing that you really want to be private. Tor is free. Tor is used by a lot of people all over the world. It's free, and it's available on your OS of choice.

Remember that ancient meme that went something like “you can’t get me, I’m behind seven proxies”. That’s how Tor works.

![Image 31: A diagram about how onion routing works.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/048.jpg)

A diagram about how onion routing works.

Tor takes your traffic and uses onion routing to send it through a bunch of nodes and then end up getting to the target through an indirect route. This gives you even more privacy advantages than a VPN server does, especially because every website is inevitably going to be using a different circuit. Your computer sends traffic to a node that decrypts it, unwraps it, and sends it along until it reaches an exit node, which sends it to the target. You get the response back, do the whole song and dance, and you get there indirectly, usually through like seven European countries.

![Image 32: A screenshot of the Tor Project website.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/049.jpg)

A screenshot of the Tor Project website.

You can download the Tor browser for free from [torproject.org](https://www.torproject.org/). Again, I’ll have a resource list linked at the end of the talk. The Tor browser is available on every major OS. The Tor Project is getting an aarch64 Linux port soon. The Tor browser is made by experts that care.

The only thing to keep in mind is that you shouldn’t use it all the time, and this is more from a practical angle rather than a theoretical angle. Tor helps keep activists safe and lets people evade government censorship, but there’s also a shocking amount of abusive traffic that comes from Tor exit nodes. Lots of websites block Tor in order to protect themselves. This probably includes your favorite websites. Lots of websites, like Reddit, block Tor to protect themselves.

### Messaging

![Image 33: A screenshot of the Signal website.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/051.jpg)

A screenshot of the Signal website.

If you’re gonna message people, use Signal. Make sure to enable disappearing messages. Disappearing messages mean that everything you send with people gets automatically deleted after a configurable amount of time. I personally use a week for most people I know.

Signal is one of the few encrypted messaging apps that has [Soatok approval](https://soatok.blog/2025/02/18/reviewing-the-cryptography-used-by-signal/).

Of note: when nation state actors attack Signal, they don’t even go after the cryptography. They just attack convenience features like [linked devices](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html). When nation-state actors attack Signal, they don't go after the cryptography; they phish you. That should say a lot about Signal's security.

One of the annoying features of Signal is that it doesn’t sync message scrollback to new devices by default. I think this is a feature and proof that the messages ARE NOT BEING SAVED ON THE SERVER, but this can be an annoyance. I think they're changing this, but I think it's a feature. It's proof that messages are _not_ being saved on the server. It's a balance of trade-offs.

### Password managers

![Image 34: 'Use a password manager' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/055.jpg)

'Use a password manager' in rather large text.

Use a password manager. Your device or browser likely comes with one. That one is free. I personally use 1Password with my husband and it works great for us. It’s effortless and even supports all the two-factor auth that we use. I use 1Password because we used it before a lot of the other options existed. But if you use a Mac, there's a password manager built into your iCloud account. I think Microsoft has a similar thing, but I try to avoid using Windows.

Your password manager has a password generator embedded into it. Use it. You should not know your passwords beyond the root password you use to unlock the password manager. If you only use randomly generated passwords, you can’t reuse passwords. A generated password cannot be reused unless someone has broken randomness, in which case we all have bigger issues. You should not know your passwords beyond the root password. If you only use generated passwords, you _can't_ reuse passwords, and reused passwords are how people get popped.

### Run updates

![Image 35: 'Run updates' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/057.jpg)

'Run updates' in rather large text.

I know that Windows is a giant pain in the ass about updates, but seriously, run them. Updates get released for a reason. Updates patch security issues. If you don’t install updates, you can’t be protected by them. Running updates regularly is one of the easiest ways to make sure that your computers are secure. Seriously, run updates.

Self-hosting
------------

![Image 36: 'Self-hosting' in rather large text.](https://cdn.xeiaso.net/file/christine-static/talks/2025/opsec-and-you/058.jpg)

'Self-hosting' in rather large text.

Finally, you should probably know how to host things yourself. This gives you the most understanding of what platform owners can see about what you do because you become a platform. Self-hosting also can give you absolute superpowers, like being able to have every TV show or movie you want steaming at a moment’s notice without having to follow a flowchart or use dedicated websites to find out where you can watch things. No, seriously, there's a website that has detailed flowcharts for every show now, based on the show, what country you're in, and so on. It's a nightmare. There was a video by videogamedunkey about figuring out where to watch a TV show. He didn't even need to write any comedy, he just described the process of trying to watch, I think it was _Severance_.

If you want to get started with self-hosting, any computer will do really. You can get used desktops off of Craigslist, your local university’s surplus store, or at Woot.com. When you’re starting out, you probably don’t really have elaborate hardware needs, but anything that can turn on and run Linux is fine. You probably just need something that can turn on.

As for what to run on it, all the normal options suck equally at this point. The important part is to pick whatever you’re the most comfortable with learning about. Ubuntu and Rocky are the closest to what you’d use in production if you were to become a career systems administrator or site reliability expert. But really by this point everything is the same brand of suckitude in different ways. Some are more up to date than others, others prioritize unchanging stability, the important part is to Just Pick Something™️. Some suck more than others. Some are more out of date than others, and consider that a feature.

Once you have the OS, set up something like [k3s](https://k3s.io/) or Docker Compose. Then you can install whatever self hosted apps you want. Here’s a whirlwind tour of the self hosted apps that I use on a regular basis: Yes, I know Kubernetes seems like a lot, but that's where the entire industry is going, because Kubernetes has sucked out all of the oxygen for everything else.

*   [Plex](https://www.plex.tv/) is self-hosted Netflix that points to a folder full of media. I use it to watch anime and catch up on old movies.
*   If you want to only run open source software, there’s also [Jellyfin](https://jellyfin.org/). I personally don’t use it because I bought a lifetime Plex pass a while ago, but when Plex inevitably kills off the lifetime Plex pass I’m gonna set up Jellyfin. I don't use it because Plex was dumb enough to sell me a lifetime Plex pass for like $20. When Plex inevitably kills that off, I'm probably going to set up Jellyfin.
*   [Nextcloud](https://nextcloud.com/) is like google docs, google calendar, an email client, google drive, and Slack all in one. It can do anything from instant messaging to meetings to integrations with self-hosted AI models. I’ve been meaning to use it more, but I mostly use it for 