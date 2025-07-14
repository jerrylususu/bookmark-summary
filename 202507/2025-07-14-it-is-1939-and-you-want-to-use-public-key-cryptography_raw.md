Title: It is 1939 and you want to use public-key cryptography

URL Source: https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/

Published Time: 2025-07-13T12:34:08+01:00

Markdown Content:
Imagine, just for a moment, that a mathematical breakthrough had occurred on the eve of the second World War. Perhaps Turing or Rejewski or Driscoll realised that prime number theory held the key to unbreakable encryption. This blog post attempts to answer the question "could public-key cryptography have been used in 1939?"

Let's briefly step back into history.

The Enigma machine represented the most powerful form of convenient cryptography available in the early 20th century. There were only two practical ways to crack its encryption.

1.   Capture a codebook with the encryption keys printed in it [0](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:u571 "As seen in the historically \"accurate\" film \"U571\"."). 
2.   Literally invent the computer [1](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:game "As seen in the historically \"accurate\" film \"The Imitation Game\"."). 

The basis of Enigma is _conceptually_ simple. You want to write a character. You follow a complex sequence of instructions and get the resulting encrypted character. You want to write the next character, so you follow the same instructions for the first which then _changes the sequence of instructions_ for the next character. And so on. Every character you type changes the algorithm for the next character. Fiendish!

You _could_ encrypt an Enigma message by hand. But it would be tiresome, error-prone, and take ages. So a machine was invented to do the hard work. A series of cogs and wheels and wires and lights.

