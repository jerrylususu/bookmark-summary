Title: Coding Without a Laptop - Two Weeks with AR Glasses and Linux on Android

URL Source: https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/

Published Time: 2025-05-11T00:00:00.000Z

Markdown Content:
I recently learned something that blew my mind; you can run a full desktop Linux environment on your phone.

Not some clunky virtual machine and not an outright OS replacement like Ubuntu Touch or postmarketOS. Just native arm64 binaries running inside a little chroot container on Android. Check it out:

![Image 1: image1](https://holdtherobot.com/assets/images/image1-fda7b7bad1f1031c2a9b93f312ec17f8.avif)

> i3, picom, polybar, firefox, and htop

That's a graphical environment via X11 with real window management and compositing, Firefox comfortably playing YouTube (including working audio), and a status bar with system stats. It launches in less than a second and feels snappy.

Ignoring the details of getting this to work for the moment, the obvious response is "okay yeah that's neat but like, _why_". And fair enough. It's novel, but surely not useful.

Thing is, I had a 2 week trip coming up where I'd need to work, and I got a little obsessed with the idea that I could somehow leave my laptop at home and _just use my phone_. So what if we add a folding keyboard and some AR glasses?

![Image 2: image2](https://holdtherobot.com/assets/images/image2-33a8991bfbc1b166d479f61b9d3a3b53.avif)

> Here's a CRDT-based ebook/audiobook reader I've been working on, running a desktop Linux app and connected to the Flutter debugger.

What's kind of amazing here is that both the glasses and the keyboard fit comfortably in my pockets. And I'm already carrying the phone, so it's not that much extra.

### The Hardware[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#the-hardware "Direct link to The Hardware")

**Keyboard:** There's plenty of little folding bluetooth keyboards on the market, and I only had to go through 5 of them before I [found one](https://amzn.to/4mnjRYq) that was tolerable. I tried some with trackpads, but they were either too big or the keys were squeezed together to make it fit. The Termux:X11 app that displays the graphical environment is able to function as a trackpad to move a mouse pointer around, and that turned out to be good enough for mouse input. I'm very keyboard-centric anyway, so I'd often go for a while without needing to touch it.

**The Glasses:** Believe it or not, "augmented reality" glasses are kinda good now. The AR part is almost entirely a misnomer; they're just tiny little OLED displays strapped to your face attached to bird bath optics. I was able to get a lightly used pair of [Xreal Air 2 Pros](https://amzn.to/4dtA4HA) off of ebay that would show me a 1080p display with a 46° field of view. Some of the newer ones can do large virtual displays rather than the pinned-to-your-head image that mine have, but I'm pretty skeptical of that setup, at least until the resolution and field of view improve.

**The Phone:** I unfortunately had to upgrade my phone, because to drive the glasses you need to have DisplayPort Alt mode. My very cheap, very crappy old phone did not. The 8 series seems to be the first Pixel phone where Google decided to be marginally less evil and not lock out the DP Alt Mode feature in software (forcing people to buy Chromecasts? IDK), so I bought a used [Pixel 8 Pro](https://amzn.to/3F02fRD) on ebay.

So the whole setup:

*   Used Pixel 8 Pro $350
*   Used Xreal Air 2 Pro - $260
*   Samers Foldable Keyboard $18

Total cost: $636. Although I'm not sure the $350 for the phone should count, because I really did need a new one.

After a few afternoons experimenting, I felt like I could _probably_ function with only this setup for the two weeks. I figured the full commit would keep me from reverting back to a PC when I hit a wall and got frustrated or bored.

### The Result[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#the-result "Direct link to The Result")

So after using this on an airplane, in coffee shops, at various family member's houses, in parks, and even sitting in the car, I think I have some answers for "why would you use this when laptops exist and are excellent".

1.   It really does fit into your pockets. No bag, nothing to carry.
2.   I can use it outdoors in bright sunlight. I wrote most of this blog post sitting at a picnic table in a park. Screen glare and brightness is not an issue.
3.   I can fit into tight spaces. This setup was infinitely more comfortable than a laptop when on a plane. Some coffee shops also have narrow bars that are too small for a laptop, but not for this.
4.   The phone has a cellular connection, so I'm not tied to wifi.

In other words, there's a sense of freedom that you do not get with a laptop. And I can be _outdoors_. One of the things I've grown tired of as software dev is feeling like I'm stuck inside all the time in front of a screen. With this I can walk to a coffee shop and work for an hour or two, then get up and walk to a park for another hour of work. It feels like a breath of fresh air, quite literally.

That said, there were plenty of pain points and nuances to the whole thing. So here's my experience:

### The Linux Environment[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#the-linux-environment "Direct link to The Linux Environment")

Linux-on-Android was _eventually_ great, but I don't want to gloss over the fact that it was a pain in the ass to figure out. My definition of "sufficiently capable" was Neovim + functioning langauge servers (Nim, Python, Dart, JS), Node, and Flutter (compiling to both desktop and web apps that could be run and debugged).

The I won't go though everything line-by-line here (I can though, if anyone is interested), but there's already some great resources out there (linked below). Here's the high level picture, based on my learnings.

There's roughly 4 different approaches to Linux on Android:

1.   A virtual machine emulating x86_64
2.   Termux, which is an Android app that provides a mix of terminal emulator, lightweight Linux userland, and set of packages that are able to run in that environment.
3.   arm64 binaries running in chroot, which is basically just a directory where those programs will run, sealed off from the rest of the filesystem. Notably, it requires the system to be rooted.
4.   proot. Same idea as chroot, but doesn't use the forbidden system calls that chroot needs root for

After way too much time spent experimenting, I landed on the chroot approach. I really didn't want to root the phone, but nothing else did what I needed. The virtual machine was way too slow and clunky, as was proot. Sticking to what can be run inside Termux got me surpisingly far, but Android's C implementation is Bionic and most programs won't run unless they're compiled with that in mind. That, plus other differences in the environment mean you're pretty limited. Chroot has no performance penalty as far as I can tell, and (for the most part), anything that can be compiled for arm64 seemed to work.

As far as distro (I tried many), here's what matters:

1.   Small and light. This is a phone, after all.
2.   Has to support aarch64, obviously.
3.   Doesn't use systemd (I could never make it work inside chroot, and it's unclear if it's possible).
4.   Has some amount of testing or support for running in chroot. Arch Linux ARM, for example, had some odd issues here, like fakeroot not working.
5.   Uses glibc. I thought Alpine was going to be the ticket, but I really needed Flutter/Dart to work, and I couldn't get it working with musl. This might not be a problem for everyone though.

So ultimately, the aarch64 glibc rootfs tarball of Void Linux fit the bill, and it's been running beautifully.

I used i3 (a keyboard-centric tiling window manager), but I tested xfce and that worked fine too.

Some usleful links:

*   [https://github.com/LinuxDroidMaster/Termux-Desktops](https://github.com/LinuxDroidMaster/Termux-Desktops)
*   [https://github.com/termux/termux-x11#using-with-chroot-environment](https://github.com/termux/termux-x11#using-with-chroot-environment)
*   [https://github.com/Magisk-Modules-Alt-Repo/chroot-distro](https://github.com/Magisk-Modules-Alt-Repo/chroot-distro)

### The AR Glasses[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#the-ar-glasses "Direct link to The AR Glasses")

The quality of the image on these things is fantastic. You're seeing bright pixels from a beatiful OLED display. But because each pixel is bounced off the lens, a black pixel just looks clear. So a black terminal background with white text means you're seeing white text floating in space. This is actually pretty cool if you want "less screen, more world around you" kind of feel, but can also be distracting. However, the model I bought has electrochromic dimming, so you can darken the actual "sunglasses" part to block out ambient light. Without this they'd be unuseable in bright sunlight as the image washes out, so I highly recommend getting a pair that has this.

![Image 3: image3](https://holdtherobot.com/assets/images/image3-131628ff6e93155fca11522aab8d04bf.avif)

> It's apparently impossible to get a good through-the-lens photo, but trust me that the image through the glasses is excellent. This is wihout the electrochromic dimming turned on, so text just floats in front of the scenery. You can darken the glasses to the point where you can hardly see through them if you want.

I do feel a little weird wearing these in public, but not _that_ weird. They more or less pass for sunglasses, so the odd part is wearing sunglasses indoors and typing on a keyboard with nothing in front of you. I had couple people ask me about them, but they seemed to just think they were cool. One guy said he was going to buy a pair. That may be selection bias though; I'm sure some people thought I was an idiot.

The biggest downside of the glasses is that the FOV is actually too big. Seeing the top and bottom edges of the screen means moving your eyeballs to angles that are just a little uncomfortable, and it's actually difficult to get the lenses in the right spot so that both are clearly in focus at the same time. I had the window manager add some extra padding at the top and bottom of the screen, and that helped quite a bit.

Worth mentioning: I tried to get multi-display mode working on Android, and it was awful. I ended up using [this app](https://play.google.com/store/apps/details?id=com.tribalfs.pixels&hl=en-US) to change the phone's resolution to 1080p, and then just mirror to the glasses. It turned out to be great, because you can pull the glasses off and just work on the phone whenever you want a break.

The focal plane of the glasses is about 10 feet. Which means if you use readers for a laptop, you probably won't need them.

### The Keyboard[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#the-keyboard "Direct link to The Keyboard")

_Sigh_. Can someone please make a good folding keyboard? This little $18 piece of plastic is decent for what it is, but this was the weakest part of the whole setup, and it feels like it should be the easiest. It feels cheap, is bulkier than it needs to be, doesn't lock when it's open (which means you can't really sit with it in your lap), and there's no firmware based key remapping.

I might continue to play alibaba roulette and see if there's a better one out there. But I would quite literally pay 10 times as much for something good.

### Performance[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#performance "Direct link to Performance")

As a rough benchmark, I tried compiling Nim from source.

*   On my Framework 13 with a Core Ultra 5 125H it took `4:15`.
*   On my Thinkpad T450s with an Intel Core i5-5300U it took `14:20`.
*   On the Pixel 8 Pro it took `11:20`.

I would say qualitatively that's about how it feels to use. Faster than the Thinkpad, but definitely not as fast as the Framework.

BTW I am glad I paid a little extra for the Pixel 8 Pro, because the 12GB of RAM it has vs the 8 of the non-pro model seems worthwhile. RAM usage often gets close to that 12GB ceiling.

### Battery Life[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#battery-life "Direct link to Battery Life")

With the glasses on and the phone screen dimmed, the phone used a little under 3 watts at idle, and 5 to 10 when compiling or doing heavier things. On average I'd drain about 15% battery per hour. So 4 to 5 hours before you need to be thinking about charging, but I'm not sure you'd want to have the glasses on longer than that anyway.

### Am I Going to Keep Using This?[​](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/#am-i-going-to-keep-using-this "Direct link to Am I Going to Keep Using This?")

I'm safely out of the novelty phase at this point, and incredibly, I think the answer is yes. If I had my laptop with me I would never reach for the phone, in the same way that if I'm sitting next to my desktop PC, I'm not going to grab my laptop. But this phone setup can go places that the laptop can't, and that freedom is something I've been wanting for a long time, even if I didn't quite realize it.

I also find it amazing that the whole thing was relatively cheap, especially when compared to something like the Apple Vision Pro. Which, funnily enough, can't do any of what I ended up caring about. It can't fit in your pockets, and it's no more capable of "real" computing than an iPhone. I guess you can use it outdoors, but your eyes are in a sealed box, so I don't think that even counts.

I think there might actually be a future for ultra-mobile software development. Especially as these AR glasses continue to improve and Linux continues to be flexible and awesome. Despite the rough edges, I'm able to go places and do things now that I couldn't do before, and I'm exited about it.
