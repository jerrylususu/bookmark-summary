Title: Designing software that could possibly work

URL Source: https://www.seangoedecke.com/planning-software/

Markdown Content:
Whenever anyone describes a piece of software to me, I think about how I would build it. Software engineers do this a lot, but many of them don’t do it very well. I know that because I see a lot of technical discussions about specific details in a general plan _that could not possibly work_. For instance, arguing about whether to use prop-drilling or context-passing to supply a piece of data to the frontend that we do not and will never have access to, or the exact persistent-data-storage strategy to implement in a backend service that must remain stateless.

To avoid this, I think it’s a good idea to **trace one important user flow end-to-end in your head**. What does that mean in practice?

### Two common anti-patterns

The first mistake I see a lot is staying too high-level. Suppose you’re building a comments system for a blog. Some engineers will stop at “oh, I’d put the comments in a relational database somewhere and pull them out to put on the page”. A relational database might end up being the right choice, but this level of design isn’t very useful for actually building the feature. You need to go one level deeper: how are the comments traveling from the user’s browser to the relational database?

The second mistake is getting too invested in the wrong specifics. Some engineers will begin designing their commenting system by saying “oh cool, I’ll use React”, and then diving into a million micro-decisions about whether to use RSC or not, or whether to fetch the data via fetch or TSQ, or to expose the comment data in GraphQL, and so on. The first time you hear about the problem is the wrong time to make decisions like these. You may have to make them eventually, but not at the outset.

### How to do it right

So what is the right way to do it? The right way is to take the **most important user flow** and trace the simplest possible implementation **all the way through** in your head. You can track only one user flow because otherwise you’ll get confused[1](https://www.seangoedecke.com/planning-software/#fn-1). You have to trace the implementation all the way through because otherwise you’ll miss key details. When I say “trace”, I mean at the level of pseudocode. You don’t have to imagine the entire code in your head, but you do have to imagine each logical step.

This is the mental equivalent of the Pragmatic Programmer’s well-known “tracer bullet” [rule](https://wiki.c2.com/?TracerBullets). The tracer bullet rule is that your first prototype should be the minimum you need to build to get one user flow working end-to-end[2](https://www.seangoedecke.com/planning-software/#fn-2). The same is true for simply thinking about writing software: your goal should be to think one user flow through end-to-end.

The benefit of thinking through the flow at that level of detail is that you’re forced to confront the important questions (just as you would be if you were building a prototype with real code). You don’t have to design the cleanest or the best solution here, but you do need to design _something that could possibly work_. If you start with something that works, you can usually iterate to something _good_ that works. If you start with something that doesn’t work, it’s much harder to iterate your way back into [the space of working solutions](https://www.seangoedecke.com/solution-space).

### Walking through an example

For instance, in the case of implementing a commenting system:

A user lands on one of my blog posts and should see a enter-your-comment form. That’s easily done by adding a `<form>` element to my post template.

When they submit the form, their comment should be stored somewhere. Okay, so I need an endpoint on my backend and some kind of data storage. My add-a-comment endpoint code will be something like this:

```
comment = params['comment_body']
post = params['post_id']
user = ???

Comment.new(comment: comment, post: post, user: user).save!

redirect_to(post)
```

How can I set the user for the comment? If people are commenting anonymously, the solution is simple (add an optional form field for `name`), but otherwise I need to support some kind of login on my previously-static site. This endpoint can be pretty slow. Users will submit comments much less often than they view pages, and it’s no big deal if it takes a second.

After the redirect, the user should then be able to view their comment. That means that I need some logic on the post page like this:

```
comments = Comment.where(post: current_post)
render(post, comments: comments)
```

And then some HTML templating on the post page that renders each comment. This endpoint must be very fast. Viewing posts is the main user activity on the site, and adding a few hundred ms of latency will meaningfully impact the experience. That points to the potential for caching or deferred loading, and the necessity for pagination once the number of comments grows.

Even with a simple example like this, you can see how it turns up what infrastructure pieces I’m missing (the ability to run code on the backend, data storage), and what questions I need to answer (how can users log in or set their identity). When you do this for a system in a large tech company, you often turn up interesting questions as well:

*   Our system needs data X, but it’s only available from a slow endpoint in service Y
*   Our system needs data that we don’t currently collect (e.g. my static blog doesn’t collect data about user identity)
*   We need to display new comments on each post, but the posts are currently long-term cached on a CDN, so we’ll need to find a way to bust that cache for each new comment
*   We need to account for one or more [wicked features](https://www.seangoedecke.com/wicked-features) - for instance, if someone’s running the on-premise version of the blog, we’ll need to figure out where we can store comments (or hide/disable the comment form)

Note that these points are all largely agnostic about what specific technologies are chosen (Rails or Express for the backend, MySQL or MongoDB for the data storage, etc). The assumptions they make are general ones that flow directly from the requirements: no matter what, comments will have to be stored _somewhere_ and associated with users _somehow_.

### How to communicate about a mental plan

The plan you make should stay mostly in your mind. In my experience, you will not be able to usefully explain it to product managers or even other engineers. The value of the plan is in how it helps you **estimate** and **ask questions**. For instance, the hardest part about adding comments to my blog would be switching to an infrastructure that isn’t entirely static (and thus allows me to store data and run my own code in user requests). Estimating that part of work would give a rough guide for the entire project, and the questions involved (e.g. what platform should I switch my blog to, or should I use a third-party-hosted comments service) will be the most important questions involved in planning the project.

Once the initial conversation is over, it can be very useful to write your plan down. I like a loose boxes-and-lines structure, usually in a Mermaid diagram, but it doesn’t really matter how you do this. A short paragraph of text is probably good enough. A written version of a plan can be a good starting point for getting into more concrete implementation details. If everyone on the team[3](https://www.seangoedecke.com/planning-software/#fn-3) agrees that the comments should be managed by a stateful backend app, then we can start talking about what technologies we should use and how.

I think this approach still works if you have a more explicit design process on your team (e.g. a collaborative design meeting, or some kind of architect-driven thing). You’re much more likely to be successful at those processes if you go in with a concrete idea about how the feature could work. One caveat: **don’t get too attached to that idea**. You should remain open to drastically changing the plan, as long as it’s to something else that could also work. The first rough idea you came up with in your head is unlikely to be the best option overall.

### Summary

This is the kind of post that feels almost too obvious to write down - when you’re planning work, of course you should think about how the system could possibly function. But I think many engineers underestimate the difficulty of getting anything to work at all, and so handwave away the concrete details that they should be paying the most attention to.

If you instead jump into those concrete details immediately - what data is available, where it needs to get to, and how it’s going to get there - you’re likely to waste much less time arguing about implementation details of a strategy that never could have worked in the first place.

* * *

1.  Well, maybe you’re built different and you can track multiple - I can only track one. Even then I suspect you’re better off sticking with one and using that extra brainpower on tracing the implementation.
    
    [↩](https://www.seangoedecke.com/planning-software/#fnref-1)
2.  It’s called the “tracer bullet” rule after real-life tracer bullets, which make it much easier for machine gunners to aim at night. Instead of having to calculate where the bullet will go first try, they can start shooting and adjust based on where the arc of incandescent bullets is landing.
    
    [↩](https://www.seangoedecke.com/planning-software/#fnref-2)
3.  If it’s just me, then substitute “if I’m convinced” here.
    
    [↩](https://www.seangoedecke.com/planning-software/#fnref-3)
