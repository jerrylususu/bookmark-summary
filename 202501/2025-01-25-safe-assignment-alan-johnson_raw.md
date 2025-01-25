Title: Safe Assignment | Alan Johnson

URL Source: https://nalanj.dev/posts/safe-assignment/

Markdown Content:
Alan Johnson
Articles
Safe Assignment
By Alan Johnson | September 09, 2024 | 4 minutes

There was a good bit of buzz today about the new proposal for a safe assignment operator (?=) in JavaScript. I love how JavaScript has improved over time, but this is also a problem I’ve run into in a few cases lately. I should whip up a quick example implementation as a function, right?

In case you haven’t read the proposal, here’s what it proposes:

1

	
const [error, value] ?= maybeThrows();


The new ?= operator would be equivalent to calling the right side of the assignment in a try/catch block, returning an array. The first value of the returned array would be an error if something threw inside the assignment, and the second value would be the result of the assignment if nothing threw.

A Common try/catch Annoyance

I frequently bump into code that feels pretty ugly around assignment and try/catch blocks. Things like this:

1
2
3
4
5
6
7

	
let errorMsg;

try {
  maybeThrow();
} catch (e) {
  errorMsg = "An error message";
}


To access errorMsg outside of the try/catch block using const or let you have to define it outside of the block.

A Non-Async Implementation

The easiest case here is handling non-async functions. I was able to whip up some test cases and a function called tryCatch in no time:

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19

	
function tryCatch(fn, ...args) {
  try {
    return [undefined, fn.apply(null, args)]
  } catch (e) {
    return [e, undefined];
  }
}

function throws() {
  throw new Error("It threw");
}

// returns a sum
// prints [ undefined, 2 ]
console.log(tryCatch(Math.sqrt, 4));

// returns an error
// prints [ Error: 'It threw', undefined ]
console.log(tryCatch(throws));


tryCatch calls the function with the given arguments wrapped in a try/catch block. It appropriately returns [undefined, result] if nothing throws inside the function, and [error, undefined] if something does throw.

Note that you can use an anonymous function with tryCatch as well if you don’t already have a function ready to call.

1
2
3

	
console.log(tryCatch(() => {
  throw new Error("It threw");
}));

Handling Async Functions

Async functions get a little trickier. One idea I initially had was to write a completely async version, maybe called asyncTryCatch, but where’s the challenge in that. This is a completely pointless exploration! Here’s an implementation of tryCatch that works with both async and non-async functions:

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45

	
function tryCatch(fn, ...args) {
  try {
    const result = fn.apply(null, args);
    
    if (result.then) {
      return new Promise(resolve => {
          result
            .then(v => resolve([undefined, v]))
            .catch(e => resolve([e, undefined]))  
      }); 
    }
    
    return [undefined, result];
  } catch (e) {
    return [e, undefined];
  }
}

function throws() {
  throw new Error("It threw");
}

async function asyncSum(first, second) {
  return first + second;
}

async function asyncThrows() {
  throw new Error("It throws async");
}

// returns a sum
// prints [ undefined, 2 ]
console.log(tryCatch(Math.sqrt, 4));

// returns an error
// prints [ Error: 'It threw', undefined ]
console.log(tryCatch(throws));

// returns a promise resolving to value
// prints [ undefined, 3 ]
console.log(await tryCatch(asyncSum, 1, 2));

// returns a promise resolving to error
// prints [ Error: 'It throws async', undefined ]
console.log(await tryCatch(asyncThrows));


It looks a lot like the original version, but with some Promise based code thrown in for good measure. With this implementation you can call tryCatch when calling a non-async function, and then call await tryCatch when calling an async function.

Let’s look at the Promise bit:

1
2
3
4
5
6
7

	
if (result.then) {
  return new Promise(resolve => {
      result
        .then(v => resolve([undefined, v]))
        .catch(e => resolve([e, undefined]))    
  }); 
}


if (result.then) checks if the given function (called with apply) returned a Promise. If it did, we need to return a Promise ourselves.

Calling result.then(v => resolve([undefined, v])) causes the promise to resolve to the value the given function returned, if nothing throws.

.catch(e => resolve([e, undefined])) is a little trickier. I originally wrote it as .catch(e => reject([e, undefined])), but that causes an uncaught error to fall out of tryCatch. We need to resolve here because we’re returning an array, not throwing an error.

And Finally

I pretty regularly have cases where I need to try/catch but feel like the explicit try/catch block takes up a ton of space and is annoying for scoping assignments. I’m not sure if I’ll use it or not, but this was a fun little exploration.

Love it? Hate it? Have something to say? Let me know at comments@nalanj.dev.

Previous
Desantis LLM Covered By Politico
RSS
