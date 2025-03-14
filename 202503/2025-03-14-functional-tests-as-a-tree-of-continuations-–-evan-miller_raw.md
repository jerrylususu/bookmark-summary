Title: 

URL Source: https://www.evanmiller.org/functional-tests-as-a-tree-of-continuations.html

Markdown Content:
Functional Tests As A Tree Of Continuations – Evan Miller
===============      

 [![Image 1](https://www.evanmiller.org/header.png)](https://www.evanmiller.org/index.html)

Functional Tests As A Tree Of Continuations
===========================================

By [Evan Miller](https://www.evanmiller.org/)

_June 15, 2010_

One of the most essential practices for maintaining the long-term quality of computer code is to write automated tests that ensure the program continues to act as expected, even when other people (including your future self) muck with it.

Test code is often longer than the code that is being tested. A former colleague estimates that the right ratio is around 3 lines of functional test code for every line of “real” code. Writing test code is often mindless and repetitive, because all you do is trace out all the steps a user could take and write down all the things that should be true about each one.

A great deal of test code simply exists to set up the tests. Sometimes you can abstract out the logic into `setup()` and `teardown()` functions, and put the fake data needed for tests into things called fixtures. Even then, you’ll often have a subset of tests that requires additional setup, and test code often becomes littered with miniature, unofficial setup functions.

The problem
-----------

It’s a wonder to me that most testing environments are structured as _lists of tests_. Lists of tests are sensible for unit tests, but they’re a disaster for functional tests. The list structure is one of the main reasons that functional test suites are so repetitive.

Let’s say you want to test a 5-step process, and test the “Continue” and “Cancel” buttons at each step. You can only get to a step by pressing “Continue” in the previous step. With the traditional “list of tests” paradigm, you have to write something like

```
test_cancel_at_step_one() {
    Result = do_step_one("Cancel");
    assert_something(Result);
}

test_cancel_at_step_two() {
    Result = do_step_one("Continue");
    assert_something(Result);
    Result = do_step_two("Cancel");
    assert_something(Result);
}

test_cancel_at_step_three() {
    do_step_one("Continue"); # tested above
    Result = do_step_two("Continue");
    assert_something(Result);
    Result = do_step_three("Cancel");
    assert_something(Result);
}

test_cancel_at_step_four() {
    do_step_one("Continue"); # tested above
    do_step_two("Continue"); # tested above
    Result = do_step_three("Continue");
    assert_something(Result);
    Result = do_step_four("Cancel");
    assert_something(Result);
}

test_cancel_at_step_five() {
    do_step_one("Continue"); # tested above
    do_step_two("Continue"); # tested above
    do_step_three("Continue"); # tested above
    Result = do_step_four("Continue");
    assert_something(Result);
    Result = do_step_five("Cancel");
    assert_something(Result);
}
```

As you can start to see, the length of each test is growing linearly in the number of steps we’re testing, so the length of the total test suite ends up being O(N2) in the number of steps.

The solution
------------

A more appropriate data structure for functional tests is a _testing tree_. The tree essentially maps out the possible actions at each step. At each node, there is a set of assertions, and parent nodes pass a _copy of state_ down to each child (representing a possible user action). Child nodes are free to modify and make assertions on the state received from the parent node, and pass a copy of the modified state down to _its_ children. Nodes should not affect the state of parents or siblings.

Let’s take a concrete example. In a 5-step process, the tree would look like:

*   Step 1
    *   Cancel
    *   Continue to Step 2
        *   Cancel
        *   Continue to Step 3
            *   Cancel
            *   Continue to Step 4
                *   Cancel
                *   Continue to Step 5

Here, the first “Cancel” and “Continue to Step 2” are like parallel universes. Rather than repeating Step 1 to test each of these, we want to automatically make a copy of the universe at the end of Step 1, then run child tests on each parallel universe. If we can write our tests as a tree in this way, the length of the total test suite will be O(N) in the number of steps, rather than O(N2).

For modern web applications, all the state is stored in a database. Therefore to make a “copy of the universe”, we just need a way to make a copy of the database to pass down to the child tests, while preserving older copies that tests further up the tree can copy and use.

The solution is to implement a _stack of databases_. As we walk down the testing tree, we push a copy of the current database onto the stack, and the child can play with the database at the top of the stack. After we’ve finished with a set of child nodes and ascend back up the testing tree, we pop the modified databases off the stack, returning to the previous database revisions.

An example
----------

I won’t go through the details of writing a testing framework or the database stack, but here’s how you’d test a multi-step process with [Chicago Boss](http://www.chicagoboss.org/)’s test framework. This is a tree implemented as nested callbacks in Erlang. Each “node” is an HTTP request with a list of callbacks that make assertions on the response, and a list of labeled continuation callbacks — these are the child nodes. Each child node receives a fresh database copy that it can thrash to its heart’s content. Managing the stack of databases is all done under the hood.

The resulting test code is surprisingly elegant:

```
start() ->
  boss_test:get_request("/step1", [],
    [ % Three assertions on the response
      fun boss_assert:http_ok/1, 
      fun(Res) -> boss_assert:link_with_text("Continue", Res) end
      fun(Res) -> boss_assert:link_with_text("Cancel", Res) end
    ],
    [ % A list of two labeled continuations; each takes the previous 
      % response as the argument

      "Cancel at Step 1", % First continuation
      fun(Response1) -> 
          boss_test:follow_link("Cancel", Response1,
            [ fun boss_assert:http_ok/1 ], []) % One assertion, no continuations
      end,

      "Continue at Step 1", % Second continuation
      fun(Response1) ->
          boss_test:follow_link("Continue", Response1,
            [ fun boss_assert:http_ok/1 ], [ 

              "Cancel at Step 2", % Two more continuations
              fun(Response2) ->
                  boss_test:follow_link("Cancel", Response2,
                    [ fun boss_assert:http_ok/1 ], [])
              end,

              "Continue at Step 2",
              fun(Response2) ->
                  boss_test:follow_link("Continue", Response2,
                    [ fun boss_assert:http_ok/1 ], [ 

                      "Cancel at Step 3",
                      fun(Response3) ->
                          boss_test:follow_link("Cancel", Response3,
                            [ fun boss_assert:http_ok/1 ], [])
                      end,

                      "Continue at Step 3",
                      fun(Response3) ->
                          boss_test:follow_link("Continue", Response3,
                            [ fun boss_assert:http_ok/1 ], [ 

                              "Cancel at Step 4",
                              fun(Response4) ->
                                  boss_test:follow_link("Cancel", Response4,
                                    [ fun boss_assert:http_ok/1 ], [])
                              end,

                              "Continue at Step 4",
                              fun(Response4) ->
                                  boss_test:follow_link("Continue", Response4,
                                    [ fun boss_assert:http_ok/1 ], [])
                              end ]) end ]) end ]) end ]).
```

If the indentation ever gets out of hand, we can simply put the list of continuations into a new function.

Conclusion
----------

There are several benefits to structuring functional tests as a tree of continuations:

*   _Eliminates code duplication._ We don’t need to repeat steps 1-3 for each action that can be taken at step 4. This reduces the code base, as well as time needed for execution.
    
*   _Eliminates most setup code._ As long as the setup actions are associated with an HTTP interface, all setup can be done as part of the testing tree with no performance penalty.
    
*   _Pinpoints the source of failing tests._ If assertions fail in a parent node, we can immediately stop before running the child nodes. By contrast, lists of tests usually produce long lists of failures for one bug, making it harder to find the source.
    
*   _Tests are well-structured._ There is a 1-1 mapping between nodes and something the user sees, and a 1-1 mapping between child nodes and something the user can do next. The tests appear in a well-structured hierarchy, instead of a haphazard “list of everything I could think of”.
    
*   _The trail of previous responses are all in scope._ This benefit is unique to a callback implementation in a language that supports closures — it’s handy if you need to compare output from two requests that are separated by several intermediate requests. With a list of tests, you would have to pass around data in return values and function arguments, but here all previous responses are at our fingertips in Response1, Response2, etc.
    

Why haven’t I been able to find anyone else using this approach? My guess is that all of the side effects of OO languages encourage a wrecking-ball mentality when it comes to unit tests — destroy all possible state after each test. But for functional tests with many steps, this approach is grossly inefficient — if you want to test every rung on a ladder, it’s pointless to climb all the way down to the ground and trudge back up for each test.

To write your own testing framework based on continuation trees, all you need is a stack of databases (or rather, a database that supports rolling back to an arbitrary revision). I don’t know what databases support this kind of revisioning functionality, but adding the feature to Chicago Boss’s in-memory database took about 25 lines of Erlang code.

Once you start writing functional tests as a tree of assertions and continuations, you really will wonder how you did it any other way. It’s just one of those ideas that seems too obvious in hindsight.

* * *

_You’re reading [evanmiller.org](https://www.evanmiller.org/), a random collection of math, tech, and musings. If you liked this you might also enjoy:

*   [Why I Program in Erlang](https://www.evanmiller.org/why-i-program-in-erlang.html)
*   [Elixir RAM and the Template of Doom](https://www.evanmiller.org/elixir-ram-and-the-template-of-doom.html)

_

* * *

_Get new articles as they’re published, via [LinkedIn](https://www.linkedin.com/in/evanmmiller/), [Twitter](https://twitter.com/EvMill), or [RSS](https://www.evanmiller.org/news.xml)._

* * *

_Want to look for statistical patterns in your MySQL, PostgreSQL, or SQLite database? My desktop statistics software **[Wizard](https://www.wizardmac.com/)** can help you analyze **more data in less time** and **communicate discoveries visually** without spending days struggling with pointless command syntax. Check it out!_

[![Image 2](https://www.evanmiller.org/images/index/wizard2.png)](https://www.wizardmac.com/)  
**[Wizard](https://www.wizardmac.com/)**  
Statistics the Mac way

* * *

[Back to Evan Miller’s home page](https://www.evanmiller.org/) – [Subscribe to RSS](https://www.evanmiller.org/news.xml) – [LinkedIn](https://www.linkedin.com/in/evanmmiller/) – [Twitter](https://twitter.com/EvMill)

* * *
