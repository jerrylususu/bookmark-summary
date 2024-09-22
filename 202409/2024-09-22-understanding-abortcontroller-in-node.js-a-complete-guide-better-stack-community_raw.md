Title: Understanding AbortController in Node.js: A Complete Guide | Better Stack Community

URL Source: https://betterstack.com/community/guides/scaling-nodejs/understanding-abortcontroller/

Markdown Content:
In Node.js, canceling asynchronous operations like network requests and file system reads has always been tricky. The absence of a standardized interruption mechanism led to a host of issues, including race conditions where cancellation logic and operation completion could unpredictably interact. In addition, memory leaks from uncollected resources tied to uncanceled operations, complex error handling scenarios, and inefficient use of system and network resources further complicated matters..

To solve these issues, Node.js introduced the [AbortController](https://nodejs.org/api/globals.html#class-abortcontroller). This handy tool lets you signal cancellation to Promise-based APIs, like fetch, making it easier to cancel ongoing operations and improve your application's responsiveness.

This article will guide you through using the `AbortController` to simplify the cancellation of asynchronous operations.

Prerequisites
-------------

To follow this tutorial, ensure you have:

*   The latest version of [Node.js installed](https://nodejs.org/en/download/package-manager).
*   Basic knowledge of asynchronous programming with Promises.

What is the AbortController API?
--------------------------------

The AbortController is an API that enables you to cancel asynchronous operations before completion. This functionality is crucial for preventing tasks from running indefinitely, which can degrade application performance and expose it to resource exhaustion attacks like [Event Handler Poisoning](https://davisjam.medium.com/a-sense-of-time-for-javascript-and-node-js-68c9114f5d48) or [Denial of Service (DoS)](https://en.wikipedia.org/wiki/Denial-of-service_attack).

Common use cases include:

*   Terminating network requests that exceed reasonable time limits.
*   Halting long-running database queries.
*   Stopping resource-intensive computations.

The AbortController API creates an AbortSignal object, which can be passed to asynchronous operations like `fetch` or custom functions. When the `abort()` method is called on the AbortController, any asynchronous operation associated with its signal is terminated.

The AbortController API was initially introduced for browsers to allow cancellation of fetch requests. It was later implemented in Node.js. It was first introduced as an experimental feature in Node.js 14.17.0 and became stable with Node.js v15.4.0, expanding its utility across different JavaScript environments.

How does AbortController work in Node.js?
-----------------------------------------

In this section, we'll explore how AbortController works in Node.js. To highlight its significance, let's first look at a common issue in asynchronous programming: a long-running operation that can't be interrupted once started.

Here’s an example demonstrating this problem:

slow-operation.js

Copied!

```
import timersPromises from "node:timers/promises";

async function slowOperation() {
  // Resolve in 10 seconds
  return timersPromises.setTimeout(10000);
}

async function doSomethingAsync() {
  try {
    await slowOperation();
    console.log("Completed slow operation");
  } catch (err) {
    console.error("Failed to complete slow operation due to error:", err);
  }
}

doSomethingAsync();
```

The `slowOperation` function simulates a task taking 10 seconds to complete using Node.js's Promise-based timer. The main execution wraps this operation in a try-catch block, awaiting its completion and logging the result.

To run the code, enter the following command:

After ten seconds, the output will be:

Once initiated, this operation will always run for its full duration, regardless of whether the result is still needed. This lack of a cancellation mechanism can lead to wasted resources, decreased application responsiveness, and potential issues during shutdown or error scenarios.

To address the issue of uninterruptible long-running operations, you can implement `AbortController` as follows:

slow-operation.js

Copied!

```
import timersPromises from "node:timers/promises";

async function slowOperation({ signal }) {
  return timersPromises.setTimeout(10000, null, { signal });
}

async function doSomethingAsync() {
  const controller = new AbortController();
  const signal = controller.signal;

  setTimeout(() => controller.abort(), 5000); // Abort after 5 seconds

  try {
    await slowOperation({ signal });
    console.log("Completed slow operation");
  } catch (err) {
    if (err.name === "AbortError") {
      console.error("Operation aborted");
    } else {
      console.error("Failed to complete slow operation due to error:", err);
    }
  }
}
doSomethingAsync();
```

The `slowOperation()` function is modified to accept a `signal` parameter, which is then passed to the `setTimeout()` function, enabling the timer to be aborted.

In the `doSomethingAsync` function, an AbortController is created, and its associated signal is set up. A separate timer is configured to call `controller.abort()` after 5 seconds, which will trigger the abortion of the slow operation.

The `signal` is then passed to the `slowOperation()` function, establishing a connection to the AbortController. The `catch` block is enhanced with a specific check for `AbortError`, allowing distinct handling of aborted operations versus other types of errors.

Upon saving the changes and running the file again, you will see an output similar to this:

With these changes, the asynchronous task can be aborted before its natural completion time, providing better control over long-running operations and improving resource management.

Now that you understand how the AbortController works, you can use it to cancel network requests in the next section.

Cancelling Network Requests
---------------------------

Applications often make network requests to APIs to fetch data, typically using built-in tools like `fetch`. Implementing timeout mechanisms is essential to prevent requests from hanging indefinitely. Although `fetch` has a default timeout of 300 seconds, the AbortController API offers a flexible way to cancel requests with shorter timeouts.

Here's an example of using AbortController with `fetch`:

```
const url = "https://jsonplaceholder.typicode.com/todos/1";

const controller = new AbortController();
const signal = controller.signal;

const fetchTodo = async () => {
  try {
    console.log("Fetching data...");
    const response = await fetch(url, { signal });
    const todo = await response.json();
    console.log("Todo:", todo);
  } catch (error) {
    if (error.name === "AbortError") {
      console.log("Operation aborted");
    } else {
      console.error("Error:", error);
    }
  }
};


 // Set a timeout to abort the fetch after 5 seconds
setTimeout(() => controller.abort(), 5000);

fetchTodo();
```

In this example, an AbortController instance is created, and its signal is extracted to enable abort functionality.

The `fetchTodo()` function uses the abort signal with a `fetch` request. When you pass the signal to `fetch` as an option, the request is linked to the AbortController, allowing for external cancellation. Error handling within the `fetchTodo()` function checks for `AbortError`, which is thrown when the request is aborted.

To simulate a timeout scenario, `setTimeout` is used to call `controller.abort()` after 5 seconds. When `abort()` is called, it triggers an `AbortError` in the `fetch` operation, which is then caught and handled in the catch block.

Save the code in a file named `fetch-data.js` and execute it with the following command:

The output will look similar to this if the request takes longer than 5 seconds:

```
Fetching data...
Aborting fetch...
Operation aborted
```

However, if the request completes in less than 5 seconds, the output will be:

```
Fetching data...
Todo: { userId: 1, id: 1, title: 'delectus aut autem', completed: false }
Aborting fetch...
```

While this method works, the AbortController API also provides an `AbortSignal.timeout()` method, which can further simplify and improve this example.

Using AbortSignal.timeout()
---------------------------

In previous sections, you created an AbortController instance and manually managed its signal and timeout. However, Node.js now offers `AbortSignal.timeout()`, which allows you to set a timeout for your network requests directly, reducing boilerplate code.

Here's how you can use `AbortSignal.timeout()` in practice:

fetch-data-with-timeout.js

Copied!

```
const url = "https://jsonplaceholder.typicode.com/todos/1";

const fetchTodo = async () => {
  const timeoutMS = 5;

  try {
    console.log("Fetching data...");
    const response = await fetch(url, {
[higlight]
      signal: AbortSignal.timeout(timeoutMS),
    });
    const todo = await response.json();
    console.log("Todo:", todo);
  } catch (error) {
    if (error.name === "TimeoutError") {
      console.log(`Operation timed out after ${timeoutMS} milliseconds`);
    } else {
      console.error("Error:", error);
    }
  }
};

fetchTodo();
```

In this example, the timeout duration is set to 5 milliseconds using the variable `timeoutMS` to demonstrate the timeout in action. In a real-world scenario, you would have a much longer timeout.

The `AbortSignal.timeout()` method sets the fetch request's timeout. The error handling section explicitly checks for a `TimeoutError` and provides clear feedback when the operation runs out.

To save and run the program, save the code in a file named `fetch-data-with-timeout.js` and execute it with the following command:

```
node fetch-data-with-timeout.js
```

You will see the following output:

```
Fetching data...
Operation timed out after 5 milliseconds
```

To simplify even further, you can use `fetch` with a helper function like this:

```
async function fetchWithTimeout(url, options = {}) {
  const { timeoutMS = 3000 } = options;

  return await fetch(url, {
    ...options,
    signal: AbortSignal.timeout(timeoutMS),
  });
}
```

Now that you can easily set timeouts for fetch requests, you can combine multiple signals for more complex scenarios.

Combining Multiple Signals with AbortSignal.any()
-------------------------------------------------

Sometimes, you might have multiple reasons for aborting an asynchronous operation. For example, you might want to abort a network request due to a timeout or a user action. In such scenarios, `AbortSignal.any()` is invaluable. It allows you to combine multiple signals into a single signal that triggers if any provided signals are aborted.

Take the following example:

use-multiple-signals.js

Copied!

```
import readline from "readline";

const url = "https://jsonplaceholder.typicode.com/todos/1";

const timeoutMS = 5000;
const timeoutSignal = AbortSignal.timeout(timeoutMS);
const userAbortController = new AbortController();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const fetchTodo = async () => {
  const combinedSignal = AbortSignal.any([
    timeoutSignal,
    userAbortController.signal,
  ]);
  try {
    console.log("Fetching data...");
    const response = await fetch(url, { signal: combinedSignal });
    const todo = await response.json();
    console.log("Todo:", todo);
  } catch (error) {
    if (timeoutSignal.aborted) {
      console.log(`Operation timed out after ${timeoutMS} ms`);
    } else if (userAbortController.signal.aborted) {
      console.log("Operation aborted by user");
    } else {
      console.error("Error:", error);
    }
  } finally {
    userAbortController.abort(); // Clean up
    rl.close();
  }
};

// Listen for user input to abort the operation
rl.question("Press Enter to abort the fetch operation:\n", () => {
  console.log("User initiated abort");
  userAbortController.abort();
});

fetchTodo();
```

This code demonstrates how to use `AbortSignal.any()` to combine multiple abort signals, allowing a network request to be cancelled either due to a timeout or user action. It sets a timeout of 5000 milliseconds and creates an `AbortController` for user-initiated aborts, combining these signals with `AbortSignal.any()`.

The combined signal is then passed to a fetch request. If the fetch is aborted due to the timeout, it logs a timeout message; if aborted by the user, it logs that the user aborted the operation. Additionally, the code prompts the user to press Enter to abort the fetch operation manually. It listens to this user's input and handles the abort accordingly.

To save and run the program:

```
node use-multiple-signals.js
```

When it runs, if you immediately press `Enter`, you will see that it will be aborted because of your action:

```
Press Enter to abort the fetch operation:
Fetching data...

User initiated abort
Operation aborted by user
```

You can also modify the timeout to a short duration, like five milliseconds, to see the timeout in action:

use-multiple-signals.js

Copied!

After saving the changes, running the program will cause it to time out quickly:

```
Press Enter to abort the fetch operation:
Fetching data...
Operation timed out after 5 ms
```

As you can see, the program can now abort due to user input or timeout, which is incredibly useful.

Handling AbortErrors
--------------------

Handling errors when using the AbortController is essential to maintaining your application's stability and reliability. This section briefly summarises error handling to ensure your application effectively manages these errors.

When working with AbortController, you will encounter two main types of errors:

*   `TimeoutError`: This error occurs when an operation exceeds the specified time limit and is aborted due to a timeout.
*   `AbortError`: This error is raised when an asynchronous operation has been aborted using an AbortController.

To handle these errors, you can use a `try-catch` block as demonstrated below:

```
const fetchDataMethod = async () => {;

  try {
    const response = await fetch(url, {
      signal: AbortSignal.timeout(3000),
    });
    ...
  } catch (error) {
    if (error.name === "TimeoutError") {
      console.log(`your error message here`);
    } else {
      console.error("Error:", error);
    }
  }
}
```

When you are not using the timeout signal, you will often encounter AbortErrors. The handling process is similar, but you will check for the `AbortError` name instead:

```
const fetchDataMethod = async () => {
  try {
    const response = await fetch(url, { signal });
    ...
  } catch (error) {
    if (error.name === "AbortError") {
      console.log("your error messsage here");
    } else {
      console.error("Error:", error);
    }
  }
};
```

With these approaches, you should now be able to handle errors confidently when using AbortController in your applications.

Cancelling streams with AbortController
---------------------------------------

Streams are essential in Node.js, allowing your programs to consume large files in smaller chunks without using too much memory. Often, once a stream operation starts, it is difficult to stop it, but with AbortController, you can cancel streams anytime.

The stream methods `stream.Writable()` and `stream.Readable()` accept abort signals, and you can also use them with methods like `fs.createReadStream` as demonstrated below:

```
import fs from "fs";
import { addAbortSignal } from "stream";
import { setTimeout as delay } from "timers/promises";

const controller = new AbortController();
setTimeout(() => controller.abort(), 50);

const inputStream = addAbortSignal(
  controller.signal,
  fs.createReadStream("text.txt")
);
const outputStream = fs.createWriteStream("output.txt");

async function process(chunk) {
  console.log(`Processing chunk: ${chunk.length} bytes`);
  // Simulating some async processing
  await delay(10);
  return chunk;
}

(async () => {
  try {
    for await (const chunk of inputStream) {
      const processedChunk = await process(chunk);
      if (!outputStream.write(processedChunk)) {
        // Handle backpressure
        await new Promise((resolve) => outputStream.once("drain", resolve));
      }
    }
    console.log("Stream processing completed");
  } catch (e) {
    if (e.name === "AbortError") {
      console.log("The operation was cancelled");
    } else {
      console.error("An error occurred:", e);
      throw e;
    }
  } finally {
    outputStream.end();
    await new Promise((resolve) => outputStream.once("finish", resolve));
    console.log("Output stream closed");
  }
})();
```

This code demonstrates stream processing with an abort mechanism in Node.js, focusing on reading from one file and writing to another while handling potential timeouts. It creates a readable stream from `text.txt` and a writable stream to `output.txt`, setting up an AbortController that triggers after 50 milliseconds (for demonstration purposes). The main operation asynchronously reads chunks from the input stream, processes them with a simulated delay, and writes them to the output stream. If the abort signal is triggered during this process, it catches the `AbortError` and logs a cancellation message.

To test this, create a `text.txt` file containing "This is a message" repeated three hundred thousand times with the following command:

```
yes "This is a message" | head -n 300000 > text.txt
```

Once the file has been created, you can run the script:

It will show output similar to this:

```
Processing chunk: 65536 bytes
Processing chunk: 65536 bytes
Processing chunk: 65536 bytes
Processing chunk: 65536 bytes
The operation was cancelled
Output stream closed
```

This output shows that the stream can be successfully cancelled.

With this, you can now cancel streams using AbortController in Node.js.

Exploring support for AbortSignal in Node.js core methods
---------------------------------------------------------

When Node.js introduced the AbortController API, many built-in methods were enhanced to accept an AbortSignal. You have seen how to use this with fetch and streams. This section covers some of the APIs that can be passed a signal. This is a partial list but is meant to get you started.

In the `child_process` module, you can pass an AbortSignal to the following methods:

*   `child_process.exec`
*   `child_process.execFile`
*   `child_process.fork`
*   `child_process.spawn`

Here is an example inspired by the documentation on how to use AbortSignal with `child_process.spawn`:

```
const controller = new AbortController();
const { signal } = controller;
const grep = spawn("grep", ["ssh"], { signal });
grep.on("error", (err) => {
  // This will be called with err being an AbortError if the controller aborts
});
controller.abort(); // stops the process
```

The `fs` module, commonly used for interacting with the file system, also supports AbortSignal. You can pass an abort signal to the following methods:

*   `fs.readFile`
*   `fs.watch`
*   `fs.writeFile`

The `readline` module can also accept an AbortSignal. You can pass an abort signal to the following methods:

*   `readline.Interface`
*   `readline.createInterface`

Final thoughts
--------------

This guide explored various techniques for using AbortController in Node.js, from cancelling network requests to managing streams. We covered how to implement abort signals to ensure that your applications can handle long-running operations gracefully and remain responsive under different conditions.

This approach will help ensure your applications provide a great user experience and remain reliable even when facing unexpected issues such as slow API services.

Thank you for reading, and happy coding!

![Image 1: Author's avatar](https://betterstack.com/assets/articles/authors/stanley-ulili-ec1fef45db6e6daed8f73b16cbf0a4ec23f30b386559cf3d2f650efde7f0f60b.png)

Stanley is a freelance web developer and researcher from Malawi. He loves learning new things and writing about them to understand and solidify concepts. He hopes that by sharing his experience, others can learn something from them too!

Got an article suggestion? [Let us know](mailto:hello@betterstack.com?subject=Suggestion%20for%20Understanding%20AbortController%20in%20Node.js%3A%20A%20Complete%20Guide&body=)

Next article

[Node.js Streams vs. Web Streams API →](https://betterstack.com/community/guides/scaling-nodejs/nodejs-streams-vs-web-streams-api/)

[![Image 2: Licensed under CC-BY-NC-SA](https://betterstack.com/assets/articles/cc-by-nc-sa-1fa5a2f7978211f24b8230a7e79097dd1f8a36be35e813693c49348cf1689f42.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
