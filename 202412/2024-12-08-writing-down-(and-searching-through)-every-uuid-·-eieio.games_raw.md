Title: Writing down (and searching through) every UUID · eieio.games

URL Source: https://eieio.games/blog/writing-down-every-uuid/

Published Time: 2024-12-04T00:00:00.000Z

Markdown Content:
[](https://eieio.games/blog/writing-down-every-uuid/)

I couldn't remember every UUID so I wrote them all down

Dec 4, 2024

I’ve been struggling to remember all of the UUIDs 1. There are a lot of them. So this week I wrote them all down. You can see my list at [everyuuid.com](https://everyuuid.com/).

The site looks like this - UUIDs are displayed in a random-ish but consistent order and you can quickly search for one that you like:

Loading...

it's so much easier to remember them all now

I think the site is great. I can quickly find my favorite UUIDs and star them or browse them all to find one that’s just right.

But having 5,316,911,983,139,663,491,615,228,241,121,378,304 2 possible values made it way harder than it needed to be to write them all down. I’m not sure why the authors of the UUID spec wanted to include so many bits!

2

While UUID have 128 bits, UUID v4s reserve 4 bits for the version and 2 or 3 bits for the variant. I chose the 2-bit variant, which left me with 122 bits of entropy.

So I think the final implementation here is pretty interesting. Let me tell you about it.

The challenges
--------------

This problem had a few major challenges:

*   Browsers do not want to render a window that is over a trillion trillion pixels high, so I needed to handle scrolling and rendering on my own 3
*   I didn’t want to generate UUIDs in order from first to last. We all know the good UUIDs are in the middle! So I needed a way to _generate_ UUIDs that ensured that I generated them all once.
*   Since I was handling scrolling and rendering on my own, `ctrl-f` didn’t really work for search. I wanted to search through every UUID, not just the ones I could see! So I had to implement that too.

3

Again, this would all be so much easier if UUIDs were just a little shorter.

Challenge 1: rendering
----------------------

Originally I figured I’d make a very very tall div only render the UUIDs that I could see. This is the approach that I took with [One Million Checkboxes](https://eieio.games/blog/one-million-checkboxes) and it worked great there.

The idea is that creating trillions of dom nodes is expensive, but having a very high scroll position isn’t (it’s still a single number!). So you make a div that is tall enough to contain all your elements and then just render the ones that are close by (along with a buffer) 4.

But unfortunately, [browsers have a maximum scroll position](https://stackoverflow.com/questions/10882769/do-the-browsers-have-a-maximum-height-for-the-body-document). I’m not entirely sure what that is across all browsers now, but it seems like it’s probably stored as a 32 bit int in at least some browsers. And even if it was a 64 bit int and we were displaying our UUIDs with a height of 1 pixel, we’d need orders of magnitude more scroll space.

![Image 9: Chatgpt saying 'Displaying 2^122 values directly in a browser is infeasible due to extreme numerical and computational limitations. Let's break this down:'](https://eieio.games/images/writing-down-every-uuid/chatgpt-no-faith.png)

chatgpt had no faith here

My solution was a little finicky to implement, but conceptually pretty simple:

*   Don’t do any “real” scrolling. Fix the height of the page to the height of the browser
*   Store a virtual scroll position in a [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt); update it whenever the user performs a scroll-like action.
*   Render UUIDs based on the scroll position - if we’re at position 1,000 then render UUID 1000, 1001, etc.

This was finicky largely because there’s a lot of stuff that the browser does for you when it comes to scrolling. So if you want a good user experience there’s a lot of stuff that you need to remember to re-implement.

You need to handle mouse wheel and touch events yourself. You need to find all the (platform-specific!) hotkeys for scrolling and add those. You need to add your own scrollbar, and if you want a nice scrolling animation you have to add that yourself too. None of this is that hard, there’s just a lot of it - for example, here’s my hotkey handling code (I’m sure I missed plenty of stuff):

hotkey handling code

```
// cmdKey is mapped to meta or ctrl depending on the platform
switch (true) {
  case handleKeyAndPrevent("ArrowDown", [cmdKey], () => {
    animateWithDelta(MAX_POSITION);
  }):
    return;
  case handleKeyAndPrevent("ArrowUp", [cmdKey], () =>
    animateWithDelta(-MAX_POSITION)
  ):
    return;
  case handleKeyAndPrevent(" ", [shiftKey], () => {
    animateWithDelta(-PAGE_SIZE);
  }):
    return;
  case handleKeyAndPrevent(" ", [], () => {
    animateWithDelta(PAGE_SIZE);
  }):
    return;
  case handleKeyAndPrevent("PageDown", [cmdKey], () => {
    animateWithDelta(MAX_POSITION);
  }):
    return;
  case handleKeyAndPrevent("PageUp", [cmdKey], () => {
    animateWithDelta(0n);
  }):
    return;
  case handleKeyAndPrevent("PageDown", [], () => {
    animateWithDelta(PAGE_SIZE);
  }):
    return;
  case handleKeyAndPrevent("PageUp", [], () => {
    animateWithDelta(-PAGE_SIZE);
  }):
    return;
  case handleKeyAndPrevent("Home", [], () => animateWithDelta(0n)):
    return;
  case handleKeyAndPrevent("End", [], () => animateWithDelta(MAX_POSITION)):
    return;
  case handleKeyAndPrevent("ArrowDown", [], () => movePosition(1n)):
    return;
  case handleKeyAndPrevent("ArrowUp", [], () => movePosition(-1n)):
    return;
  default:
    break;
}
```
That said, most of this was well within Claude’s abilities - for example, it slammed out a pretty reasonable easing-based scroll implementation when I asked:

scroll animation

```
const startPosition = virtualPosition;
const startTime = performance.now();
const duration = 300;

const animate = () => {
  const currentTime = performance.now();
  const elapsed = currentTime - startTime;
  const progress = Math.min(elapsed / duration, 1);
  const easeProgress = 1 - Math.pow(1 - progress, 4);
  const currentPos =
    startPosition +
    ((targetPosition - startPosition) *
      BigInt(Math.floor(easeProgress * 1000))) /
      1000n;
  setVirtualPosition(currentPos);

  if (progress < 1) {
    animationRef.current = requestAnimationFrame(animate);
  } else {
    setVirtualPosition(targetPosition);
    setIsAnimating(false);
    setTargetPosition(null);
  }
};

animationRef.current = requestAnimationFrame(animate);
```
So this got me to a list of all of the UUIDs. I added some other important functionality - for example, if I see a UUID that I wanted to be able to favorite it (to come back to it later) or to copy it to my clipboard. And that gave me something like this:

Loading...

pretty boring to scroll through!

That…works. But the UUIDs are displayed in a super obvious order. Scrolling through a list of UUIDs should be exciting! I wanna see bb166283-2e09-4b72-ba32-70a43521c70e, not 00000000-0000-4000-8000-000000000000!

We can certainly do better.

Challenge 2: ordering
---------------------

I wanted to display the UUIDs in an interesting order. I came up with the following constraints:

*   There should be no distinguishable pattern to the UUIDs displayed
*   We should display every UUID exactly once
*   UUIDs should be displayed in a consistent order

After all, it’d be disappointing if you scrolled through every UUID and realized that you hadn’t seen one. And it’d be very hard to show someone a UUID that you found if you couldn’t scroll back to the same spot to find it.

So: we need to map our integer indices to UUIDs in an interesting way. How do we do that?

The first idea I came across was a [linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) (LCG). An LCG generates pseudo-random numbers using the following formula:

> X(N+1) = (A \* X(N) + c) mod M

That is, to get the “next” term, you take the previous term, multiply it by `A`, add `C`, and take that mod `M`.

For reasons that are beyond me, if `M` is a power of 2, `M` and `C` share no common factors, `A-1` is divisible by all prime factors of `M`, and `A-1` is divisible by 4 if `M` is divisible by 4 5, you will generate all values below `M` before you get any repeats.

5

The divisible by 4 part is absolute magic to me

So this seemed like a good fit! We can set `M` to 2^122, choose any odd number for `C`, and easily pick an `A` that is 1 above a number divisible by 4. But I quickly ran into problems.

```
Position    UUID
--------------------------------------------------
0            00000000-0000-8000-4000-000000000000
1            00000000-0000-8000-4000-000000000005
2            00000000-0000-8000-4000-000000000032
3            00000000-0000-8000-4000-0000000001c7
4            00000000-0000-8000-4000-000000001004
```

There’s a table of some UUIDs generated using 9 for `A` and 5 for `C`. The UUIDs sure don’t look random! And that makes sense. If we want to see anything but 0s for the high bits of the second UUID that we generate, we need `A*C` to approach 2^122 - so they’d need to each be close to 2^61. Those are big numbers to multiply together, but computers are fast these days.

But that gets tricky when generating later terms. While there are ways to “skip steps” with LCGs - that is, to generate the LCG for input 1,000,000 without generating the 999,999 prior calculations - I found it hard to get that math working consistently with large constants because the intermediate steps were _so big_.

![Image 10: text from the wikipedia article on LCGs. The phrase ' (The low-order bits of LCGs when m is a power of 2 should never be relied on for any degree of randomness whatsoever.)' is highlighted](https://eieio.games/images/writing-down-every-uuid/lcg-no-randomness.png)

wikipedia brought me back down to earth

As I was working through that problem I noticed that Wikipedia said “the low-order bits of LCGs when m is a power of 2 should never be relied on for any degree of randomness whatsoever.” So I decided to pivot.

### Entropy and bijectivity

So I wanted to add more entropy to the displayed UUIDs - but to display each UUID exactly once. Mathematicians would say I wanted a _bijective_ mapping - that is, for each index to be mapped to exactly one UUID (and vice-versa).

I found bijectivity hard to reason about! I knew my original mapping was bijective (it’s very clear that index 0 maps to UUID 00000000-0000-4000-8000-000000000000 6 and vice-versa), but how could I tell whether I was preserving that bijectivity when adding entropy? Could I take my index and add a constant to it? Could I multiply each index by 1000?

6

Remember that some bits of a UUID are reserved - that’s why the UUID isn’t filled with 0s.

![Image 11: text from wikipedia: A bijection, bijective function, or one-to-one correspondence between two mathematical sets is a function such that each element of the second set (the codomain) is the image of exactly one element of the first set (the domain). Equivalently, a bijection is a relation between two sets such that each element of either set is paired with exactly one element of the other set.
The text goes on to explain that a function is bijective if and only if it is invertible.](https://eieio.games/images/writing-down-every-uuid/wikipedia-bijective.png)

Wikipedia was very intimidating and then very helpful on this point

But eventually I stumbled on an observation that is probably obvious to many of you but blew my mind: **as long as I could always reverse the steps that I took, I had preserved bijectivity.**

The way I think about this is:

*   I have a function. It takes in an index and returns exactly one UUID. It always returns the same UUID for the same input
*   The way that I add entropy is reversible, which means that I can take a UUID, reverse the steps that I took, and recover the index that generated it
*   Having a duplicate would require two indices to have the same UUID
*   Which would mean that I couldn’t recover one of those two indices by reversing the steps that I took
*   But we said we could always do that!

Maybe this is silly to you. But framing the problem as “come up with a function that looks like it adds entropy but is reversible” was a lot easier for me to think about than “preserve bijectivity between these two sets.” 7

7

Look, I’m a college dropout, leave me alone

So this gave me a new approach. To try to write it down with some precision:

*   We’re given 122 bits of input (for index 0 all of those bits happen to be 0, but they’re there)
*   We can do _anything_ we want to those bits to add entropy as long as:
    *   We end up with exactly 122 bits (the number we need to create a UUID)
    *   We can take our final 122 bits and recover the original 122 bits

So “multiply by a large number” was out 8, since that would increase our number of bits. But `XOR` was very much alive, since if you `XOR` a number with some other number twice, you get back the original number.

8

I think this is not always strictly true and that some forms of multiplication and modding are always reversible, but I didn’t understand the domain well enough to try this.

### Feistel ciphers

So I wanted to preserve the number of bits that I had and add some entropy in a reversible way. A cipher seemed like a good approach - the whole idea of a cipher is to scramble text in an interesting but totally-reversible (if you know how) way!

I’m sure there are lots of good options here, but I settled on a [feistel cipher](https://en.wikipedia.org/wiki/Feistel_cipher) because it was easy for me to see how it would satisfy my constraints. Feistel ciphers are cool and very elegant. The basic idea looks like this:

```
# This isn't quite valid code, but it's good enough!

round_constants = [1, 2, 3] # big numbers here

def produce_cipher_text(unscrambled):
    left = unscrambled[:len(unscrambled) // 2]
    right = unscrambled[len(unscrambled) // 2:]
    for round in round_constants:
        seed = round_function(right, round) # seed is a function of right
        newRight = left ^ seed # new right is XOR of old left and the seed
        left = right # new left side is the old right side
        right = newRight

    return left + right

def round_function(right, round):
    # do anything you want with right_side and round
    # to produce an interesting seed
    # truncate the seed to have the same number of bits as right
    pass
```

That is, split your input into two chunks. Several times in a row, feed the “right” chunk into a function that produces some interesting value. XOR that output with your left chunk and make that your new right chunk. Make your new left chunk equal to your old right chunk. And then smush the chunks back together at the end.

And what’s really cool about this is that it is reversible for _any_ round function, as long as the round function is pure 9.

9

Produces the same output for the same input

That was originally confusing to me - why is it ok for `round_function` to be basically anything? Can it do something silly like always return 1? To see why that’s ok, we can look at the steps to reverse a feistel cipher:

```
round_constants = [1, 2, 3] # big numbers here

def unscramble(scrambled):
    left = scrambled[:len(unscrambled) // 2]
    right = scrambled[len(unscrambled) // 2:]
    for round in reversed(round_constants):
        oldRight = left
        seed = roundFunction(oldRight, round)
        oldLeft = right ^ seed
        left = oldLeft
        right = oldRight

    return left + right

def round_function(right, round):
    # same as above
    pass
```

The trick here is that we can always recover our “seed” (because it’s the left chunk of our current iteration), and from that we can always recover our old left chunk (because XORing something twice produces the original input). And that means that if `round_function` always returned 1 (or something equally silly), our data might not be mixed particularly well - but it’d still be recoverable.

I implemented a feistel cipher and tweaked my round function until it scrambled my UUIDs in a satisfying way. This was pretty straightforward; my round implementation (suggested by claude) is a bunch of bit shifts and XORs with some multiplication mixed in.

```
const ROUND_CONSTANTS = [
  BigInt("0x47f5417d6b82b5d1"),
  BigInt("0x90a7c5fe8c345af2"),
  BigInt("0xd8796c3b2a1e4f8d"),
  BigInt("0x6f4a3c8e7d5b9102"),
  BigInt("0xb3f8c7d6e5a49201"),
  BigInt("0x2d9e8b7c6f5a3d4e"),
  BigInt("0xa1b2c3d4e5f6789a"),
  BigInt("0x123456789abcdef0"),
];

function feistelRound(block, round) {
    // Mix using rotations, XORs, and addition, maintaining 61-bit blocks
    let mixed = block;
    mixed ^= ROUND_CONSTANTS[round] & ((BigInt(1) << BigInt(61)) - BigInt(1));
    mixed =
    ((mixed << BigInt(7)) | (mixed >> BigInt(54))) &
    ((BigInt(1) << BigInt(61)) - BigInt(1));
    mixed =
    (mixed \* BigInt("0x6c8e944d1f5aa3b7")) &
    ((BigInt(1) << BigInt(61)) - BigInt(1));
    mixed =
    ((mixed << BigInt(13)) | (mixed >> BigInt(48))) &
    ((BigInt(1) << BigInt(61)) - BigInt(1));

    return mixed;
}

```

But then I needed to take my scrambled bits and turn them back into a UUID. And that was surprisingly tricky!

#### Aside: bit twiddling is hard

If we didn’t care about generating valid UUID v4s, we could just generate 2^128 numbers, scramble them, convert the resulting bits into a hex string, and intersperse some dashes. But it’d be heartbreaking if someone found a UUID on the site only to realize that it didn’t correspond to the V4 standard. A UUID V4 must look like this:

```
UUID V4 format. Values:
X: any 4 bits
4: these 4 bits must be 0100 (4)
V: the top two bits here are 10; valid values are 8, 9, A, B

XXXXXXXX-XXXX-4XXX-VXXX-XXXXXXXXXXXX
```

It’s a little awkward to take our two chunks of 61 bits and map it onto the available bits here. We need to do something like this:

```
XXXXXXXX-XXXX     - take these 48 bits from left
4XXX              - skip the next 4 bits (for the version)
                    and take 12 more bits from left
V                 - skip the next 2 bits (for the variant)
                    and add the last bit from left
XXX-XXXXXXXXXXXX  - the lower 61 bits come from right
```

I’m sure that someone more comfortable with bit twiddling would have come up with a better approach here. But I couldn’t think of a solution other than carefully twiddling all of the bits into place:

careful bit twiddling

```
function indexToUUID(index) {
  let initialLeft = BigInt(index) >> BigInt(61);
  let initialRight = BigInt(index) & ((BigInt(1) << BigInt(61)) - BigInt(1));
  let { left, right } = runFeistel({ initialLeft, initialRight });

  let result = BigInt(0);
  // first 48 bits from the left
  // left: 13 bits remaining; right: 61 bits remaining; total: 48 bits used
  result |= (left >> BigInt(13)) << BigInt(80);
  // 4 bits for version
  // left: 13 bits remaining; right: 61 bits remaining; total: 52 bits used
  result |= BigInt(4) << BigInt(76);
  // next 12 bits from left
  // left: 1 bit remaining; right: 61 bits remaining; total: 64 bits used
  const next12BitsFromLeft =
    (left >> BigInt(1)) & ((BigInt(1) << BigInt(12)) - BigInt(1));
  result |= next12BitsFromLeft << BigInt(64);
  // 2 bits for variant
  // left: 1 bit remaining; right: 61 bits remaining; total: 66 bits used
  result |= BigInt(2) << BigInt(62);
  // 1 bit remaining from the left!
  // left: 0 bits remaining; right: 61 bits remaining; total: 67 bits used
  const lastBitFromLeft = left & BigInt(1);
  // good to use all the bits from the right
  result |= lastBitFromLeft << BigInt(61);
  result |= right;

  let hex = result.toString(16).padStart(32, "0");
  return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(
    12,
    16
  )}-${hex.slice(16, 20)}-${hex.slice(20)}`;
}
```
This was bug-prone for me (I am bad at bit twiddling) and an area where LLMs seemed to really struggle - maybe because the process is mathy. I had to draw everything out to get it working.

But eventually it worked. And it gave me a very nice list of random-looking but consisently-ordered UUIDs:

Challenge 3: search
-------------------

Shuffling the order of displayed UUIDs posed a problem - how could I find the UUIDs that I liked? Back when the UUIDs were more ordered I could at least try to scroll to the right area to find one, but that didn’t work now. So I needed to add search.

Because our mixing function was reversible, adding search for a _specific_ UUID was actually pretty easy. We just take the UUID, un-scrambled it to retrieve its original index, and then jump to that index!

So I added a little search widget that did just that. But that definitely wasn’t enough - a search function should be able to search for substrings!

### Full text search

The next step was also pretty straightforward. I knew all of the UUIDs in view, so I could easily add full-text search over them. And I could extend that buffer to include UUIDs above and below where I was currently looking and search over those too.

Loading...

we're getting somewhere

But - and this is really a spot where you wonder why the UUID spec authors thought we needed so many UUIDs - I couldn’t make those buffers trillions of items large to hold all the UUIDs! That’s too much RAM! I needed to take a different approach.

### What do I do with search strings?

I couldn’t search over all of the UUIDs directly. But maybe I could take in the search string and then back out some UUIDs that fit it. Something like:

*   Take in the current search string
*   Find all of the places the string could fit within a UUID
*   Choose one of those places and fill in the surrounding digits to make a valid UUID

So for example, if the user typed the string `A`, that could go in 31 different positions in the UUID (there are 32 characters but one must be a 4). But `AAAAA-` that could only go in a single position, since it has more than 4 digits (so it must go in the first or last grouping) and a trailing dash (so it can’t go in the last grouping, and must instead be be the last 5 characters of the first grouping, followed by a dash).

Maybe it’s just because I was tired, but I _massively_ overcomplicated this problem to start. I thought I needed to do something like:

*   Split the search string on `-` and group it into chunks
*   Analyze each chunk figuring out where it could go (long chunks must go first or last, etc)
*   Use that to determine which digits we still need to fill in to generate a valid UUID

I went in circles, throwing away a ton of code that looked like this:

Lots of bad code you don't need to see

```
const KINDS = {
  twelve: 12,
  eight: 8,
  four: 4,
};

function selectableIndices(kind, chunks) {
  const maxBits = KINDS[kind];
  const indices = [];
  for (let i = 0; i < chunks.length; i++) {
    if (chunks[i].length <= maxBits) {
      indices.push(i);
    }
  }
}

const emptySearchIndex = (index, maxChars) => ({
  index,
  maxChars,
  value: null,
});

function candidatesForSearchString(search, rand) {
  const randInt = (high) => Math.floor(rand() * high);

  const randHexChar = () => {
    const digit = randInt(16);
    return digit.toString(16);
  };

  const chunks = search.split("-");
  const indices = [
    emptySearchIndex(0, 8),
    emptySearchIndex(1, 4),
    emptySearchIndex(2, 4),
    emptySearchIndex(3, 4),
    emptySearchIndex(4, 12),
  ];

  const chunksWithMetadata = chunks.map((chunk, index) => ({
    index,
    chunk,
    greaterThan4: chunk.length > 4,
    greaterThan8: chunk.length > 8,
  }));

  // const chunksSortedByLength = [...chunks].map((chunk, i) => {chunk, i}
  //   sort((a, b) => b.length - a.length);
  const greaterThan8 = chunks.filter((chunks) => chunks.length > 8);
  const greaterThan4 = chunks.filter((chunks) => chunks.length > 4);
  if (greaterThan8.length > 0 && greaterThan4.length > 0) {
  }

  let minIndex = 0;
  for (const chunk of chunks) {
    let found = false;
    for (let i = minIndex; i < indices.length; i++) {
      const index = indices[i];
      if (index.maxChars >= chunk.length && index.value === null) {
        found = true;
        minIndex = i;
        index.value = chunk;
        break;
      }
    }
    if (!found) {
      return null;
    }
  }
  // const choices = indices.filter((index, indexIdx) => {
  //   return index.maxChars >= chunk.length && index.value === null;
  // });
  // if (choices.length === 0) {
  //   return null;
  // }
  // // const choice = choices[randInt(choices.length)];
  // const choice = choices[0];
  // choice.value = chunk;
  // chunkIdx++;

  for (const index of indices) {
    if (index.value === null) {
      index.value = "0".repeat(index.maxChars);
    } else if (index.value.length < index.maxChars) {
      const remaining = index.maxChars - index.value.length;
      index.value += "0".repeat(remaining);
      // index.value = index.value + randHexChar();
    }
  }

  return indices.map((index) => index.value).join("-");
}
```
One theme of this project was that Claude really struggled with what I was asking it to do, and that was certainly true here - Claude was as confused about the problem as I was.

![Image 12: output from the LLM agent claude. it says 'I think I still haven't gotten it quite right - I can see some inconsistencies in my implementation vs the rules you laid out. Would you point out what I'm still missing?'](https://eieio.games/images/writing-down-every-uuid/claude-confused.png)

I'm the LLM now

But at some point I took a step back and realized there was a much simpler solution. Since we want the user’s search string to appear verbatim in any UUID that we match, we can simply:

*   Take their input
*   Ask “could this input string go at the start of a UUID?”
*   Ask “could this input string go at the second character of a UUID?”
*   etc

Visually, that looks something like this:

XAny hex character

\-Must be a dash

4 (version)Must be a 4

V (variant)Must be \[8, 9, A, B\]

4AAB-

XXXXXXXX-XXXX-4XXX-VXXX-XXXXXXXXXXXX

Dashes in the search must in the right spot. If a search character overlaps with the version character it must be a 4. And if a search character overlaps with the variant character it must be an 8, 9, A, or B.

### Generating UUIDs

Search string processing gave me a set of valid patterns; those patterns would look like this for the string “4AAA-”:

```
# valid patterns for 4AAA-
XXXX4AAA-XXXX-4XXX-VXXX-XXXXXXXXXXXX
XXXXXXXX-4AAA-4XXX-VXXX-XXXXXXXXXXXX
XXXXXXXX-XXXX-4AAA-VXXX-XXXXXXXXXXXX
```

What do we do with those?

Well, what we _want_ to do is something like:

*   Feed those patterns into our unscrambler and determine which bits would need to be set in our input index in order to output that pattern
*   Find the index closest to our current position that has those bits set

Now clearly we can’t just feed those patterns into our unscrambler as-is; they’re not valid UUIDs! But that’s the idea behind what we’d want to do.

And it’s here that I hit a wall. The dependency graph for any bit spit out of our cipher was wildly complicated.

At first I thought I could fix this by using a different scrambling technique - maybe I could change the semantics of my cipher, or use a known “bad” crypto algorithm and exploit its breakability.

But those ideas were fundamentally at odds with my goal around presentation:

*   For the UUIDs to appear randomly ordered, I _needed_ each input bit to affect every output bit
*   But to reason about the dependency graph of a bit effectively, I _needed_ each input bit to only affect a few output bits

Anything I did to improve one problem made the other problem harder!

Here I was left with a feeling that if I had a better understanding of cryptanalysis I might be able to make some headway. But getting the MVP of this project out the door seemed too valuable to divert into studying for that long 10 - people need to browse UUIDs.

So I punted.

My solution was pretty simple. For search, I just:

*   Take the patterns that I generated while analyzing search strings
*   Repeatedly filled in the remaining digits to generate valid UUIDs
*   Took the “best” one - the one closest to the current position

Loading...

better than nothing

And this…works pretty well! It’s not perfect, but it certainly lets you cycle through a large set of matching UUIDs.

Missing features and wrapping up
--------------------------------

Flaws of the UUID spec aside, I’m glad that I finally have all the UUIDs in one place.

There are a few things that I think the site is currently missing. Having more social features would be really neat - maybe you could see the UUIDs your friends have favorited so that you could use those UUIDs too? Or maybe the site could feature “trending UUIDs” that are particular popular across the world right now.

And of course I’m still very curious whether there’s a cryptanalysis approach that lets me achieve more effective search over a random-ish ordering of UUIDs. I’m gonna do some more reading there.

But all that said, I’m very happy to have launched the site in its current state. I hope you get as much utility out of it as I do.
