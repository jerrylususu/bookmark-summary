Title: Everything I know about good API design

URL Source: https://www.seangoedecke.com/good-api-design/

Markdown Content:
Most of what modern software engineers do[1](https://www.seangoedecke.com/good-api-design/#fn-1) involves APIs: public interfaces for communicating with a program, like [this one](https://www.twilio.com/docs/iam/api/account#fetch-an-account-resource) from Twilio. I’ve spent a _lot_ of time working with APIs, both building and using them. I’ve written public APIs for third-party developers, private APIs for internal use (or consumption by a single frontend page), REST and GraphQL APIs, and even non-network interfaces like the ones for command-line tools.

Like [designing good software systems](https://www.seangoedecke.com/good-system-design), I think much of the advice floating around about API design is too fancy. People get wrapped up in what “real” REST is, or whether HATEOAS is a good idea, and so on. This post is my attempt at writing down everything I know about designing good APIs.

### Designing APIs is a balance between familiarity and flexibility

If this is true about systems - and it is - it’s even more true about APIs: **good APIs are boring**. An API that’s interesting is a bad API (or at least it would be a better one if it were less interesting). For the developers who build them, APIs are complex products that they spend time designing and polishing. But for the developers who use them, APIs are tools that they use in order to accomplish some other goal. Any time they spend thinking about the API instead of about that goal is time wasted. From their perspective, an ideal API should be so familiar that they will more or less know how to use it before they read any documentation[2](https://www.seangoedecke.com/good-api-design/#fn-2).

However, one big difference from most software systems is that **APIs are hard to change**. Once you publish an API and people start using it, any change to the interface will break your users’ software. Of course, it is _possible_ to make changes. But (as I’ll say below) each change imposes a serious cost: every time you force your users to update their software, they will give serious thought to using a different API that’s more stable. That gives API-builders a strong incentive to design carefully and get it right the first time.

This tension leads to an interesting dynamic for engineers who build APIs. On the one hand, they want to build the simplest API possible. On the other hand, they want to do clever things to maintain flexibility long-term. In broad strokes, API design is about finding a balance between those two incompatible goals.

### WE DO NOT BREAK USERSPACE

What happens when you need to make changes to your API? Additive changes - for instance, putting a new field in the response - are typically fine. There are some consumers which will blow up if they’re getting more fields than they expect, but in my view this is irresponsible. You should expect API consumers to ignore unexpected fields (sensible JSON-parsing typed languages do this by default).

However, you can’t _remove_ or change the types of fields. You can’t change the structure of existing fields (for instance, moving `user.address` to `user.details.address` in the JSON response). If you do, every single piece of code that relies on those fields will immediately break. Consumers of that code will report it as a bug, and the maintainers of the code will (when they figure it out) be rightfully furious that you deliberately broke their software.

The principle here is something like Linus Torvalds’ famous slogan [WE DO NOT BREAK USERSPACE](https://lore.kernel.org/all/CA+55aFy98A+LJK4+GWMcbzaa1zsPBRo76q+ioEjbx-uaMKH6Uw@mail.gmail.com/). As a maintainer of an API, you have something like a sacred duty to avoid harming your downstream consumers. The norm is so strong because so much software depends on so many APIs (which in turn depend on upstream APIs, and so on). One careless API maintainer far enough upstream can break hundreds or thousands of pieces of software downstream.

You should never make a change to an API just because it’d be neater, or because it’s a little awkward. The “referer” header in the HTTP specification is famously a misspelling of the word “referrer”, but they haven’t changed it, _because we do not break userspace_.

### Changing APIs without breaking userspace

It’s honestly hard to think of examples where an API really _needs_ a breaking change. But sometimes the technical value of a change is high enough that you decide to bite the bullet and do it anyway. In those cases, how can you change your API responsibly? The answer is _versioning_.

API versioning means “serve both the old and new version of your API at the same time”. Existing consumers can continue to use the old version, while new consumers can opt-in to the new one. The easiest way to do this is to include something like `/v1/` in your API url. OpenAI’s chat API is at [v1/chat/completions](https://platform.openai.com/docs/api-reference/chat/create), so if they ever want to totally rework the structure, they can do that in `v2/chat/completions` and keep the existing consumers working.

Once you have the new and old version working simultaneously, you can start telling users to upgrade to the new version. This takes a _long_ time: months or even years. Even with banners on the website, docs, custom emails, and headers on the API response, when you finally remove the old version, you will still get a lot of angry users upset that you’ve broken their software. But at least you’ll have done what you can about it.

There are lots of other ways to do API versioning. The Stripe API does versioning in a [header](https://docs.stripe.com/api/versioning), and lets accounts set their default version in the UI. But the principle is the same - any consumers of the Stripe API can be confident that Stripe won’t decide to break their applications, and they can upgrade versions at their own pace.

**I don’t like API versioning.** I think at best it’s a necessary evil, but it’s still evil. It’s confusing to users, who can’t easily search for your API docs without making sure that the version selector matches the version they’re using. And it’s a _nightmare_ for maintainers. If you have thirty API endpoints, every new version you add introduces thirty new endpoints to maintain. You will rapidly end up with hundreds of APIs that all need testing, debugging, and customer support.

Of course, adding a new version doesn’t double the size of your codebase. Any sensible API versioning backend will have something like a translation layer that can turn a response into any of your public API versions. Stripe has [something like this](https://stripe.com/blog/api-versioning): the actual business logic is the same for all versions, so only the parameter serializing and deserializing needs to be aware of versioning. However, abstractions like that will always leak. See this 2017 [HN comment](https://news.ycombinator.com/item?id=13711171) from a Stripe employee, pointing out that some versioning changes need conditional logic throughout the “core code”.

In short, **you should only use API versioning as a last resort**.

### The success of your API depends entirely on the product

An API by itself doesn’t do anything. It’s a layer between the user and the thing they actually want. For the [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create), that’s the ability to do inference with a language model. For the [Twilio API](https://www.twilio.com/docs/iam/api/account#fetch-an-account-resource), that’s sending SMS messages. Nobody uses an API because the API itself is so elegantly designed. They use it to _interact with your product_. **If your product is valuable enough, users will flock to even a terrible API.**

This is why some of the most popular APIs are a nightmare to use. Facebook and Jira are famous for having appalling APIs, but it doesn’t matter - if you want to integrate with Facebook or Jira, which you do, you need to spend the time to figure them out. Sure, it would be nice if those companies had a better API. But why invest the time and money into improving it when people are going to integrate with it anyway? Writing good APIs is _really hard_.

I’m going to give a lot of concrete advice in the rest of this post about how to write good APIs. But it’s worth remembering that most of the time it doesn’t matter. If your product is desirable, any barely-functional API will do; if it isn’t, it doesn’t matter how good your API is. API quality is a marginal feature: it only matters when a consumer is choosing between two basically-equivalent products.

Incidentally, the _presence_ of an API is an entirely different story. If one product doesn’t have an API at all, that’s a big problem. Technical users will demand some way to integrate with the software they’re buying via code.

### Poorly-designed products will usually have bad APIs

A technically-great API can’t save a product that nobody wants to use. However, **a technically-poor product can make it nearly impossible to build an elegant API**. That’s because API design usually tracks the “basic resources” of a product (for instance, Jira’s resources would be [issues](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-issueidorkey-get), [projects](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-projects/#api-rest-api-2-project-projectidorkey-get), [users](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-users/#api-rest-api-2-user-get) and so on). When those resources are set up awkwardly, that makes the API awkward as well.

As an example, consider a blogging system that stored comments in-memory as a linked list (each comment has a `next` field that points to the next comment in the thread). This is a terrible way to store comments. The naive way to bolt a REST API onto this system would be to have an interface that looks like this:

`GET /comments/1 -> { id: 1, body: "...", next_comment_id: 2 }`

Or even worse, like this:

`GET /comments -> {body: "...", next_comment: { body: "...", next_comment: {...}}}`

This might seem like a silly example, because in practice you’d just iterate over the linked list and return an array of comments in the API response. But even if you’re willing to do that extra work, how far down do you iterate? In a thread with thousands of comments, is it just impossible to fetch any comment after the first few hundred? Will your comment-fetching API have to use a background job, forcing the interface to turn into something like:

`POST /comments/fetch_job/1 -> { job_id: 589 }``GET /comments_job/589 -> { status: 'complete', comments: [...] }`

This is how some of the worst APIs happen. Technical constraints that can be cleverly hidden in the UI are laid bare in the API, forcing API consumers to understand far more of the system design than they should reasonably have to.

### Authentication

**You should let people use your APIs with a long-lived API key.** Yes, API keys are not as secure as various forms of short-lived credentials, like OAuth (which you should probably also support). It doesn’t matter. Every integration with your API begins life as a simple script, and using an API key is the easiest way to get a simple script working. You want to make it as easy as possible for engineers to get started.

Although consumers of an API will (almost by definition) be writing code, **many of your users will not be professional engineers**. They may be salespeople, product managers, students, hobbyists, and so on. When you’re an engineer at a tech company building an API, it’s easy to imagine that you’re building it for other people like yourself: full-time, competent, professional software engineers. But you’re not. You’re building it for a very wide cross-section of people, many of whom are not comfortable writing or reading code. If your API requires users to do anything difficult - like performing an OAuth handshake - many of those users will struggle.

### Idempotency and retries

When an API request succeeds, you know it did what it tried to do. What about when it fails? Some types of failure tell you what happened: a 422 typically means it failed during the request-validation stage, before any action was taken[3](https://www.seangoedecke.com/good-api-design/#fn-3). But what about a 500? What about a timeout?

This is important for API operations that _take action_. If you’re hitting some Jira API to create an issue comment, and the request 500s or times out, should you retry? You don’t know for sure whether the comment has been created or not, since the error might be happening after that operation. If you retry, you might end up posting two comments. This is even more important when there’s more at stake than a Jira comment. What if you’re transferring some amount of money? What if you’re dispensing medication?

The solution is _idempotency_, which is a fancy word for “the request should be safely retriable without creating duplicates”. The standard way to do this is to support an “idempotency key” in the request (say, some user-defined string in a parameter or header). When the API server gets a “create comment” request with an idempotency key, it first looks to see if it’s seen this idempotency key before. If so, it does nothing; otherwise it goes and creates the comment, then saves the idempotency key. That way you can send as many retries as you like, as long as they’ve all got the same idempotency key - the operation will only be performed once.

How should you store the key? I’ve seen people store it in some durable, resource-specific way (e.g. as a column on the `comments` table), but I don’t think that’s strictly necessary. The easiest way is to put them in Redis or some similar key/value store (with the idempotency key as the key). UUIDs are unique enough that you don’t need to scope them by user, but you may as well. If you’re not dealing with payments, you can even expire them after a few hours, since most retries happen immediately.

Do you need idempotency keys for every request? Well, you don’t need them for read requests, since double-reads are harmless. You also typically[4](https://www.seangoedecke.com/good-api-design/#fn-4) don’t need them for delete requests, since if you’re deleting by resource ID, that ID serves as the idempotency key. Think about it - if you send three `DELETE comments/32` requests in a row, it won’t delete three comments. The first successful request will delete the comment with ID 32, and the remaining requests will 404 when they can’t find the already-deleted comment.

For most cases, idempotency should be optional. Like I said above, you want to make sure that your API is accessible to non-engineers (who often find idempotency a tricky concept). In the grand scheme of things, getting more people on your API is more important than the occasional duplicated comment from users who didn’t read the documentation.

### Safety and rate limiting

Users who are interacting with your UI are limited by the speed of their hands. If there’s some flow that’s expensive for your backend to serve, a malicious or careless user can only trigger that flow as fast as they can click through it. APIs are different. **Any operation you expose via an API can be called at the speed of code.**

Be careful about APIs that do a lot of work in a single request. When I worked at Zendesk, we had an API that let you fan out notifications to all the users of a particular app. Some enterprising third-party developer[5](https://www.seangoedecke.com/good-api-design/#fn-5) used this to build an in-app chat system, where every message sent a notification to every other user on the account. For accounts with more than a handful of active users, this reliably killed the Apps backend server.

We didn’t anticipate people building a chat app on top of this API. But once it was out there, people did what they wanted with it. I’ve been in many, many incident calls where the root cause was some hand-rolled customer integration that was doing something silly, like:

*   Creating and deleting the same records hundreds of times per-minute, for no real reason
*   Polling a big `/index` endpoint with no delay in between, forever
*   Importing or exporting a ton of data without backing off in case of errors

**You should put a rate limit on your API, with tighter limits for expensive operations.** It’s also sensible to reserve the ability to temporarily disable the API for specific customers, so you can take the pressure off your backend system if it’s really getting hammered.

Include rate limiting metadata in your API responses. `X-Limit-Remaining` and `Retry-After` headers give clients the information they need to be respectful consumers of your API, and allow you to set stricter rate limits than you would otherwise be able to.

### Pagination

Almost every API has to serve a long list of records. Sometimes a very long list (for instance, the Zendesk `/tickets` API can contain millions of tickets). How can you serve those records?

A naive `SELECT * FROM tickets WHERE...` approach will blow out your available memory (if not in the database, then in the application layer where you’re trying to serialize this million-item list). You just can’t serve every ticket in a single request. Instead, you have to _paginate_.

The simplest way to paginate is to use pages (or “offsets”, more generically). When you hit `/tickets`, you get the first ten tickets on the account. To get more, you have to hit either `/tickets?page=2` or `/tickets?offset=20`. This is easy to implement, since the server can just add `OFFSET 20 LIMIT 10` to the end of the database query. But it doesn’t scale to really high numbers of records. Relational databases have to count through your offset every time, so each page you serve gets a little slower than the last page. By the time your offset is in the hundreds of thousands, it’s a real problem.

The solution is “cursor-based pagination”. Instead of passing `offset=20` to get the second page, you take the final ticket on the first page (say, with ID 32) and pass `cursor=32`. The API will then return the next ten tickets, _starting with ticket number 32_. Instead of using `OFFSET`, the query becomes `WHERE id > cursor ORDER BY id LIMIT 10`. That query is equally quick whether you’re at the start of the collection or hundreds of thousands of tickets in, because the database can instantly find the (indexed) position of your cursor ticket instead of having to count through the entire offset.

**You should always use cursor-based pagination for datasets that might end up being large.** Even though it’s harder for consumers to grasp, when you run into scaling problems you might _have_ to change to cursor-based pagination anyway, and the cost of making that change is often very high. However, I think it’s fine to use page or offset-based pagination otherwise.

It’s usually wise to include a `next_page` field in your API list responses. That saves consumers having to figure out the next page number or cursor on their own.

### Optional fields and GraphQL

**If parts of your API response are expensive to serve, make them optional.** For instance, if fetching the user’s subscription status requires your backend to make an API call, consider making your `/users/:id` endpoint not return subscription unless the request passes an `include_subscription` parameter. As a more general approach, you could have an `includes` array parameter with all your optional fields. This is often used for records that are associated (for instance, you could pass `includes: [posts]` to your user request to get the user’s posts in the response).

This is part of the idea behind [GraphQL](https://graphql.org/), a style of API where instead of hitting different endpoints per-operation, you craft a single query with all the data you need and the backend figures it out[6](https://www.seangoedecke.com/good-api-design/#fn-6).

**I don’t like GraphQL very much**, for three reasons. First, it’s completely impenetrable to non-engineers (and to many engineers). Once you learn it, it’s a tool like any other, but the barrier to entry is just so much higher than `GET /users/1`. Second, I don’t like giving users the freedom to craft arbitrary queries. It makes caching more complicated and increases the number of edge cases you have to think about. Third, in my experience the backend implementation is so much more fiddly than your standard REST API.

I don’t feel _that_ strongly about my dislike of GraphQL. I’ve spent maybe six months working with it in various contexts and am far from an expert. I’m sure there are use cases where it buys you enough flexibility to be worth the costs. But right now I’d only use it where I absolutely had to.

### Internal APIs

Everything I’ve said so far is about _public_ APIs. What about internal APIs: APIs that are only used by your colleagues at a particular company? Some of the assumptions I’ve made above don’t hold for internal APIs. For instance, your consumers are usually professional software engineers. It’s also possible to safely make breaking changes, because (a) you often have an order of magnitude fewer users, and (b) you have the ability to go in and ship new code for all of those users. You can require as complex a form of authentication as you want.

However, internal APIs can still be a source of incidents, and still need to be idempotent for key operations.

### Summary

*   APIs are hard to build because they’re inflexible but must be easy to adopt
*   API maintainers’ primary duty is to NOT BREAK USERSPACE. Never make breaking changes to public APIs
*   Versioning your API lets you make changes, but imposes significant implementation and adoption barriers
*   If your product is valuable enough, it doesn’t really matter how good your API is, people will use it anyway
*   If your product is badly-designed enough, it doesn’t matter how carefully you design your API, it will likely suck
*   Your API should support simple API keys for authentication, because many of your users will not be professional engineers
*   Requests that take action (particularly high-stakes action like payments) should include some kind of idempotency key to make retries safe
*   Your API will always be a source of incidents. Make sure you have rate limits and killswitches in place
*   Use cursor-based pagination for datasets that might end up being very large
*   Make expensive fields optional and off-by-default, but (in my opinion) GraphQL is overkill
*   Internal APIs are different in some ways (because your consumers are very different)

What haven’t I written about? I haven’t written much about REST vs SOAP, or JSON vs XML, because I don’t think that stuff is particularly important. I like REST and JSON, but I don’t feel strongly about it. I also haven’t mentioned OpenAPI schema - it’s a useful tool, but I think it’s also fine to just write your API docs in Markdown if you want.

* * *

1.   Well, in my neck of the woods (big tech SaaS).

[↩](https://www.seangoedecke.com/good-api-design/#fnref-1)
2.   This is why [REST](https://document360.com/blog/what-is-rest-api/) is such a common pattern for APIs. It’s not necessarily better than any other way, but at this point it’s familiar enough that consumers can figure it out without ever reading your API documentation.

[↩](https://www.seangoedecke.com/good-api-design/#fnref-2)
3.   Some types of API (like SOAP) will instead respond 200 with a `<Fault>` XML element, but the principle is the same.

[↩](https://www.seangoedecke.com/good-api-design/#fnref-3)
4.   Unless you’ve got some weird non-ID-scoped operation like “delete the most recent record”.

[↩](https://www.seangoedecke.com/good-api-design/#fnref-4)
5.   He was later hired to the Apps team, where I worked with him for several years.

[↩](https://www.seangoedecke.com/good-api-design/#fnref-5)
6.   The other part of the GraphQL idea is to let different backend services serve different parts of a single API, in a way that’s opaque to the API consumer.

[↩](https://www.seangoedecke.com/good-api-design/#fnref-6)