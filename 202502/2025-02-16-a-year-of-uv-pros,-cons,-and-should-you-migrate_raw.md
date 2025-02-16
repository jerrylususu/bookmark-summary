Title: A year of uv: pros, cons, and should you migrate

URL Source: https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should

Published Time: 2025-02-15T12:51:41+00:00

Markdown Content:
_**(Warning, this is a long article. I got carried away.)**_

_After one year of trying_ [uv](https://github.com/astral-sh/uv)_, the new Python project management tool by [Astral](https://astral.sh/), with many clients, I have seen what it's good and bad for._

_My conclusion is: if your situation allows it, always try_ `uv` _first. Then fall back on something else if that doesn’t work out._

_It is the Pareto solution because it's easier than trying to figure out what you should do and you will rarely regret it. Indeed, the cost of moving to and from it is low, but the value it delivers is quite high._

_While this article will get into the details of why this is so, we will have a dedicated section of **when you don't want to use uv**._

_However, this is NOT an article on HOW to use uv. One will come later._

Despite my enthusiasm for `uv`, I insisted that I couldn't recommend it before having seen it in a lot of different contexts at work.

That's because the Python community is huge and diverse. You have students, data scientists, AI devs, web devs, sysadmins, biologists, geographers, plugin authors... They may work at university, in the administration, in a startup, in the army, in a lab, or in a big corporation.

They operate at different level of skill, experience, environement and contraints, and the more universally useful the tool, the more I can recommend it.

This is a very different situation than say, PHP, JS, Java, or Ruby. Few people, comparatively, create an X-plane plugin in Java, script a GIS in Ruby, code a bank pricing engine in JS, or develop their latest LLM model with a PHP main wrapper. All things you can do with them, but I've seen way more done with Python.

Because I'm a freelancer dev, and also a trainer, I get to navigate those waters and I've seen all other tools fail spectacularly. pyenv, poetry, pipenv, pdm, pyflow, pipx, anaconda...

In fact, this blog started to become popular with one article: [Why not tell people to "simply" use pyenv, poetry, pipx or anaconda](https://bitecode.substack.com/p/why-not-tell-people-to-simply-use)

So I didn't want to give false hopes to people, and sell them something that would only work in my bubble, which unfortunatly [most geeks do](https://www.bitecode.dev/p/lies-damn-lies-and-feedback-on-arch).

Now that I've seen how `uv` is used and how it breaks, I can not only tell you that you should use it, but also why.

But obviously, I can tell you when not to use it.

I'm repeating myself, but bootstrapping in Python is the root of all evil. By bootstrapping, I mean provisioning Python itself, and configuring a new project so that you can later on install dependencies or build a package. Most problems you have down the road (E.G: packaging problems) actually stem from this.

That's because:

*   There are a lot of different ways to install Python, all with different default settings, and gotchas. And those also vary depending of the OS.
    
*   There are a lot to know upfront just to install Python, a language that is particularly suited to beginners who, by definition, don't.
    
*   Python is used in so many different contexts it's extremly hard to create "one tutorial to rule them all". A python experience provided on locked down company laptop Windows machine looks nothing like one on a debian hobbyist laptop.
    
*   Very few people give good advice on the matter, but everyone and their cat talk with an authoritative tone about it. There. Is. So. Much. BS. About. This. Online.
    
*   There are many tools that try to solve that problem, so we now suffer from the paradox of choices.
    
*   `PATH`, `PYTHONPATH`, terrible naming conventions, having multiple Python versions on the same machine, optional packages on Linux, and Python being a system dependency create a thousand ways to shoot yourself in the foot.
    
*   `-m` and `py` failed in their mission. Most people don't even know they exist.
    
*   The popularity of compiled extensions adds a lot of fun to the mix.
    
*   People will encounter problems directly linked to all this, but with no clue it's the case, and will just say things like "Python packaging suck" since they will blame the thing that they were trying to use, not the root cause they have no idea about.
    

A good Python project manager, therefore, should have the following properties:

*   Being independent from Python bootstrapping, so that there are no chicken-and-egg problems, also working around `PATH` and `PYTHONPATH` issues.
    
*   Being capable of installing and running Python in one unified congruent way across all situations and platforms.
    
*   Providing a bridge between the basic tooling (`pip` and `venv`) and itself.
    
*   Having a very strong dependency resolver.
    
*   Making simple things simple (installing stuff) and complicated things possible (installing locked dependencies on a different OS than dev).
    
*   All that while being easy to install & use, and of course, so reliable you trust it enough with what is one of the most important aspects of your stack.
    

I mean, what's the big deal?

`uv`'s vision is brilliant. There, I said it.

That's not by mistake, that's been carefully orchestrated by the very talented and hard-working team at Astral.

First, they made it completely independent from Python itself. Whether you install & update `uv` or Python have no impact on each other. There is no bootstrapping problem from Python, `PATH` problem, or import problem that can affect `uv` in any way.

As a consequence, you don't have to know much about the Python ecosystem when installing it. No confusion about where to install it (in the system? in a venv?) or how a new keyword or deprecation is going to affect it.

Then, they started by providing a `pip` and `venv` interface so that you could work with your existing projects, tooling, and paradigm. This is an underrated benefit of `uv`. Not only it makes adoption easier and less scary, but it also:

*   Shows that Astral respects the existing community.
    
*   Acknowledges the importance of the huge legacy pile of code that already exists around the world.
    
*   Demonstrate their will to assume the cost of developping and maintening that quite nasty piece of history for years and years.
    

To me, this was signaling "we know our tribe and we are serious about this".

It also means you could use `uv` as you used `pip` and `venv` before (and even [pip-tools](https://pypi.org/project/pip-tools/)) yet never have to learn anything more, forever. You don't have to learn about `uv run`, `uv add` or `uvx`. The reliability and speed you gain alone on the basic tasks would justify the migration since it would essentially cost nothing as it's the same workflow, just faster and with fewer bugs.

So `uv` would still be a net benefit if they just stopped there.

But of course, they didn't.

They added a way to install Python:

*   In a unified manner across all OS.
    
*   Without requiring admin rights.
    
*   Independant of the system.
    
*   Without conflicts if you install multiple versions.
    
*   All with the same stdlib (yeah, tkinter everywhere!).
    
*   Including Pypy and No-GIL versions (!).
    
*   With no shim, no compilation, and sane defaults.
    

While working on this part of the article, I installed "pypy3.8" in a few seconds with `uv`. I didn't even remember how to do it, but the API and the help messages were so clear I figured it out quickly, and boom, a new Python on my machine:

```
❯ uv python list
cpython-3.14.0a4+freethreaded-linux-x86_64-gnu    <download available>
cpython-3.14.0a4-linux-x86_64-gnu                 <download available>
cpython-3.13.1+freethreaded-linux-x86_64-gnu      <download available>
cpython-3.13.1-linux-x86_64-gnu                   /usr/bin/python3.13
cpython-3.13.1-linux-x86_64-gnu                   /bin/python3.13
...
cpython-3.8.20-linux-x86_64-gnu                   <download available>
cpython-3.7.9-linux-x86_64-gnu                    /home/user/.local/share/uv/python/cpython-3.7.9-linux-x86_64-gnu/bin/python3.7 -> python3.7m
pypy-3.10.14-linux-x86_64-gnu                     <download available>
pypy-3.9.19-linux-x86_64-gnu                      <download available>
pypy-3.8.16-linux-x86_64-gnu                      /home/user/.local/share/uv/python/pypy-3.8.16-linux-x86_64-gnu/bin/pypy3.8 -> pypy3
pypy-3.7.13-linux-x86_64-gnu                      /home/user/.local/share/uv/python/pypy-3.7.13-linux-x86_64-gnu/bin/pypy3.7 -> pypy3

❯ uv python install pypy3.8
Installed Python 3.8.16 in 2.71s
 + pypy-3.8.16-linux-x86_64-gnu

❯ uvx -p pypy3.8 python
Python 3.8.16 (a9dbdca6fc3286b0addd2240f11d97d8e8de187a, Dec 29 2022, 11:45:13)
[PyPy 7.3.11 with GCC 10.2.1 20210130 (Red Hat 10.2.1-11)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>> import tkinter
>>>> import zipfile
>>>> import ssl
>>>>
```

It says "Installed Python 3.8.16 in 2.71s". **2.71s**! And I can do the same and run it the same way afterward on Mac or Windows. This is spectacular.

There is no missing package for tcl, openssl or gzip. No conflict with the other sources of Python. No need for a different paradigm for each OS I use. No missing command or misconfigured `PATH`.

And it works because Astral capitalized on a very promising project called [python-build-standalone](https://github.com/astral-sh/python-build-standalone) and eventually took ownership of it. Those are Python builds that work without installers. The team not only improved the project a lot, but are now actively trying to contribute those benefits upstream to cPython. In fact, all along the project, [they demonstrated](https://github.com/astral-sh/tokio-tar/pull/6) their will to contribute to adjacent FOSS projects.

I'm not sponsored by them, I swear!

Of course, they also added advanced project management to `uv` to go beyond `pip` and `venv`. They are optional, so you can start adopting them at your own pace.

*   `uv init` not only create a ".venv", but also a `pyproject.toml`, a git repo (with Python-specific .gitignore), a `README.md` and a `hello.py` by default. [Configurable](https://github.com/astral-sh/uv/pull/11192) of course.
    
*   You can declare your root dependencies in `pyproject.toml` or add them with `uv add`.
    
*   `uv remove` actually cleans up your repo correctly.
    
*   `uv lock --upgrade-package <package>==<version>` let you upgrade carefully your packages one version at a time.
    
*   `uv build` create a `.whl` package out of your project, but `uv` doesn't require your project to be able to be built.
    
*   `uv run` will run any command in the venv, even if it's not activated. You don't even need to know there is a venv, or what activation means.
    
*   All those commands update the lock file automatically and transparently. You don't need to babysit your project. It's all taken care of. This is possible because `uv` is so fast you won't even feel an update is happening. You don't even need to know what a lock file is.
    
*   [The lock file is cross platform](https://docs.astral.sh/uv/concepts/resolution/#universal-resolution) (a crazy fact in itself!), so you can dev on windows and deploy on linux.
    

The fantastic performance (again, by design, Astral has very interesting tricks they use to speed it all up, see [our interview](https://www.bitecode.dev/p/charlie-marsh-on-astral-uv-and-the)) means not only it will feel effortless, but it will encourage you to experiment. You will not pay the price for trying things out anymore. You can just start all over in a few seconds after all.

The last, but not least important point, is the reliability of the tool. I can't count the number of times `pyenv`, `pipenv` or `poetry` broke on me, giving me some stack trace to deal with. Fans of those tools will tell you it doesn't happen to them, but firstly, they lie (I've seen someone say that minutes after one did!), secondly, they use it usually in one or two contexts only, giving them a very small angle of vision on the scenery.

On the other hand, not only `uv` has been immensely robust, it also comes with 3 particularly rare and desirable qualities:

*   Astral is extremely good at fixing bugs. They listen to feedback. They are reactive to reports. And they are very industrious. Their bug tracker is kind of mind-blowing to be honest.
    
*   They have a great testing culture. E.G: they have [a hell of a resolution testing suite](https://github.com/astral-sh/packse/tree/main/scenarios). And they made it a separate package so other projects can use it.
    
*   They provide excellent error messages. Look at this beautiful resolution failure:
    

```
❯ uv add httpie==2
  × No solution found when resolving dependencies for split (python_full_version >= '3.10'):
  ╰─▶ Because httpie==2.0.0 depends on requests>=2.22.0 and your project depends on httpie==2, we can conclude that your project depends on requests>=2.22.0.
      And because your project depends on requests==1, we can conclude that your project's requirements are unsatisfiable.
  help: If you want to add the package regardless of the failed resolution, provide the `--frozen` flag to skip locking and syncing.
```

You can argue this is thanks to [pubgrub](https://github.com/pubgrub-rs/pubgrub) but all their error message strive to be like this, and they chose their dependency mindfully.

Basically, they took what was working in `pip`, `rye` and `poetry`, and discarded all the stuff that didn't work. Then they spent months killing tickets to bring it to an insane level of quality.

This cannot be understated, as such a level of quality and dedication is so extremely rare in software that I usually associate it with things like VLC or sqlite. This is the league I put `uv` in.

The result is that when I put `uv` in the hand of my students in trainings, I had very little work to do. I was surprised to see how easily they got to being productive with it, without much of my input. How rare I had to intervene. Something that never happened with any other tool.

In professional projects, it was a slightly different story. New projects would benefit easily from `uv`. Legacy projects were where blockers could show up, as we will see later on.

You would think I'm done praising what looks like nothing more than a glorified package manager, but I have a few additional notes on it.

When creating `uv`, Astral created strong, fast, and robust primitives. What happens when you do that is that you open a whole new universe of use cases.

And it did.

In this case, the primitives are Python + dependencies provisioning and isolation.

This doesn't sound like much, but it's a paradigm shift. Before, I though about those as contraints. Something I had to do, that could go wrong, that was slow, and that I had to be careful about, to get to the part that was interesting to me.

But now with `uv`, I experience them as capabilities: I can play with them to tailor my workflow as I please.

I published a whole article on [uv tricks](https://www.bitecode.dev/p/uv-tricks) but to illustrate my point, I'll copy here two of them:

*   `uv run --with jupyter jupyter notebook` will run [jupyter](http://jupyter.org/) in the current project... without adding jupyter and its dependencies to the project! And because of how `uv` caching works, subsequent calls will be fast.
    
*   Want to know how `pendulum` behaves when imported in the new Python no GIL build? I just ran `uvx --with pendulum -p 3.13t python`, right now. It downloaded the new Python, installed it, created a temporary venv, installed `pendulum` in it, then started a Python shell. In a few seconds. And then, I exited, and it was gone.
    

This is the kind of thing that changes completely how you work. I used to have one big `test` venv that I destroyed regularly. I used to avoid testing some stuff because it would be too cumbersome. I used to avoid some tooling or pay the price for using them because they were so big or not useful enough to justify the setup. And so on, and so on.

`uv` brought, unexpectedly, at least to me, more than Python project management. It added `uvx`, a `npx` like software for Python that I see as "pipx done right". But it also added support for [inline dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies), which, coupled with other `uv` capabilities (remember the good primitives?), alter deeply the way you use Python scripts.

It used to be that either you avoided dependencies in small Python script, or you had some cumbersome workaround to make them work for you. Personally I used to manage a gigantic venv just for my local scripts, which I had to kill and clean every year.

Now, you are free to use whatever. It's fast. Transparent. Efficient. Self-descriptive.

Because all those are not in your face nor mandatory, you can discover them and adopt them in your own time. And I bet the community will discover more and more ways to combine those as the time go by.

I maintained a list of `uv` shortcomings over the year, just for the purpose of this article. But this list grew smaller and smaller, as Astral crunched their bug tracker day after day. They added editable installs, a python fallback to `uv run`, tkinter available everywhere, added support for non-packaged projects, respected XDG, shipped header files (yep!), etc. They even are working on [task support](https://github.com/astral-sh/uv/issues/5903) as you read.

**So there is not a lot to complain about anymore**, but I have to mention it.

Ironically, `uv` can't solve packaging problems. Real packaging problems, not broken bootstrapping consequences. Things like bad versioning markers, absence of wheels, name conflicts, etc. That's because it's out of `uv`'s control, and those are inherent to the quality of the data available on Pypi. The only reason you will see tremendously fewer packaging problems with `uv` is because it does everything else right.

Therefore I won't judge `uv` on that point, which is incredibly funny given it's a package manager. `uv` works very well with what it has.

However, because it has a much better resolver, it can actually break your venv on legacy projects where you used an old version of `pip` that had a more lenient approach to package resolution.

I had a friend who decided to not use `uv`, because the first time it used it, it was on a 15 years old codebase that had just been migrated to Python 3. It was standing on a pile of never cleaned up `pip freeze` exports, and `uv` could not make it work.

Another problem is that, because `uv` uses `python-build-stand-alone`, you are limited to the versions of Python that have been built for that format. While you can install many more versions of Python with the installer in python.org, using deadsnake or pyenv. It seems like not a problem for a greenfield project, but it is for a project that has been running for a long time and needs one specific version of Python to run. Fortunately, `uv` doesn't mind playing with a version of Python installed externally, so it's not a big deal, but it's something that people may not realize.

It's an important feature anyway if you want to swap the provided Python with a faster one. python-build-standalone executables are a tiny bit slower by themselves (I just ran the [pyperformance](https://pyperformance.readthedocs.io/) benchmark, and uv's 3.10 is 3% slower than my Ubuntu one), plus you may want one day to use a Python that is compiled with optimizations for your hardware. Not a common thing to do, but a good option to have.

Yes, I am nitpicking at this point.

One more issue is how much space `uv`'s cache take. After one year of use, it took more than 20Gb on my disk. You can delete it with `uv cache clean`, but then you lose the incredible speed advantage it gives you.

Again, it's not a terrible problem. I have 2 TB of hard drive. Besides, the space taken `uv` is likely to be less than all the venvs combined I had before, since unlike with `pip`, packages are hard linked, and take only space once.

I have one paper cut right now, which is that `$UV_PYTHON` forces a version of Python instead of giving you a default version of Python, [but it's been taken care of.](https://github.com/astral-sh/uv/issues/6645)

Evidently, I also have to address the elephant in the room: `uv` is a product from a commercial venture, Astral. Despite the fact it's open source, and no matter how incredible Astral has been, you have to trust them to keep it available and up to date for the community. What's more, they are not profitable yet, we have seen no commercial offering from them, so we don't know what's going to hit us. Some people, like in our [interview with Russell Keith-Magee](https://www.bitecode.dev/p/russell-keith-magee-on-beeware-packaging), are getting nervous about it and argue we should be prudent before giving control to such an important part of our stack.

I'm not personally worried about this. Migrating to `uv` has been easy in _almost_ all projects I've done, and migrating off it is not hard either. Painful because of the mourning period of the awesome features, but not hard. Plus, Astral has accumulated a huge amount of trust through their stellar behavior, so if I have to trust some entity, I'd rather trust them. In fact, I'll welcome a paid product from their part, I want to give them money. I want them to thrive.

What else do you want them to do to gain your trust? Perform CPR on your grandma's choking on Xmas dinner? They already went above and beyond. I don't feel entitled to more demonstration of good faith.

It's open source, anybody can fork it. Not to mention the code is incredibly clean. And sure, it's Rust, but there are plenty of Pythonistas that know Rust now. Pretty sure if Charlie were hit by a bus (sorry mate, I don't wish that but buses are merciless creatures), Armin would jump in, or somebody else.

No, the biggest limitation to using `uv` as of today is corporate adoption. It's extremely hard to install new dependencies in big, secure, locked-down corporate settings. Right now, if you have an IT security department that governs what you can and can't do on your machine, they are not going to let you install `uv`. Not until it reaches a stable version and has checked a lot of boxes.

However, I'm assuming this is how Astral is going to make money, by being a direct competitor to Anaconda. And I assure you, there is an appetite for it, because Anaconda is the opposite of Batman, and if they manage the lobbying part (which is super hard, don't get me wrong), the technical side will be already singing `uv`'s praises on arrival.

If they want to, though, they’ll have to fix another issue: there is a non-trivial amount of Python coders that are not comfortable with the command line. Especially on Windows, a.k.a, most of the corporate market. This is why Anaconda has a GUI. This is one of the reasons I recommend python.org installers. Requiring a CLI tool for total beginners is a big barrier to entry.

Finally, `uvx` (and so `uv tool install`) suffers from a similar problem then `pipx`, is that it encourages you to install some tools outside of your project. This makes sense for things like [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [httpie](https://httpie.io/) which are self-contained independent tools. But it's a trap for dev tools that care about syntax or libs, like `mypy` that will be installed in a certain Python version, but then used on a project with another potentially incompatible Python version. They will break spectacularly and many users won't understand why.

As you can see, there is no deal-breaker left, all of those are annoyances. We are past the point where I can point at something and say "this is why you should definitely not use uv ever".

Basically, there are 5 situations when you should not use `uv`:

*   You have a legacy project where using `uv` to resolve dependency would not work and you can't (or don't want to) afford to clean up the mess for the purpose of migrating.
    
*   You are in a corporate environment that will not let you use it.
    
*   You don't trust it just yet, because it's not a stable version yet, because Astral hasn't released their commercial offering, because the Rust contributor pool is too small, etc.
    
*   You need a specific version of Python that `uv` doesn't provide, and you don't want to use `uv` if you can't install Python with it as well despite the fact it works very well with 3rd party installed Python.
    
*   You think the CLI is too big of a show-stopper for the team.
    

To me, 3 and 4 are not really technical, so they are not so much blockers as they are choices. I'm not here to convince you to make different choices, I have no horse in this race, you do you.

Number 2 is not something you can't do much about, so the point is moot.

This means I really only have to consider cases 1 and 5, and for this, I have one single advice:

**Always try** `uv` **first. If it doesn't work (which is very rare), go back to what you did before or find a workaround.**

If the CLI proves to be too much of a problem, suggest using the python.org installer for provisioning, and an IDE plugin that abstracts `uv` away. But try it first, people who can program usually can learn enough of the command line basics to use uv.

If really it doesn’t work, then you move to something else.

Given the sheer benefit of using the tool, the very low cost of adoption, and the even more limited chances that it doesn't work for you (whether it's case 1, 2, or something I don't know about; after all, I have to assume there are other edge cases I didn't hit), it's just a good bet.

Statistically, you will win most of the time, and that's all you need.

There are still some gaps until v1, a requirement for a corporate future as you can’t update much there. I'm assuming some form of bundling will be added to the tool as an alternative to pex/shiv, and probably a build backend. I don't know if they have plans to allow the creation of an installer for your app, but that would be the logical conclusion, although a lot more complicated than it seems (the signing alone is tough to get right).

I frantically run `uv self update` to get the new goodies that they keep coming up with, but to be honest, once they get the task story refined, the tool is feature-complete for my needs.

Anyway, I'm going to edit all my articles about `pip` and `venv` to mention `uv`. And write an `uv` tutorial.

One should still learn how to use `pip` and `venv` anyway if Python is your job, since you will probably end up one day in a situation where `uv` is not available.

Nevertheless, starting from now on, I will tell everyone to "just use `uv`".

It's the Pareto solution, and you know how much I love Pareto.
