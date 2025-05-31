Title: In C++, use exchange or swap with nullopt to move out of std::optional

URL Source: https://keunwoo.com/notes/cpp-moving-std-optional/

Markdown Content:
What to do
----------

When you want to move out of C++ [`std::optional`](https://en.cppreference.com/w/cpp/utility/optional) in an expression, prefer to `std::exchange` it with a `std::nullopt`:

```
std::optional<std::string> src = "hi";
auto dest = std::exchange(src, std::nullopt);
```

The source receives the `nullopt` state (so it no longer holds a value), and the expression evaluates to the optional’s former state. If the source was `nullopt`, then the expression evaluates to `nullopt`; if you are sure that the source is non-`nullopt`, then you can immediately use `.value()` or dereference `*` on the expression to obtain the underlying value.

(For readers familiar with Rust, this is analogous to [Option::take](https://doc.rust-lang.org/std/option/enum.Option.html#method.take).)

Using [`std::swap`](https://en.cppreference.com/w/cpp/algorithm/swap) also works, but requires a separate statement and a previously declared swap destination that is “move-assignable”:

```
std::optional<std::string> swap_src = "hi";
std::optional<std::string> swap_dest;
std::swap(swap_src, swap_dest);
```

In some cases, swap may be more efficient, because it is more common for swap to be template-specialized than exchange, but the difference is unlikely to matter outside of hot loops. Consult [Godbolt](https://godbolt.org/) and a profiler if performance is an overriding concern; otherwise prefer the version that’s more readable.

What not to do: pitfalls of other approaches
--------------------------------------------

It is tempting to only move the optional:

```
std::optional<std::string> moved_from_optional = "hi";
auto only_moved_to = std::move(moved_from_optional);
std::cout << "moved_from_optional: " << moved_from_optional.has_value() << std::endl;
```

but this leaves the original in the non-`nullopt` state (older C++ standards proposals call this the “engaged” state, but modern references don’t seem to use this terminology). The snippet above will print `moved_from_optional: 1`.

Leaving the moved-from optional with the hollowed-out, moved-from value is almost never useful. In the above example, `moved_from_optional` contains the empty string. It is almost certainly a programming defect to use this value in any way; you’re probably better off with an optional that returns false from `.has_value()` and throws on `.value()`.

What if we only move the contained value, not the `optional`? The same result pertains:

```
std::optional<std::string> moved_from_value = "hi";
auto moved_value = std::move(moved_from_value.value());
std::cout << "moved_from_value: " << moved_from_value.has_value() << std::endl;
```

This will print `moved_from_value: 1`.

Note that there are multiple references out there suggesting that one of the above approaches is better than the other. This is wrong: for most practical purposes, they are not even meaningfully different, and neither is what you want in the common case. The only benefit, compared to doing `exchange` or `swap` with a `nullopt`, is that you might save an instruction clearing the discriminant field of the optional. In most cases, this is unlikely to matter, and may even be optimized away if the compiler can detect that the source optional is dead after the move.

One can make raw move less error-prone by following it with a separate `reset` call; the following call will print `move_then_reset: 0`:

```
std::optional<std::string> move_then_reset = "hi";
auto moved_to = std::move(move_then_reset);
move_then_reset.reset();
std::cout << "move_then_reset: " << move_then_reset.has_value() << std::endl;
```

This prints `moved_then_reset: 0`. However, this seems strictly worse than using `std::exchange`: it is more verbose and requires more diligence.

Postscript
----------

A couple of closing thoughts:

First, as of writing, none of the top hits on Stack Overflow or Google currently recommend using `std::exchange` or `std::swap` for this task, even though they have been in the standard since C++14 and C++11 respectively. The actual best other source I can find is [this answer on StackOverflow](https://stackoverflow.com/a/71981117), which is not even the top voted response on its question. I don’t know what to make of this, other than to point out that if you’re doing engineering, then (a) don’t expect other people to do your work for you, and (b) recognize that our information ecosystem does not reliably rank the best information most highly.

Second, this post is one of just a handful of pieces of writing that I’ve posted to my extremely sparse homepage in the past few years. You might guess from this that I am some kind of C++ aficionado. In reality, I have written only tens of KLOC of C++ code in my entire life, and the necessity of mastering countless subtleties like the above to do mundane tasks well is a major reason that I dislike C++. Even “modern” C++ is a terrifying mountain of complexity and user-hostile design with minimal guardrails to prevent you from tumbling down, and it is not true, as is often claimed, that you can easily avoid the steep ledges by sticking to “modern” idioms. (For example, bonus fact about `std::optional`: the standard does not promise that dereferencing an unset (`nullopt`) optional fails in any well-defined way; it’s simply undefined behavior.) If the use of C++ for building important large-scale systems does not worry you, then you either don’t know enough C++ or you fundamentally misunderstand the stochastic nature of software engineering at scale.

Appendix: Complete demonstration code
-------------------------------------

Save this as optional.cpp and run `g++ --std=c++17 optional.cpp && ./a.out`:

```
#include <iostream>
#include <optional>
#include <utility>

template <typename T>
void print(const char *prefix, const std::optional<T> &opt) {
    std::cout << prefix;
    if (opt.has_value()) {
        std::cout << "some(" << *opt << ")";
    } else {
        std::cout << "none";
    }
    std::cout << std::endl;
}

int main() {
    std::optional<std::string> src = "hi";
    auto dest = std::exchange(src, std::nullopt);
    print("src: ", src);
    print("dest: ", dest);
    std::cout << std::endl;

    std::optional<std::string> swap_src = "hi";
    std::optional<std::string> swap_dest;
    std::swap(swap_src, swap_dest);
    print("swap_src: ", swap_src);
    print("swap_dest: ", swap_dest);
    std::cout << std::endl;

    std::optional<std::string> moved_from_optional = "hi";
    auto only_moved_to = std::move(moved_from_optional);
    print("moved_from_optional: ", moved_from_optional);
    print("only_moved_to: ", only_moved_to);
    std::cout << std::endl;

    std::optional<std::string> moved_from_value = "hi";
    auto moved_value = std::move(moved_from_value.value());
    print("moved_from_value: ", moved_from_value);
    std::cout << "moved_value (not an optional): " << moved_value << std::endl;
    std::cout << std::endl;

    std::optional<std::string> move_then_reset = "hi";
    auto moved_to = std::move(move_then_reset);
    move_then_reset.reset();
    print("move_then_reset: ", move_then_reset);
    print("moved_to: ", moved_to);

    return 0;
}
```

Output:

```
src: none
dest: some(hi)

swap_src: none
swap_dest: some(hi)

moved_from_optional: some()
only_moved_to: some(hi)

moved_from_value: some()
moved_value (not an optional): hi

move_then_reset: none
moved_to: some(hi)
```
