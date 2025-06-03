Title: Directive prologues and JavaScript dark matter

URL Source: https://macwright.com/2025/04/29/directive-prologues-and-javascript-dark-matter

Markdown Content:
Pragmas, magic comments and directive prologues are some of the oddest parts of TypeScript/JavaScript. They’re ways to affect the interpretation or transpilation of code: TypeScript, V8, other JavaScript engines, and other transpilers read them and use them to change their output or behavior.

JSX pragmas
-----------

For example, you could write this TypeScript code:

```
/** @jsx h */
import { h } from "preact";
const HelloWorld = () => <div>Hello</div>;
```

And TypeScript transpilers will turn it into

```
/** @jsx h */
import { h } from "preact";
const HelloWorld = () => h("div", null, "Hello");
```

That `/** @jsx h */` comment controls the transpiler, telling it to turn JSX syntax into the `h()` function. There are a few other pragmas like this - [jsxFragmentFactory](https://www.typescriptlang.org/tsconfig/#jsxFragmentFactory), [jsxImportSource](https://www.typescriptlang.org/tsconfig/#jsxImportSource), [jsxFactory](https://www.typescriptlang.org/tsconfig/#jsxFactory).

JSX pragmas aren’t well-documented. What are the rules? By experimentation, you’ll find that pragmas have to be C-style comments, they can’t use C++ syntax, so `// @jsx x` won’t work. Also, the comment needs to be at the very start of the file: if you have an import statement _before_ the comment, it has no effect.

When you parse a file with the TypeScript parser, the source file object gets a `pragmas` member that shows you which pragmas were included:

```
import * as ts from "typescript";

const s = ts.createSourceFile(
	"index.tsx",
	'/** @jsx hi */\nimport {hi} from "hi"',
	{},
);
console.log(s.pragmas);
/**
Map(1) {
  'jsx' => {
    arguments: { factory: 'hi' },
    range: { kind: 3, pos: 0, end: 14, hasTrailingNewLine: true }
  }
}
*/
```

I tried to dig up the history of this syntax, and the [3rd issue in the React issue tracker, back in 2013](https://github.com/facebook/react/issues/16), is about this comment syntax. Paul O’Shannessy responded that it was a syntax cooked up inside Facebook/Instagram. [Babel](https://babeljs.io/) supported the same syntax, and eventually TypeScript did too. I’d love to dig up more history for this!

Directive Prologues
-------------------

I’m old enough to remember when JavaScript files started with the line

```
"use strict";
```

What did this do? It convinced old browsers to use [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode), which fixed some problems in the language, like how easy it was to accidentally create global variables. I just knew this as a trick that we had to do all the time, but didn’t know the name of it, which is a [directive prologue](https://262.ecma-international.org/5.1/#sec-14.1). This is specified in the ECMA standard, which is neat:

> A Directive Prologue is the longest sequence of ExpressionStatement productions occurring as the initial SourceElement productions of a Program or FunctionBody and where each ExpressionStatement in the sequence consists entirely of a StringLiteral token followed a semicolon.

The [“use client”](https://react.dev/reference/rsc/use-client) and [“use server”](https://react.dev/reference/rsc/use-server) directives in React use the same syntax for something very different - magically changing where a code runs and which bundle it lands in.

Other directives have been proposed:

*   [“hide source”](https://github.com/tc39/proposal-function-implementation-hiding) for hiding the implementation source code of functions
*   [“use asm”](https://developer.mozilla.org/en-US/docs/Games/Tools/asm.js) for the deprecated asm.js language subset
*   [“use lazy-eval”](https://github.com/tc39/proposal-defer-import-eval/blob/main/bikeshed.md) was an option for proposal-defer-import-eval

I got the idea to write this because of this morning’s [V8 blog post](https://v8.dev/blog/explicit-compile-hints) about explicit compile hints, which proposed:

```
//# allFunctionsCalledOnLoad

function foo() { ... } // will now be eagerly parsed and compiled
function bar() { ... } // will now be eagerly parsed and compiled
```

I thought this was a new syntax at first, but then I read through and learned that this is the same general syntax as for [sourcemap magic comments](https://sourcemaps.info/spec.html):

```
//# sourceMappingURL=<url>
```

And, noting for fun that source map references used to have another syntax entirely, with [`//@` instead of `//#`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma).

Three (or more) standards
-------------------------

So, rounding up this resource, there are a bunch of ways to control how JavaScript is interpreted and transpiled, and the syntax looks like:

```
"a directive";
/** @aPragma */
//# aMagicComment
```

Directives are the only option standardized in the ECMAScript specification, but unlike the comments, they are actual code - they potentially bloat the source code size.

Neither of the comment-based syntaxes, pragmas or magic comments, have been standardized to my knowledge.

This stuff is neat: it’s kind of the dark matter around JavaScript, and it’s the kind of code that you can stick at the top of files for years, writing `"use strict"` like I did early in my career, and not even know what that thing is called.
