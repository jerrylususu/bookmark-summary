Title: Gist of Go: Pipelines

URL Source: https://antonz.org/go-concurrency/pipelines/

Markdown Content:
_This is a chapter from my book on [Go concurrency](https://antonz.org/go-concurrency), which teaches the topic from the ground up through interactive examples._

We've learned how to use [goroutines](https://antonz.org/go-concurrency/goroutines/) and [channels](https://antonz.org/go-concurrency/channels/), now let's see how to assemple them into concurrent pipelines!

*   [Leaked goroutine](https://antonz.org/go-concurrency/pipelines/#leaked-goroutine)
*   [Cancel channel](https://antonz.org/go-concurrency/pipelines/#cancel-channel)
*   [Cancel vs. done](https://antonz.org/go-concurrency/pipelines/#cancel-vs-done)
*   [Merging: sequentially](https://antonz.org/go-concurrency/pipelines/#merging-channels-sequentially)
*   [Merging: concurrently](https://antonz.org/go-concurrency/pipelines/#merging-channels-concurrently)

*   [Merging: select](https://antonz.org/go-concurrency/pipelines/#merging-channels-select)
*   [Pipeline](https://antonz.org/go-concurrency/pipelines/#pipeline)
*   [Preventing goroutine leaks](https://antonz.org/go-concurrency/pipelines/#preventing-goroutine-leaks)
*   [Keep it up](https://antonz.org/go-concurrency/pipelines/#keep-it-up)

Leaked goroutine
----------------

Here's a function that sends numbers within a specified range to a channel:

```
func rangeGen(start, stop int) <-chan int {
    out := make(chan int)
    go func() {
        for i := start; i < stop; i++ {
            out <- i
        }
        close(out)
    }()
    return out
}
```

It seems to work fine:

```
func main() {
    generated := rangeGen(41, 46)
    for val := range generated {
        fmt.Println(val)
    }
}
```

Let's see what happens if we exit the loop early:

```
func main() {
    generated := rangeGen(41, 46)
    for val := range generated {
        fmt.Println(val)
        if val == 42 {
            break
        }
    }
}
```

At first glance, it still works correct. But not quite — the `rangeGen()` goroutine is stuck:

```
func rangeGen(start, stop int) <-chan int {
    out := make(chan int)
    go func() {
        for i := start; i < stop; i++ {    // (1)
            out <- i                       // (2)
        }
        close(out)
    }()
    return out
}
```

Since `main()` breaks its loop at number 42 and stops reading from the `generated` channel, the loop inside `rangeGen()` ➊ didn't finish. It got permanently blocked trying to send number 43 to the `out` channel ➋. The goroutine is stuck. The`out` channel didn't close, so if other goroutines depended on it, they would also get stuck.

In this case, it's not a big deal: when `main()` exits, the runtime will terminate all other goroutines. But if `main()` continued to run and called `rangeGen()` repeatedly, the leaked goroutines would pile up. This is problematic: goroutines are lightweight but not completely "free". Eventually, you might run out of memory (the garbage collector doesn't collect goroutines).

Seems like we need a way to terminate a goroutine early.

Cancel channel
--------------

First, we'll create a separate _cancel channel_ through which `main()` will signal `rangeGen()` to exit:

```
func main() {
    cancel := make(chan struct{})    // (1)
    defer close(cancel)              // (2)

    generated := rangeGen(cancel, 41, 46)    // (3)
    for val := range generated {
        fmt.Println(val)
        if val == 42 {
            break
        }
    }
}
```

We create a `cancel` channel ➊ and immediately set up a deferred `close(cancel)` ➋. This is a common practice to avoid tracking every place in the code where the channel needs to be closed. `defer` ensures that the channel is closed when the function exits, so you don't have to worry about it.

Next, we pass the `cancel` channel to the goroutine ➌. Now, when the channel closes, the goroutine needs to detect this and exit. Ideally, you'd add a check like this:

```
func rangeGen(cancel <-chan struct{}, start, stop int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for i := start; i < stop; i++ {
            out <- i
            if <-cancel == struct{}{} {    // (1)
                return
            }
        }
    }()
    return out
}
```

```
fatal error: all goroutines are asleep - deadlock!
```

If `cancel` is closed, the check ➊ will pass (a closed channel always returns a zero value, remember?), and the goroutine will exit. However, if `cancel` isn't closed, the goroutine would block and not continue to the next loop iteration.

We need a different, non-blocking approach:

*   If `cancel` is closed, exit the goroutine;
*   Otherwise, send the next value to `out`.

Go has a _select_ statement for this:

```
func rangeGen(cancel <-chan struct{}, start, stop int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for i := start; i < stop; i++ {
            select {
            case out <- i:    // (1)
            case <-cancel:    // (2)
                return
            }
        }
    }()
    return out
}
```

`select` is somewhat like `switch`, but specifically designed for channels. Here's what it does:

*   Checks which cases are not blocked.
*   If multiple cases are ready, randomly selects one to execute.
*   If all cases are blocked, waits until one is ready.

In our case, while `cancel` is open, its case ➋ is blocked (you can't read from a channel if no one is writing to it). However, the `out <- i` case ➊ is unblocked because `main()` is reading from `out`. So, `select` will execute `out <- i` in each loop iteration.

Then `main()` will reach number 42 and stop reading from `out`. After that, both `select` cases will block, and the goroutine will (temporarily) hang.

Finally, `main()` will execute the deferred `close(cancel)`, which will unblock the second `select` case ➋, and the goroutine will exit. The `out` channel will close too, thanks to `defer`.

If `main()` decides not to stop at 42 and continues to read all values, the cancel channel approach will still work correctly:

```
func main() {
    cancel := make(chan struct{})
    defer close(cancel)

    generated := rangeGen(cancel, 41, 46)
    for val := range generated {
        fmt.Println(val)
    }
}
```

```
41
42
43
44
45
```

Here, `rangeGen()` will finish before `main()` calls `close(cancel)`. Which is perfectly fine.

So thanks to the cancel channel and the select statement, the `rangeGen()` goroutine will exit correctly regardless of what happens in `main()`. No more leaked goroutines!

Cancel vs. done
---------------

The cancel channel is similar to the done channel that we covered in the previous chapter.

Done channel:

```
// Goroutine B receives a channel to signal
// when it has finished its work.
func b(done chan<- struct{}) {
    // do work...
    done <- struct{}{}
}

func a() {
    done := make(chan struct{})
    go b(done)
    // Goroutine A waits for B to finish its work.
    <-done
}
```

Cancel channel:

```
// Goroutine B receives a channel
// to get a cancel signal.
func b(cancel <-chan struct{}) {
    // do work...
    select {
    case <-cancel:
        return
    }
}

func a() {
    cancel := make(chan struct{})
    go b(cancel)
    // Goroutine A signals to B
    // that it is time to stop.
    close(cancel)
}
```

In practice, both cancel and done channels are often named "done", so don't be surprised. In the book, I'll use "cancel" for cancellation and "done" for completion to avoid confusion.

**✎ Exercise: Canceling goroutines**

Practice is essential for turning knowledge into skills, making theory alone insufficient. The full version of the book contains a lot of interactive exercises with automated tests — that's why I recommend [getting it](https://antonz.gumroad.com/l/go-concurrency).

If you're okay with just reading for now, let's continue.

Merging channels (sequentially)
-------------------------------

Sometimes several independent functions send results to their own channels. But it's more convenient to work with a single result channel. So you need to merge the output channels of these functions into a single channel.

The `rangeGen()` function sends numbers in a specified range to a channel:

```
func rangeGen(start, stop int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for i := start; i < stop; i++ {
            time.Sleep(50 * time.Millisecond)
            out <- i
        }
    }()
    return out
}
```

> For the sake of simplicity, we'll work with non-cancelable goroutines in this and the following steps. You already know how to turn any non-cancelable goroutine into a cancelable one (by adding a cancel channel).

Let's run `rangeGen()` twice, merge the output channels, and print the results:

```
func main() {
    in1 := rangeGen(11, 15)
    in2 := rangeGen(21, 25)

    start := time.Now()
    merged := merge(in1, in2)
    for val := range merged {
        fmt.Print(val, " ")
    }
    fmt.Println()
    fmt.Println("Took", time.Since(start))
}
```

Now we just need to implement the `merge()` function.

Here's the first idea that comes to mind. Iterate through the first channel, then the second, and send the results to the merged channel:

```
func merge(in1, in2 <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for val := range in1 {
            out <- val
        }
        for val := range in2 {
            out <- val
        }
    }()
    return out
}
```

```
11 12 13 14 21 22 23 24
Took 350ms
```

However, this implementation does not support concurrency. While `merge()` reads results from the first `rangeGen()` goroutine, the second `rangeGen()` goroutine is blocked — no one is ready to read from its output channel. That's why it took 350 ms instead of the expected 200 ms (8 values \* 50 ms / 2 goroutines = 200 ms).

We need a different approach.

Merging channels (concurrently)
-------------------------------

To read the input channels independently, let's start two goroutines:

```
func merge(in1, in2 <-chan int) <-chan int {
    var wg sync.WaitGroup
    wg.Add(2)

    out := make(chan int)

    // The first goroutine reads from in1 to out.
    go func() {
        defer wg.Done()
        for val := range in1 {
            out <- val
        }
    }()

    // The second goroutine reads from in2 to out.
    go func() {
        defer wg.Done()
        for val := range in2 {
            out <- val
        }
    }()

    // Wait until both input channels are exhausted,
    // then close the output channel.
    go func() {
        wg.Wait()
        close(out)
    }()

    return out
}
```

```
11 21 12 22 23 13 14 24
Took 200ms
```

Thanks to `merge()` processing the output channels of two `rangeGen()`s concurrently, `main()` takes 200 ms, just as we expected. Nice!

Merging channels (select)
-------------------------

You can get by with a single goroutine while maintaining performance — by using the `select` statement. Note its useful property:

> If multiple branches are unblocked, it randomly selects and executes one of them.

So selecting one branch from `in1` and another from `in2` should be almost as fast as using two independent goroutines:

```
func merge(in1, in2 <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for {
            select {
            case out <- <-in1:
            case out <- <-in2:
            }
        }
    }()
    return out
}
```

In practice, however, it looks something like this:

```
21 11 12 22 13 23 24 14 0 0 0 0 0 0 0 0 0 0... and so on
```

This implementation keeps selecting values from the input channels even after they are closed — indefinitely.

Here's an idea on how to fix it:

*   Select values from `in1` only if it's open.
*   Select values from `in2` only if it's open.
*   Exit the loop if both `in1` and `in2` are closed.

Select can handle this thanks to the nil channels property discussed in the previous chapter:

> Reading from a nil channel blocks the goroutine forever.

If you set `in1` to nil after it closes, select will stop reading from it (since it ignores blocked branches). The same goes for `in2`:

```
func merge(in1, in2 <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for in1 != nil || in2 != nil {
            select {
            case val1, ok := <-in1:
                if ok {
                    out <- val1
                } else {
                    in1 = nil
                }

            case val2, ok := <-in2:
                if ok {
                    out <- val2
                } else {
                    in2 = nil
                }
            }
        }
    }()
    return out
}
```

```
21 11 22 12 23 13 24 14
Took 200ms
```

Now each select branch is disabled after its corresponding channel is closed. When both channels are closed, the for loop stops.

Works like a charm!

> Remember I mentioned that nil channels are useful in some special cases? This is one of them.

**✎ Exercise: Merging N channels**

Practice is essential for turning knowledge into skills, making theory alone insufficient. The full version of the book contains a lot of interactive exercises with automated tests — that's why I recommend [getting it](https://antonz.gumroad.com/l/go-concurrency).

If you're okay with just reading for now, let's continue.

Pipeline
--------

A _pipeline_ is a sequence of operations where each step takes input data, processes it in a specific way, and outputs it. The input and output of each operation is a channel.

In fact, we've been building pipelines for the last three chapters. Let's reinforce this concept.

A typical pipeline looks like this:

*   _Reader_: Reads input data from a file, database, or network.
*   _N processors_: Transform, filter, aggregate, or enrich data using external sources.
*   _Writer_: Writes the processed data to a file, database, or network.

There can be any number of processing stages: e.g., first filter, then transform, then aggregate. Each stage can have multiple concurrent processors, but often there's only one reader and one writer.

Consider a 5-stage pipeline:

*   `rangeGen()` generates numbers within a given range (reader).
*   `takeLucky()` selects "lucky" numbers (processor).
*   `merge()` combines independent channels (processor).
*   `sum()` sums the numbers (processor).
*   `printTotal()` prints the result (writer).

```
┌─────────────┐
│   rangeGen  │
└─────────────┘
       │
  readerChan─┬────────┬──────────────┬──────────────┐
┌─────────────┐┌─────────────┐┌─────────────┐┌─────────────┐
│  takeLucky  ││  takeLucky  ││  takeLucky  ││  takeLucky  │
└─────────────┘└─────────────┘└─────────────┘└─────────────┘
       │               │              │              │
 luckyChans[0]   luckyChans[1]  luckyChans[2]  luckyChans[3]
       │               │              │              │
┌──────────────────────────────────────────────────────────┐
│                           merge                          │
└──────────────────────────────────────────────────────────┘
       │
   mergedChan
       │
┌─────────────┐
│     sum     │
└─────────────┘
       │
   totalChan
       │
┌─────────────┐
│ printTotal  │
└─────────────┘
```

In code:

```
// Total represents the count
// and the sum of the lucky numbers.
type Total struct {
    count  int
    amount int
}

// rangeGen generates numbers within a given range.
func rangeGen(start, stop int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for i := start; i < stop; i++ {
            out <- i
        }
    }()
    return out
}

// takeLucky selects lucky numbers.
func takeLucky(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for num := range in {
            if num%7 == 0 && num%13 != 0 {
                out <- num
            }
        }
    }()
    return out
}

// sum sums the numbers.
func sum(in <-chan int) <-chan Total {
    out := make(chan Total)
    go func() {
        defer close(out)
        total := Total{}
        for num := range in {
            total.amount += num
            total.count++
        }
        out <- total
    }()
    return out
}

// printTotal prints the result.
func printTotal(in <-chan Total) {
    total := <-in
    fmt.Printf("Total of %d lucky numbers = %d\n", total.count, total.amount)
}

func main() {
    readerChan := rangeGen(1, 1000)
    luckyChans := make([]<-chan int, 4)
    for i := range 4 {
        luckyChans[i] = takeLucky(readerChan)
    }
    mergedChan := merge(luckyChans)
    totalChan := sum(mergedChan)
    printTotal(totalChan)
}
```

```
Total of 132 lucky numbers = 66066
```

Even for a toy task like this, a pipeline is more convenient than a single large function:

*   Each stage performs a single task, making the code easier to understand.
*   You can add or remove stages without affecting the rest of the logic.
*   You can adjust the level of parallelism in each stage independently.
*   Stages can be reused in other pipelines.

"Read-process-write" tasks are common in practice, and pipelines work pretty well for them.

Preventing goroutine leaks
--------------------------

Leaked goroutines are the second most common problem in concurrent programs after deadlocks. Go doesn't complain about them, so they often go unnoticed.

In this book, stuck goroutines cause an error in the exercises:

```
ERROR: there are leaked goroutines
```

Common reasons why goroutines get stuck:

*   You forgot to create a cancel channel and check it via select.
*   There is a cancel channel, but the goroutine gets stuck inside the select (yes, really!)

We covered the first reason earlier in the chapter, so let's look at the second. It often catches people off guard.

Suppose there's a function that sends numbers to a channel:

```
func generate(cancel <-chan struct{}) chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for i := 0; ; i++ {
            select {
            case out <- i:
            case <-cancel:
                return
            }
        }
    }()
    return out
}
```

And a function that modifies numbers:

```
func modify(cancel <-chan struct{}, in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer fmt.Println("modify done")    // (1)
        defer close(out)
        for {
            select {
            case num := <-in:
                out <- num * 2
            case <-cancel:
                return
            }
        }
    }()
    return out
}
```

Thanks to ➊, the goroutine prints when it is done.

Together, these two functions would run indefinitely, so let's add a third that reads the first 10 numbers and stops:

```
func print(in <-chan int) {
    for range 10 {
        <-in
        fmt.Printf(".")
    }
    fmt.Println()
}
```

Let's run it:

```
func main() {
    cancel := make(chan struct{})
    c1 := generate(cancel)
    c2 := modify(cancel, c1)
    print(c2)

    close(cancel)
    // Wait some time for the goroutines to finish
    // after the cancel channel is closed.
    time.Sleep(50 * time.Millisecond)
}
```

Seems to work. After all, we used select + cancel everywhere, so there shouldn't be an error.

But there is. To see it, just add a 10 ms delay ➊:

```
func modify(cancel <-chan struct{}, in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer fmt.Println("modify done")
        defer close(out)
        for {
            select {
            case num := <-in:
                time.Sleep(10 * time.Millisecond)    // (1)
                out <- num * 2                       // (2)
            case <-cancel:
                return
            }
        }
    }()
    return out
}
```

The "modify done" text is never printed. That's because the `modify()` goroutine got stuck at point ➋. When the `cancel` channel closed, it was waiting to write to `out` inside a select branch, so the select couldn't help anymore.

There are two ways to deal with this. The first is to keep the select branches empty:

```
func modify(cancel <-chan struct{}, in <-chan int) <-chan int {
    out := make(chan int)

    multiply := func(num int) int {
        time.Sleep(10 * time.Millisecond)
        return num * 2
    }

    go func() {
        defer fmt.Println("modify done")
        defer close(out)
        for num := range in {
            select {
            case out <- multiply(num):
            case <-cancel:
                return
            }
        }
    }()
    return out
}
```

No matter how slow the `multiply()` function is, we won't fall into the select branch, so closing the `cancel` channel is guaranteed to trigger a return.

The second way is to use nested selects wherever you are reading from or writing to a channel:

```
func modify(cancel <-chan struct{}, in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer fmt.Println("modify done")
        defer close(out)
        for {
            select {
            case num, ok := <-in:
                if !ok {
                    return
                }
                time.Sleep(10 * time.Millisecond)
                select {
                case out <- num * 2:
                case <-cancel:
                    return
                }
            case <-cancel:
                return
            }
        }
    }()
    return out
}
```

Here, the nested select protects us when writing to `out`, so nothing can hang.

The second example shows another important principle: If you use a regular for loop instead of for-range, always check if the input channel is closed. Better yet, use for-range whenever possible, so that it checks for you.

Concurrent programming is hard. Go provides useful primitives like channels and select, but they're not a panacea. Always test your code: both individual goroutines and their composition.

To check for goroutine leaks in tests, use `runtime.NumGoroutine()` or a more sophisticated solution like [goleaks](https://github.com/uber-go/goleak).

**✎ Exercise: Flipping unique words**

Practice is essential for turning knowledge into skills, making theory alone insufficient. The full version of the book contains a lot of interactive exercises with automated tests — that's why I recommend [getting it](https://antonz.gumroad.com/l/go-concurrency).

If you're okay with just reading for now, let's continue.

Keep it up
----------

Pipelines are one of the most common uses of concurrency in real-world programs. Now you know how to:

*   Combine pipelines of independent blocks.
*   Split and merge data streams.
*   Cancel pipeline stages.
*   Prevent goroutine leaks.

In the next chapter, we'll work with time (coming soon).

[Pre-order for $10](https://antonz.gumroad.com/l/go-concurrency)   or [read online](https://antonz.org/go-concurrency/)

[★ Subscribe](https://antonz.org/subscribe/) to keep up with new posts.
