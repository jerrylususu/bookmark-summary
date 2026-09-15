# Your Recursion Is Lying to You
- URL: https://blog.gaborkoos.com/posts/2026-05-09-Your-Recursion-Is-Lying-to-You/
- Added At: 2026-09-15 15:12:52
- Tags: #read #js

## TL;DR
递归没问题，错在假设 JS 运行时支持尾调用优化。尾递归不等于栈安全，深度可能增长时应改用迭代、显式栈或 trampoline，别在生产中依赖 TCO。

## Summary
这篇文章的核心观点是：递归本身没问题，有问题的是你对 JavaScript 运行时栈行为的假设。递归写法看起来优雅，逻辑也可能完全正确，但每次调用都会占用调用栈；深度一大，就会栈溢出。

它先从一个最简单的递归求和开始：

```js
function sum(n) {
  if (n === 0) return 0;
  return n + sum(n - 1);
}

sum(10); // 55
```

小输入没问题，但 `sum(100000)` 在大多数 JS 运行时里会抛出 `RangeError` 或 `InternalError: too much recursion`。原因不是结果算错了，而是每个 `sum` 调用都要等下一层返回，栈帧一直累积，最后超过运行时能承受的物理上限。

很多人接下来会想到尾递归优化。尾调用的关键是：递归调用必须是函数最后执行的事情，返回值被立即转发，后面没有任何待处理计算。上面这个 `sum` 看起来最后一行是 `sum(n - 1)`，但返回后还要做 `n + ...`，所以它不是尾递归。真正的尾递归版本会把待处理状态放进累加器：

```js
function sumTR(n, acc = 0) {
  if (n === 0) return acc;
  return sumTR(n - 1, acc + n);
}
```

这里 `sumTR(...)` 是最后发生的事，没有待处理的 `+`。理论上，如果运行时实现 TCO，也就是尾调用优化，就可以复用同一个栈帧，在常量栈空间里执行。但问题是：大多数 JavaScript 运行时并不稳定支持这个优化。

```js
sumTR(100000); // 仍然可能抛 RangeError
```

ECMAScript 2015 曾在严格模式里正式规定 proper tail calls，但主流引擎大多没有一致采用。有的实现过，后来又因为性能回退撤掉；有的根本没实现。所以你不能在生产 JavaScript 里假设尾递归一定栈安全。代码结构是尾递归，不等于运行时一定复用栈帧。

文章还特别讲了 Fibonacci。朴素递归版本有两个问题，而且很容易被混淆：

```js
function fib(n) {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
}
```

第一，它会栈溢出。第二，它是指数时间复杂度，大约按 `O(2ⁿ)` 增长，更精确地说接近 `Θ(φⁿ)`。`fib(30)` 已经超过一百万次调用，`fib(50)` 是百亿级别。在浏览器里，它往往还没到栈上限，页面就已经卡死了。表层现象都是“卡住或崩溃”，但根因一个是栈溢出，一个是指数爆炸，修复方式完全不同。

尾递归版 Fibonacci 可以变成线性时间：

```js
function fibTR(n, a = 0, b = 1) {
  if (n === 0) return a;
  if (n === 1) return b;
  return fibTR(n - 1, b, a + b);
}
```

但它仍然会因为 TCO 不可靠而面临大 `n` 的栈溢出风险。

文章列出的运行时现实是：Chrome、Node.js、Deno 使用的 V8 不依赖 proper tail calls；Firefox 的 SpiderMonkey 也不能把尾递归当成安全保证；Safari 的 JavaScriptCore 历史上对 TCO 的支持不稳定，曾实现又撤回；Bun 基于 JavaScriptCore，行为取决于具体版本。结论是：尾递归是代码结构属性，栈复用是运行时实现属性。生产代码通常要跨多个运行环境，正确性不能依赖某个优化器的具体行为。

所以生产环境更推荐迭代写法：

```js
function sumIter(n) {
  let acc = 0;
  for (let i = n; i > 0; i--) acc += i;
  return acc;
}

sumIter(1000000); // 不会递归增长栈
```

如果你还想保留递归的可读性，可以用 trampoline。它的思路是用一个循环反复调用函数，直到返回的是最终结果，而不是另一个待调用函数：

```js
function trampoline(fn) {
  let result = fn;
  while (typeof result === 'function') {
    result = result();
  }
  return result;
}

function sumTrampoline(n, acc = 0) {
  if (n === 0) return acc;
  return () => sumTrampoline(n - 1, acc + n);
}

trampoline(() => sumTrampoline(100000)); // 不会栈溢出
```

trampoline 的代价是更多函数分配和调度开销，所以它适合“保留递归结构比极致性能更重要”的场景。它不依赖运行时 TCO，因此可移植性和栈安全性更可控。

实用规则是：深度小、你自己能控制时，可以用递归；一旦深度由用户输入、数据规模或不确定环境决定，就改用迭代控制流。热路径可以两种都测，但不能把正确性建立在“假设有 TCO”上。

文章最后的清单可以概括为：不要在生产关键路径假设 TCO；用真实上限测试，不要只用玩具输入；深度可能增长时优先迭代；把递归当可读性工具，而不是栈安全保证。

结论是：递归不是敌人，未经验证的运行时假设才是。尾递归的“形状”不会自动让 JavaScript 栈安全。递归适合深度有界且能提升清晰度的场景；深度可能增长时，应该用迭代、显式栈或 trampoline，让栈行为变得明确且可移植。这个主题和“Debounce 在骗你”“Throttle 在骗你”“包管理器在骗你”“JS Date 在骗你”“JSON 在骗你”“模块在骗你”一样，讲的都是：熟悉的抽象背后，藏着容易被忽略的运行边界。
