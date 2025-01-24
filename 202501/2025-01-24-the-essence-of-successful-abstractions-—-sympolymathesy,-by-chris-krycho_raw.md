Title: The Essence of Successful Abstractions — Sympolymathesy, by Chris Krycho

URL Source: https://v5.chriskrycho.com/journal/essence-of-successful-abstractions/

Published Time: 2025-01-21T18:06:00.000-07:00

Markdown Content:
**[Assumed audience](https://v4.chriskrycho.com/2018/assumed-audiences.html):** Software developers who want to improve at their craft. Assumes a bit of background about programming in general, and also just a _little_ bit of background knowledge about Rust and TypeScript. (You’ll be just fine if you know no more of either than that they exist and roughly what they are.)

As a bit of a prelude, consider this extended quote from Fred Hebert, [Complexity Has to Live Somewhere](https://ferd.ca/complexity-has-to-live-somewhere.html)

> Fighting complexity is a recurring theme of software development I’ve seen repeat itself over and over again. It’s something I keep seeing debated at all levels: just how much commenting should go on in functions and methods? What’s the ideal amount of abstraction? When does a framework start having “too much magic”? When are there too many languages in an organisation?
> 
> We try to get rid of the complexity, control it, and seek simplicity. I think framing things that way is misguided. Complexity has to live somewhere.
> 
> …
> 
> When we adopt something like microservices, we try to make it so that each service is individually simple. But unless this simplicity is so constraining that your actual application inherits it and is forced into simplicity, it still has to go somewhere. If it’s not in the individual microservices, then where is it?
> 
> Complexity has to live somewhere. If you are lucky, it lives in well-defined places. In code where you decided a bit of complexity should go, in documentation that supports the code, in training sessions for your engineers. You give it a place without trying to hide all of it. You create ways to manage it. You know where to go to meet it when you need it. If you’re unlucky and you just tried to pretend complexity could be avoided altogether, it has no place to go in this world. But it still doesn’t stop existing.
> 
> With nowhere to go, it has to roam everywhere in your system, both in your code and in people’s heads. And as people shift around and leave, our understanding of it erodes.

There’s more, and it’s good, so [read the whole thing](https://ferd.ca/complexity-has-to-live-somewhere.html)! And as you do, you might consider how it pairs with the quote from Peter Naur [I shared yesterday](https://v5.chriskrycho.com/notes/two-quotes-on-software-engineering/). Now —

Hebert applies this to microservices, I think appropriately. I think it also applies to _types_. The types always exist; the complexity they represent always exists. The question is first of all whether we have written them down anywhere — that is, whether we have a contract about them that can be enforced, and if so what can enforce them. Secondarily, then, the expressiveness of a type system is a measure of what kinds of the program’s complexity we _can_ write down as types.

People who are a bit allergic to types often feel constrained by them, but those of us who like robust types see that relationship the other way around. As [Dan Freeman](https://dfreeman.io/) put it to me recently: types are a tool, just like tests, but you have to _use_ that tool. Types do provide constraints, much as tests do — but they are only the types _we choose to impose_. That is, they are knowledge we are encoding into the program.

The same basic thesis applies to our tests, which represent a different set of knowledge than our types. This is the benefit of “test-driven development”, particularly in the red-green cycle: it is a way of encoding knowledge into the program. Test expressiveness works in different ways than type expressiveness, but it is a useful way of evaluating different kinds of and different approaches to testing.

This is why I like Rust. The complexity of correctly [spatial and temporal safety](https://blog.yoshuawuyts.com/temporal-spatial-memory-safety/) has to live somewhere. Rust pushes the majority of that complexity into its type system, and particularly the famed borrow checker. The rest of the complexity it isolates in `unsafe` blocks. Mind: `unsafe` allows you to know where the complexity lives, but it does not tell you where your getting that complexity wrong will _surface_. But the combination of the borrow checker and the isolation that `unsafe` offers _does_ allow us to _control_ the complexity. We cannot get rid of it. We can only isolate it.

A garbage collector gives you memory safety and not having to think explicitly about memory allocation and deallocation, but the complexity is still not gone — it has moved to the implementation, to weird performance cliffs, and to difficult-to-debug leaks of memory or other resources. That trade is very often worth it, though!

Whether with Rust or with a garbage collector, isolating the temporal and spatial safety means we don’t have to keep it in our heads _most of the time_, and that allows us to focus on other problems. This is why there are so many developer tools for JavaScript and Python being written in Rust: not because people didn’t want fast tools before, but because for many developers, keeping all the safety issues in their heads as they would have had to do with C or C++ was more than they felt they could reasonably do _and also ship the thing they cared about_. Rust’s borrow checking opens that door to many more people, because it has isolated that complexity, and thereby provided a more usable tool.

This exact dynamic is also why I like TypeScript, even including some of the wilder types I ended up writing for Ember and LinkedIn in years past. The complexity was always there — often far more than anyone realized before we started trying to write down types that actually accurately represented the system. TypeScript did not create the complexity, much as people sometimes _felt_ like it added complexity to the code we were looking at. No, it merely shone a light on the existing complexity, and gave us the opportunity — and a tool with which — to [start grappling with it](https://v5.chriskrycho.com/journal/is-typescript-good/#:~:text=In%20software%2C%20the,of%20the%20system.).

Isolating complexity is useful. As Hebert says, “If you are lucky, it lives in well-defined places.” It is not always possible to isolate complexity — we are not always lucky — , but when isolating complexity _is_ possible, it is glorious, because isolating complexity is the essence of successful abstractions.
