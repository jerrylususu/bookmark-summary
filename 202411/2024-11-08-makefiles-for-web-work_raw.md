Title: Makefiles for Web Work

URL Source: https://rosszurowski.com/log/2022/makefiles

Markdown Content:
`make` is a build tool that’s been around since the 1970s. It was originally designed for automating the building of C programs: installing dependencies, running tests, and compiling binaries.

These days, web projects involve many of the same steps: installing node\_modules, running linters and tests, starting dev servers, and compiling files with esbuild or Rollup.

The default choice for automating these steps is often [npm/yarn scripts](https://docs.npmjs.com/cli/v6/using-npm/scripts): little shell commands written into your project’s `package.json` file. More complex projects sometimes evolve into using tools like Gulp/Grunt, or even full-blown Docker builds.

But I find `make` often fills many of the same needs without as much fuss.

Its age and simplicity means it gets a lot of things right:

*   **It’s already available everywhere**. Most systems install `make` when you first set up developer tools. There’s rarely extra steps to get it working.
*   **It’s fast**. People [routinely point out](https://twitter.com/jarredsumner/status/1557694790359085057?s=20&t=R7w-EaxCLuhMhVVaFg_M1g) that npm/yarn scripts are [shockingly slow to start](https://gist.github.com/rosszurowski/1b7971ab2eaf150c5039f3f7ef5e76a0). `make` routinely runs commands **~30x faster**, which is nice, because [fast software is good software](https://craigmod.com/essays/fast_software/).
*   **It’s language-agnostic**. Since `make` is already installed and works off shell scripts, it doesn’t require commitment to one language or toolchain. You can use it for Go, PHP, Rust, or Node projects equally. And you can shell out to language-specific tools when needed.
*   **It’s simple, with room to grow**. Makefiles have a reputation for getting out-of-hand on large projects. But for smaller projects, the simple file structure, and dependency tracking, and support for multiple commands hits a nice sweet spot.

### A consistent interface to project scripts

Thanks to these qualities, `make` shines as a way to create a consistent interface to commands across projects.

Most projects I work on require some kind of build process. To get to work, I need to re-learn the project’s tools, and the multiple commands needed to download dependencies, build assets, and start a dev server.

Building a site with [Kirby](https://getkirby.com/)[1](https://rosszurowski.com/log/2022/makefiles#user-content-fn-1) I need a mix of `php`, `tailwindcss`, `esbuild`, and `rsync` commands. For a [Next.js](https://nextjs.org/) site, I’m using their built-in CLI. And with [Fresh](https://fresh.deno.dev/), I don’t even have a `package.json` file — I’m using `deno run` and `deno fmt`. It’s annoying to track these commands down again and refamiliarize myself with where they live: in a JSON file? In a set of script files? In the README?

A Makefile acts as a conventional home for these tools and commands. It’s a single file at the root of the repository, that works with any language, and is easy read/add new commands to.

I leverage this conventionality to create consistent commands between different projects. For example, in every new project, I add a `make dev` command, which [auto-downloads dependencies](https://rosszurowski.com/log/2022/makefiles#auto-installing-node_modules), starts a dev server, and watches for changes, no matter the language.

For reference, here’s a list of common commands I’ll add:

*   `make dev` starts a development server with live reloading
*   `make build` builds a production-ready binary or set of files
*   `make deploy` tags a release for CI to build, or rsyncs files to a server
*   `make format` formats all code to a standard style, using [prettier](https://prettier.io/) or [gofmt](https://go.dev/blog/gofmt)
*   `make lint` runs code quality checks, like [eslint](https://eslint.org/) or [golanglint-ci](https://golangci-lint.run/)
*   `make test` runs a full set of test suites. Sometimes I’ll include `lint` scripts in here so there’s a single command to run in CI
*   `make clean` removes all build artifacts and downloaded dependencies
*   `make help` lists all the commands in a Makefile ([discussed here](https://rosszurowski.com/log/2022/makefiles#self-documenting-makefiles))

This “one command” and “one interface” is highly beneficial for teammates too. They can get started quickly, and if they want to learn more or tinker, the commands and dependency relationships are all documented in a single place.

### Recipes

Other articles cover the basics of how to write a Makefile in great depth,[2](https://rosszurowski.com/log/2022/makefiles#user-content-fn-2) so I’ll leave syntax aside and instead focus on sharing some common techniques that I use:

*   [Tasks without dependencies](https://rosszurowski.com/log/2022/makefiles#tasks-without-dependencies)
*   [Referencing node\_modules](https://rosszurowski.com/log/2022/makefiles#referencing-node_modules-binaries)
*   [Auto-installing node\_modules](https://rosszurowski.com/log/2022/makefiles#auto-installing-node_modules)
*   [Skipping re-runs of slow tasks](https://rosszurowski.com/log/2022/makefiles#skipping-re-runs-of-slow-tasks)
*   [Using environment variables](https://rosszurowski.com/log/2022/makefiles#using-environment-variables)
*   [Configuring tasks with default variables](https://rosszurowski.com/log/2022/makefiles#configuring-tasks-with-default-variables)
*   [Self-documenting Makefiles](https://rosszurowski.com/log/2022/makefiles#self-documenting-makefiles)
*   [Parallel dev servers](https://rosszurowski.com/log/2022/makefiles#parallel-dev-servers)
*   [Hermetic environments](https://rosszurowski.com/log/2022/makefiles#hermetic-environments)

* * *

### Tasks without dependencies

By default, `make` rule names refer to actual files to be built. If you write a rule like this:

Makefile

```
dev:
	@echo "Hello, world!"
```

And then later create a file named `dev`, `make` doesn’t run the commands.

```
$ touch dev
$ make dev
make: 'dev' is up to date.
```

For one-off scripts that you just want to run when you tell them to run, this default is a little annoying.

In these cases, add `.PHONY: <name>` to the end of the target definition. This tells `make` to skip the dependency checks and run the command every time:

Makefile

```
dev:
	@echo "Hello, world!"
.PHONY: dev
```

Now:

```
$ touch dev
$ make dev
Hello, world!
$ make dev
Hello, world!
```

I usually bundle the `.PHONY` line directly with the command it’s associated with, which makes it easy to tell which commands are “tasks” and which ones are instructions for building files:

Makefile

```
dev: node_modules ## Start a dev server
	@./node_modules/.bin/next dev
.PHONY: dev
 
lint: node_modules ## Lint files for code quality
	@./node_modules/.bin/next lint
.PHONY: lint
 
format: node_modules ## Format code to a standard style
	@./node_modules/.bin/eslint --fix 'src/**/*.{js,jsx,ts,tsx}'
	@./node_modules/.bin/prettier --write 'src/**/*.{js,jsx,ts,tsx}'
.PHONY: format
 
node_modules: package.json
	@yarn install
```

### Referencing node\_modules binaries

In web projects, you’ll often want to reference tools installed via `yarn` or `npm`, like `next`, `prettier`, or `eslint`. In npm/yarn scripts, you reference these utilities by name:

package.json

```
{
  "scripts": {
    "format": "prettier --write 'src/**/*.{js,jsx,ts,tsx}'"
  }
}
```

Under the hood, these scripts are stored in the `node_modules/.bin` directory. When you run `yarn dev`, it adds that directory to your `$PATH`, so running `yarn next` refers to the local installation instead of any global ones.

In Makefiles, we can reference these tools by being explicit. Write `./node_modules/.bin/<name>` before commands you want to use. So instead of `prettier`, you write:

Makefile

```
format: node_modules
	@./node_modules/.bin/prettier --write 'src/**/*.{js,jsx,ts,tsx}'
.PHONY: format
```

This explicitness has the benefit of throwing an error if the local `prettier` isn’t installed (but it should be if you [set up node\_modules as a dependency](https://rosszurowski.com/log/2022/makefiles#auto-installing-node_modules)).

There are techniques to modify your `$PATH` inside Makefiles, but they don’t seem to work consistently with the version of `make` that ships with macOS.[3](https://rosszurowski.com/log/2022/makefiles#user-content-fn-3) Better to keep things simple.

### Auto-installing node\_modules

When working with teammates unfamiliar with Node, I’ll sometimes help troubleshoot errors like this:

> I ran `yarn start` and got this error:
> 
> ```
> $ yarn start
> $ run-p start:*
> /bin/sh: run-p: command not found
> error Command failed with exit code 127.
> ```

This message means they tried running `yarn start` without running `yarn install` first. But it’s not terribly clear that’s how to resolve the error unless you know what you’re looking for.

Instead, with `make`, we can express the relationship between all these dependent tasks at once so we don’t need to think about them again.

For example, if we create a task to build node\_modules when package.json changes, we can leverage that in all the other scripts:

Makefile

```
dev: node_modules
	@./node_modules/.bin/next dev
.PHONY: dev
 
build: node_modules
	@./node_modules/.bin/next build
.PHONY: build
 
node_modules: package.json
	@yarn install
```

Running `make dev` will install node\_modules first, then run the `dev` command after. And on subsequent runs, it’ll skip the install step and just run the dev command.

### Skipping re-runs of slow tasks

For slow tasks, you can save time on subsequent runs by adding known dependencies to your rules.

For example, when working on a Next.js app locally, Next runs data fetching functions like `getStaticProps` on every page navigation. Sometimes, when I’m working on a feature that requires me to navigate between pages quickly (like transitions between pages), I run a production build to avoid the delay of the data fetching when previewing my work.

With `make`, I do this by defining the dependent files and folders, which we should rebuild the output for when they change. For this Next.js example, it means we can run a production build and start up the server. When running the command again, if the production build is up-to-date, we can just start up the server without the delay of rebuilding.

In order to get a list of all the files in a directory, we can use the `$(shell <cmd>)` expression and the `find` command:

Makefile

```
start: node_modules .next
	@./node_modules/.bin/next start
.PHONY: start
 
.next: node_modules next.config.js $(shell find src -type f -name "*.ts" -o -name "*.tsx")
	@./node_modules/.bin/next build
```

Now running `make start`:

```
$ make start
# ... next.js build output
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

Running it again skips the build and just starts the server, since the files haven’t changed.

```
$ make start
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

You can add different file extensions by adding more instances of `-o -name "*.<ext>"`. To add CSS files to the mix:

Makefile

```
.next: node_modules next.config.js $(shell find src -type f -name "*.ts" -o -name "*.tsx" -o -name "*.css")
	@./node_modules/.bin/next build
```

### Using environment variables

To use env variables you’ve defined in a local file, like a `.env`, you can use the following block at the top of your Makefile:

I find this makes it easy to store secret token for one-off tasks like API calls or just avoiding installing a dotenv dependency into my projects:

.env

```
SSH_USER="user"
SSH_HOST="example.com"
SSH_DIR="public_html"
```

Makefile

```
include .env
export
 
content:  ## Sync content from the server to the local environment.
	@rsync -avz --delete "$(SSH_USER)@$(SSH_HOST):$(SSH_DIR)/content/" content/
```

### Configuring tasks with default variables

Using `?=` you can set default variables that you can override outside of `make`. This lets you expose some configuration options to Makefile users.

Makefile

```
PORT ?= 9000
 
dev: node_modules
	@php -S localhost:$(PORT) index.php
.PHONY: dev
 
node_modules: package.json
	@yarn install
```

Now you can customize the port (while falling back to a default value) like so:

```
$ PORT=2000 make dev
PHP 8.2.1 Development Server (http://localhost:2000) started
```

### Self-documenting Makefiles

Makefiles can grow to contain lots of commands over time. One trick I’ve seen is to use this `make help` target to document important scripts:

```
help: ## Show this help
	@echo "\nSpecify a command. The choices are:\n"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[0;36m%-12s\033[m %s\n", $$1, $$2}'
	@echo ""
.PHONY: help
```

Using this, you can document commands with a `## comment` at the end of a line. For example:

Makefile

```
dev: node_modules ## Start a local development server
	@./node_modules/.bin/next dev
.PHONY: dev
 
format: node_modules ## Format all source files
	@./node_modules/.bin/prettier --write 'src/**/*.{ts,tsx}'
.PHONY: format
 
node_modules: package.json
	@yarn install
```

Adding this target means running `make help` will list all the targets labelled with the `## comment`. Use this to call out important commands for yourself or your teammates.

```
$ make help

Specify a command. The choices are:

  dev          Start a local development server
  format       Format all source files
  clean        Clean all built files
  help         Show this help
```

### Parallel dev servers

I’ll often want to run multiple long-lived processes while working on a project. For example, a recent website I worked on uses:

*   A `php -S` dev server
*   A `tailwindcss --watch` process
*   An `esbuild --watch` process

Unfortunately, like npm/yarn scripts, `make` doesn’t have meaningful tools for running long-lived parallel tasks. There _are_ technically a few ways you could get parallel servers running, but each technique gets a little fiddly for my tastes:

*   Using `make -j3 <a> <b> <c>` doesn’t treat processes as a group. So if one subprocess fails (eg. a syntax error stops the Tailwind `--watch` process), the others keep on going. You lose your live-updating changes without noticing until things are broken.
*   Shell background jobs with `<command> &` suffer the same process group issue, plus can sometimes leave processes hanging around after you Ctrl+C out.
*   External binaries like GNU’s `parallel` command, or `foreman` work, but they need separate installation steps.

Thankfully, `make` doesn’t care: we can just pop into language-specific tools that are suitable for the job. In Go projects, I’ll use a custom Go script. In Node projects, I’ll use the [concurrently](https://www.npmjs.com/package/concurrently) npm package:

```
yarn add --dev concurrently
```

Makefile

```
PORT ?= 9000
 
dev: node_modules
	@./node_modules/.bin/concurrently \
		'php -S localhost:$PORT index.php' \
		'./node_modules/.bin/esbuild src/*.ts --bundle --outdir=assets/ --watch' \
		'./node_modules/.bin/tailwindcss -i src/index.css -o assets/index.css --watch'
.PHONY: dev
 
node_modules: package.json
	@yarn install
```

You still get the nice `make dev` interface and dependency tracking, but proper parallel dev server handling behind-the-scenes.

**Update:** as of recently, I’ve been using [tandem](https://github.com/rosszurowski/tandem), a tool I built for running multiple commands as a process group. You pass it multiple commands and it runs them in parallel, shutting down the whole group if one fails.

It’s designed to be easily embedded in Makefiles with a one-line installation script. Add `.cache` to your `.gitignore` file, and use the following block:

Makefile

```
PORT ?= 9000
 
dev: .cache/tandem node_modules
	@.cache/tandem \
		'php -S localhost:$PORT index.php' \
		'esbuild src/*.ts --bundle --outdir=assets/ --watch' \
		'tailwindcss -i src/index.css -o assets/index.css --watch'
.PHONY: dev
 
.cache/tandem:
	@mkdir -p $$(dirname $@)
	@curl -fsSL https://raw.githubusercontent.com/rosszurowski/tandem/main/install.sh | bash -s -- --dest="$$(dirname $@)"
 
node_modules: package.json
	@yarn install
```

The first time you run `make dev`, it’ll download and cache it for future uses.

### Hermetic environments

Building on [the auto-installing node\_modules technique](https://rosszurowski.com/log/2022/makefiles#auto-installing-node_modules): you can get fancy with dependencies to download local versions of your _entire_ toolchain. This way everyone runs the same version of everything, without the slowness of using Docker.

This snippet reads yarn and node versions from files called `yarn.rev` and `node.rev`, downloads local copies into the `tool`, and uses those instances for all your scripts.

Makefile

```
export CACHE_PATH := .cache
export PATH := ./tool:$(PATH)
 
dev: node_modules ## Run a local development server
	@./node_modules/.bin/next dev
.PHONY: dev
 
clean: ## Clean all build artifacts
	@rm -rf ./tool
	@rm -rf ./cache
	@rm -rf ./node_modules
.PHONY: clean
 
node_modules: package.json tool/yarn tool/node
	@yarn install
 
# Reads a version number from a file called `node.rev`
tool/node: node.rev
	@mkdir -p tool
	@mkdir -p $(CACHE_PATH)/node
	@$(eval OS=$(shell uname -s | tr A-Z a-z))
	@$(eval ARCH=$(shell uname -m | sed -e "s/x86_64/x64/" | sed -e "s/aarch64/arm64/"))
	@read -r REV <$< && \
		cd $(CACHE_PATH)/node && \
		curl -L -o node.tar.gz https://nodejs.org/dist/v$$REV/node-v$$REV-$(OS)-$(ARCH).tar.gz && \
		tar --strip-components=1 -xzf node.tar.gz
	@echo "#!/bin/sh" > $@
	@echo 'exec /usr/bin/env PATH="$(CACHE_PATH)/node:$$PATH" "$(CACHE_PATH)/node/bin/node" "$$@"' >> $@
	@chmod +x $@
 
# Reads a version number from a file called `yarn.rev`
tool/yarn: yarn.rev
	@mkdir -p tool
	@mkdir -p $(CACHE_PATH)/yarn
	@read -r REV <$< && \
		cd $(CACHE_PATH)/yarn && \
		curl -L -o yarn.tar.gz https://github.com/yarnpkg/yarn/releases/download/v$$REV/yarn-v$$REV.tar.gz && \
		tar --strip-components=1 -xzf yarn.tar.gz
	@echo "#!/bin/sh" > $@
	@echo 'exec /usr/bin/env PATH="$(CACHE_PATH)/yarn:$$PATH" "$(CACHE_PATH)/yarn/bin/yarn" "$$@"' >> $@
	@chmod +x $@
```

This example probably pushes the limit of what should go directly in a Makefile vs. being broken out into a separate shell script or tool, but hopefully it demonstrates the extent to which you can automate your dev environment with Makefiles.

We use something similar to this [at Tailscale](https://tailscale.com/), and it greatly simplifies getting new teammates started, and upgrading versions of core dependencies like Go, Node, or Yarn.

* * *

### Limitations

While `make` is great for many projects, it’s not always the right thing to reach for. A few cases where you should avoid it:

*   **If you’re working with Windows.** Makefiles usually rely on a lot of UNIX tools and conventions, like `ENV=val` environment variables, or `awk`, `sed`, and `grep`, which don’t work on Windows. It’s possible to make cross-platform Makefiles, but if this is important to you, it may be better to use a tool that abstracts away platform differences.
*   **If you’re automating complex builds.** `make` gives you simple tools for simple builds. With involved chains of dependencies, Makefiles get unwieldly fast. If you start mucking with file modification timestamps, dealing with weird shell quoting rules or anything to do with automake, you’ve probably gone too far, and would be better served by another tool.
*   **If you already have a setup you’re happy with**. For simple projects, npm/yarn scripts can be enough! Don’t change if you’ve got something working. That said, I find Make’s speed, simplicity, and little bit of extra flexibility helpful, and suggest you give it a try.

### Reference Makefiles

*   The [stripe-cli](https://github.com/stripe/stripe-cli/blob/master/Makefile) has some great snippets, including a `// TODO:` comment finder, a Git tag generator, and Git hook installation step.
*   This [Tailscale docker desktop extension](https://github.com/tailscale/docker-extension/blob/main/Makefile) shows using a Makefile to make a nicer dev experience. Rather than manually building containers, installing them, and configuring dev server options, I composed them into some commands that made working on the project a lot easier.
*   This [Kirby CMS Makefile](https://gist.github.com/rosszurowski/24bdc2cce3bd440e6210c9c7d7164745) which has commands to update a vendored dependency, sync content with a remote server, and deploy via rsync to a PHP server.

Know other good web-centric Makefiles? [Let me know!](mailto:ross@rosszurowski.com)

1.  Here’s a [more complete Makefile example for Kirby](https://gist.github.com/rosszurowski/24bdc2cce3bd440e6210c9c7d7164745) if you’re interested in seeing how this approach expands. [↩](https://rosszurowski.com/log/2022/makefiles#user-content-fnref-1)
    
2.  I’ve found [this article](https://earthly.dev/blog/make-tutorial/) and [this one](https://www.olioapps.com/blog/the-lost-art-of-the-makefile/) to be decent introductions to the Makefile syntax. [↩](https://rosszurowski.com/log/2022/makefiles#user-content-fnref-2)
    
3.  More details about the specific weirdness are [in this gist](https://gist.github.com/rosszurowski/eee05cebb67fd869b7db1914b844db9c). [↩](https://rosszurowski.com/log/2022/makefiles#user-content-fnref-3)
