Title: Can LLMs write better code if you keep asking them to “write better code”?

URL Source: https://minimaxir.com/2025/01/write-better-code/

Published Time: 2025-01-02T09:30:00-08:00

Markdown Content:
In November 2023, after OpenAI [added the ability](https://openai.com/index/dall-e-3-is-now-available-in-chatgpt-plus-and-enterprise/) for ChatGPT to generate images from DALL-E 3 within the ChatGPT web interface, there was a [short-lived meme](https://lifehacker.com/tech/chat-gpt-make-it-more-ai-images-trend) where users gave the LLM a base image and kept asking the model to “make it more _X_”, where _X_ can be anything.

![Image 12: A regular guy becomes more “bro” every time. via /u/Jojop0tato on Reddit.](https://minimaxir.com/2025/01/write-better-code/bro.webp#center)

A regular guy becomes more “bro” every time. [via /u/Jojop0tato on Reddit.](https://www.reddit.com/r/ChatGPT/comments/18ukiz2/a_regular_guy_becomes_more_bro_every_time/)

![Image 13: Asked ChatGPT to make Santa Claus more and more serious. via /u/hessihan on Reddit.](https://minimaxir.com/2025/01/write-better-code/santa.webp#center)

Asked ChatGPT to make Santa Claus more and more serious. [via /u/hessihan on Reddit.](https://www.reddit.com/r/ChatGPT/comments/1887z49/asked_chatgpt_to_make_santa_claus_more_and_more/)

The trend quickly died as all of these images were very samey and uninteresting, aside from the unexplainable trend that all of the examples eventually converged into something cosmic, irrespective of the starting image and the prompt. Although the trend was [AI slop](https://en.wikipedia.org/wiki/AI_slop) before the term AI slop was codified, it’s still academically interesting that such a meaningless and vague prompt had _some_ appropriate impact on the final image, and that this change was obvious to the user.

What would happen if we tried a similar technique with code? LLM-generated code is unlikely to be slop (although [not impossible](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/)) as it follows strict rules, and unlike creative outputs such as images, code quality can be measured more objectively.

If code can indeed be improved simply through iterative prompting such as asking the LLM to “make the code better” — even though it’s very silly — it would be a massive productivity increase. And if that’s the case, what happens if you iterate on the code too much? What’s the equivalent of code going cosmic? There’s only one way to find out!

Casually Coding With An LLM
---------------------------

Despite researching and developing tooling around LLMs even long before ChatGPT, I haven’t been fond of using LLM code copilots such as [GitHub Copilot](https://github.com/features/copilot) for coding assistance. The constant mental context switching between “oh, the LLM autocompleted my code, neat”/“what question should I ask the LLM” and “is the LLM-generated code is actually _correct_ and not [hallucinating](https://en.wikipedia.org/wiki/Hallucination_%28artificial_intelligence%29) correct code” kept creating enough distractions that any productivity gains from using the AI were net neutral at best. That’s also disregarding the expensive cost of using said LLMs.

[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) has made me rethink things. Due to whatever secret sauce [Anthropic](https://www.anthropic.com/) used in its training, the latest version of Claude 3.5 Sonnet (`claude-3-5-sonnet-20241022`) has _incredible_ prompt adherence for all types of prompts, especially coding prompts. [Coding](https://www.vellum.ai/blog/llm-benchmarks-overview-limits-and-model-comparison) [benchmarks](https://aider.chat/docs/leaderboards/) confirm that testing between Claude 3.5 Sonnet and GPT-4o, Claude wins, and anecdotally I’ve had the same experience across a variety of technical and creative tasks.

### Initial Ask

For this experiment, we will give Claude 3.5 Sonnet an interview-style coding prompt using Python: one that is both simple and could be implemented by a novice software engineer, but one that can be heavily optimized. This simple, casual prompt represents how the typical software engineer uses LLMs. Additionally, the test prompt must also be wholly original and not taken from coding tests such as [LeetCode](https://leetcode.com/) or [HackerRank](https://www.hackerrank.com/), as LLMs were also likely trained on those and could possibly cheat by reciting the memorized answer.

> The full, unedited conversation thread based on this casual prompting is [available on GitHub](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md).

Therefore, here’s the test prompt that I’ve written myself:

```
Write Python code to solve this problem:

Given a list of 1 million random integers between 1 and 100,000, find the difference between the smallest and the largest numbers whose digits sum up to 30.
```

Providing that as the user prompt to the Claude API and setting `temperature=0` for the best/most deterministic answer [1](https://minimaxir.com/2025/01/write-better-code/#fn:1), results in this implementation:

```
import random

def digit_sum(n):
    """Calculate the sum of digits of a number"""
    return sum(int(digit) for digit in str(n))

def find_difference():
    # Generate list of 1 million random integers
    numbers = [random.randint(1, 100000) for _ in range(1000000)]

    # Initialize variables for min and max numbers with digit sum 30
    min_num = float('inf')  # Initialize to positive infinity
    max_num = float('-inf')  # Initialize to negative infinity

    # Find numbers whose digits sum to 30
    for num in numbers:
        if digit_sum(num) == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    # Check if we found any numbers with digit sum 30
    if min_num == float('inf') or max_num == float('-inf'):
        return "No numbers found with digit sum of 30"

    return max_num - min_num
```

[This implementation](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-initial-ask) is correct and consistent with what most novice Python programmers would write, with bonus handling if there are no valid numbers that fit the criteria. For each number in the list, check whether the digits sum to 30: if so, check whether it’s larger than the most-recently-seen largest number or smaller than the most-recently-seen smallest number and update those variables accordingly. After searching through the list, return the difference.

But I’m sure many coders reading that implementation got [nerd sniped](https://xkcd.com/356/) and are thinking about optimizations. One example is the `digit_sum()` function: although the implementation is a fun Pythonic one-liner, the type-casting between `str` and `int` causes a lot of unnecessary overhead.

On my M3 Pro Macbook Pro, this code takes on average **657 milliseconds** to run. We’ll use this performance as a baseline to compare future implementations to see how they benchmark relative to it. (spoilers: they’re _all_ faster)

### Iteration #1

Now we can ask Claude to improve the code by including its current answer and all that came before it as a part of the conversation prompt. Thus, we add the iteration prompt:

What, you though the title of this blog post was a joke? I _never_ joke.

Claude [now outputs](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-1) revised code, or as it says, “optimized version of the code with several improvements.” Instead of colocating all the code in functions, it decided to refactor it into a Python `class` and made it more object-oriented:

```
class DigitSumFinder:
    def __init__(self, target_sum: int = 30,
                 range_start: int = 1,
                 range_end: int = 100_000,
                 count: int = 1_000_000):
        self.target_sum = target_sum
        self.range_start = range_start
        self.range_end = range_end
        self.count = count

        # Pre-calculate digit sums for all possible numbers
        self.digit_sums = self._precompute_digit_sums()

    def _precompute_digit_sums(self) -> array:
        """Precompute digit sums for all possible numbers in range."""
        digit_sums = array('B', [0] * (self.range_end + 1))
        for num in range(self.range_start, self.range_end + 1):
            total = 0
            n = num
            while n:
                total += n % 10
                n //= 10
            digit_sums[num] = total
        return digit_sums

    def find_difference(self) -> Tuple[int, Optional[int], Optional[int]]:
        """
        Find the difference between max and min numbers with target digit sum.
        Returns: (difference, min_number, max_number)
        """
        min_num = float('inf')
        max_num = float('-inf')
        count_found = 0

        # Generate and process random numbers
        for _ in range(self.count):
            num = random.randint(self.range_start, self.range_end)
            if self.digit_sums[num] == self.target_sum:
                count_found += 1
                if num < min_num:
                    min_num = num
                if num > max_num:
                    max_num = num

        if count_found == 0:
            return 0, None, None

        return max_num - min_num, min_num, max_num
```

Here, the code does two smart algorithmic improvements:

*   When computing the digit sum it uses integer operations and avoids the need for the type-casting mentioned previously.
*   It precomputes all possible digit sums and stores them in a byte array (somewhat unusual instead of a list) for lookup, meaning that the digit sum will not need to be recalculated when there are duplicates in the one-million-number-list. Since this array is stored as field in the class, it will not need to be recalculated when searching a new list of random numbers.

These optimizations speed up the code **2.7x** relative to the initial implementation.

### Iteration #2

After another `write better code`, Claude [discovers](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-2) more obvious optimizations (truncated for readabilty):

```
class DigitSumAnalyzer:
    """Analyzes numbers based on their digit sums."""

    def __init__(self, number_range: NumberRange):
        self.number_range = number_range
        self._digit_sums = self._precompute_digit_sums()

    def _precompute_digit_sums(self) -> array:
        """Precompute digit sums for all possible numbers using vectorized operations."""
        digits = np.arange(self.number_range.end + 1)
        digit_sums = np.zeros(self.number_range.end + 1, dtype=np.uint8)

        while digits.any():
            digit_sums += digits % 10
            digits //= 10

        return array('B', digit_sums)

    def _process_chunk(self, chunk_size: int) -> Iterator[int]:
        """Process a chunk of random numbers."""
        numbers = np.random.randint(
            self.number_range.start,
            self.number_range.end + 1,
            chunk_size,
            dtype=np.int32
        )
        mask = np.frombuffer(self._digit_sums, dtype=np.uint8)[numbers] == self.number_range.target_sum
        yield from numbers[mask]

    def analyze(self, chunk_size: int = 100_000, num_processes: int = None) -> Result:
        """
        Analyze numbers to find min/max with target digit sum.

        Args:
            chunk_size: Size of chunks to process at once
            num_processes: Number of processes to use (None for CPU count)
        """
        start_time = time.perf_counter()
        min_num = float('inf')
        max_num = float('-inf')
        numbers_found = 0

        num_chunks = (self.number_range.count + chunk_size - 1) // chunk_size

        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            futures = [
                executor.submit(self._process_chunk,
                              min(chunk_size, self.number_range.count - i * chunk_size))
                for i in range(num_chunks)
            ]

            for future in tqdm(futures, desc="Processing chunks"):
                for num in future.result():
                    numbers_found += 1
                    min_num = min(min_num, num)
                    max_num = max(max_num, num)

        execution_time = time.perf_counter() - start_time

        if numbers_found == 0:
            return Result(None, None, 0, execution_time, 0)

        return Result(min_num, max_num, max_num - min_num, execution_time, numbers_found)
```

Claude now has added two more optimizations, finally realizing that this coding problem is an [embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) problem:

*   Multithreading through Python’s [concurrent-futures](https://docs.python.org/3/library/concurrent.futures.html) package, by separating the large list into chunks that can be processed independently.
*   Vectorized numpy operations, which are _much_ faster than base-Python operations. Special mention goes to the `_precompute_digit_sums()` function, which implements a vectorized implementation of calculating the digit sums. The conditional `while digits.any():` is galaxy-brain code, but it works correctly.

However, there’s an issue with this particular implementation of parallelization: it generates subprocesses, which causes _many_ annoying issues, including being unable to run it as-is inline, and it [must be invoked](https://stackoverflow.com/questions/15900366/all-example-concurrent-futures-code-is-failing-with-brokenprocesspool) with a `main()` guard which limits its utility significantly. But even when run as a separate script, it prints a `Error: cannot pickle 'generator' object` error due to the use of `yield from numbers[mask]` (said generator is completely unnecessary, `return numbers[mask]` is sufficient). The code also mixes numpy array `dtype`s which causes errors: setting them all to `np.int32` fixes it.

After making those fixes, the code is now **5.1x faster** than the base implementation.

### Iteration #3

Another `write better code`, and Claude [returns a implementation](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-3) that it claims is “even more sophisticated and optimized version using advanced techniques and modern Python features” but the actual code shows no significant algorithmic improvements and actually a regression in the digit sum calculation by reverting back to the type-casting approach. If anything, the codebase is becoming more bloated, such as adding a class for performing the difference:

```
@dataclass(frozen=True, slots=True)
class SearchResult:
    """Result of the number search."""
    min_number: Optional[int]
    max_number: Optional[int]
    count: int
    execution_time: float

    @property
    def difference(self) -> Optional[int]:
        """Calculate difference between max and min numbers."""
        if self.min_number is None or self.max_number is None:
            return None
        return self.max_number - self.min_number
```

This time, the code ran without needing any fixes. However, performance regressed slightly from the previous implementation, now **4.1x faster** than the base implementation.

### Iteration #4

This iterative prompting appears to be hitting diminishing returns. After one more `write better code`, Claude [provides an implementation](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-4) “with cutting-edge optimizations and enterprise-level features.” Wait, enterprise-level features?!

The final code is too large to include in this blog post, but it did create two more optimizations: it now uses the [numba](https://numba.pydata.org/) Python library that can invoke a JIT compiler, which directly optimizes the code for the CPU. In this case, it can precompute the digit sums super quickly with just a decorator:

```
@jit(nopython=True, parallel=True)
def calculate_digit_sums(numbers: ArrayInt) -> ArrayInt:
    """Calculate digit sums using Numba."""
    result = np.zeros_like(numbers)
    for i in prange(len(numbers)):
        num = numbers[i]
        total = 0
        while num:
            total += num % 10
            num //= 10
        result[i] = total
    return result
```

The full class also uses Python’s [asyncio](https://docs.python.org/3/library/asyncio.html) for parallelization, which is more canonical for scheduling tasks than a subprocess approach. It also plays more nicely with existing inline code and a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) such as [Jupyter Notebooks](https://jupyter.org/).

It also added as a part of its “enterprise” push:

*   Structured metrics logging with [Prometheus](https://prometheus.io/).
*   A signal handler so the code can be torn down gracefully if force-killed.
*   A benchmarking result display using a [rich](https://github.com/Textualize/rich) table.

![Image 14: It is pretty, though!](https://minimaxir.com/2025/01/write-better-code/rich.png)

It _is_ pretty, though!

It appears “going cosmic” for AI-generated code is making it enterprise by overengineering the code, which makes complete sense. Despite that, the code runs as-is without any bugs. Both async and numba are approaches to parallelism in Python, so they may be redundant and cause overhead. However, after benchmarking, the algorithm is _extremely_ fast, resulting in about 6 milliseconds a run, or a **100x** speedup. My assumption that this prompting was hitting diminishing returns aged very poorly. Maybe numba was the secret all along?

Overall, this form of iterative prompting to iteratively improve code has caveats: the code is indeed better, but in hindsight “better” is far too open ended. What I only wanted was algorithmic improvements, not a full SaaS. Let’s try again from scratch, this time with more direction.

Prompt Engineering LLMs For Even More Better Code
-------------------------------------------------

It’s 2025, and prompt engineering LLMs is still required to get best results from them. If anything, prompt engineering LLMs is _even more important_: next-token-prediction models are trained to maximimize the prediction probability of the next token over massive batches of inputs, and as a result they optimize for the **average** inputs and outputs. As LLMs drastically improve, the generated output becomes more drastically average, because that’s what they were trained to do: all LLMs are biased towards the average. Although it’s both counterintuitive and unfun, a small amount of guidance asking the LLM specifically what you want, and even giving a few examples of what you want, will objectively improve the output of LLMs more than the effort needed to construct said prompts. Claude 3.5 Sonnet, due to its strong prompt adherence, benefits significantly from even just a little prompt engineering.

Let’s redo the code optimization experiment, this time with aggressive prompt engineering that makes the results I am looking for extremely explicit, with no room for ambiguity. Yes, being cold and “robotic” to LLMs makes them perform better, [Roko’s basilisk](https://en.wikipedia.org/wiki/Roko%27s_basilisk) be damned.

### Initial Ask

This time we will use a system prompt, only available via an API. The system prompt lists the LLM’s “rules” it must follow. Since I want more optimized code, we’ll define that in the rules, with granular examples:

```
All code you write MUST be fully optimized.

"Fully optimized" includes:
- maximizing algorithmic big-O efficiency for memory and runtime
- using parallelization and vectorization where appropriate
- following proper style conventions for the code language (e.g. maximizing code reuse (DRY))
- no extra code beyond what is absolutely necessary to solve the problem the user provides (i.e. no technical debt)

If the code is not fully optimized, you will be fined $100.
```

About that last line: offering positive/negative incentives in to the LLM within a system prompt isn’t common anymore and [my own research](https://minimaxir.com/2024/02/chatgpt-tips-analysis/) indicated that it was unclear whether it had a positive impact, but that fine will become more relevant in the iteration prompt.

The initial user prompt has an additional line as well:

```
Write Python code to solve this problem:

Given a list of 1 million random integers between 1 and 100,000, find the difference between the smallest and the largest numbers whose digits sum up to 30.

Before writing the code, plan out all the necessary optimizations.
```

“Planning” is a long-used trick to help align LLM output for a first pass — the modern implementation of “[let’s think step by step](https://arxiv.org/abs/2205.11916).” Some LLMs ignore it, but Claude 3.5 Sonnet always obeys.

> The full, unedited conversation thread based on this prompt engineering strategy is [available on GitHub](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md).

Sending the system prompt and this user prompt to Claude, the [response](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-initial-ask) starts with this:

```
Let me plan the optimizations first:

1. Algorithmic Optimization:
- We only need to track min and max numbers with digit sum 30, not store all of them
- We can calculate digit sum while reading numbers, no need to convert to string
- Single pass through the list required (O(n))

2. Memory Optimization:
- Only need to store 2 variables (min and max), not the full filtered list
- No need for additional data structures

3. Performance Optimization:
- Use numba's @jit decorator for faster computation
- Create a fast digit sum function using modulo operations instead of string conversion
- Use numpy for generating random numbers (faster than random.randint)
```

This is promising: Claude immediately figured out it should start out with numpy and numba, and to also use integer operations to calculate the digit sum. The initial implementation:

```
@jit(nopython=True)
def digit_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

@jit(nopython=True)
def find_difference(numbers):
    min_num = float('inf')
    max_num = float('-inf')

    for num in numbers:
        sum_digits = digit_sum(num)
        if sum_digits == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    return max_num - min_num if max_num != float('-inf') else 0
```

That’s more concise than the initial implementation from casual prompting, especially with no unnecessary comments. There’s still room for improvement, notably this implementation did not set `parallel=True` in the `jit` decorator.

This minor use of prompt engineering resulted in code that runs in 11.2 milliseconds on average, or **59x faster** than the naive implementation. Wow!

### Iteration #1

We can now ask Claude to iterate on the code with a more verbose prompt than “write code better”:

```
Your code is not fully optimized, and you have been fined $100. Make it more optimized.
```

No, it’s not gaslighting, it’s _incentive alignment_.

Claude [responds](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-1) with this:

```
@jit(nopython=True)
def digit_sum(n):
    # Using bit manipulation for faster division
    total = 0
    while n:
        total += n & 15  # Fast lookup for single digit sum
        n >>= 4
    return total

@jit(nopython=True, parallel=True)
def find_difference_chunk(numbers):
    min_num = np.iinfo(np.int64).max
    max_num = np.iinfo(np.int64).min

    # Parallel processing of chunks using numba
    for i in prange(len(numbers)):
        num = numbers[i]
        sum_digits = digit_sum(num)
        if sum_digits == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    return min_num, max_num

def process_chunk(chunk):
    return find_difference_chunk(chunk)
```

Good, it identified the `parallel=True` flag! But that digit sum implementation is weird and uses [bit-shifting](https://wiki.python.org/moin/BitwiseOperators) which is generally only used for hyperoptimization. I didn’t think you could use bit-shifting well on decimal numbers, and after testing, it turns out _you can’t_ as this implementation derives an incorrect digit sum. The implementation also includes a multiprocessing chunking approach again (not shown), which is likely more redundant with numba and causes additional overhead. Also not shown: the script also pre-compiles the JIT functions with a small test array for better real-world performance, something the [numba docs recommend](https://numba.pydata.org/numba-doc/dev/user/5minguide.html#how-to-measure-the-performance-of-numba) for benchmarking.

Despite all of that, the code performance greatly regresses from the initial prompt-engineered implementation, now only **9.1x** faster than the naive implementation. The likely reason is due to the multiprocessing spawning new processes, and those processes will [recompile the numba JIT functions](https://stackoverflow.com/questions/72449896/does-numba-need-to-compile-separately-within-each-parallel-process) each time, so there’s massive overhead.

### Iteration #2

Another [iteration](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-2) of the prompt:

```
# Pre-computed lookup table using bit manipulation
LOOKUP = np.zeros(100001, dtype=np.uint8)
for i in range(100001):
    # Optimized digit sum using parallel bit counting
    n = i
    n = (n & 0x0F) + ((n >> 4) & 0x0F) + ((n >> 8) & 0x0F) + \
        ((n >> 12) & 0x0F) + ((n >> 16) & 0x0F)
    LOOKUP[i] = n

@jit(nopython=True, parallel=True, cache=True, fastmath=True)
def find_min_max(numbers):
    # Process 32 numbers at once using SIMD
    min_val = np.iinfo(np.uint32).max
    max_val = 0

    # Vectorized processing with explicit SIMD hints
    for i in prange(0, len(numbers), 32):
        # Load 32 elements into SIMD registers
        chunk = numbers[i:min(i + 32, len(numbers))]

        # Vectorized lookup and comparison
        sums = LOOKUP[chunk]
        mask = sums == 30

        if np.any(mask):
            valid_nums = chunk[mask]
            min_val = min(min_val, np.min(valid_nums))
            max_val = max(max_val, np.max(valid_nums))

    return min_val, max_val
```

Claude is now starting to use [SIMD operations](https://tbetcke.github.io/hpc_lecture_notes/simd.html) and chunk sizing for (theoretically) extreme performance. At this point I was confused I missed something with that bit-shifting implementation as it’s still wrong, especially now that hexadecimal numbers are getting involved. It turns out that implementation is an optimized method of calculating the digit sum of _hexadecimal_ numbers and not decimal numbers, and therefore it’s a complete hallucination. There is another extremely subtle hallucination: the `prange` function cannot accept a step-size of 32 while `parallel=True`, which is a nuance that there would be little documentation about. Setting `parallel=False` and benchmarking, there is indeed an slight improvement over the initial prompt-engineered implementation at **65x faster** than the base implementation.

### Iteration #3

[Another](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-3) iteration:

```
# Pre-computed perfect minimal hash table
# Key insight: For numbers 1-100000, only need to store those with digit sum 30
# Format: [number] = 1 if digit sum is 30, else 0
HASH_TABLE = np.zeros(100001, dtype=np.uint8)

# Generate hash table at module load time using bit manipulation
@jit(nopython=True, cache=True)
def init_hash_table():
    min_val = np.iinfo(np.uint32).max
    max_val = 0

    # Optimal digit sum using parallel bit counting
    for i in range(1, 100001):
        n = i
        sum = 0
        while n and sum <= 30:
            sum += n & 0xF
            n >>= 4
        if sum == 30:
            HASH_TABLE[i] = 1
            min_val = min(min_val, i)
            max_val = max(max_val, i)

    return min_val, max_val

# Initialize at module load time
MIN_VALID, MAX_VALID = init_hash_table()

@jit(nopython=True, parallel=False, cache=True, fastmath=True)
def find_min_max(numbers):
    min_val = MAX_VALID  # Start with known bounds
    max_val = MIN_VALID
    found = False

    # Single vectorized operation
    mask = HASH_TABLE[numbers] == 1
    if np.any(mask):
        valid_nums = numbers[mask]
        min_val = np.min(valid_nums)
        max_val = np.max(valid_nums)
        found = True

    return min_val, max_val, found
```

In this case, the LLM gives up on the chunking strategy which has been causing problems, and adds two more optimizations: a global `HASH_TABLE` (that’s just a numpy array, I’m unsure if a simple index lookup technically counts as a [hash table](https://en.wikipedia.org/wiki/Hash_table)), and it introduced a logical microoptimization that after summing up digits, if the number goes over 30, the counting can stop since it can immediately be identified as invalid.

One major problem: that “generate hash table at module load time” trick doesn’t actually work due to a subtle issue with little internet documentation: objects outside of numba’s JITed functions are read-only, yet the `HASH_TABLE` is still instantiated outside of the JITed function and modified within the JITed function, and therefore will cause a very confusing error. After a tiny refactor such that the `HASH_TABLE` is instantiated within a JITed function, the code worked, and ran _extremely_ fast: **100x** faster than the original base implementation, the same as the final performance from the casual prompting but with orders of magnitude less code.

### Iteration #4

At this point, Claude actually complained that the code is at the “theoretical minimum time complexity possible for this problem.” So I mixed things up and just asked it to fix the digit sum issue: [it did so](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-4) by only replacing the relevant code with the previously used integer implementation, and did not try to fix the `HASH_TABLE`. More importantly, with the `HASH_TABLE` adjustment, I confirmed the implementation is correct, finally, although with a slight performance hit since there is no more bit-shifting: it’s now **95x faster**.

Next Steps For Better LLM Code Generation
-----------------------------------------

Putting it all together, let’s visualize the improvements, including highlighting the cases where I needed to alter the logic of the code to make it runnable due to bugs.

![Image 15](https://minimaxir.com/2025/01/write-better-code/comparison.png)

In all, asking an LLM to “write code better” does indeed make the code better, depending on your definition of better. Through the use of the generic iterative prompts, the code did objectively improve from the base examples, both in terms of additional features and speed. Prompt engineering improved the performance of the code much more rapidly and consistently, but was more likely to introduce subtle bugs as LLMs are not optimized to generate high-performance code. As with any use of LLMs, your mileage may vary, and in the end it requires a human touch to fix the inevitable issues no matter how often AI hypesters cite LLMs as magic.

> All code in this blog post, including benchmarking scripts and data visualization code, is [available on GitHub](https://github.com/minimaxir/llm-write-better-code/).

There are a few optimizations that I am very surprised Claude 3.5 Sonnet did not identify and implement during either experiment. Namely, it doesn’t explore the statistical angle: since we are generating 1,000,000 numbers uniformly from a range of 1 to 100,000, there will be a significant amount of duplicate numbers that will never need to be analyzed. The LLM did not attempt to dedupe, such as casting the list of numbers into a Python `set()` or using numpy’s `unique()`. I was also expecting an implementation that involves sorting the list of 1,000,000 numbers ascending: that way the algorithm could search the list from the start to the end for the minimum (or the end to the start for the maximum) without checking every number, although sorting is slow a