![Image 1: The Enigma machine. A typewriter with a complex mechanical set of rotors and electrical wiring. Photo by Museo Nazionale Scienza e Tecnologia Leonardo da Vinci. CC BY-SA.](https://shkspr.mobi/blog/wp-content/uploads/2025/07/Enigma_crittografia_-_Museo_scienza_e_tecnologia_Milano.jpg)

One of the weaknesses of Enigma is that it used _symmetric_ encryption. The password used to scramble the message was the same as the one used to descramble it. Each day the codes changed, so they were printed in a handy codebook which was distributed to each operator. If someone captured the codebook, they could decrypt all sent and received messages.

Decades after the war, _asymmetric_ cryptography was invented[2](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:history "As seen in the historically \"accurate\" film By either the Brits or the Americans depending on whose history you think is accurate."). The magic of asymmetric encryption is that it allows you to have one password to scramble the message and a _totally different_ one to unscramble it. This completely obliterates the risk of your codebooks being discovered; you can have a "public key" for encryption. Anyone with that key can encrypt a message, but not decrypt it. You have a private key for decryption which you guard with your life.

Asymmetric encryption powers the modern world. It is made possible by high-speed computer chips which can precisely perform mind-boggling calculations in microseconds.

Let us slip into an _alternate_ timeline. The mathematics behind asymmetric encryption are conceptually simple - even if they are exceedingly difficult to execute without a computer. If the mathematicians of the day had made the necessary intellectual breakthroughs, could public-key encryption have worked in WW2?

I'm going to work through the following problem to prove that it was _just about_ possible[3](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:ed "With huge thanks to my gang of unpaid editors, including Colin and Liz. Any mistakes, errors, and typos are my responsibility.").

1.   Could a public / private keypair have been calculated in the 1930s?
2.   Is it possible to use paper-and-pencil to encrypt a message using a very short public key?
3.   Would it have been possible to build a machine to encrypt using longer public keys?
4.   What key length would have prevented the private key being cracked by brute-force?

Let's take a look at the last question first.

*   [Table of Contents](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#table-of-contents)
-------------------------------------------------------------------------------------------------------------------------------

    *   [Why brute force?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#why-brute-force)
    *   [Generating a Keypair](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#generating-a-keypair)        *   [What is a keypair?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#what-is-a-keypair)
        *   [Calculating a keypair](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#calculating-a-keypair)
    *   [Let's Encrypt!](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#lets-encrypt)
    *   [Let's Decrypt!](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#lets-decrypt)
    *   [The Land of Big Numbers](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#the-land-of-big-numbers)        *   [Manual decryption](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#manual-decryption)
    *   [The Benefits of Symmetric Encryption](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#the-benefits-of-symmetric-encryption)        *   [A brief look into key exchange](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#a-brief-look-into-key-exchange)
    *   [Would a machine have helped?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#would-a-machine-have-helped)
    *   [So it is possible?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#so-it-is-possible)

[Why brute force?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#why-brute-force)
----------------------------------------------------------------------------------------------------------------------------

The original machines used to crack Enigma used brute-force; trying every possible combination until they discovered the right one. That's not _strictly_ true - a large part of cryptanalysis was understanding the statistics behind the encryption algorithm, the likely content of messages, and common phrases that they contained.

Modern encryption algorithms are resistant to most of those statistical attacks. So the only feasible method of cracking a private key is by trying each combination sequentially.

Let's suppose there's a very short private key - for example just 4 bits long. There are 2 4 possible combinations; 16 in total. It seems reasonable to suppose that, if the message can be easily decrypted by the intended recipient, it could easily be cracked by someone able to try 16 different key combinations.

For every bit of length added to the key, the number of combinations doubles. 2 4=16. 2 5=32. 2 6=64. Once you get the 2 32, you're at 4 _billion_ combinations[4](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:bits "By contrast, the Enigma had about 67 bits of complexity, resulting in approximately 158 quintillion combinations. Hence the need for cryptanalysis rather than just brute force!"). Trying one combination per second would take over 120 years to complete.

Of course, manually using a 32 bit key might be too complex for the technology of the day. So a shorter key might be easier to use while still retaining sufficient strength. How difficult is it to manually encipher and decipher messages with short keys?

Let's go back to question 0.

[Generating a Keypair](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#generating-a-keypair)
-------------------------------------------------------------------------------------------------------------------------------------

How do we generate an asymmetric keypair? Remember, no computers allowed[5](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:computers "Well, OK, you could have a staff of several women who were called computers.")!

### [What is a keypair?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#what-is-a-keypair)

Briefly and incorrectly put, keys are based on prime factors.

Multiply these two prime numbers: 29 and 113.

You can easily do that on paper or on a pocket calculator. It is trivial. But suppose I asked you to reverse the equation? Find out which two prime numbers are multiplied to give the number 40,133. That's much harder. For larger numbers, it is [even harder than you think](https://en.wikipedia.org/wiki/Integer_factorization).

### [Calculating a keypair](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#calculating-a-keypair)

Mathematically, it is relatively simple. You need to know the following concepts:

*   What is a prime number? (A number divisible by nothing other than itself and 1. For example, 13.)
*   What is a coprime? (Another number with no common factors to the first [6](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:coprime "Confusingly, a co-prime doesn't have to be a prime number."). For example, the number 13 has a coprime of 9.) 
*   What is a modular inverse? (When the Prime is multiplied by Coprime, then divided by the modular inverse, the remainder is 1.)

You can [follow along with this Python example](https://www.teach.cs.toronto.edu/~csc110y/fall/notes/08-cryptography/05-rsa-cryptosystem-implementation.html), but the steps are simple enough to do by hand using sufficiently small numbers.

[Here's the algorithm](https://www.baeldung.com/cs/prime-numbers-cryptography):

*   Pick two prime numbers, 𝒑 and 𝒒
*   Multiply them to get 𝒏
*   Calculate (𝒑-1) × (𝒒-1) to get ϕ(𝒏)
*   Pick a coprime of ϕ(𝒏) to get 𝒆 
    *   Any coprime can be randomly selected, although [there are some choices which are bad](https://eprint.iacr.org/2020/1059.pdf). 

*   Calculate 𝒅 where 𝒅 × 𝒆 = 1 (mod ϕ(𝒏))
*   The private key consists of 𝒏 and 𝒅
*   The public key consists of 𝒏 and 𝒆

Let's do that with two small prime numbers 17 and 61. They are sufficiently small to be calculated by hand[7](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:small "By the end of the 19th century, all prime numbers up to 1 billion had been discovered - that's around 50 million different primes. Far fewer combinations than the Enigma, but still a formidable…").

*   𝒏 = 17 × 61 = 1037
*   ϕ(𝒏) = 16 × 60 = 960
*   𝒆 = 77 (Chosen randomly)
*   𝒅 = 773 (Calculated using the Extended Euclidean Algorithm, which was [first described in 1740](https://rjlipton.com/2016/08/28/descending-proofs-into-algorithms/)) 

Here's how calculating 𝒅 works. This isn't intended to be a complete explanation of how the algorithm works, but it is sufficient to show that generating keypairs would have been well within the grasp of mathematicians of the 1930s. Feel free to [skip to the next section](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#lets-encrypt).

| Step | ri−2 | ri−1 | qi=⌊(ri−2)÷(ri−1)⌋ | ri=(ri−2_−qi×(ri−1) | xi=(xi−2)−qi×(xi−1) | yi=(yi−2)−qi×(yi−1) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 960 |  |  |  | 1 | 0 |
| 1 | 77 |  |  |  | 0 | 1 |
| 2 | 960 | 77 | 960÷77=12 | 960−12×77=960−924=36 | 1−12×0=1 | 0−12×1=−12 |
| 3 | 77 | 36 | 77÷36=2 | 77−2×36=77−72=5 | 0−2×1=−2 | 1−2×(−12)=1+24=25 |
| 4 | 36 | 5 | 36÷5=7 | 36−7×5=36−35=1 | 1−7×(−2)=1+14=15 | −12−7×25=−12−175=−187 |
| 5 | 5 | 1 | 5÷1=5 | 5−5×1=0 | −2−5×15=−2−75=−77 | 25−5×(−187)=25+935=960 |

From Step 4, we have: 1 = 15 × 960 + (−187) × 77

We are interested in the coefficient of 77, which is −187. This means −187 × 77 ≡ 1 (mod 960)

We need a positive value for d, we add ϕ(𝒏) to −187.

𝒅 = −187 + 960 = 773

[Let's Encrypt!](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#lets-encrypt)
-----------------------------------------------------------------------------------------------------------------------

We have a plaintext message (𝒎), we calculate the encrypted version (𝒄) with the formula 𝒄=𝒎 𝒆%𝒏

Let's suppose our message starts "HELLO". We'll give every letter a number. Our message starts with H - the eighth number of the alphabet.

8 77 % 1037 = 638

You can do that today on any pocket calculator. But could a competent mathematician calculate that by hand?

Exponentials get very large very quickly. There are some shortcuts, like [Modular Exponentiation](https://crypto.stanford.edu/pbc/notes/numbertheory/exp.html), but it is a fairly manual process. Doable, but not pleasant.

With enough time, you could manually encrypt a message like HELLO from `8 5 12 12 15` to `638 768 388 388 835`.

[Let's Decrypt!](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#lets-decrypt)
-----------------------------------------------------------------------------------------------------------------------

We have an encrypted version (𝒄), we calculate the plaintext message (𝒎) using the formula 𝒎=𝒄 𝒅%𝒏

638 773 % 1037 = 8

Again, piece of cake today, but an almost insurmountable a manual grind for a pencil and paper computer.

[The Land of Big Numbers](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#the-land-of-big-numbers)
-------------------------------------------------------------------------------------------------------------------------------------------

In the toy example above, we turned `8 5 12 12 15` into `638 768 388 388 835`. That's a _very bad_ way of encrypting text. Working on individual letters allows for fairly trivial attacks in the form of frequency analysis. You might not know what prime numbers were used, but you know what the most common letter in English is and which letters often come in pairs.

Let's pretend that a binary code like ASCII had been invented by the 1930s, giving each letter its own number[8](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:baudot "This isn't too much of a stretch. The Baudot code was invented in the late 1800s. It is the binary code from which ASCII descends."). So the text translates to `1001000 1000101 1001100 1001100 1001111` 7 bits is sufficient to store 128 characters, which is good enough for text, numbers, and punctuation.

Smooshing those bits together gives `10010001000101100110010011001001111`, which is 19,473,311,311 in decimal.

But here we hit a snag! And rather an important one. Our message 𝒎 _must_ be less than the key 𝒏 otherwise the maths doesn't work. So each "chunk" that is encrypted must be less than, in this case, 1037. In binary, 1037 is an 11 bit number - `10000001101` so let's chop the long binary string into groups of ten bit numbers[9](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:ten "In this example, we might still be subject to some frequency analysis issues. There are common ways to start a message which could be pre-computed.").

`1001000100 0101100110 0100110010 01111` which, in decimal is `580 358 306 15`.

How easy is it to calculate 580 77 % 1037?

Well, 580 77 is this 213 digit number:

```
608072697981095702436950488113933187346914897948969284857902654293722732546509642998889930612690327222151182305275310987597838669368524800000000000000000000000000000000000000000000000000000000000000000000000000000
```

Erk!

But, using Modular Exponents as mentioned above, it is just about doable to calculate it modulo 1037, to give the answer of 287.

### [Manual decryption](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#manual-decryption)

The reverse starts with 287 773 - which is a 1,900 digit monster:

```
8764076814703289747574882682976372218202744117677541506077211396661935894880088329104690573410169261407987339892509470735016770231680618285939631509696980819464283401576517028048058993738338212389624747625283501942530083096110122657663164247353946331224458655354563571410933387843518380823303070498533169970946532897148031815166130665099650412982697122333628263892989475993249398481489331587762699843745762158170438822856768199827373555952739238985122598013870248178442111493156638843557234189706340583484083198539928533412908164601212156510176835050241254357263891198022046581958723118373933025616238122851775785374806117735760339884871872459839891658484324244684568308566814363900160248669794871064158507228968139134265889106231940693454825286506694141354013548608249280312471711991110620182847512187270642477617113287609180070026599666866308043914633111575444534093596344978016090107810671208184558268833063049379828413374691670084694302906835473338305746126263384285289946318656379558672414106052389234651640556324925755102419977400705380530065200979454412655589210213499344464257545650144053951331232875248144510526902329651434948453811412299881757959472385612984529276884875992403776906120156323972516615974836750108651889727547635267691073017967972912857552981641062535868781437285961802657794299581952590634427029261618023579258415033039194531248890027241354305598494848058858007937053616885726584609180601099791624229397351704959975692231801353195625613188074479028803108341519961929058549691769420863241680253570449204941176209229012471375228095132443055306202854239923235089133210534407289759826457721708012298751583195590595588629155245907825766955419953439709562536473174022072079161000252263007473231270835574140865544015688184196904473193955950050289022786886850214941882872222159427413174019940977015728353647777297220099220515546638682392602897440872932518693189627668062600415788447
```

There is no sensible way for a human to calculate that without mechanical or algorithmic assistance.

So our 1939 cryptographers are ready to pack up and go home, right?

Wrong! Remember, the plaintext message 𝒎 = 𝒄 𝒅 % 𝒏

For this operation, that's 287 773 % 1037

Let's turn 𝒅 into binary - decimal `773` is `1100000101` - we can now use the ["square-and-multiply" algorithm](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) to calculate the plaintext.

Again, you don't need to read this table and can [skip to the next section](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#the-benefits-of-symmetric-encryption) - this is just to show that the calculations are possible (if somewhat convoluted).

| Exponent Bit | base 2 % modulus | If bit is 1, result = (result * base) % modulus | Current base | Current result |
| --- | --- | --- | --- | --- |
| 1 |  | result = (1 * 287) % 1037 = 287 | 287 | 287 |
|  | base = 287 2 % 1037 |  |  |  |
|  | 287 2 = 82369 |  |  |  |
|  | 82369÷1037=79, remainder 486 |  | 486 | 287 |
| 0 |  | (No change to result) |  |  |
|  | base = 486 2 % 1037 |  |  |  |
|  | 486 2=236196 |  |  |  |
|  | 236196÷1037=227, remainder 177 |  | 177 | 287 |
| 1 |  | result = (287 * 177) % 1037 |  |  |
|  | 287×177=50799 |  |  |  |
|  | 50799÷1037=49, remainder 36 | 36 |  | 36 |
|  | base = 177 2 % 1037 |  |  |  |
|  | 177 2=31329 |  |  |  |
|  | 31329÷1037=30, remainder 219 |  | 219 | 36 |
| 0 |  | (No change to result) |  |  |
|  | base = 219 2 % 1037 |  |  |  |
|  | 219 2=47961 |  |  |  |
|  | 47961÷1037=46, remainder 239 |  | 239 | 36 |
| 0 |  | (No change to result) |  |  |
|  | base = 239 2 % 1037 |  |  |  |
|  | 239 2=57121 |  |  |  |
|  | 57121÷1037=55, remainder 036 |  | 36 | 36 |
| 0 |  | (No change to result) |  |  |
|  | base = 36 2 % 1037 |  |  |  |
|  | 36 2=1296 |  |  |  |
|  | 1296÷1037=1, remainder 259 |  | 259 | 36 |
| 0 |  | (No change to result) |  |  |
|  | base = 259 2 % 1037 |  |  |  |
|  | 259 2=67081 |  |  |  |
|  | 67081÷1037=64, remainder 789 |  | 789 | 36 |
| 0 |  | (No change to result) |  |  |
|  | base = 789 2 % 1037 |  |  |  |
|  | 789 2=622521 |  |  |  |
|  | 622521÷1037=600, remainder 321 |  | 321 | 36 |
| 1 |  | result = (36 * 321) % 1037 |  |  |
|  | 36×321=11556 |  |  |  |
|  | 11556÷1037=11, remainder 119 | 119 |  | 119 |
|  | base = 321 2 % 1037 |  |  |  |
|  | 321 2=103041 |  |  |  |
|  | 103041÷1037=99, remainder 450 |  | 450 | 119 |
| 1 |  | result = (119 * 450) % 1037 |  |  |
|  | 119×450=53550 |  |  |  |
|  | 53550÷1037=51, remainder 580 | 580 |  | 580 |

Yeeeesh! Tedious, but absolutely doable by hand. As long as you don't make mistakes and don't fall asleep.

Could this be made easier? Perhaps - but let's consider whether this effort would be worth it.

[The Benefits of Symmetric Encryption](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#the-benefits-of-symmetric-encryption)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

As discussed earlier, Enigma's password let you encrypt and decrypt using the same password. That means if the password leaks, you have lost the secrecy of both your outgoing _and_ incoming messages.

The key advantage of symmetric encryption is that it is _much_ easier to use. You set today's secret, then you can send and receive with ease. You do not need to manage two separate codes.

Let's imagine that there is a theoretical machine which can mechanically or electronically code and decode messages. You have the public key for sending messages back to base - but what about if you want to _receive_ a message?

You will need a private key. A key which has to be protected in exactly the same way as Enigma's codebooks. If your private key is captured, all the messages previously sent to you can be decrypted.

OK, perhaps the solution is to give every machine its own unique keypair? Well, to quote the sages, [now you have two problems](https://regex.info/blog/2006-09-15/247).

First is the complexity of managing all the public keys. You have to remember which one to use when sending information.

Secondly, it means that you cannot broadcast a _general_ message to all recipients. If HQ wants to send a message, they need to encrypt it separately for each receiver and also broadcast it separately. That also means the receivers have to know which message is intended for them[10](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:listening "Yes, there are ways round this. You could start each message with a plaintext callsign, or broadcast on different frequencies, or some other differentiator. The point is that it adds complexity."). Similarly, if a single user wants to send an encrypted message to all nearby units, they need to know who they are and separately encrypt messages to them[11](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fn:separate "Again, there are ways round this. But they mostly involve generating even more shared keys. At which point, you're almost back to symmetric encryption!").

Simplicity is the main factor in making usable security [as I've written about before](https://shkspr.mobi/blog/2014/01/the-hardest-problem-in-encryption-usability/). Regardless of whether a machine could have done the calculations, key management is a tough problem.

### [A brief look into key exchange](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#a-brief-look-into-key-exchange)

[Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) is a cryptographic technique which allows two or more parties to use an insecure channel to exchange enough information to create a unique public/private keypair for themselves. As with all the other maths talked about, it is conceptually simple - but rather difficult to do by hand.

Given the limitations of the speed of 1930s technology, it might be easier just to broadcast in plaintext "Hello! I'm station 123 and my public key is ..." That would be a simple way of distributing your keys but has two disadvantages:

*   The enemy can flood you with encrypted messages. You have no way to verify that they come from a legitimate source.
*   There's no way to verify who the public key is from.

I'm not going to get into cryptographic signature verification because this blog post is already too long!

[Would a machine have helped?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#would-a-machine-have-helped)
----------------------------------------------------------------------------------------------------------------------------------------------------

This, alas, is approaching the limits of my ignorance. I know it is possible to [build a Difference Engine out of Lego](https://www.cs.princeton.edu/~chazelle/courses/BIB/BabbageEngine.html). Similarly, in the late 1930s it was possible to build a [mechanical calculator](https://en.wikipedia.org/wiki/Curta) which was small, lightweight, and accurate.

There were [massive analogue computers on battleships](https://arstechnica.com/information-technology/2020/05/gears-of-war-when-mechanical-analog-computers-ruled-the-waves/), able to solve "20-plus variable calculus problems in real-time". At around 1,400Kg these weren't as portable as the typewriter sized Enigma - but do go some way to showing it _might_ have been possible to design a mechanical computer for these equations.

[So it _is_ possible?](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#so-it-is-possible)
----------------------------------------------------------------------------------------------------------------------------------

The mathematics behind public key cryptography are simple and, in my estimation, could easily have been understood by people nearly a century ago.

The various algorithms for simplifying the necessary calculations were neither obscure nor difficult to implement.

With smaller keys, it is possible to hand-calculate encryption and decryption

But, could it work in practice? If you had suitably trained battlefield mathematicians, it would be _just about_ feasible to encrypt a message for transmission and decrypt something you've received. You wouldn't want to do it while under fire or for any long messages or while using large prime numbers. But, _technically_ it is possible to hand-calculate the encryption and decryption of public key cryptography!

Let's look through the steps again.

*   Generate a public / private keypair. 
    *   Yes! Tedious for larger primes, but well within the abilities of skilled mathematicians.

*   Converting a plaintext message to binary. 
    *   Yes! Baudot codes were well known, as were things like Morse code.

*   Splitting a binary message into smaller chunks. 
    *   Yes! A trivial exercise on paper, but might be difficult mechanically.

*   Encrypting a chunk. 
    *   Possible but difficult - especially with larger keys.

*   Decrypting a chunk. 
    *   Possible but difficult - especially with larger keys.

*   Creating a machine to do the difficult work. 
    *   A very cautious maybe. Large battlefield mechanical-computers existed and were precise. Given the effort that went on in Bletchley Park, I don't doubt _something_ could have been created. 
    *   However, given the complexity of the calculations, I don't think a portable machine would have been possible.

*   Key management. 
    *   A nightmare, as always.

Aside from the conceptual leaps required and the lack of computational power, the major problem with successfully deploying public key cryptography in 1939 is… usability!

The usability of security systems is often hidden from us. Managing a complex key infrastructure is a problem which _still_ plagues the security industry. Despite decades of advances, we still regularly read stories about ["secure" microchips getting hacked for their keys](https://blog.stackademic.com/breaking-rsa-encryption-on-hardware-devices-with-side-channel-power-analysis-leaking-the-private-201374858545) - I imagine it would be trivial to extract them from a mechanical computer.

Could public-key cryptography have been used in 1939? Possibly, but the complexity of mechanical computation would have made it impractical.

If you happen across a time machine with access to the mid-20th century, please pop back and let me know if I am right.

* * *

1.   As seen in the historically "accurate" film "[U571](https://www.imdb.com/title/tt0141926/)".[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:u571)

2.   As seen in the historically "accurate" film "[The Imitation Game](https://www.imdb.com/title/tt2084970)".[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:game)

3.   ~~As seen in the historically "accurate" film~~ By either the Brits or the Americans [depending on whose history you think is accurate](https://en.wikipedia.org/wiki/Public_key_infrastructure#History).[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:history)

4.   With huge thanks to my gang of unpaid editors, including [Colin](https://solipsys.co.uk/) and Liz. Any mistakes, errors, and typos are my responsibility.[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:ed)

5.   By contrast, [the Enigma had about 67 bits of complexity](https://en.wikipedia.org/wiki/Enigma_machine#Mathematical_analysis), resulting in approximately 158 quintillion combinations. Hence the need for cryptanalysis rather than just brute force![↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:bits)

6.   Well, OK, you could have a staff of several [women who were called computers](https://www.sciencemuseum.org.uk/objects-and-stories/women-computing).[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:computers)

7.   Confusingly, a co-prime doesn't have to be a prime number.[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:coprime)

8.   By the end of the 19th century, [all prime numbers up to 1 billion](https://arxiv.org/pdf/1810.05244) had been discovered - that's around 50 million different primes. Far fewer combinations than the Enigma, but still a formidable challenge to try and randomly guess which two had been used.[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:small)

9.   This isn't too much of a stretch. The [Baudot code](https://en.wikipedia.org/wiki/Baudot_code) was invented in the late 1800s. It is the binary code from which ASCII descends.[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:baudot)

10.   In this example, we might still be subject to _some_ frequency analysis issues. There are common ways to start a message which could be pre-computed.[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:ten)

11.   Yes, there are ways round this. You could start each message with a plaintext callsign, or broadcast on different frequencies, or some other differentiator. The point is that it adds complexity.[↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:listening)

12.   Again, there are ways round this. But they mostly involve generating even more shared keys. At which point, you're almost back to symmetric encryption![↩︎](https://shkspr.mobi/blog/2025/07/it-is-1939-and-you-want-to-use-public-key-cryptography/#fnref:separate)
