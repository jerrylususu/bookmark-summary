Title: Making algorithms faster

URL Source: https://learnmoderncpp.com/2024/10/12/making-algorithms-faster/

Published Time: 2024-10-12T07:58:33+00:00

Markdown Content:
It is possible to write poor-quality code in any programming language, and this often stems from sub-optimal algorithms being used. Most of the execution time in modern software is spent in loops, so making these as efficient as possible is effort well spent. In addition, we want to utilize all of the CPUs available in a modern machine to maximize throughput. In this article we’ll perform a case-study of a simple algorithm being improved and parallelized, together with benchmarking to demonstrate the real-world gains.

Pythagoras’ Theorem states that for a right-triangle of sides _a_, _b_ and _c_, where the angle between _a_ and _b_ is 90°, the formula _a2 + b2 = c2_ always holds. There are an infinite number of right-triangles where all three numbers are integers, and these sets of numbers are called Pythagorean Triples. We can write a program to calculate all of the Pythagorean Triples up to a given maximum hypotenuse in order from smallest to greatest. Let’s start by defining the types to be used:

template<typename T\>
struct PythagoreanTriple {
    T a, b, c;
};
using Side = unsigned;

Using a generic struct allows changing the type in one place in the future, and we are assuming that 32-bit `unsigned int`s are the fastest data type. A container to store the valid Triples can be defined as:

std::vector<PythagoreanTriple<Side\>\> triples;

The algorithm is three nested loops for each of the sides, where _a<b<c_ always holds. We only want to store unique triples, not those which are similar to earlier ones ({6,8,10} is similar to {3,4,5} so we don’t store it). This can be achieved by applying Euclid’s _greatest common divisor_ algorithm to all three sides, and if there is one greater than unity, not storing the triple.

void get\_triples(const Side limit\_c, std::vector<PythagoreanTriple<Side\>\> &triples) {
    for (Side c = 5; c != limit\_c; ++c) {
        for (Side b = 4; b != c; ++b) {
            for (Side a = 3; a != b; ++a) {
                if (a \* a + b \* b == c \* c && std::gcd(std::gcd(a, b), c) == 1) {
                    triples.emplace\_back(a, b, c);
                }
            }
        }
    }
}

With some boilerplate code which calls this function written, the output from calling this function is:

Maximum hypotenuse: 5000
Time elapsed: 14171350us
Number of triples: 792
Press Enter to view...
(3,4,5) (5,12,13) (8,15,17) (7,24,25) (20,21,29) (12,35,37) (9,40,41) (28,45,53) (11,60,61) (33,56,65) (16,63,65)...

This gives us a starting benchmark to compare to later versions:

Time taken (unoptimized)

Speed factor

14171350µs

1x

The nested loops execute in cubic time (_O3_) so it is worthwhile trying to make them quicker by taking advantage of other invariants (besides _a<b<c_). We observe that upon finding a triple, the innermost loop is done, so we can break out straightaway. Also, for the innermost loop, the invariant _a<√(c2\-b2)_ always holds, so we can reduce the extent of this loop significantly by calculating the limit of _a_ outside the loop. Here is the revised code:

void get\_triples(const Side limit\_c, std::vector<PythagoreanTriple<Side\>\> &triples) {
    for (Side c = 5; c != limit\_c; ++c) {
        for (Side b = 4; b != c; ++b) {
            Side limit\_a = sqrt(c \* c - b \* b) + 1;
            for (Side a = c - b; a < limit\_a && a < b; ++a) {
                if (a \* a + b \* b == c \* c && std::gcd(std::gcd(a, b), c) == 1) {
                    triples.emplace\_back(a, b, c);
                    break;
                }
            }
        }
   }
}

The use of a floating-point function with integer arithmetic may not appeal to some, but modern machines have fast floating-point and the speedup is noticeable:

Time taken (optimized)

Speed factor

5043447µs

2.81x

Having decided that there are no further optimizations to be made, we’ll investigate parallelizing the code. Many of the standard library algorithms have an initial (template) parameter to specify the execution policy, which is one of sequenced (in the style of a single-threaded for-loop), unsequenced (iterations can happen in any order), parallel (the order of iterations is guaranteed to commence in order) or parallel unsequenced (where the order of iterations is not guaranteed). The best way to parallelize this function would appear to be to rework the outer loop to use `std::for_each()` instead of `for()`:

template<typename T\>
void get\_triples(const T policy, const Side limit\_c, std::vector<PythagoreanTriple<Side\>\> &triples) {
    std::mutex mutex;
    std::vector<Side\> side\_c(limit\_c - 1);
    std::iota(side\_c.begin(), side\_c.end(), 1);
    std::for\_each(policy, side\_c.cbegin(), side\_c.cend(), \[&triples,&mutex\](const Side c){
        for (Side b = 1; b != c; ++b) {
            Side limit\_a = sqrt(c \* c - b \* b) + 1;
            for (Side a = c - b; a < limit\_a && a < b; ++a) {
                if (a \* a + b \* b == c \* c && std::gcd(std::gcd(a, b), c) == 1) {
                    std::unique\_lock<std::mutex\> lock(mutex);
                    triples.emplace\_back(a, b, c);
                    break;
                }
            }
        }
    });
}

A few things to notice about this modified function:

*   `std::for_each()` needs to iterate over a container (or entity which provides `begin()` and `end()`) so we populate a vector with all of the required values for `c`.
*   The optional first parameter to this function is the execution policy, which can be one of `std::seq`, `std::unseq`, `std::par` or `std::par_unseq`. This needs to be specified at compile-time by the caller function.
*   The fourth parameter is a lambda which captures the necessary variables and accepts a `Side` parameter being the element of the container being iterated over.
*   Write access to the `std::vector` of triples needs to be scheduled (although there is no guarantee of order for any policy other than `std::seq`), so we use a single `std::mutex` and a scoped `std::unique_lock` when a successful test is made.

It is important to benchmark with `std::seq` to ensure that adapting the code to use a standard library algorithm does not affect performance significantly. The full list of benchmarks for each policy is:

Time taken (policy)

Speed factor

5059061µs (sequenced)

2.80x

5088973µs (unsequenced)

2.78x

769096µs (parallel)

18.43x

767454µs (parallel unsequenced)

18.47x

As can be seen from this table, there is no significant performance degradation from using the standard algorithm, and both parallel algorithms show a significant speedup. It can be seen that parallelizing this algorithm had a bigger impact than optimizing it, but optimizing was worthwhile as it is equivalent to using three times as many CPUs.

The generalized method for making an algorithm faster which we have explored can be summarized as:

1.  Improve the algorithm in a single-threaded context as much as possible.
2.  Replace at least one of the loops with a standard library algorithm, testing with policy `std::seq` initially
3.  Make any changes necessary to accommodate the parallel algorithm, such as sorting the results if they can appear out-of-order.

Source code for this article can be [found on GitHub](https://learnmoderncpp.com/2024/10/12/making-algorithms-faster/).
