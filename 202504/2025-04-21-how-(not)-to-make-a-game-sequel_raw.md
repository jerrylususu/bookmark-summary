Title: How (Not) to Make a Game Sequel

URL Source: https://ruoyusun.com/2025/04/18/game-sequel-lessons.html

Markdown Content:
18 Apr 2025

I have recently started to work on my third Steam game: [Spaceship Idle](https://store.steampowered.com/app/3454630/Spaceship_Idle_Design_Build_Explore__Battle/), which is a sequel to [CivIdle](https://store.steampowered.com/app/2181940/CivIdle/), which itself is a sequel to [Industry Idle](https://store.steampowered.com/app/1574000/Industry_Idle/). CivIdle is my first sequel game, and I’ve learned a lot during its development: some worked well, others not so much. I’ve decided to write down all the lessons learned for my own sake, and hopefully, they are an interesting read as well.

What Works
----------

### Focus on a Smaller Number of Platforms

I once wrote about my experience releasing Industry Idle on six different platforms during early access, and it was not a pleasant experience; I ended up having to spend a lot of time dealing with platform-specific issues and paperwork.

For CivIdle, I’ve decided to focus on Steam, specifically Windows and Linux, as the macOS build requires notarization, which makes the build pipeline go from a few minutes to potentially hours. I understand that eventually I will need to get to those platform-specific shenanigans, but hopefully, at that time, the game is more or less stable and complete, so I don’t have to make builds very frequently.

So far, this has been working great, and I plan to port the game to other platforms once the game exits early access.

### Design with Ease of Operation in Mind

Industry Idle’s global player trade system was a later addition, and it shows. And inadvertently, I stepped into a death triangle:

*   The game is free-to-play: this means it’s impossible to block bots, spammers, and alt accounts. And if a cheater is banned, they can easily get a new account.
*   I am the only developer: I have neither the time nor money to run a proper anti-cheat solution (server-driven check). And heuristic-based anti-cheat requires lots of manual intervention.
*   The economy is player-driven: a cheater can ruin the game experience for everyone. Because player trading is global, the problem can spread very quickly, and simply banning the cheater is not enough.

This problem became so bad that I had to spend almost half of my time dealing with it - time I could have spent on making more game content instead. And it only became less of an issue when the game entered the long tail of its life cycle and there weren’t that many players.

So for CivIdle, I’ve decided to tackle this one by one:

*   I still keep the game free. However, all free-to-play players are put under a 48-hour probation period, during which they have limited access to the player trading system. This adds a significant cost for bots, spammers, and cheaters, and players who are out of the probation period rarely cheat. I am not completely happy with this solution and plan to introduce a more gradual system in Spaceship Idle.
*   I still have limited resources, given I am working on the game during my free time and the game is not heavily monetized. However, I’ve made some gameplay changes so that the heuristic becomes much more reliable - it will not cause false positives, and the whole process can be automated.
*   I still keep the global player trade economy, but I’ve introduced some restrictions, specifically a price cap. In this case, even if a cheater manages to access the player trade, they will not drive the price down to zero and can only have limited impact before getting caught.

During the very early stage of development, I had a small-scale playtest, which resulted in me completely rewriting the gameplay code - because the game lacked a goal and was not fun. The feedback I got from that playtest was much more useful than me trying to polish the game design myself.

And one thing I did when dealing with player feedback was to focus on the problem, rather than the solution. For example, when a player said, “you should change this feature,” I’d follow up by asking, “Why do you think this feature needs changes?” The player would then reveal the reason, which was often more valuable. After this exercise was done several times, game design issues often revealed themselves.

And one thing I could do better is to engage with the community more often. I didn’t have time to do another small-scale playtest before the game entered early access, and unsurprisingly, it turned out the game still had lots of problems. Nowadays, players expect a certain level of polish even in early access. So I will try to do several more small-scale tests before entering early access, if time allows.

### Complete Engine Rewrite

Kickstarting a new game (sequel or not) is usually like this: copy-paste the existing game, rename the folder, and start changing code. This is exactly how Industry Idle was kickstarted. In fact, my renaming was badly done, and to this day, the main save file of Industry Idle is still called “IdlePinballBreakout,” which is a leftover from my previous game.

However, for CivIdle, I decided to do an engine rewrite: I created an empty folder and started from scratch. The main reason is that the rendering library of Industry Idle was based on an abandoned branch of cocos2dx-js, which started to show its age. It did not support a package manager and still used an outdated workflow where I had to include JavaScript files manually. It was also a complete engine and was quite heavyweight - I was only using it as a rendering library, so, at most, 5% of the features.

For CivIdle, I’ve chosen Pixi.JS as the rendering library, React as the UI framework, and Vite as the build tooling. Having a more mainstream set of libraries and tooling helps a lot:

*   Web ecosystem: As an indie game developer, I have to make sure that the limited time I can spend on the project will bring maximum value. And being able to focus on the gameplay and rely on existing libraries is a great time saver.
*   Modern tooling: Hot module reload vastly improves the iteration speed. Library-specific debuggers/inspectors are also very useful. And I managed to integrate my asset pipeline into the build system (Vite). In addition, I could set up the CI/CD server easily with Github Actions. All of these saved a lot of time I would otherwise have had to spend.
*   External contributors: The game is open source (GPL 2.0), even though the majority of the development is done by me. There are occasional external contributors, and I no longer needed to ask them to download some specific version of executables. Also, lots of people know React and Pixi.JS, so it lowers the entry barrier for making a contribution.
*   More useful AI: This is a rather surprising benefit. Because when CivIdle started, AI-assisted coding wasn’t really a thing - and even now, 99% of the time, I only use tab-completion. However, I can clearly notice that AI can give very good completion for more mainstream libraries but tends to hallucinate badly for custom code. A well-behaved AI can save me a lot of typing - and this alone saves a lot of time.

What Does Not Work
------------------

### Complete Engine Rewrite

Yes, the title is not a copy-paste error. The engine rewrite is such a double-edged sword that to this day I still cannot decide whether it’s worth it.

First, I vastly underestimated the amount of work. Industry Idle is based on the previous engine I glued together over the years, and it had lots of stuff that needed to be reimplemented in the new engine. Although I was able to get rid of some legacy code and improve some code along the way, which resulted in a much better codebase, the sheer amount of work added almost a year to CivIdle’s development time. As an example, it took me 6 months to get Industry Idle from an idea to the first playable build and almost one and a half years for CivIdle. There are other factors that have contributed to this, but the engine rewrite is a major one.

Second, when I started without the Industry Idle codebase, I lost a lot of battle-tested code. Because the engine is completely different, gameplay code needed to be completely redone, which resulted in the initial build of CivIdle lacking lots of content and QoL features that were found in Industry Idle. Also, Industry Idle’s codebase contains lots of “special logic” and “hacks” that had been added over the years to address game design problems: edge cases, loopholes, and imbalances. These were the result of the hard work by me and the player community: testing, finding reproductions, figuring out potential solutions, and playtesting them. Of course, I’ve taken all the major learnings from Industry Idle when working on CivIdle; still, I found that I had to re-implement some of those non-obvious “fixes” in CivIdle.

Third, I had to adapt to a new workflow. Most people think of a “game engine” as code that is shipped with the game executable. However, that’s only half of it. The other half, which I’d argue is more significant, is the code that is not shipped with the game - level editors, content pipelines, debugging/profiling tools, development workflows, etc. Because of the engine rewrite, not only did I have to reimplement these tools, but also adjust the overall workflow. For example, I had to figure out a new art production pipeline. If you take a look at the game, you might be wondering: the game barely has any art, which is very true. Because I am not an artist, even the very limited amount of art in the game took significantly longer for me to produce. And since I hadn’t already mastered different art tools, having to switch tools was a big effort for me.

### Abstract Too Early

Industry Idle’s gameplay code was very imperative - this is because a lot of features were added outside the initial game design. Oftentimes they were added as small experiments first and later expanded before it was too much effort to reimplement them.

When working on CivIdle, I thought I would take this chance to implement them properly - introducing more abstractions and more declarative code. This itself isn’t a bad idea, but my mistake was that I did it too early - I did it from the beginning. A lot of the abstractions I introduced would have worked well in Industry Idle, but not CivIdle - because CivIdle is a sequel, not a carbon-copy reskin. I soon found out that many abstractions I thought would help turned out to be handcuffs, and I had to painfully get rid of them. I wouldn’t normally make this mistake when making a completely new game - I am aware of the damage that bad abstractions can do. However, because I was making a sequel, I thought they would be more helpful - it turned out I was wrong.

### Forget to Prototype

This is another mistake that I wouldn’t have made if I were working on a completely new game. From the experience with Industry Idle, I thought I already had a winning formula - so I skipped prototyping completely. After all, prototyping usually means a lot of trial and error and “wasted” effort. Being able to jump right into the game’s production would save me a lot of time - or so I thought.

Halfway through the production, I started to feel a bit worried as the game felt a bit bland. But I managed to convince myself to forge on - after all, this had happened to me before - in fact, it happened during the development of Industry Idle as well.

After getting all the feedback from the first playtest, the issue became clear - there were some fundamental issues with the game’s design, and I had to correct the course right away. Fortunately, after some heavy-handed changes, the game turned out okay. Now, looking back, had I done some prototyping, I would have avoided a lot of the painful course correction.

### Too Hung Up on Continuity

When working on CivIdle, I followed Sid Meier’s “rule of thirds”: one-third is traditional gameplay, one-third is improved from the last version, and one-third is brand new. This is a good guideline to follow when making a sequel, but my mistake was that I took it too literally and followed it too strictly. Before development, I first listed out all features of Industry Idle that I wanted in the sequel, put them into the first two categories, and then I added some new ideas I wanted to try in CivIdle.

During development, I found out that oftentimes the new features didn’t work well with the existing ones. Since I was trying to follow the “rule of thirds,” I would change the new features and keep the existing ones intact. After a few iterations, I started to feel that I had run out of options. Because Industry Idle and CivIdle are essentially complex economics simulation games, there are too many moving parts, and a small change usually requires more changes than I expected. It soon became impossible to keep the first third unchanged.

Now, looking back, I feel the “rule of thirds” is more from a player’s experience: a sequel should make a player feel one third familiar, one third improved, and one third new, which does not necessarily mean keeping one third of the features or the codebase unchanged. A game can have everything changed and yet bring players the familiar feeling of playing the prequel.

Before making CivIdle, I was concerned that the game differed too much from Industry Idle to be considered a sequel. Now I can say that the concern was unwarranted - similarity is the easy part of making a sequel. In fact, simply staying in the same genre is almost half the job done. Because it’s still me making the game, there are lots of traces of “me” in the game: not only the game design, but also the art, UI, writing, sound, etc. In fact, several players who had never played Industry Idle pointed out the similarity between CivIdle and Industry Idle.

### Forget About New Players

During the development of CivIdle, I spent too much effort ensuring continuity and forgot about the new audience. After all, in addition to servicing the existing player base, a sequel should also attract new players.

As I was too eager to try out some new ideas that I didn’t have a chance to implement for Industry Idle, I made CivIdle so complex that it was impossible for players who hadn’t played Industry Idle to get started. I only realized this after the first playtest and had to cut some features and mechanisms in the very late stages of development. This resulted in the first early access release having too complex mechanism, but too little content. It took me several content patches to make enough content to justify the mechanisms, and I managed to gradually add back some features that I had had to cut earlier.

I should have kept the overall complexity in check during the whole development cycle. It is something that can easily go overboard when developing a sequel. And because playtesting is usually done with existing players who have quite some experience with the prequel, the problem can remain hidden until the last minute. And if possible, it would be very helpful to conduct a playtest with players who haven’t played the prequel, although for an indie developer, this is not always feasible.

### Trying Too Hard To Avoid Mistakes

I made a lot of mistakes during the development of Industry Idle. Some of them were relatively easy to correct, others had long-running consequences. So when developing CivIdle, I felt I should have known better by then. I carefully took all the learnings and tried to avoid making the same mistakes again - “Success can’t be copied, but failure can be avoided.” However, even the latter half of the saying needs a pinch of salt. Not that failures cannot be avoided, but getting too hung up on trying to avoid mistakes can have adverse effects.

For example, there are several mechanisms that didn’t work very well for Industry Idle - they are either too complex, too hard to balance, or have negative consequences in the long run. When developing CivIdle, I carefully avoided these mechanisms, thinking I was on the right track.

After the first playtest, it became clear that some of those mechanisms could help solve the issues discovered. However, I still resisted them, believing that I must have missed something and that adding them would have a negative effect in the long run. After the early access release, more feedback came in, and they all pointed in the same direction. So as an experiment, I picked one of the easily reversible features and added it to CivIdle - it worked fine and hasn’t caused any issues since.

A sequel should be a good game first, and then a good sequel, not the other way around. Most of the mistakes I made while developing CivIdle (apart from the engine rewrite) were because of the wrong mindset.

Discuss on [HN](https://news.ycombinator.com/item?id=43730799) or [Reddit](https://www.reddit.com/r/gamedev/comments/1k2cesm/how_not_to_make_a_game_sequel/)
