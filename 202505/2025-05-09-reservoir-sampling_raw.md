Title: Reservoir Sampling

URL Source: https://samwho.dev/reservoir-sampling/

Markdown Content:
[![Image 1: samwho keyboard logo](https://samwho.dev/images/samwho-keyslogo.svg)](https://samwho.dev/)

Reservoir sampling is a technique for selecting a fair random sample when you don't know the size of the set you're sampling from. By the end of this essay you will know:

*   When you would need reservoir sampling.
*   The mathematics behind how it works, using only basic operations: subtraction, multiplication, and division. No math notation, I promise.
*   A simple way to implement reservoir sampling if you want to use it.

> ![Image 2: A picture of a cartoon husky called "Doe"](https://samwho.dev/images/dogs/doe/default.svg)Before you scroll! This post has been sponsored by the wonderful folks at [ittybit](https://ittybit.com/?ref=sam), and their API for working with videos, images, and audio. If you need to store, encode, or get intelligence from the media files in your app, check them out!

[#](https://samwho.dev/reservoir-sampling/#sampling-when-you-know-the-size) Sampling when you know the size
-----------------------------------------------------------------------------------------------------------

In front of you are 10 playing cards and I ask you to pick 3 at random. How do you do it?

The first technique that might come to mind from your childhood is to mix them all up in the middle. Then you can straighten them out and pick the first 3. You can see this happen below by clicking "Shuffle."

A A

4 4

K K

2 2

J J

Q Q

5 5

8 8

10 10

9 9

Every time you click "Shuffle," the chart below tracks what the first 3 cards were.

A

4

K

2

J

Q

5

8

10

9

At first you'll notice some cards are selected more than others, but if you keep going it will even out. All cards have an equal chance of being selected. This makes it "fair."

Click "Shuffle 100 times" until the chart evens out. You can reset the chart if you'd like to start over.

This method works fine with 10 cards, but what if you had 1 million cards? Mixing those up won't be easy. Instead, we could use a random number generator to pick 3 indices. These would be our 3 chosen cards.

A A

4 4

K K

2 2

J J

Q Q

5 5

8 8

10 10

9 9

We no longer have to move all of the cards, and if we click the "Select" button enough times we'll see that this method is just as fair as the mix-up method.

A

4

K

2

J

Q

5

8

10

9

I'm stretching the analogy a little here. It would take a long time to count through the deck to get to, say, index 436,234. But when it's an array in memory, computers have no trouble finding an element by its index.

Now let me throw you a curveball: what if I were to show you 1 card at a time, and you had to pick 1 at random?

> How many cards are you going to show me?
> 
> ![Image 3: A picture of a cartoon husky puppy called "Haskie" looking confused.](https://samwho.dev/images/dogs/haskie/confused.svg)

That's the curveball: you don't know.

> Can I hold on to all the cards you give me and then pick 1 after you stop?
> 
> ![Image 4: A picture of a cartoon husky puppy called "Haskie"](https://samwho.dev/images/dogs/haskie/default.svg)

No, you can only hold on to 1 card at a time. You're free to swap your card with the newest one each time I show you a card, but you can only hold one and you can't go back to a card you've already seen.

> Then it's impossible! Why would I ever need to do this anyway?
> 
> ![Image 5: A picture of a husky dog called "Haskie", with a concerned facial expression](https://samwho.dev/images/dogs/haskie/concerned.svg)

Believe it or not, this is a real problem and it has a real and elegant solution.

For example, let's say you're building a log collection service. Text logs, not wooden ones. This service receives log messages from other services and stores them so that it's easy to search them in one place.

One of the things you need to think about when building a service like this is what do you do when another service starts sending you way too many logs. Maybe it's a bad release, maybe one of your videos goes viral. Whatever the reason, it threatens to overwhelm your log collection service.

Let's simulate this. Below you can see a stream of logs that experiences periodic spikes. A horizontal line indicates the threshold of logs per second that the log collection service can handle, which in this example is 5 logs per second.

2:03:18 PM

W

\- AI assistant insisted on a 4-hour lunch break to "find themselves"

2:03:18 PM

E

\- git blame revealed teleporter wrote entire codebase in Excel

2:03:18 PM

E

\- your favorite framework wrote tests that test the tests while listening to music

2:03:18 PM

W

\- social media algorithm implemented authentication via interpretive dance

2:03:19 PM

W

\- a guitar decided to become a cryptocurrency influencer

You can see that every so often, logs per second spikes above the threshold. One way to deal with this is "sampling." Deciding to send only a fraction of the logs to the log collection service. Let's send 10% of the logs.

Below we will see the same simulation again, but this time logs that don't get sent to our log collection service will be greyed out. The graph has 2 lines: a black line tracks sent logs, the logs that are sent to our log collection service, and a grey line tracks total logs.

2:03:18 PM

W

\- DNS started routing traffic based on enterprise-grade vibes

2:03:18 PM

E

\- have you tried turning the a parrot off and on again?

2:03:18 PM

I

\- blockchain AI synergy engine escaped and exploded the Captain America

2:03:18 PM

W

\- Kubernetes cluster submitted PR in self-driving car format

2:03:18 PM

I

\- cache implemented blockchain-based cat photo storage

The rate of sent logs never exceeds the threshold, so we never overwhelm our log collection service. However, in the quieter periods we're throwing away 90% of the logs when we don't need to!

What we really want is to send _at most_ 5 logs per second. This would mean that during quiet periods you get all the logs, but during spikes you discard logs to protect the log collection service.

The simple way to achieve this would be to send the first 5 logs you see each second, but this isn't fair. You aren't giving all logs an equal chance of being selected.

[#](https://samwho.dev/reservoir-sampling/#sampling-when-you-don-t-know-the-size) Sampling when you don't know the size
-----------------------------------------------------------------------------------------------------------------------

We instead want to pick a fair sample of all the logs we see each second. The problem is that we don't know how many we will see. Reservoir sampling is an algorithm that solves this exact problem.

> 1 second isn't a long time, can't we just store all the messages we see and then use the select method from way back up there?
> 
> ![Image 6: A picture of a cartoon husky puppy called "Haskie" looking confused.](https://samwho.dev/images/dogs/haskie/confused.svg)

You _could_, but why live with that uncertainty? You'd be holding on to an unknown number of logs in memory. A sufficiently big spike could cause you problems. Reservoir sampling solves this problem, and does so without ever using more memory than you ask it to.

Let's go back to our curveball of me showing you 1 card at a time. Here's a recap of the rules:

1.  I'll draw cards one at a time from a deck.
2.  Each time I show you a card, you have to choose to hold it or discard it.
3.  If you were already holding a card, you discard your held card before replacing it with the new card.
4.  At any point I can stop drawing cards and whatever card you're holding is the one you've chosen.

How would you play this game in a way that ensures all cards have been given an equal chance to be selected when I decide to stop?

> How about we flip a coin every new card? If it's heads, we keep the card we have. If it's tails, we swap it out for the new card.
> 
> ![Image 7: A picture of a husky dog called "Haskie", looking triumphant](https://samwho.dev/images/dogs/haskie/triumphant.svg)

You're on the right track. Let's have a look at how the coin flip idea plays out in practice. Below you see a deck of cards. Clicking "Deal" will draw a card and 50% of the time it will go to the discard pile on the right, and 50% of the time it will become your held card in the center, with any previously held card moving to the discard pile.

0

0

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

The problem is that while the hold vs discard counts are roughly equal, which feels fair, later cards are much more likely to be held when I stop than earlier cards. The first card drawn has to win 10 coin flips to still be in your hand after the 10th card is drawn. The last card only has to win 1.

Scrub the slider below to see how the chances change as we draw more cards. Each bar represents a card in the deck, and the height of the bar is the chance we're holding that card when I stop. Below the slider are the chances we're holding the first card drawn vs. the last card drawn.

Slide to draw cards.

K K

card 1

\-

K K

card -

\-

Anything older than 15 cards ago is has a less than 0.01% chance of being held when I stop.

> You said I was on the right track! How can this be the right track when I'm more likely to win the lottery than to be holding the card I saw 24 draws ago?
> 
> ![Image 8: A picture of a husky dog called "Haskie", with a concerned facial expression](https://samwho.dev/images/dogs/haskie/concerned.svg)

Because believe it or not, we only have to make one small change to this idea to make it fair.

Instead of flipping a coin to decide if we'll hold the card or not, instead we give each new card a `1/n` chance of being held, where `n` is the number of cards we've seen so far.

> Wait, that's it? That makes it fair?
> 
> ![Image 9: A picture of a husky dog called "Haskie", with a concerned facial expression](https://samwho.dev/images/dogs/haskie/concerned.svg)

Yep! In order to be fair, every card must have an equal chance of being selected. So for the 2nd card, we want both cards to have a `1/2` chance. For the 3rd card, we want all 3 cards to have a `1/3` chance. For the 4th card, we want all 4 cards to have a `1/4` chance, and so on. So if we use `1/n` for the new card, we can at least say that the new card has had a fair shot.

Let's have a look at the chances as you draw more cards with this new method.

Slide to draw cards.

K K

card 1

\-

K K

card -

\-

> I get how each **new** card has the right chance of being selected, but how does that make the **older** cards fair?
> 
> ![Image 10: A picture of a cartoon husky puppy called "Haskie" looking confused.](https://samwho.dev/images/dogs/haskie/confused.svg)

So far we've focused on the chance of the new card being selected, but we also need to consider the chance of the card you're holding staying in your hand. Let's walk through the numbers.

### [#](https://samwho.dev/reservoir-sampling/#card-1) Card 1

The first card is easy: we're not holding anything, so we always choose to hold the first card. The chance we're holding this card is `1/1`, or `100%`.

Hold

100%

Replace

\-

### [#](https://samwho.dev/reservoir-sampling/#card-2) Card 2

This time we have a real choice. We can keep hold of the card we have, or replace it with the new one. We've said that we're going to do this with a `1/n` chance, where `n` is the number of cards we've seen so far. So our chance of replacing the first card is `1/2`, or `50%`, and our chance of keeping hold of the first card is its chance of being chosen last time multiplied by its chance of being replaced, so `100% * 1/2`, which is again `50%`.

Hold

100% \* 1/2

50%

Replace

1/2

50%

### [#](https://samwho.dev/reservoir-sampling/#card-3) Card 3

The card we're holding has a `50%` chance of being there. This is true regardless what happened up to this point. No matter whether we're holding card 1 or card 2, it's `50%`.

The new card has a `1/3` chance of being selected, so the card we're holding has a `1/3` chance of being replaced. This means that our held card has a `2/3` chance of remaining held. So its chances of "surviving" this round are `50% * 2/3`.

Hold

50% \* 2/3

33.33%

Replace

1/3

33.33%

### [#](https://samwho.dev/reservoir-sampling/#card-n) Card N

This pattern continues for as many cards as you want to draw. We can express both options as formulas. Drag the slider to substitute `n` with real numbers and see that the two formulas are always equal.

Hold

1/(n-1) \* (1-(1/n))

\-

Replace

1/n

\-

If `1/n` is the chance of choosing the new card, `1/(n-1)` is the chance of choosing the new card from the previous draw. The chance of _not_ choosing the new card is the _complement_ of `1/n`, which is `1-(1/n)`.

Below are the cards again except this time set up to use `1/n` instead of a coin flip. Click to the end of the deck. Does it feel fair to you?

0

0

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

There's a good chance that through the 2nd half of the deck, you never swap your chosen card. This _feels_ wrong, at least to me, but as we saw above the numbers say it is completely fair.

[#](https://samwho.dev/reservoir-sampling/#choosing-multiple-cards) Choosing multiple cards
-------------------------------------------------------------------------------------------

Now that we know how to select a single card, we can extend this to selecting multiple cards. There are 2 changes we need to make:

1.  Rather than new cards having a `1/n` chance of being selected, they now have a `k/n` chance, where `k` is the number of cards we want to choose.
2.  When we decide to replace a held card, we choose one of the `k` cards we're holding at random.

So our new previous card selection formula becomes `k/(n-1)` because we're now holding `k` cards. Then the chance that any of the cards we're holding get replaced is `1-(1/n)`.

Let's see how this plays out with real numbers.

Hold

k/(n-1) \* (1-(1/n))

\-

Replace

k/n

\-

The fairness still holds, and will hold for any `k` and `n` pair. This is because all held cards have an equal chance of being replaced, which keeps them at an equal likelihood of still being in your hand every draw.

A nice way to implement this is to use an array of size `k`. For each new card, generate a random number between 0 and `n`. If the random number is less than `k`, replace the card at that index with the new card. Otherwise, discard the new card.

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

A A

2 2

3 3

4 4

5 5

6 6

7 7

8 8

9 9

10 10

J J

Q Q

K K

And that's how reservoir sampling works!

[#](https://samwho.dev/reservoir-sampling/#applying-this-to-log-collection) Applying this to log collection
-----------------------------------------------------------------------------------------------------------

Let's take what we now know about reservoir sampling and apply it to our log collection service. We'll set `k=5`, so we're "holding" at most 5 log messages at a time, and every second we will send the selected logs to the log collection service. After we've done that, we empty our array of size 5 and start again.

This creates a "lumpy" pattern in the graph below, and highlights a trade-off when using reservoir sampling. It's no longer a real-time stream of logs, but chunks of logs sent at an interval. However, sent logs never exceeds the threshold, and during quiet periods the two lines track each other almost perfectly.

2:03:18 PM

I

\- quantum computer automated themselves out of a job

2:03:18 PM

I

\- log aggregator became legacy poetry generator

2:03:18 PM

E

\- samwho estimated task as "somewhere between now and heat death of universe"

2:03:18 PM

W

\- cryptocurrency started philosophical debate about meme generator

2:03:18 PM

I

\- 3 hamsters in a trench coat fell asleep during their own demo

No logs lost during quiet periods, and never more than threshold logs per second sent during spikes. The best of both worlds. It also doesn't store more than `k=5` logs, so it will have predictable memory usage.

[#](https://samwho.dev/reservoir-sampling/#further-reading) Further reading
---------------------------------------------------------------------------

Something you may have thought while reading this post is that some logs are more valuable than others. You almost certainly want to keep all error logs, for example.

For that use-case there _is_ a [weighted](https://en.wikipedia.org/wiki/Reservoir_sampling#Weighted_random_sampling) variant of reservoir sampling. I wasn't able to find a simpler explanation of it, so that link is to Wikipedia which I personally find a bit hard to follow. But the key point is that it exists and if you need it you can use it.

[#](https://samwho.dev/reservoir-sampling/#conclusion) Conclusion
-----------------------------------------------------------------

Reservoir sampling is one of my favourite algorithms, and I've been wanting to write about it for years now. It allows you to solve a problem that at first seems impossible, in a way that is both elegant and efficient.

Thank you again to [ittybit](https://ittybit.com/?ref=sam) for sponsoring this post. I really couldn't have hoped for a more supportive first sponsor. Thank you for believing in and understanding what I'm doing here.

Thank you to everyone who read this post and gave their feedback. You made this post much better than I could have done on my own, and steered me away from several paths that just weren't working.

If you want to tell me what you thought of this post by sending me an anonymous message that goes directly to my phone, go to [https://samwho.dev/ping](https://samwho.dev/ping).
