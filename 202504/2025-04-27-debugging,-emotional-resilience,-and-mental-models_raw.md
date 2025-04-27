Title: Debugging, emotional resilience, and mental models

URL Source: https://www.seangoedecke.com/debugging/

Markdown Content:
Being good at debugging is more useful than being good at writing code - you only write a piece of code once, but you may end up debugging it hundreds of times[1](https://www.seangoedecke.com/debugging/#fn-1). As programmers use more AI-written code, debugging may end up being the _only_ remaining programming skill. But for some reason, the vast majority of programming content is about writing code well, not about debugging. What’s different about debugging?

Debugging can be a confusing and emotionally unpleasant process. Writing code involves building neat mental models and fitting them together in satisfying ways. Everything is nicely labeled and accounted for. When something goes wrong, it doesn’t just break your code - it also breaks this comforting illusion of control and understanding. The natural human reaction to this, like with any kind of pain, is to get away from the painful stimulus as quickly as possible: like jerking our hand away from the hot stove, we want to rush right in with a bugfix. In the case of software, this is a bad thing. Debugging is the very time you most need to slow down and reconsider your mental model of the codebase, because if you’re debugging it’s a good sign that your mental model is broken.

Getting good at programming requires building up an emotional tolerance to confusion. Software engineers often talk about “flow state”: that space when the code seems to flow effortlessly onto your screen, and problems are solved in the instant of their arrival. But being in a “flow state” is often a sign that the problems we’re solving are easy problems - how to structure a familiar software component, for instance - and not hard problems that require really engaging with the problem domain. Coders who rely on flow state will find themselves drowning when confronted with a truly difficult problem, and will make hasty compromises to get back into flow. These compromises will almost certainly cause further problems down the track. You must be able to work outside of flow state to be an effective debugger.

Debugging is the act of fixing code. But what does it mean to “fix” code? In a sense it’s false to say that your code has broken. Your poor code is doing exactly what it’s supposed to be doing: assigning variables here, returning values there. If the values returned aren’t the values you wanted, the problem lies with the coder, not the code. What needs fixing is your mental model[2](https://www.seangoedecke.com/debugging/#fn-2).

### Mental models, framework models

What distinguishes a really good programmer from a mediocre or bad one? Well, lots of superficial things: familiarity with syntax, knowledge of more languages and frameworks, and so on. But I think the main difference is in the accuracy and sophistication of the programmer’s mental model. Good programmers have a much more explicit mental model of what their code is doing.

Let’s take a Rails controller action as an example. A beginner will probably have only a shaky idea of what actually goes on when the code in an action is hit:

“A browser puts a URL in the address bar, which hits the Rails app (how?) and is directed by `config/routes.rb` to a controller action (how?). Some stuff (what stuff?) from the browser is accessible in the controller code, using magic variables like `params`, and by calling methods like `render` the controller can send stuff in a Rails view (how?) back to the browser.”

This is a pretty serviceable model. You can build a working Rails app with it. But what happens when you’re not getting the right stuff in the browser? This could be incorrect data on the page, or just a 404/500 error page. Something in your mental model has not gone to plan. If you’re not used to debugging, you might panic and begin changing code at random until it starts to work again. Instead, what you should do is begin narrowing down where the error in your mental model is. **This is actually a simple array search problem**, and can be approached multiple ways. Let’s represent your model as a series of steps:

1.  Browser puts the URL in the address bar
2.  The Rails app is hit
3.  The code in the controller action runs
4.  The controller action performs an operation on some data from the browser
5.  The controller action selects a Rails template
6.  The Rails template is rendered on the browser

Where to start? Well, you could start at one end or the other, and work back or forwards until you discover the step that isn’t behaving as you expect. If you can, it’s often a good idea to perform a binary search: check in the middle, and if everything’s OK there, check halfway between the middle and the end, and so on. For simplicity’s sake, I’ll sketch out walking through these steps from the start to the end.

First, (1) make sure the right URL is being accessed. Look at the URL in the address bar on your page with the incorrect data. Is it the URL you expect to see? If so, is there a typo in the URL? If everything looks OK here, (2) check that the Rails app is hit. Go to your server logs in the terminal and refresh the broken page. Do any log lines appear? Is your server actually running? Is there an obvious error in the logs? If you’re not sure, continue to the next step (3). Throw a debugger (`byebug`, or `binding.pry`) in your controller code, refresh the page, and see if the debugger triggers. If it does, you know the controller code is executing, and everything so far has probably gone well. To check (4), step through the code in the debugger and check that the variables have the values you expect them to have. If they do, move onto steps (5) and (6). Open your browser dev tools and eyeball the HTML of the broken page. Does it match the HTML in your Rails view? In parts where you’ve put templating logic, does the generated HTML look right?

At every point in the process, **you should have an idea of what you expect to see before you look**. For instance, before you start investigating variables from a debugger, ask yourself what value this variable should have at this point in the code. Once you’re pretty sure you know, check what the actual value is. If there’s a discrepancy, you’ve got a misunderstanding about how your code works, which is likely the cause of your current bug. If it’s not, it’ll probably be the cause of future bugs.

So far this model is pretty vague: there are only six steps, and the transition between the steps is largely magical. How does hitting the Rails app cause the controller action to run? Where the beginner shrugs, or says “Rails handles that”, a more experienced developer has additional steps. Their mental model is finer-grained, and thus their debugging can pick up finer-grained problems. Where the beginner developer throws up their hands and says “Rails is getting hit when I access this URL, but it’s not going to the controller for some dumb reason”, a more advanced developer might identify the problem (for instance) as an issue with the `strong_parameters` feature: the right controller action is being invoked, but `strong_parameters` is expecting different parameters and is thus responding with a 400 status code before executing any of the code in the controller. Even though the problem identified is more explicit, the debugging process still involves going through steps in a mental model.

Programmers have multiple mental models on multiple different levels. We could call the example above a “framework model”: a model about how code other people have written works. If you’ve ever learned a framework like Rails or React, you’ve developed a model like this. You’ve probably seen how your idea of “how Rails works” (your mental model of the steps Rails takes to respond to stimuli like incoming requests) grows more sophisticated and more definite over time.

Framework models are hard to build, since there’s a lot of functionality to wrap your head around, but they come with one big advantage: lots of other people are trying to understand the same framework as you. There’s likely to be solid documentation, Stack Overflow questions and answers, tutorials, and blog posts about the framework you’re trying to learn.

I’m going to talk about two other kinds of model: “code models” and “domain models”.

### Code models

If a framework model is a high-level model of how other people’s code works, a code model is a low-level model of how your own code works. Many programmers probably develop their code model before they type a single line of code. Just like a framework model, seriously debugging your own code involves stepping through that code model and verifying its accuracy against the world. Let’s take FizzBuzz as an example:

```
for i in range(1,21):
	if (i % 5 == 0):
        print "fizz"
elif (i % 10 == 0):
    print "buzz" 
else:
	print i
```

This is supposed to print the numbers between 1 and 20, but every number divisible by 10 is replaced with “buzz”, and every other number divisible by 5 with “fizz”. For instance: “1 2 3 4 fizz 6 7 8 9 buzz…”

What might a mental model of this code look like?

1.  Take the number 1
2.  If it’s divisible by 5 print fizz
3.  If it’s divisible by 10 print buzz
4.  If neither, print the number
5.  Keep doing this until we get to 20

What happens when we run the code above? Well, we get a bug: “1 2 3 4 fizz 6 7 8 9 fizz…“. Where’d our buzz go? Our mental model doesn’t match the real world. Let’s throw a debugger in the code and see where the mismatch is. Everything looks fine up until the number 10, when step (3) in our model becomes problematic. 10 is divisible by 5, so our code prints “fizz”. 10 is also divisible by 10, but this condition’s in an `else if`, so our code never gets there. In fact, the code can never match our mental model - any number divisible by 10 is also divisible by 5, so the program will print “fizz” and move on to the next number. This also reveals an ambiguity in our mental model. According to our model, our program should print “fizzbuzz” for the number 10, since it’s divisible by both 5 and 10. But this isn’t what we want to do. Bugs in our code and bugs in our mental model of how our code should look often go hand in hand.

Fixing our mental model will require switching around steps (2) and (3):

1.  Take the number 1
2.  If it’s divisible by 10, print buzz
3.  If it’s divisible by 5, and not also by 10, print fizz
4.  If neither, print the number
5.  Keep doing this until we get to 20

Likewise, we’ll need to switch around the conditions in our code, and check for divisibility by 10 before we check for divisibility by 5.

Code models are the easiest kind of mental models to build. Whenever you write code, you build one as you go, and once you’ve written enough code it becomes effortless to visualise what steps your code will take to achieve your goal. (Of course, retaining code models is not easy, and communicating a code model to another programmer is more difficult still.)

### Domain models

The third kind of model, domain models, are the hardest. They combine the difficulties of both code and framework models. Like code models, you’re likely to be building a domain model without the benefit of documentation. Like framework models, domain models involve understanding a lot of functionality. Worse still, the structure of a domain is not designed, but rather grows organically, so it often includes vestigial elements, dead-ends and edge cases.

What is a domain model? If a code model is a mental picture of how lines of code work, and a framework model is a mental picture of how a framework functions, then a domain model is a mental picture of how a thing in the real world functions. Suppose you’re building a Rails app that’s like Uber for dogs. You’ll need a framework model of how Rails functions, and various code models of how the controller actions and views you write function. And, tying together all of this, you’ll need a model of how “Uber for dogs” is supposed to work in the first place. A domain model is effectively a list of requirements for your app. Conversely, changes in the requirements usually reflect changes in the domain model.

Here’s a very rough domain model: you hit a button on the app, and someone drives to you with a very cute dog in the backseat that you can pat. But rough domain models very quickly get more complicated. Some people only want to pat certain kinds of dog, and some drivers only want their dogs to be patted for short periods of time. Some drivers have multiple dogs, and will only drive to certain areas. To be compliant with local laws, certain breeds of dog must have a license to be involved in a business enterprise - but only in certain areas. The complexity of your domain model is spiralling out of control very quickly.

If you make a mistake in your code model, you will get a bug in your code. If you make a mistake in your framework model, you will get a bug in your code. **If you make a mistake in your domain model, you will spend days or months writing the wrong code.** The cost of a mistake in your domain model can be significantly more than the cost of a mistake in your other models, in part because it is much less likely to be caught by testing your code or eyeballing your app.

If there’s a way to express your domain model in a series of steps - as I did with code and framework models - I’m not aware of it. This means that I don’t know how to debug a broken domain model. If I identify something wrong with my domain model, the best I can do is flail around changing random things, like the beginner who alters their code at random because they don’t know how to debug it. If you know a methodical way of identifying mistakes in your domain model, you’re probably capable of making a very profitable side project or startup.

### Summary

*   Debugging is a mechanical process. You don’t need any great insight to debug your code, just patience and persistence.
*   Although it’s mechanical, the challenge of debugging is at least partially emotional. You need to be comfortable with staying in a place where your code is broken and you’re not sure why, rather than just rushing to the quickest solution available.
*   Debugging doesn’t just involve stepping through your code. It’s a process of stepping through your mental models.
*   A bug almost always represents a place where your mental model diverges from the state of the real world.
*   There are multiple kinds of mental model that you should maintain: at the level of lines of code, at the level of framework APIs, and at the (most difficult) level of the real-world problem your app is solving.

* * *

1.  I know _you_ are so good at writing code that you don’t actually produce bugs. I’m writing this post for all the other programmers.
    
    [↩](https://www.seangoedecke.com/debugging/#fnref-1)
2.  There are bugs that can happen that don’t necessarily represent a problem with your mental model (cosmic rays, some unpredictable third-party regression), but in my experience these are rare.
    
    [↩](https://www.seangoedecke.com/debugging/#fnref-2)

April 27, 2025 │ Tags: [shipping](https://www.seangoedecke.com/tags/shipping/), [emotional regulation](https://www.seangoedecke.com/tags/emotional%20regulation/)

* * *
