Title: Linguistic Relativity and the Tyranny of the Compiler

URL Source: https://ingrids.space/posts/tyranny-of-the-compiler/

Markdown Content:
Linguistic Relativity and the Tyranny of the Compiler | Ingrid's Space

1.   [Where does this leave us when considering programming languages?](https://ingrids.space/posts/tyranny-of-the-compiler/#where-does-this-leave-us-when-considering-programming-languages)
2.   [You only have your chains to lose](https://ingrids.space/posts/tyranny-of-the-compiler/#you-only-have-your-chains-to-lose)
3.   [Wait, maybe the chains weren’t such a bad idea](https://ingrids.space/posts/tyranny-of-the-compiler/#wait-maybe-the-chains-werent-such-a-bad-idea)
4.   [Aside: codified vs constructed languages](https://ingrids.space/posts/tyranny-of-the-compiler/#aside-codified-vs-constructed-languages)
5.   [The actual takeaway: teaching and learning](https://ingrids.space/posts/tyranny-of-the-compiler/#the-actual-takeaway-teaching-and-learning)

The idea has been floating around in Linguistics for about a century, that language affects one’s thoughts. Known as [linguistic relativity](https://en.wikipedia.org/wiki/Linguistic_relativity), aka the Sapir-Whorf hypothesis, this comes in two flavours: the strong version, where language _determines_ and _limits_ thought; and the weak version, where language only _influences_ thought.[1](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:1) For human languages, linguists largely agree that the strong version is false, and instead hold to the weak version.

We can propose a mechanism to explain this starting from two premises: humans are capable of abstract thought in the absence of language, and are capable of modifying their languages. From these, we can conclude not only that the strong version is false, but that the relationship appears to flow in the other direction: one thinks an abstract thought, and modifies their language to express it. Thought determines language.

To explain how the weak version might hold, we must introduce one more idea: language as a framework for thought. You see, abstract thinking is _hard_, and humans usually avoid doing things that are hard when there’s another option. Language offers us a ready-made set of concepts (vocabulary), and systems for connecting them (grammar). Using language feels like building with Lego, where abstract thought can often feel like trying to mix and mould concrete in your living room.[2](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:2) Unless you care a lot about how you form or express a thought, you’ll likely default to the ready-made option, and this is where language influences your thoughts.

### Where does this leave us when considering programming languages?

Well, one of our premises has been compromised: capability to modify the language. While it is _technically_ possible to edit your compiler (or interpreter) on the fly, this is so out of reach for most programmers that it doesn’t even register as an option. Furthermore, even for those who do have sufficient domain knowledge and familiarity with their compiler’s source, it isn’t exactly a trivial task one would undertake on a whim. Compare this to natural human languages, where ordinary people without linguistics degrees modify their languages with such ease that they often don’t even realise they’re doing it.[3](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:3)

### You only have your chains to lose

It doesn’t _need_ to be this way though, and I can almost see the LISPers throwing their macros at the screen at this point. And indeed, macros are a powerful tool, they let you define syntax on the fly, albeit still limited to the context of s-expressions.

Yet the LISPs have more to offer. Due to their extremely small and easily-parseable syntax, interpreters for them are easy to write. So easy in fact, that [a textbook aimed at first-year undergrads](https://sarabander.github.io/sicp/) casually walks you through implementing interpreters and compilers from scratch.

### Wait, maybe the chains weren’t such a bad idea

Once you’ve gone through the trouble of editing the compiler, you run into a problem. It turns out you have a compatibility nightmare on your hands. Compiling your own code goes just fine, but you can’t compile code from your friend who also edited her compiler, nor can she compile yours. Given how reliant we programmers are on the work of others, we need to reconcile this. We try to form a committee, but everyone disagrees, it devolves into a flame-war, and all ends in tears.

And here we see how the proposed boon of LISP becomes its bane. Implementations are so easy to write that everyone and their cat wrote one, and we can’t seem to make any progress. It also often feels impossible to figure out which LISP to even use. Which dialect do you pick? Scheme? Common LISP? Guile? Racket? Clojure? Say you pick Scheme, which implementation? Chicken? Chez? Stalin? MIT? Bigloo? They all have their incompatibilities to boot. The situation with macros is fraught too, it’s painful to try to read someone else’s code when they change the syntax out from under you, to the point that some jest that LISPs are “write-only” languages.[4](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:4)

Compare this sorry state of affairs to natural languages, where modifications live or die by organic consensus. The gap is wide indeed. Perhaps it is unfair to compare programming languages to natural human languages though, as the former comprises a formal system for computation, and the latter a casual medium for ad-hoc communication. It may be that we are condemned to accept and use what is handed down to us from the ivory tower.

### Aside: codified vs constructed languages

Here’s something that doesn’t sit right with me: the popular dichotomy between “natural” and “constructed” languages. The line is commonly drawn by saying that constructed languages are consciously devised, instead of naturally developed.

This is an unconvincing distinction to me, because all language constructs originate as an idea in someone’s head, and I believe many of those in “natural” languages came about consciously. I know I am consciously selective of what language constructs I use, and how I break language norms. I’d also posit that many constructs of “constructed” languages and not devised consciously, but are rather blind-spots that the originator unknowingly borrows from languages they are already familiar with.

One might also draw a distinction based on the number of people involved in creating a language, and when/whether changes to the language are made. This too is unconvincing to me, as many “constructed” languages develop iteratively, through many people. A good example is [Toki Pona](https://tokipona.org/), whose original creator made a point of eschewing standardization, and recently compiled a reference of how the language is used in practice by its speakers. In the world of programming, one might also point out how C++ is an iteration on C, which itself iterated in B, and so on down the line to BCPL, CPL, etc. C++ Also borrows from languages it didn’t directly descend from, like Smalltalk and ML, just like natural languages.

In my opinion, the more meaningful dichotomy can be drawn between “codified” and “natural” (or “ad-hoc”) languages, where the distinction is made on whether there is a codified standard of correctness applied to usage of the language. Notably, unlike the former dichotomy, this would classify languages like Standard English outside the realm of natural, while letting in things like Toki Pona.

This provides a clarity on why programming languages can’t seem to behave like “natural” languages; to use them, one _needs_ codify them through the act of writing a compiler.

### The actual takeaway: teaching and learning

This all seems a bit _academic_ so far, but I actually came to write all this because I wanted to tackle a practical difficulty. In talking to Informatics and IT students, I noticed one particular topic they all seemed to be failing to grok: first-class functions (or “lambdas”[5](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:5) as they put it). The relevant common denominator, as it turns out, is that they were all taught through Java.

It could be that first-class functions are just a difficult idea to grasp (I have to admit, they were a bit mind-bendy when I first encountered the concept), but I don’t think that’s it, since these students managed to wrap their heads around things like interfaces and abstract classes just fine.

I think the real reason becomes clear when you look at the syntax for functions in Java:

```
import java.util.function.Function;

// "Normal" way to define functions (well, methods)
class Incrementor {
    // I know this could be static, but I'm trying
    // to represent typical Java method definition
    public int inc(int arg) {
        return arg + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        // "Normal" way to use a method
        Incrementor incrementor = new Incrementor();
        incrementor.inc(1);

        // Defining a first-class function
        Function<Integer, Integer> inc = arg -> arg + 1;
        // Using a first-class function
        inc.apply(1);
    }
}
```

Lua, for reference:

```
-- "Normal" way to use functions
-- these are already first-class
function inc(arg)
    return arg + 1
end

-- anonymous function (which I immediately name...)
inc = function(arg)
    return arg + 1
end

-- applying either (it's the same)
inc(1)
```

What’s immediately striking is how alien the two forms look compared to each other in Java. While that is indeed striking, and certainly doesn’t help a learner’s understanding, I think it’s only a secondary concern. To reach my larger concern, we need to consider what is going on in the student’s head.

I’ve always viewed methods as a special case of functions, as I think most people would. Imagine, however, that you had never learned about the general concept of functions, but instead only methods. The students in question were flabbergasted when I presented the idea of a function outside the context of a class. Instead of conceiving of functions as abstractions over subroutines or mappings between types, they instead viewed them as components of the interface to an object. It’s understandable that they see it this way, because that’s how they’re presented in Java’s syntax, which goes so far as disallow writing functions outside of classes. When this is all the background you’ve been given on functions, of course “lambdas” seem inscrutable.

In this clear-cut example of linguistic relativity, after exploring and playing with the concept of functions as presented in other languages, the students grasped “lambdas” with relative ease.

What can we learn from this? As teachers, we should probably be more conscious of how teaching tools affect learners, both so we can make more informed choices of tooling, and so that we can better identify and rectify gaps in learners’ understanding. As learners, I can’t espouse strongly enough the value of learning a programming language from a different paradigm than the one(s) you’re familiar with, and analyzing problems through the lens of that paradigm. It will make you a better programmer even in the languages you’re already familiar with.

> **P.S.** Why are we teaching programming through Java anyway? Even if one takes the rather cynical view that everything in industry ought to be done in Java, and that the sole purpose of education is to stamp out ready-made cogs to slot into the machine of industry, I find it hard to justify. The ideal traits of a practical language[6](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:6) are not necessarily those of an instructional language,[7](https://ingrids.space/posts/tyranny-of-the-compiler/#fn:7) and, as we saw in the above example, teaching Java first only hampered the learner’s ability to understand and use Java features.

* * *

1.   Perhaps this would be better conceived as a spectrum.[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:1)

2.   And concrete does indeed have more expressive power than lego.[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:2)

3.   If you don’t believe me on this point, consider how the dialects of English spoken around the world have grown apart over the past few hundred years. To how many of those differences could one ascribe conscious intent?[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:3)

4.   I actually like LISP, please don’t kill me.[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:4)

5.   _technically_*** the word lambda is conventionally used to refer specifically to anonymous functions, but who am I to prescribe language to anyone when I just wrote all this about linguistic relativity? I do want to make it clear though, that I’m talking about the concept of first-class functions, not just specifically the anonymous ones.[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:5)

6.   Not that I’m endorsing Java in practice either, mind.[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:6)

7.   I’m partial to Scheme because of [the aforementioned textbook](https://sarabander.github.io/sicp/). It has an extremely minimal and consistent syntax that gets out of the way of learning, yet I certainly wouldn’t pick it for a large project.[↩︎](https://ingrids.space/posts/tyranny-of-the-compiler/#fnref:7)
