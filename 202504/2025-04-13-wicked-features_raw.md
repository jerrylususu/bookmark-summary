Title: Wicked features

URL Source: https://www.seangoedecke.com/wicked-features/

Markdown Content:
Why is working at large tech companies so hard?[1](https://www.seangoedecke.com/wicked-features/#fn-1)

It’s because a small subset of “wicked features” dominate everything else. If you’re building a todo app, adding the ability to attach images to todo items might be a large feature, but it’s not a wicked feature. However, offering your todo app as a webapp and a standalone executable is a wicked feature. What’s the difference? Wicked features are features that must be considered _every time you build any other feature_.

Here’s some examples of wicked features:

*   Adding a new user type
*   Adding an on-premise version of your SaaS
*   Sharding your customers across many different databases
*   Supporting strong data locality
*   Supporting the ability for customers to move their accounts between regions
*   I18n (translating your customer-facing text into their native language)

Let’s say you’ve done all these, and now you’re building the image-attachment feature. Can the new user type add images? Say you’re storing images in S3 normally - where are images being stored on-premises, where S3 isn’t available? If customer data is sharded, are you sharding your `images` table appropriately as well? Are you making sure that you have a S3 bucket for each user region? If your customer moves their data between regions, do you have an automatic system for shifting the S3 images along with it? Have you pulled out all the new strings involved in image attachment, and have you budgeted the time it’ll take to get them translated?

Why wicked features are hard
----------------------------

Wicked features are like the [Password Game](https://neal.fun/password-game/). In the Password Game, new rules - e.g. “your password must contain its own length as a number”, or “all numbers in your password must sum to 200” - cannot be considered and solved in isolation. They must be solved as a group, because changing the solution to accommodate one rule will often break several others. In fact, the Password Game is very generous by telling you immediately which rules are currently broken and why. In large tech projects, you’ll find out from user tickets or incidents.

This is a common reason for engineers underestimating tasks. It’s easy to forget one or more wicked features that complicate the implementation, and then to get blindsided when someone asks “what about X?” This is particularly true of engineers who haven’t spent much time at the company and might just straight-up not know about some of the wicked features. Company “veterans” are valuable largely because they’re familiar with all the wicked features.

### Are wicked features a skill issue?

Are wicked features just bad design? Couldn’t you factor your program better to satisfy the requirements without adding a wicked feature? Sure, sometimes. I’m sure you could make any feature wicked with a sufficiently-clumsy implementation[2](https://www.seangoedecke.com/wicked-features/#fn-2). But I think some requirements are inherently wicked.

Take “make this SaaS runnable on-premises”. It doesn’t matter how careful you are. Even if you make sure your SaaS build pipeline is completely on-prem friendly so you never have to maintain two versions, the fact that you have to be careful to do that is itself a wicked feature that you have to keep in mind for all future changes to the build pipeline.

Or take “add a new user type that can do X but not Y”. Suppose you do a great job refactoring out user abilities so you never have to do `isUserTypeX(user)`. The fact that new capabilities have to fit your homemade user ability framework is itself a wicked feature.

What’s wicked about these features isn’t the implementation, but the fundamental domain model. It’s wicked at the level of the user-flow diagram. No matter how well-factored your code is, you must still answer the questions I listed above (e.g. “can every user type access this new capability I’m building?“)

### Why build wicked features?

If companies could avoid building wicked features, they would. The problem is that the highest-paying users _love_ wicked features. On-premise SaaS offerings are typically extremely profitable, since they appeal to a segment of users that are doing very well financially and who are comfortable paying high enterprise software contract prices (instead of low SaaS subscription prices). Likewise, data locality and sharding also appeal to enterprise customers with deep pockets.

Other wicked features are built by lazy or incompetent developers. For instance, companies with five users who nevertheless have built out a full sharding system for their data because it sounded like fun to the engineer in question. I’ve also seen engineers try to build wicked features because they couldn’t see another way of doing things (or just felt that it was the “right” way to go about it). Extracting all user-facing strings for an app that only supports one language is a classic low-stakes example.

One of the most valuable things you can do as an engineer is to prevent your team from building wicked features where possible, and to limit the damage where the wicked feature must be built: by sensible factoring with an eye to “how will this affect developers trying to build completely unrelated features in the same system?”

### Summary

*   Wicked features are requirements that must be considered every time you build anything else
*   They massively increase implementation complexity and coordination cost
*   Some wicked features are unavoidable, especially when selling to high-paying enterprise users
*   Others are self-inflicted by overengineering, dogma, or poor taste
*   Good engineers limit the blast radius: they prevent unnecessary wicked features, and factor the necessary ones so they don’t pollute everything

* * *

1.  If you’re already answering “it isn’t”, remember how George Hotz (a clearly technically-strong engineer) joined Twitter in 2022 and [failed to fix](https://news.ycombinator.com/item?id=33723257) search. More generally, think of the hundreds of strong startup engineers who are acqui-hired into large tech companies and then struggle to be productive. Of course, it’s possible that you’re built different.
    
    [↩](https://www.seangoedecke.com/wicked-features/#fnref-1)
2.  Maybe you implement image attachments by reusing the normal todo-adding APIs with a bunch of flags to like `isAttachmentRequest`, so any future development on those APIs has to think about whether they’re currently handling an attachment or not.
    
    [↩](https://www.seangoedecke.com/wicked-features/#fnref-2)
