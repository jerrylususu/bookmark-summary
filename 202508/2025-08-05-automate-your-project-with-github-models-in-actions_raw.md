Title: Automate your project with GitHub Models in Actions

URL Source: https://github.blog/ai-and-ml/generative-ai/automate-your-project-with-github-models-in-actions/

Published Time: 2025-08-04T16:00:00+00:00

Markdown Content:
Learn how to integrate AI features with GitHub Models directly in GitHub Actions workflows.

August 4, 2025

|

6 minutes

*    Share: 
*   [](https://x.com/share?text=Automate%20your%20project%20with%20GitHub%20Models%20in%20Actions&url=https%3A%2F%2Fgithub.blog%2Fai-and-ml%2Fgenerative-ai%2Fautomate-your-project-with-github-models-in-actions%2F)
*   [](https://www.facebook.com/sharer/sharer.php?t=Automate%20your%20project%20with%20GitHub%20Models%20in%20Actions&u=https%3A%2F%2Fgithub.blog%2Fai-and-ml%2Fgenerative-ai%2Fautomate-your-project-with-github-models-in-actions%2F)
*   [](https://www.linkedin.com/shareArticle?title=Automate%20your%20project%20with%20GitHub%20Models%20in%20Actions&url=https%3A%2F%2Fgithub.blog%2Fai-and-ml%2Fgenerative-ai%2Fautomate-your-project-with-github-models-in-actions%2F)

[GitHub Models](https://docs.github.com/en/github-models) brings AI into your [GitHub Actions](https://github.com/features/actions) workflows, helping you automate triage, summarize, and more — right where your project lives.

Let’s explore three ways to integrate and automate the use of GitHub Models in GitHub Actions workflows, from the most straightforward to the most powerful.

But first: Add the right permissions
------------------------------------

Before you can use GitHub Models in your Actions workflows, you need to grant your workflow access to AI models. Without the correct permissions, any step that tries to call an AI model will fail.

Giving permissions to use GitHub Models is one line in your permissions block:

```
permissions:
  contents: read
  issues: write
  models: read
```

These permissions will give your workflow the ability to read repository content; to read, create, or update issues and comments; and, most importantly for this tutorial, to enable access to GitHub Models.

Example one: Request more information in bug reports
----------------------------------------------------

_This example will show you how to use the AI inference action and how to use AI to create branching logic. You can find the full_[_workflow_](https://github.com/github-samples/models-in-actions/blob/main/workflows/bug-reproduction-check/bug-reproduction-check.yml)_in this repo._

One of the most time-consuming and menial parts of our work as developers is triaging new issues that often contain too little information to reproduce.

Instead of having to spend time assessing and responding to these issues, you can use the AI inference action lets you call leading AI models to analyze or generate text as part of your workflow. The workflow below, for example, will automatically check if new bug reports have enough information to be actionable, and respond if they’re not.

To set up the workflow, create a new file in your repository’s `.github/workflows` directory called `bug-reproduction-instructions.yml` (create the directory if it doesn’t exist). It will trigger whenever a new issue is opened and then fetch the issue’s title and body for future steps.

```
name: Bug Report Reproduction Check

on:
  issues:
    types: [opened]

permissions:
  contents: read
  issues: write
  models: read

jobs:
  reproduction-steps-check:
    runs-on: ubuntu-latest
    steps:
      - name: Fetch Issue
        id: issue
        uses: actions/github-script@v7
        with:
          script: |
            const issue = await github.rest.issues.get({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number
            })
            core.setOutput('title', issue.data.title)
            core.setOutput('body', issue.data.body)
```

Now that your workflow has the necessary context, create a new step. This step should only execute if the issue is tagged with a bug label. This step will use the AI inference action, configured with a system prompt that outlines the characteristics of effective reproduction instructions, and provide the value from the issue.

```
- name: Analyze Issue For Reproduction
  if: contains(join(github.event.issue.labels.*.name, ','), 'bug')
  id: analyze-issue
  uses: actions/ai-inference@v1
  with:
  model: mistral-ai/ministral-3b
  system-prompt: |
    Given a bug report title and text for an application, return 'pass' if there is enough information to reliably reproduce the issue, meaning the report clearly describes the steps to reproduce the problem, specifies the expected and actual behavior, and includes environment details such as browser and operating system; if any of these elements are missing or unclear, return a brief description of what is missing in a friendly response to the author instead of 'pass'. Consider the following title and body:
  prompt: |
    Title: ${{ steps.issue.outputs.title }}
    Body: ${{ steps.issue.outputs.body }}
```

This step will either return a `pass` if there is enough information provided (more on why we’re doing this in a moment), or return a response detailing what is missing.

You can use over 40 AI models available in the [GitHub Models catalog](https://github.com/marketplace?type=models). Just swap out the model value with the identifier on each model’s page.

Next, add one final step, which will post the comment only if the value returned was not `pass`.

```
- name: Comment On Issue
  if: contains(join(github.event.issue.labels.*.name, ','), 'bug') && steps.analyze-issue.outputs.response != 'pass'
  uses: actions/github-script@v7
  env:
    AI_RESPONSE: steps.analyze-issue.outputs.response
    with:
      script: |
        await github.rest.issues.createComment({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: context.issue.number,
          body: process.env.AI_RESPONSE
        })
```

By prompting the AI model to return a fixed string if certain criteria are met (in this case, a good bug report was filed with enough reproduction information), we can create AI-powered conditional logic in our workflows.

![Image 1: An issue on GitHub named "Doesn't work on firefox" with no description and a bug label. The github-actions bot responds asking for more information - specifically reproduction steps, expected and actual behavior, and browser and operating system details.](https://github.blog/wp-content/uploads/2025/07/image1_5f1e88.png?resize=1024%2C755)
Example two: Creating release notes from merged pull requests
-------------------------------------------------------------

_This example will show you how to use the gh CLI with the_ _gh-models_ _extension. You can find the full_[_workflow_](https://github.com/github-samples/models-in-actions/blob/main/workflows/add-merged-pr-to-changelog/add-merged-pr-to-changelog.yml)_in this repo._

Generating thorough release notes with new versions of a project can take time, between collating what’s changed and finding a succinct way to explain it to users.

But you can actually trigger GitHub Actions workflow steps when pull requests are merged and use the GitHub CLI to gather information and take action, including calling models. The workflow below, for example, will summarize merged pull requests and add them to a release notes issue — showing how you can save time and energy with each pull request.

To set up this workflow, create a new label called `release`, and create one issue with this label called `Publish next release changelog`. Then, create a new file in your repository’s `.github/workflows` directory called `release-notes.yml`. It will trigger whenever a new pull request is closed, and its single job conditionally will run only if its merged status is true.

```
name: Add to Changelog

on:
  pull_request:
    types:
      - closed

permissions:
  pull-requests: read
  issues: write
  contents: read
  models: read

jobs:
  add_to_changelog:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
```

Install the `gh-models` extension with a new step, providing your workflow’s token which now has permissions to use GitHub Models:

```
- name: Install gh-models extension
  run: gh extension install https://github.com/github/gh-models
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

The rest of the steps will take place in one step:

```
- name: Summarize pull request and append to release issue
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |-
    PR_NUMBER="${{ github.event.pull_request.number }}"

    # Fetch PR and save to a file
    gh pr view "$PR_NUMBER" --json title,body,comments,reviews > pr.json
    
    # Generate a summary using the model by reading from file
    cat pr.json | gh models run xai/grok-3-mini \
      "Given the following pull request information, generate a single, clear, and concise one-line changelog entry that summarizes the main change (feature, fix, or bug) introduced by this PR. Use neutral, user-facing language and avoid technical jargon or internal references. Only write the line, with no additional introduction or explanation text." > summary.md

    # Fetch release issue number
    RELEASE_ISSUE=$(gh issue list --label release --limit 1 --json number --jq '.[0].number')

    # Fetch current release issue body
    RELEASE_ISSUE_BODY=$(gh issue view "$RELEASE_ISSUE" --json body --jq '.body')

    # Append summary to release issue body
    FORMATTED_LINE="- $(cat summary.md) (#$PR_NUMBER)"
    NEW_BODY="${RELEASE_ISSUE_BODY}"$'\n'"$FORMATTED_LINE"

    # Update the release issue with the new body
    gh issue edit "$RELEASE_ISSUE" --body "$NEW_BODY"
```

The pull request’s title, body, comments, and reviews are grabbed and passed to a model using the `gh models run` command. The release issue is fetched and updated with the summarized line.

![Image 2: A pull request named Publish Next Release Changelog. The description has two bullet list items - each one describing a change in 8-12 words with a link to the merged pull request.](https://github.blog/wp-content/uploads/2025/07/image2_f6eb85.png?resize=1024%2C438)
Example three: summarizing and prioritizing issues
--------------------------------------------------

_This example demonstrates how to use the ⁠GitHub CLI with the ⁠_ _gh-models_ _extension and a prompt file to automate a more complex, scheduled workflow. Review the full_[_workflow file_](https://github.com/github-samples/models-in-actions/blob/main/workflows/weekly-issue-summary/weekly-issue-summary.yml)_and_[_prompt file_](https://github.com/github-samples/models-in-actions/blob/main/workflows/weekly-issue-summary/issue-summary.prompt.yml)_._

It’s easy to lose track of new activity, especially as your project grows. And even then, actually keeping track of repeated issues and themes requires a surprising amount of time. To open a weekly issue to summarize, thematize, and prioritize newly opened issues, you can trigger GitHub Actions on a schedule.

To set up the workflow, create a new file in your repository’s .github/workflows directory called weekly-issue-summary.yml. It will trigger every Monday at 9 a.m.

```
name: Weekly Issue Summary

on:
  workflow_dispatch:
  schedule:
    - cron: '0 9 * * 1'

permissions:
  issues: write
  contents: read
  models: read

jobs:
  create_weekly_summary:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install gh-models extension
        run: gh extension install https://github.com/github/gh-models
        env:
          GH_TOKEN: ${{ github.token }}
```

Create a new step to get open issues from the last week and save them to a file:

```
- name: Get issues from the past week and summarize
  id: get_issues
    run: |-
      LAST_WEEK=$(date -d "7 days ago" +"%Y-%m-%d")
      gh search issues "created:>$LAST_WEEK" --state=open --json title,body,url --repo ${{ github.repository }} > issues.json

      # further code will go here
    env:
      GH_TOKEN: ${{ github.token }}
```

Pass in the week’s worth of issues to a `gh models run` call:

`cat issues.json | gh models run --file prompts/issue-summary.prompt.yml > summary.md`
Unlike the previous example, a separate prompt file is being used by this command. Create a prompts directory in your repository and, within it, a `issue-summary.prompt.yml` file:

```
name: Issue summarizer
description: Summarizes weekly issues
model: openai/gpt-4.1
messages:
  - role: system
    content: You are a helpful issue summarizer. When given issue content, respond in markdown format.
  - role: user
    content: "Please summarize the following issues into a few short bullet points. Include links if provided. If possible, pull out general themes and help the team prioritize based on impact. Issues begin here:\n {{input}}"
```

This file contains all of the required information: the model, the system and user prompts, and, optionally, parameters used to tune your response. By using a `.prompt.yml` file, you can also leverage the GitHub Models’ repository integration to iterate on the prompt with a rich UI.

Back in the workflow file, straight under the `gh models run` command, create the issue with the summary:

```
ISSUE_TITLE="Issue Summary - $(date -d '7 days ago' '+%B %d') to $(date '+%B %d')"
gh issue create --title "$ISSUE_TITLE" --label summary --body-file summary.md
```
![Image 3: An issue with the title "Issue Summary - June 16 to June 23". It has three sections - an issue summary which details and links each issue that has been opened, general themes which contains three groupings for the issues, and suggested prioritization. The top issue is on data integrity - issue 37.](https://github.blog/wp-content/uploads/2025/07/image3_6c2c47.png?resize=972%2C1024)
Whether you start simple with the AI inference action, use the `gh-models` CLI with inline prompts, or create full-featured, prompt-driven workflows, GitHub Models makes it easy to scale your processes with AI.

Just add the right permissions, pick an example above, and try out GitHub Models in your next workflow.

Written by
----------

![Image 4: Kevin Lewis](https://avatars.githubusercontent.com/u/1461554?v=4&s=200)

Senior Developer Advocate

Related posts
-------------

We do newsletters, too
----------------------

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address