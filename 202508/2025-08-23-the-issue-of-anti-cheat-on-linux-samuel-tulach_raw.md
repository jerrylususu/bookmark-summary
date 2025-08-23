Title: The issue of anti-cheat on Linux | Samuel Tulach

URL Source: https://tulach.cc/the-issue-of-anti-cheat-on-linux/

Markdown Content:
The number of people choosing Linux as their primary operating system to play games has been slowly but steadily going up, at least [according to the Steam hardware survey](https://www.gamingonlinux.com/2024/06/linux-user-share-on-steam-breaks-2pc-thanks-to-steam-deck/). This is most likely because of the [Steam Deck release](https://store.steampowered.com/steamdeck) and the [increasingly obnoxious features being added to Windows](https://www.theverge.com/2024/9/2/24233992/microsoft-recall-windows-11-uninstall-feature-bug).

If you switch to Linux today, you’ll probably be surprised by how many games run out of the box just fine (mostly due to the [Windows compatibility layer Proton](https://github.com/ValveSoftware/Proton) built right into Steam), _except_ for basically all competitive multiplayer games that utilize any sort of anti-cheat technology.

Just to name a few, here is a [list sorted by concurrent player count from ProtonDB](https://www.protondb.com/explore?sort=playerCount):

*   [PUBG: BATTLEGROUNDS](https://www.protondb.com/app/578080) - uses a combination of [BattlEye](https://www.battleye.com/) and in-house AC, won’t launch at all.
*   [Call of Duty](https://www.protondb.com/app/1938090) - uses RICOCHET AC, won’t launch at all.
*   [Rust](https://www.protondb.com/app/252490) - uses [Easy Anti-Cheat](https://www.easy.ac/en-US), will launch, but you won’t be able to connect to any EAC-protected server (so basically any server except self-hosted ones).
*   [Tom Clancy’s Rainbow Six Siege](https://www.protondb.com/app/359550) - uses [BattlEye](https://www.battleye.com/), won’t launch at all.
*   [EA SPORTS FC 24](https://www.protondb.com/app/2195250) - uses [EAAC](https://help.ea.com/en/help/pc/ea-anticheat/), won’t launch at all.
*   [Destiny 2](https://www.protondb.com/app/1085660) - uses [BattlEye](https://www.battleye.com/), won’t launch at all.

Those are just games on Steam. Then there’s also [Valorant](https://playvalorant.com/en-gb/) and [League of Legends](https://www.leagueoflegends.com/cs-cz/), which both now use [Vanguard](https://support-valorant.riotgames.com/hc/en-us/articles/360046160933-What-is-Vanguard), so they also won’t launch at all. While you can play [Counter-Strike 2](https://www.counter-strike.net/cs2) on [VAC-secured](https://help.steampowered.com/en/faqs/view/571A-97DA-70E9-FF74) servers natively on Linux, anyone trying to play more seriously will likely be playing on [FACEIT](https://www.faceit.com/en) or [ESEA](https://play.esea.net/), which both also won’t work.

Now I can finally get to the point of the article… _Why am I writing this?_ As someone who uses Linux daily, I would love to see these games support it, but I just don’t see that happening any time soon. Many people in the Linux community are frustrated by the fact that these anti-cheat solutions are stopping them from playing their favorite games. It also doesn’t help that some are [fear-mongering about kernel-level anti-cheat solutions](https://youtu.be/_dOCtaBObg4?si=bxrl7H5Xl6FBafH5) and [spreading misinformation](https://www.reddit.com/r/riotgames/comments/1cjq63h/vanguard_real_is/).

In this article, I want to give you a high-level overview of how modern anti-cheat solutions work (which will hopefully be understandable even for non-technical people) and then explain why anti-cheat solutions in their current state just cannot work on Linux, as well as what the alternatives are.

[](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#the-basics) The basics
-----------------------------------------------------------------------------

_What is a videogame cheat?_ We could talk for hours about whether all sorts of macros and exploits should be considered cheats, but the main thing that comes to people’s minds when talking about multiplayer games is an external program that somehow manipulates the game or reads information from the game to provide you with an advantage over others. A prime example of this would be a [wallhack or aimbot](https://en.wikipedia.org/wiki/Cheating_in_online_games#Wallhacking).

There are generally two ways you can go about this:

1.   (**External**) Have a completely separate process that copies memory between itself and the game.
2.   (**Internal**) Force the game to load a [DLL file](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/dynamic-link-library) (a [shared library file](https://en.wikipedia.org/wiki/Dynamic-link_library) containing code) directly into the game, executing custom code from within the game.

Unless you find some very niche way to load a DLL into the game, in both cases you will need the ability to read (and write) the game’s process memory.

[](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#little-detour) Little detour
-----------------------------------------------------------------------------------

If you are not a programmer (or [you are a JavaScript developer](https://www.youtube.com/watch?v=dQw4w9WgXcQ)), you most likely don’t really know how memory management works on modern systems. Let’s imagine this situation: two programs are loaded in memory. What is stopping one program from directly accessing the memory of the other program?

![Image 1: screenshot](https://tulach.cc/assets/img/posts/9_address_space.png)

_Virtual address space in Windows ([source](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/virtual-address-spaces))._

While in the past it would have been perfectly possible to read (almost) any of the physical memory installed in the computer, nowadays OSes use [virtual address spaces](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/virtual-address-spaces). I don’t want to go into the details of how this is handled, but all you need to know is that each program is isolated in its own address space and cannot access other programs’ memory unless it uses functions provided by the operating system itself, like [`ReadProcessMemory`](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-readprocessmemory) and [`WriteProcessMemory`](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory).

In order to use those two functions, you will need to open a [handle](https://learn.microsoft.com/en-us/windows/win32/sysinfo/handles-and-objects) to the process you want to read or write memory from. This handle will be specific to your process and represent the access rights that you have relative to the object it represents (in this case, the game process). Remember this for later, as it will be important.

Modern anti-cheat solutions have three main goals:

1.   Block other processes from accessing the game’s memory whenever possible.
2.   Detect and ban anyone who tries to get around the blocking mentioned above.
3.   Once someone is banned, ensure that they cannot simply create a new game account and continue playing (HWID bans).

This is usually achieved by multiple components working together. Let’s take a look at [Easy Anti-Cheat](https://www.easy.ac/en-US) as an example:

*   Loader (usually `Game_EAC.exe` or `start_protected_game.exe`)
*   Game library (`EasyAntiCheat_x64.dll` and “invisible” module)
*   Service (`EasyAntiCheat.exe`)
*   Kernel-mode driver (`EasyAntiCheat.sys`)

Without a kernel-mode driver, there is no way to _effectively_ block memory access into the game. With the kernel-mode driver, though, it’s incredibly simple. All that the driver needs to do is [register a callback for handle creation](https://github.com/Microsoft/Windows-driver-samples/blob/main/general/obcallback/driver/callback.c), filter out requests to open such handles to the game process, check the requested permissions, and if they allow memory access, either deny the request or lower the permissions. That way, no usermode process can now read or write the games memory. Same can be applied to module loading and file system access.

![Image 2: screenshot](https://tulach.cc/assets/img/posts/9_cheat_engine.png)

_Using open-source [Cheat Engine](https://github.com/cheat-engine/cheat-engine) to try to read protected game’s memory (all reads fail)._

So how can anyone get around it? They also **somehow** need to get their code into the kernel, which will open many ways for them to access the game memory.

Notice how I highlighted “somehow”? That’s because Windows is a closed system where Microsoft has the control to decide [who should get access to the kernel](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/kernel-mode-code-signing-requirements--windows-vista-and-later-). All official kernel components are signed with Microsoft code signing certificates, so it’s trivial to verify their authenticity. All 3rd party drivers need to be signed with an [EV code signing certificate](https://learn.microsoft.com/en-us/windows-hardware/drivers/dashboard/code-signing-reqs) (which can only be bought by companies) and then go through the [Hardware Developer Center](https://learn.microsoft.com/en-us/windows-hardware/drivers/dashboard/hardware-program-register) certification so they can even be loaded. I am not saying this is perfect; in fact, I will most likely be writing an article about how bad actors are still getting their stuff certified. However, when they do, it usually gets quickly revoked, and it’s so costly and complicated that most don’t even bother trying.

There is, of course, a way to get around it by using [all sorts of exploits](https://github.com/SamuelTulach/nullmap) or by [using vulnerable drivers](https://github.com/hfiref0x/KDU) (drivers that expose a programming interface to user-mode processes without any checks in place, which allows them to escalate their privileges and possibly even manipulate kernel components). This is where the second goal defined above comes in. The anti-cheat has to actively scan the system and try to find code that is not associated with any legitimate module (a module that was loaded properly, with all certs in place) and other modifications or patches that would otherwise not be there.

While most gamers are going to say that those anti-cheats are useless and that they see cheaters left and right, the truth is that they add a huge skill check, so not everyone is able to write a cheat and then not get banned. In fact, if done properly, the cheating problem can be basically eliminated this way (I’ll get to this later).

Another reason to run in the kernel is HWID (hardware identifier) banning (the 3rd point mentioned above). If a player is banned and creates a new account, playing on the same hardware will result in an immediate ban. Since the anti-cheat has a kernel component, it can directly talk to the hardware and read its serials that way. If it was running only as a user-mode process, it would be trivial to fake the serial reads. I am not personally a big fan of this since, as you can imagine, it can result in all sorts of unintended issues (people buying used hardware), but in reality, it’s not really a problem since those HWID bans usually expire after a few months (the game devs won’t tell you this though 😉).

[](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#doing-it-properly) Doing it properly
-------------------------------------------------------------------------------------------

If I had to pick a game which handles cheating the best, then as of now in my humble opinion it would be [Valorant](https://playvalorant.com/en-gb/) by [Riot Games](https://www.riotgames.com/en). Keep in mind the stuff that you’ve just read and let me explain:

*   The anti-cheat is loaded on boot. While scary for some, this allows them to block/detect the previously mentioned vulnerable drivers and exploits. This raises the skill required to write a cheat for the game even higher (usually, people resort to [bootkits](https://tulach.cc/bootkits-and-kernel-patching/)).
*   The kernel driver then doesn’t do anything apart from logging (locally). When the game is actually started, it goes through those logs and figures out if the game launch should be allowed or not and does all the kernel protection stuff mentioned above.
*   More advanced methods to obtain HWID are used, such as reading [TPM EK](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/tpm-key-attestation), which is very hard to spoof properly.

But that’s not all. If that was all there was to it, other anti-cheats would be just as effective. The anti-cheat team closely works with the game development team as well. How? The anti-cheat introduces [extra protection for certain memory regions of the game](https://reversing.info/posts/guardedregions/). Some [game data are encrypted](https://www.unknowncheats.me/forum/valorant/401729-valorant-1-01-names-decryption.html), and the encryption keys change with every (even small) game update, making it really annoying for cheat developers. On top of all that, the team is very active in the cheating communities to get intel about what they are up to.

I have played Valorant quite extensively, all the way from Silver to Ascendant, and I have yet to meet a cheater.

[](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#concerns) Concerns
-------------------------------------------------------------------------

There are two main concerns that people have with those kernel-mode anti-cheats:

1.   They are in the kernel doing in-depth scans; therefore, they must be vulnerable and a security issue.
2.   They are so deep in the system (and some start on system boot) that they can spy on us without us noticing.

### [](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#security) Security

Let me ask you a question. How many vulnerable drivers (yes, those that can be abused by bad actors to gain kernel access) do you think the average gamer has on their Windows install? I’ll start with my own system. This is what I can immediately think of:

*   [MSI Afterburner](https://www.msi.com/Landing/afterburner/graphics-cards) - `RTCore64.sys` driver (yes, even in the latest version) has a [vulnerability that allows any usermode process to read and write any kernel memory it wishes](https://github.com/oakboat/RTCore64_Vulnerability/blob/main/RTCore64_Vulnerability/MemoryAccessor.cpp)
*   [CPU-Z](https://www.cpuid.com/softwares/cpu-z.html) - `cpuz142_x64.sys` driver has (again) [kernel memory read/write vulnerability and MSR register read/write](https://github.com/shareef12/cpuz)

If I looked hard enough, I would most likely find more.

It would be really stupid of me to just point to random crap you could have on your computer and say “you have so much exploitable stuff, don’t even bother with security,” and that’s not what I am trying to say. Or maybe it is, but just a little bit… What I am trying to say is that there are many ways a malicious actor could do bad stuff with your system, but anti-cheat is very unlikely to have anything to do with it. In fact, I personally trust those anti-cheat developers much more than random vendors, since they are going to be very well aware of the possible abuse.

Furthermore, if you are using any commercial anti-malware solution, it’s definitely running its own kernel-mode driver (sometimes even multiple of them), and it’s most likely [doing much more sketchy stuff to your system](https://en.wikipedia.org/wiki/2024_CrowdStrike_incident).

Overall, the Windows driver ecosystem is a mess, but unfortunately, that is not going to change any time soon.

### [](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#spying) Spying

As someone who is very well versed in Windows internals, I can tell you one thing, it doesn’t make sense. If you give the program administrative permissions (at least once), it can spy on you in the same way a kernel-mode driver could. There is absolutely no difference and it’s significantly easier to just write a standalone program. There are people who don’t want to play games because of their connection to [Tencent](https://www.tencent.com/) (for example), but if it wasn’t for the kernel-mode anti-cheat, they would have no problem with it. Isn’t it a bit hypocritical? If the game company wanted to spy on you, they could have done so from the game process or the [service they have most likely installed for DRM purposes](https://gamerant.com/stalker-2-drm/).

Oh and just by the way, the vast majority of the data networked by those previously mentioned anti-cheats to their respective servers comes from their usermode component. The only thing that’s sent “by the kernel component” (in quotes since the usermode service requests the data from the driver and then networks it, drivers cannot directly network data) is the HWID mentioned multiple times above and then detections (something that’s out of the ordinary). There is really not some magic data grabbing happening that’s only possible in the kernel.

Another thing that is sometimes mentioned is that since it’s in the kernel, it would be harder for security researchers to debug and assess the possible spying. While technically true that it’s harder, it’s definitely not impossible or problematic for an experienced person, so trust me, security researchers and _especially_ the entire cheating community keep a close eye on it, in the same way they do on the usermode components.

[](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#linux) Linux
-------------------------------------------------------------------

Congratulations, you have successfully made it. You have read all of the stuff and now we can finally get to the Linux part of this post 🎉.

As you can probably already tell by the extensive rant above, I don’t have much good news. Linux is an open system. There is no central authority like on Windows that would tell you what you can and what you cannot do in the kernel. This obviously has countless advantages and it’s why so many people (and big corporations) love it, but is also the reason why anti-cheats cannot really function like they do on Windows.

There is no way for them to block or detect memory access into the game. Anything you could think of would just not work. Kernel module? Just recompile the kernel and change the functions it uses to hide the possible cheat and bypass all checks. Mandatory kernel patch? Same thing. What about usermode detections? Just run the game in a [fakeroot environment](https://wiki.debian.org/FakeRoot) while the cheat runs with real root privileges, being hidden from the game completely… Mandatory custom kernel build? Entire Linux system dedicated to the anti-cheat? I mean… that could work, but at that point, you can just install Windows.

There have been attempts to get anti-cheat to work on Linux. [Easy Anti-Cheat](https://www.easy.ac/en-US) is the most prominent one. Developers can [choose whether they want to allow it to run on Linux or not](https://www.gamingonlinux.com/2021/09/epic-games-announce-full-easy-anti-cheat-for-linux-including-wine-a-proton/). Linux gamers look at this and use it as an argument that anti-cheat on Linux does not face any issues, but the truth is that apart from the most basic sanity checks, EAC does absolutely nothing on Linux. It’s just a simple module that facilitates the server connection and data encryption/decryption for the game.

One of the games that allowed EAC to run under Wine/Proton is [Apex Legends](https://www.ea.com/games/apex-legends). I won’t be putting any links here, but if you search [GitHub](https://github.com/) for cheats for this game, you will find many that work on Linux and there is absolutely no anti-cheat bypass required. It just works.

[](https://tulach.cc/the-issue-of-anti-cheat-on-linux/#all-hope-lost) All hope lost?
------------------------------------------------------------------------------------

As mentioned above, if you want to achieve the best results, you need to utilize both the **active** and **passive** measures. Active being the kernel component on Windows blocking memory access and trying to find possible discrepancies. Passive being the code virtualization, obfuscation, game data encryption as well as proper game networking and server-sided checks.

An example of how **not** to utilize kernel-mode anti-cheat would be [Fall Guys](https://www.fallguys.com/en-US) (yes, that’s the game that one friend made you buy just so you could play it for 30 minutes and then never open again). This game is very specific. There would be no gain in having some sort of wallhack, there would be no gain in having any sort of aimbot (you don’t aim at stuff). All that people did was speedhacking and modifying the game in a way that allowed them to jump higher and generally change their movement. This game is a prime example of why you should write your network code properly. If the game had proper networking and server checks in place (tick-based system, actions performed on both the client and server, if there is a mismatch, the server is the authority and resets the player - that’s how [CS:GO](https://en.wikipedia.org/wiki/Counter-Strike:_Global_Offensive) did it, and that’s why people were not flying over the map in that game or speedhacking, it had other issues though), there would be no need for anti-cheat. Not even a usermode one. Instead, they fixed absolutely nothing from their side and slapped [Easy Anti-Cheat](https://www.easy.ac/en-US) on top of their game.

While it’s not really possible to do any of the previously mentioned active measures, there is nothing stopping you from utilizing the passive ones. So, if you are a game developer and want to limit cheating in your game on Linux:

*   Write proper networking code, verify data sent by the client so your game server does not blindly accept mach 8 as a walking speed.
*   Use code obfuscation and virtualization as much as possible (be aware of the performance penalty, be smart about what parts of the code you protect), try to change it a bit with every update (commercial bin2bin obfuscators like [VMProtect](https://vmpsoft.com/) or [Themida](https://www.oreans.com/Themida.php) will produce different results on each run).
*   If you have control over the game engine itself, try to keep sensitive information on the stack as much as possible.
*   Do not ship debug symbols with your game, [make sure the Linux binaries are stripped](https://www.baeldung.com/linux/strip-executables).

Thanks for reading.