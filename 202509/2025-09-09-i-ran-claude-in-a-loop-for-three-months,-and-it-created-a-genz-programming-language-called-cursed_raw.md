Title: i ran Claude in a loop for three months, and it created a genz programming language called cursed

URL Source: https://ghuntley.com/cursed/

Published Time: 2025-09-09T03:36:48.000Z

Markdown Content:
It's a strange feeling knowing that you can create anything, and I'm starting to wonder if there's a seventh stage to the "[people stages of AI adoption by software developers](https://ghuntley.com/ngmi/)"

![Image 1](https://ghuntley.com/content/images/2025/03/image-17.png)
whereby that seventh stage is essentially this scene in the matrix...

It's where you deeply understand that '[you can now do anything](https://ghuntley.com/dothings/)' and just start doing it because it's possible and fun, and doing so is faster than explaining yourself. Outcomes speak louder than words.

There's a falsehood that AI results in SWE's skill atrophy, and there's no learning potential.

> If you’re using AI only to “do” and not “learn”, you are missing out
> 
> - [David Fowler](https://x.com/davidfowl/status/1910930253608001565?ref=ghuntley.com)

I've never written a compiler, yet I've always wanted to do one, so I've been working on one for the last three months by running Claude in a while true loop (aka "[Ralph Wiggum](https://ghuntley.com/ralph)") with a simple prompt:

> Hey, can you make me a programming language like Golang but all the lexical keywords are swapped so they're Gen Z slang?

Why? I really don't know. But it exists. And it produces compiled programs. During this period, Claude was able to implement anything that Claude desired.

The programming language is called "cursed". It's cursed in its lexical structure, it's cursed in how it was built, it's cursed that this is possible, it's cursed in how cheap this was, and it's cursed through how many times I've sworn at Claude.

![Image 2](https://ghuntley.com/content/images/2025/09/image-1.png)

https://cursed-lang.org/ 

For the last three months, Claude has been running in this loop with a single goal:

> "Produce me a Gen-Z compiler, and you can implement anything you like."

It's now available at:

*   [https://cursed-lang.org/](https://cursed-lang.org/?ref=ghuntley.com)
*   [https://github.com/ghuntley/cursed](https://github.com/ghuntley/cursed?ref=ghuntley.com)

[the 💀 cursed programming language: programming, but make it gen z ![Image 3](https://static.ghost.org/v5.0.0/images/link-icon.svg)💀 cursed](https://cursed-lang.org/?ref=ghuntley.com)

the website

[GitHub - ghuntley/cursed: the 💀 cursed programming language: programming, but make it gen z the 💀 cursed programming language: programming, but make it gen z - ghuntley/cursed ![Image 4](https://ghuntley.com/content/images/icon/pinned-octocat-093da3e6fa40-28.svg)GitHub ghuntley ![Image 5](https://ghuntley.com/content/images/thumbnail/cursed-2)](https://github.com/ghuntley/cursed?ref=ghuntley.com)

the source code

whats included?
---------------

Anything that Claude thought was appropriate to add. Currently...

*   The compiler has two modes: interpreted mode and compiled mode. It's able to produce binaries on Mac OS, Linux, and Windows via LLVM.
*   There are some half-completed VSCode, Emacs, and Vim editor extensions, and a Treesitter grammar.
*   A whole bunch of really wild and incomplete standard library packages.

lexical structure
-----------------

**Control Flow:**

`ready`→ if

`otherwise`→ else

`bestie`→ for

`periodt`→ while

`vibe_check`→ switch

`mood`→ case

`basic`→ default

**Declaration:**

`vibe`→ package

`yeet`→ import

`slay`→ func

`sus`→ var

`facts`→ const

`be_like`→ type

`squad`→ struct

**Flow Control:**

`damn`→ return

`ghosted`→ break

`simp`→ continue

`later`→ defer

`stan`→ go

`flex`→ range

**Values & Types:**

`based`→ true

`cringe`→ false

`nah`→ nil

`normie`→ int

`tea`→ string

`drip`→ float

`lit`→ bool

`ඞT`(Amogus) → pointer to type T

**Comments:**

`fr fr`→ line comment

`no cap...on god`→ block comment

example program
---------------

Here is leetcode 104 - maximum depth for a binary tree:

```
vibe main
yeet "vibez"
yeet "mathz"

// LeetCode #104: Maximum Depth of Binary Tree 🌲
// Find the maximum depth (height) of a binary tree using ඞ pointers
// Time: O(n), Space: O(h) where h is height

struct TreeNode {
    sus val normie
    sus left ඞTreeNode   
    sus right ඞTreeNode  
}

slay max_depth(root ඞTreeNode) normie {
    ready (root == null) {
        damn 0  // Base case: empty tree has depth 0
    }
    
    sus left_depth normie = max_depth(root.left)
    sus right_depth normie = max_depth(root.right)
    
    // Return 1 + max of left and right subtree depths
    damn 1 + mathz.max(left_depth, right_depth)
}

slay max_depth_iterative(root ඞTreeNode) normie {
    // BFS approach using queue - this hits different! 🚀
    ready (root == null) {
        damn 0
    }
    
    sus queue ඞTreeNode[] = []ඞTreeNode{}
    sus levels normie[] = []normie{}
    
    append(queue, root)
    append(levels, 1)
    
    sus max_level normie = 0
    
    bestie (len(queue) > 0) {
        sus node ඞTreeNode = queue[0]
        sus level normie = levels[0]
        
        // Remove from front of queue
        collections.remove_first(queue)
        collections.remove_first(levels)
        
        max_level = mathz.max(max_level, level)
        
        ready (node.left != null) {
            append(queue, node.left)
            append(levels, level + 1)
        }
        
        ready (node.right != null) {
            append(queue, node.right)
            append(levels, level + 1)
        }
    }
    
    damn max_level
}

slay create_test_tree() ඞTreeNode {
    // Create tree: [3,9,20,null,null,15,7]
    //       3
    //      / \
    //     9   20
    //        /  \
    //       15   7
    
    sus root ඞTreeNode = &TreeNode{val: 3, left: null, right: null}
    root.left = &TreeNode{val: 9, left: null, right: null}
    root.right = &TreeNode{val: 20, left: null, right: null}
    root.right.left = &TreeNode{val: 15, left: null, right: null}
    root.right.right = &TreeNode{val: 7, left: null, right: null}
    
    damn root
}

slay create_skewed_tree() ඞTreeNode {
    // Create skewed tree for testing edge cases
    //   1
    //    \
    //     2
    //      \
    //       3
    
    sus root ඞTreeNode = &TreeNode{val: 1, left: null, right: null}
    root.right = &TreeNode{val: 2, left: null, right: null}
    root.right.right = &TreeNode{val: 3, left: null, right: null}
    
    damn root
}

slay test_maximum_depth() {
    vibez.spill("=== 🌲 LeetCode #104: Maximum Depth of Binary Tree ===")
    
    // Test case 1: Balanced tree [3,9,20,null,null,15,7]
    sus root1 ඞTreeNode = create_test_tree()
    sus depth1_rec normie = max_depth(root1)
    sus depth1_iter normie = max_depth_iterative(root1)
    vibez.spill("Test 1 - Balanced tree:")
    vibez.spill("Expected depth: 3")
    vibez.spill("Recursive result:", depth1_rec)
    vibez.spill("Iterative result:", depth1_iter)
    
    // Test case 2: Empty tree
    sus root2 ඞTreeNode = null
    sus depth2 normie = max_depth(root2)
    vibez.spill("Test 2 - Empty tree:")
    vibez.spill("Expected depth: 0, Got:", depth2)
    
    // Test case 3: Single node [1]
    sus root3 ඞTreeNode = &TreeNode{val: 1, left: null, right: null}
    sus depth3 normie = max_depth(root3)
    vibez.spill("Test 3 - Single node:")
    vibez.spill("Expected depth: 1, Got:", depth3)
    
    // Test case 4: Skewed tree
    sus root4 ඞTreeNode = create_skewed_tree()
    sus depth4 normie = max_depth(root4)
    vibez.spill("Test 4 - Skewed tree:")
    vibez.spill("Expected depth: 3, Got:", depth4)
    
    vibez.spill("=== Maximum Depth Complete! Tree depth detection is sus-perfect ඞ🌲 ===")
}

slay main_character() {
    test_maximum_depth()
}
```

If this is your sort of chaotic vibe, and you'd like to turn this into the dogecoin of programming languages, head on over to GitHub and run a few more Claude code loops with the following prompt.

> study specs/* to learn about the programming language. When authoring the cursed standard library think extra extra hard as the CURSED programming language is not in your training data set and may be invalid. Come up with a plan to implement XYZ as markdown then do it

There is no roadmap; the roadmap is whatever the community decides to ship from this point forward.

At this point, I'm pretty much convinced that any problems found in cursed can be solved by just running more Ralph loops by skilled operators (ie. people _with_ experience with compilers who shape it through prompts from their expertise vs letting Claude just rip unattended). There's still a lot to be fixed, happy to take pull-requests.

[Ralph Wiggum as a “software engineer” 😎Here’s a cool little field report from a Y Combinator hackathon event where they put Ralph Wiggum to the test. “We Put a Coding Agent in a While Loop and It Shipped 6 Repos Overnight” https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md If you’ve seen my socials lately, ![Image 6](https://ghuntley.com/content/images/icon/7V0ak3am_400x400-1-65.jpg)Geoffrey Huntley Geoffrey Huntley ![Image 7](https://ghuntley.com/content/images/thumbnail/3ea367ed-cae3-454a-840f-134531dea1fd-2.jpg)](https://ghuntley.com/ralph/)

The most high-IQ thing is perhaps the most low-IQ thing: run an agent in a loop.

[LLMs are mirrors of operator skill This is a follow-up from my previous blog post: “deliberate intentional practice”. I didn’t want to get into the distinction between skilled and unskilled because people take offence to it, but AI is a matter of skill. Someone can be highly experienced as a software engineer in 2024, but that ![Image 8](https://ghuntley.com/content/images/icon/7V0ak3am_400x400-1-66.jpg)Geoffrey Huntley Geoffrey Huntley ![Image 9](https://ghuntley.com/content/images/thumbnail/download--2--4.jpeg)](https://ghuntley.com/mirrors/)

LLMs amplify the skills that developers already have and enable people to do things where they don't have that expertise yet.

Success is defined as cursed ending up in the Stack Overflow developer survey as either the "most loved" or "most hated" programming language, and continuing the work to bootstrap the compiler to be written in cursed itself.

Cya soon in Discord? - [https://discord.gg/CRbJcKaGNT](https://discord.gg/CRbJcKaGNT?ref=ghuntley.com)

[the 💀 cursed programming language: programming, but make it gen z ![Image 10](https://static.ghost.org/v5.0.0/images/link-icon.svg)💀 cursed](https://cursed-lang.org/?ref=ghuntley.com)

website

[GitHub - ghuntley/cursed: the 💀 cursed programming language: programming, but make it gen z the 💀 cursed programming language: programming, but make it gen z - ghuntley/cursed ![Image 11](https://ghuntley.com/content/images/icon/pinned-octocat-093da3e6fa40-29.svg)GitHub ghuntley ![Image 12](https://ghuntley.com/content/images/thumbnail/cursed-3)](https://github.com/ghuntley/cursed?ref=ghuntley.com)

source code

ps. socials

> I ran Claude in a loop for 3 months and created a brand new "GenZ" programming language.
> 
> 
> It's called [@cursedlang](https://twitter.com/cursedlang?ref_src=twsrc%5Etfw&ref=ghuntley.com).
> 
> 
> v0.0.1 is now available, and the website is ready to go.
> 
> 
> Details below! [pic.twitter.com/Ku5kbWMRgR](https://t.co/Ku5kbWMRgR?ref=ghuntley.com)
> 
> — geoff (@GeoffreyHuntley) [September 9, 2025](https://twitter.com/GeoffreyHuntley/status/1965258228314636524?ref_src=twsrc%5Etfw&ref=ghuntley.com)