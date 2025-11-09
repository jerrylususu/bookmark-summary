Title: Thinking clearly about software

URL Source: https://www.seangoedecke.com/thinking-clearly/

Markdown Content:
You can go a long way as a software engineer without ever managing to think clearly. The feedback loop of writing and running code is so immediate that we can often get by with trial-and-error.

### Why is it important to think clearly?

Here are five reasons.

If you can think clearly about software, you can communicate clearly, which can lift other people up out of their confusion. If you write it down, you can do that at scale. There are few higher-leverage things you can do in an organization than writing down clear thoughts about your work.

Thinking clearly increases the rate at which you can learn. You can learn by trial-and-error, but what you learn is mostly heuristics: this kind of thing tends to work in that situation. If you can, it’s better to learn systematically, so you can understand _why_ things work or don’t work.

Clear thought is not a binary but a spectrum. Your progress along that spectrum compounds with practice: if you’ve been trying to think clearly for ten years, you’ll be more successful than someone who’s just starting now.

If you can think clearly about some parts of a problem, that gives you a clear indication of the difficult parts that you ought to spend more time on: i.e. the parts that you’re struggling to think clearly about.

Unlike many other avenues of work, software systems are largely deterministic, so it’s both easier and more useful to think clearly about them.

### To think clearly, think slowly

My philosophy MA supervisor, Karen Jones, used to tell me to “think in slow motion”. She was right, and the lesson applies doubly to tech. Slow down! The opposite of thinking clearly is frantically trying different things until the problem goes away. Instead, take no action, breathe, and think slowly and deliberately through the problem. This is intellectually hard, but the main challenge is actually emotional. You need to get comfortable with the problem just sitting there in your mind: the bug, or the incident, or the thing you don’t understand.

When thinking slowly, you should never take an action (e.g. running a test or interacting with your program) without predicting what will happen and why. Do this even with the most obvious predictions: this empty test should pass, or when I visit my local app I should see the main page in my browser. Be as specific as possible. Don’t predict “I should get an error here”, predict the specific type of error. This is particularly important when debugging, because a buggy program always reflects a lack of understanding, and a lack of understanding always causes failed predictions about how the software should behave. If you can find the spot where you fail to predict the software, you’re well on your way to debugging it.

### Focus on the invariants

What’s the difference between a complete beginner and an expert? The beginner sees a thousand facts and has a thousand ideas, almost all of which are wrong or irrelevant. The expert sees the one relevant fact and has the one correct idea. That’s because expertise in software is the mastery of invariants: beliefs about how software works that are true 99.99% of the time. For instance, if you know that the service you work on always returns 403s for auth failures, then if you’re getting a 401 you know it’s probably coming from another layer. This works for more general beliefs too. For instance, a process must be running to serve requests. So when you’re troubleshooting your dev environment, and you kill the dev server but you’re still getting responses, you know it’s definitely not coming from the process you killed.

Software is great because there are lots and lots of invariants - more than almost any other field. The more comfortable you are with them, the more you can scope down the problem. Of course, sometimes a belief you think is an invariant is actually wrong. That’s typically the cause of a really nasty debugging session. Maybe there’s some unusual setup where the latency of the request is significant, not just the headers and body. Or maybe the process you killed somehow has left an open socket with buffered data on it. Beneath the clean abstractions of software, it’s still the messy real world where anything can happen.

### Prepare for a backlash

Surprisingly, thinking clearly really bothers some people. I think the cause is psychological: if you hate uncertainty, and you’re flailing around trying to find a solution, it’s unpleasant to have someone suggesting that you slow down and sit in the uncertainty for longer. I’ve worked with people who only felt comfortable when they had a theory about why a bug was happening or how to implement something - they found it very hard to be in the position of not knowing the answer.

Can you think clearly by yourself, and then come to others with a fully-formed solution? No, not really. You’ll still have to explain your solution to others or discuss their solution, which will at minimum require thinking clearly about their ideas. There’s no real way around it. My suggestion is to try and work with people who are happy to sit in uncertainty for a while.

If you liked this post, consider[subscribing](https://buttondown.com/seangoedecke)to email updates about my new posts, or[sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/thinking-clearly/&t=Thinking%20clearly%20about%20software). Here's a preview of a related post that shares tags with this one.

> Crushing JIRA tickets is a party trick, not a path to impact
> 
> 
> Don’t be a JIRA ticket zombie! I think a common experience among ambitious juniors - certainly I did this once - is to get frustrated at the slow pace of a team and decide “screw it, I’ll just burn through all these tickets”. On many teams, it’s not that hard to do 2x or 3x more tickets than the next most productive person. But this is a dead end. You’ll get a pat on the head, told “nice work, don’t burn yourself out”, and no progress towards a senior promotion.
> 
> [Continue reading...](https://www.seangoedecke.com/party-tricks/)

* * *