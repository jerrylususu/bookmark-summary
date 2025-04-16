Title: JSX Over The Wire — overreacted

URL Source: https://overreacted.io/jsx-over-the-wire/

Markdown Content:
Suppose you have an API route that returns some data as JSON:

```
app.get('/api/likes/:postId', async (req, res) => {
  const postId = req.params.postId;
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  const json = {
    totalLikeCount: post.totalLikeCount,
    isLikedByUser: post.isLikedByUser,
    friendLikes: friendLikes,
  };
  res.json(json);
});
```

You also have a React component that needs that data:

```
function LikeButton({
  totalLikeCount,
  isLikedByUser,
  friendLikes
}) {
  let buttonText = 'Like';
  if (totalLikeCount > 0) {
    // e.g. "Liked by You, Alice, and 13 others"
    buttonText = formatLikeText(totalLikeCount, isLikedByUser, friendLikes);
  }
  return (
    <button className={isLikedByUser ? 'liked' : ''}>
      {buttonText}
    </button>
  );
}
```

How do you get that data into that component?

You could pass it from a parent component using some data fetching library:

```
function PostLikeButton({ postId }) {
  const [json, isLoading] = useData(`/api/likes/${postId}`);
  // ...
  return (
    <LikeButton
      totalLikeCount={json.totalLikeCount}
      isLikedByUser={json.isLikedByUser}
      friendLikes={json.friendLikes}
    />
  );
}
```

That’s one way of thinking about it.

But have another look at your API:

```
app.get('/api/likes/:postId', async (req, res) => {
  const postId = req.params.postId;
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  const json = {
    totalLikeCount: post.totalLikeCount,
    isLikedByUser: post.isLikedByUser,
    friendLikes: friendLikes,
  };
  res.json(json);
});
```

Do these lines remind you of anything?

Props. _You’re passing props._ You just didn’t specify _where to_.

But you already know their final destination—`LikeButton`.

Why not just fill that in?

```
app.get('/api/likes/:postId', async (req, res) => {
  const postId = req.params.postId;
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  const json = (
    <LikeButton
      totalLikeCount={post.totalLikeCount}
      isLikedByUser={post.isLikedByUser}
      friendLikes={friendLikes}
    />
  );
  res.json(json);
});
```

Now the “parent component” of `LikeButton` is the _API itself_.

Wait, what?

Weird, I know. We’re going to worry about whether it’s a good idea later. But for now, notice how this inverts the relationship between components and the API. This is sometimes known as the Hollywood Principle: “Don’t call me, I’ll call you.”

Your components don’t call your API.

Instead, your API _returns_ your components.

Why would you ever want to do that?

* * *

