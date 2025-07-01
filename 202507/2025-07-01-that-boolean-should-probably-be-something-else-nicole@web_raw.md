Title: That boolean should probably be something else

URL Source: https://ntietz.com/blog/that-boolean-should-probably-be-something-else/

Published Time: Mon, 30 Jun 2025 13:01:42 GMT

Markdown Content:
One of the first types we learn about is the boolean. It's pretty natural to use, because boolean logic underpins much of modern computing. And yet, it's one of the types we should probably be using a lot less of. In almost every single instance when you use a boolean, it should be something else.

The trick is figuring out _what_ "something else" is. Doing this is worth the effort. It tells you a lot about your system, and it will improve your design (even if you end up using a boolean).

There are a few possible types that come up often, hiding as booleans. Let's take a look at each of these, as well as the case where using a boolean _does_ make sense. This isn't exhaustive—[[1]](https://ntietz.com/blog/that-boolean-should-probably-be-something-else/#fn-em-dash)there are surely other types that can make sense, too.

Datetimes
---------

A lot of boolean data is representing a temporal event having happened. For example, websites often have you confirm your email. This may be stored as a boolean column, `is_confirmed`, in the database. It makes a lot of sense.

But, you're throwing away data: when the confirmation happened. You can instead store _when_ the user confirmed their email in a nullable column. You can still get the same information by checking whether the column is null. But you also get richer data for other purposes.

Maybe you find out down the road that there was a bug in your confirmation process. You can use these timestamps to check which users would be affected by that, based on when their confirmation was stored.

This is the one I've seen discussed the most of all these. We run into it with almost every database we design, after all. You can detect it by asking if an _action has to occur_ for the boolean to change values, and if values can only change one time. If you have both of these, then it really looks like it is a datetime being transformed into a boolean. Store the datetime!

Enums
-----

Much of the remaining boolean data indicates either what type something is, or its status. Is a user an admin or not? Check the `is_admin` column! Did that job fail? Check the `failed` column! Is the user allowed to take this action? Return a boolean for that, yes or no! These usually make more sense as an enum.

Consider the admin case: this is really a user role, and you should have an enum for it. If it's a boolean, you're going to eventually need more columns, and you'll keep adding on other statuses. Oh, we had users and admins, but now we also need guest users and we need super-admins. With an enum, you can add those easily.

```
enum UserRole {
  User,
  Admin,
  Guest,
  SuperAdmin,
}
```

And then you can usually use your tooling to make sure that all the new cases are covered in your code. With a boolean, you have to add _more_ booleans, and then you have to make sure you find _all_ the places where the old booleans were used and make sure they handle these new cases, too. Enums help you avoid these bugs.

Job status is one that's pretty clearly an enum as well. If you use booleans, you'll have `is_failed`, `is_started`, `is_queued`, and on and on. Or you could just have one single field, `status`, which is an enum with the various statuses. (Note, though, that you probably _do_ want timestamp fields for each of these events—but you're still best having the status stored explicitly as well.) This begins to resemble a state machine once you store the status, and it means that you can make much cleaner code and analyze things along state transition lines.

And it's not just for storing in a database, either. If you're checking a user's permissions, you often return a boolean for that.

```
fn check_permissions(user: User) -> bool {
  false // no one is allowed to do anything i guess
}
```

In this case, `true` means the user can do it and `false` means they can't. Usually. I think. But you can really start to have doubts here, and with any boolean, because the application logic meaning of the value _cannot_ be inferred from the type.

Instead, this can be represented as an enum, even when there are just two choices.

```
enum PermissionCheck {
  Allowed,
  NotPermitted(reason: String),
}
```

As a bonus, though, if you use an enum? You can end up with richer information, like returning a reason for a permission check failing. And you are safe for future expansions of the enum, just like with roles.

You can detect when something should be an enum a proliferation of booleans which are mutually exclusive or depend on one another. You'll see multiple columns which are all changed at the same time. Or you'll see a boolean which is returned and used for a long time. It's important to use enums here to keep your program maintainable and understandable.

Conditionals
------------

But when _should_ we use a boolean? I've mainly run into one case where it makes sense: when you're (temporarily) storing the result of a conditional expression for evaluation. This is in some ways an optimization, either for the computer (reuse a variable[[2]](https://ntietz.com/blog/that-boolean-should-probably-be-something-else/#fn-optimization)) or for the programmer (make it more comprehensible by giving a name to a big conditional) by storing an intermediate value.

Here's a contrived example where using a boolean as an intermediate value.

```
fn calculate_user_data(user: User, records: RecordStore) {
  // this would be some nice long conditional,
  // but I don't have one. So variables it is!
  let user_can_do_this: bool = (a && b) && (c || !d);

  if user_can_do_this && records.ready() {
    // do the thing
  } else if user_can_do_this && records.in_progress() {
    // do another thing
  } else {
    // and something else!
  }
}
```

But even here in this contrived example, some enums would make more sense. I'd keep the boolean, probably, simply to give a _name_ to what we're calculating. But the rest of it should be a `match` on an enum!

* * *

Sure, not every boolean should go away. There's probably no single rule in software design that is always true. But, we should be paying a lot more attention to booleans.

They're sneaky. They feel like they make sense for our data, but they make sense for our _logic_. The data is usually something different underneath. By storing a boolean as our data, we're coupling that data tightly to our application logic.

Instead, we should remain critical and ask what data the boolean depends on, and should we maybe store that instead? It comes easier with practice. Really, all good design does. A little thinking up front saves you a _lot_ of time in the long run.

* * *

1.   I know that using an em-dash is treated as a sign of using LLMs. LLMs are _never_ used for my writing. I just really like em-dashes and have a dedicated key for them on one of my keyboard layers. [↩](https://ntietz.com/blog/that-boolean-should-probably-be-something-else/#fr-em-dash-1)

2.   This one is _probably_ best left to the compiler. [↩](https://ntietz.com/blog/that-boolean-should-probably-be-something-else/#fr-optimization-1)

If you're looking to grow more effective as a software engineer, please consider my [coaching services](https://ntietz.com/coaching/).
