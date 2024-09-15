Title: Notes on running Go in the browser with WebAssembly

URL Source: https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/

Markdown Content:
Recently I've had to compile Go to WebAssembly to run in the browser in a couple of small projects ([#1](https://eliben.github.io/go-sudoku/), [#2](https://eliben.github.io/go-sentencepiece/)), and in general spent some time [looking at WebAssembly](https://eli.thegreenplace.net/tag/webassembly). I find WebAssembly to be an exciting technology, both for the web and for other uses (e.g. with WASI); specifically, it's pretty great that we can take existing projects and components written in Go and run them in the browser.

In this post, I will summarize some useful patterns in running Go in the browser via WebAssembly. All the patterns are demonstrated by small, self-contained programs you can find in [this GitHub repository](https://github.com/eliben/code-for-blog/tree/main/2024/go-wasm-js-cookbook).

Basics: calling Go from JS
--------------------------

This sample serves as the basis for other samples in this post: let's write a Go function that we'll call in the browser using JS. This function uses Go's math/big stdlib package to calculate the sum of the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_/(mathematics/)) for some duration [\[1\]](https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/#footnote-1), and returns the result with high precision:

// calcHarmonic calculates the harmonic series for approximately the given
// number of seconds and returns the accumulated result in a string.
func calcHarmonic(nsecs float64) string {
  d := time.Duration(nsecs \* float64(time.Second))
  start := time.Now()
  r1 := big.NewRat(1, 1)
  for i := 2; ; i++ {
    addend := big.NewRat(1, int64(i))
    r1 \= r1.Add(r1, addend)

    if i%10 \== 0 && time.Now().Sub(start) \>\= d {
      break
    }
  }
  return r1.FloatString(40)
}

To export this function to JS in the browser, we add the following code:

func main() {
  // Export the name "calcHarmonic" to JS, with our wrapper as value
  js.Global().Set("calcHarmonic", jsCalcHarmonic)

  // The Go main function compiled to WASM is expected to block
  // indefinitely.
  select {}
}

// wrap calcHarmonic to be callable from JS
var jsCalcHarmonic \= js.FuncOf(func(this js.Value, args \[\]js.Value) any {
  if len(args) != 1 {
    panic("want one argument")
  }

  s := calcHarmonic(args\[0\].Float())
  return js.ValueOf(s)
})

This Go file is compiled to the WASM/js target with:

GOOS=js GOARCH=wasm go build -o harmonic.wasm harmonic.go

And load it from JS:

const go \= new Go();
WebAssembly.instantiateStreaming(fetch("harmonic.wasm"), go.importObject).then(
    (result) \=\> {
        go.run(result.instance);
    });

![Shows the UI of our "calculate harmonic sum" demo](https://eli.thegreenplace.net/images/2024/calc-harmonic-ui2.png)

The JS code that calls calcHarmonic is:

let buttonElement \= document.getElementById("submitButton");
document.getElementById("submitButton").addEventListener("click", () \=\> {
    let input \= document.getElementById("timeInput").value;
    let s \= calcHarmonic(parseFloat(input));
    document.getElementById("outputDiv").innerText \= s;
});

Finally, the wasm\_exec.js file from the Go distribution has to be included with something like:

<script src\="wasm\_exec.js"\></script\>

The easiest way to obtain this file is download it from the Go project's GitHub mirror (for the same Go version your Go code is compiled with); this is handled by the Makefile in our sample project:

wasm\_exec.js:
  wget https://raw.githubusercontent.com/golang/go/release-branch.go1.22/misc/wasm/wasm\_exec.js

This is the basic recipe for invoking Go from JS in the browser: the Go code is platform-agnostic and presents some API and all the glue logic is done in JS. The next samples show some variations on this basic scheme.

[Link to the full code for this sample](https://github.com/eliben/code-for-blog/tree/main/2024/go-wasm-js-cookbook/basic-call-go-from-js).

DOM manipulation from Go
------------------------

In the previous example, Go implemented the calcHarmonic function, but the rest of the program's logic was in JS - setting up an event listener for a button click, updating output, etc.

We can move more of the code to Go, if we want. The calcHarmonic remains unchanged, but our main function in Go becomes:

func main() {
  doc := js.Global().Get("document")
  buttonElement := doc.Call("getElementById", "submitButton")
  inputElement := doc.Call("getElementById", "timeInput")
  outputElement := doc.Call("getElementById", "outputDiv")

  buttonElement.Call("addEventListener", "click", js.FuncOf(
    func(this js.Value, args \[\]js.Value) any {
      input := inputElement.Get("value")
      inputFloat, err := strconv.ParseFloat(input.String(), 64)
      if err != nil {
        log.Println(err)
        return nil
      }
      s := calcHarmonic(inputFloat)
      outputElement.Set("innerText", s)
      return nil
    }))

  select {}
}

We obtain JS values from the js.Global() context and can call functions or set attributes on them. If you squint, this looks very similar to JS code, but written in Go-ish.

This code sample demonstrates some useful capabilities of DOM manipulation in Go:

*   Adding event listeners on DOM elements, with Go callbacks
*   Getting values from DOM elements
*   Setting attributes on DOM elements

The only code JS remaining in our index.html is the WebAssembly loader:

const go \= new Go();
WebAssembly.instantiateStreaming(fetch("harmonic.wasm"), go.importObject).then(
    (result) \=\> {
        go.run(result.instance);
    });

All the rest is done in Go! [Link to the full code for this sample](https://github.com/eliben/code-for-blog/tree/main/2024/go-wasm-js-cookbook/dom-in-go).

For a more full-featured sample, check out [this directory](https://github.com/eliben/code-for-blog/tree/main/2024/go-wasm-js-cookbook/go-canvas-gameoflife). It implements a simple Game of Life running in the browser, entirely in Go. All the game logic, canvas manipulation and event management is done in Go; here too, the only JS code in the project is the few lines used to load the WebAssembly module.

![Game of Life screenshot](https://eli.thegreenplace.net/images/2024/gameoflife-go-wasm.png)

I personally prefer keeping the UI logic in JS, but if you're interested in Go purity all the way - it's definitely feasible.

Using TinyGo as an alternative compiler
---------------------------------------

The Go compiler's support for WebAssembly is pretty good these days, but there's a small snag that may be important to users: the entire Go runtime is compiled into the WASM binary. On my machine, the .wasm files produced for the sample Go code weigh in at around 2.5 MiB, which will take some time to load in the browser - especially on slow connections [\[2\]](https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/#footnote-2).

There's an alternative: [TinyGo](https://tinygo.org/) is a Go toolchain "for small places", specializing in embedded controllers; the same considerations apply to WASM. The TinyGo runtime is lightweight compared to Go, and the binaries are about 1/4 the size. Not everything is perfect with TinyGo, though: compilation is much slower, and the resulting code is a bit slower as well. Finally, TinyGo has [some limitations](https://tinygo.org/docs/reference/lang-support/stdlib/) that make stdlib packages that rely on reflection not work; this can be painful when interacting with JS because encoding/json relies on reflection - so you may need to look for an alternative JSON package.

The [dom-in-go sample directory](https://github.com/eliben/code-for-blog/tree/main/2024/go-wasm-js-cookbook/dom-in-go) also shows how to build the project with TinyGo; take a look at the Makefile. Note that TinyGo has its own wasm\_exec.js support file - it won't work with the one taken from the standard Go distribution; the Makefile handles this too.

Keeping the main thread free: WebAssembly in a web worker
---------------------------------------------------------

If we come back to the original sample and run the calculation for some non-trivial amount of time (say, 2 seconds or more) - you may notice something: the page appears "frozen" while the calculation is running. You can't interact with the UI in any way, can't select text with the mouse; if you try to add periodic console.log printouts or some spinner animation - nothing will show until calcHarmonic returns with the result.

This is the expected behavior for JS when it calls a blocking, CPU-intensive function! Let's revisit the code again:

 let buttonElement \= document.getElementById("submitButton");
 document.getElementById("submitButton").addEventListener("click", () \=\> {
     let input \= document.getElementById("timeInput").value;
     let s \= calcHarmonic(parseFloat(input));     document.getElementById("outputDiv").innerText \= s;
 });

The highlighted line will block the main thread for 2+ seconds, but the main thread in JS is also used for all the UI interaction. This is one of the most common manifestations of [function coloring problem](https://eli.thegreenplace.net/2018/go-hits-the-concurrency-nail-right-on-the-head/) - blocking is problematic. Luckily, all modern browsers support _Web Workers_ - isolated threads that can execute concurrently.

It's not hard to make web workers work with WebAssembly, which is what our next demo shows. The main HTML file includes, in addition to the UI logic:

const worker \= new Worker("worker.js");
worker.onmessage \= ({ data }) \=\> {
    let { action, payload } \= data;
    switch (action) {
        case "log":
            console.log(\`worker.log: ${payload}\`);
            break;
        case "result":
            resultReady(payload);
            break;
        default:
            console.error(\`Unknown action: ${action}\`);
    }
};

Where worker.js is:

importScripts("wasm\_exec.js");
console.log("Worker is running");

// Load the WASM module with Go code.
const go \= new Go();
WebAssembly.instantiateStreaming(fetch("harmonic.wasm"), go.importObject).then(
    (result) \=\> {
        go.run(result.instance);
        console.log("Worker loaded WASM module");
    }).catch((err) \=\> {
        console.error("Worker failed to load WASM module: ", err)
    });

onmessage \= ({ data }) \=\> {
    let { action, payload } \= data;
    postMessage({
        action: "log",
        payload: \`Worker received message ${action}: ${payload}\`,
    });
    switch (action) {
        case "calculate":
            let result \= calcHarmonic(payload);
            postMessage({ action: "result", payload: result });
            break;
        default:
            throw (\`unknown action '${action}'\`);
    }
};

(The Go code remains unchanged.)

We see that the worker does the WebAssembly loading now, meaning that the Go code executes in a separate thread and the UI thread is free to run while the computation is ongoing. This sample adds a spinner that animates until the web worker returns calcHarmonic's answer, to show the effect.

![Shows the UI of our "calculate harmonic sum" demo with a spinner](https://eli.thegreenplace.net/images/2024/calc-harmonic-spinner.png)

[Link to the full code for this sample](https://github.com/eliben/code-for-blog/tree/main/2024/go-wasm-js-cookbook/go-in-web-worker).

* * *

[\[1\]](https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/#footnote-reference-1)

The harmonic series is known to diverge, but _very slowly_. You need over 200 million elements to get to the sum of 20, etc. (see [A004080](https://oeis.org/A004080)).

[\[2\]](https://eli.thegreenplace.net/2024/notes-on-running-go-in-the-browser-with-webassembly/#footnote-reference-2)

There are some additional mitigations we can explore, like compressing the WASM binary. This is outside the scope of this post, and it applies to the TinyGo output as well.
