Title: Spec-driven development: Using Markdown as a programming language when building with AI

URL Source: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/

Published Time: 2025-09-30T12:07:46-07:00

Markdown Content:
The usual workflow with AI coding agents like GitHub Copilot is simple: _“Write app A that does X_._“_ You start with that seed, then iterate: _“Add feature Y,”_ _“Fix bug Z_._“_ This works, at least until the agent loses track of your app’s purpose or past decisions.

If you’re new to AI coding agents, the change is subtle. Suddenly, the agent asks you to repeat things you’ve already explained, or suggests changes that ignore your previous instructions. Sometimes, it forgets why a feature exists, or proposes solutions that contradict earlier choices.

Some AI coding agents try to address this by supporting custom instructions files. For example, GitHub Copilot [supports](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=vscode)`copilot-instructions.md`. You can put your app’s purpose and design decisions in this Markdown file, and GitHub Copilot will read it every time it generates code.

When I’m in a coding rush, I often forget to update `copilot-instructions.md` after asking GitHub Copilot to do things. It feels redundant to put the same information into both the chat prompt and the instructions file.

**Which made me wonder:****_What if I “wrote” the entire app in the Markdown instructions file?_**

For my latest pet project — [GitHub Brain MCP Server](https://github.com/wham/github-brain) — I tried exactly that by writing the app code in Markdown and letting GitHub Copilot _compile_ it into actual Go code. As a result, I rarely edit or view the app’s Go code directly.

This process should work with any AI coding agent and programming language, though I’ll use VS Code, GitHub Copilot, and Go as examples. [GitHub Brain MCP Server](https://github.com/wham/github-brain) will be my example app throughout this post.

Let’s jump in.

Setup: What I used to get started
---------------------------------

There are four key files:

```
.
├── .github/
│   └── prompts/
│       └── compile.prompt.md
├── main.go
├── main.md
└── README.md
```

At a high level, I edit `README.md` or `main.md` to develop the app, invoke `compile.prompt.md` to let the AI coding agent generate `main.go`, then build and run `main.go` like any other Go app. Next, I’ll break down each file and the workflow.

### README.md: User-facing documentation

The example app, [GitHub Brain MCP Server](https://github.com/wham/github-brain), is a command-line tool. Its `README.md` provides clear, user-facing instructions for installation and usage. If you write libraries, this file should contain API documentation. Below is a condensed excerpt from the example app’s [`README.md`](https://github.com/wham/github-brain/blob/main/README.md):

```
# GitHub Brain MCP Server

**GitHub Brain** is an experimental MCP server for summarizing GitHub discussions, issues, and pull requests.

## Usage

```sh
go run main.go <command> [<args>]
```

**Workflow:**

1. Populate the local database with the `pull` command.
2. Start the MCP server with the `mcp` command.

### `pull`

Populate the local database with GitHub data.

Example:

```sh
go run main.go pull -o my-org
```

Arguments:

- `-t`: Your GitHub personal access token. **Required.**
- `-o`: The GitHub organization to pull data from. **Required.**
- `-db`: Path to the SQLite database directory. Default: `db` folder in the current directory.

### `mcp`

Start the MCP server using the local database.

...README.md continues...
```

Nothing special here , just regular documentation. But it gets interesting when this file is included in `main.md`.

### main.md: AI coding agent specification

`main.md` is the actual source code of the app: the Markdown instructions file. Whenever I need to add features or fix bugs, I edit this file. Here’s the opening of the example app’s [`main.md`](https://github.com/wham/github-brain/blob/main/main.md):

```
# GitHub Brain MCP Server

AI coding agent specification. User-facing documentation in [README.md](README.md).

## CLI

Implement CLI from [Usage](README.md#usage) section. Follow exact argument/variable names. Support only `pull` and `mcp` commands.

## pull

- Resolve CLI arguments and environment variables into `Config` struct:
  - `Organization`: Organization name (required)
  - `GithubToken`: GitHub API token (required)
  - `DBDir`: SQLite database path (default: `./db`)
- Use `Config` struct consistently, avoid multiple environment variable reads
- Pull items: Repositories, Discussions, Issues, Pull Requests, Teams
- Use `log/slog` custom logger for last 5 log messages with timestamps in console output

...main.md continues...
```

Notice how the user-facing documentation from `README.md` is embedded in the specification. This keeps documentation and implementation in sync. If I want to add an alias for the `-o` argument, I just update [`README.md`](http://readme.md/) with no extra steps required.

Here’s another snippet from the example app’s [`main.md`](https://github.com/wham/github-brain/blob/main/main.md):

```
### Discussions

- Query discussions for each repository with `has_discussions_enabled: true`
- Record most recent repository discussion `updated_at` timestamp from database before pulling first page

```graphql
{
  repository(owner: "<organization>", name: "<repository>") {
    discussions(first: 100, orderBy: { field: UPDATED_AT, direction: DESC }) {
      nodes {
        url
        title
        body
        createdAt
        updatedAt
        author {
          login
        }
      }
    }
  }
}
```

- If repository doesn't exist, remove the repository, and all associated items from the database and continue
- Query discussions ordered by most recent `updatedAt`
- Stop pulling when hitting discussions with `updatedAt` older than recorded timestamp
- Save or update by primary key `url`
- Preserve the discussion markdown body

...main.md continues...
```

This is effectively programming in Markdown and plain English: storing variables, loops, and logical conditions. You get all the usual keywords — `if`, `foreach`, or `continue`. It’s a blend of structural and declarative styles, with Markdown links `[]()` for imports.

The database schema is also coded in Markdown:

```
## Database

SQLite database in `{Config.DbDir}/{Config.Organization}.db` (create folder if needed). Avoid transactions. Save each GraphQL item immediately.

### Tables

#### table:repositories

- Primary key: `name`
- Index: `updated_at`

- `name`: Repository name (e.g., `repo`), without organization prefix
- `has_discussions_enabled`: Boolean indicating if the repository has discussions feature enabled
- `has_issues_enabled`: Boolean indicating if the repository has issues feature enabled
- `updated_at`: Last update timestamp

...main.md continues...
```

### compile.prompt.md: AI coding agent prompt

`compile.prompt.md` uses GitHub Copilot’s [prompt file](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file) format. This repeatable prompt tells the agent to compile `main.md` into `main.go`. Here’s [`compile.prompt.md`](https://github.com/wham/github-brain/blob/main/.github/prompts/compile.prompt.md) from the example app:

```
---
mode: agent
---

- Update the app to follow [the specification](../../main.md)
- Build the code with the VS Code tasks. Avoid asking me to run `go build` or `go test` commands manually.
- Fetch the GitHub home page for each used library to get a documentation and examples.
```

I keep this prompt simple . The real information is in [`main.md`](http://main.md/), after all. This example uses GitHub Copilot’s format, but keeping it simple makes it portable to other AI coding agents.

The workflow to bring this all together
---------------------------------------

The development loop is straightforward:

1.   Edit the specification in `main.md` or `README.md`.
2.   Ask the AI coding agent to compile it into Go code.
3.   Run and test the app. Update the spec if something doesn’t work as expected.
4.   Repeat.

In GitHub Copilot for VS Code, use the `/` command to invoke the prompt.

![Image 1: Screenshot showing the use of the / command in GitHub Copilot for VS Code to invoke the AI coding agent prompt.](https://github.blog/wp-content/uploads/2025/09/image-2.png?resize=1024%2C516)
For smaller specs, GitHub Copilot usually catches changes automatically. As the spec grows, I nudge it in the right direction by appending _”focus on <the-change>”_.

![Image 2: Screenshot demonstrating how to prompt GitHub Copilot in VS Code to focus on a specific change using the / command.](https://github.blog/wp-content/uploads/2025/09/image-2_87448b.png?resize=1770%2C2836)
### Coding

Coding in `main.md` is sometimes harder than writing Go directly . You have to clearly describe what you want, which might be the hardest part of software development 😅. Fortunately, you can use GitHub Copilot to help with this, just like you probably do with your Go code daily.

Here we ask it to add pagination to all MCP tools in `main.md`. Copilot not only saves us from doing repetitive work, but it also recommends proper pagination style and parameter names.

![Image 3: Screenshot showing GitHub Copilot in VS Code recommending pagination style and parameter names for MCP tools in the Markdown specification.](https://github.blog/wp-content/uploads/2025/09/image-4.png?resize=1760%2C2672)
### Linting

`main.md` can get messy like any code. To help with this, you can ask Copilot to clean it up. Here’s [lint.prompt.md](https://github.com/wham/github-brain/blob/main/.github/prompts/lint.prompt.md) from the example app:

```
---
mode: agent
---

- Optimize [the app specification](../../main.md) for clarity and conciseness
- Treat the english language as a programming language
- Minimize the number of synonyms - i.e. pull/get/fetch. Stick to one term.
- Remove duplicate content
- Preserve all important details
- Do not modify the Go code with this. Only optimize the Markdown file.
- Do not modify this prompt itself.
```

Like with `compile.prompt.md`, I use the `/` command to invoke this prompt. The AI coding agent lints `main.md`, and if the result looks good, I can compile it to Go with `compile.prompt.md`.

![Image 4: Screenshot of GitHub Copilot in VS Code cleaning up and linting the Markdown specification for improved clarity and conciseness.](https://github.blog/wp-content/uploads/2025/09/image-3_bc6205.png?resize=1742%2C2416)
Closing thoughts
----------------

After a few months using this workflow, here are my observations:

*   **It works!** And it gets better with each agentic update to Copilot.
*   **Compilation slows down as `main.go` grows.** Something I want to work on next is modifying the spec to break compiled code into multiple modules — by adding _“Break each ## section into its own code module.”_
*   **Testing?** I haven’t tried adding tests yet. But even with spec-driven workflows, testing remains essential. The spec may describe intended behavior, but tests verify it.

Something else I want to try next? Discarding all Go code and regenerating the app from scratch in another language. Will the new code work right away?

The rapid advances in this field are really encouraging, and I hope my experimental workflows give you some practical ideas to try.

Written by
----------

![Image 5: Tomas Vesely](https://avatars.githubusercontent.com/u/448809?v=4&s=200)

Engineering manager on the GitHub Licensing team.

Explore more from GitHub
------------------------

![Image 6: Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

### Docs

Everything you need to master GitHub, all in one place.

[Go to Docs](https://docs.github.com/)

![Image 7: GitHub](https://github.blog/wp-content/uploads/2024/07/Icon_95220f.svg)

### GitHub

Build what’s next on GitHub, the place for anyone from anywhere to build anything.

[Start building](https://github.com/)

![Image 8: Customer stories](https://github.blog/wp-content/uploads/2024/07/Icon_da43dc.svg)

### Customer stories

Meet the companies and engineering teams that build with GitHub.

[Learn more](https://github.com/customer-stories)

![Image 9: GitHub Universe 2025](https://github.blog/wp-content/uploads/2024/04/Universe24-North_Star.svg)

### GitHub Universe 2025

Last chance: Save $700 on your IRL pass to Universe and join us on Oct. 28-29 in San Francisco.

[Register now](https://githubuniverse.com/?utm_source=Blog&utm_medium=GitHub&utm_campaign=module)