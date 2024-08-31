Title: why lowercase letters save data

URL Source: https://endtimes.dev/why-lowercase-letters-save-data/

Markdown Content:
Lowercase letters and uppercase letters use the same amout of data — `1 byte` each.

So, it's surprising to learn that swapping uppercase letters for lowercase letters saves data.

For example: I took the front page of [Hacker News](https://news.ycombinator.com/) and rewrote the title of each article in `sentence case` instead of `title case` — reducing the size by `31 bytes`.

How can it be true that changing a few uppercase letters to lowercase letters saves data? The answer is **compression**.

It isn't intuitive, but once you understand how text compression works, it will begin to make sense.

In this article I hope to…

*   Help you understand how text compression works, using **interactive examples**!
*   Show you how I came to the conclusion that `title case` on hacker news emits the **equivalent yearly carbon as a car driving the width of Sri Lanka.**
*   Show you some examples of where this knowledge can be used to **systematically save data.**

Text compression is more effective when…

*   There's a smaller variety of characters in the text
*   The less common characters use used less frequently
*   Characters or groups of characters are repeated more often.

Replacing uppercase characters with their more common lowercase counterparts helps with all three of these.

To understand why this works you need to understand how compression works.

How does text compression work? [#](https://endtimes.dev/why-lowercase-letters-save-data/#how-does-text-compression-work)
-------------------------------------------------------------------------------------------------------------------------

To explain how text compression works, we'll specifically look at the `deflate` algorithm commonly used in `zip` files. The principles are the same for other algorithms too.

Deflate uses two compression methods — `Huffman encoding` and `LZSS` — both of these compression methods are effected by replacing uppercase letters with lowercase.

### Huffman encoding [#](https://endtimes.dev/why-lowercase-letters-save-data/#huffman-encoding)

The deflate algorithm starts with `Huffman encoding`.

Each character in an uncompressed text file uses up the same amount of data. (This isn't exactly true, but is true enough for this explanation.)

In `utf-8` this is `8 bits`. (a bit is a binary `1` or `0`)

A text file using `utf-8` encodes the letters like this:

`B` is `01000010`

`b` is `01100010`

`a` is `01100001`

`o` is `01101111`

Now, take a word that only uses those four characters, say `Baobab`.

Using `utf-8` the text `Baobab` is encoded like this: `010000100110000101101111011000100110000101100010`.

If we know we don't need any other letters, we can save a lot of data by changing the encoding to use fewer bits.

We could change `B` to `10`, `b` to `11`, `a` to `00`, and `o` to `01`.

The text `Baobab` would compress to `100001110011`.

The word `Baobab` contains four distinct characters, the best we can do is give them each a `2-bit` sequence.

But if we lowercased the `B`, we'd only have three distinct characters, and we could take things a step further.

We could change the encoding so that the most frequently used character, `b`, is represented by only `1-bit`. Reducing the compressed version of `baobab` to `101001011`

We do this using `Huffman encoding`.

**Using `Huffman encoding` we can represent more frequently used characters with fewer bits.**

Here's an interactive explanation for how it works. Enter text below to see its uncompressed and compressed binary forms.

To compress our text using huffman encoding we first need to build a frequency table of all the characters in our text. To do this we…

1.  **count the number of each character**
2.  **order them by frequency**.

Then we build a **Huffman tree** following these rules:

1.  Make each character a `leaf` in our tree.
2.  Take the two characters with the lowest frequency and connect them with a node — give that node the combined frequency of both our leaves.
3.  Remove those two leaves from the list — and add their connecting node to the list instead.
4.  Repeat the above steps until there are no more leaves or nodes left in the list.

It's a little complicated but once you're done you can make a pretty diagram like this:

We can use the above tree to work out the new encoding for each of our characters.

To determine each character's encoding, we begin at the top of the tree and climb down towards the character to find its encoding. Each time we climb dow to the left we add a `0`, when we go down to the right we add a `1`.

The characters that appear more frequently in our text require a shorter climb down the tree — and so can be encoded with fewer `1s` and `0s`.

### More savings with smaller trees [#](https://endtimes.dev/why-lowercase-letters-save-data/#more-savings-with-smaller-trees)

We can't decode `Huffman encoding` without the tree. So when we send text compressed with `Huffman encoding` we send the tree along too.

**By using fewer uppercase letters in our text, we increase the chance of their being no instance of any given uppercase letter. Meaning the tree we send is smaller too.**

For instance if we change the text "Decompression is the Mission of the Compression Commission" from `title case` to `sentence case` we don't need a leaf in our tree for uppercase `M` and `C`. This makes our compression more efficient — but also makes the `Huffman tree` smaller.

LZSS [#](https://endtimes.dev/why-lowercase-letters-save-data/#lzss)
--------------------------------------------------------------------

`Deflate` also uses another compression method. It compresses data with `Huffman encoding` and then again using the `Lempel-Ziv-Storer-Szymanski (LZSS)` algorithm.

`LZSS` works by finding repeated chunks of data and replacing them with a shorter reference to the first time they appeared.

The referencing is done by replacing the repeated sequence with a `pointer`. This pointer consists of two numbers:

*   the first number tells us how far back to go to find the original sequence
*   the second number tells us how long the original sequence is

Here's a simplified example of how the LZSS algorithm works, the pointers are displayed like this `<1,2>`.

Play around with the input below. See how removing capital letters can result in more repeated sequences — and fewer bytes.

How much data can lowercase save? [#](https://endtimes.dev/why-lowercase-letters-save-data/#how-much-data-can-lowercase-save)
-----------------------------------------------------------------------------------------------------------------------------

Before you start lowercasing everything, remember that there are much worse offenders when it comes to online waste. _e.g. unoptimized images, auto-playing videos, unused JavaScript._ Do those first!

But that being said, lowercasing is surprisingly effective. Here's an example:

### Replacing title case with sentence case on Hacker News [#](https://endtimes.dev/why-lowercase-letters-save-data/#replacing-title-case-with-sentence-case-on-hacker-news)

As mentioned in the intro — I took the front page of Hacker News and rewrote the title of each article in `sentence case` instead of `title case`.

Each `html` file had the exact same number of characters — but when compressed into zip files the `title case` file was `5,992 bytes` and the `sentence case` file was `5,961 bytes`. Saving `31 bytes`!

Perhaps not a lot, but a nice side effect of making headings easier to read.

Using the fomula provided by [sustainablewebdesign.org](https://sustainablewebdesign.org/calculating-digital-emissions/) tells us that for each visit to Hacker News would save `0.00001059642g` of carbon if written in `sentence case`.

Assuming that Hacker News gets about `10 million` visits a day[1](https://endtimes.dev/why-lowercase-letters-save-data/#fn1) changing to sentence case would result in the prevention of `105g` of carbon daily. that's the equivalent of burning `4.3` gallons of gasoline a year.[2](https://endtimes.dev/why-lowercase-letters-save-data/#fn2) Enough fuel to drive a Mini Cooper `137.6 miles`[3](https://endtimes.dev/why-lowercase-letters-save-data/#fn3) — roughly the width of Sri Lanka.

Systematically lowercasing case‑insensitive code. [#](https://endtimes.dev/why-lowercase-letters-save-data/#systematically-lowercasing-case%E2%80%91insensitive-code)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some minifiers automatically lowercase some code to save a few bytes after compressing — but this is not common or applied consistently.

Any given optimisation from a `minifier` probably falls into the category of _too small to care about_ — but collectively they save lots of data, which makes websites faster and less energy intensive.

For instance, many `html` files start with am uppercase doctype declaration like this:

```
<!DOCTYPE html>
```

but the [`HTML5` specification states that this is case insensitive](https://html.spec.whatwg.org/multipage/syntax.html#the-doctype), so an `html minifier` could save some data by changing this to:

```
<!doctype html>
```

This optimizations has been implemented by [`html-minifier`](https://github.com/kangax/html-minifier/issues/822) but not by others.

### Some examples of lowercase‑able code [#](https://endtimes.dev/why-lowercase-letters-save-data/#some-examples-of-lowercase%E2%80%91able-code)

There are many examples of code that can be lowercased to save data. Here are some examples that are commonly uppercase when they needn't be.

*   **hex colors**
    
    ```
    * {    color:#ABCDEF}
    ```
    
    ```
    * {    color:#abcdef}
    ```
    
*   **character encodings**
    
    ```
    <meta charset="UTF-8">
    ```
    
    ```
    <meta charset="utf-8">
    ```
    
*   **JavaScript exponents**
    
    ```
    const trillion = 10E12
    ```
    
    ```
    const trillion = 10e12
    ```
    
*   **lang attributes**
    
    ```
    <html lang="EN"></html>
    ```
    
    ```
    <html lang="en"></html>
    ```
    
*   **svg path commands**
    
    ```
    <path d="M 1 1 L 1 -1 Z" />
    ```
    
    ```
    <path d="m 1 1 L 2 0 z" />
    ```
    

I've hope you found this interesting. If you're similarly inclined to help optimize the web to save energy you can help me gather more of these examples in [this git repo](https://github.com/DitheringIdiot/lowercase-able-code).

  

* * *

1.  [A comment from Hacker News moderator dang](https://news.ycombinator.com/item?id=33454140) [↩︎](https://endtimes.dev/why-lowercase-letters-save-data/#fnref1)
    
2.  [Greenhouse gas emissions from a typical passenger vehicle — EPA](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle) [↩︎](https://endtimes.dev/why-lowercase-letters-save-data/#fnref2)
    
3.  [2024 Best and Worst Fuel Economy Vehicles — fueleconomy.gov](https://fueleconomy.gov/feg/best-worst.shtml) [↩︎](https://endtimes.dev/why-lowercase-letters-save-data/#fnref3)
    

published

25 Nov 2023

modified

25 Nov 2023

author

Nathaniel

tags

`posts` `minutia` `web performance` `compression` `site speed`
