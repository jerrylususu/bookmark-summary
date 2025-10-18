Title: The Temporal Dead Zone, or why the TypeScript codebase is littered with var statements

URL Source: https://vincentrolfs.dev/blog/ts-var

Markdown Content:
October 1, 2025

If you have been working with JavaScript for a while, you probably know there are a couple of different ways to initialize a variable. Nowadays we usually use

`const password = "hunter2"`
and only occasionally, if you need some mutable state:

`let password = "hunter2"`
These declarations have been around for a while and they have reasonable block scoping rules:

```
function example(measurement) {
  console.log(calculation); // ReferenceError
  console.log(anotherCalc); // ReferenceError

  if (measurement > 1) {
    const calculation = measurement + 1;
    let anotherCalc = measurement * 2;
    // ...
  } else {
    // ...
  }

  console.log(calculation); // ReferenceError
  console.log(anotherCalc); // ReferenceError
}
```

But if you have been working with JS for a **really** long while, you might remember the time when neither of these declarations were possible. All we had was `var`. And `var` stinks. Not only is every variable mutable, with no way to enforce immutability, but to make matters worse, `var` leaks beyond block scope:

```
function example(measurement) {
  console.log(calculation); // undefined - accessible! calculation leaked out
  console.log(i); // undefined - accessible! i leaked out

  if (measurement > 1) {
    var calculation = measurement + 1;
    // ...
  } else {
    // ...
  }

  console.log(calculation); // 1 - accessible! calculation leaked out

  for (var i = 0; i < 3; i++) {
    // ...
  }

  console.log(i); // 3 - accessible! i leaked out
}
```

Terrible!

So it was a big surprise to me to find out that the TypeScript codebase (which is itself written in TypeScript — [for now](https://devblogs.microsoft.com/typescript/typescript-native-port/)) is [littered with var statements like it's 2003](https://github.com/microsoft/TypeScript/blob/968d5deb8b5fd4af3ce85433872bdefc1eb17f10/src/compiler/scanner.ts#L1033):

```
/** @internal */
export function createSourceMapGenerator(
  host: EmitHost,
  file: string,
  sourceRoot: string,
  sourcesDirectoryPath: string,
  generatorOptions: SourceMapGeneratorOptions
): SourceMapGenerator {
  /* eslint-disable no-var */
  var { enter, exit } = generatorOptions.extendedDiagnostics
    ? performance.createTimer("Source Map", "beforeSourcemap", "afterSourcemap")
    : performance.nullTimer;

  // Current source map file and its index in the sources list
  var rawSources: string[] = [];
  var sources: string[] = [];
  var sourceToSourceIndexMap = new Map<string, number>();
  var sourcesContent: (string | null)[] | undefined; // eslint-disable-line no-restricted-syntax

  var names: string[] = [];
  var nameToNameIndexMap: Map<string, number> | undefined;
  var mappingCharCodes: number[] = [];
  var mappings = "";

  // Last recorded and encoded mappings
  var lastGeneratedLine = 0;
  var lastGeneratedCharacter = 0;
  var lastSourceIndex = 0;
  var lastSourceLine = 0;
  var lastSourceCharacter = 0;
  var lastNameIndex = 0;
  var hasLast = false;

  // ... etc
}
```

The reason has to do with what is called the [Temporal Dead Zone (TDZ)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz). For each variable in your code, there is a zone where the variable is declared but not initialized. The following example makes this clear:

```
function example() {
  const result = Math.random() < 0.5 ? useX() : 1; // 50% probability of a ReferenceError
  const x = 10;

  return result;

  function useX() {
    return x;
  }
}
```

In the above example, it is totally valid to declare `useX` at the bottom of the function. The trouble comes when you call it before `x` has been initialized - in other words, when the interpreter is still in the TDZ of `x`. The interpreter refuses to let you access `x` and throws an error.

And that is great! Because if you would use `var` instead of `const` in this example, there would be no error and the function would simply return undefined!

```
function example() {
  var result = useX(); // undefined
  var x = 10;

  return result; // undefined

  function useX() {
    return x;
  }
}

console.log(example()); // undefined
```

Terrible!

So the TDZ is actually a super useful feature brought on by `const` and `let`. So why doesn't TypeScript want to use it? It's because _Performance_.

Figuring out whether it is in a variable's TDZ is a lot of work for the interpreter. As you can see above, it cannot be done statically, but depends on nondeterministic runtime behavior. That brings a penalty which was significant for the TypeScript codebase. After migrating a decent amount of their statements to `var`, [they saw an 8% performance improvement across some benchmarks](https://github.com/microsoft/TypeScript/issues/52924).

I for one am very happy that I don't have to use `var` anymore. And for TypeScript, I'm sure it's just another reason to [migrate their codebase to Go](https://devblogs.microsoft.com/typescript/typescript-native-port/).

Discuss this article on [Reddit](https://www.reddit.com/r/typescript/comments/1nw0cmg/the_temporal_dead_zone_or_why_the_typescript/).

Feel free to email me at [mail@vincentrolfs.dev](mailto:mail@vincentrolfs.dev). Or you can follow me on Mastodon at [@vincentrolfs@hachyderm.io](https://hachyderm.io/@vincentrolfs).