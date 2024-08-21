Title: Software engineering practices

URL Source: https://simonwillison.net/2022/Oct/1/software-engineering-practices/

Markdown Content:
1st October 2022

Gergely Orosz [started a Twitter conversation](https://twitter.com/GergelyOrosz/status/1576161504260657152) asking about recommended “software engineering practices” for development teams.

(I really like his rejection of the term “best practices” here: I always feel it’s prescriptive and misguiding to announce something as “best”.)

I decided to flesh some of my replies out into a longer post.

*   [Documentation in the same repo as the code](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#docs-same-repo)
*   [Mechanisms for creating test data](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#create-test-data)
*   [Rock solid database migrations](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#rock-solid-migrations)
*   [Templates for new projects and components](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#new-project-templates)
*   [Automated code formatting](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#auto-formatting)
*   [Tested, automated process for new development environments](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#tested-dev-environments)
*   [Automated preview environments](https://simonwillison.net/2022/Oct/1/software-engineering-practices/#automated-previews)

#### Documentation in the same repo as the code

The most important characteristic of internal documentation is trust: do people trust that documentation both exists and is up-to-date?

If they don’t, they won’t read it or contribute to it.

The best trick I know of for improving the trustworthiness of documentation is to put it in the same repository as the code it documents, for a few reasons:

1.  You can enforce documentation updates as part of your code review process. If a PR changes code in a way that requires documentation updates, the reviewer can ask for those updates to be included.
2.  You get versioned documentation. If you’re using an older version of a library you can consult the documentation for that version. If you’re using the current main branch you can see documentation for that, without confusion over what corresponds to the most recent “stable” release.
3.  You can integrate your documentation with your automated tests! I wrote about this in [Documentation unit tests](https://simonwillison.net/2018/Jul/28/documentation-unit-tests/), which describes a pattern for introspecting code and then ensuring that the documentation at least has a section header that matches specific concepts, such as plugin hooks or configuration options.

#### Mechanisms for creating test data

When you work on large products, your customers will inevitably find surprising ways to stress or break your system. They might create an event with over a hundred different types of ticket for example, or an issue thread with a thousand comments.

These can expose performance issues that don’t affect the majority of your users, but can still lead to service outages or other problems.

Your engineers need a way to replicate these situations in their own development environments.

One way to handle this is to provide tooling to import production data into local environments. This has privacy and security implications—what if a developer laptop gets stolen that happens to have a copy of your largest customer’s data?

A better approach is to have a robust system in place for generating test data, that covers a variety of different scenarios.

You might have a button somewhere that creates an issue thread with a thousand fake comments, with a note referencing the bug that this helps emulate.

Any time a new edge case shows up, you can add a new recipe to that system. That way engineers can replicate problems locally without needing copies of production data.

#### Rock solid database migrations

The hardest part of large-scale software maintenance is inevitably the bit where you need to change your database schema.

(I’m confident that one of the biggest reasons NoSQL databases became popular over the last decade was the pain people had associated with relational databases due to schema changes. Of course, NoSQL database schema modifications are still necessary, and often they’re even more painful!)

So you need to invest in a really good, version-controlled mechanism for managing schema changes. And a way to run them in production without downtime.

If you do not have this your engineers will respond by being fearful of schema changes. Which means they’ll come up with increasingly complex hacks to avoid them, which piles on technical debt.

This is a deep topic. I mostly use Django for large database-backed applications, and Django has the best [migration system](https://docs.djangoproject.com/en/4.1/topics/migrations/) I’ve ever personally experienced. If I’m working without Django I try to replicate its approach as closely as possible:

*   The database knows which migrations have already been applied. This means when you run the “migrate” command it can run just the ones that are still needed—important for managing multiple databases, e.g. production, staging, test and development environments.
*   A single command that applies pending migrations, and updates the database rows that record which migrations have been run.
*   Optional: rollbacks. Django migrations can be rolled back, which is great for iterating in a development environment but using that in production is actually quite rare: I’ll often ship a new migration that reverses the change instead rather than using a rollback, partly to keep the record of the mistake in version control.

Even harder is the challenge of making schema changes without any downtime. I’m always interested in reading about new approaches for this—GitHub’s [gh-ost](https://github.com/github/gh-ost) is a neat solution for MySQL.

An interesting consideration here is that it’s rarely possible to have application code and database schema changes go out at the exact same instance in time. As a result, to avoid downtime you need to design every schema change with this in mind. The process needs to be:

1.  Design a new schema change that can be applied without changing the application code that uses it.
2.  Ship that change to production, upgrading your database while keeping the old code working.
3.  Now ship new application code that uses the new schema.
4.  Ship a new schema change that cleans up any remaining work—dropping columns that are no longer used, for example.

This process is a pain. It’s difficult to get right. The only way to get good at it is to practice it a lot over time.

My rule is this: **schema changes should be boring and common**, as opposed to being exciting and rare.

#### Templates for new projects and components

If you’re working with microservices, your team will inevitably need to build new ones.

If you’re working in a monorepo, you’ll still have elements of your codebase with similar structures—components and feature implementations of some sort.

Be sure to have really good templates in place for creating these “the right way”—with the right directory structure, a README and a test suite with a single, dumb passing test.

I like to use the Python [cookiecutter](https://cookiecutter.readthedocs.io/) tool for this. I’ve also used GitHub template repositories, and I even have a neat trick for [combining the two](https://simonwillison.net/2021/Aug/28/dynamic-github-repository-templates/).

These templates need to be maintained and kept up-to-date. The best way to do that is to make sure they are being used—every time a new project is created is a chance to revise the template and make sure it still reflects the recommended way to do things.

#### Automated code formatting

This one’s easy. Pick a code formatting tool for your language—like [Black](https://github.com/psf/black) for Python or [Prettier](https://prettier.io/) for JavaScript (I’m so jealous of how Go has [gofmt](https://pkg.go.dev/cmd/gofmt) built in)—and run its “check” mode in your CI flow.

Don’t argue with its defaults, just commit to them.

This saves an incredible amount of time in two places:

*   As an individual, you get back all of that mental energy you used to spend thinking about the best way to format your code and can spend it on something more interesting.
*   As a team, your code reviews can entirely skip the pedantic arguments about code formatting. Huge productivity win!

#### Tested, automated process for new development environments

The most painful part of any software project is inevitably setting up the initial development environment.

The moment your team grows beyond a couple of people, you should invest in making this work better.

At the very least, you need a documented process for creating a new environment—and it has to be known-to-work, so any time someone is onboarded using it they should be encouraged to fix any problems in the documentation or accompanying scripts as they encounter them.

Much better is an automated process: a single script that gets everything up and running. Tools like Docker have made this a LOT easier over the past decade.

I’m increasingly convinced that the best-in-class solution here is cloud-based development environments. The ability to click a button on a web page and have a fresh, working development environment running a few seconds later is a game-changer for large development teams.

[Gitpod](https://www.gitpod.io/) and [Codespaces](https://github.com/features/codespaces) are two of the most promising tools I’ve tried in this space.

I’ve seen developers lose hours a week to issues with their development environment. Eliminating that across a large team is the equivalent of hiring several new full-time engineers!

#### Automated preview environments

Reviewing a pull request is a lot easier if you can actually try out the changes.

The best way to do this is with automated preview environments, directly linked to from the PR itself.

These are getting increasingly easy to offer. [Vercel](https://vercel.com/features/previews), [Netlify](https://www.netlify.com/products/deploy-previews/), [Render](https://render.com/docs/pull-request-previews) and [Heroku](https://devcenter.heroku.com/articles/github-integration-review-apps) all have features that can do this. Building a custom system on top of something like [Google Cloud Run](https://cloud.google.com/run) or [Fly Machines](https://fly.io/blog/fly-machines/) is also possible with a bit of work.

This is another one of those things which requires some up-front investment but will pay itself off many times over through increased productivity and quality of reviews.
