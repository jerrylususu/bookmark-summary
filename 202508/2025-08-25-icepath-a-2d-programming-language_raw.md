Title: Icepath: a 2D Programming Language

URL Source: https://healeycodes.com/icepath-a-2d-programming-language

Markdown Content:
I've made a little 2D programming language called Icepath. Named after the [ice puzzles](https://bulbapedia.bulbagarden.net/wiki/Ice_Path) in Pokémon Gold and Silver. The vibe I was going for was sliding around a cave and hitting opcodes.

Below, you can see a program running. The program's source code is also a map of execution. Take a second and see if you can reverse engineer how it works and what the opcodes do.

###########################

#@o|>&!±#

##

#l h#

#>&l&e&^#

###########################

An Icepath program contains opcodes and literals. The cursor starts at the `@` (start pointer) and faces right. It moves around the source code like a grid, following its current direction until it hits an opcode like `|`, `>`, `<`, `^` (down, right, left, up).

Programs halt when the cursor lands on `±`.

It uses a stack machine. Numbers can be added by placing two literals followed by `+` (addition) like `1 2 +` which leaves `3` on the stack.

In order to join characters and create strings, `&` (join) pops the top two values and concatenates as strings in top-then-next order; numbers are stringified. So with ... `l o &` you get `lo` (the top of stack `o` comes first, then the next item `l`).

// Pop two and join as string

if (nextChar === "&") {

stack.push([pop(stack), pop(stack)].join(""));

continue;

}

`!` pops and prints the top of the stack – writing the repeatedly joined string `hello` to stdout.

Fibonacci
---------

One of the first programs I try to write in a programming language that I've created is calculating part of the Fibonacci sequence. This requires math opcodes and the ability to keep track of some state, with an output that I recognize. For my other languages, it has been a good performance benchmark as well (I haven't optimized Icepath but an optimizing compiler would be interesting).

##################################################

#@>9 1+1 0||<#

#>>:!~;+R 1-:0=R R^#

#±#

##################################################

The program above calculates the first 10 numbers in the Fibonacci sequence. It uses two constructs which require logical opcodes. You may have noticed that by using direction pointers, we can direct the cursor to follow a circular pattern. A loop.

To escape this loop and halt, I've used `=` (equals) which pops two items from the stack and alters the direction of the cursor to point downwards if they are equal. In this case, we're checking if the counter has hit `0` meaning that we've output the required 10 numbers.

Since we're limited by not having variables, like `a = 1`, we need to store the counter on the stack. But there are other items we need to store on the stack too:

*   Counter (e.g. `10`).
*   Last Fibonacci number (e.g. `3`).
*   Current Fibonacci number (e.g. `5`).

There are four opcodes that allow us to manage this state:

*   `R` is used to perform a three-element rotation where `a b c` becomes `b c a`.
*   `:` duplicates the top of the stack.
*   `;` duplicates the second from the top.
*   `~` swaps the top two elements.

By using these, we can move the counter around, decrease it, and check if it's hit zero yet. All while adding together the last two Fibonacci numbers to find the next one.

Note that we start by adding `9` and `1`. This is because we can't write `10` – that's two characters. So we need to add two numbers to reach `10`. You'll also see `1 0` elsewhere – those are the seed values for Fibonacci, not the literal `10`.

Ladders and Boulders
--------------------

There are some more features from the Ice Path [cave puzzles](https://bulbapedia.bulbagarden.net/wiki/Ice_Path) that I've been trying to bring in.

The cave sections of my language are arbitrary; in fact, if the cursor lands on `#` it just gets pushed to the stack as a character. I use them to mark out and separate parts of a program.

Below is my ladder demo that lets the cursor travel back-and-forth between two cave sections. The direction is maintained and the ladder works like a teleport.

###################

#@3 5 8|#

#>~‖#

###################

#‖R<#

###################

Another feature I'm looking into is the ability to push boulders onto trigger areas. This would mean that the grid becomes mutable. One of the earliest 2D programming languages, [Befunge](https://en.wikipedia.org/wiki/Befunge), had a mutable grid. However, that language was designed to be as hard to compile as possible!

Implementation
--------------

After I had put the idea down on paper, implementing the interpreter in TypeScript felt a little bit like an Advent of Code problem. It took me an hour or so to get it working, and then 30 minutes to get the first version of `fibonacci.ice` working. Funnily enough, the trickiest part was getting it to render here on the page you're reading.

const grid = Array.from({ length: width }, (_, x) =>

Array.from({ length: height }, (_, y) => rawLines[y]?.[x])

); // grid[x][y]

const stack: (string | number)[] = [];

let cursor: Cursor = findInit(grid);

let stdout: (string | number)[] = [];

while (true) {

await render(fp, file, cursor, stack, stdout, setTerminal);

cursor = move(cursor);

const nextChar = grid[cursor.x]?.[cursor.y];

// Handle ladder climbing (teleport to other ladder)

if (nextChar === "‖") {

const otherLadder = findOtherLadder(grid, cursor);

cursor.x = otherLadder.x;

cursor.y = otherLadder.y;

continue;

}

// ROT (3-element rotation) a b c -> b c a

if (nextChar === "R") {

const a = pop(stack);

const b = pop(stack);

const c = pop(stack);

stack.push(b);

stack.push(a);

stack.push(c);

continue;

}

// .. rest of ops

}

I've been enjoying playing with stack machine languages since I worked on a [VM for my Lisp](https://healeycodes.com/compiling-lisp-to-bytecode-and-running-it). I'd like to see if I can get the Fibonacci program to use fewer opcodes. To really strip back what's required.

Icepath isn't doing anything that new but I like it. I think it's cute.

It would be cool to take a swing at something very original, like [Hexagony](https://esolangs.org/wiki/Hexagony) where the cursor follows a hexagonal grid – and the memory layout also resembles a _separate_ hexagonal grid.