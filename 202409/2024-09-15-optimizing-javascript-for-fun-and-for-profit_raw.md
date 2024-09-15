Title: Optimizing Javascript for fun and for profit

URL Source: https://romgrk.com/posts/optimizing-javascript

Markdown Content:
I often feel like javascript code in general runs much slower than it could, simply because it’s not optimized properly. Here is a summary of common optimization techniques I’ve found useful. Note that the tradeoff for performance is often readability, so the question of when to go for performance versus readability is a question left to the reader. I’ll also note that talking about optimization necessarily requires talking about benchmarking. Micro-optimizing a function for hours to have it run 100x faster is meaningless if the function only represented a fraction of the actual overall runtime to start with. If one is optimizing, the first and most important step is benchmarking. I’ll cover the topic in the later points. Be also aware that micro-benchmarks are often flawed, and that may include those presented here. I’ve done my best to avoid those traps, but don’t blindly apply any of the points presented here without benchmarking.

I have included runnable examples for all cases where it’s possible. They show by default the results I got on my machine (brave 122 on archlinux) but you can run them yourself. As much as I hate to say it, Firefox has fallen a bit behind in the optimization game, and represents a very small fraction of the traffic [for now](https://foundation.mozilla.org/en/?form=donate-header), so I don’t recommend using the results you’d get on Firefox as useful indicators.

0\. Avoid work
--------------

This might sound evident, but it needs to be here because there can’t be another first step to optimization: if you’re trying to optimize, you should first look into avoiding work. This includes concepts like memoization, laziness and incremental computation. This would be applied differently depending on the context. In React, for example, that would mean applying `memo()`, `useMemo()` and other applicable primitives.

1\. Avoid string comparisons
----------------------------

Javascript makes it easy to hide the real cost of string comparisons. If you need to compare strings in C, you’d use the `strcmp(a, b)` function. Javascript uses `===` instead, so you don’t see the `strcmp`. But it’s there, and a string comparison will usually (but not always) require comparing each of the characters in the string with the ones in the other string; string comparison is `O(n)`. One common JavaScript pattern to avoid is strings-as-enums. But with the advent of TypeScript this should be easily avoidable, as enums are integers by default.

```
// No
enum Position {
  TOP    = 'TOP',
  BOTTOM = 'BOTTOM',
}
```

```
// Yeppers
enum Position {
  TOP,    // = 0
  BOTTOM, // = 1
}
```

Here is a comparison of the costs:

```
// 1. string compare
const Position = {
  TOP: 'TOP',
  BOTTOM: 'BOTTOM',
}
 
let _ = 0
for (let i = 0; i < 1000000; i++) {
  let current = i % 2 === 0 ?
    Position.TOP : Position.BOTTOM
  if (current === Position.TOP)
    _ += 1
}
```

```
// 2. int compare
const Position = {
  TOP: 0,
  BOTTOM: 1,
}
 
let _ = 0
for (let i = 0; i < 1000000; i++) {
  let current = i % 2 === 0 ?
    Position.TOP : Position.BOTTOM
  if (current === Position.TOP)
    _ += 1
}
```

As you can see, the difference can be significant. The difference isn’t necessarily due to the `strcmp` cost as engines can sometimes use a string pool and compare by reference, but it’s also due to the fact that integers are usually passed by value in JS engines, whereas strings are always passed as pointers, and memory accesses are expensive (see section 5). In string-heavy code, this can have a huge impact.

For a real-world example, I was able to [make this JSON5 javascript parser run 2x faster](https://github.com/json5/json5/pull/278)\* just by replacing string constants with numbers.  
\*Unfortunately it wasn’t merged, but that’s how open-source is.

2\. Avoid different shapes
--------------------------

Javascript engines try to optimize code by assuming that objects have a specific shape, and that functions will receive objects of the same shape. This allows them to store the keys of the shape once for all objects of that shape, and the values in a separate flat array. To represent it in javascript:

```
const objects = [
  {
    name: 'Anthony',
    age: 36,
  },
  {
    name: 'Eckhart',
    age: 42
  },
]
```

```
const shape = [
  { name: 'name', type: 'string' },
  { name: 'age',  type: 'integer' },
]
 
const objects = [
  ['Anthony', 36],
  ['Eckhart', 42],
]
 
```

For example, at runtime if the following function receives two objects with the shape `{ x: number, y: number }`, the engine is going to speculate that future objects will have the same shape, and generate machine code optimized for that shape.

```
function add(a, b) {
  return {
    x: a.x + b.x,
    y: a.y + b.y,
  }
}
```

If one would instead pass an object not with the shape `{ x, y }` but with the shape `{ y, x }`, the engine would need to undo its speculation and the function would suddenly become considerably slower. I’m going to limit my explanation here because you should read the [excellent post from mraleph](https://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html) if you want more details, but I’m going to highlight that V8 in particular has 3 modes, for accesses that are: monomorphic (1 shape), polymorphic (2-4 shapes), and megamorphic (5+ shapes). Let’s say you _really_ want to stay monomorphic, because the slowdown is drastic:

```
// setup
let _ = 0
```

```
// 1. monomorphic
const o1 = { a: 1, b: _, c: _, d: _, e: _ }
const o2 = { a: 1, b: _, c: _, d: _, e: _ }
const o3 = { a: 1, b: _, c: _, d: _, e: _ }
const o4 = { a: 1, b: _, c: _, d: _, e: _ }
const o5 = { a: 1, b: _, c: _, d: _, e: _ } // all shapes are equal
```

```
// 2. polymorphic
const o1 = { a: 1, b: _, c: _, d: _, e: _ }
const o2 = { a: 1, b: _, c: _, d: _, e: _ }
const o3 = { a: 1, b: _, c: _, d: _, e: _ }
const o4 = { a: 1, b: _, c: _, d: _, e: _ }
const o5 = { b: _, a: 1, c: _, d: _, e: _ } // this shape is different
```

```
// 3. megamorphic
const o1 = { a: 1, b: _, c: _, d: _, e: _ }
const o2 = { b: _, a: 1, c: _, d: _, e: _ }
const o3 = { b: _, c: _, a: 1, d: _, e: _ }
const o4 = { b: _, c: _, d: _, a: 1, e: _ }
const o5 = { b: _, c: _, d: _, e: _, a: 1 } // all shapes are different
```

```
// test case
function add(a1, b1) {
  return a1.a + a1.b + a1.c + a1.d + a1.e +
         b1.a + b1.b + b1.c + b1.d + b1.e }
 
let result = 0
for (let i = 0; i < 1000000; i++) {
  result += add(o1, o2)
  result += add(o3, o4)
  result += add(o4, o5)
}
```

#### What the eff should I do about this?

Easier said than done but: **create all your objects with the exact same shape**. Even something as trivial as **writing your React component props in a different order can trigger this**.

For example, here are [simple cases](https://github.com/facebook/react/pull/28569) I found in React’s codebase, but they already had a [much higher impact case](https://v8.dev/blog/react-cliff) of the same problem a few years ago because they were initializing an object with an integer, then later storing a float. Yes, changing the type also changes the shape. Yes, there are integer and float types hidden behind `number`. Deal with it.

3\. Avoid array/object methods
------------------------------

I love functional programming as much as anyone else, but unless you’re working in Haskell/OCaml/Rust where functional code gets compiled to efficient machine code, functional will always be slower than imperative.

```
const result =
  [1.5, 3.5, 5.0]
    .map(n => Math.round(n))
    .filter(n => n % 2 === 0)
    .reduce((a, n) => a + n, 0)
```

The problem with those methods is that:

1.  They need to make a full copy of the array, and those copies later need to be freed by the garbage collector. We will explore more in details the issues of memory I/O in section 5.
2.  They loop N times for N operations, whereas a `for` loop would allow looping once.

```
// setup:
const numbers = Array.from({ length: 10_000 }).map(() => Math.random())
```

```
// 1. functional
const result =
  numbers
    .map(n => Math.round(n * 10))
    .filter(n => n % 2 === 0)
    .reduce((a, n) => a + n, 0)
```

```
// 2. imperative
let result = 0
for (let i = 0; i < numbers.length; i++) {
  let n = Math.round(numbers[i] * 10)
  if (n % 2 !== 0) continue
  result = result + n
}
```

Object methods such as `Object.values()`, `Object.keys()` and `Object.entries()` suffer from similar problems, as they also allocate more data, and memory accesses are the root of all performance issues. No really I swear, I’ll show you in section 5.

4\. Avoid indirection
---------------------

Another place to look for optimization gains is any source of indirection, of which I can see 3 main sources:

```
const point = { x: 10, y: 20 }
 
// 1.
// Proxy objects are harder to optimize because their get/set function might
// be running custom logic, so engines can't make their usual assumptions.
const proxy = new Proxy(point, { get: (t, k) => { return t[k] } })
// Some engines can make proxy costs disappear, but those optimizations are
// expensive to make and can break easily.
const x = proxy.x
 
// 2.
// Usually ignored, but accessing an object via `.` or `[]` is also an
// indirection. In easy cases, the engine may very well be able to optimize the
// cost away:
const x = point.x
// But each additional access multiplies the cost, and makes it harder for the
// engine to make assumptions about the state of `point`:
const x = this.state.circle.center.point.x
 
// 3.
// And finally, function calls can also have a cost. Engine are generally good
// at inlining these:
function getX(p) { return p.x }
const x = getX(p)
// But it's not guaranteed that they can. In particular if the function call
// isn't from a static function but comes from e.g. an argument:
function Component({ point, getX }) {
  return getX(point)
}
```

The proxy benchmark is particularly brutal on V8 at the moment. Last time I checked, proxy objects were always falling back from the JIT to the interpreter, seeing from those results it might still be the case.

```
// 1. proxy access
const point = new Proxy({ x: 10, y: 20 }, { get: (t, k) => t[k] })
 
for (let _ = 0, i = 0; i < 100_000; i++) { _ += point.x }
```

```
// 2. direct access
const point = { x: 10, y: 20 }
const x = point.x
 
for (let _ = 0, i = 0; i < 100_000; i++) { _ += x }
```

I also wanted to showcase accessing a deeply nested object vs direct access, but engines are very good at [optimizing away object accesses via escape analysis](https://youtu.be/KiWEWLwQ3oI?t=1055) when there is a hot loop and a constant object. I inserted a bit of indirection to prevent it.

```
// 1. nested access
const a = { state: { center: { point: { x: 10, y: 20 } } } }
const b = { state: { center: { point: { x: 10, y: 20 } } } }
const get = (i) => i % 2 ? a : b
 
let result = 0
for (let i = 0; i < 100_000; i++) {
  result = result + get(i).state.center.point.x }
```

```
// 2. direct access
const a = { x: 10, y: 20 }.x
const b = { x: 10, y: 20 }.x
const get = (i) => i % 2 ? a : b
 
let result = 0
for (let i = 0; i < 100_000; i++) {
  result = result + get(i) }
```

5\. Avoid cache misses
----------------------

This point requires a bit of low-level knowledge, but has implications even in javascript, so I’ll explain. From the CPU point of view, retrieving memory from RAM is slow. To speed things up, it uses mainly two optimizations.

### 5.1 Prefetching

The first one is prefetching: it fetches more memory ahead of time, in the hope that it’s the memory you’ll be interested in. It always guesses that if you request one memory address, you’ll be interested in the memory region that comes right after that. So **accessing data sequentially** is the key. In the following example, we can observe the impact of accessing memory in random order.

```
// setup:
const K = 1024
const length = 1 * K * K
 
// Theses points are created one after the other, so they are allocated
// sequentially in memory.
const points = new Array(length)
for (let i = 0; i < points.length; i++) {
  points[i] = { x: 42, y: 0 }
}
 
// This array contains the *same data* as above, but shuffled randomly.
const shuffledPoints = shuffle(points.slice())
```

```
// 1. sequential
let _ = 0
for (let i = 0; i < points.length; i++) { _ += points[i].x }
```

```
// 2. random
let _ = 0
for (let i = 0; i < shuffledPoints.length; i++) { _ += shuffledPoints[i].x }
```

#### What the eff should I do about this?

This aspect is probably the hardest to put in practice, because javascript doesn’t have a way of placing objects in memory, but you can use that knowledge to your advantage as in the example above, for example to operate on data before re-ordering or sorting it. You cannot assume that objects created sequentially will stay at the same location after some time because the garbage collector might move them around. There is one exception to that, and it’s arrays of numbers, preferably `TypedArray` instances:

```
// from this
const points = [{ x: 0, y: 5 }, { x: 0, y: 10 }]
 
// to this
const points = new Int64Array([0, 5, 0, 10])
```

For a more detailed example, [see this link](https://mrale.ph/blog/2018/02/03/maybe-you-dont-need-rust-to-speed-up-your-js.html#optimizing-parsing---reducing-gc-pressure)\* .  
\*Note that it contains some optimizations that are now outdated, but it’s still accurate overall.

### 5.2 Caching in L1/2/3

The second optimization CPUs use is the L1/L2/L3 caches: those are like faster RAMs, but they are also more expensive, so they are much smaller. They contain RAM data, but act as an LRU cache. Data comes in while it’s “hot” (being worked on), and is written back to the main RAM when new working data needs the space. So the key here is **use as little data as possible to keep your working dataset in the fast caches**. In the following example, we can observe what are the effects of busting each of the successive caches.

```
// setup:
const KB = 1024
const MB = 1024 * KB
 
// These are approximate sizes to fit in those caches. If you don't get the
// same results on your machine, it might be because your sizes differ.
const L1  = 256 * KB
const L2  =   5 * MB
const L3  =  18 * MB
const RAM =  32 * MB
 
// We'll be accessing the same buffer for all test cases, but we'll
// only be accessing the first 0 to `L1` entries in the first case,
// 0 to `L2` in the second, etc.
const buffer = new Int8Array(RAM)
buffer.fill(42)
 
const random = (max) => Math.floor(Math.random() * max)
```

```
// 1. L1
let r = 0; for (let i = 0; i < 100000; i++) { r += buffer[random(L1)] }
```

```
// 2. L2
let r = 0; for (let i = 0; i < 100000; i++) { r += buffer[random(L2)] }
```

```
// 3. L3
let r = 0; for (let i = 0; i < 100000; i++) { r += buffer[random(L3)] }
```

```
// 4. RAM
let r = 0; for (let i = 0; i < 100000; i++) { r += buffer[random(RAM)] }
```

#### What the eff should I do about this?

**Ruthlessly eliminate every single data or memory allocations** that can be eliminated. The smaller your dataset is, the faster your program will run. Memory I/O is the bottleneck for 95% of programs. Another good strategy can be to split your work into chunks, and ensure you work on a small dataset at a time.

For more details on CPU and memory, [see this link](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf).

  
  

6\. Avoid large objects
-----------------------

As explained in section 2, engines use shapes to optimize objects. However, when the shape grows too large, the engine has no choice but to use a regular hashmap (like a `Map` object). And as we saw in section 5, cache misses decrease performance significantly. Hashmaps are prone to this because their data is usually randomly & evenly distributed over the memory region they occupy. Let’s see how it behaves with this map of some users indexed by their ID.

```
// setup:
const USERS_LENGTH = 1_000
```

```
// setup:
const byId = {}
Array.from({ length: USERS_LENGTH }).forEach((_, id) => {
  byId[id] = { id, name: 'John'}
})
let _ = 0
```

```
// 1. [] access
Object.keys(byId).forEach(id => { _ += byId[id].id })
```

```
// 2. direct access
Object.values(byId).forEach(user => { _ += user.id })
```

And we can also observe how the performance keeps degrading as the object size grows:

```
// setup:
const USERS_LENGTH = 100_000
```

#### What the eff should I do about this?

As demonstrated above, avoid having to frequently index into large objects. Prefer turning the object into an array beforehand. Organizing your data to have the ID on the model can help, as you can use `Object.values()` and not have to refer to the key map to get the ID.

7\. Use eval
------------

Some javascript patterns are hard to optimize for engines, and by using `eval()` or its derivatives you can make those patterns disappear. In this example, we can observe how using `eval()` avoids the cost of creating an object with a dynamic object key:

```
// setup:
const key = 'requestId'
const values = Array.from({ length: 100_000 }).fill(42)
```

```
// 1. without eval
function createMessages(key, values) {
  const messages = []
  for (let i = 0; i < values.length; i++) {
    messages.push({ [key]: values[i] })
  }
  return messages
}
 
createMessages(key, values)
```

```
// 2. with eval
function createMessages(key, values) {
  const messages = []
  const createMessage = new Function('value',
    `return { ${JSON.stringify(key)}: value }`
  )
  for (let i = 0; i < values.length; i++) {
    messages.push(createMessage(values[i]))
  }
  return messages
}
 
createMessages(key, values)
```

Another good use-case for `eval` could be to compile a filter predicate function where you discard the branches that you know will never be taken. In general, any function that is going to be run in a very hot loop is a good candidate for this kind of optimization.

Obviously the usual warnings about `eval()` apply: don’t trust user input, sanitize anything that gets passed into the `eval()`‘d code, and don’t create any XSS possibility. Also note that some environments don’t allow access to `eval()`, such as browser pages with a CSP.

8\. Use strings, carefully
--------------------------

We’ve already seen above how strings are more expensive than they appear. Well I have kind of a good news/bad news situation here, which I’ll announce in the only logical order (bad first, good second): strings are more complex than they appear, but they can also be quite efficient used well.

String operations are a core part of JavaScript due to its context. To optimize string-heavy code, engines had to be creative. And by that I mean, they had to represent the `String` object with multiple string representation in C++, depending on the use case. There are two general cases you should worry about, because they hold true for V8 (the most common engine by far), and generally also in other engines.

First, strings concatenated with `+` don’t create a copy of the two input strings. The operation creates a pointer to each substring. If it was in typescript, it would be something like this:

```
class String {
  abstract value(): char[] {}
}
 
class BytesString {
  constructor(bytes: char[]) {
    this.bytes = bytes
  }
  value() {
    return this.bytes
  }
}
 
class ConcatenatedString {
  constructor(left: String, right: String) {
    this.left = left
    this.right = right
  }
  value() {
    return [...this.left.value(), ...this.right.value()]
  }
}
 
function concat(left, right) {
  return new ConcatenatedString(left, right)
}
 
const first = new BytesString(['H', 'e', 'l', 'l', 'o', ' '])
const second = new BytesString(['w', 'o', 'r', 'l', 'd'])
 
// See ma, no array copies!
const message = concat(first, second)
```

Second, string slices also don’t need to create copies: they can simply point to a range in another string. To continue with the example above:

```
class SlicedString {
  constructor(source: String, start: number, end: number) {
    this.source = source
    this.start = start
    this.end = end
  }
  value() {
    return this.source.value().slice(this.start, this.end)
  }
}
 
function substring(source, start, end) {
  return new SlicedString(source, start, end)
}
 
// This represents "He", but it still contains no array copies.
// It's a SlicedString to a ConcatenatedString to two BytesString
const firstTwoLetters = substring(message, 0, 2)
```

But here’s the issue: once you need to start mutating those bytes, that’s the moment you start paying copy costs. Let’s say we go back to our `String` class and try to add a `.trimEnd` method:

```
class String {
  abstract value(): char[] {}
 
  trimEnd() {
    // `.value()` here might be calling
    // our Sliced->Concatenated->2*Bytes string!
    const bytes = this.value()
 
    const result = bytes.slice()
    while (result[result.length - 1] === ' ')
      result.pop()
    return new BytesString(result)
  }
}
```

So let’s jump to an example where we compare using operations that use mutation versus only using concatenation:

```
// setup:
const classNames = ['primary', 'selected', 'active', 'medium']
```

```
// 1. mutation
const result =
  classNames
    .map(c => `button--${c}`)
    .join(' ')
```

```
// 2. concatenation
const result =
  classNames
    .map(c => 'button--' + c)
    .reduce((acc, c) => acc + ' ' + c, '')
```

#### What the eff should I do about this?

In general, try to **avoid mutation for as long as possible**. This includes methods such as `.trim()`, `.replace()`, etc. Consider how you can avoid those methods. In some engines, string templates can also be slower than `+`. In V8 at the moment it’s the case, but might not be in the future so as always, benchmark.

A note on `SlicedString` above, you should note that if a small substring to a very large string is alive in memory, it might prevent the garbage collector from collecting the large string! If you’re processing large texts and extracting small strings from it, you might be leaking large amounts of memory.

```
const large = Array.from({ length: 10_000 }).map(() => 'string').join('')
const small = large.slice(0, 50)
//    ^ will keep `large` alive
```

The solution here is to use mutation methods to our advantage. If we use one of them on `small`, it will force a copy, and the old pointer to `large` will be lost:

```
// replace a token that doesn't exist
const small = small.replace('#'.repeat(small.length + 1), '')
```

For more details, see [string.h on V8](https://github.com/v8/v8/blob/main/src/objects/string.h) or [JSString.h on JavaScriptCore](https://github.com/WebKit/WebKit/blob/main/Source/JavaScriptCore/runtime/JSString.h).

9\. Use specialization
----------------------

One important concept in performance optimization is _specialization_: adapting your logic to fit in the constraints of your particular use-case. This usually means figuring out what conditions are _likely_ to be true for your case, and coding for those conditions.

Let’s say we are a merchant that sometimes needs to add tags to their product list. We know from experience that our tags are usually empty. Knowing that information, we can specialize our function for that case:

```
// setup:
const descriptions = ['apples', 'oranges', 'bananas', 'seven']
const someTags = {
  apples: '::promotion::',
}
const noTags = {}
 
// Turn the products into a string, with their tags if applicable
function productsToString(description, tags) {
  let result = ''
  description.forEach(product => {
    result += product
    if (tags[product]) result += tags[product]
    result += ', '
  })
  return result
}
 
// Specialize it now
function productsToStringSpecialized(description, tags) {
  // We know that `tags` is likely to be empty, so we check
  // once ahead of time, and then we can remove the `if` check
  // from the inner loop
  if (isEmpty(tags)) {
    let result = ''
    description.forEach(product => {
      result += product + ', '
    })
    return result
  } else {
    let result = ''
    description.forEach(product => {
      result += product
      if (tags[product]) result += tags[product]
      result += ', '
    })
    return result
  }
}
function isEmpty(o) { for (let _ in o) { return false } return true }
 
```

```
// 1. not specialized
for (let i = 0; i < 100; i++) {
  productsToString(descriptions, someTags)
  productsToString(descriptions, noTags)
  productsToString(descriptions, noTags)
  productsToString(descriptions, noTags)
  productsToString(descriptions, noTags)
}
```

```
// 2. specialized
for (let i = 0; i < 100; i++) {
  productsToStringSpecialized(descriptions, someTags)
  productsToStringSpecialized(descriptions, noTags)
  productsToStringSpecialized(descriptions, noTags)
  productsToStringSpecialized(descriptions, noTags)
  productsToStringSpecialized(descriptions, noTags)
}
```

This sort of optimization can give you moderate improvements, but those will add up. They are a nice addition to more crucial optimizations, like shapes and memory I/O. But note that specialization can turn against you if your conditions change, so be careful when applying this one.

  

10\. Data structures
--------------------

I won’t go in details about data structures as they would require their own post. But be aware that using the incorrect data structures for your use-case can have a **bigger impact than any of the optimizations above**. I would suggest you to be familiar with the native ones like `Map` and `Set`, and to learn about linked lists, priority queues, trees (RB and B+) and tries.

But for a quick example, let’s compare how `Array.includes` does against `Set.has` for a small list:

```
// setup:
const userIds = Array.from({ length: 1_000 }).map((_, i) => i)
const adminIdsArray = userIds.slice(0, 10)
const adminIdsSet = new Set(adminIdsArray)
```

```
// 1. Array
let _ = 0
for (let i = 0; i < userIds.length; i++) {
  if (adminIdsArray.includes(userIds[i])) { _ += 1 }
}
```

```
// 2. Set
let _ = 0
for (let i = 0; i < userIds.length; i++) {
  if (adminIdsSet.has(userIds[i])) { _ += 1 }
}
```

As you can see, the data structure choice makes a very impactful difference.

As a real-world example, I had a case where we were able to [reduce the runtime of a function from 5 seconds to 22 milliseconds](https://github.com/mui/mui-x/pull/9200) by switching out an array with a linked list.

11\. Benchmarking
-----------------

I’ve left this section for the end for one reason: I needed to establish credibility with the fun sections above. Now that I (hopefully) have it, let me tell you that benchmarking is the most important part of optimization. Not only is it the most important, but it’s also _hard_. Even after 20 years of experience, I still sometimes create benchmarks that are flawed, or use the profiling tools incorrectly. So whatever you do, please **put the most effort into benchmarking correctly**.

### 11.0 Start with the top

Your priority should always be to optimize the function/section of code that makes up the biggest part of your runtime. If you spend time optimizing anything else than the top, you are wasting time.

### 11.1 Avoid micro-benchmarks

Run your code in production mode and base your optimizations on those observations. JS engines are very complex, and will often behave differently in micro-benchmarks than in real-world scenarios. For example, take this micro-benchmark:

```
const a = { type: 'div', count: 5, }
const b = { type: 'span', count: 10 }
 
function typeEquals(a, b) {
  return a.type === b.type
}
 
for (let i = 0; i < 100_000; i++) {
  typeEquals(a, b)
}
```

If you’ve payed attention sooner, you will realize that the engine will specialize the function for the shape `{ type: string, count: number }`. But does that hold true in your real-world use-case? Are `a` and `b` always of that shape, or will you receive any kind of shape? If you receive many shapes in production, this function will behave differently then.

### 11.2 Doubt your results

If you’ve just optimized a function and it now runs 100x faster, doubt it. Try to disprove your results, try it in production mode, throw stuff at it. Similarly, doubt also your tools. The mere fact of observing a benchmark with devtools can modify its behavior.

### 11.3 Pick your target

Different engines will optimize certain patterns better or worse than others. You should benchmark for the engine(s) that are relevant to you, and prioritize which one is more important. [Here’s a real-world example](https://github.com/babel/babel/pull/16357) in Babel where improving V8 means decreasing JSC’s performance.

Various remarks about profiling and devtools.

### 12.1 Browser gotchas

If you’re profiling in the browser, make sure you use a clean and empty browser profile. I even use a separate browser for this. If you’re profiling and you have browser extensions enabled, they can mess up the measurements. React devtools in particular will substantially affect results, rendering code may appear slower than it appears in the mirror to your users.

### 12.2 Sample vs structural profiling

Browser profiling tools are sample-based profilers, which take a sample of your stack at regular intervals. This had a big disadvantage: very small but very frequent functions might be called between those samples, and might be very much underreported in the stack charts you’ll get. Use Firefox devtools with a custom sample interval or Chrome devtools with CPU throttling to mitigate this issue.

### 12.3 The tools of the trade

Beyond the regular browser devtools, it may help to be aware of these options:

*   Chrome devtools have quite a few experimental flags that can help you figure out why things are slow. The style invalidation tracker is invaluable when you need to debug style/layout recalculations in the browser.  
    [https://github.com/iamakulov/devtools-perf-features](https://github.com/iamakulov/devtools-perf-features)
    
*   The deoptexplorer-vscode extension allows you to load V8/chromium log files to understand when your code is triggering deoptimizations, such as when you pass different shapes to a function. You don’t need the extension to read log files, but it makes the experience much more pleasant.  
    [https://github.com/microsoft/deoptexplorer-vscode](https://github.com/microsoft/deoptexplorer-vscode)
    
*   You can always compile the debug shell for each JS engine to understand more in details how it works. This allows you to run `perf` and other low-level tools, and also to inspect the bytecode and machine code generated by each engine.  
    [Example for V8](https://mrale.ph/blog/2018/02/03/maybe-you-dont-need-rust-to-speed-up-your-js.html#getting-the-code) | [Example for JSC](https://zon8.re/posts/jsc-internals-part1-tracing-js-source-to-bytecode/) | Example for SpiderMonkey (missing)
    

Final notes
-----------

Hope you learned some useful tricks. If you have any comments, corrections or questions, email in the footer. I’m always happy to receive feedback or questions from readers.

If you’ve made it this far, I invite you to view [The Castle](https://romgrk.com/castle).
