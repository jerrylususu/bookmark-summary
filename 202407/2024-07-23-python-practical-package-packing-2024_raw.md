Title: Python Practical Package Packing 2024

URL Source: https://matt.sh/python-project-structure-2024

Markdown Content:
Proper Python Project Structure 2024
------------------------------------

are you interested in proper python project perfection for 2024? you’ve come to the right place. let’s get into it.

Require This
------------

If you see a modern active python project with only `requirements.txt` or `setup.py / setup.cfg` in the wild, you must assume the maintainers haven’t learned anything new in half a dozen years.

`requirements.txt` (or “requirements in `setup()` call”) is not a valid way to manage dependencies — and it hasn’t been for the past 5+ years. If you are still using `requirements.txt` it shows you need professional help. luckily, [i’m a professional](https://www.youtube.com/watch?v=K5q9xUFvQXk).

Let’s go over some bad / good / example practices for [living your best python life in 2024](https://www.youtube.com/shorts/B0QdKbIFfr0).

### Python Project Worst Practices

Indicators your python architecture is outdated:

*   **BAD:** using `requirements.txt`
    *   `requirements.txt` has no mechanism to ensure all dependencies are compatible based on their other transitive dependencies. also `requirements.txt` usage defaults to poor developer hygiene because many people [just list names with no versions](https://github.com/google-research/skai/blob/ec52a5744de5bd84e2c8ff969508db78ee2a86aa/requirements.txt), so builds end up completely non-reproducible as time drifts forward.
*   **BAD:** manually creating and entering venv virtual environments — your dependency/package manager should be controlling the creation and destruction of your venvs as well as automatically managing install/uninstall cycles for packages in the venv.
*   **BAD:** any code not in a proper python directory/package structure using python namespace formats. If you are manually setting `PYTHONPATH` because your code isn’t following the 20 year old standard python directory layout, your code is also not reusable and probably difficult to advance and extend too.
*   **BAD:** if you are using `setup.py` to build extensions but you don’t understand `setup.py` runs _outside_ of any installed packages, you are creating software uninstallable in the modern python ecosystem. If you are doing “system tests” for installed packages before installing your own packages, logic is corrupt and you need to fix it (looking at you, poorly maintained [detectron2](https://github.com/facebookresearch/detectron2/blob/main/setup.py) and [flash-attention](https://github.com/Dao-AILab/flash-attention/blob/main/setup.py) install logic)

Better Practices
----------------

Basic template for a modern python project:

*   All python projects must use a [`pyproject.toml` file](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) for declaring all aspects of the local package.
*   Each single-purpose repository should have only one `pyproject.toml` file at the top level.
*   All python package code goes in a directory for your package name (sometimes called _stuttering_ since your package directory will often just be your repo name again like `packagename/packagename`)
*   So your directory structure looks like:
    *   `project_name/`
        *   `pyproject.toml`
        *   `project_name/__init__.py`

[Using `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) lets us define dependencies in a more reliable fashion than the outdated legacy ways of `requirements.txt` / `setup.py` / `setup.cfg`. Writing all your metadata parameters in `pyproject.toml` is much cleaner and much better defined than metadata just being parameters to setup functions.

For creating and managing `pyproject.toml`, the best tool is currently [Poetry](https://github.com/python-poetry/poetry). Poetry includes typical features you’d expect such as versioned dependency resolution (without the broken dependency performance of previous python dependency managers) and automatic virtual environment management and automatic package building/uploading and automatic command running too.

Here’s a quick buhbample:

### Use the poetry `init` wizard for creating your defaults

Also notice how your package now depends on a python version too (which will need to be adjusted forward in time as versions grow unless you relax the restriction here, but may dependencies will also require you have a narrow range of acceptable python versions.).

One missing feature of the python/poetry setup environment though: poetry doesn’t let you define which _poetry_ versions are allowed to operate with your `pyproject.toml` file, so sometimes poetry will add or remove features in newer `poetry` versions and you have outdated syntax in your project files, but there’s no way to tell your project files which poetry versions are acceptable.

### Add your initial dependencies

As one would expect from modern tools, the dependency manager automatically pulls deps in a reasonably performant manner and generates a hash-defined lockfile (though, there’s been a poetry bug (skill issue) for a while where sometimes you need to force-delete your local package cache if installs get stuck resolving dependencies via `poetry cache clear pypi --all`).

### Look at your dependency graph _(look at it!)_

and it’s useful to view your dependency tree especially in larger projects when you get a security alert how Version X.Y.Z.Q.M has A SINGLE INVALID QUATARI CERTIFICATE AND NOW MUST BE FIXED GLOBALLY TO Version X.Y.Z.Q.M+1 but you’re not sure how many packages it may impact.

A proper dependency tree is the core of all modern software development and legacy methods of `requirements.txt` or `setup.py / setup.cfg` package specifications do not ensure cross-package version compatibility, which is why we need `poetry` to handle all our dependency logic in a single consistent well-behaved source of truth operating environment.

Living with `pyproject.toml`
----------------------------

But what about most common people who are copy-paste-by-example developers and just use the same `pip install -r requirements.txt` pattern everywhere because they read it on a forum somewhere in 2012 and never looked up anything again?

You never need to invoke `pip install` anywhere except for your initial global `pip install pip poetry wheel setuptools -U` because all other packages and projects are managed in your poetry-controlled virtual environments.

Technically you _can_ look inside your poetry-managed virtual environment with `poetry shell` or even `poetry run python` or `poetry run pip` — but it’s a big anti-pattern to poke the venv [python environment](https://www.youtube.com/shorts/ZEw4HakhRoI) directly unless you are performing extreme debugging operations. Your `pyproject.toml` file should be configured to [run all entry points to your package using auto-generated scripts logic](https://matt.sh/python-project-structure-2024#_poetry-script-entry-point-management-excellence).

The largest problem with `pyproject.toml` is all the outdated online forum posts telling people to just `install -r requirements.txt` when you should never be generating a `requirements.txt` anymore in the first place.

So, anyway, to contribute to the discourse arena, here’s a simple modern non-legacy example of a (ugh) docker (ugh) setup using no `requirements.txt` at all:

Using this pattern you are, yes, creating a virtualenv in your docker image and using it, but LOOK HOW CLEAN IT IS. You ARE NOT generating a redundant and potentially out-of-sync `requirements.txt` file; you are using your built-in tooling as expected without any extra weird workarounds and all your expectations play out without any additional mental indirection across incompatible tool usage. nobody likes incompatible tools.

**FREE TIP**: did you know `Dockerfile` is actually a file extension? So you should name things like `hello.Dockerfile` and not `helloDockerfile` or `Dockerfile.hello`. _the more you know_

Poetry Script Entry Point Management Excellence
-----------------------------------------------

Perhaps the most practical day-to-day feature of poetry is its nice ability to automatically generate global python commands from a simple one line `package.module:function` declaration.

### le example

Let’s make a simple web fetcher nicely encapsulated in a dataclass so we can run it all via a CLI.

#### creating `hello/entrypoint.py`

Pretty simple, right? We have a dataclass with one required parameter `url` and the other instance variables all have defaults so the user doesn’t need to provide values for them.

But how do we run this? If you were using legacy outdated python logic, you’d bring out more _dunders_ with something like `if __name__ == "__main__": Fetcher(*sys.argv[1:]).fetch()`.

But we can also just use `fire.Fire` (or even `jsonargparse`) and it automatically generates a full CLI from the class parameters itself.

Instead of adding the name-main _dunder_, we create a proper command entrypoint where it will auto-detect required parameters just from the class definition and allow us to run any methods declared on the class:

#### appending to `hello/entrypoint.py`

Now we tell poetry where to find the `cmd()` top-level function by adding this to our `pyproject.toml`:

#### updating `pyproject.toml`

Now we just run it via:

#### running examples

and it worked! Except we didn’t actually run it yet. We can run it too:

Here’s an example of the output using `jsonargparse` instead of `fire.Fire` too:

How to decide between `fire.Fire` or `jsonargparse.CLI`? If you only have a simple interface with a couple parameters and a couple commands, `fire.Fire` is easy to run and is flexible if you want to be lazy (`fire.Fire` parses _inputs_ to types, but not the _declared code_ types, so it’s more likely to work for any input even if your code types aren’t perfect), while `jsonargparse` allows inputs to be fully defined nested objects if you want to have more complex inputs (like inputs being other nested dataclasses of their own fields to create) and `jsonargparse` will validate types of all fields from your class definitions from either CLI or config file input. basically, `fire.Fire` is good for being being quick and lazy (it also supports nice [pipeline workflow systems](https://google.github.io/python-fire/guide/#grouping-commands)); `jsonargparse.CLI` is good for more complex and more long-lived systems. Also note in our example above, `fire.Fire` generated config params for all instance variables while `jsonargparse.CLI` properly ignored our `init=False` fields since users shouldn’t be editing those values anyway.

so there’s one example of running a fully modern `pyproject.toml` + `poetry` + good class layout + auto-generated-CLI system. Everything you create should have a structure very similar to the format above for basic interactive tools or any systems requiring the ability for users to _run_ some part of your project (i.e. it’s not “just a library” somebody else is importing).

Conclusion
----------

i dunno. do good work i guess?

also it helps to read your primary language API docs front-to-back at least once per year.

the modern tech landscape is a huge mess. few people seem to care about proper tooling and performance and code structure and logical encapsulation anymore. it seems 80% of the industry is now comprised of “16 layers of abstraction API glue developers” where everything is implemented by barely understanding how anything works but trying to generate massive amounts of output anyway (while the other 20% of the developer census are celebrity developers all on immortal 8 figure yearly comp packages apparently).

The modern practice of high margin “cloud-native, sass-native, product-first, zero-architecture, zero-infrastructure, full-marketing, full-sales, minimal-development, minimal-creative-effort-because-thinking-isnt-shipping” companies out there has now broken one or two developer generations into just being full time copy/paste developers. Who has time to do the proper “deep work” of understanding how all 74 parts of our modern architecture works? YOU HAVE TO SCRUM THE AGILE VELOCITY POINTS! If you can’t steal open source work for free, you buy a sass version, and if you can’t steal pre-existing libraries from individuals on github, then we DO NOT DO IT because THE PRODUCT VELOCITY MUST ALWAYS INCREASE. and your _“education”_ or _“learning”_ or _“expertise”_ is NOT INCREASING OUR HIGH MARGIN DEVELOPER VELOCITY WE WILL OUTSOURCE YOUR ROLE TO MONGOLIA YOU OVERPAID ENTITLED AMERICAN SHIT (just some feedback from a recent job life is fun).

so we are stuck in an industry death spiral where an untouchable developer priest class of prommie architects continue to create more complicated frameworks everybody else just copy/pastes solutions into while AWS reaps their legally mandated 10,000% markup on compute and networking due to a perfect balance of exponentially growing systems ignorance (you would never _buy a server_ would you??!?! are you some server commie bastard? you must only pay AWS or YOUR ENTIRE COMPANY WILL DIE FROM SYSADMIN COSTS!!!) combined with exponentially degrading performance and data inefficiencies throughout the entire body software. my laptop has 10 5 GHz cores and I have a 5 Gbps wired ISP connection but all webpages still take 15 seconds to load text only interfaces because every webpage contacts 40 external high latency domains for “personalized marketing research purposes.” great job everybody.

sometimes you have to stop though. sometimes you actually have to learn something more than one [level deep](https://www.youtube.com/watch?v=k01y9cVWYks&list=PLYjGzYXYjSsZ1mj05ZX-IFJOac62W6LQZ&index=26). sometimes you have to enhance the world model inside your brain by understanding how systems work from electrons to bits to photons and back. who else is doing the work if not us, the ones charged with creating the future in the first place? oh, sorry, no time to do meaningful growth work because the sass scrum velocity is down six poker points this sprint so back to lighting up the burndown chart with react hooks before the next 8am status meeting.

dawn your peepers on some of these fun adventures in hiring i’ve had recently:

*   rejected in interviews by a 25 year old senior hiring manager
*   rejected in interviews by a 28-something who had worked at google for 5 years and had a PhD from stanford
*   rejected for arguing, _akshually_, i made more 10 years ago than what your scale is rated at
*   rejected by some founders who got rich by selling an ios fart app to apple ten years ago
*   rejected via HR/email/auto-reject a couple places

at least nobody has ever accused me of not being sufficiently candid.

i mean, sure, i’m a useless piece of garbage. what value could i possibly create since i didn’t go to stanford and haven’t worked at google for 5+ years and don’t have a PhD in the certainly not purely imaginary field of “alignment?” just throw me in the acme wood chipper already.

remember a couple years ago when all the CEOs were saying “yeah, nobody needs a CS degree anymore, you can just learn it all online by watching 3,000 videos!” but then, AI development happens, and now every company is saying “[we only hire 28 year old Stanford PhDs](https://matt.sh/tech-terms#_section) who have worked at google for 5 years” so anybody with more than 5 years of non-google real-world is suddenly just told to rot? I’m pretty sure long-term stable development requires a decade or more of continuous growth and experience in production systems, but somehow teenagers in palo alto (heh, palo algo) are more in demand than people who helped build the structure of the internet we have today (the good parts, like fast networking and scalable services and high performance servers, not the shit parts like search results flooded with a million adsense-powered algo-generated spam sites). anyway, guess all those 37 year old billionaires in the 600 person 30-under-30 list know what is best for the world and the next trillion year future of humanity, so we must abide by the market declaring us incompetent.

cheer up, it’s [only getting worse](https://www.youtube.com/watch?v=2wca6J0xqtY&list=PLdkdX9a8ac9StGfVV72Z9qZDGOQTziwX1&index=2).

Bonus: Legacy Outdated Python Usage Warning Signs
-------------------------------------------------

Other signs your python knowledge is outdated or you only learned from online spam tutorials without reading platform updates over the past 5+ years:

*   **BAD**: you use anything is the `os.path` namespace. You should only use the much nicer `from path import Path` namespace for file introspection.
*   **BAD**: you manually create CLI structures with `argparse` or `click`. All your CLI interaction should be generated from [`fire.Fire`](https://github.com/google/python-fire) for simple interfaces or [jsonargparse](https://jsonargparse.readthedocs.io/en/stable/) for more complex interfaces (`jsonargparse` also includes a built-in config file parser just from your project structure, which you’ll find familiar if you’ve used the [pytorch lightning config syntax](https://lightning.ai/docs/pytorch/stable/cli/lightning_cli_advanced.html) before)
*   **BAD**: you aren’t using a nice time wrapper. `Arrow` or `pendulum` often provide nicer interfaces than python’s built-in poorly named `from datetime import datetime` system.
*   **BAD**: mega red flag: you manually configure `PYTHONPATH` anywhere. Manually setting `PYTHONPATH` shows you don’t understand the basic operations of python module path logic (which, we must admit _is_ confusing by itself), but using `pyproject.toml` with `poetry` to manage your dependencies and environments means you should _never_ use `PYTHONPATH` ever again.
*   **BAD**: you don’t realize `List[]` and `Tuple[]` and `Set[]` and `Optional[]` are deprecated in favor of just `list[]`, `tuple[]`, `set[]`, `deque[]`, `x | None` typing annotations (it is also difficult to teach current code LLMs to stop outputting legacy type annotations though).
*   **BAD**: your python version is more than 1 version old. As of this writing, you are allowed to use Python 3.11+ and Python 3.12+. If you are still creating new systems targeting older versions, STOP IT. JOIN THE FUTURE. if you are “stuck” on your current version because your “system python” isn’t updated, you should be using [pyenv](https://github.com/pyenv/pyenv) so _you_ control your language version directly.
*   **BAD**: not using a standard code formatter: pick one or more of `black`, `ufmt` (groups/sorts imports too), `ruff format`
*   **BAD**: using “anaconda” or “conda” for _anything_ — those are just crutches for people who don’t know how to install their own packages, but if you can’t even install a package, you need to just learn more instead of operating at borderline-incompetent levels of understanding in your professional work.
*   **BAD**: reliance on jupyter interfaces for much of anything. just be a real grown up human developer and create reusable interactive systems instead of buggy sprawling low quality “notebooks” everywhere.
*   **BAD**: you aren’t using `@dataclass` everywhere. You should _never_ write `def __init__(self, ...) -> None:` ever again. [dataclasses](https://docs.python.org/3/library/dataclasses.html) allow you to define your instance variables _once_ then a constructor is auto-generated and you can hook into them with `def __post_init__(self) -> None:` but basically every python class should be a `dataclass` going forward with no exceptions (only exception maybe if you need to inherit from a non-dataclass, but even such cases can be worked around too where a dataclass inherits from a non-dataclass even if you have to annotate with `@dataclass(unsafe_hash=True)` (using said trick you can create dataclasses inheriting from `nn.Module` for a very clean system) or something else fun).
*   **BAD**: you use the built-in python `logging` module. It is a complete disaster of an API. You should use [`loguru`](https://loguru.readthedocs.io/en/stable/) everywhere instead.
*   **BAD**: you write too much top-level code instead of behaviors being nicely encapsulated in self-contained dataclass components. python sadly encourages a lot of top-level unstructured code like how flask and fastapi expect to use a global object as their root decorator source, but this can be worked around with a couple clever levels of nesting using instance variables and closures.
*   **BAD**: here’s a fun minor nit: you should never use an in-line generator because it is _always_ faster to use a list comprehension instead: `max(x + 3 for x in range(100))` is always slower than `max([x + 3 for x in range(100)])` because, unless your source is _truly_ infinite or _truly_ generated-per-call, collecting and iterating a list is faster than building and running the generator state management logic on every call (plus, using inline generators introduces an entire class of bugs where you forget it’s a generator and you iterate it _twice_, but the second time, it had _already fully generated all the data_ and then returns _nothing_ instead of your data even though it “looks right” because you didn’t think it through abstractly enough.)
*   **BAD**: general unawareness or lack of experience using [built-in features](https://xkcd.com/353/) from things like [collections](https://docs.python.org/3/library/collections.html) and [itertools](https://docs.python.org/3/library/itertools.html) or even helpful wrappers like [more-itertools](https://more-itertools.readthedocs.io/en/stable/) and [boltons](https://boltons.readthedocs.io/en/latest/) and standard useful things like [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/) and [diskcache](https://grantjenks.com/docs/diskcache/) and [peewee minimal orm](http://docs.peewee-orm.com/en/latest/) and [httpx](https://www.python-httpx.org/) and [loguru](https://loguru.readthedocs.io/en/stable/overview.html) and [orjson](https://github.com/ijl/orjson) (at least if you aren’t using pypy) — many of those tools and APIs require actual practice/play/experience to remember when it’s appropriate to use them since they are often higher order abstractions which don’t feel intuitive until you’ve learned to think in more advanced data processing logic.
*   **OPTIONAL:** using type checkers and/or linters via `mypy` or `ruff` too — depending on the size of your project and its purpose/complexity/cost/value, sometimes it isn’t worth spending an extra couple days or weeks tracking down all the proper types (especially if you are returning instances of classes with poorly defined types you have to code dive to find manually), but it’s always best if you _can_ pass mypy strict just for peace of mind during updates and refactors. also, at least attempting proper type annotation everywhere feasible helps you write more self-documenting code and continually reflect on the appropriate use cases and structure of input types and response values (also, declaring type annotations on parameters helps you notice when maybe you are generating too many ad-hoc data structures via nested list/dicts/sets where instead you should be passing around better structured single-purpose encapsulated dataclasses, etc).
*   contribute your own [bugbear](mailto:bugbear@matt.sh) here!

if you’ve made it this far, i’m still soliciting [ai indulgences](https://matt.sh/ai-indulgence) for yourself and everyone you know (buy now before rates go up again in another step function!). also I still have some domains for sale as well if you have more money than sense: [make.ai](https://make.ai/) and [god.ai](https://god.ai/) are currently ready and waiting to live their best lives with you as soon as possible for the low low price of millions of dollars direct from you to me.
