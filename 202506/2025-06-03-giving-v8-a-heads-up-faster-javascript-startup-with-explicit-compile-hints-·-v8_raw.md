Title: Faster JavaScript Startup with Explicit Compile Hints · V8

URL Source: https://v8.dev/blog/explicit-compile-hints

Markdown Content:
Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottlenecks. Knowing which JavaScript functions to compile during the initial script compilation can speed up web page loading.

When processing a script loaded from the network, V8 has to choose for each function: either compile it immediately ("eagerly") or defer this process. If a function that hasn't been compiled is later called, V8 must then compile it on demand.

If a JavaScript function ends up being called during page load, compiling it eagerly is beneficial, because:

*   During the initial processing of the script, we need to do at least a lightweight parse to find the function end. In JavaScript, finding the function end requires parsing the full syntax (there are no shortcuts where we could count the curly braces - the grammar is too complex). Doing the lightweight parsing first and the actual parsing afterwards is duplicate work.
*   If we decide to compile a function eagerly, the work happens on a background thread, and parts of it are interleaved with loading the script from the network. If we instead compile the function only when it's being called, it's too late to parallelize work, since the main thread cannot proceed until the function is compiled.

You can read more about how V8 parses and compiles JavaScript in [here](https://v8.dev/blog/preparser).

Many web pages would benefit from selecting the correct functions for eager compilation. For example, in our experiment with popular web pages, 17 out of 20 showed improvements, and the average foreground parse and compile times reduction was 630 ms.

We're developing a feature, [Explicit Compile Hints](https://github.com/WICG/explicit-javascript-compile-hints-file-based), which allows web developers to control which JavaScript files and functions are compiled eagerly. Chrome 136 is now shipping a version where you can select individual files for eager compilation.

This version is particularly useful if you have a "core file" which you can select for eager compilation, or if you're able to move code between source files to create such a core file.

You can trigger eager compilation for the whole file by inserting the magic comment

`//# allFunctionsCalledOnLoad`
at the top of the file.

This feature should be used sparingly though - compiling too much will consume time and memory!

See for yourself - compile hints in action [#](https://v8.dev/blog/explicit-compile-hints#see-for-yourself---compile-hints-in-action)
-------------------------------------------------------------------------------------------------------------------------------------

You can observe compile hints working by telling v8 to log the function events. For example, you can use the following files to set up a minimal test.

index.html:

`<script src="script1.js"></script><script src="script2.js"></script>`
script1.js:

`function testfunc1() {  console.log('testfunc1 called!');}testfunc1();`
script2.js:

`//# allFunctionsCalledOnLoadfunction testfunc2() {  console.log('testfunc2 called!');}testfunc2();`
Remember to run Chrome with a clean user data directory, so that code caching won't mess with your experiment. An example command line would be:

`rm -rf /tmp/chromedata && google-chrome --no-first-run --user-data-dir=/tmp/chromedata --js-flags=--log-function_events > log.txt`
After you've navigated to your test page, you can see the following function events in the log:

`$ grep testfunc log.txtfunction,preparse-no-resolution,5,18,60,0.036,179993,testfunc1function,full-parse,5,18,60,0.003,181178,testfunc1function,parse-function,5,18,60,0.014,181186,testfunc1function,interpreter,5,18,60,0.005,181205,testfunc1function,full-parse,6,48,90,0.005,184024,testfunc2function,interpreter,6,48,90,0.005,184822,testfunc2`
Since `testfunc1` was compiled lazily, we see the `parse-function` event when it's eventually called:

`function,parse-function,5,18,60,0.014,181186,testfunc1`
For `testfunc2`, we don't see a corresponding event, since the compile hint forced it to be parsed and compiled eagerly.

Future of Explicit Compile Hints [#](https://v8.dev/blog/explicit-compile-hints#future-of-explicit-compile-hints)
-----------------------------------------------------------------------------------------------------------------

In the long term, we want to move towards selecting individual functions for eager compilation. This empowers web developers to control exactly which functions they want to compile, and squeeze out the last bits of compilation performance to optimize their web pages. Stay tuned!
