Title: crawshaw - 2025-01-06

URL Source: https://crawshaw.io/blog/programming-with-llms

Markdown Content:
How I program with LLMs
-----------------------

_2025-01-06_

This document is a summary of my personal experiences using generative models while programming over the past year. It has not been a passive process. I have intentionally sought ways to use LLMs while programming to learn about them. The result has been that I now regularly use LLMs while working and I consider their benefits net-positive on my productivity. (My attempts to go back to programming without them are unpleasant.)

Along the way I have found oft-repeated steps that can be automated, and a few of us are working on building those into a tool specifically for Go programming: [sketch.dev](https://sketch.dev/). It’s very early but so far the experience has been positive.

Background
----------

I am typically curious about new technology. It took very little experimentation with LLMs for me to want to see if I could extract practical value. There is an allure to a technology that can (at least some of the time) craft sophisticated responses to challenging questions. It is even more exciting to watch a computer attempt to write a piece of a program as requested, and make solid progress.

The only technological shift I have experienced that feels similar to me happened in 1995, when we first configured our LAN with a usable default route. We replaced the shared computer in the other room running Trumpet Winsock with a machine that could route a dialup connection, and all at once I had The Internet on tap. Having the internet all the time was astonishing, and felt like the future. Probably far more to me in that moment than to many who had been on the internet longer at universities, because I was immediately dropped into high internet technology: web browsers, JPEGs, and millions of people. Access to a powerful LLM feels like that.

So I followed this curiosity, to see if a tool that can generate something mostly not wrong most of the time could be a net benefit in my daily work. The answer appears to be yes, generative models are useful for me when I program. It has not been easy to get to this point. My underlying fascination with the new technology is the only way I have managed to figure it out, so I am sympathetic when other engineers claim LLMs are “useless.” But as I have been asked more than once how I can possibly use them effectively, this post is my attempt to describe what I have found so far.

Overview
--------

There are three ways I use LLMs in my day-to-day programming:

1.  **Autocomplete**. This makes me more productive by doing a lot of the more-obvious typing for me. It turns out the current state of the art can be improved on here, but that’s a conversation for another day. Even the standard products you can get off the shelf are better for me than nothing. I convinced myself of that by trying to give them up. I could not go a week without getting frustrated by how much mundane typing I had to do before having a FIM model. This is the place to experiment first.  
    
2.  **Search**. If I have a question about a complex environment, say “how do I make a button transparent in CSS” I will get a far better answer asking any consumer-based LLM, o1, sonnet 3.5, etc, than I do using an old fashioned web search engine and trying to parse the details out of whatever page I land on. (Sometimes the LLM is wrong. So are people. The other day I put my shoe on my head and asked my two year old what she thought of my hat. She dealt with it and gave me a proper scolding. I can deal with LLMs being wrong sometimes too.)  
    
3.  **Chat-driven programming**. This is the hardest of the three. This is where I get the most value of LLMs, but also the one that bothers me the most. It involves learning a lot and adjusting how you program, and on principle I don’t like that. It requires at least as much messing about to get value out of LLM chat as it does to learn to use a slide rule, with the added annoyance that it is a non-deterministic service that is regularly changing its behavior and user interface. Indeed, the long-term goal in my work is to replace the need for chat-driven programming, to bring the power of these models to a developer in a way that is not so off-putting. But as of now I am dedicated to approaching the problem incrementally, which means figuring out how to do best with what we have and improve it.

As this is about the _practice_ of programming, this has been a fundamentally qualitative process that is hard to write about with quantitative rigor. The closest I will get to data is to say: it appears from my records that for every two hours of programming I do now, I accept more than 10 autocomplete suggestions, use LLM for a search-like task once, and program in a chat session once.

The rest of this is about extracting value from chat-driven programming.

Why use chat at all?
--------------------

Let me try to motivate this for the skeptical. A lot of the value I personally get out of chat-driven programming is I reach a point in the day when I know what needs to be written, I can describe it, but I don’t have the energy to create a new file, start typing, then start looking up the libraries I need. (I’m an early-morning person, so this is usually any time after 11am for me, though it can also be any time I context-switch into a different language/framework/etc.) LLMs perform that service for me in programming. They give me a first draft, with some good ideas, with several of the dependencies I need, and often some mistakes. Often, _I find fixing those mistakes is a lot easier than starting from scratch_.

This means chat-based programming may not be for you. I am doing a particular kind of programming, product development, which could be roughly described as trying to bring programs to a user through a robust interface. That means I am building a lot, throwing away a lot, and bouncing around between environments. Some days I mostly write typescript, some days mostly Go. I spent a week in a C++ codebase last month exploring an idea, and just had an opportunity to learn the HTTP server-side events format. I am all over the place, constantly forgetting and relearning. If you spend more time proving your optimization of a cryptographic algorithm is not vulnerable to timing attacks than you do writing the code, I don’t think any of my observations here are going to be useful to you.

Chat-based LLMs do best with exam-style questions
-------------------------------------------------

Give an LLM a specific objective and all the background material it needs so it can craft a well-contained code review packet and expect it to adjust as you question it. There are two major elements to this:

1.  Avoid creating a situation with so much complexity and ambiguity that the LLM gets confused and produces bad results. This is why I have had little success with chat inside my IDE. My workspace is often messy, the repository I am working on is by default too large, it is filled with distractions. One thing humans appear to be much better than LLMs at (as of January 2025) is not getting distracted. That is why I still use an LLM via a web browser, because I want a blank slate on which to craft a well-contained request.  
    
2.  Ask for work that is easy to verify. Your job as a programmer using an LLM is to read the code it produces, think about it, and decide if the work is good. You can ask an LLM to do things you would never ask a human to do. “Rewrite all of your new tests introducing an <intermediate concept designed to make the tests easier to read\>” is an appalling thing to ask a human, you’re going to have days of tense back-and-forth about whether the cost of the work is worth the benefit. An LLM will do it in 60 seconds and not make you fight to get it done. Take advantage of the fact that **redoing work is extremely cheap**.

The ideal task for an LLM is one where it needs to use a lot of common libraries (more than a human can remember, so it is doing a lot of small-scale research for you), working to an interface you designed or produces a small interface you can verify as sensible quickly, and it can write readable tests. Sometimes this means choosing the library for it, if you want something obscure (though with open source code LLMs are quite good at this).

You always need to pass an LLM’s code through a compiler and run the tests before spending time reading it. They all produce code that doesn’t compile sometimes. (Always making errors I find surprisingly human, every time I see one I think, there but for the grace of God go I.) The better LLMs are very good at recovering from their mistakes, often all they need is for you to paste the compiler error or test failure into the chat and they fix the code.

Extra code structure is much cheaper
------------------------------------

There are vague tradeoffs we make every day around the cost of writing, the cost of reading, and the cost of refactoring code. Let’s take Go package boundaries as an example. The standard library has a package “net/http” that contains some fundamental types for dealing with wire format encoding, MIME types, etc. It contains an HTTP client, and an HTTP server. Should it be one package, or several? Reasonable people can disagree! So much so, I do not know if there is a correct answer today. What we have works, after 15 years of use it is still not clear to me that some other package arrangement would work better.

Advantages of a larger package include: centralized documentation for callers, easier initial writing, easier refactoring, easier sharing of helper code without devising robust interfaces for them (which often involves pulling the fundamental types of a package out into yet another leaf package filled with types). The disadvantages include the package being harder to read because many different things are going on (try reading the net/http client implementation without tripping up and finding yourself in the server code for a few minutes), or it being harder to use because there is too much going on in it. For example I have a codebase that uses a C library in some fundamental types, but parts of the codebase need to be in a binary widely distributed to many platforms that does not technically need the C library, so have more packages than you might expect in the codebase isolating the use of the C library to avoid cgo in the multi-platform binary.

There are no right answers here, instead we are trading off different types of work that an engineer will have to do (upfront and ongoing). LLMs influence those tradeoffs:

*   As LLMs do better with exam-style questions, more and smaller packages make it easier to give a complete and yet isolated context for a piece of work. This is true for humans too, which is why we use packages at all, but we trade off package size against the extra typing/plumbing/filing to make more readable code. With an LLM both doing and benefiting from a big chunk of that extra work, the tradeoff shifts. (As a bonus, we humans get more readable code!)  
    
*   Smaller and more numerous packages can be compiled and tested independently of unrelated code. This is helpful for the LLM dev cycle as it means changes can be compiled and tested before other dependent packages are refactored, and the package has a simpler test environment.

An example
----------

Let me work an example to combine a few of the discussed ideas:

Write a reservoir sampler for the quartiles of floats.

First off, package structure. Were I doing this before LLMs, I would have chosen to have some sort of streamstat package that contained several algorithms, maybe one per file. This does not seem to be a unique opinion, here is an open source [quantile](https://pkg.go.dev/github.com/alexander-yu/stream@v0.2.0/quantile) package following that model. Now, I want just this one algorithm in its own package. Other variants or related algorithms can have their own package.

Next up, what do we get from an LLM. The first pass is not bad. That prompt, with some details about wanting it in Go got me quartile\_sampler.go:

```
// QuartileSampler maintains a reservoir sample to estimate quartiles of a stream  
// of float64 values. It uses reservoir sampling to maintain a representative  
// sample when processing large streams of data.  
type QuartileSampler struct {  
   reservoir []float64  
   seen      int  
   maxSize   int  
   rng       *rand.Rand  
}

// NewQuartileSampler creates a new sampler that maintains up to maxSize samples.  
// A larger maxSize provides more accurate estimates but uses more memory.  
func NewQuartileSampler(maxSize int) *QuartileSampler { … }
```

The core interface is good too:

```
// Add adds a new value to the sampler.  
func (qs *QuartileSampler) Add(value float64) { … }

// Quartiles returns the estimated 25th, 50th (median), and 75th percentiles  
// of the data seen so far. Returns (0,0,0) if no data has been added.  
func (qs *QuartileSampler) Quartiles() (q1, median, q3 float64) {  
   if len(qs.reservoir) == 0 {  
       return 0, 0, 0  
   }  
    
   // Make a copy to avoid modifying the reservoir  
   sorted := make([]float64, len(qs.reservoir))  
   copy(sorted, qs.reservoir)  
   slices.Sort(sorted)  
    
   n := len(sorted)  
   q1 = percentile(sorted, 0.25)  
   median = percentile(sorted, 0.50)  
   q3 = percentile(sorted, 0.75)  
    
   return q1, median, q3  
}
```

Great! There are also tests.

An aside: this may be the place to stop. Sometimes I use LLM codegen as a form of specialized search. E.g. I’m curious about reservoir sampling, but want to see how the algorithm would be applied under some surprising constraint, for example time-windowed sampling. Instead of doing a literature search I might amend my prompt for an implementation that tracks freshness. (I could also ask it to include references to the literature in the comments, which I could manually check to see if it’s making things up or if there’s some solid research to work from.) Often I spend 60 seconds reading some generated code, see an obvious trick I hadn’t thought of, then throw it away and start over. Now I know the trick is possible. This is why it is so hard to attribute value generated by LLMs. Yes sometimes it makes bad code, gets stuck in a rut, makes up something impossible (it hallucinated a part of the monaco API I wish existed the other day) and wastes my time. It can also save me hours by pointing out something relevant I don’t know.

Back to the code. Fascinatingly, the initial code produced didn’t compile. In the middle of the Quartiles implementation there was the line:

```
n := len(sorted)
```

Which is a fine line, sorted is a slice defined a few lines earlier. But the value is never used so gopls (and the Go compiler if you run go build) immediately says:

```
declared and not used: n
```

This is a very easy fix. If I paste the error back into the LLM it will correct it. Though in this case, as I’m reading the code, it’s quite clear to me that I can just delete the line myself, so I do.

Now the tests. I got what I expected. In quartile\_sampler\_test.go:

```
func TestQuartileSampler(t *testing.T) {  
   tests := []struct {  
       name     string  
       data     []float64  
       wantQ1   float64  
       wantMed  float64  
       wantQ3   float64  
       epsilon  float64 // allowed error for floating point comparison  
   }{  
       {  
           name:    "basic sequence",  
           data:    []float64{1, 2, 3, 4, 5, 6, 7},  
           wantQ1:  2,  
           wantMed: 4,  
           wantQ3:  6,  
           epsilon: 0.1,  
       },  
	…  
   }

   for _, tt := range tests {  
       t.Run(tt.name, func(t *testing.T) {  
           qs := NewQuartileSampler(100) // Use large reservoir for accurate testing  
           for _, v := range tt.data {  
               qs.Add(v)  
           }

           q1, med, q3 := qs.Quartiles()  
            
           if math.Abs(q1-tt.wantQ1) > tt.epsilon {  
               t.Errorf("Q1 = %v, want %v (±%v)", q1, tt.wantQ1, tt.epsilon)  
           }  
           if math.Abs(med-tt.wantMed) > tt.epsilon {  
               t.Errorf("Median = %v, want %v (±%v)", med, tt.wantMed, tt.epsilon)  
           }  
           if math.Abs(q3-tt.wantQ3) > tt.epsilon {  
               t.Errorf("Q3 = %v, want %v (±%v)", q3, tt.wantQ3, tt.epsilon)  
           }  
       })  
   }
}
```

Exactly the sort of thing I would write! I would run some cases through another implementation to generate expected outputs and copy them into a test like this. But there are two issues with this.

The first is the LLM did _not_ run these numbers through another implementation. (To the best of my knowledge. When using a sophisticated LLM service, it is hard to say for sure what is happening behind the scenes.) It made them up, and LLMs have a reputation for being weak at arithmetic. So this sort of test, while reasonable for a human to write because we base it on the output of another tool, or if we are particularly old-school do some arithmetic ourselves, is not great from an LLM.

The second issue with this is we can do better. I am happy we now live in a time when programmers write their own tests, but we do not hold ourselves to the same standards with tests as we do with production code. That is a reasonable tradeoff, there are only so many hours in the day. But what LLMs lack in arithmetical prowess, they make up for in enthusiasm.

Let’s ask for an even better test.

> In the tests, implement the simplest, most readable version of the standard code for quartiles over a fixed set of known values in a slice. Then pass the test cases through the standard code and the reservoir sampler and confirm they are within an epsilon of each other. Structure the comparison code such that it can be used in a fuzz test too.

This got us some new test code:

```
// referenceQuartiles calculates the exact quartiles for a slice of float64 values  
// using linear interpolation, matching the behavior expected from the sampler.  
func referenceQuartiles(data []float64) (q1, median, q3 float64) { … }

// compareQuartiles checks if two sets of quartiles are within epsilon of each other.  
// Returns true if they match within the tolerance, false otherwise.  
func compareQuartiles(q1a, meda, q3a, q1b, medb, q3b, epsilon float64) bool { … }

// checkQuartiles is a test helper that compares sampler output against the reference  
// implementation and reports any differences.  
func checkQuartiles(t *testing.T, data []float64, epsilon float64) {  
   t.Helper()  
    
   // Get reference values  
   wantQ1, wantMed, wantQ3 := referenceQuartiles(data)  
    
   // Get sampler values using a large reservoir for accuracy  
   qs := NewQuartileSampler(1000)  
   for _, v := range data {  
       qs.Add(v)  
   }  
   gotQ1, gotMed, gotQ3 := qs.Quartiles()  
    
   if !compareQuartiles(gotQ1, gotMed, gotQ3, wantQ1, wantMed, wantQ3, epsilon) {  
       t.Errorf("Quartiles mismatch:\ngot  (q1=%v, med=%v, q3=%v)\nwant (q1=%v, med=%v, q3=%v)\nepsilon=%v",  
           gotQ1, gotMed, gotQ3, wantQ1, wantMed, wantQ3, epsilon)  
   }  
}
```

The original test from above has been reworked to to use checkQuartiles and we have something new:

```
func FuzzQuartileSampler(f *testing.F) {  
   // Add some seed corpus  
   f.Add([]float64{1, 2, 3, 4, 5})  
    
   f.Fuzz(func(t *testing.T, data []float64) {  
       // Use a larger epsilon for fuzzing since we might get more extreme values  
       checkQuartiles(t, data, 0.2)  
   })  
}
```

This is fun, because it's wrong. My running `gopls` tool immediately says:

```
fuzzing arguments can only have the following types:
    string, bool, float32, float64,
    int, int8, int16, int32, int64,
    uint, uint8, uint16, uint32, uint64,
    []byte
```

Pasting that error back into the LLM gets it to regenerate the fuzz test such that it is built around a `func(t *testing.T, data []byte)` function that uses `math.Float64frombits` to extract floats from the data slice. Interactions like this point us towards automating the feedback from tools: all it needed was the obvious error message to make solid progress towards something useful. I was not needed.

Doing a quick survey of the last few weeks of my LLM chat history shows (which as I mentioned earlier, is not a proper quantitative analysis by any measure) that more than 80% of the time there is a tooling error, the LLM can make useful progress without me adding any insight. About half the time it can completely resolve the issue without me saying anything of note, I am just acting as the messenger.

Where are we going? Better tests, maybe even less DRY
-----------------------------------------------------

There was a programming movement some 25 years ago focused around the principle “don’t repeat yourself.” As is so often the case with short snappy principles taught to undergrads, it got taken too far. There is a lot of cost associated with abstracting out a piece of code so it can be reused, it requires creating intermediate abstractions that must be learned, and it requires adding features to the factored out code to make it maximally useful to the maximum number of people, which means we depend on libraries filled with useless distracting features.

The past 10-15 years has seen a far more tempered approach to writing code, with many programmers understanding it is better to reimplement a concept if the cost of sharing the implementation is higher than the cost of implementing and maintaining separate code. It is far less common for me to write on a code review “this isn’t worth it, separate the implementations.” (Which is fortunate, because people really don’t want to hear things like that after they have done all the work.) Programmers are getting better at tradeoffs.

What we have now is a world where the tradeoffs have shifted. It is now easier to write more comprehensive tests. You can have the LLM write the fuzz test implementation you want but didn’t have the hours to build properly. You can spend a lot more time writing tests to be readable, because the LLM is not sitting there constantly thinking “it would be better for the company if I went and picked another bug off the issue tracker than doing this.” So the tradeoff shifts in favor of having more specialized implementations.

The place where I expect this to be most visible is language-specific _REST API wrappers_. Every major company API comes with dozens of these, usually low quality, wrappers written by people who aren’t actually using their implementations for a specific goal, instead are trying to capture every nook and cranny of an API in a large and complex interface. Even when it is done well, I have found it easier to go to the REST documentation (usually a set of curl commands), and implement a language wrapper for the 1% of the API I actually care about. It cuts down the amount of the API I need to learn upfront, and it cuts down how much future programmers (myself) reading the code need to understand.

For example, as part of my recent work on sketch.dev I implemented a Gemini API wrapper in Go. Even though the [official wrapper](https://pkg.go.dev/github.com/google/generative-ai-go@v0.19.0/genai) in Go has been carefully handcrafted by people who know the language well and clearly care, there is a lot to read to understand it:

```
$ go doc -all genai | wc -l  
    1155
```

My simplistic initial wrapper was 200 lines of code total, one method, three types. Reading the entire implementation is 20% of the work of reading the documentation of the official package, and if you decide to try digging into its implementation you will discover that it is a wrapper around another largely code-generated implementation with protos and grpc and the works. All I want is to cURL and parse a JSON object.

There obviously comes a point in a project, where Gemini is the foundation of the entire app, where nearly every feature is used, where building on gRPC aligns well with the telemetry system elsewhere in your organization, where you should use the large official wrapper. But most of the time it is so much more time consuming, both upfront and ongoing, to do so given we almost always want only some wafer-thin sliver of whatever API we need to use today, that custom clients, largely written by a GPU, are far more effective for getting work done.

So I foresee a world with far more specialized code, with fewer generalized packages, and more readable tests. Reusable code will continue to thrive around small robust interfaces and otherwise will be pulled apart into specialized code. Depending how well this is done, it will lead to either better software or worse software. I would expect both, with a long-term trend towards better software by the metrics that matter.

Automating these observations: sketch.dev
-----------------------------------------

As a programmer my instinct is to make computers do work for me. It is a lot of work getting value out of LLMs, how can a computer do it?

I believe the key to solving a problem is not to overgeneralize. Solve a particular problem and then expand slowly. So instead of building a general-purpose UI for chat programming that is just as good at COBOL as it is for Haskell, we want to focus on one particular environment. The bulk of my programming is in Go, and so what I want is easy to imagine for a Go programmer:

*   something like the Go playground, built around editing a package and tests  
    
*   with a chat interface onto editable code  
    
*   a little UNIX env where we can run go get and go test  
    
*   goimports integration  
    
*   gopls integration  
    
*   automatic model feedback: on model edit run go get, go build, go test, feedback missing packages, compiler errors, test failures to the model to try and get them fixed automatically

A few of us have built an early prototype of this: [sketch.dev](https://sketch.dev/).

The goal is not a “Web IDE” but rather to challenge the notion that chat-based programming even belongs in what is traditionally called an IDE. IDEs are collections of tools arranged for people. It is a delicate environment where I know what is going on. **I do not want an LLM spewing its first draft all over my current branch.** While an LLM is ultimately a developer tool, it is one that needs its own IDE to get the feedback it needs to operate effectively.

Put another way: we didn’t embed goimports into sketch for it to be used by humans, but to get Go code closer to compiling using automatic signals, so that the compiler can provide better error feedback to the LLM driving it. It might be better to think of sketch.dev as a “Go IDE for LLMs”.

This is all very recent work with a lot left to do, e.g. git integration so we can load existing packages for editing and drop the results on a branch. Better test feedback. More console control. (If the answer is to run sed, run sed. Be you the human or the LLM.) We are still exploring, but are convinced that focusing an environment for a particular kind of programming will give us better results than the generalized tool.
