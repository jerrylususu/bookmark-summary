Title: Is TypeScript Good?—A Reply to Rach Smith — Sympolymathesy, by Chris Krycho

URL Source: https://v5.chriskrycho.com/journal/is-typescript-good/

Published Time: 2023-07-17T16:32:00.000-06:00

Markdown Content:
**[Assumed audience](https://v4.chriskrycho.com/2018/assumed-audiences.html):** JavaScript-forward folks open to hearing a take on why TypeScript might indeed be good. This neither assumes deep technical familiarity with TypeScript nor addresses philosophical objections; the emphasis is on the practical questions raised by the post to which this one is responding.

**[Epistemic status](https://v5.chriskrycho.com/journal/epistemic-status/):** I have lived and breathed TypeScript’s tradeoffs for the last 6½ years: it is not impossible that I would change my mind here, but these are not tentative or provisional thoughts.

Rach Smith [writes](https://rachsmith.com/is-typescript-good/) — and I quote extensively for the sake of a robust response to her — :

> The Mere Exposure effect describes our tendency to develop preferences for things simply because we are familiar with them.…
> 
> TypeScript. I really didn’t like it at first. Writing it felt slow and clunky, and I couldn’t see how it could benefit us as a team when 99% of the codebase was still JavaScript.
> 
> But I stuck with it, and kept plodding through, learning how to type our codebase. I’ve been working with it for over six months, and I’m growing to like it. I’m still unsure if TypeScript is preferable to JavaScript or just the exposure effect at play. Do I like it just because I’m familiar with it?
> 
> The part I like most is being able to “see what things are”. Now I get frustrated when I hover over a function or variable in VSCode, expecting it to tell me its types, and it can’t because it was imported from a JS file.
> 
> The part that makes me wary is how clever it makes me feel. TypeScript… tickles my brain in a way I’ve learned to be wary of because whenever I get too clever, I write code that is harder for others (or me, in 6 months) to read. There’s a real dopamine rush from successfully converting a gnarly JS file into a TS one, even though I’ve achieved basically nothing in reality. The product is doing the same thing.

I like reading Rach because she offers a perspective quite different to the one I am around most of the time in my day job, and she obviously thinks hard about how to build software well. No surprise then that her post here does a great job of capturing two things:

*   an important question about what a TypeScript conversion does or does not accomplish
*   a real and important tradeoff around the language and the complexity it can enable

In the tradition of old-school blogging,[1](https://v5.chriskrycho.com/journal/is-typescript-good/#fn1) I thought I would respond… publicly! I am going to take these in reverse order, because on the tradeoff she highlights, I largely agree. On the value provided by a conversion, I both sympathize with her and also think there is more to say.

[Tradeoffs](https://v5.chriskrycho.com/journal/is-typescript-good/#tradeoffs)
-----------------------------------------------------------------------------

The key challenge with TypeScript — perhaps with _any_ language with a robust type system — is the one Rach highlights here:

> TypeScript… tickles my brain in a way I’ve learned to be wary of because whenever I get too clever, I write code that is harder for others (or me, in 6 months) to read.

Type systems very often do mash a puzzle-solving button in our brains. Figuring out how to get the types _just right_ for a given design can lead an unwary developer (reader: I mean myself) into an hours-long maze. Getting out of one of those mazes with a good solution feels incredibly satisfying. But it is not always _worth_ it. A simpler type might be a little less precise, might catch a couple fewer errors, might make the system mildly less robust at runtime, might make it possible for there to be runtime bugs the system could in principle have ruled out entirely by clever use of the type system… and be 100% worth those tradeoffs given the context.

It is more than just the puzzle-solving aspect at play, though: many software developers and engineers (like me!) also deeply prioritize the correctness of the code we write.[2](https://v5.chriskrycho.com/journal/is-typescript-good/#fn2) However, correctness as such is (a) on a spectrum and (b) not free. Software engineers like me often get sucked into a second trap of maximizing correctness — even at the cost of more time than it is worth for the problem we are solving.

There are times when absolutely maximizing correctness is the right tradeoff. For example: if you are implementing TLS, you should be using every tool at your disposal to guarantee correctness: a memory-safe language, formal modeling, TDD, formal verification, you name it. To a large degree, the same goes when you are writing foundational framework or library code; I do not regret one second spent on making the TypeScript types for LinkedIn’s i18n and tracking libraries, or [Ember’s TypeScript types](https://blog.emberjs.com/stable-typescript-types-in-ember-5-1), both correct and useful (brutal though those efforts were).

That does not mean that maximizing type-driven correctness is the right choice everywhere. I often shorthand this by saying: most TypeScript app code should have a minimal number of type annotations and close to zero “fancy” type definitions — because well-written libraries should absorb that type-level complexity and make it possible to mostly just rely on type inference. Put another way: good library code should make it so most app code can be written and read mostly like JavaScript.

This does not always hold for [conversions](https://v5.chriskrycho.com/journal/note-on-typescript-conversions/), because conversions tend to expose just how wild our JavaScript code really was. I say more on this in [the section on value](https://v5.chriskrycho.com/journal/is-typescript-good/#value) below.

TypeScript can make these two traps of puzzle-solving and correctness-maximizing particularly alluring. It comes with type system features available in no other language deployed so widely and targeting such a mainstream audience; the only languages really deployed in “industrial” contexts with comparable or greater type system complexity (albeit along different axes) are Rust and Haskell.[3](https://v5.chriskrycho.com/journal/is-typescript-good/#fn3) Those features enable puzzle-solving and correctness-maximizing you simply cannot get trapped by in Java or C♯.

Long story short, I very much agree with Rach about the temptation to _cleverness_ offered by TypeScript. All of the most advanced TypeScript code I have written — the well-motivated examples listed above — comes accompanied by an even greater amount of comments and documentation, because the complexity is real, and high, and difficult for anyone to maintain (myself included).

[Value](https://v5.chriskrycho.com/journal/is-typescript-good/#value)
---------------------------------------------------------------------

I still think TypeScript is good. The reason is suggested by the one bit of Rach’s post I disagree with (emphasis mine):

> There’s a real dopamine rush from successfully converting a gnarly JS file into a TS one, _even though I’ve achieved basically nothing in reality. The product is doing the same thing._

I hear this sentiment quite often, and I think there is something real behind it. I also think it is not quite right.

The “something real” is this: the product as experienced by the user is usually largely the same as it was before the conversion. However: the qualifiers “usually” and “largely” here matter enormously. It is only “usually” and “largely” because converting to TypeScript very often exposes bugs. Fixing those bugs means the product is only “doing the same thing” if we are speaking purely in terms of features _per se_ and exclude the user experience of bugs as something which matters.

When I was researching the possible impact of TypeScript adoption on our apps at LinkedIn, I found that up to a quarter of all the JavaScript errors experienced by our members would be caught by even a minimal TypeScript conversion. Our experience so far bears that out: Despite a lot of very smart software developers doing their best in the plain-JS code base we started with, we find and fix bugs whenever we convert some significant chunk of code to TypeScript. Likewise, the single worst and longest-standing bug in the app I converted at my previous job was flagged immediately by TypeScript when we converted the relevant parts of the codebase.[4](https://v5.chriskrycho.com/journal/is-typescript-good/#fn4)

Those kinds of real changes to the product can go much further as you make more investments, too. For example, we have done a lot of work at LinkedIn to get type safety in our internationalization and tracking libraries, and that has paid real dividends. Untranslated strings are a big deal for our members! And from an internal perspective, the same goes for our tracking libraries: if your A – B test data is not reliable, it is very hard to know whether a given experimental feature is paying for itself or not.

Net, very often the result of a conversion is _not_ a product which “does the same thing”, but one which actually works better than it did before.

But let us grant the basic claim for a moment, because there are times when converting a file requires some ingenuity but does genuinely leave all the end-user functionality unchanged. I still do not think we have “achieved basically nothing in reality” in those cases.

First, when Rach describes the “real dopamine rush from successfully converting a gnarly JS file into a TS one”, she indirectly highlights an important reality — that in many cases the complexity was already present in the code base. The TypeScript conversion did not create that complexity: It exposed it. Real-world JavaScript code is often incredibly complicated — indeed, _clever_ — in ways that only become obvious when we try to express in types the contracts the code already invisibly assumes. As a result, conversions from JavaScript require complex types far more than code written in TypeScript from the start. Much of the complexity is (permanently!) implicit in JavaScript, while writing out the contracts in TypeScript makes it explicit. That enables better choices: does this particular API actually warrant some complicated types, or should we just keep it simple? Usually: the latter.

Second, I often think of [a post by Mark Seeman](https://blog.ploeh.dk/2019/03/04/code-quality-is-not-software-quality/) on exactly this theme, and at a far more general level (emphasis his, strong emphasis mine):

> You can write quality software in many different languages, using various styles. When you evaluate the externally observable qualities of software, the code is invisible. It’s not part of the evaluation.
> 
> It seems to me that some people try to make an erroneous conclusion from this premise. They’d say that since no employer, client, or end user evaluates the software based on the code that produced it, then no one cares about the code. … It’s easy to refute that argument. All you have to do is to come up with a counter-example. You just have to find one person who cares about the code. That’s easy.
> 
> **_You_ care about the code.…**
> 
> I think every programmer cares about their code bases; if not in an active manner, then at least in a passive way. Bad code can seriously impede progress. I’ve seen more than one organisation effectively go out of business because of bad legacy code.
> 
> **Code quality is when you care about the readability and malleability of the code… about the code’s ability to _sustain_ the business, not only today, but also in the future.…**
> 
> Yes, you should write code such that it produces software that provides value here and now, but you should also do your best to enable it to provide value in the future. This is _sustainable_ code. It’s code that can sustain the organisation during its lifetime.

Even a TypeScript conversion which leaves all the end-user functionality untouched can meaningfully improve the sustainability of the code base. (I say “can” not “does” because the details always matter. That holds for any code we write, though.) The cost of the conversion is important, and so we have to watch out for the puzzle-solving and correctness-maximizing traps described above. When we get that balance right, though, we improve our ability to “deliver value” to our users going forward.

Third, then, a TypeScript conversion can be thought of as improving the _stocks_ in a system: language I borrow from Donella Meadows’ [Thinking in Systems](https://bookshop.org/a/21126/9781603580557). A _stock_ is the capacity from which the _flows_ out of a system are drawn. The water in an aquifer is the stock, the running faucet a flow. We should not spend all our time on building the stock of a system; that becomes unhealthy: a stagnant pool not only does not benefit anyone, but in fact can cause active harm to the environment. However, a failure to invest in and sustain the stocks of a system can cause catastrophe: an empty aquifer is very bad news for the community which relies on it.

In software, the stock of a code base is its sustaining capacity to deliver the flow of new end-user capabilities over time.[5](https://v5.chriskrycho.com/journal/is-typescript-good/#fn5) Any improved ability to understand, to navigate, and to change our code represents and improved stock. Even making complexity visible rather than invisible, as in the case of many JavaScript-to-TypeScript conversions, is an improvement to a stock. Investing in these sorts of non-functional changes to code which make it easier to work with later is therefore not “achieving nothing”. It is, rather, investing in the future of the system.

As Rach herself put it:

> The part I like most is being able to “see what things are”. Now I get frustrated when I hover over a function or variable in VSCode, expecting it to tell me its types, and it can’t because it was imported from a JS file.

This is a stock: type information makes the code base easier to understand, and things which make code easier to understand enable us to make changes more easily. The same goes for robust go-to-definition which just works, everywhere, all the time, instead of being flaky and incomplete (because driven by a fragile pile of heuristics which are often wrong).[6](https://v5.chriskrycho.com/journal/is-typescript-good/#fn6) We cannot successfully change code we do not understand: neither adding new abilities, nor improving existing abilities, nor even fixing bugs.[7](https://v5.chriskrycho.com/journal/is-typescript-good/#fn7)

Nor is the improved stock limited to better comprehensibility of the code. It also includes far more powerful and reliable refactoring. For one thing, many refactors can be done automatically. For another, many even of the changes which cannot be automated are still easier after a JS\-to-TS conversion. Right up front, being able to accurately and instantaneously find all references to a given API makes it far easier to design a sweeping change involving that code. Then, after making a change, the ability to “just follow the compiler errors” makes the change far more trustworthy, not least because it tends to expose knock-on effects which are easy to miss in the absence of the types.

In sum, smart use of types helps sustain the ability to add features or to change how existing features work. They enable future flows.

Not every investment pays for itself, and the right balance of investments in stocks against the delivery of flows (features and capabilities) is something every software developer and team has to consider carefully. That a change is an investment delivering value sometime besides _today_ does not make it less valuable, though. Indeed, sometimes the exact opposite is true: in software as in life.

* * *

1.  As my friend Brad East [put it](https://www.bradeast.org/blog/substack-vs-blogging) a while back (emphasis mine):
    
    > Blogging is the shaggy dog of internet writing. It’s playful, experimental, occasional, topical, provisional, personal, tentative. It is inexpert, even when written by experts. It is off the cuff, even when polished and thought through.
    > 
    > And _it is conversational_, at its origins and in its form. _It’s constantly linking, talking, referring, thinking out loud by bouncing ideas off of other ideas, typically found on other blogs._
    
    That’s what this post is. [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref1)
    
2.  And the code our code enables _others_ to write! [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref2)
    
3.  I do not have in mind here features like sum types/tagged unions/”custom types”, which _ought_ to be treated as non-negotiables in any modern language. Nor am I thinking even of generics, which are also fairly indispensable as far as I am concerned: it is telling that even Java has had some kind of generic types for ages now. Rather, I am thinking of things like [mapped types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html), [conditional types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html), and [template literal types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html), which combine to produce a type-level language which can literally _parse SQL in the type system_. [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref3)
    
4.  That conversion was actually a cautionary tale, and a deeply formative experience for me. I _ignored_ the error TypeScript flagged: “No, I know better; this piece of data can never actually be `null` or `undefined` here for .” I was wrong. It took another year and many more millions — literal millions! — of that error affecting end users for us to catch it, purely by happenstance, and realize that TypeScript was right and I was wrong; that particular field absolutely _could_ be `null` there. [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref4)
    
5.  That types are a help to this rather than an impediment is of course a primary bone of contention between the static and dynamic typing camps. I can say only that I find types to _dramatically_ improve the ability to change a system over time, comparable in degree though different in specifics to the effect of good tests. [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref5)
    
6.  Insofar as it already “just works” in a lot of JavaScript code bases, TypeScript is to thank for that, too, since most of that is powered by the TypeScript Language Server! [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref6)
    
7.  On which I recommend that everyone working in software read Peter Naur’s still-completely-relevant [Programming as Theory-Building](https://pablo.rauzy.name/dev/naur1985programming.pdf) (though skip the introduction and “commentary” after the conclusion in that PDF). [↩︎](https://v5.chriskrycho.com/journal/is-typescript-good/#fnref7)
