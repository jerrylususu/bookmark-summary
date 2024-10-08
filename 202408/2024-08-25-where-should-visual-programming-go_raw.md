Title: Where Should Visual Programming Go?

URL Source: https://tonsky.me/blog/diagrams/

Published Time: 2024-07-18

Markdown Content:
There’s a wonderful article by Sebastian Bensusan: “[We need visual programming. No, not like that.](https://blog.sbensu.com/posts/demand-for-visual-programming/)” (the dot is part of the title ¯\\\_(ツ)\_/¯).

In it, Sebastian argues that we shouldn’t try to replace all code with visual programming but instead only add graphics where it makes sense:

> Most visual programming environments fail to get any usage. Why? They try to replace code syntax and business logic but developers never try to visualize that. Instead, developers visualize state transitions, memory layouts, or network requests.
> 
> In my opinion, those working on visual programming would be more likely to succeed if they started with aspects of software that developers already visualize.

I love diagrams myself! Whenever I encounter a complicated task and try to solve it in code, it always gets messy. But after drawing a diagram, my understanding improves, and the code gets cleaner. Win-win!

Here’s one I made for button states in Humble UI:

![Image 1](https://tonsky.me/blog/diagrams/button.webp?t=1722327208)

I bet you thought buttons are easy? Me too, at first. But after certain threshold your head just can’t fit all the states and transitions.

Or for an image upload component:

![Image 2](https://tonsky.me/blog/diagrams/image_upload.webp?t=1722327208)

Again: it would’ve been easy if not for error handling. But with a principled approach, you can get through any of that.

Sebastian gives many more examples of useful visualizations in his article, too.

But now, how does all this relate to code? I think there’re four levels.

Level 0: Diagrams live separately
---------------------------------

You draw them in a separate tool, then use that to help you write code. Maybe put them on a wiki for other people to see. The point is: the diagram lives completely separate from the code.

Downsides: hard to discover, can get out of date.

This is what I did in the two examples above, and I guess what most of us can do given modern tools. But hey—it’s still not that bad!

Level 1: Diagrams live next to code
-----------------------------------

One simple trick would solve the problem of discovery: what if we could put images into our text files?

Currently, the best you can do is this:

```
                   +-----+  -->
                   | N_4 |------     <--- +-----+
                   +-----+     |    |-----| R_3 |
                      |    15  |    | 5   +-----+
                      |50      |    |        |
    +-----+  --->     |        +-----+       | 70
    | N_2 |------     |        | N_3 |       |
    +-----+     |     |        +-----+       |
     |       15 |     |            | 30      |
     | 10       |   +-----+  <---  |         |
  @  |          ----|  S  |--------|         |
  @  |       <@@@   +-----+                  |
  V  |                 |   |                 |
     |              10 |   |                 |
  +-----+              |   V                 |
  | R_2 |          +-----+                   |
  +-----+          |  E  |                   |
|  |               +-----+                   |
|  | 40             |  |                     |
V  |             10 |  |                     |
   |    +-----+     |  V                     |
   -----| R_1 |-----|                        |
        +-----+                              |
           |     --->         +-----+        |
           |------------------|  D  |---------
                   10         +-----+
```

But it gets messy real quick. What if we could do this instead?

![Image 3](https://tonsky.me/blog/diagrams/sublime.webp?t=1722327208)

Upsides: easy to implement (once everybody agrees on _how_ to do that), universal (probably many other use cases).

Downsides: still can get out of date. “Comments are not code”—the same applies here.

Oh, and if you are coding in a terminal, this party is not for you. Sorry. We are thinking about the future here.

Level 2: Diagrams are generated from code
-----------------------------------------

This is what Sebastian was hinting at. Code and diagrams co-exist, one is generated from the other.

Generating diagrams from code is definitely something IDEs can do:

![Image 4](https://tonsky.me/blog/diagrams/autogenerated.webp?t=1722327208)

Upsides:

*   Always up to date.
*   Non-invasive: can be integrated into IDE without affecting how code is stored.

Downsides:

*   It can help you understand, but can it help you think?
*   Probably not very visually appealing, as these things tend to be. It’s hard to automatically lay out a good diagram.

Level 3: Diagrams are code
--------------------------

This is what the endgame should be IMO. Some things are better represented as text. Some are best understood visually. We should mix and match what works best on a case-by-case basis. Don’t try to visualize simple code. Don’t try to write code where a diagram is better.

One of the attempts was Luna. They tried dual representation: everything is code _and_ diagram at the same time, and you can switch between the two:

![Image 5](https://tonsky.me/blog/diagrams/luna.webp?t=1722327208)

From [luna-lang.org](https://web.archive.org/web/20160730111343/http://www.luna-lang.org/)

But this way, you are not only getting benefits of both ways, you are also constrained by both text _and_ visual media at the same time. You can’t do stuff that’s hard to visualize (loops, recursions, abstractions) AND you can’t do stuff that’s hard to code.

No, I think textual coding should stay textual where it works, BUT we should also be able to jump into a diagram tool, draw a state machine there and execute it the same way we execute text code.

![Image 6](https://tonsky.me/blog/diagrams/new_file@2x.png?t=1722327208)

And when I mean draw, I mean draw. With direct manipulation, all that jazz. And _without_ converting it back to text.

So what I’m saying is: diagrams should not replace or “augment” text. They should be just another tool that lives _next_ to the text. But a tool on its own.

Think of it as a game engine like Godot or Unity. In them, you can write normal text code, but you can _also_ create and edit scenes. These scenes are stored in their own files, have specialized editors that know how to edit them, and have no code representation. Because why? The visual way _in this particular case_ is better.

![Image 7](https://tonsky.me/blog/diagrams/godot.jpg?t=1722327208)

So the challenge here is not about integrating diagrams, but to think about which types of diagrams can be useful, can work better than code, and be directly executed.

Non-goal: Diagrams replace code
-------------------------------

Important note: we are not talking about doing code graphically. This is just a less convenient way of doing things that text already does.

![Image 8](https://tonsky.me/blog/diagrams/blockly.webp?t=1722327208)

We are also not talking about no-code platforms: sometimes code is just better.

But until this bright future arrives, put a diagram or two on the wiki. Your teammates will thank you for that.
