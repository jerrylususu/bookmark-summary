Title: Mocking is an Anti-Pattern

URL Source: https://www.amazingcto.com/mocking-is-an-antipattern-how-to-test-without-mocking/

Markdown Content:
I’m for more tests. I push my clients to measure and increase test coverage. When doing so, the start is easy. It is easy to get to 10%, 20% and 30% of coverage. It gets more interesting after that. You come to a point where you need to test code that contains calls to `IO` - code with side effects, e.g. databases or services.

There people introduce mocks. A mock is a an object that imitates another service, like a database Repository or a service. Mocks make testing code that has service calls in them easy. Mock frameworks are genius, a marvel to use. People use mocks they want to test things “in isolation”—not understanding that isolation is the core of the problem, not the solution. The bugs of the IO code you want to test, arises from the interaction with the service. If you mock that, you don’t test the reason for your bugs.

[“Mocking frameworks are a path to insanity!”](https://dunnhq.com/posts/2024/prefer-test-doubles-over-mocking/)

Whenever I look at mocks, they mostly have the same problem as all unit tests that I see, they only model the happy path (I wrote about how to write unit tests to really find bugs in [“How Unit Tests Really Help Preventing Bugs”](https://www.amazingcto.com/how-unit-tests-find-prevent-bugs/)). Modelling the happy path is great for [refactoring](https://refactoring.com/) - even a necessity, but doesn’t help with finding bugs.

You can do mocks the right way, but it takes a lot of effort, and many skip this effort. Or are not aware of this effort. It’s worse to have bad mocks than no mocks, because they give you a wrong feeling of confidence in your tests—especially when mocks increase test coverage. You think your tests are testing things that in reality - they are not testing. Confusing, I know.

Back to the title: Mocking is an anti-pattern. Mocking adds complexity, is hard to maintain, introduces its own bugs, doesn't test what should be tested and creates a false sense of security.

What is Mocking
---------------

Lets look at the term _“Mocking”_. From [Martin Fowler](https://www.martinfowler.com/articles/mocksArentStubs.html) there are **Dummy** objects, **Fake** objects, **Stubs**, **Spies** and **Mocks**. All of them are different, in the context of this article I consider them the same.

When talking about IO, in general terms I mean side effects (in functional speak). This can include calling external services, REST calls, database calls, sending emails and reading and writing files.

Lets start at the beginning. Ha! **How does mocking help with testing?** Assuming you want to test this code:

```
z(x) {
  if x {
    service.IO1()
  } else {
    service.IO2()
  }
}
```

without executing the IO (too slow, no test setup possible etc.), how do you do that?

You replace the service with a mock:

```
ServiceMock {
  IO1() { return 1 }
  IO2() { return 2 }
}
```

and put that into your code instead of `IOService` for testing (the mock is created with some [mock library](https://github.com/golang/mock) the code above is just for illustration).

Refactoring `z` so we can inject the mock service:

_(there are many other ways to inject the service)_.

Now we can write a test:

```
TestZ() {
  service = ServiceMock
  result = z(true, service)
  check(result, 1)
}
```

This works fine.

The problem is when `IOService` has edge cases. When building the mock, does it address the edge cases? When you want to find bugs by testing, the tests need to test the real world. So to work, the mock for `IOService` needs to model the edge cases of `IOService`. Does it? Does the developer know they need to model the edge cases, or the mock is not helping with finding bugs? Do you even know the edge cases of `IOService`? When `IOService` is a database service, does your mock work for records that do not exist? Or return more than one record?

Beside edge cases, `IOService` has failure modes. To detect bugs in the code you’re testing, that is using `IOService`, your tests need to test for those failure modes, and your mock needs to model those failure modes. If `IOService` is a database service, does your mock model disconnects correctly? Is it even possible to model all failure modes when `IOService` is from another team or even another company (like a cloud service)? Do you know all the failure modes for a starter?

**This leads to bugs in the interaction of services being undetected and tests with mocks do less than people think they’ll do for them.**

As my friend [Oliver Wehrens](https://www.linkedin.com/in/oliverwehrens/) wrote: _“Especially when mocking services from other teams. Just had the case and bugs just showed up in e2e test by a qa team.”_

**Instead of finding bugs, is the goal of the developer when using mocks here to increase test coverage and tell a “check, z() tested” to their manager?**

Lets look at a more real world example. Many mocked tests I see look - simplified - like this:

```
find(id, service) string {
 return service.find(id)
}

Test() {
  mock = NewMock
  mock.find(3).return("Stephan")
  result = find(3, mock)
  checkCall("find", 3)
  checkEqual(result, "Stephan")
}
```

This does not test anything of value. It tests your mock library or your mock. I have looked at hundreds of tests that use mocks, and many of them test nothing - like the test above. But they increase test coverage and give a false sense of security (They are often the result of aggressive code coverage goals).

Alternatives to Mocking
-----------------------

With all the problems of mocking, are there other ways to increase testing in the eye of `IO`?

There are several things you can do instead of mocking:

*   More unit testing
*   Easier to Test IO
*   Just do IO
*   Separation of logic and services / IO
*   E2E integration tests

_Then after you have done all of that, and you still need more tests, go with mocking._

More unit testing
-----------------

First of all, do more unit testing without mocks. I’d bet there is a huge potential for more testing in your code base. You might need to refactor your code to do so. The refactoring I love most is [Decompose Conditional](https://www.refactoring.com/catalog/decomposeConditional.html).

It does replace

```
if user.isGoodStanding
  && len(user.orders)>5
  && user.hasOpenedEmail
  && len(user.email)>0 {
    send(CouponEmail)
}
```

with the cleaner and easier to read - and possible to test! -

```
if goodCustomer(user)
  && canSendTo(user) {
    send(CouponEmail)
}
```

`goodCustomer` and `canSendTo` are now easy to test. And there is no need to test the `if` or the `send`.

Another one is [Introduce Parameter Object](https://refactoring.com/catalog/introduceParameterObject.html). The refactoring replaces several parameters in a function call with one parameter.

How does it help with testing? Given the code

```
invoiceCustomer(startDate, endDate) {
  if endDate < startDate { return }
  ...
}
```

you can refactor it to

```
invoiceCustomer(dateRange) {
  if ! valid(dateRange) { return }
  ...
}

valid(dateRange) {
  return endDate > startDate
}
```

Now `valid` can easily be tested.

Refactoring all you your (more complex) IF conditionals into their own functions, make the code easier to understand and you can write meaningful tests. There are many more refactorings (read the book!) to make your code easier to test. Start here, instead of mocking.

Easier to Test IO
-----------------

We can use alternatives to our dependencies. This often happens with an in-memory database, which is compatible to your main database you do use in production, but is faster. This way queries are faster, tests are faster, and especially fast enough to run them like unit tests. Then there is no need to mock the test service, just replace the database connection URL with the in-memory one and your done.

Where this is more common is with file access. When you use a virtual file system (like [afero](https://github.com/spf13/afero)) in your application, it is easy to swap that out with a memory one during testing. You still create files and delete files, but everything happens in memory and is blazingly fast. This way it is easy to test code that does file operations, without creating or destroying files. An easy way to reduce the need for mocking.

Before you use a virtual file system though to check operations, refactor your code to work on abstractions, like `Reader`. Instead of a filename in your method, give the method a `Reader`. The caller opens the file, creates a `Reader` and hands it to the method. In testing, you create a `Reader` from a string or byte array and pass it into the method to be tested.

What can’t be abstracted, like testing the creation of a file in a correct way, with correct attributes, you can test with a virtual file system.

Just do IO
----------

One reason to replace IO with testing - beside easier setup - is performance. Tests with IO are slow.

Or so it seems.

IO is getting faster and faster. I come from an 8bit world of tape drives. To play a game as a kid, you had to start the tape drive, have lunch, then play the game because it took minutes to load. I was amazed when I got my first disc drive. Then my first hard drive. Then a Seagate Barracuda (look it up). At one company we put expensive hard drives and sound isolation into developer machines, to speed up testing. Then came SSDs. And even they become [faster and faster](https://www.octobench.com/).

Now it might be the time to just do IO - in files or a database - because the IO has become blazingly fast. _Just do IO does not help with external services, but helps with IO._

And with Postgres you can easily copy a test database with a random name from a template for each test. So there is your easy setup.

Separation of logic and IO
--------------------------

Another way to get out of mocking, is to remove IO from your code. by separating IO logic from business logic.

Starting with your code that you want to test:

```
z() {
  if x {
    IO1()
  } else {
    IO2()
  }
}
```

How to move IO out of this code? First there is often logic in that code than can be separated. Take this code that I see often and that is hard to test:

```
z(order) {
  customer = IO1()
  customer.payed = true
  customer.order = order
  customer.orders = customter.orders + 1
  IO2(customer)
}
```

Refactoring this to:

```
addOrder(customer, order) {
  customer.payed = true
  customer.order = order
  customer.orders = customter.orders + 1
}

z(order) {
  customer = IO1()
  addOrder(customer, order)
  IO2(customer)
}
```

makes the logic of transforming a customer by adding a order easy to test. Just write a test for `addOrder`. I call this first step `untangling`.

After you’ve untangled all of your code, you end up with `IO` skeletons. How do you proceed testing `z()`?

One way is to use the command pattern:

```
  IF x {
    return IO1Command
  } else {
    return IO2Command
  }
```

_(Functional programming would implement the separation of logic and IO with Monads, Monad Transformers and Monad Transformer stacks - [a simple example](https://betterprogramming.pub/investigating-the-i-o-monad-in-go-3c0fabbb4b3d]))_

Then either the commands have an `execute()` method that does the IO for you (commands need to be very very simple, with logic inside commands you just moved the logic around, you haven’t separated the logic!)

Or somewhere in the code you have

```
// z() is pure and returns a command
command = z()
SWITCH command {
  CASE IO1Command:
    IO1()
  ...
}
```

_(with parameters like the user ID as fields in the command)_

You then can test the code and see if it returns `IO1Command` and `IO2Command` correctly. No need to mock IO.

What if there is more IO in `z`? You might create a `command` list:

```
IF x {
  commands.append(IO1Command)
} else {
  commands.append(IO2Command)
}
// ... more comands here ...
return commands
```

Now `z` can perform a series of IO calls. But what if your decisions depend on IO (like the number of customers?):

```
IF IO0() {
  IO1()
} else {
  IO2()
}
```

you might be drawn to solve this with:

```
commands.append(
  IF(IOCommand0, IOCommand1, IOCommand2)
)
```

and you’ve ended up with an interpreter. An interpreter? Yes, most often you end up with a complicated interpreter when separating the last bits of `IO`. Or as [Greenspun’s tenth rule](https://en.wikipedia.org/wiki/Greenspun%27s_tenth_rule) puts it: _“Any sufficiently complicated C or Fortran program contains an ad hoc, informally-specified, bug-ridden, slow implementation of half of Common Lisp.”_

E2E integration testing
-----------------------

_See my article [I Had a Great Idea - E2E Testing For Free](https://www.amazingcto.com/brilliant-idea-e2e-tests-that-work-for-free/)_

One problem as outlined above is that mocks do not represent reality. Or a changing reality. When an external services changes, your mocks will still run fine!

You need to test reality. Instead of mocking, invest in end-to-end (E2E) testing. E2E testing and integration testing is often seen as UI driven. You use Selenium or Playwright to drive the browser or a mobile application for E2E testing.

And while I do think some amount of UI driven E2E tests is necessary to check for a broken UI, the majority of E2E tests should be backend-serverside tests. Why do I personally prefer server side E2E tests?

For example I use:

```
user = NewUser(name, email)
RegisterUserUseCase(user)
CheckUserNotValidated(user)

token = EmailValidationToUserUseCase(user)
ok = ValidateUserUseCase(user)
CheckUserValidated(user)
```

Server side E2E testing can do things, UI-driven testing can’t.

For my last startup, I wrote a DSL to write server side E2E tests for it’s subscription and payment service.

```
sub = newSubscriptionWithMonths(customer, 3)
time.OneMonthForward()
subscriptionService.Run(sub)
time.OneMonthForward()
subscriptionService.Run(sub)
time.OneMonthForward()
subscriptionService.Run(sub)
CheckSubscriptionEnded(sub)
CheckInvoicesCreated(sub, 2)
```

For every subscription model, for early cancellation, for refunds etc. we had end to end testing (simulating months) - finding bugs, finding edge cases and making sure there are no bugs in payment, invoicing and subscriptions.

E2E tests test the real thing. If they break, you have a bug.

When you add UI-driven tests (and you should have some), don’t add too many. UI-driven tests are fragile, break easily, take long to run, are flacky and a pain to maintain. Have some to test the main use cases (signup, checkout) to make sure the UI is not broken. Don’t overstretch or you will break under maintenance of UI-driven tests.

More in my Upcoming Book
------------------------

[![Image 1: Amazing CTO Book Cover](https://www.amazingcto.com/images/TechDebtCover.png.webp)](https://techdebtbook.dev/)

Technical Debt
--------------

### The essential guide

Everyone has technical debt. Eveyone wants to get out of technical debt.

Join CTO Newsletter
-------------------

### Join more than 2700 CTOs and Engineering Managers

### More Stuff from Stephan

Other interesting articles for CTOs
-----------------------------------

• [Best books for CTO](https://www.amazingcto.com/best-books-for-cto-should-read/ "Books for CTOs to read") • [The CTO Book](https://www.amazingcto.com/cto-book/ "The book for CTOs") • [Experienced CTO Coach](https://www.amazingcto.com/cto-coach-experienced/ "CTO Coach") • [Engineering Manager Coaching](https://www.amazingcto.com/cto-coaching-from-experienced-cto/ "CTO Coaching") • [Consulting and Workshops to Save you Time](https://www.amazingcto.com/consulting-cto-workshop-help "Consulting and Workshops") • [CTO Mentor](https://www.amazingcto.com/cto-mentor/ "CTO Mentor") • [CTO Mentoring](https://www.amazingcto.com/cto-mentoring/ "CTO Mentoring") • [CTO Newsletter](https://www.amazingcto.com/cto-newsletter/ "Weeky Newsletter for CTOs") • [How many developers do you need?](https://www.amazingcto.com/how-many-developers-do-you-need/ "How many developers do you need?") • [Postgres for Everything](https://www.amazingcto.com/postgres-for-everything/ "Just use Postgres") [Product Roadmaps for CTOs](https://www.amazingcto.com/product-roadmaps-cto-technology/ "Product Roadmaps for CTOs") • [How to become a CTO in a company - a career path](https://www.amazingcto.com/roadmap-to-become-cto/ "How to become a CTO in a company - a roadmap to chief technology officer")