*   [Part 1: JSON as Components](https://overreacted.io/jsx-over-the-wire/#part-1-json-as-components)
*   [Part 2: Components as JSON](https://overreacted.io/jsx-over-the-wire/#part-2-components-as-json)
*   [Part 3: JSX Over The Wire](https://overreacted.io/jsx-over-the-wire/#part-3-jsx-over-the-wire)

* * *

[Part 1: JSON as Components](https://overreacted.io/jsx-over-the-wire/#part-1-json-as-components)
-------------------------------------------------------------------------------------------------

### [Model, View, ViewModel](https://overreacted.io/jsx-over-the-wire/#model-view-viewmodel)

There is a fundamental tension between how we want to _store_ information and how we want to _display_ it. We generally want to store more things than we display.

For example, consider a Like button on a Post. When we store Likes for a given Post, we might want to represent them as a table of `Like` rows like this:

```
type Like = {
  createdAt: string, // Timestamp
  likedById: number, // User ID
  postId: number     // Post ID
};
```

Let’s call this kind of data a “Model”. It represents the raw shape of the data.

```
type Model = Like;
```

So our Likes database table might contain data of that shape:

```
[{
  createdAt: '2025-04-13T02:04:41.668Z',
  likedById: 123,
  postId: 1001
}, {
  createdAt: '2025-04-13T02:04:42.668Z',
  likedById: 456,
  postId: 1001
}, {
  createdAt: '2025-04-13T02:04:43.668Z',
  likedById: 789,
  postId: 1002
}, /* ... */]
```

However, what we want to _display_ to the user is different.

What we want to display is the _number of Likes_ for that Post, whether the _user has already liked it_, and the names of _their friends who also liked it_. For example, the Like button could appear pressed in (which means that you already liked this post) and say “You, Alice, and 13 others liked this.” Or “Alice, Bob, and 12 others liked this.”

```
type LikeButtonProps = {
  totalLikeCount: number,
  isLikedByUser: boolean,
  friendLikes: string[]
}
```

Let’s call this kind of data a “ViewModel”.

```
type ViewModel = LikeButtonProps;
```

A ViewModel represents data in a way that is directly consumable by the UI (i.e the _view_). It is often significantly different from the raw Model. In our example:

*   ViewModel’s `totalLikeCount` is aggregated from individual `Like` models.
*   ViewModel’s `isLikedByUser` is personalized and depends on the user.
*   ViewModel’s `friendLikes` is both aggregated and personalized. To calculate it, you’d have to takes the Likes for this post, filter them down to likes from friends, and get the first few friends’ names (which are likely stored in a different table).

Clearly, Models will need to turn into ViewModels at some point. The question is _where_ and _when_ this happens in the code, and how that code evolves over time.

* * *

### [REST and JSON API](https://overreacted.io/jsx-over-the-wire/#rest-and-json-api)

The most common way to solve this problem is to expose some kind of a JSON API that the client can hit to assemble the ViewModel. There are different ways to design such an API, but the most common way is what’s usually known as REST.

The typical way to approach REST ([let’s say we’ve never read this article](https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/)) is to pick some “Resources”—such as a Post, or a Like—and provide JSON API endpoints that list, create, update, and delete such Resources. Naturally, REST does not specify anything about how you should _shape_ these Resources so there’s a lot of flexibility.

Often, you might start by returning the shape of the Model:

```
// GET /api/post/123
{
  title: 'My Post',
  content: 'Hello world...',
  authorId: 123,
  createdAt: '2025-04-13T02:04:40.668Z'
}
```

So far so good. But how would you incorporate Likes into this? Maybe `totalLikeCount` and `isLikedByUser` could be a part of the Post Resource:

```
// GET /api/post/123
{
  title: 'My Post',
  content: 'Hello world...',
  authorId: 123,
  createdAt: '2025-04-13T02:04:40.668Z',
  totalLikeCount: 13,
  isLikedByUser: true
}
```

Now, should `friendLikes` also go there? We need this information on the client.

```
// GET /api/post/123
{
  title: 'My Post',
  authorId: 123,
  content: 'Hello world...',
  createdAt: '2025-04-13T02:04:40.668Z',
  totalLikeCount: 13,
  isLikedByUser: true,
  friendLikes: ['Alice', 'Bob']
}
```

Or are we starting to abuse the notion of a Post by adding too much stuff to it? Okay, how about this, maybe we could offer a separate endpoint for a Post’s Likes:

```
// GET /api/post/123/likes
{
  totalCount: 13,
  likes: [{
    createdAt: '2025-04-13T02:04:41.668Z',
    likedById: 123,
  }, {
    createdAt: '2025-04-13T02:04:42.668Z',
    likedById: 768,
  }, /* ... */]
}
```

So a Post’s Like becomes its own “Resource”.

That’s nice in theory but we’re going to need to know the likers’ names, and we don’t want to make a request for each Like. So we need to “expand” the users here:

```
// GET /api/post/123/likes
{
  totalCount: 13,
  likes: [{
    createdAt: '2025-04-13T02:04:41.668Z',
    likedBy: {
      id: 123,
      firstName: 'Alice',
      lastName: 'Lovelace'
    }
  }, {
    createdAt: '2025-04-13T02:04:42.668Z',
    likedBy: {
      id: 768,
      firstName: 'Bob',
      lastName: 'Babbage'
    }
  }]
}
```

We also “forgot” which of these Likes are from friends. Should we solve this by having a separate `/api/post/123/friend-likes` endpoint? Or should we order by friends first and include `isFriend` into the `likes` array items so we can disambiguate friends from other likes? Or should we add `?filter=friends`?

Or should we include the friend likes directly into the Post to avoid two API calls?

```
// GET /api/post/123
{
  title: 'My Post',
  authorId: 123,
  content: 'Hello world...',
  createdAt: '2025-04-13T02:04:40.668Z',
  totalLikeCount: 13,
  isLikedByUser: true,
  friendLikes: [{
    createdAt: '2025-04-13T02:04:41.668Z',
    likedBy: {
      id: 123,
      firstName: 'Alice',
      lastName: 'Lovelace'
    }
  }, {
    createdAt: '2025-04-13T02:04:42.668Z',
    likedBy: {
      id: 768,
      firstName: 'Bob',
      lastName: 'Babbage'
    }
  }]
}
```

This seems useful but what if `/api/post/123` gets called from other screens that don’t need this information—and you’d rather not slow them down? Maybe there could be an opt-in like `/api/post/123?expand=friendLikes`?

Anyway, the point I’m trying to make here is not that it’s _impossible_ to design a good REST API. The vast majority of apps I’ve seen works this way so it’s at the very least doable. But anyone who designed one and then worked on it for more than a few months knows the drill. _Evolving REST endpoints is a pain in the ass._

It usually goes like this:

1.  Initially, you have to decide how to structure the JSON output. None of the options are _clearly better_ than the rest; mostly you’re just guessing how the app will evolve.
2.  The initial decisions tend to settle down after a few back-and-forth iterations… until the next UI redesign which causes ViewModels to have slightly different shapes. The already existing REST endpoints don’t quite cover the new needs.
3.  It’s possible to add new REST API endpoints, but at some point you’re not really “supposed to” add more because you already defined all the possible Resources. For example, if `/posts/123` exists, you likely won’t add another “get post” API.
4.  Now you’re running into issues with calculating and sending either _not enough_ or _too much_ data. You either aggressively “expand” fields in the existing Resources or come up with an elaborate set of conventions for doing it on-demand.
5.  Some ViewModels are only needed by a subset of screens but they’re always included in the response because that’s easier than making them configurable.
6.  Some screens resort to cobbling their ViewModels together from multiple API calls because no single response contains all the necessary information anymore.
7.  Then the design and the functionality of your product changes again. _Repeat._

There’s clearly some fundamental tension here, but what is causing it?

First, note how the shape of the ViewModels is determined by the UI. It’s not a reflection of some platonic idea of a Like; rather, it’s dictated by the design. We want to show “You, Ann, and 13 others liked this”, _therefore_ we need these fields:

```
type LikeButtonProps = {
  totalLikeCount: number,
  isLikedByUser: boolean,
  friendLikes: string[]
}
```

If this screen’s design or functionality changes (for example, if you want to show the avatars of your friends who liked the post), the ViewModel will change as well:

```
type LikeButtonProps = {
  totalLikeCount: number,
  isLikedByUser: boolean,
  friendLikes: {
    firstName: string
    avatar: string
  }[]
}
```

But here’s the rub.

REST (or, rather, how REST is broadly used) encourages you to think in terms of Resources rather than Models _or_ ViewModels. At first, your Resources start out as mirroring Models. But a single Model rarely has enough data for a screen, so you develop ad-hoc conventions for nesting Models in a Resource. However, including _all_ the relevant Models (e.g. all Likes of a Post) is often impossible or impractical, so you start adding ViewModel-ish fields like `friendLikes` to your Resources.

But putting ViewModels in Resources also doesn’t work very well. ViewModels are not abstract concepts like “a post”; each ViewModel describes a _specific piece of UI_. As a result, the shape of your “Post” Resource grows to encompass the needs of every screen displaying a post. But those needs also _change over time,_ so the “Post” Resource’s shape is at best a compromise between what different screens need now, and at worst a fossilized record of everything they’ve ever needed in the past.

Let me put this more bluntly:

**REST Resources don’t have a firm grounding in the reality.** Their shapes are not sufficiently constrained—we’re making up concepts mostly out of thin air. Unlike Models, they’re not grounded in the reality of how the data is stored. And unlike ViewModels, they’re not grounded in the reality of how the data is presented. Unfortunately, nudging them in either direction only makes things worse.

If you keep REST Resources close to the Models, you’ll hurt the user experience. Now things that could be fetched in a single request would require a couple or, god forbid, N calls. This is especially noticeable in products from companies where the backend team “hands off” a REST API to the frontend team and takes no feedback. The API may look simple and elegant but it is completely impractical to consume.

On the other hand, if you nudge REST Resources to stay closer to the ViewModels, you’re hurting maintainability. ViewModels are fickle! Most ViewModels are going to change the next time the corresponding piece of UI is redesigned. But changing the shape of REST Resources is hard—the same Resources are being fetched by many screens. As a result, their shape gradually drifts away from the needs of the current ViewModels, and becomes difficult to evolve. There’s a reason the backend teams often resist adding UI-specific fields to the response: they’ll likely get stale!

This doesn’t necessarily mean that REST itself, as it’s broadly understood, is broken. It can be very nice to use when the Resources are well-defined and their fields are well-chosen. But this often goes against the client’s needs, which is to get all the data _for a particular screen_. There’s something missing in the middle.

We need a translation layer.

* * *

### [API for ViewModels](https://overreacted.io/jsx-over-the-wire/#api-for-viewmodels)

There is a way to resolve this tension.

You have some latitude with how exactly you could approach it but the main idea is that your client should be able to request _all data for a specific screen at once_.

It’s such a simple idea!

Instead of requesting “canonical” REST Resources from the client such as:

```
GET /data/post/123       # Get Post Resource
GET /data/post/123/likes # Get Post Likes Resource
```

you request a ViewModel for _a specific screen_ (i.e. a route):

```
GET /screens/post-details/123 # Get ViewModel for the PostDetails screen
```

This data would include _everything_ that screen needs.

The difference is subtle but profound. You’re no longer trying to define a universal canonical shape of a _Post_. Rather, you send whatever data the _PostDetails screen_ needs in order to display its components _today_. If the PostDetails screen gets deleted, this endpoint gets deleted too. If a different screen wants to display some related information (for example, a PostLikedBy popup), it will gets its own route:

```
GET /screens/post-details/123 # Get ViewModel for the PostDetails screen
GET /screens/post-liked-by/123 # Get ViewModel for the PostLikedBy screen
```

Okay, but how does this help?

This avoids the trap of “ungrounded” abstraction. The ViewModel interface for every screen precisely specifies the shape of the server response. If you need to change it or fine-tune it, you can do that without affecting any other screens.

For example, a `PostDetails` screen ViewModel might look like this:

```
type PostDetailsViewModel = {
  postTitle: string,
  postContent: string,
  postAuthor: {
    name: string,
    avatar: string,
    id: number
  },
  friendLikes: {
    totalLikeCount: number,
    isLikedByUser: boolean,
    friendLikes: string[]
  }
};
```

So that’s what the server would return for `/screens/post-details/123`. Later, if you want to display avatars of friend likes, you’d just add it to _that_ ViewModel:

```
type PostDetailsViewModel = {
  postTitle: string,
  postContent: string,
  postAuthor: {
    name: string,
    avatar: string,
    id: number
  },
  friendLikes: {
    totalLikeCount: number,
    isLikedByUser: boolean,
    friendLikes: {
      firstName: string
      avatar: string
    }[]
  }
}
```

Note that you’d only have to update _that screen’s endpoint_. You’re no longer forced to balance what one screen needs with what another screen needs. There are no questions like “which Resource does this field belong to?”, or whether it should be “expanded”. If some screen needs more data than others, you can just include more data in _that_ screen’s response—it doesn’t have to be generic or configurable. **The shape of the server response is exactly determined by each screen’s needs.**

This _does_ solve the stated problems with REST.

It also introduces a few novel questions:

1.  There’s going to be _a lot_ more endpoints than with REST Resources—an endpoint per screen. How will these endpoints be structured and kept maintainable?
2.  How do you reuse code between the endpoints? Presumably there would be a lot of duplicated data access and other business logic between those endpoints.
3.  How do you convince the backend team to pivot from their REST APIs to this?

The last question is probably the first we need to resolve. The backend team will likely have very warranted reservations about this approach. At the very least, if this approach proves terrible, it would be good to have a way to migrate back.

Luckily, there’s no need to throw anything away.

* * *

### [Backend For Frontend](https://overreacted.io/jsx-over-the-wire/#backend-for-frontend)

Instead or _replacing_ your existing REST API, you can add a new _layer_ in front of it:

```
// You're adding new screen-specific endpoints...
app.get('/screen/post-details/:postId', async (req, res) => {
  const [post, friendLikes] = await Promise.all([
    // ...which call your existing REST API here
    fetch(`/api/post/${postId}`).then(r => r.json()),
    fetch(`/api/post/${postId}/friend-likes`).then(r => r.json()),
  ]);
  const viewModel = {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes: {
      totalLikeCount: post.totalLikeCount,
      isLikedByUser: post.isLikedByUser,
      friendLikes: friendLikes.likes.map(l => l.firstName)
    }
  };
  res.json(viewModel);
});
```

This is not a new idea. Such a layer is often called BFF, or _Backend for Frontend._ In this case, the job of the BFF is to adapt your REST API to returning ViewModels.

**If some screen needs more data, a BFF lets you serve more data to it without changing your entire data model. It keeps screen-specific changes scoped. Crucially, it lets you deliver all the data any screen needs in a single roundtrip.**

The BFF doesn’t have to be written in the same language as your REST API. For reasons we’ll get into later, it’s advantageous to write BFF in the same language as your frontend code. You can think of it as _a piece of the frontend that happens to run on the server_. It’s like the frontend’s “ambassador” to the server. It “adapts” the REST responses into the shape that each screen of the frontend UI actually wants.

Although you can get some of the benefits of BFF with client-only per-route loaders like [`clientLoader` in React Router](https://reactrouter.com/start/framework/data-loading#client-data-loading), there’s a lot you unlock by actually deploying this layer on the server close to where the REST endpoints are deployed.

For example, even if you _do_ have to make several REST API requests serially one after another to load all the necessary data for a screen, the latency between the BFF and your REST API would be much lower than when making multiple serial requests from the client. If your REST API responses are fast on the internal network, you can cut down literal seconds of what used to be client/sever waterfalls without actually parallelizing the (sometimes inevitable) serial calls.

A BFF also lets you apply data transformations _before_ sending data to the client, which can significantly improve performance on low-end client devices. You can even go as far as to cache or persist some computations on the disk, even _between_ different users, since you have access to the disk—and to server caches like Redis. In that sense, a BFF lets a frontend team have _their very own little slice of the server_.

Importantly, a BFF gives you a way to experiment with alternatives to your REST APIs without affecting the client application. For example, if your REST API has no other consumers, you can turn it into an internal microservice and avoid exposing it to the world. Moreover, you could turn it into a _data access layer_ rather than an HTTP service, and simply _import_ that data access layer in-process from your BFF:

```
import { getPost, getFriendLikes } from '@your-company/data-layer';
 
app.get('/screen/post-details/:postId', async (req, res) => {
  const postId = req.params.postId;
  const [post, friendLikes] = await Promise.all([
    // Reads from an ORM and applies business logic.
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  const viewModel = {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes: {
      totalLikeCount: post.totalLikeCount,
      isLikedByUser: post.isLikedByUser,
      friendLikes: friendLikes.likes.map(l => l.firstName)
    }
  };
  res.json(viewModel);
});
```

(Of course, this part only works if you can write lower-level backend logic in JS.)

This can help you avoid problems like loading the same information many times from the database (no `fetch` calls means database reads can be batched). It also lets you “drop down” the abstraction level when needed—for example, to run a fine-tuned stored database procedure that isn’t neatly exposed over the REST API.

There’s a lot to like about the BFF pattern. It solves quite a few problems but it also raises new questions. For example, how do you organize its code? If each screen is essentially its own API method, how do you avoid duplication of code? And how do you keep your BFF synchronized with data requirements of the front-end side?

Let’s try to make some progress on answering those.

* * *

### [Composable BFF](https://overreacted.io/jsx-over-the-wire/#composable-bff)

Suppose you’re adding a new `PostList` screen. It’s going to render _an array_ of `<PostDetails>` components, each of which needs the same data as before:

```
type PostDetailsViewModel = {
  postTitle: string,
  postContent: string,
  postAuthor: {
    name: string,
    avatar: string,
    id: number
  },
  friendLikes: {
    totalLikeCount: number,
    isLikedByUser: boolean,
    friendLikes: string[]
  }
};
```

So the ViewModel for `PostList` contains an array of `PostDetailsViewModel`:

```
type PostListViewModel = {
  posts: PostDetailsViewModel[]
};
```

How would you load the data for `PostList`?

Your first inclination may be to make a series of requests from the client to the existing `/screen/post-details/:postId` endpoint which already knows how to prepare a ViewModel for a single post. We just need to call it for every post.

But wait, this defeats the entire purpose of the BFF! Making many requests for a single screen is inefficient and is precisely the kind of compromise that we’ve been trying to avoid. **Instead, we’ll add a new BFF endpoint for the new screen.**

The new endpoint might initially look like this:

```
import { getPost, getFriendLikes, getRecentPostIds } from '@your-company/data-layer';
 
app.get('/screen/post-details/:postId', async (req, res) => {
  const postId = req.params.postId;
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  const viewModel = {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes: {
      totalLikeCount: post.totalLikeCount,
      isLikedByUser: post.isLikedByUser,
      friendLikes: friendLikes.likes.map(l => l.firstName)
    }
  };
  res.json(viewModel);
});
 
app.get('/screen/post-list', async (req, res) => {
  // Grab the recent post IDs
  const postIds = await getRecentPostIds();
  const viewModel = {
    // For each post ID, load the data in parallel
    posts: await Promise.all(postIds.map(async postId => {
      const [post, friendLikes] = await Promise.all([
        getPost(postId),
        getFriendLikes(postId, { limit: 2 }),
      ]);
      const postDetailsViewModel = {
        postTitle: post.title,
        postContent: parseMarkdown(post.content),
        postAuthor: post.author,
        postLikes: {
          totalLikeCount: post.totalLikeCount,
          isLikedByUser: post.isLikedByUser,
          friendLikes: friendLikes.likes.map(l => l.firstName)
        }
      };
      return postDetailsViewModel;
    }))
  };
  res.json(viewModel);
});
```

However, note that there’s significant code duplication between the endpoints:

```
import { getPost, getFriendLikes, getRecentPostIds } from '@your-company/data-layer';
 
app.get('/screen/post-details/:postId', async (req, res) => {
  const postId = req.params.postId;
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  const viewModel = {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes: {
      totalLikeCount: post.totalLikeCount,
      isLikedByUser: post.isLikedByUser,
      friendLikes: friendLikes.likes.map(l => l.firstName)
    }
  };
  res.json(viewModel);
});
 
app.get('/screen/post-list', async (req, res) => {
  const postIds = await getRecentPostIds();
  const viewModel = {
    posts: await Promise.all(postIds.map(async postId => {
      const [post, friendLikes] = await Promise.all([
        getPost(postId),
        getFriendLikes(postId, { limit: 2 }),
      ]);
      const postDetailsViewModel = {
        postTitle: post.title,
        postAuthor: post.author,
        postContent: parseMarkdown(post.content),
        postLikes: {
          totalLikeCount: post.totalLikeCount,
          isLikedByUser: post.isLikedByUser,
          friendLikes: friendLikes.likes.map(l => l.firstName)
        }
      };
      return postDetailsViewModel;
    }))
  };
  res.json(viewModel);
});
```

It’s almost like there is a notion of “`PostDetails` ViewModel” begging to be extracted. This should not be surprising—both screens render the same `<PostDetails>` component, so they need similar code to load the data for it.

* * *

Let’s extract a `PostDetailsViewModel` function:

```
import { getPost, getFriendLikes, getRecentPostIds } from '@your-company/data-layer';
 
async function PostDetailsViewModel({ postId }) {
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  return {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes: {
      totalLikeCount: post.totalLikeCount,
      isLikedByUser: post.isLikedByUser,
      friendLikes: friendLikes.likes.map(l => l.firstName)
    }
  };
}
 
app.get('/screen/post-details/:postId', async (req, res) => {
  const postId = req.params.postId;
  const viewModel = await PostDetailsViewModel({ postId });
  res.json(viewModel);
});
 
app.get('/screen/post-list', async (req, res) => {
  const postIds = await getRecentPostIds();
  const viewModel = {
    posts: await Promise.all(postIds.map(postId =>
      PostDetailsViewModel({ postId })
    ))
  };
  res.json(viewModel);
});
```

This makes our BFF endpoints significantly simpler.

In fact, we can go a bit further. Look at this part of `PostDetailsViewModel`:

```
async function PostDetailsViewModel({ postId }) {
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  return {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes: {
      totalLikeCount: post.totalLikeCount,
      isLikedByUser: post.isLikedByUser,
      friendLikes: friendLikes.likes.map(l => l.firstName)
    }
  };
}
```

We know that the purpose of the `postLikes` field is to eventually become props for the `LikeButton` component—i.e. this field is `LikeButton`’s ViewModel:

```
function LikeButton({
  totalLikeCount,
  isLikedByUser,
  friendLikes
}) {
  // ...
}
```

So let’s extract the logic preparing these props into `LikeButtonViewModel`:

```
import { getPost, getFriendLikes, getRecentPostIds } from '@your-company/data-layer';
 
async function LikeButtonViewModel({ postId }) {
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  return {
    totalLikeCount: post.totalLikeCount,
    isLikedByUser: post.isLikedByUser,
    friendLikes: friendLikes.likes.map(l => l.firstName)
  };
}
 
async function PostDetailsViewModel({ postId }) {
  const [post, postLikes] = await Promise.all([
    getPost(postId), // It's fine to getPost() here again. Our data layer deduplicates calls via an in-memory cache.
    LikeButtonViewModel({ postId }),
  ]);
  return {
    postTitle: post.title,
    postContent: parseMarkdown(post.content),
    postAuthor: post.author,
    postLikes
  };
}
```

Now we have a tree of functions that load data as JSON—our ViewModels.

Depending on your background, this might remind you of a few other things. It might remind you of composing Redux reducers out of smaller reducers. It might also remind you of composing GraphQL fragments out of smaller fragments. Or it might remind you of composing React components from other React components.

Although the code style is a little verbose now, there is something oddly satisfying in breaking apart a screen’s ViewModel into smaller ViewModels. It feels similar to writing a React component tree, except that we’re decomposing a backend API. It’s like _the data has its own shape but it roughly lines up with your React component tree_.

Let’s see what happens when the UI needs to evolve.

* * *

### [Evolving a ViewModel](https://overreacted.io/jsx-over-the-wire/#evolving-a-viewmodel)

Suppose the UI design changes, and we want to display friends’ avatars too:

```
type LikeButtonProps = {
  totalLikeCount: number,
  isLikedByUser: boolean,
  friendLikes: {
    firstName: string
    avatar: string
  }[]
}
```

Assuming we use TypeScript, we’ll immediately get a type error in the ViewModel:

```
async function LikeButtonViewModel(
  { postId } : { postId: number }
) : LikeButtonProps {
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  return {
    totalLikeCount: post.totalLikeCount,
    isLikedByUser: post.isLikedByUser,
    // 🔴 Type 'string[]' is not assignable to type '{ firstName: string; avatar: string; }[]'.
    friendLikes: friendLikes.likes.map(l => l.firstName)
  };
}
```

Let’s fix it:

```
async function LikeButtonViewModel(
  { postId } : { postId: number }
) : LikeButtonProps {
  const [post, friendLikes] = await Promise.all([
    getPost(postId),
    getFriendLikes(postId, { limit: 2 }),
  ]);
  return {
    totalLikeCount: post.totalLikeCount,
    isLikedByUser: post.isLikedByUser,
    friendLikes: friendLikes.likes.map(l => ({
      firstName: l.firstName,
      avatar: l.avatar,
    }))
  };
}
```

Now the BFF response for every screen that includes a `LikeButton` ViewModel will use the new `friendLikes` format, which is exactly what the `LikeButton` React component wants. There are no further changes to make—_it just works_. We _know_ that it works because `LikeButtonViewModel` is the only place generating props for a `LikeButton`, no matter which screen we’re requesting from the BFF. (For now assume that this is true; we’re still yet to decide how exactly to tie them.)

I’d like to call attention to the previous fact because this is quite profound.

When was the last time you c