Title: Font with Built-In Syntax Highlighting

URL Source: https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/

Markdown Content:
Note:

I received a lot of great feedback from the discussions at [Mastodon](https://typo.social/@gdc/112959308500800771) and [Hacker News](https://news.ycombinator.com/item?id=41245159), so I've updated the post with some improvements to the font! I've also added some further examples and acknowledgements at the end.

Syntax Highlighting in Hand-Coded Websites
------------------------------------------

### The problem

I have been trying to identify practical reasons why hand-coding websites with HTML and CSS is so hard (_by hand-coding, I mean not relying on frameworks, generators or 3rd party scripts that modify the DOM_).

Let's say, I want to make a blog. What are the **actual** things that prevent me from making—and maintaining—it by hand? What would it take to clear these roadblocks?

There are many, of course, but for a hand-coded programming oriented blog one of these roadblocks is **syntax highlighting**.

When I display snippets of code, I want to make the code easy to read and understand by highlighting it with colors. To do that, I would normally need to use a complex syntax highlighter library, like [Prism](https://prismjs.com/) or [highlight.js](https://highlightjs.org/). These scripts work by scanning and chopping up the code into small language-specific patterns, then wrapping each part in tags with special styling that creates the highlighted effect, and then injecting the resulting HTML back into the page.

But, I want to write code by hand. I don't want any external scripts to inject things I didn't write myself. Syntax highlighters also add to the overall complexity and bloat of each page, which I'm trying to avoid. I want to keep things as simple as possible.

### Leveraging OpenType features to build a simple syntax highlighter inside the font

This lead me to think: **could it be possible to build syntax highlighting directly into a font**, skipping JavaScript altogether? Could I somehow leverage OpenType features, by creating colored glyphs with the COLR table, and identifying and substituting code syntax with contextual alternates?

```
<div class="spoilers">
  <strong>Yes, it's possible!</strong>
  <small>...to some extent =)</small>
</div>
```

The colors in the HTML snippet above **comes from within the font itself**, the code is **plain text**, and requires **no JavaScript**.

To achieve that, I modified an open source font Monaspace Krypton to include colored versions of each character, and then used OpenType contextual alternates to essentially find & replace specific strings of text based on HTML, CSS and JS syntax. The result is a simple syntax highlighter, **built-in** to the font itself.

If you want to try it yourself, download the font: [FontWithASyntaxHighlighter-Regular.woff2](https://blog.glyphdrawing.club/assets/fonts/FontWithASyntaxHighlighter-Regular.woff2)

And include the following bits of CSS:

```
@font-face {
  font-family: 'FontWithASyntaxHighlighter';
  src: 
    url('/FontWithASyntaxHighlighter-Regular.woff2') 
    format('woff2')
  ;
}
code {
  font-family: "FontWithASyntaxHighlighter", monospace;
}
```

And that's it!

What are the Pros and Cons of this method?
------------------------------------------

This method opens up some interesting possibilities...

### Pros

1.  Install is as easy as using any custom font.
2.  Works without JavaScript.
3.  Works without CSS themes.
4.  ...but can be themed with CSS.
5.  It's fast.
6.  Snippets of code can be put into `<pre>` and `<code>`, with no extra classes or `<span>`s.
7.  Clean HTML source code.
8.  Works everywhere that supports OpenType features, like InDesign.
9.  Doesn't require maintenance or updating.
10.  Works in `<textarea>` and `<input>`! Syntax highlighting inside `<textarea>` has been [previously impossible](https://css-tricks.com/creating-an-editable-textarea-that-supports-syntax-highlighted-code/), because textareas and inputs can only contain plain text. This is where the interesting possibilities lie. As a demo, I made this tiny HTML, CSS & JS sandbox, with native undo and redo, in a single, [~200 line web component](https://blog.glyphdrawing.club/assets/webcomponents/tinybox.js).

### Cons

There are, of course, some limitations to this method. It is not a direct replacement to the more robust syntax highligting libraries, but works well enough for simple needs.

1.  Making modifications to the syntax highligher, like adding more language supports or changing the look of the font, requires modifying the font file. This is inaccessible for most people. I used Glyphs to modify this font, but it only works on Mac, and costs ~300 euros.
2.  It only works where OpenType is supported. Fortunately, that's all major browsers and most modern programs. However, something like PowerPoint doesn't support OpenType.
3.  Finding patterns in text with OpenType contextual alternates is quite basic, and is no match for scripts that use regular expressions. For example, words within `<p>` tags that are JS keywords will be always highlighted: `<p>if I throw this Object through the window, catch it, for else it’ll continue to Infinity & break</p>`. Comment blocks can't have new lines etc.

How does it actually work?
--------------------------

Here's roughly how it works. There are two features in OpenType that make this possible: OpenType COLR table and contextual alternates.

### OpenType COLR table

OpenType COLR table makes multi-colored fonts possible. [There is a good guide on creating a color font using Glyphs](https://glyphsapp.com/learn/creating-a-microsoft-color-font).

I made a palette with 8 colors.

I duplicated letters `A` `–` `Z`, numbers `0` `–` `9` and the characters `.` `#` `*` `-` and `_` four times. Each duplicated character is then suffixed with .alt, .alt2, .alt3 or .alt4, and then assigned a color from the palette. For example, all .alt1 glyphs are `this` lime-yellow.

I also duplicated all characters twice, and gave them suffices .alt1 and .alt5 and assigned them colors used in `<!-- comment blocks -->` and `"strings within quotes"`

![Image 1](https://blog.glyphdrawing.club/assets/kmFZTjkTcx-320.jpeg)

View from Glyps app. Each alternate character has a different color.

The two other colors I used for symbols `& | $ + − = ~ [] () {} / ; : " @ %` and `'`, and they are always in one color. Numbers `0 1 2 3 4 5 6 7 8 9` are also always a certain color, unless overriden by other rules.

### OpenType contextual alternates

The second required feature is OpenType contextual alternates. [Here's a great introductory guide to advanced contextual alternates for Glyphs](https://glyphsapp.com/learn/features-part-3-advanced-contextual-alternates).

Contextual alternates makes characters "aware" of their adjacent characters. An example would be fonts that emulate continuous hand writing, where _how_ a letter connects depends on which letter it connects to. There is a [nice article covering possible uses here](https://ilovetypography.com/2011/04/01/engaging-contextuality/).

#### JavaScript syntax rules

The core feature of contextual alternates is substituting glyphs. Here is a simplified code for finding the JavaScript keyword `if` and substituting the letters i and f with their colored variant:

```
sub i' f by i.alt2;
sub i.alt2 f' by f.alt2;
```

In English:

1.  When i is followed by f, substitute the default i with an alternate (i.alt2).
2.  When i.alt2 is followed by f, substitute the default f with an alternate (f.alt2).
3.  As a result, every "if" in text gets substituted with `if`.

OpenType doesn't support many-to-many substitutions directly, but [@behdad](https://typo.social/@behdad/112967180363218632) on Mastodon had a great suggestion: keywords could be elegantly colored by _chaining_ contextual substitutions.

To do this, I made a lookup which substitutes each letter with its colored variant.

```
lookup ALT_SUBS {
    sub a by a.alt; 
    sub b by b.alt; 
    sub c by c.alt; 
    [etc.]
    sub Y by Y.alt;
    sub Z by Z.alt;
} ALT_SUBS;
```

I moved this lookup rule to the [Prefix](https://handbook.glyphsapp.com/layout/standalone-lookups/) section, which just means it doesn't get applied automatically unlike the other lookups.

Then, I made a lookup rule for each keyword in the contextual alternates section. Here's one for `console`:

```
lookup console {
    ignore sub @AllLetters c' o' n' s' o' l' e';
    ignore sub c' o' n' s' o' l' e' @AllLetters;
    sub c' lookup ALT_SUBS
        o' lookup ALT_SUBS
        n' lookup ALT_SUBS
        s' lookup ALT_SUBS
        o' lookup ALT_SUBS
        l' lookup ALT_SUBS
        e' lookup ALT_SUBS;
} console;
```

First two lines tells it to ignore strings like `Xconsole` or `consoles`, but not if there's a period like `console.log()`.

The third line starts by replacing the first letter 'c' with its colored variant `c`, by using definitions from the other lookup table "ALT\_SUBS". This repeats until each letter is replaced by its color variant, and the result is `console`.

Identifying JavaScript keywords is fairly straightforward. Logic is the same for each keyword, and I used a python script to generate them.

#### HTML & CSS syntax rules

But for HTML and CSS... I had to get a bit more creative. There are simply too many keywords for both HTML and CSS combined. Making a separate rule for each keyword would inflate the file size.

Instead, I came up with this monstrosity. Here's how I find CSS value functions:

```
lookup CssParamCalt useExtension {
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' @CssParam parenleft by @CssParamAlt4;
  sub @CssParam' parenleft by @CssParamAlt4;
} CssParamCalt;
```

@CssParam is a custom OpenType glyph class I've set up. It includes the characters `A` `–` `Z`, `a` `–` `z`, and `-`, which are all the possible characters used in CSS value function names. Because the longest possible CSS value function name is `repeating-linear-gradient()`, with 25 letters, the first line of the lookup starts with @CssParam repeated 25 times, followed by parenleft (`(`). This lookup will match any word up to 25 letters long, if it's immediately followed by an opening parenthesis. When a match occurs, it substitutes the matched text with its alternate color form (@CssParamAlt4).

This lookup works for both CSS and JavaScript. It will colorize standard CSS functions like `rgb()` as well as custom JavaScript functions like `myFunction()`. The result is a semi-flexible syntax highlighter that doesn't require complex parsing. I've repeated the same principle for finding HTML tags and attributes, and for CSS selectors and parameters.

#### Unknown length rules

Comment blocks and strings between quotes also required extra care, because their length can be anything. OpenType doesn't support loops or anything resembling regular expressions. For example, I can't just tell it to simply substitute everything it finds between two quotes.

However, I got a great suggestion from @penteract on [_Hacker News_](https://news.ycombinator.com/item?id=41259124) to use a finite state machine for these kinds of situations. Here our aim is to colorize eveything between /\* and \*/ gray:

```
lookup CSScomment useExtension {
  // stop if we encounter a colored */
  ignore sub asterisk.alt1 slash.alt1 @All';

  // color first letter after /*
  sub slash asterisk @All' by @AllAlt1;
  sub slash asterisk space @All' by @AllAlt1;
  
  // color /* itself
  sub slash' asterisk by slash.alt1;
  sub slash.alt1 asterisk' by asterisk.alt1;
  
  // finite state machine to color rest of the characters
  // or until ignore condition is met
  sub @AllAlt1 @All' by @AllAlt1;
} CSScomment;
```

The last line is the important one. The lookup will just continue replacing characters if the previous character is already colored.

### End note

The full process is a little bit too convoluted to go into step-by-step, but if you're a type designer who wants to do this with their own font, don't hesitate to contact me. I'm also not an OpenType expert, so I'm sure the substitution logics could be improved upon. I'm open to sharing the modified source file to anyone interested. If you have any ideas, suggestions or feedback, let me know. You can reach me at `hlotvonen@gmail.com` or leave a comment on [Mastodon](https://typo.social/@gdc/112959308500800771).

Changing the color theme
------------------------

You can even change the color theme with CSS [`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-palette-values/override-colors)! Browser support is great.

Potential future
----------------

Many people suggested that this concept could be taken one step further with [harfbuzz-wasm](https://github.com/harfbuzz/harfbuzz-wasm-examples). With harfbuzz-wasm a real parser could be used instead of my crazy opentype lookup rules. Essentially, all the cons could be eliminated... Any harfbuzz-wasm experts who wants to take this on?

Licence
-------

The original font ([MonaSpace](https://monaspace.githubnext.com/)) has [SIL open font license v1.1](https://github.com/githubnext/monaspace/blob/main/LICENSE), which carries over to my modified version. So, you're free to use the font in any way that the SIL v1.1 license permits.

As for the code examples, they are MIT licensed. The tiny sandbox web component can be found here: [https://github.com/hlotvonen/tinybox](https://github.com/hlotvonen/tinybox)

More examples
-------------

```
as, in, of, if, for, while, finally, var, new, function,
do, return, void, else, break, catch, instanceof, with,
throw, case, default, try, switch, continue, typeof, delete,
let, yield, const, class, get, set, debugger, async, await,
static, import, from, export, extends

true, false, null, undefined, NaN, Infinity

Object, Function, Boolean, Symbol, Math, Date, Number, BigInt, 
String, RegExp, Array, Float32Array, Float64Array, Int8Array, 
Uint8Array, Uint8ClampedArray, Int16Array, Int32Array, Uint16Array, 
Uint32Array, BigInt64Array, BigUint64Array, Set, Map, WeakSet,
WeakMap, ArrayBuffer, SharedArrayBuffer, Atomics, DataView, 
JSON, Promise, Generator, GeneratorFunction, AsyncFunction, 
Reflect, Proxy, Intl, WebAssembly, Error, EvalError, InternalError, 
RangeError, ReferenceError, SyntaxError, TypeError, URIError, 
setInterval, setTimeout, clearInterval, clearTimeout, require, 
exports, eval, isFinite, isNaN, parseFloat, parseInt, decodeURI, 
decodeURIComponent, encodeURI, encodeURIComponent, escape, 
unescape, arguments, this, super, console, window, document, 
localStorage, sessionStorage, module, global
```

* * *

```
<!-- this is a comment! -->
/* and this */
// and this
<!-- however...
it breaks when your code goes to a newline.
there's no way to keep context line to line...
-->
```

* * *

```
<!-- can't disable highlighting JS keywords in between tags -->
<p>
  give me a break...
</p>
```

* * *

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Syntax Highlighter Example</title>
  <style>
    body {
      background-color: rgb(255, 0, 0);
      font-family: 'Arial Narrow', sans-serif;
      line-height: 1.44;
      color: #333;
    }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to the Syntax Highlighter Test</h1>
  </header>
  <nav>
    <ul>
      <li><a href="#section1">Section 1</a>
    </ul>
  </nav>
  <main>
    <section id="section1">
      <h2>Section 1</h2>
      <p>This is a <span class="highlight">highlighted</span> paragraph.</p>
      <img src="/api/placeholder/300/200" alt="Placeholder image">
    </section>
  </main>
  <script>
    console.log("This is a JavaScript comment");
    function greet(name) {
      return `Hello, ${name}!`;
    }
    document.addEventListener('DOMContentLoaded', () => {
      console.log(greet('Syntax Highlighter'));
    });
  </script>
</body>
</html>
```

* * *

```
.crazyBackground {
  /* don't try this at home */
  background:
    radial-gradient(
      100% 50% at 50% 50%,
      hsl(90 90% 45%) 0% 5%,
      hsl(250 70% 40%) 50%,
      hsl(50 50% 50%)
    ),
    radial-gradient(
      100% 100% at 50% 25%,
      hsl(90 40% 85%) 30%,
      hsl(40 80% 20%) 60% 90%,
      transparent
    ),
    linear-gradient(
      90deg,
      hsl(150 90% 90%) 0 10%,
      hsl(10 10% 20%),
      hsl(150 90% 90%) 90% 100%
    )
  ;
  background-size:
    5% 10%,
    10% 200%,
    25% 100%
  ;
  background-blend-mode:
    color-dodge,
    difference,
    normal
  ;
  animation: fire2 60s linear infinite;
}

@keyframes fire2 {
  from {
    background-position: 0% 0%, 0 30%, 0 0;
  }

  to {
    background-position: 0% -100%, -100% 30%, 200% 0%;
  }
}
```

* * *

```
// Variables and constants
let variable = 'Hello';
const CONSTANT = 42;

// Template literals
const name = 'World';
console.log(`${variable}, ${name}!`);

// Function declaration
function greet(name) {
  return `Hello, ${name}!`;
}

// Arrow function
const multiply = (a, b) => a * b;

// Class definition
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  sayHello() {
    console.log(`Hello, my name is ${this.name}`);
  }
}

// Object literal
const config = {
  apiKey: 'abc123',
  maxRetries: 3,
  timeout: 5000
};

// Array methods
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
const sum = numbers.reduce((acc, curr) => acc + curr, 0);

// Async/await
async function fetchData(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Destructuring
const { apiKey, maxRetries } = config;
const [first, second, ...rest] = numbers;

// Spread operator
const newArray = [...numbers, 6, 7, 8];

// Conditional (ternary) operator
const isAdult = age >= 18 ? 'Adult' : 'Minor';

// Switch statement
function getDayName(dayNumber) {
  switch (dayNumber) {
    case 0: return 'Sunday';
    case 1: return 'Monday';
    // ... other cases
    default: return 'Invalid day';
  }
}

// Regular expression
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Symbol
const uniqueKey = Symbol('description');

// Set and Map
const uniqueNumbers = new Set(numbers);
const userRoles = new Map([['admin', 'full'], ['user', 'limited']]);

// Promises
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Done!'), 1000);
});

// Export statement
export { greet, Person };
```

Acknowledgements
----------------

Thanks to jfk13 on hn, and [@pixelambacht](https://typo.social/@kizu@front-end.social/112960336521542558) on Mastodon for pointing out that 'calt' is turned on by default, and that 'colr' is not an opentype feature that needs to be "turned on".

Thanks to [penteract](https://news.ycombinator.com/item?id=41259124) on hn and [@behdad](https://typo.social/@behdad/112967180363218632) on Mastodon for suggesting better substitution rules.

Thanks to [@kizu](https://typo.social/@kizu@front-end.social/112960336521542558) and [@pixelambacht](https://typo.social/@kizu@front-end.social/112960336521542558) on Mastodon for suggesting color theming with `override-colors` CSS rule.

As said earlier, if you have any ideas, suggestions or feedback, let me know. You can reach me at `hlotvonen@gmail.com` or leave a comment on [Mastodon](https://typo.social/@gdc/112959308500800771).

Thanks to all who sent emails, messages and commented!
