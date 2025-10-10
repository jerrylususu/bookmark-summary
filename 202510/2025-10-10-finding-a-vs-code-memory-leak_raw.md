Title: Finding a VS Code Memory Leak

URL Source: https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/

Published Time: 2025-10-09T20:21:07+00:00

Markdown Content:
Finding a VS Code Memory Leak | Random ASCII – tech blog of Bruce Dawson

===============

[Random ASCII – tech blog of Bruce Dawson](https://randomascii.wordpress.com/ "Random ASCII – tech blog of Bruce Dawson")

Forecast for randomascii: programming, tech topics, with a chance of unicycling

[![Image 4](https://randomascii.wordpress.com/wp-content/uploads/2011/07/blog-header-from-p2090787.jpg)](https://randomascii.wordpress.com/ "Random ASCII – tech blog of Bruce Dawson")

[Skip to content](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#content "Skip to content")

*   [Home](https://randomascii.wordpress.com/)
*   [About](https://randomascii.wordpress.com/about/)

[← Acronis True Image Costs Performance When Not Used](https://randomascii.wordpress.com/2025/05/26/acronis-true-image-costs-performance-when-not-used/)

[Finding a VS Code Memory Leak](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)
------------------------------------------------------------------------------------------------------------

Posted on[October 9, 2025](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/ "1:21 pm")by[brucedawson](https://randomascii.wordpress.com/author/brucedawson/ "View all posts by brucedawson")

In 2021 I found a huge memory leak in VS code, totalling around 64 GB when I first saw it, but with no actual limit on how high it could go. I found this leak despite two obstacles that should have made the discovery impossible:

1.   The memory leak didn’t show up in Task Manager – there was no process whose memory consumption was increasing.
2.   I had never used VS Code. In fact, I have still never used it.

So how did this work? How did I find an invisible memory leak in a tool that I have never used?

This was during lockdown and my whole team was working from home. In order to maintain connection between teammates and in order to continue transferring knowledge from senior developers to junior developers we were doing regular pair-programming sessions. I was watching a coworker use VS Code for… I don’t remember what… and I noticed something strange.

So many of my blog posts start this way. “This doesn’t look right”, or “huh – that’s weird”, or some variation on that theme. In this case I noticed that the process IDs on her system had seven digits.

That was it. And as soon as I saw that I knew that there was a process-handle leak on her system and I was pretty sure that I would find it. Honestly, the rest of this story is pretty boring because it was so easy.

You see, Windows process IDs are just numbers. For obscure technical reasons they are [always multiples of four](https://devblogs.microsoft.com/oldnewthing/20080228-00/?p=23283). When a process goes away its ID is eligible for reuse immediately. Even if there is a delay before the process ID (PID) is reused there is no reason for the highest PID to be much more than four times the maximum number of processes that were running at one time. If we assume a system with 2,000 processes running (according to pslist my system currently has 261) then PIDs should be four decimal digits. Five decimal digits would be peculiar. But seven decimal digits? That implies at least a quarter-million processes. The PIDs I was seeing on her system were mostly around four million, which implies a million processes. Nope. I do not believe that there were that many processes.

It turns out that “when a process goes away its ID is eligible for reuse” is not quite right. If somebody still has a handle to that process then its PID will be retained by the OS. Forever. So it was quite obvious what was happening. Somebody was getting a handle to processes and then wasn’t closing them. It was a handle leak.

The [first time I dealt with a process handle leak](https://randomascii.wordpress.com/2018/02/11/zombie-processes-are-eating-your-memory/) it was a complicated investigation as I learned the necessary techniques. That time I only realized that it was a handle leak through pure luck. Since then I’ve shipped [tools to find process-handle and thread handle leaks](https://github.com/randomascii/blogstuff/tree/main/FindZombieHandles), and have documented the [techniques to investigate handle leaks of all kinds](https://randomascii.wordpress.com/2021/07/25/finding-windows-handle-leaks-in-chromium-and-others/). Therefore this time I just followed my own recipe. Task Manager showed me which process was leaking handles:

[![Image 5](https://randomascii.wordpress.com/wp-content/uploads/2025/10/image-1.png?w=229)](https://randomascii.wordpress.com/wp-content/uploads/2025/10/image-1.png)
And an ETW trace gave me a call stack for the leaking code within the hour (this image stolen from the [github issue](https://github.com/microsoft/vscode/issues/134939)):

[![Image 6](https://randomascii.wordpress.com/wp-content/uploads/2025/10/image.png?w=1024)](https://randomascii.wordpress.com/wp-content/uploads/2025/10/image.png)
The bug was pretty straightforward. A call to OpenProcess was made, and there was no corresponding call to CloseProcess. And because of this a boundless amount of memory – roughly 64 KiB for each missing CloseProcess call – was leaked. A tiny mistake, with consequences that could easily consume all of the memory on a high-end machine.

[This is the buggy code](https://github.com/microsoft/vscode-windows-process-tree/blob/bc0ee891ca3df19dad46b023e3bb1266dfd1a205/src/process.cc#L44-L58) (yay open source!):

```
void GetProcessMemoryUsage(ProcessInfo process_info[1024], uint32_t* process_count) {
  DWORD pid = process_info[*process_count].pid;
  HANDLE hProcess;
  PROCESS_MEMORY_COUNTERS pmc;
  hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, false, pid);
  if (hProcess == NULL) {
    return;
  }
  if (GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
    process_info[*process_count].memory = (DWORD)pmc.WorkingSetSize;
  }
}
```

And this is the code with the fix – the bold-faced line was added to fix the leak:

```
void GetProcessMemoryUsage(ProcessInfo& process_info) {
  DWORD pid = process_info.pid;
  HANDLE hProcess;
  PROCESS_MEMORY_COUNTERS pmc;
  hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, false, pid);
  if (hProcess == NULL) {
    return;
  }
  if (GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
    process_info.memory = (DWORD)pmc.WorkingSetSize;
  }
  CloseHandle(hProcess);
}
```

That’s it. One missing line of code is all that it takes to waste tens of GB of memory.

The bug was found back when I still used Twitter so I [reported my findings there](https://github.com/microsoft/vscode/issues/134939) (broken link, cached copy found in the [wayback machine](https://web.archive.org/web/20220506224017/https:/twitter.com/BruceDawson0xB/status/1447668569626476548)) and somebody else then filed a [github issue](https://github.com/microsoft/vscode/issues/134939) based on my report. I stopped using twitter a couple of years later and then my account got banned (due to not being used?) and then deleted, so now that bug report along with everything else I ever posted is gone. That’s pretty sad actually. Yet another reason for me to dislike the owner of Twitter.

The bug was fixed within a few days of the report. Maybe [The Great Software Quality Collapse](https://techtrenches.substack.com/p/the-great-software-quality-collapse) hadn’t quite started then. Or maybe I got lucky.

Anyway, if you don’t want me posting embarrassing stories about your software on my blog or on [bsky](https://bsky.app/profile/randomascii.bsky.social) then be sure to leave the Handles column open in Task Manager and pay attention if you ever see it getting too high in a process that you are responsible for.

Sometimes I think it would be nice to have limits on resources in order to more automatically find mistakes like this. If processes were automatically crashed (with crash dumps) whenever memory or handles exceeded some limit then bugs like this would be found during testing. The limits could be set higher for software that needs it, but 10,000 handles and 4 GiB RAM would be more than enough for most software when operating correctly. The tradeoff would be more crashes in the short term but fewer leaks in the long term. I doubt it will ever happen, but if this mode existed as a per-machine opt-in then I would enable it.

### Share this:

*   [Click to email a link to a friend (Opens in new window)Email](mailto:?subject=%5BShared%20Post%5D%20Finding%20a%20VS%20Code%20Memory%20Leak&body=https%3A%2F%2Frandomascii.wordpress.com%2F2025%2F10%2F09%2Ffinding-a-vs-code-memory-leak%2F&share=email)
*   [Click to share on Reddit (Opens in new window)Reddit](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?share=reddit)
*   [Click to share on X (Opens in new window)X](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?share=twitter)

Like Loading...

[](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)

### _Related_

![Image 7: Unknown's avatar](https://2.gravatar.com/avatar/5046e4ce5e1de3d9e062e3ff22d7f3ba7a997c221a6b6d84a73194db7e0aa0d7?s=60&d=identicon&r=G)

About brucedawson
-----------------

 I'm a programmer, working for Google, focusing on optimization and reliability. Nothing's more fun than making code run 10x as fast. Unless it's eliminating large numbers of bugs. I also unicycle. And play (ice) hockey. And sled hockey. And juggle. And worry about whether this blog should have been called randomutf-8. 2010s in review tells more: https://twitter.com/BruceDawson0xB/status/1212101533015298048 

[View all posts by brucedawson →](https://randomascii.wordpress.com/author/brucedawson/)

 This entry was posted in [Bugs](https://randomascii.wordpress.com/category/bugs/), [Code Reliability](https://randomascii.wordpress.com/category/code-reliability/), [Debugging](https://randomascii.wordpress.com/category/debugging-2/), [Investigative Reporting](https://randomascii.wordpress.com/category/investigative-reporting/), [memory](https://randomascii.wordpress.com/category/memory/), [Programming](https://randomascii.wordpress.com/category/programming/), [Rants](https://randomascii.wordpress.com/category/rants/) and tagged [ETW](https://randomascii.wordpress.com/tag/etw/), [handles](https://randomascii.wordpress.com/tag/handles/), [leaks](https://randomascii.wordpress.com/tag/leaks/), [VS Code](https://randomascii.wordpress.com/tag/vs-code/), [Windows](https://randomascii.wordpress.com/tag/windows/). Bookmark the [permalink](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/ "Permalink to Finding a VS Code Memory Leak"). 

[← Acronis True Image Costs Performance When Not Used](https://randomascii.wordpress.com/2025/05/26/acronis-true-image-costs-performance-when-not-used/)

### 11 Responses to _Finding a VS Code Memory Leak_

1.   ![Image 8: joyful255a8a71aa's avatar](https://2.gravatar.com/avatar/2cc9ae8484700ce4caa6fd0af3959d5522bbad42b4aed84ccc2c19fba246b191?s=40&d=identicon&r=G)joyful255a8a71aa says: [October 9, 2025 at 1:55 pm](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105048) This is an identical problem I ran into: A process had opened a handle to a subprocess to collect some information and had one code path that failed to close the handle. (Which is why we should all start using raii objects in C++). This went out in a commercial product!Instead of developing a tool like you :-), I used sysinternals process explorer, to find the dangling handles. While the tool does pinpoint where the handle leaks from, knowing the code, it was pretty straight forward to hone in on it. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105048#respond)  
    *   ![Image 9: joyful255a8a71aa's avatar](https://2.gravatar.com/avatar/2cc9ae8484700ce4caa6fd0af3959d5522bbad42b4aed84ccc2c19fba246b191?s=40&d=identicon&r=G)joyful255a8a71aa says: [October 9, 2025 at 1:56 pm](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105049) Oh, and a one-line fix solved the problem too 😉 [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105049#respond)  
    *   ![Image 10: Jon's avatar](https://1.gravatar.com/avatar/17502ffd8b2f93775c3d86cfce6ee4ac1993d2028c4e83af4b73df21517661f3?s=40&d=identicon&r=G)Jon says: [October 9, 2025 at 4:36 pm](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105050) +1 to RAII, that naked `OpenProcess`() call is like a naked “new”. I’d hope that static analysis could’ve picked this up.

Now we have AI, I asked ChatGPT to review the code:

**Process handle not closed**

You call `OpenProcess`, but never call `CloseHandle(hProcess)`.

That leaks a handle every time the function is called.

(It didn’t like the *process_count dereference without bounds checking either) [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105050#respond)  
        *   ![Image 11: brucedawson's avatar](https://2.gravatar.com/avatar/5046e4ce5e1de3d9e062e3ff22d7f3ba7a997c221a6b6d84a73194db7e0aa0d7?s=40&d=identicon&r=G)[brucedawson](https://randomascii.wordpress.com/)says: [October 10, 2025 at 2:20 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105053) The indexing into the process_info array was indeed weird, as was the declaration of the parameter as having 1024 entries (meaningless!) since it suggests a misunderstanding of the contract.

And yeah, a naked OpenProcess does feel just as bad as a naked “new” which is a dirty feeling.

The new code is much better, although some RAII would make it even better. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105053#respond)  

2.   ![Image 12: Andrija's avatar](https://2.gravatar.com/avatar/8dfb1e419f9fb395835e0bd17cd2e83e1c3b7f829de2356170a3c94b7f29e367?s=40&d=identicon&r=G)Andrija says: [October 9, 2025 at 9:45 pm](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105051) Good to see another blog post! FWIW, one of the Web archive versions has the Twitter thread, even some pictures are there: [https://web.archive.org/web/20220506224017/https://twitter.com/BruceDawson0xB/status/1447668569626476548](https://web.archive.org/web/20220506224017/https://twitter.com/BruceDawson0xB/status/1447668569626476548) [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105051#respond)  
    *   ![Image 13: brucedawson's avatar](https://2.gravatar.com/avatar/5046e4ce5e1de3d9e062e3ff22d7f3ba7a997c221a6b6d84a73194db7e0aa0d7?s=40&d=identicon&r=G)[brucedawson](https://randomascii.wordpress.com/)says: [October 10, 2025 at 2:25 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105055) Wonderful! Thanks for finding that. It was good to check how good my recollection of the events was. I had a few details wrong, but not enough to matter. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105055#respond)  

3.   ![Image 14: crafty348bba429f's avatar](https://0.gravatar.com/avatar/6809456596e90260c8c388549fabd74aae593bb2a1b23c78b2280721ab285ecd?s=40&d=identicon&r=G)crafty348bba429f says: [October 10, 2025 at 1:08 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105052) Thanks Bruce, I love your posts! And you made me curious. I rebooted my machine and went straight into proc exp. Highest PID is 2242 and 260 processes are running.

So I suppose something is leaking handles, a lot. And I even haven’t started VS Code yet. 😜 [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105052#respond)  
    *   ![Image 15: brucedawson's avatar](https://2.gravatar.com/avatar/5046e4ce5e1de3d9e062e3ff22d7f3ba7a997c221a6b6d84a73194db7e0aa0d7?s=40&d=identicon&r=G)[brucedawson](https://randomascii.wordpress.com/)says: [October 10, 2025 at 2:24 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105054) Maybe there was briefly about 550 processes, or maybe there are slight delays in reusing PIDs. You could run the FindZombieHandles tool to find out for sure:

[https://github.com/randomascii/blogstuff/tree/main/FindZombieHandles](https://github.com/randomascii/blogstuff/tree/main/FindZombieHandles)

My system shows 261 total zombie processes, with half of those held by HPPrintScanDoctorService.exe. The leaking of handles is slow enough to not be tragic – it’s only wasting about 16 MB, which is “cheap enough” now. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105054#respond)  
        *   ![Image 16: crafty348bba429f's avatar](https://0.gravatar.com/avatar/6809456596e90260c8c388549fabd74aae593bb2a1b23c78b2280721ab285ecd?s=40&d=identicon&r=G)crafty348bba429f says: [October 10, 2025 at 2:27 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105056) Sorry Bruce, there was a typo and because I could not post the entire proc exp image here, I just mistyped the number. The highest PID was 22424, which indicated about 5600 processes, right after the boot.

Will run FindZombieHandles right now. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105056#respond)  
            *   ![Image 17: crafty348bba429f's avatar](https://0.gravatar.com/avatar/6809456596e90260c8c388549fabd74aae593bb2a1b23c78b2280721ab285ecd?s=40&d=identicon&r=G)crafty348bba429f says: [October 10, 2025 at 2:33 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105057) I did run it. Nothing explains this case:

23 total zombie processes.

14 total zombie threads.

11 zombies held by HPPrintScanDoctorService.exe(5080)

11 zombies of HPSUPD-Win32Exe.exe – process handle count: 11 – thread handle count: 11

2 zombies held by WMIRegistrationService.exe(5636)

2 zombies of mofcomp.exe – process handle count: 2 – thread handle count: 0

1 zombie held by com.docker.backend.exe(21500)

1 zombie of wsl.exe – process handle count: 1 – thread handle count: 0

1 zombie held by devenv.exe(8620)

1 zombie of PerfWatson2.exe – process handle count: 1 – thread handle count: 1

1 zombie held by vmcompute.exe(4592)

1 zombie of vmwp.exe – process handle count: 1 – thread handle count: 0

1 zombie held by NVDisplay.Container.exe(2728)

1 zombie of dbInstaller.exe – process handle count: 1 – thread handle count: 1

1 zombie held by svchost.exe(2580)

1 zombie of userinit.exe – process handle count: 1 – thread handle count: 0

@Bruce do you have a consolidated approach to identify the abundance of PIDs during boot?

Is it running Windows Performance Recorder through a boot cycle and then use some Randomascii view in WPA? I clicked through the links in your post but was not sure what the latest “how I’ve done it and it worked” actually was. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105057#respond)  

4.   ![Image 18: Marek Knápek's avatar](https://1.gravatar.com/avatar/76e5ed21301dba1dc8c7917a186ead51311ae7f2623d78c44697c1e043d1b42b?s=40&d=identicon&r=G)[Marek Knápek](http://knapek.wordpress.com/)says: [October 10, 2025 at 5:16 am](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comment-105058) I have an idea, job objects. Create a Windows job object, set some limits on it, then create a new process within that job object.

I’m using this with Visual Studio (not VSCode). Because I’m doing lot of C++ constexpr programming, sometimes the C++ compiler starts eating all my RAM (and swap) and as side effect, other apps on my computer might suffer or crash. Yeah, I’m poor and I have little RAM. Also, after exiting VS, some processes might be still lurking around, blocking folder rename and such.

Not with job objects! When I make a mistake and the compiler starts to eat all my RAM, it hits an artificial wall and dies. Rest of my computer surviving just fine. When I’m done for a while, I can exit the IDE, I can then instruct the job object to kill the remaining processes that survived longer than they should. Typically this is some PDB server writer and telemetry apps.

I’m using github / lowleveldesign / process-governor app for this.

Marek Knápek. [Reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/?replytocom=105058#respond)  

### Leave a comment [Cancel reply](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#respond)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

*   Search for:  
*   ### Recent Posts

    *   [Finding a VS Code Memory Leak](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)
    *   [Acronis True Image Costs Performance When Not Used](https://randomascii.wordpress.com/2025/05/26/acronis-true-image-costs-performance-when-not-used/)
    *   [Google Maps Doesn’t Know How Street Addresses Work](https://randomascii.wordpress.com/2025/04/24/google-maps-doesnt-know-how-street-addresses-work/)
    *   [What this blog is about](https://randomascii.wordpress.com/2025/03/25/what-this-blog-is-about/)
    *   [Find me on bsky](https://randomascii.wordpress.com/2025/01/17/find-me-on-bsky/)

*   ### Categories

    *   [AltDevBlogADay](https://randomascii.wordpress.com/category/altdevblogaday/)
    *   [Bugs](https://randomascii.wordpress.com/category/bugs/)
    *   [Chromium](https://randomascii.wordpress.com/category/chromium/)
    *   [Code analysis](https://randomascii.wordpress.com/category/code-analysis/)
    *   [Code Reliability](https://randomascii.wordpress.com/category/code-reliability/)
    *   [Commuting](https://randomascii.wordpress.com/category/commuting/)
    *   [Computers and Internet](https://randomascii.wordpress.com/category/computers-and-internet/)
    *   [Debugging](https://randomascii.wordpress.com/category/debugging-2/)
    *   [Documentation](https://randomascii.wordpress.com/category/documentation-2/)
    *   [Drinks](https://randomascii.wordpress.com/category/drinks/)
    *   [Environment](https://randomascii.wordpress.com/category/environment/)
    *   [Floating Point](https://randomascii.wordpress.com/category/floating-point/)
    *   [Fractals](https://randomascii.wordpress.com/category/fractals/)
    *   [Fun](https://randomascii.wordpress.com/category/fun/)
    *   [Gaming](https://randomascii.wordpress.com/category/gaming/)
    *   [Investigative Reporting](https://randomascii.wordpress.com/category/investigative-reporting/)
    *   [Linux](https://randomascii.wordpress.com/category/linux/)
    *   [Math](https://randomascii.wordpress.com/category/math/)
    *   [memory](https://randomascii.wordpress.com/category/memory/)
    *   [metric](https://randomascii.wordpress.com/category/metric/)
    *   [Performance](https://randomascii.wordpress.com/category/performance/)
    *   [Programming](https://randomascii.wordpress.com/category/programming/)
    *   [Quadratic](https://randomascii.wordpress.com/category/quadratic/)
    *   [Rants](https://randomascii.wordpress.com/category/rants/)
    *   [Security](https://randomascii.wordpress.com/category/security/)
    *   [Symbols](https://randomascii.wordpress.com/category/symbols-2/)
    *   [Travel](https://randomascii.wordpress.com/category/travel/)
    *   [uiforetw](https://randomascii.wordpress.com/category/uiforetw-2/)
    *   [Uncategorized](https://randomascii.wordpress.com/category/uncategorized/)
    *   [Unicycling](https://randomascii.wordpress.com/category/unicycling/)
    *   [Visual Studio](https://randomascii.wordpress.com/category/visual-studio-2/)
    *   [WLPG](https://randomascii.wordpress.com/category/wlpg/)
    *   [Xbox 360](https://randomascii.wordpress.com/category/xbox-360/)
    *   [xperf](https://randomascii.wordpress.com/category/xperf/)

*   ### Meta

    *   [Create account](https://wordpress.com/start?ref=wplogin)
    *   [Log in](https://randomascii.wordpress.com/wp-login.php)
    *   [Entries feed](https://randomascii.wordpress.com/feed/)
    *   [Comments feed](https://randomascii.wordpress.com/comments/feed/)
    *   [WordPress.com](https://wordpress.com/ "Powered by WordPress, state-of-the-art semantic personal publishing platform.")

[Random ASCII – tech blog of Bruce Dawson](https://randomascii.wordpress.com/ "Random ASCII – tech blog of Bruce Dawson")

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

*   [Comment](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#comments)
*   [Reblog](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)
*   [Subscribe](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)[Subscribed](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)

 

    *   [![Image 19](https://randomascii.wordpress.com/wp-content/uploads/2017/07/cropped-uiforetwicon2.png?w=50) Random ASCII - tech blog of Bruce Dawson](https://randomascii.wordpress.com/)
    

Join 2,557 other subscribers

 Sign me up 

    *    Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Frandomascii.wordpress.com%2F2025%2F10%2F09%2Ffinding-a-vs-code-memory-leak%2F&signup_flow=account) 

*   [Privacy](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#)
*   
 

    *   [![Image 20](https://randomascii.wordpress.com/wp-content/uploads/2017/07/cropped-uiforetwicon2.png?w=50) Random ASCII - tech blog of Bruce Dawson](https://randomascii.wordpress.com/)
    *   [Subscribe](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)[Subscribed](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)
    *   [Sign up](https://wordpress.com/start/)
    *   [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Frandomascii.wordpress.com%2F2025%2F10%2F09%2Ffinding-a-vs-code-memory-leak%2F&signup_flow=account)
    *   [Copy shortlink](https://wp.me/p1fTCO-150)
    *   [Report this content](https://wordpress.com/abuse/?report_url=https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)
    *   [View post in Reader](https://wordpress.com/reader/blogs/18565082/posts/4154)
    *   [Manage subscriptions](https://subscribe.wordpress.com/)
    *   [Collapse this bar](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/)

[](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#)[](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#)

Loading Comments...

Write a Comment... 

Email (Required) Name (Required) Website 

[](https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/#)

%d