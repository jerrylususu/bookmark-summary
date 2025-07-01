Title: So you want to serialize some DER? · Alex Gaynor

URL Source: https://alexgaynor.net/2025/jun/20/serialize-some-der/

Markdown Content:
Fri, Jun 20, 2025

(Editor’s Note: My day job is at Anthropic.)

This story starts where all good stories start, with ASN.1. ASN.1 is… I guess you’d call it a meta-serialization format? It’s a syntax for describing data abstractly (a notation, you might say), and then there’s a bunch of different actual encodings that you can use to turn data into bytes. There’s only one encoding I choose to acknowledge, which is DER (the Distinguished Encoding Representation, it’s got a monocle and tophat). DER and ASN.1 are often used as synonyms, even though they’re technically not – it’s fine. I maintain a Rust library for doing DER parsing and serialization, `rust-asn1` (yes, I’m contributing to the naming confusion).

DER is a type-length-value (TLV) binary format. Which means serialized data is all of the form `[type code][length][value]`, where `value` is always `length` bytes long. (Let’s Encrypt has a great [introduction to DER](https://letsencrypt.org/docs/a-warm-welcome-to-asn1-and-der/) if you’re interested.) The way `length` is encoded is itself variable length, if length is 8, its encoded as a single `[0x08]` byte. If length is 100, its encoded two bytes `[0x81, 0x64]`. If you’re serializing some data, and you’re just filling in your buffer from left to right, this gives you an interesting challenge: either you need to know how long each `value` is going to be when you start serializing, or you have to do some tricks.

When I started this adventure, `rust-asn1` did tricks. Specifically, what it did is that when you went to serialize some value into a TLV, it reserved 1 byte of space for the length in the buffer, and then asked the value to write itself to the buffer. Then it compared the length of the buffer before and after, to see how long the value was. If the `length` fit in the 1 byte we reserved, we’d write it and be done. If not, we expand our buffer, copy the data to make space for the `length`, and then write the `length` in. The basic theory is that most TLVs are short, so this is fine in practice. If you’ve got a lot of larger TLVs, this will incur a whole bunch of extra copying, which is too bad.

So I went to do the obvious optimization: allow the value we’re encoding to tell `rust-asn1` how long its value will be, so that `rust-asn1` can just write out the length correctly the first time. Not rocket science. I wrote up a [benchmark](https://github.com/alex/rust-asn1/commit/bef978a6492413d17be32c95cc6d4f3443949813), then a [PR](https://github.com/alex/rust-asn1/pull/547) (`claude-code` did the first draft of both), and admired my handiwork.

And then I started ruminating on how we pre-compute a value’s length. For lots of types its trivial, for an `OCTET STRING` its just the length of the data in bytes, for a `BOOLEAN` its always 1. What about `INTEGER`? Those are a variable length encoding. (It’s not the same encoding as we use for `length`, that would be too easy.) Here’s what the original implementation (which predated this optimization work) looked like, its inside of a macro which generates implementations for each integer width, hence the ugliness:

```
let mut num_bytes = 1;
let mut v: $t = *self;
#[allow(unused_comparisons)]
while v > 127 || ($signed && v < (-128i64) as $t) {
    num_bytes += 1;
    v = v.checked_shr(8).unwrap_or(0);
}

num_bytes
```

Something about this implementation bothered me. There was an intuitive wastefulness to need to loop over the bytes to know how long the integer was. Surely we could do better? I was feeling a bit lazy so I [asked Claude](https://claude.ai/share/ab67c7a5-eb62-420b-87c6-6b4b2c0c7b5a) for improvements (I also looked at the implementation in another library). After some back and forth with Claude, I landed on:

```
let num_bytes = if *self == 0 {
    1
} else {
    #[allow(unused_comparisons)]
    let bits_needed = if $signed && *self < 0 {
        // For negative numbers, count significant bits
        // including sign bit
        <$t>::BITS - self.leading_ones() + 1
    } else {
        // For positive numbers, count all significant bits
        <$t>::BITS - self.leading_zeros()
    };

    let bytes_needed = bits_needed.div_ceil(8);

    // Check if we need an extra byte for ASN.1 encoding
    let shift = (bytes_needed - 1) * 8;
    let most_significant_byte = (*self >> shift) as u8;
    #[allow(unused_comparisons)]
    let needs_extra_byte = if $signed && *self < 0 {
        false
    } else {
        most_significant_byte >= 0x80
    };

    bytes_needed + needs_extra_byte as u32
};
```

It’s more code (by a fair bit) and it’s way subtler, but it has the benefit of being branch-free for unsigned integers and being composed exclusively of simple operations. It’s not clear that it’s faster than the old implementation. In a fit of curiosity, I decided to see what the assembly generated for the `bits_needed.div_ceil(8)` line was. And the answer is that if you move just that expression into its own function, you get:

```
mov     eax, edi
shr     eax, 3
and     edi, 7
cmp     edi, 1
sbb     eax, -1
ret
```

If you expand it out to `(u32::BITS - v.leading_zeros()).div_ceil(8)` you get:

```
mov     ecx, 63
bsr     ecx, edi
xor     ecx, -32
add     ecx, 33
mov     eax, ecx
shr     eax, 3
and     ecx, 7
cmp     ecx, 1
sbb     eax, -1
ret
```

In the same way the loop felt ugly, this assembly feels ugly. There are just too many instructions, probably twice as many as I’d have, off the cuff, guessed were required.

So I [asked Claude](https://claude.ai/share/d998511d-45ee-4132-bee4-fe7f70350a67) if it was possible to do better. I want to stress here, that I was not really expecting this to work. I’ve had a lot of successes, and some failures, using Claude to help me write code. But using Claude as some sort of bizarro optimizing compiler? There were so many ways it could screw it up: it could pessimize the code, it could change the behavior in edge cases, it could just spit out gibberish.

So I was impressed when Claude gave me something that looked ok. But looking ok is easy, was it _actually_ ok? Fortunately, it’s possible to know things! [Alive2](https://alive2.llvm.org/ce/) is a formal verification tool that takes two functions in LLVM IR and confirms that it is valid to optimize the first to the second. And Alive2 gave us the thumbs up. Not only was the new LLVM IR self-evidently more optimal, but it was correct.

So I filed an [LLVM bug](https://github.com/llvm/llvm-project/issues/142497) explaining the missed optimization with the original source, the current generated code, the more optimal code, and the Alive2 proof that this optimization was valid.

If the story ended here, I’d have honestly been impressed. The optimization here wasn’t really rocket science, but it also wasn’t so trivial that LLVM already performed it. Obviously the next move is to see if I can send a PR to LLVM, but it’s been years since I was doing compiler development or was familiar with the LLVM internals and I wasn’t really prepared to invest the time and energy necessary to get back up to speed. But as a friend pointed out… what about Claude?

At this point my instinct was, “Claude is great, but I’m not sure if I’ll be able to effectively code review any changes it proposes, and I’m _not_ going to be the asshole who submits an untested and unreviewed PR that wastes a bunch of maintainer time”. But excitement got the better of me, and I asked `claude-code` to see if it could implement the necessary optimization, based on nothing more than the test cases. Here’s the exact prompt I used:

```
I'd like you to implement a new optimization in LLVM that fixes a
place where there's currently sub-optimal code generation.

I have the following IR, which the LLVM optimizer emits:

```
define noundef range(i32 0, 6) i32 @src(i32 noundef %v) unnamed_addr #0 {
start:
  %0 = tail call range(i32 0, 33) i32 @llvm.ctlz.i32(i32 %v, i1 false)
  %_2 = sub nuw nsw i32 32, %0
  %_41 = lshr i32 %_2, 3
  %_5 = and i32 %_2, 7
  %_6.not = icmp ne i32 %_5, 0
  %1 = zext i1 %_6.not to i32
  %_0.sroa.0.0 = add nuw nsw i32 %_41, %1
  ret i32 %_0.sroa.0.0
}
```

However, it can be optimized to the following, better, IR:

```
define noundef range(i32 0, 5) i32 @tgt(i32 noundef %v) unnamed_addr #0 {
start:
  %0 = tail call i32 @llvm.ctlz.i32(i32 %v, i1 false)
  %1 = sub nuw nsw i32 32, %0
  %2 = add nuw nsw i32 %1, 7
  %3 = lshr i32 %2, 3
  ret i32 %3
}
```

I would like you to a) add a test for this optimization to LLVM's
existing test suite for compiler optimizations, and then b) implement
the necessary optimization in LLVM.

You'll need to think hard and make a plan to do this.

You can re-build and run the tests by running the following command
`ninja -C build check-llvm`. Do not try to run the tests or build any
other way. If other tests fail after you make changes, review closely
to see if the tests themselves should be updated for the new
optimization, or if they indicate a bug in the code.
```

And then it went to work. My contributions were: a) reviewing the initial test cases it wrote and telling it that a few of them weren’t actually correct because of integer overflows, b) pointing out a few times when it was trying to run a test without having rebuilt the code, c) not actually sending the pull request until I had reviewed the change and was confident in it. Everything else `claude-code` did itself, including implementing changes requested by code reviewers. Thanks also go to the LLVM maintainers for their timely and helpful code reviews.

You can judge the [final product](https://github.com/llvm/llvm-project/pull/142869) for yourself. But from my perspective: holy shit, it fucking worked?

Lessons learned
---------------

What are the takeaways here? First, obviously, the universe revolves around ASN.1 and optimizing compilers exist to serve it.

More seriously, I gave these problems to Claude, not expecting meaningful results, and it absolutely blew my expectations out of the water. I am incredibly leery about [over-generalizing](https://alexgaynor.net/2025/mar/05/generality/) how to understand the capacity of the models, but at a minimum it seems safe to conclude that sometimes you should just let the model have a shot at a problem and you may be surprised – particularly when the problem has very clear success criteria. This only works if you have the capacity to review what it produces, of course. (And by “of course”, I mean probably many people will ignore this, even though it’s essential to get meaningful, consistent, long-term value out of these systems.)

The pairing of an LLM with a formal verification tool like Alive2 was incredibly powerful. Indeed, you can imagine giving an LLM Alive2 as a tool the LLM can invoke itself and letting an agent hammer away at finding the most optimal code it can that verifies and then using its findings as the basis to implement new compiler optimizations.

Another clear takeaway is that there’s always money in the banana stand that is missing compiler optimizations. If you go looking, it’s quite likely you can find something sub-optimal that a compiler does, even in 2025. And it’s, apparently, easier to produce a working PR to implement the optimization than I would have guessed.
