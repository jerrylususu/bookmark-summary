Title: Jeremy Bernier

URL Source: https://www.jbernier.com/p?id=nodejs-stream-async-iterator

Markdown Content:
Here’s an interesting Node.js exercise:

Let’s say you’re streaming something (eg. reading a file in memory), but the only API you have available to you is a series of event handler callbacks.

For example the stream API of the `csv-parse` library has an API like the following (ignore the fact that the library also has an Async Iterator API for now):

```
import { parse } from 'csv-parse';
const parser = parse({ delimiter: ',' });

parser.on('readable', () => {
  let record;
  while ((record = parser.read()) !== null) {
    console.log(record);
  }
});
parser.on('error', (err) => console.error(err.message));
parser.on('end', () => {});
```

This is a bit ugly though.

How can one turn the above code into a simple `for await` loop?

```
for await (const record of asyncIterable) {
  console.log(record);
}
```

The task is essentially to turn that first callback code into an Async Iterable, so that the Async Iterable can be iterated via a `for await` loop.

Why might we want to do this? Well beyond the `for await` loop just looking a hell of a lot cleaner, if we ever needed to programmatically iterate through multiple streams simultaneously (eg. comparing multiple files line by line), then that would be practically impossible to do via the callback option.

So how do we create an Async Iterable object from the callback code above?

We can wrap the callback code inside an **async generator function.**

Turns out this is fairly complicated (at least for my small brain). This is probably the hardest Node.js specific problem I recall working on - the equivalent of a Node.js Leetcode hard.

Try to do it yourself if you’d like. Otherwise, here’s what I ended up with.

### Solution

```
async function* createCsvParseStream(parser) {
    let results: any[] = [];
    let done = false;
    let resolve: (value?: any) => void;
    let reject: (value?: any) => void;
    let promise = new Promise((res, rej) => {
        resolve = res;
        reject = rej;
    });

    parser.on('readable', () => {
        let record;
        while ((record = parser.read()) !== null) {
            results.push(record);
            resolve();
            promise = new Promise((res, rej) => {
                resolve = res;
                reject = rej;
            });
        }
    });

    parser.on('error', (err) => {
        console.error(err.message);
        done = true;
        reject();
    });

    parser.on('end', () => {
        done = true;
        resolve();
    });

    while (!done) {
        await promise;
        yield* results;
        results = [];
    }
}
```

I’ll be honest, I found this on StackOverflow, and slightly modified it. I’d reference the answer, but don’t have the link (if someone replies with it, I’ll add the link).

Essentially you create a `Promise` (`promise = new Promise(...)`), store its `resolve` and `reject` functions, and then `await` on the promise inside a `while` loop. When an event is called (`parser.on('readable', () => {})`), you grab the data (`results.push(record)`), call `resolve()` or `reject()`, and then update your `promise` reference with a new `Promise` object, along with its updated `resolve` and `reject` functions.

The results are returned via `yield*`, which delegates to the iterable `results` array, ensuring that each `yield` call only returns a single record (eg. if `results = [a, b, c]` , then `a`, `b`, and `c` are returned separately.

The `while` loop will then await on this next promise. This continues until an `error` or `end` event is fired, which sets `done = false`, exiting the `while` loop.

Now one can iterate through that event callback code like this:

```
const asyncIterable = createCsvParseStream(inputStream);

for await (const input of asyncIterable) {
    console.log(input);
}
```

Much nicer!

_Note: I’m leaving out other code specific to the `csv-parse` library that I used in this example that would be required to get this to work, but that’s irrelevant to the point here._

All this being said, the `csv-parse` library actually has an [Async Iterator API](https://csv.js.org/parse/api/async_iterator/), so thankfully there’s no need to do all of this for this specific example.

### Conditionally iterating multiple streams simultaneously

Now if we wanted to conditionally iterate through multiple streams simultaneously (eg. comparing an older version of a sorted CSV file with a newer version to find rows that were added or deleted), we could do something like the following:

```
const iter = asyncIterable1[Symbol.asyncIterator]();
const iter2 = asyncIterable2[Symbol.asyncIterator]();

let [res1, res2] = await Promise.all([iter.next(), iter2.next()]);

while (!res1.done && !res2.done) {
  console.log("do stuff", res1, res2);
  
  if (...) {
    ...
    res1 = await iter.next();
  } else if (...) {
    ...
    res2 = await iter2.next();
  } else {
    ...
    [res1, res2] = await Promise.all([iter.next(), iter2.next()]);
  }
}
```

### What is a "for await" loop?

Taking a step back, let's define what a `for await` loop is.

Given the following Async Iterable object (`parser`):

```
import fs from "fs";
import { parse } from "csv-parse";

const parser = fs.createReadStream("test.csv").pipe(parse());
```

The following `for await` loop:

```
for await (const res of parser) {
  console.log("res", res);
}
```

is equivalent to:

```
const iter = parser[Symbol.asyncIterator]();
let res = await iter.next();

while (!res.done) {
  console.log("res", res.value);
  res = await iter.next();
}
```

I thought this was a fun exercise.
