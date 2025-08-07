Title: We shouldn’t have needed lockfiles

URL Source: https://tonsky.me/blog/lockfiles/

Published Time: 2025-08-06

Markdown Content:
Imagine you’re writing a project and need a library. Let’s call it `libpupa`.

You look up its current version, which is `1.2.3`, and add it to your dependencies:

`"libpupa": "1.2.3"`
In turn, the developer of `libpupa`, when writing its version `1.2.3`, needed another library: `liblupa`.

So they did the same thing: they looked up the version, which was `0.7.8` at the time, and added it to the dependencies of `libpupa 1.2.3`:

`"liblupa": "0.7.8"`
The version `0.7.8` of `liblupa` is immortalized forever in the dependencies of `libpupa 1.2.3`. No matter how many other versions of either `liblupa` or `libpupa` are released, `libpupa 1.2.3` will always depend on `liblupa 0.7.8`.

Our dependency resolution algorithm thus is like this:

*   Get the top-level dependency versions
*   Look up versions of libraries they depend on
*   Look up versions of libraries they depend on
*   ...

The important point of this algorithm is that it’s fully deterministic. Given just the top-level dependencies, it will produce the entire dependency tree, identical every time.

It’s also space-efficient: you don’t need to specify all the versions, just the top-level ones. Given `libpupa 1.2.3`, we will always arrive at `liblupa 0.7.8`. So why write it down in a separate file?

And that’s it. End of story. Write down your top-level dependencies. The computer will figure out transitive ones. They are guaranteed to be the same, since everything is immutable. The sun is shining, the grass is green, and builds are fully reproducible.

But people had to invent lockfiles.

Imagine you voluntarily made your build non-reproducible by making them depend on time. If I build my app now, I get `libpupa 1.2.3` and `liblupa 0.7.8`. If I repeat the same build in 10 minutes, I’ll get `liblupa 0.7.9`. Crazy, right? That would be chaos.

But this is what version ranges essentially are. Instead of saying “`libpupa 1.2.3` depends on `liblupa 0.7.8`”, they are saying “`libpupa 1.2.3` depends on whatever the latest `liblupa` version is at the time of the build.”

Notice that this is determined not at the time of publishing, but at the time of the build! If the author of `libpupa` has published `1.2.3` a year ago and I’m pulling it now, I might be using a `liblupa` version that didn’t even exist at the time of publishing!

But... why would `libpupa`’s author write a version range that includes versions that don’t exist yet? How could they know that `liblupa 0.7.9`, whenever it will be released, will continue to work with `libpupa`? Surely they can’t see the future? Semantic versioning is a hint, but it has never been a guarantee.

For that, kids, I have no good answer.

The funny thing is, these version ranges end up not being used anyway. You lock your dependencies once in a lockfile and they stay there, unchanged. _You don’t even get the good part!_

I guess, builds that depend on the calendar date are too crazy even for people who believe that referencing non-existing versions is fine.

“But Niki, you can regenerate the lockfile and pull in all the new dependencies!”

Sure. In exactly the same way you can update your top-level dependencies.

“But Niki, lockfiles help resolve version conflicts!”

In what way? Version conflicts don’t happen because of what’s written in dependency files. Your library might work with the newer dependency, or it might not. It doesn’t really depend on what the library’s author has guessed.

Your library might have a version range of `0.7.*`, work with `0.7.8`, `0.7.9` but not with `0.7.10`. Either way, the solution is the same: you have to pick the version that works. And the fact that someone somewhere long time ago wrote `0.7.*` doesn’t really help you.

“But Niki, if lockfiles exist, there must be a reason! People can’t be doing it for nothing!”

You are new in IT, I see. People absolutely can and do things here for no good reason all the time.

But if you want an existence proof: Maven. The Java library ecosystem has been going strong for 20 years, and during that time not once have we needed a lockfile. And we are pulling hundreds of libraries just to log two lines of text, so it is actively used at scale.

In conclusion, lockfiles are an absolutely unnecessary concept that complicates things without a good reason. Dependency managers can and are working without it just the same.

UPD: Reading comments, I see that I missed a part of version resolution that is important. In Maven, if you have conflicting transitive dependencies, the version that will picked is the version closest to the root. E.g.:

```
My app
├╴a 1.0
│ └╴ d 1.0
└╴b 1.0
  └╴c 2.0
    └╴ d 2.0
```

In this case, `d 1.0` will be picked. This is still deterministic, but it lets you override versions when needed. For example, if `d 2.1` is released with security patches, you can always add it to the root and that’s the version that will be picked:

```
My app
├╴a 1.0
│ └╴d 1.0   x-- ignored
├╴b 1.0
│ └╴c 2.0
│   └╴d 2.0 x-- ignored
└╴d 2.1     <-- picked
```

No need to wait for the whole world to update. Still deterministic. Still no lockfiles.

Why not pick the biggest version? Then you’ll lose the ability to override.