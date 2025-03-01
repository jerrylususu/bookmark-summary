Title: Optimizing with Novel Calendrical Algorithms

URL Source: https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/

Published Time: 2025-02-03

Markdown Content:
[Background](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#background)
-----------------------------------------------------------------------------------------------

I have maintained the `time` crate for over five years now. In that time, tens of thousands of lines of code have been added, probably just as many removed, and countless more written but never committed. While benchmarks have been present for quite a while, I had never done one thing: truly optimize. Sure, some algorithms have been changed over the years, but I have never _created_ a nontrivial date-time algorithm from scratch. The speed was _good enough_, even if it was slower than comparable crates.

So why now? Well, I have a private board with 40+ tasks for `time` (in addition to the public issue tracker). Many of these are breaking changes, some have already been implemented, others don't neatly fit into the current API, and a few haven't haven been "accepted", meaning it may not be a good idea. There's one item that is quite literally at the bottom of the list: a general performance audit. It's at the bottom because it's not a priority and requires significant effort. It's not a priority because no one has complained. But I wanted to do something different, and this seemed like a good idea. It's my project, after all, so I can work on what I want.

[Starting point](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#starting-point)
-------------------------------------------------------------------------------------------------------

Looking through the code, there were some clear candidates for where I could start, based largely on my knowledge of where well-known algorithms were used, where I rolled my own without much thought beyond correctness, and methods that were likely used with disproportionate frequency. One method in particular stood out: `Date::to_calendar_date`.

For the purposes of this post, I am writing a method that accepts `year` and `ordinal` as parameters and returns a `(year, month, day)` tuple. The actual implementation is slightly different, but the differences are not relevant to the optimization.

[Status quo](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#status-quo)
-----------------------------------------------------------------------------------------------

The pre-existing implementation is about as simple as it gets. Using a lookup table, it finds the number of days in the year preceding the desired month, excluding January as it's the final case. Subtracting that number from the ordinal day gives us the day of the month, with the month itself being determined by reverse iteration.

```
const fn ordinal_date_to_calendar_date(year: i32, ordinal: u16) -> (i32, u8, u8) {
     The number of days up to and including the given month. Common years
     are first, followed by leap years.
    const CUMULATIVE_DAYS_IN_MONTH_COMMON_LEAP: [[u16; 11]; 2] = [
        [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
        [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335],
    ];

    let days = CUMULATIVE_DAYS_IN_MONTH_COMMON_LEAP[is_leap_year(year) as usize];

    let (month, day) = if ordinal > days[10] {
        (12, (ordinal - days[10]) as _)
    } else if ordinal > days[9] {
        (11, (ordinal - days[9]) as _)
    } else if ordinal > days[8] {
        (10, (ordinal - days[8]) as _)
    } else if ordinal > days[7] {
        (9, (ordinal - days[7]) as _)
    } else if ordinal > days[6] {
        (8, (ordinal - days[6]) as _)
    } else if ordinal > days[5] {
        (7, (ordinal - days[5]) as _)
    } else if ordinal > days[4] {
        (6, (ordinal - days[4]) as _)
    } else if ordinal > days[3] {
        (5, (ordinal - days[3]) as _)
    } else if ordinal > days[2] {
        (4, (ordinal - days[2]) as _)
    } else if ordinal > days[1] {
        (3, (ordinal - days[1]) as _)
    } else if ordinal > days[0] {
        (2, (ordinal - days[0]) as _)
    } else {
        (1, ordinal as _)
    };

    (year, month, day)
}
```

### [Binary search?](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#binary-search)

The first thing that came to mind was a binary search. The lookup table is sorted, so it is certainly possible. However, the table is small — only 11 elements after determining if it's a leap year — and the cost of a binary search is likely higher than the cost of a linear search. I have previously benchmarked this and quickly found that the linear search was faster. Manually unrolling the search improves performance some, but I wanted to keep investigating.

### [Loop?](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#loop)

Why not a loop instead of a series of `if` statements? I investigated this possibility at the same time as the binary search, as it would be more idiomatic in _any_ language. For whatever reason, Rust had difficulty optimizing this. Performance was worse than writing out the `if` statements manually.

[Designing a new algorithm](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#designing-a-new-algorithm)
-----------------------------------------------------------------------------------------------------------------------------

Despite maintaining `time` for years, I have never written a date-time algorithm from scratch. Doing so [is known to be a fun endeavor](https://youtu.be/-5wpm-gesOY). However, I recently ran across [a paper from Cassio Neri and Lorenz Schneider](https://onlinelibrary.wiley.com/doi/full/10.1002/spe.3172) introducing me to Euclidean affine functions and their potential applications in date-time calculations. Using methods similar to theirs, I decided to give it a shot.

I had a few guiding principles in mind when designing the new algorithm:

*   **Correctness**: It must be correct. I won't be performing a rigorous mathematical analysis, though, as I'm proving correctness by exhaustion (365 cases for common years and 366 for leap years).
*   **Performance**: It must be faster than the existing one. This is the entire point of optimizing it, after all.
*   **Integers only**: Floating point operations are significantly slower than integer operations, so I wanted to avoid them. I have previously adapted floating point algorithms to use integers, so I was confident that I could do so again.
*   **`const` compatible**: `Date::to_calendar_date` is currently a `const fn`. Breaking changes are unacceptable, so the new algorithm must be a `const fn` as well. Given Rust's limitations on what is permitted in `const` nowadays, this is largely a non-issue.

[Calculating the month](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#calculating-the-month)
---------------------------------------------------------------------------------------------------------------------

The first step was to determine the month. For this, I actually knew where to start. The Gregorian calendar (which most of the world uses) has two five-month "blocks": March through July and August through December, both of which contain 153 days. Neri and Schneider use a "computational calendar" that starts on March 1, but that is not what I was interested in. I wanted to calculate it from the _true_ ordinal, not a contrived one. Additionally, treating January and February as the start of a 153-day block would work flawlessly, as the first month in the block has 31 days (as January does).

Perhaps a visualization helps.

| Month | Days in month |
| --- | --- |
| January | 31 |
| February | 28/29 |
|   |  |
|   |  |
|   |  |

| Month | Days in month |
| --- | --- |
| March | 31 |
| April | 30 |
| May | 31 |
| June | 30 |
| July | 31 |

| Month | Days in month |
| --- | --- |
| August | 31 |
| September | 30 |
| October | 31 |
| November | 30 |
| December | 31 |

Programming the algorithm directly without figuring out the formula ahead of time would have been tricky, so I opted for a simpler solution: a spreadsheet. While not originating from a March-based ordinal, I believed that doing so for calculation purposes was in fact a good idea. The spreadsheet started off with three columns: the adjusted ordinal day (starting from March 1), the _actual_ month (entered manually) and the _calculated_ month (determined by a to-be-created algorithm). If the latter two columns were identical, the algorithm was necessarily correct.

Let's start by taking a view at the mapping of ordinal days from the true ordinal day.

To achieve this, it is necessary to determine the number of days in January and February combined. This is easy to do.

```
fn ordinal_date_to_calendar_date(year: i32, ordinal: u16) -> (i32, u8, u8) {
    let jan_feb_len = 59 + is_leap_year(year) as u16;

    todo!()
}
```

The `todo!()` macro is a great way to indicate that you plan to implement something later.

Now we can shift the ordinal day if necessary. We will need to disambiguate January and March as well as February and April later, but for the time being let's ignore those two months entirely.

```
let ordinal_adj = if ordinal <= jan_feb_len {
    0
} else {
    jan_feb_len
};

let ordinal = ordinal - ordinal_adj;
```

Our ordinal day now runs from 1 to 306, consisting solely of the two complete blocks of months. As the range contains 10 months, the average month length is exactly 30.6. So let's start with an approximation; divide the ordinal day by 30.6 and round down. This will give us our first estimate for what the month is, ranging from 0 to 9. We'll correct for that by adding the appropriate value (3 here).

```
=FLOOR(ordinal / 30.6, 1, 1) + 3
```

The extra parameters to `FLOOR` indicate that we want to round towards zero. For positive values it makes no difference, but they are included in case we somehow end up with a negative value in the spreadsheet. This behavior is important as it is the same as integer division when programming.

This gets us most of the way there! In fact, only six days are incorrect.

*   March 31
*   May 31
*   July 31
*   August 31
*   October 31
*   December 31

Interestingly, all the incorrect calculations are for months with 31 days. Thinking about it, this makes sense. The calculation tells us that it only has `FLOOR(30.6)` days (i.e. 30). We need to "build up" the 31st day. Perhaps if we force the first month to start with 31 days, the calculation will be correct. Because we're adding 30 days to the start, we need to adjust the result by two instead of three.

```
=FLOOR((ordinal + 30) / 30.6, 1, 1) + 2
```

Perfect! This correctly calculates all cases. Recall that we don't want to use floating point values, so we need to adapt this to integers. Rather than dividing by 30.6, multiply by 10 and divide by 306. Simple enough.

```
=FLOOR((ordinal + 30) * 10 / 306, 1, 1) + 2
```

Translating this into code is straightforward.

```
let month = (ordinal + 30) * 10 / 306 + 2;
```

Great; we can now calculate the month. But wait a minute, remember how I said we'd have to disambiguate January and March as well as February and April? Now is the time to do that. If the month is January or February, the value is already correct. For other months, we need to add the already-used adjustment. We can code this into the existing calculation.

```
let (month_adj, ordinal_adj) = if ordinal <= jan_feb_len {
    (0, 0)
} else {
    (2, jan_feb_len)
};

let ordinal = ordinal - ordinal_adj;
let month = (ordinal + 30) * 10 / 306 + month_adj;
```

At this point, we have calculated the month in an efficient manner.

[Calculating the day](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#calculating-the-day)
-----------------------------------------------------------------------------------------------------------------

Calculating the day of the month once we have the month is not terribly difficult. I added more columns to the spreadsheet: the known correct day, the calculated day, and whether the calculation was correct.

For this calculation, we will continue using the mapped ordinal day where March 1 is equivalent to January 1. Because of this, it's simplest to defer the month adjustment until later. The code in this section will be between the calculation of the month and the adjustment.

```
- let month = (ordinal + 30) * 10 / 306 + month_adj;
+ let month = (ordinal + 30) * 10 / 306;
+ let month = month + month_adj;
```

As we know the ordinal day, the only other things we need to know is how many days are in all previous months cumulatively. Once we know that, we can subtract that value from the ordinal day to get the day of the month.

But how do we calculate the cumulative number of days in previous months? In short, do the opposite calculation of how we calculated the month. Use the average length of the month — 30.6 — and multiply it by the month number less one (to account for the fact that the first month has no preceding days).

```
=FLOOR((month - 1) * 30.6, 1, 1)
```

It looks like some of the calculations are off by one day, as was the case when calculating the month. That's not too surprising given that we needed a correction before. Experimenting with small values quickly yields something that works.

```
=FLOOR((month + 3) * 30.6, 1, 1) - 122
```

Because we are treating January and February the same as March and April, there is no need to account for a leap day. However, we still need to make a minor alteration to avoid floating point numbers.

```
=FLOOR((month + 3) * 306 / 10, 1, 1) - 122
```

Great! This calculation works for all months. We can now translate this into code.

```
let days_in_preceding_months = (month + 3) * 306 / 10 - 122;
```

We now have all the information we need to perform the final calculation. All that's left to do is subtract the days in the preceding months from the ordinal day. As we've already eliminated the special casing for January and February, this just works™.

```
let day = ordinal - days_in_preceding_months;
```

Does it _really_ work? Yes! This algorithm was tested using a straightforward script to compare the results against the original implementation.

Test scriptThis script requires the nightly compiler as of publishing. It can be run with `cargo +nightly script.rs`. To use stable, you can add the dependency in a `Cargo.toml` file in a standard configuration.

```
#!/usr/bin/env cargo

---
package.edition = "2021"
[dependencies]
time = "=0.3.37" # pin to uses the previous algorithm which is known to be correct
---

use time::{util::is_leap_year, Date};

const fn ordinal_date_to_calendar_date(year: i32, ordinal: u16) -> (i32, u8, u8) {
    let jan_feb_len = 59 + is_leap_year(year) as u16;

    let (month_adj, ordinal_adj) = if ordinal <= jan_feb_len {
        (0, 0)
    } else {
        (2, jan_feb_len)
    };

    let ordinal = ordinal - ordinal_adj;
    let month = (ordinal + 30) * 10 / 306;
    let days_in_preceding_months = (month + 3) * 306 / 10 - 122;
    let day = ordinal - days_in_preceding_months;
    let month = month + month_adj;

    (year, month as _, day as _)
}

fn main() {
    for ordinal in 1..=366 {
        let calculated = ordinal_date_to_calendar_date(2024, ordinal);
        let correct = Date::from_ordinal_date(2024, ordinal)
            .unwrap()
            .to_calendar_date();
        let correct = (correct.0, correct.1 as u8, correct.2);
        assert_eq!(calculated, correct);
    }
    for ordinal in 1..=365 {
        let calculated = ordinal_date_to_calendar_date(2025, ordinal);
        let correct = Date::from_ordinal_date(2025, ordinal)
            .unwrap()
            .to_calendar_date();
        let correct = (correct.0, correct.1 as u8, correct.2);
        assert_eq!(calculated, correct);
    }
}
```

[Preliminary comparison](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#preliminary-comparison)
-----------------------------------------------------------------------------------------------------------------------

Let's look at the generated assembly for both the pre-existing and new algorithm. [`cargo asm`](https://crates.io/crates/cargo-show-asm) is used to generate this.

Pre-existing implementation

```
ordinal_date_to_calendar_date:
    imul eax, edi, -1030792151
    rorx eax, eax, 2
    cmp eax, 42949673
    mov eax, 15
    mov ecx, 3
    cmovb ecx, eax
    xor eax, eax
    test ecx, edi
    sete al
    lea rcx, [rax + 4*rax]
    lea rcx, [rax + 4*rcx]
    add rcx, rax
    lea rdx, [rip + .L__unnamed_5]
    movzx eax, word ptr [rdx + rcx + 20]
    cmp ax, si
    jae .LBB8_2
    movabs rcx, 51539607552
    jmp .LBB8_21
.LBB8_2:
    lea rax, [rdx + rcx]
    movzx eax, word ptr [rax + 18]
    cmp ax, si
    jae .LBB8_4
    movabs rcx, 47244640256
    jmp .LBB8_21
.LBB8_4:
    movzx eax, word ptr [rdx + rcx + 16]
    cmp ax, si
    jae .LBB8_6
    movabs rcx, 42949672960
    jmp .LBB8_21
.LBB8_6:
    movzx eax, word ptr [rdx + rcx + 14]
    cmp ax, si
    jae .LBB8_8
    movabs rcx, 38654705664
    jmp .LBB8_21
.LBB8_8:
    movzx eax, word ptr [rdx + rcx + 12]
    cmp ax, si
    jae .LBB8_10
    movabs rcx, 34359738368
    jmp .LBB8_21
.LBB8_10:
    movzx eax, word ptr [rdx + rcx + 10]
    cmp ax, si
    jae .LBB8_12
    movabs rcx, 30064771072
    jmp .LBB8_21
.LBB8_12:
    movzx eax, word ptr [rdx + rcx + 8]
    cmp ax, si
    jae .LBB8_14
    movabs rcx, 25769803776
    jmp .LBB8_21
.LBB8_14:
    movzx eax, word ptr [rdx + rcx + 6]
    cmp ax, si
    jae .LBB8_16
    movabs rcx, 21474836480
    jmp .LBB8_21
.LBB8_16:
    movzx eax, word ptr [rdx + rcx + 4]
    cmp ax, si
    jae .LBB8_18
    movabs rcx, 17179869184
    jmp .LBB8_21
.LBB8_18:
    movzx eax, word ptr [rdx + rcx + 2]
    cmp ax, si
    jae .LBB8_20
    movabs rcx, 12884901888
    jmp .LBB8_21
.LBB8_20:
    xor ecx, ecx
    xor edx, edx
    cmp si, 32
    setae dl
    mov eax, 31
    cmovb eax, ecx
    shl rdx, 32
    movabs rcx, 4294967296
    add rcx, rdx
.LBB8_21:
    sub esi, eax
    movzx edx, sil
    shl rdx, 40
    or rdx, rcx
    mov eax, edi
    or rax, rdx
    ret

```

Preliminary new implementation

```
ordinal_date_to_calendar_date:
    imul eax, edi, -1030792151
    add eax, 85899344
    rorx eax, eax, 2
    cmp eax, 42949673
    mov eax, 15
    mov ecx, 3
    cmovb ecx, eax
    and ecx, edi
    xor edx, edx
    cmp ecx, 1
    mov ecx, 0
    adc cx, 59
    xor eax, eax
    cmp cx, si
    setb al
    cmovae ecx, edx
    sub esi, ecx
    lea ecx, [rsi + rsi]
    lea ecx, [rcx + 4*rcx]
    add ecx, 300
    movzx ecx, cx
    imul ecx, ecx, 13707
    shr ecx, 22
    imul edx, ecx, 306
    add edx, 918
    movzx edx, dx
    imul edx, edx, 52429
    shr edx, 19
    sub esi, edx
    add esi, 122
    lea ecx, [rcx + 2*rax]
    movzx eax, sil
    shl rax, 40
    shl rcx, 32
    add rcx, rax
    mov eax, edi
    or rax, rcx
    ret
```
Assembly isn't the easiest to read, but it's clear from a glance that there are significantly fewer instructions. More impressive, in my opinion, is that the new implementation is _branchless_. This should help with performance, as branches are potentially expensive if mispredicted.

Rather than eyeballing it, what does MCA have to say?

Overall things look good! While there are some negatives, it's worth noting that MCA can be misleading. MCA assumes that all branches fall through, which is certainly not the case. It also is unable to account for cache locality, which are likely to be significant factors in the performance of the new implementation. One item of note is the throughput, which is significantly reduced and is also likely a significant factor.

[Further improvement](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#further-improvement)
-----------------------------------------------------------------------------------------------------------------

### [Month](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#month)

What's left to do? The algorithm is known to be correct and is likely faster than the pre-existing one. There are some further optimizations we can do, including some that are already performed by the compiler.

Let's start with the calculation of the month.

```
let month = (ordinal + 30) * 10 / 306;
```

The first thing that can be done is distributing the multiplication.

```
let month = (month * 10 + 300) / 306;
```

This is done by the compiler already, but there is one more trick we can do. Compilers _love_ division by powers of two because they are trivially replaced with a bitshift. While 306 is very much not a power of two, we can turn the division into one. The first power of two greater than 306 is 512. By multiplying the integers in the numerator by 512÷306 (≈1.67), we can turn the denominator into a power of two. This is in turn optimized into a bitshift.

```
let month = (month * 17 + 502) / 512;
```

This causes our script to fail. Let's try more powers of two. This is because with greater powers our approximation of the true ratio becomes more accurate.

Turns out that 8192 (i.e. 2¹³) is the magic number! Our final code for calculating the month is

```
let month = (ordinal * 268 + 8031) >> 13;
```

Hm. That didn't work. Rust is great, though, so it tells us why.

> attempt to multiply with overflow

Given the range of `ordinal` (1 to 306), the result of the multiplication is larger than a `u16` can hold, so we need to cast `ordinal` and its adjustment to a `u32`.

```
- let ordinal = ordinal - ordinal_adj;
+ let ordinal = ordinal as u32 - ordinal_adj as u32;
```

With this minor change, the code runs successfully.

### [Day](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#day)

Let's try the same with the day calculation.

```
let days_in_preceding_months = (month + 3) * 306 / 10 - 122;
```

First, we distribute the multiplication.

```
let days_in_preceding_months = (month * 306 + 918) / 10 - 122;
```

Since 122 is being added to the result of a division by 10, we can subtract 1220 from the numerator.

```
let days_in_preceding_months = (month * 306 - 302) / 10;
```

Now for the same trick utilizing powers of two, starting with 16.

By utilizing these new constants, we end up with the following code.

```
let days_in_preceding_months = (month * 3917 - 3866) >> 7;
```

### [One final change](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#one-final-change)

Remember how we had to zero-extend the adjusted ordinal? I tried moving around the cast in a few ways to see if it might optimize differently. And it did, just always as a slight regression. _While writing this post_, I considered one scenario I had not before: moving the cast to be the very first thing the function does. This allows eliminating subsequent casts and ensures that all operations are performed on `u32` values, no extending or truncating necessary.

```
+    let ordinal = ordinal as u32;

-    let jan_feb_len = 59 + is_leap_year(year) as u16;
+    let jan_feb_len = 59 + is_leap_year(year);

-    let ordinal = ordinal as u32 - ordinal_adj as u32;
+    let ordinal = ordinal - ordinal_adj;
```

The reason `ordinal` is not a `u32` from the start is because the field is semantically a `u16`.

[Final code](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#final-code)
-----------------------------------------------------------------------------------------------

After designing the new algorithm from the ground up, optimizing it along the way, making it work better for computers, and performing one final optimization, we have the following code.

```
const fn ordinal_date_to_calendar_date(year: i32, ordinal: u16) -> (i32, u8, u8) {
    let ordinal = ordinal as u32;
    let jan_feb_len = 59 + is_leap_year(year) as u32;

    let (month_adj, ordinal_adj) = if ordinal <= jan_feb_len {
        (0, 0)
    } else {
        (2, jan_feb_len)
    };

    let ordinal = ordinal - ordinal_adj;
    let month = (ordinal * 268 + 8031) >> 13;
    let days_in_preceding_months = (month * 3917 - 3866) >> 7;
    let day = ordinal - days_in_preceding_months;
    let month = month + month_adj;

    (year, month as _, day as _)
}
```

Does this code make any sense whatsoever on its own? No, not in the slightest. _But_ the end result is a solid piece of code that is faster than the pre-existing implementation, leverages optimizations that the compiler does not perform, and is branchless. When a new implementation is all upsides with only one downside (being less readable code), it would be foolish not to use it.

### [Comparison](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#comparison)

Looking at the assembly for the final code, we see many of the constants we introduced verbatim. This is a good sign that there isn't much more (if anything) that can be done for further optimizations within this style of algorithm. That is not to say that this code is perfect, but it is likely as good as it will get unless I have missed something obvious.

Assembly for the final code

```
ordinal_date_to_calendar_date:
    movzx eax, si
    imul ecx, edi, -1030792151
    rorx ecx, ecx, 2
    cmp ecx, 42949673
    mov ecx, 15
    mov edx, 3
    cmovb edx, ecx
    and edx, edi
    xor ecx, ecx
    cmp edx, 1
    mov edx, 0
    adc edx, 59
    xor esi, esi
    cmp edx, eax
    setb sil
    cmovae edx, ecx
    sub eax, edx
    imul ecx, eax, 268
    add ecx, 8031
    shr ecx, 13
    imul edx, ecx, 3917
    add edx, 28902
    shr edx, 7
    sub eax, edx
    lea ecx, [rcx + 2*rsi]
    movzx eax, al
    shl rax, 40
    movzx ecx, cl
    shl rcx, 32
    or rcx, rax
    mov eax, edi
    or rax, rcx
    ret
```
MCA analysis shows that the new implementation is _significantly_ better than the pre-existing code. The only "negatives" are the slight declines in micro-operations per cycle and instructions per cycle, but that is a non-issue given the significant decrease in total cycles.

### [Benchmarks](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#benchmarks)

For benchmarks, I used a representative sample of 24 values. To avoid giving the branch predictor any hints, the order was randomized. Using [`criterion`](https://crates.io/crates/criterion) and a tight loop around values, we get our results. Note that these results are for all 24 values, not any given one. It also includes the overhead of iteration, but that is almost certainly minimal.

Subtracting out the no-op iteration as overhead and dividing by the number of calculations performed, this is the time for a single calculation.

With these values, we are able to determine the 43.5% performance improvement from the pre-existing algorithm to the preliminary one, with an additional 24.7% improvement from the preliminary to final algorithm. Combined, this is a 57.5% decrease in time taken to perform the calculation.

[Truncated algorithms](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#truncated-algorithms)
-------------------------------------------------------------------------------------------------------------------

The final algorithm is not only faster when calculating the month and day together, but also when calculating them separately. This is because some calculations can be entirely omitted as unnecessary when calculating only one of the two. I won't go into detail on how this is done; it should be straightforward. The code, generated assembly, and benchmarks are provided.

### [Month-only](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#month-only)

```
const fn ordinal_date_to_month(year: i32, ordinal: u16) -> u8 {
    let ordinal = ordinal as u32;
    let jan_feb_len = 59 + is_leap_year(year) as u32;

    let (month_adj, ordinal_adj) = if ordinal <= jan_feb_len {
        (0, 0)
    } else {
        (2, jan_feb_len)
    };

    let ordinal = ordinal - ordinal_adj;
    (((ordinal * 268 + 8031) >> 13) + month_adj) as _
}
```

Generated assembly

```
ordinal_date_to_month:
    movzx eax, si
    imul ecx, edi, -1030792151
    add ecx, 85899344
    rorx ecx, ecx, 2
    cmp ecx, 42949673
    mov ecx, 15
    mov edx, 3
    cmovb edx, ecx
    and edx, edi
    xor ecx, ecx
    cmp edx, 1
    mov edx, 0
    adc edx, 59
    xor esi, esi
    cmp edx, eax
    setb sil
    cmovae edx, ecx
    sub eax, edx
    imul eax, eax, 268
    add eax, 8031
    shr eax, 13
    lea eax, [rax + 2*rsi]
    ret
```

### [Day-only](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#day-only)

```
const fn ordinal_date_to_day_of_month(year: i32, ordinal: u16) -> u8 {
    let ordinal = ordinal as u32;
    let jan_feb_len = 59 + is_leap_year(year) as u32;

    let ordinal_adj = if ordinal <= jan_feb_len {
        0
    } else {
        jan_feb_len
    };

    let ordinal = ordinal - ordinal_adj;
    let month = (ordinal * 268 + 8031) >> 13;
    let days_in_preceding_months = (month * 3917 - 3866) >> 7;
    (ordinal - days_in_preceding_months) as _
}
```

Generated assembly

```
ordinal_date_to_day_of_month:
    movzx eax, si
    imul ecx, edi, -1030792151
    add ecx, 85899344
    rorx ecx, ecx, 2
    cmp ecx, 42949673
    mov ecx, 15
    mov edx, 3
    cmovb edx, ecx
    and edx, edi
    xor ecx, ecx
    cmp edx, 1
    mov edx, 0
    adc edx, 59
    cmp edx, eax
    cmovae edx, ecx
    sub eax, edx
    imul ecx, eax, 268
    add ecx, 8031
    shr ecx, 13
    imul ecx, ecx, 3917
    add ecx, 28902
    shr ecx, 7
    sub eax, ecx
    ret
```

[Summary](https://jhpratt.dev/blog/optimizing-with-novel-calendrical-algorithms/#summary)
-----------------------------------------------------------------------------------------

Success! I was able to create performant, branchless, and `const`\-compatible algorithms for converting an ordinal date to a calendar date that is 57.5% faster than the previous implementation, the month-only algorithm 43.2% faster, and the day-only algorithm 48.1% faster. After exercising some creativity and applying some mathematical tricks, I was able to achieve something that I am more than happy with.

In the future, I hope to create more algorithms like this. While time-consuming and not straightforward, the end result was well worth it here. Algorithmic improvements may not be glamorous in release notes, but they cumulatively have a significant impact in the real world.
