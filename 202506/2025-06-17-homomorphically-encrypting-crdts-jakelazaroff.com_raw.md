Title: Homomorphically Encrypting CRDTs | jakelazaroff.com

URL Source: https://jakelazaroff.com/words/homomorphically-encrypted-crdts/

Markdown Content:
Here’s a problem with local-first software.

You want to work on a document together with a friend who lives far away from you. That sounds like local-first’s bread and butter: store the document as a CRDT, then use some sort of sync server to merge updates and relay them between you and your friend.

But there’s a catch: the contents of that document are secret. So secret, in fact, that _you don’t even want the app developer to know what they are_.

One way to solve this is end-to-end encryption. You and your friend agree on a secret key, known only to each other. You each use that key to encrypt your changes before sending them, decrypt them upon receipt, and no one in the middle is able to listen in. Because the document is a CRDT, you can each still get the latest document without the sync server merging the updates.

That is indeed a solution, and modern browser APIs make it fairly simple to implement a basic version of it. [Excalidraw’s writeup of their implementation](https://plus.excalidraw.com/blog/end-to-end-encryption) is only about 750 words — including code samples![1](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-e2ee)

Unfortunately, we’ve introduced a new problem.

You and your friend live far away from each other, so you tend to work while they’re sleeping and vice versa. That was fine when the sync server could merge your changes and send you the latest document when you opened it.

Now, however, the server can no longer understand the changes you send. If you want to see your friend’s latest changes, you’ll need to both be online at the same time.

Enter **homomorphic encryption**: a special form of encryption that allows a computer to _run programs on encrypted data without decrypting it_. Using a homomorphically encrypted CRDT, a sync server could merge your friend’s and your changes into one document without ever knowing what the document contains.[2](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-otherways)

In this article, we’ll explore how homomorphic encryption works and build a homomorphically encrypted last write wins register CRDT. We’ll also learn about some fundamental limitations of homomorphic encryption, and how they affect local-first software specifically.

I try to assume as little knowledge as possible about both encryption and CRDTs. If you want to brush up before continuing on, my [Interactive Intro to CRDTs](https://jakelazaroff.com/words/an-interactive-intro-to-crdts/) and Jeremy Kun’s [A High-Level Technical Overview of Fully Homomorphic Encryption](https://www.jeremykun.com/2024/05/04/fhe-overview/) are good places to start.

(Obligatory disclaimer: I am not a cryptographer! While I’m reasonably confident that my code and advice here is generally sound, cryptography is a field in which subtle bugs and exploits can look fine to the untrained eye. Before using anything here in an environment you’d describe with the word “production”, consult someone who works on this professionally.)

Homomorphic Hello World
-----------------------

First, let’s look at a small code sample that uses homomorphic encryption.

Writing the encryption code itself from scratch would take much more code than can fit in this article. Instead, we’ll use [THFE-rs](https://github.com/zama-ai/tfhe-rs), a homomorphic encryption library written in Rust.

The flow goes something like this:

1.   A client generates a key pair consisting of a client key and a server key.
2.   The client encrypts their data using the client key and sends both the encrypted data and server key to the server.
3.   The server uses the server key to perform some computation on the encrypted data and sends the result back to the client.
4.   The client decrypts the result with the client key.

Here’s what this looks like in code. We’ll take two numbers — `clear_a` and `clear_b` — and add them together. Rather than actually sending anything over a network, we’ll just use a function called `server_compute` to play the part of the server.

```
use tfhe::prelude::*;
use tfhe::{generate_keys, set_server_key, ConfigBuilder, FheUint32, ServerKey};

fn main() {
    let config = ConfigBuilder::default().build();

    // generate client and server keys
    let (client_key, server_key) = generate_keys(config);

    // generate plaintext
    let clear_a: u32 = 27;
    let clear_b: u32 = 128;

    // encrypt plaintext and "send to server"
    let result = server_compute(
        server_key,
        FheUint32::encrypt(clear_a, &client_key),
        FheUint32::encrypt(clear_b, &client_key),
    );

    // decrypt the result
    let decrypted_result: u32 = result.decrypt(&client_key);

    // assert that the result is what we expect
    assert_eq!(decrypted_result, clear_a + clear_b);
}

fn server_compute(key: ServerKey, cipher_a: FheUint32, cipher_b: FheUint32) -> FheUint32 {
    set_server_key(key);
    return cipher_a + cipher_b;
}
```

Get the keys, encrypt two numbers, add their ciphertexts together, decrypt the result. Not too bad, right?

The simplicity is deceptive! Rust supports operator overloading, so when we run `cipher_a + cipher_b` and both of the operands are `FheUint32`, what’s _really_ happening is that TFHE-rs runs a bunch of cryptography code.

Before we build our homomorphically encrypted CRDT, let’s peek at what TFHE-rs is doing under the hood.

Under the Hood
--------------

To start, what does it even mean to “run programs on encrypted data”?

In short, it means you can use encrypted data in certain math operations, and when you decrypt the data you get the result you would have gotten if you had performed the same operations with the plaintext data. That requires an encryption scheme in which at least one of the following is true (I’ll use the notation `E(a)` to indicate the encrypted version of the plaintext `a`):

*   `E(a) + E(b) = E(a + b)`: adding the encrypted values of the plaintext numbers `a` and `b` results in the encrypted sum of the plaintext sum `a + b`.
*   `E(a) × E(b) = E(a × b)`: multiplying the encrypted values of the plaintext numbers `a` and `b` results in the encrypted product of the plaintext product `a × b`.

What this means is that **if you add or multiply two homomorphically encrypted values, then decrypt them, _you get the respective sum or product of the original plaintext values_**.

Here’s an extremely simple example that you should absolutely never use anywhere. First, let’s pick a number as a key. We “encrypt” numbers by multiplying them by the key, and “decrypt” numbers by dividing them.

Let’s say our key is 7 and our “plaintext” numbers are 5 and 6. We can multiply each number by our key 6 to get “encrypted” numbers of 35 and 42. Even if someone has access to our encrypted numbers, they can’t figure out what our original plaintext numbers were without the key.

What they _can_ do is add the encrypted numbers together. If they give us back the sum, 77, we can divide it by our key 7 to get 11 — _the same result we’d get by directly adding our original numbers_. Try it out by changing the numbers in the playground below:

Because it satisfies the first criterion — `E(a) + E(b) = E(a + b)` — we can say that our toy encryption scheme is homomorphic over addition. Encryption that supports only one operation is called _partially homomorphic encryption_. All in all, there are four different levels:

*   **Partially homomorphic encryption** allows only one of the two operations: _either_ addition _or_ multiplication, but not both.
*   **Somewhat homomorphic encryption** and **leveled homomorphic encryption** allow both operations, but limit the amount of times they can be used.
*   **Fully homomorphic encryption** allows an unlimited amount of both operations.

Partially homomorphic encryption is relatively easy to implement, but has limited uses. The word “relatively” is doing some heavy lifting here — you or I probably couldn’t come up with a partially homomorphic encryption scheme — but it’s simple enough that there are algorithms such as RSA that are accidentally homomorphic over one operation.

Supporting _more than one_ operation is significantly more useful, but each calculation adds “noise” to the result. Too much noise makes it impossible to decrypt. There are two broad strategies for reducing noise: limiting the number or “depth” of operations (_somewhat_ and _leveled_ homomorphic encryption), and “bootstrapping”, which reduces the level of noise mid-computation (_fully_ homomorphic encryption).

Why does it matter whether we can perform _both_ addition and multiplication?

When we talk about doing math on encrypted data, we’re really talking about the underlying bits: the 1s and 0s that make it up. To add and multiply the bits, we use the logical operations “exclusive or” (XOR) and “binary and” (AND), respectively.

Click on the switches in the playground below to toggle between 1 and 0. You can see that the AND output is the product of its two inputs, and the XOR output is roughly the sum of its two inputs.[3](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-addition)

This is called a _Boolean circuit_ — essentially, a function that takes 1s and 0s as input and returns 1s and 0s as output. In this context, the logical operations are called _logic gates_.

We can create new logic gates by combining ones we have. Here’s how to create “inclusive or” (OR) and inverter (NOT) operations using only XOR and AND.

Once we’ve built a gate, we can then use it to build _yet other_ gates. Here’s how to make an “exclusive nor” (XNOR) using XOR and our newly-constructed NOT gate:

It turns out that combining just XOR and AND like this is enough to perform _any computation_! All other logical operations can be created by combining only XOR and AND, which means that adding and multiplying the encrypted data is sufficient to simulate arbitrary Boolean logic.

Here’s a circuit that implements the “greater than” operator on two-bit numbers (between 0 and 3). Using only AND, XOR and the other gates we’ve built with them, it returns 1 if the first number is greater than the second, and 0 otherwise.

Type in the square boxes at the top to enter the input numbers. The two rounded boxes below each square input box are the _binary representation_ of that number.

Don’t forget this circuit — it’ll come in handy later!

In these examples, we’ve been looking at circuits that use plaintext 1s and 0s as their inputs and outputs. With homomorphic encryption, the circuits operate on _encrypted data_. Performing an AND on two encrypted bits returns another encrypted bit — and we can’t find out what it is unless we have the key.

So that’s how homomorphic encryption works in a nutshell. You express your program as a Boolean circuit, and then simulate the circuit using the encrypted data as input. The output of the circuit will be the encrypted result, which the client can then decrypt.

Crucially, _none of this reveals any sort of relationship between the plaintext values_. For example, even if `E(a) + E(b)` were positive, `E(a + b)` might be negative. Adding and multiplying ciphertext corresponds to the same operations on the underlying plaintext, but there’s no correlation between any of the ciphertext results and the underlying plaintext results — you need to decrypt the result to figure out what happened.

A Fully Homomorphic CRDT
------------------------

Now that we have a high level understanding of homomorphic encryption, let’s build a homomorphically-encrypted last write wins register.

A last write wins register holds a single value and two additional bits of metadata: a “clock” that gets incremented by one whenever the value is set, and an ID indicating the peer who last wrote to it. Like all CRDTs, it also has a merge function that describes how it should be combined with another of the same type.

The last write wins register merge algorithm works like this:

*   If the received clock is less than the local clock, the register doesn’t change its state.
*   If the received clock is greater than the local clock, the register overwrites its local value with the received value. It also stores the received clock and peer ID.
*   Ties are broken by comparing the local peer ID to the peer ID in the received state.

Here’s a playground in which you can see how this algorithm works:

Try playing around with the latency and the network toggle. See how updates are accepted only if the sending peer’s clock is higher than the receiving peer’s clock. If the clocks are tied, the update from the right peer will win out, since the peer ID `bob` is lexicographically greater than `alice`.

Okay, let’s look at some code. First, here’s what an _unencrypted_ last write wins register might look like in Rust:

```
const DATA_SIZE: usize = 16;

pub struct Register {
    pub peer: u64,
    pub clock: u64,
    pub value: [u8; DATA_SIZE],
}

impl Register {
    pub fn new(peer: u64) -> Register {
        Register {
            peer,
            clock: 0,
            value: [0; DATA_SIZE],
        }
    }

    pub fn set(&mut self, peer: u64, value: [u8; DATA_SIZE]) {
        self.peer = peer;
        self.clock += 1;
        self.value = value;
    }

    pub fn set_string(&mut self, peer: u64, value: &str) {
        let bytes = value.as_bytes();
        let len = bytes.len().min(DATA_SIZE);

        let mut data = [0; DATA_SIZE];
        data[..len].copy_from_slice(&bytes[..len]);

        self.set(id, data);
    }

    pub fn merge(&mut self, other: &Register) {
        if self.clock > other.clock {
            return;
        };

        if self.clock == other.clock && self.peer > other.peer {
            return;
        }

        self.peer = other.peer;
        self.clock = other.clock;
        self.value = other.value;
    }
}
```

It has a peer ID, a clock and a value. To merge with another register, it just takes the peer ID, clock and value from the register with the higher clock. In case of a tie, it uses the peer ID as a tiebreaker.

Because Rust is a low-level language, we need separate functions to convert types such as strings into the raw bytes to store as the value. We also store the value in an array with a statically-known size — although as we’ll see, that’s less of a Rust limitation than it is a fundamental constraint of homomorphic encryption.

Here’s the skeleton of an `EncryptedRegister` struct:

```
use core::array;
use tfhe::prelude::*;
use tfhe::{ClientKey, FheUint64, FheUint8};

use crate::Register;

const DATA_SIZE: usize = 16;

pub struct EncryptedRegister {
    peer: FheUint64,
    clock: FheUint64,
    value: [FheUint8; DATA_SIZE],
}

impl EncryptedRegister {
    pub fn encrypt(clear: &Register, key: &ClientKey) -> EncryptedRegister {
        EncryptedRegister {
            peer: FheUint64::encrypt(clear.peer, key),
            clock: FheUint64::encrypt(clear.clock, key),
            value: array::from_fn(|i| FheUint8::encrypt(clear.value[i], key)),
        }
    }

    pub fn decrypt(&self, key: &ClientKey) -> Register {
        Register {
            peer: FheUint64::decrypt(&self.peer, key),
            clock: FheUint64::decrypt(&self.clock, key),
            value: array::from_fn(|i| FheUint8::decrypt(&self.value[i], key)),
        }
    }

    pub fn merge(&mut self, other: EncryptedRegister) {
        // ...
    }
}
```

Pretty similar to the unencrypted `Register` struct! `FheUint64` has replaced `u64`, and `value` is now an array of `FheUint8` rather than `u8`. These are TFHE-rs types that encrypt the corresponding Rust types. But other than that, the struct is the same.

The implementation has two new methods:

*   `encrypt`, which takes a normal `Register` and a client key, encrypts all the fields and returns an `EncryptedRegister`.
*   `decrypt`, which takes a client key, decrypts all the fields and returns a normal `Register`.

We’ve also omitted the `set` and `set_string` methods. Since `EncryptedRegister` runs on the server, the value will never be set manually. The only thing it needs to do is merge an incoming register with the register it has in memory.

Okay, so what does the `merge` method look like?

As we saw before, TFHE-rs overloads operators like `+` to make working with encrypted values more convenient. For operators that don’t support overloading such as `<`, TFHE-rs has methods like `gt`.

Given that, you might think we could write the `merge` method like this:

```
impl EncryptedRegister {
  // ...

  pub fn merge(&mut self, other: EncryptedRegister) {
    if self.clock.gt(&other.clock) {
      return;
    }

    if self.clock.eq(&other.clock) && self.id.gt(&other.id) {
      return;
    }

    self.id = other.id;
    self.clock = other.clock;
    self.value = other.value;
  }
}
```

This will _definitely not work_!

Remember that we can’t retrieve any information by operating on the encrypted data — _including information about the results of intermediate steps_.

To more clearly show the problem with this strategy, we can add some logging:

```
impl EncryptedRegister {
  // ...

  pub fn merge(&mut self, other: EncryptedRegister) {
    if self.clock.gt(&other.clock) {
      println!("local clock is greater than other clock!");
      return;
    }

    if self.clock.eq(&other.clock) && self.peer.gt(&other.peer) {
      println!("clocks are equal but local peer is greater than other peer!");
      return;
    }

    println!("overwriting local data with remote data!");
    self.peer = other.peer;
    self.clock = other.clock;
    self.value = other.value;
  }
}
```

Although we still couldn’t decrypt the encrypted data, this (fake) implementation would reveal the result of the merge! We’d know which branches our code took, and therefore learn which decrypted clock was higher and which encrypted data was written to the register.

Instead, our merge function must _eagerly_ evaluate all branches in our code. It also means that all loops must run for a statically-known number of iterations. More generally, **our code must always execute as though operating on the worst case input**, because altering behavior based on the input would leak information about it.

Here’s the _real_ code for our merge function:

```
pub fn merge(&mut self, other: &EncryptedRegister) {
    let higher_clock = self.clock.gt(&other.clock);

    let equal_clock = self.clock.eq(&other.clock);
    let higher_peer = self.peer.gt(&other.peer);

    let keep_self = higher_clock | (equal_clock & higher_peer);

    self.peer = keep_self.select(&self.peer, &other.peer);
    self.clock = keep_self.select(&self.clock, &other.clock);
    self.value = array::from_fn(|i| keep_self.select(&self.value[i], &other.value[i]));
  }
```

Superficially, it looks fairly similar, but there are a couple of important differences. Let’s take it line by line.

First, we determine whether the local clock is higher than the other clock:

```
let higher_clock = self.clock.gt(&other.clock);
```

If we think back to the logic gates, we can imagine what’s going on under the hood here, right? We built this exact circuit! Ours only operated on two-bit numbers, but the idea was the same: accept two numbers and return a 0 or 1 indicating whether the first number is higher than the second.

(In our circuit, the result was a _plaintext_ 0 or 1 — but remember, homomorphic encryption operates with _encrypted_ values! The `gt` method actually returns an `FheBool`: an _encrypted bool_ which indicates whether the local clock is higher than the other one.)

If we had the client key, we could decrypt that variable and find out its true value. We can’t do that, but we can still _combine it with other encrypted values_ to write our merge algorithm.

Here are the conditions to break a tie between the clocks:

```
let equal_clock = self.clock.eq(&other.clock);
let higher_peer = self.peer.gt(&other.peer);
```

Two more `FheBool`s indicating whether the clocks are equal and if the local peer ID is higher.

Next, we combine them:

```
let keep_self = higher_clock | (equal_clock & higher_peer);
```

This combines all those `FheBool`s to determine whether to keep the local data or overwrite it with the merged data.[4](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-astute)

Those `|` and `&` operators are bitwise AND and bitwise OR, which work exactly like the AND and OR logic gates we made earlier. They’re similar to the logical AND and OR we’re used to — `&&` and `||`, but with one big difference: bitwise operators are _eager_. Whereas logical AND and OR might skip the second expression depending on the first, bitwise operators will _always_ evaluate both sides.

Now that we’ve determined the register values to keep — even if we can’t tell which ones — we need to write the data to the register. Here’s the secret sauce:

```
self.peer = keep_self.select(&self.peer, &other.peer);
self.clock = keep_self.select(&self.clock, &other.clock);
self.value = array::from_fn(|i| keep_self.select(&self.value[i], &other.value[i]));
```

Rather than `if` or `match` expressions, we use `FheBool`’s `select` method. It returns the first argument if the underlying `FheBool` value is `true`, or the second argument if the underlying value is `false`.

This is important: _the return value is different from both arguments_. While decrypting the return value would reveal the same plaintext as one of the arguments, in ciphertext all three are distinct. This means that we can’t tell which values we’ve set on the register by the end of the merge.

When the merge is done, every piece of ciphertext has changed — the peer ID, the clock and the register value. The plaintext values might have updated (or might not have!) but there’s no way to tell by looking at the ciphertext.

Problem solved, right? We can now have the server merge our CRDT without knowing what it contains? Weeeellllllll…

Fundamental Limitations
-----------------------

Homomorphic encryption has constraints that sharply limit its effectiveness with regard to local-first software.

For starters: encryption keys. In both the simple adding example and the last-write wins register, we generated a key that would be passed to the server. That only needs to happen once, but the difference between the size of our key and the size of our data can be surprising.

Our register took up only 32 bytes of data — 8 bytes each for the peer and clock, and 16 bytes for the value. Meanwhile, TFHE-rs generated a _123 megabyte_ server key. We can compress the key down to about 27 megabytes, but still: that’s almost 850,000 times more key than data!

The payload here is particularly small, but a disparity of that size isn’t unheard of. In his [overview of fully homomorphic encryption](https://www.jeremykun.com/2024/05/04/fhe-overview/), Jeremy Kun cites examples in which ciphertexts of dozens or hundreds of _kilobytes_ require keys on the order of _gigabytes_.

Runtime performance is also — to put it lightly — lacking. I benchmarked the unencrypted and encrypted versions of the last write wins register on an M4 MacBook Pro. The unencrypted one averaged a merge time of 0.52 nanoseconds.

The encrypted one? _1.06 seconds_. That’s not a typo: the homomorphically encrypted merge is _two billion times slower_.[5](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-gpu)

Not great!

That’s not all. We said before that our code must execute as though operating on the worst case input. Even if the performance issues improve by many orders of magnitude, the “worst case” requirement will still impose constraints on the CRDT algorithm itself.

Consider a fully homomorphically encrypted last-write wins _map_ CRDT. Most maps store keys sparsely, so the map only grows in size as keys are added.

Here’s a playground that simulates encrypting a sparse map.[6](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-pretend) When you modify the plaintext map on the left, the encrypted map on the right updates. Can you see a security issue?

Imagine you only had access to the map on the right. You could still see data being added and removed! Furthermore, this map lazily encrypts only the data that changes, which would allow you to see exactly which key changed (if any).

A homomorphically encrypted map CRDT couldn’t do that. Since it must assume a worst-case input, it must store the keys _densely_: limiting the size to a fixed number of keys and reserving all the space up front. Merging two identical maps would be exactly as computationally intensive as merging two maps in which _every_ key was updated.[7](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-op)

The playground below simulates a homomorphically encrypted map. While you can add and remove keys to the plaintext map on the left, the encrypted map on the right behaves as though every key is filled. And no matter how you modify the plaintext map, _everything_ in the encrypted map changes:

From the outside, there’s no way to tell what changed in the map: we see the exact same number of keys, and every value has changed. To calculate the new map, the server must go through and merge _every single key_. After that, it needs to transfer the full map to each peer — because remember, as far as it knows, the entire map is different.

These are fundamental limitations of homomorphic encryption! The requirement that homomorphically encrypted code performs as though operating on the worst-case input dramatically increases both the space and time required to update.

Parting Thoughts
----------------

I started this article thinking that local-first software and homomorphic encryption would be natural bedfellows.

But honestly, I came away… a little less enamored. The fundamental limitations of homomorphic encryption mean that it will always operate under a set of worst-case assumptions. Homomorphically encrypted CRDTs aren’t intractable, but they are severely limited by these intrinsic constraints.

So the question remains: how can we secure local-first apps without severely degrading usability?

Luckily, I’m not the only one thinking about this problem!

*   There are [a bunch of](https://dicg-workshop.github.io/2022/papers/jannes.pdf)[research papers](https://repositorio.inesctec.pt/server/api/core/bitstreams/9d417c53-456f-4227-9440-fffb9650e3dd/content)[on secure CRDTs](https://eprint.iacr.org/2023/584.pdf).
*   Martin Kleppman has written spoken about [combining secure group messaging protocols with CRDTs](https://martin.kleppmann.com/2019/05/15/encrypted-crdts.html).
*   Last (but certainly not least), local-first pioneers Ink & Switch have been working on a project called [Keyhive](https://www.inkandswitch.com/keyhive/) that explores how to add access control to local-first data.[8](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-meri)
*   Probably many other projects I’ve missed!

CRDTs are a relatively young technology — the paper formalizing them was published in 2011 — so there’s still a lot of unexplored solution space. We may not have solved this problem yet, but I’m confident that we’re closing in on it!
