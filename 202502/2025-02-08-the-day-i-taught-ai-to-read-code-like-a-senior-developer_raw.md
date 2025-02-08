Title: The day I taught AI to read code like a Senior Developer

URL Source: https://nmn.gl/blog/ai-senior-developer

Published Time: 2025-01-05T00:00:00+00:00

Markdown Content:
_A messy experiment that changed how we think about AI code analysis_

Last week, I watched our AI choke on a React codebase - again. As timeout errors flooded my terminal, something clicked. We’d been teaching AI to read code like a fresh bootcamp grad, not a senior developer.

Here’s what I mean.

The Bootcamp vs Senior Mindset
------------------------------

Remember your first day reading production code? Without any experience with handling mature codebases, you probably quickly get lost in the details\[0\]

But watch a senior dev review a massive PR:

*   They jump straight to the core files
*   Group changes by feature (“all auth changes, all db changes”)
*   Build a mental model of architecture first
*   Only then dive into implementation

Obvious in hindsight, right? This realization led us to completely rewire our analyzer.

The Experiment
--------------

Instead of dumping files linearly, [we built a context-aware grouping system](https://nmn.gl/blog/giga):

```
interface FileGroup {
  files: ProjectFile[];
  totalSize: number;
  groupContext: string; // 'auth', 'database', etc.
}

export const groupFiles = (files: ProjectFile[]): FileGroup[] => {
  // Group files by related functionality and size
  const fileInfos = files.map(file => ({
    file,
    size: file.content?.length || 0,
    context: getFileContext(file.path)
  }));

  // Process larger, more important files first
  fileInfos.sort((a, b) => b.size - a.size);

  const groups: FileGroup[] = [];
  let currentGroup = createEmptyGroup();

  for (const { file, size, context } of fileInfos) {
    if (shouldStartNewGroup(currentGroup, size, context)) {
      groups.push(currentGroup);
      currentGroup = createNewGroup(file, size, context);
    } else {
      addFileToGroup(currentGroup, file, size);
    }
  }

  return groups;
}
```

Then we changed how we prompt the AI. Instead of “analyze this file”, we give it context about the feature group first:

```
const buildGroupPrompt = (group: FileGroup): string => {
  return `
    Analyzing authentication system files:
    - Core token validation logic
    - Session management
    - Related middleware
    
    Focus on:
    1. How these integrate with existing auth patterns
    2. Security implications
    3. Performance impact on other systems

    Files to analyze:
    ${formatFiles(group.files)}
  `;
}
```

The Holy Shit Moment
--------------------

The results broke our testing scripts. We thought it was a bug.

The AI went from:

```
"This file contains authentication logic using JWT tokens"
```

To:

```
"Warning: This auth change could impact websocket connections.
The token refresh logic shares patterns with the notification 
service (added last month), suggesting a potential race 
condition during high-traffic socket reconnects.

Related PR: #1234 (merged last week) modified the same
retry logic. Consider adding backoff."
```

That’s senior dev level awareness. It was catching connections we hadn’t explicitly taught it about.

What Actually Changed?
----------------------

The magic isn’t in fancy ML or bigger models. It’s in mirroring how senior devs think:

1.  **Context First**: We front-load system understanding before diving into code
2.  **Pattern Matching**: Group similar files to spot repeated approaches
3.  **Impact Analysis**: Consider changes in relation to the whole system
4.  **Historical Understanding**: Track why code evolved certain ways

The Unexpected Side Effects
---------------------------

The system started catching things we didn’t design for:

*   Spotting copy-pasted code across different features
*   Flagging inconsistent error handling patterns
*   Warning about potential performance bottlenecks
*   Suggesting architectural improvements based on usage patterns

Why This Matters
----------------

Every few days there’s a new “AI-powered IDE” on Product Hunt. They’re solving the wrong problem. Making code suggestions without deep context is like having a brilliant junior dev who just joined yesterday - they’ll write clean code that subtly breaks everything.

The key isn’t better code generation. It’s better code understanding.

Open Questions
--------------

We’re still figuring out:

*   When to refresh vs preserve historical understanding
*   How to handle conflicting patterns in different parts of the system
*   Whether to expose uncertainty in the analysis

What’s Next?
------------

I’m curious if we can teach AI to spot other senior dev instincts:

*   Identifying tech debt before it happens
*   Suggesting architectural improvements
*   Catching security issues from usage patterns
*   Understanding unwritten team conventions

The problem isn’t making AI write more code. It’s teaching it to think about code the way experienced developers do.

\[0\] Previously said _You probably did what I did - start at line 1, read every file top to bottom, get lost in the details._, edited in response to [feedback from advael](https://news.ycombinator.com/item?id=42602156)
