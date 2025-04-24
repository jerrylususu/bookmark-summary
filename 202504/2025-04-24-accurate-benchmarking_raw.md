Title: Accurate Benchmarking

URL Source: https://ates.dev/posts/2025-01-12-accurate-benchmarking/

Markdown Content:
I'll share a mathematical approach to discounting the loop overhead when looping over a piece of code in order to measure how long it takes (as compared to some alternative piece of code).

This might be a well-known approach, and there might be better methods, but it is nevertheless a method I independently came up with and have used in the past.

### [The premise](https://ates.dev/posts/2025-01-12-accurate-benchmarking/#the-premise)

We have a piece of code, `method1()`, that we want to benchmark to see how fast it is as compared to `method2()`.

Since computers are very fast, running something just once isn't a viable way to measure how long it takes to run. We therefore run it many times in a loop and measure the total amount of time it takes.

### [A standard, qualitative approach](https://ates.dev/posts/2025-01-12-accurate-benchmarking/#a-standard-qualitative-approach)

A straightforward way to set up a `benchmark()` utility could look something like this:

```
function benchmarkTotal(fn, iterations) {
  const start = performance.now();

  for (let i = 0; i < iterations; i++) {
    fn();
  }

  const end = performance.now();
  const total = end - start;

  return total;
}

// Usage:
const elapsed1 = benchmarkTotal(method1, 1_000_000);
const elapsed2 = benchmarkTotal(method2, 1_000_000);
```

This approach is sufficient for qualitatively comparing `method1` and `method2` to see which one is faster.

*   `method1` is faster than `method2` if `elapsed1` < `elapsed2`
*   `method1` is slower than `method2` if `elapsed1` \> `elapsed2`

### [Factor in the loop overhead for quantitative comparisons](https://ates.dev/posts/2025-01-12-accurate-benchmarking/#factor-in-the-loop-overhead-for-quantitative-comparisons)

To get a quantitative "X is p% faster than Y", we should factor in the loop overhead. If `method1` and `method2` are both "slow" methods that take many computational cycles to run, the tiny overhead of the `for` loop will be insignificant. The faster the methods we're comparing, the more significant the loop overhead becomes.

Let’s denote the total time for `method1` to run n times as t1, and the total loop overhead for n iterations as e. And `method2` takes t2.

Then:

elapsed1 \= t1 + e elapsed2 \= t2 + eThe only mathematically accurate quantitative result we can derive from the above is:

delta \= elapsed1 \- elapsed2 \= ( t 1 + e ) \- ( t 2 + e ) \= t 1 + e \- t 2 \- e \= t 1 \- t 2We can say that the difference between `method1` and `method2` running n times is delta milliseconds.

We can also calculate a percentage, `p = delta / elapsed1 * 100`, and say:

*   `method2` is `p`% faster than `method1` if `p` is negative
*   `method2` is `p`% slower than `method1` if `p` is positive

We can also say the difference between the run time of a single call is `delta / n`, but what if we want to measure a single call to either function? We haven't isolated t1 or t2 yet. We just know their difference.

### [Timing a single call](https://ates.dev/posts/2025-01-12-accurate-benchmarking/#timing-a-single-call)

Here’s the key insight of this post.

If we want to loop n times, we can still loop a total of n times by looping a bit, and then a bit more. We can partition the loop by first calling the method **once** n3 times, followed by calling it **twice** n3 times, ensuring the total number of calls equals n:

```
function benchmarkSingle(fn, iterations) {
  const oneThird = iterations / 3;

  const start1 = performance.now();

  for (let i = 0; i < oneThird; i++) {
    fn();
  }

  const end1 = performance.now();
  const elapsed1 = end1 - start1;

  const start2 = performance.now();

  for (let i = 0; i < oneThird; i++) {
    fn();
    fn();
  }

  const end2 = performance.now();
  const elapsed2 = end2 - start2;

  const partition = elapsed2 - elapsed1;
  const single = partition / oneThird;

  return single;
}

// Usage:
const elapsed = benchmarkSingle(method, 1_000_000);
```

Let's break it down:

If the time it takes for n3 calls to `method` is tp and the loop overhead of n3 iterations is ep, then the two loops have the following durations:

elapsed1 \= tp + ep elapsed2 \= 2tp + epThen their difference is:

delta \= elapsed 2 \- elapsed 1 \= ( 2 tp + ep ) \- ( tp + ep ) \= 2 tp + ep \- tp \- ep \= tpWe have gotten rid of the loop overhead and isolated tp! Then we can accurately compute the time it takes for a single call to the method by dividing tp by n3:

single \= 3 tp n

### [Sanity check](https://ates.dev/posts/2025-01-12-accurate-benchmarking/#sanity-check)

Let's use both `benchmarkTotal` and `benchmarkSingle` 100 times over 10 million iterations of `Math.atan2()` with random numbers and compare the results:

```
// The subject
const fn = () => Math.atan2(Math.random(), Math.random());
const iterations = 10_000_000;

function average(measurer, samples = 100) {
  let total = 0;

  for (let i = 0; i < samples; i++) {
    total += measurer();
  }

  return total / samples;
}

const totalWithOverhead = average(() => benchmarkTotal(fn, iterations));
const single = average(() => benchmarkSingle(fn, iterations));
const total = single * iterations;
```

After waiting for the computations to finish:

| technique | variable | value |
| --- | --- | --- |
| simple | `totalWithOverhead` | `130.08399999946357` |
| improved | `total` | `127.3620000086725` |

Conclusion:

It takes `Math.atan2()` ~127ms to run 10 million times over random numbers. With the simple approach of running a single loop for the measurement, there is a ~3ms loop overhead, or 2% of the measurement from the simple technique.

Does a 2% loop overhead matter in most cases? Probably not. `¯\_(ツ)_/¯`
