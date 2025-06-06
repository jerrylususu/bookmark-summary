Title: How Imports Work in RSC — overreacted

URL Source: https://overreacted.io/how-imports-work-in-rsc/

Markdown Content:
React Server Components (RSC) is a programming paradigm that lets you express a client/server application as a single program spanning over two environments. Concretely, RSC extends the module system (the `import` and `export` keywords) with novel semantics that let the developer control the frontend/backend split.

I’ve [previously written](https://overreacted.io/what-does-use-client-do/) about the `'use client'` and `'use server'` directives which mark the “split points” between the two environments. In this post, I’d like to focus on _how_ these directives interact with the `import` and `export` keywords.

This post is a deep dive for anyone who’d like to build an accurate mental model of RSC, as well as for folks who are interested in module systems in general. You might find the RSC approach both surprising _and_ simpler than you might think.

As usual, 90% of this article won’t be _about_ RSC. It’s about how imports work in general, and what happens when we try to share code between the backend and the frontend. My aim is to show how RSC provides a natural solution to the last 10% of tensions that arise when we write code spanning both sides of the wire.

Let’s start with the fundamentals.

* * *

### [What’s a Module System?](https://overreacted.io/how-imports-work-in-rsc/#whats-a-module-system)

When a computer executes a program, it doesn’t need “modules”. The computer needs the program’s code and data to be _fully loaded in memory_ before it can run and process them. It’s actually _us humans_ who want to split code into modules:

*   Modules let us break complex programs into parts that can fit into our brains.
*   Modules let us constrain which lines of code are meant to be visible (or _exported_) to other parts of the code, and which should remain an implementation detail.
*   Modules let us reuse code written by other humans (and by ourselves).

**We want to _author_ our programs as split into parts—but _executing_ a program involves “unrolling” those parts in memory. The job of a module system is to bridge the gap between how humans write code and how computers execute it.**

Concretely, a _module system_ is a set of rules that specify how a program can be split into files, how the developer controls which parts can “see” which other parts, and how those parts get linked into a single program that can be loaded in memory.

In JavaScript, the module system is exposed via `import` and `export` keywords.

* * *

### [Imports Are Like Copy and Paste…](https://overreacted.io/how-imports-work-in-rsc/#imports-are-like-copy-and-paste)

Consider these two files, which we’ll call `a.js` and `b.js`:

```
export function a() {
  return 2;
}
```

```
export function b() {
  return 2;
}
```

By themselves, they don’t do anything except defining some functions.

Now consider this file called `index.js`:

```
import { a } from './a.js';
import { b } from './b.js';
 
const result = a() + b(); // 4
console.log(result);
```

Now, that’s a module that ties them together into a single program!

The rules of the JavaScript module system are complex. There are many intricacies to how it works. But there’s a simple intuition we can use. The JavaScript module system is designed to ensure that **by the time the program above runs, it should behave identically to this single-file program** (which doesn’t use modules at all):

```
function a() {
  return 2;
}
 
function b() {
  return 2;
}
 
const result = a() + b(); // 4
console.log(result);
```

In other words, the `import` and `export` keywords are **designed to work in a way that’s reminiscent of copying and pasting**—because ultimately, in the end, the program _does_ need to be “unrolled” in the process’s memory by the JS engine.

* * *

### […Except They’re Not](https://overreacted.io/how-imports-work-in-rsc/#except-theyre-not)

Earlier I said imports are like copy and paste. That’s not _exactly_ true. To see why, it’s intructive to take a trip down the memory lane to the `#include` directive in C.

The `#include` directive, which predates the JavaScript `import` by about 40 years, behaved [quite literally like copy and paste](https://stackoverflow.com/a/5735389/458193)! For example, here’s a C program:

```
#include "a.h"
#include "b.h"
 
int main() {
  return a() + b();
}
```

In C, the `#include` directive would **literally embed the entire contents** of `a.h` and `b.h` into the file above. This behavior is simple, but it has two big downsides:

1.   One problem with `#include` is that [unrelated functions from different files would clash](https://softwareengineering.stackexchange.com/a/202156/3939) if their names were the same. That’s something we take for granted with modern module systems, where all identifiers are local to the file they’re in.
2.   Another problem with `#include` is that the same file could get “included” from several places—and thus get repeated in the output program many times! To work around this, the best practice was to surround the contents of each file you want to be “includable” with a [build-time “skip including me if you already included me”](https://stackoverflow.com/a/12928949/458193) guard. Modern module systems, like `import`, do something similar automatically.

Let’s unpack that last point because it’s important.

* * *

### [JavaScript Modules Are Singletons](https://overreacted.io/how-imports-work-in-rsc/#javascript-modules-are-singletons)

Suppose we’ve added a new module called `c.js` that looks like this:

```
export function c() {
  return 2;
}
```

Now suppose that we’ve rewritten both `a.js` and `b.js` so that _each of them_ imports the `c` function from the `c.js` file and does something with it:

```
import { c } from './c.js';
 
export function a() {
  return c() * 2;
}
```

```
import { c } from './c.js';
 
export function b() {
  return c() * 3;
}
```

If `import` was literally copy-and-paste (like `#include`), we’d end up with two copies of the `c` function in our program. But thankfully, that’s not what happens!

The JavaScript module system ensures that the code above, along with `index.js` file from earlier, is equivalent in its semantics to the single-file program below. **Notice how the `c` function is defined once despite having been imported twice:**

```
function c() {
  return 2;
}
 
function a() {
  return c() * 2;
}
 
function b() {
  return c() * 3;
}
 
const result = a() + b(); // (2 * 2) + (2 * 3) = 10
console.log(result);
```

In other words, modern module systems, such as the JavaScript module system, guarantee that **the code inside each individual module executes _at most once,_** no matter how many times and from how many places that module gets imported.

This is a crucial design choice that enables many advantages:

*   When the code is turned into a single program (whether as an executable, as a bundle, or in-memory), the output size does not “explode” from repetition.
*   Each module can keep some “private state” in top-level variables and be sure that it’s retained (and not recreated) no matter how many times it got imported.
*   The mental model is dramatically simpler because each module is a “singleton”. If you want some code to only execute once, write it at the top level of its module.

Under the hood, module systems usually do this by holding a `Map` that keeps track of which modules (keyed by their filename) have already been loaded, and what their exported values are. Any JS `import` implementation will have this logic _somewhere,_ for example: [Node.js source](https://github.com/nodejs/node/blob/ed2c6965d2f901f3c786f9d24bcd57b2cd523611/lib/internal/modules/esm/loader.js#L114-L139), [webpack source](https://github.com/webpack/webpack/blob/19ca74127f7668aaf60d59f4af8fcaee7924541a/lib/javascript/JavascriptModulesPlugin.js#L1435-L1446), [Metro (RN) source](https://github.com/facebook/metro/blob/15fef8ebcf5ae0a13e7f0925a22d4211dde95e02/packages/metro-runtime/src/polyfills/require.js#L204-L209).

Let’s repeat that: each JavaScript module is a singleton. Importing the same module twice will not execute its code twice. Every module runs at most once.

We’ve talked about _multiple modules,_ but what about _multiple computers?_

* * *

### [One Program, One Computer](https://overreacted.io/how-imports-work-in-rsc/#one-program-one-computer)

Most JavaScript programs are written for a single computer.

That could be the browser, or a Node.js server, or some exotic JavaScript runtime. Still, I think it’s safe to say **the majority of JS programs are written for a single machine to execute.** The program is loaded, the program runs, the program stops.

The JavaScript module system, as described earlier, was designed to support exactly this most common use case. Here’s one last recap of how it works:

1.   There’s some file that acts as an _entry point_ into our program. In our earlier example, that was `index.js`. This is where the JavaScript engine starts.
2.   This file may import other modules, like `a.js` or `b.js`, which themselves can import more modules. The JavaScript engine executes the code of those modules. It also stores the exports of each module in an in-memory cache for later.
3.   If the JavaScript engine sees an `import` to a module it has _already loaded_ (such as the second import to `c.js`), it’s not going to run the module again. Modules are singletons! Instead, it will read that module’s exports from an in-memory cache.

Ultimately, it’s convenient to think of the end result as being similar to copy-pasting the modules into one file, surgically renaming any clashing variables, and ensuring that the contents of each individual module is only ever included once:

```
/* c.js */ function c() { return 2; }
/* a.js */ function a() { return c() * 2; }
/* b.js */ function b() { return c() * 3; }
 
const result = a() + b(); // (2 * 2) + (2 * 3) = 10
console.log(result);
```

In that sense, when you `import` some code, you bring it _into_ your program.

But what if we want to write _both our backend and frontend_ in JavaScript? (Or, alternatively, what if we realize that adding a [JS BFF can make our app better?](https://overreacted.io/jsx-over-the-wire/#backend-for-frontend))

* * *

### [Two Programs, Two Computers](https://overreacted.io/how-imports-work-in-rsc/#two-programs-two-computers)

Traditionally, a frontend and a backend in JS means that we’re working on two different programs that run on two different computers. In many cases, they might even be maintained by two different teams that barely talk to each other.

Let’s take a closer look at both of these programs. The _backend_ is responsible for serving an HTML page (and potentially some APIs for more data-intensive apps). The _frontend_ is responsible for pieces of the interactive logic on that HTML page.

The backend code might live in `backend/index.js`:

```
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

The frontend code might live in `frontend/index.js`:

```
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Let’s put them close to emphasize these are two different but related programs:

```
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Now let’s see what happens when we import something from either side.

Suppose we import `a.js` and `b.js` from `backend/index.js`:

```
import { a } from '../a.js';
import { b } from '../b.js';
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Importing them _from_ the backend code would bring them _into_ the backend code:

```
/* c.js */ function c() { return 2; }
/* a.js */ function a() { return c() * 2; }
/* b.js */ function b() { return c() * 3; }
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Now suppose that we _also_ import them from `frontend/index.js`:

```
import { a } from '../a.js';
import { b } from '../b.js';
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
import { a } from '../a.js';
import { b } from '../b.js';
 
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Importing them _from_ the frontend code brings them _into_ the frontend code:

```
/* c.js */ function c() { return 2; }
/* a.js */ function a() { return c() * 2; }
/* b.js */ function b() { return c() * 3; }
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
/* c.js */ function c() { return 2; }
/* a.js */ function a() { return c() * 2; }
/* b.js */ function b() { return c() * 3; }
 
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Notice how the frontend and the backend don’t share the module system!

That’s an important insight. Importing code _from_ either side brings that code _into_ that side—nothing more. The two sides have two _independent_ module systems. Modules still act like singletons—but they are only _singletons per environment._

Although we are _reusing_ the `a.js`, `b.js`, and `c.js` implementations between both sides, it would be more accurate to think that both the backend code and the frontend sides have “their own versions” of the `a.js`, `b.js`, and `c.js` modules.

So far, there’s nothing unusual about what I’ve described. It’s how sharing code between the backend and the frontend has always worked in full-stack apps. However, as more of our code gets reused between the environments, we’re risking accidentally reusing something that’s _not meant_ for the other side.

How can we constrain and control code reuse?

* * *

### [Build Failures Are Actually Good](https://overreacted.io/how-imports-work-in-rsc/#build-failures-are-actually-good)

Suppose that somebody edits `c.js` to include some code that _only_ makes sense on the backend. For example, imagine that we use `fs` to read a file on the server:

```
import { readFileSync } from 'fs';
 
export function c() {
  return Number(readFileSync('./number.txt', 'utf8'));
}
```

This would not cause problems for the backend code:

```
/* fs.js */ function readFileSync() { /* ... */}
/* c.js */  function c() { return Number(readFileSync('./number.txt', 'utf8')); }
/* a.js */  function a() { return c() * 2; }
/* b.js */  function b() { return c() * 3; }
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

However, it would fail the frontend build because `fs` does not exist there:

```
import { readFileSync } from 'fs'; // 🔴 Build error: Cannot import 'fs'
/* c.js */ function c() { return Number(readFileSync('./number.txt', 'utf8')); }
/* a.js */ function a() { return c() * 2; }
/* b.js */ function b() { return c() * 3; }
 
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

And this is actually good!

When we start reusing code between the two sides, we want to have some confidence that the code we’re trying to reuse will _actually work_ on both sides.

If some APIs only make sense on one side (like `fs` only makes sense on the backend), we _want_ the build to fail early so that we can decide how to fix our code:

1.   We could choose to move the `fs` call somewhere other than `c.js`.
2.   We could refactor `a.js` and `b.js` to not need `c.js`.
3.   We could change `frontend/index.js` to not need `a.js` and `b.js`.

It’s important to note that **all of the above solutions are valid.** The solution you pick depends on what you’re actually trying to do. There is no automated way to pick “the best” solution—if anything, this is similar to resolving a real Git conflict. It’s not _fun_ to resolve but the behavior you want _is up to you (or an LLM) to decide._

This is the price you pay for reusing code. The benefit is that it’s easy to shift the logic around depending on which side needs it. The downside is that, when things blow up, you have to look at the build failure and _decide_ which module needs a fix.

In this case, we were lucky that importing something “on the wrong side” actually caused a build error. This let us immediately see the problem. But what if it didn’t?

* * *

### [Server-Only Code](https://overreacted.io/how-imports-work-in-rsc/#server-only-code)

Suppose that instead, somebody edits `c.js` to import a server-side secret.

```
import { secret } from './secrets.js';
 
export function c() {
  return secret;
}
```

This is much worse than the previous example! There would be no build failure, and the `secret` would become a part of both the backend _and_ the frontend code:

```
/* secrets.js */ const secret = 12345;
/* c.js */       function c() { return secret; }
/* a.js */       function a() { return c() * 2; }
/* b.js */       function b() { return c() * 3; }
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
/* secrets.js */ const secret = 12345;
/* c.js */       function c() { return secret; }
/* a.js */       function a() { return c() * 2; }
/* b.js */       function b() { return c() * 3; }
 
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

This is a nightmare scenario, but many fullstack apps don’t employ any protection against a developer accidentally pulling in secrets into the frontend code like this!

How could we improve on that?

Here’s one idea. In the previous section, we’ve seen that using `fs` from the frontend code failed the frontend build, forcing us to actually fix the problem.

That’s _exactly_ what we want to happen here, too!

**Suppose that we create a special package, which we’re going to call `server-only`, that serves as a _marker_ for code that must never reach the frontend.** By itself, that package will not contain any real code. It is a “poison pill”. We’ll teach our frontend bundler to _fail the build_ if this module gets into the frontend bundle.

Assuming we’ve done that, we can now mark `secrets.js` as server-only:

```
import 'server-only';
 
export const secret = 12345;
```

With this change, pulling `secrets.js` into the bundle fails the frontend build. Concretely, both `a.js` and `b.js` will bring `c.js`, which will bring `secrets.js`, which will bring `server-only`—and that’s the poison pill that fails the build:

```
/* server-only */ /* (This does nothing on the backend.) */
/* secrets.js */  const secret = 12345;
/* c.js */        function c() { return secret; }
/* a.js */        function a() { return c() * 2; }
/* b.js */        function b() { return c() * 3; }
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
/* server-only */ /* 🔴 (This fails the build on the frontend.) */
/* secrets.js */  const secret = 12345;
/* c.js */        function c() { return secret; }
/* a.js */        function a() { return c() * 2; }
/* b.js */        function b() { return c() * 3; }
 
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Now we can control which code is not allowed to escape the backend! (As a concrete implementation example, here’s the [related](https://github.com/vercel/next.js/blob/f684e973f1ddbbdc99cdda9a89070d6d228a1dd7/crates/next-custom-transforms/src/transforms/react_server_components.rs#L640)[logic](https://github.com/vercel/next.js/blob/f684e973f1ddbbdc99cdda9a89070d6d228a1dd7/crates/next-custom-transforms/src/transforms/react_server_components.rs#L772-L778) in the Next.js bundler.)

Like with the `fs` import earlier, we’d have different options to fix it:

1.   We could choose to move the `secrets.js` import somewhere other than `c.js`.
2.   We could refactor `a.js` and `b.js` to not need `c.js`.
3.   We could change `frontend/index.js` to not need `a.js` and `b.js`.

But the important part about this solution is that it _automatically propagates up the import chain_. You don’t need to mark individual files like `a.js`, `b.js`, and `c.js` as server-only unless there’s some specific reason _local to them_ that must prevent their inclusion. It’s enough to mark files that should _definitely_ not be included (like `secrets.js`), and then rely on the “poison pill” propagating up the import chain.

* * *

### [Client-Only Code](https://overreacted.io/how-imports-work-in-rsc/#client-only-code)

Similarly to the `server-only` “poison pill”, we can create a mirror twin `client-only` “poison pill” that fails the server-side build. (If you don’t bundle the server, you could instead run this check separately similar to running TypeScript.)

Suppose that we used a browser-specific API in `c.js`. This may be a decent reason for us to decide that it’s _never valid_ to pull it into the backend code:

```
import 'client-only';
 
export function c() {
  return Number(prompt('How old are you?'));
}
```

This is not as critical, but it helps discover mistakes more quickly. Our goal is to turn confusing _runtime_ errors that stem from importing code that wasn’t meant for the other side—like DOM logic—into _build_ errors that force us to fix it:

```
/* client-only */ /* 🔴 (This fails the build on the backend.) */
/* c.js */        function c() { return Number(prompt('How old are you?')); }
/* a.js */        function a() { return c() * 2; }
/* b.js */        function b() { return c() * 3; }
 
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
/* client-only */ /* (This does nothing on the frontend.) */
/* c.js */        function c() { return Number(prompt('How old are you?')); }
/* a.js */        function a() { return c() * 2; }
/* b.js */        function b() { return c() * 3; }
 
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

Again, this would present us with a choice:

1.   We could refactor `c.js` to work on the backend (and remove the poison pill).
2.   We could refactor `a.js` and `b.js` to not need `c.js`.
3.   We could change `backend/index.js` to not need `a.js` and `b.js`.

We could further envision a more granular version of `client-only` and `server-only` that applies to individual package imports. For example, the React package could declare APIs like `useState` and `useEffect` to be `client-only` so that pulling them into the backend code immediately fails the build. (Hint: React actually _does_ do that via the [`package.json` Conditional Exports](https://nodejs.org/api/packages.html#conditional-exports) mechanism.)

I suspect you’re starting to see a theme here. As we move to share and reuse more code between the backend and frontend codebases—and indeed, as these two codebases blend into one—these build-time assertions give us a peace of mind.

Not every module _needs_ to be exclusive to some side. In fact, most modules don’t care because they aren’t the _source_ of incompatibilities. For example, `a.js` and `b.js` don’t prescribe that they must only exist on one side because they _don’t know_ the implementation details of `c.js.` But if some module _does_ care to be exclusive, it can now express this “locally” with `server-only` or `client-only`. The declared incompatibility then transitively “infects” every importing module.

It is also crucial to understand that the `server-only` and `client-only` “poison pills” do not _control_ where the code goes. They don’t “put” the code “on the backend” or “on the frontend”. The only thing these assertions do is _prevent_ code from being pulled into an unsupported environment. They’re poison pills _only._

By this point, we’ve almost invented RSC.

There’s just one last detail left.

* * *

### [One Program, Two Computers](https://overreacted.io/how-imports-work-in-rsc/#one-program-two-computers)

Let’s have one more look at our backend and our frontend as separate programs:

```
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

By now, we have a good mental model for how these programs can share code:

*   Importing code _from_ either side always bring it _into_ that side.
*   The two module systems remain completely independent. If you import some shared code from _both_ sides, it will be independently brought _into_ both sides.
*   By default, we assume that any code is reusable. But we provide `server-only` and `client-only` poison pills that should be used in modules that _should never get brought into_ a particular side due to some code _directly inside of_ those modules. This doesn’t change how or where the code _runs,_ but it gives us early build errors.

Honestly, we could stop here, and we’d have a compelling setup for full-stack development that provides safer code reuse than many popular setups.

However, there’s one remaining weakness in our approach. Currently, the backend code and the frontend code rely on _convention_ to stay in sync. The backend wants to _refer_ to the `sayHello` function from the frontend, but there’s no way to do it syntactically so it has to resort to _assuming_ that it will exist on the other side:

```
function server() {
  return (
    `<html>
      <body>
        <button onClick="sayHello()">
          Press me
        </button>
        <script src="/frontend/index.js type="module"></script>
      </body>
    </html>`
  );
}
```

```
function sayHello() {
  alert('Hi!');
}
 
window['sayHello'] = sayHello;
```

This is kind of fragile.

Of course, the backend couldn’t _just import_`sayHello`, for—as an observant reader might already realize—that would just bring it _into_ the backend code.

It would be nice if there was some way for the backend code to _refer_ to `sayHello` without bringing it _into_ the backend. Luckily, that is what [`'use client'` does](https://overreacted.io/what-does-use-client-do/):

```
import { sayHello } from '../frontend/index.js';
 
function Server() {
  return (
    <html>
      <body>
        <button onClick={sayHello}>
          Press me
        </button>
      </body>
    </html>
  );
}
```

```
'use client';
 
export function sayHello() {
  alert('Hi.');
}
```

That’s the “remaining 10%” that RSC adds.

In RSC, imports on both sides normally _work like regular imports_—but `'use client'` changes this behavior to “opening a door” to the frontend environment.

When you add `'use client'`, you’re saying: “If you import me from the backend world, don’t actually bring my code _into_ the backend—instead, provide a reference that React can turn eventually into a `<script>` tag and revive on the frontend.”

Likewise, [`'use server'`](https://overreacted.io/what-does-use-client-do/#use-server) lets a piece of the frontend code “open the door” to the backend and _refer_ to a backend module _without_ bringing it _into_ the frontend world.

**The directives aren’t for specifying “where the code runs” module by module. You shouldn’t put `'use client'` in all frontend modules or `'use server'` into all backend modules—that’s pointless!** All they do is let you create “doors” between the two module systems. They let you _refer to_ the other world.

If you want to pass data from the backend to the frontend (as a `<script>` tag), you need to `'use client'`. If you want to pass data from the frontend to the backend (as an API call), you need to `'use server'`. Otherwise, you don’t need either directive—you just use `import` as usual and stay in the current world.

* * *

### [In Conclusion](https://overreacted.io/how-imports-work-in-rsc/#in-conclusion)

RSC does not shy away from the fact that the backend and the frontend each have their own module system. It works exactly like traditional JavaScript codebases that reuse some code between the frontend and the backend, where reused code effectively exists on both sides. What RSC adds on top are just two mechanisms:

*   The `import 'client-only'` and `import 'server-only'` poison pills that let some individual modules declare they _must not be brought_ into the other world.
*   The `'use client'` and `'use server'` directives that let you _refer_ to the modules from the other world and pass data to them without _bringing them in_.

With these two mechanisms, you can see an RSC application as a single program spanning two computers—with two independent module systems, two poison pills, and two doors to pass information between those module systems.

As this “layered” approach settles in your muscle memory, you’ll realize that the `frontend/` and `backend/` directories become unnecessary and downright misleading because the information is already contained in the modules. But it’s contained _locally_ so the boundaries automatically shift as you evolve your code.

The poison pills ensure that nothing is brought into a wrong world, the directives let you pass information between the worlds, and regular imports work as usual.

Now all you have to do is to fix the build errors.

I heard LLMs are getting quite good at that.
