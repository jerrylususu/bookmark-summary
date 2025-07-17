Title: How to actually use Model Context Protocol

URL Source: https://www.seangoedecke.com/how-to-actually-use-mcp/

Markdown Content:
Everyone’s very excited about [Model Context Protocol](https://www.seangoedecke.com/model-context-protocol), or MCP for short. In a sentence, MCP is a universal protocol for exposing sets of tools to AI agents - instead of manually adding “hit the Issues API” and “create a PR” tools to my agent, I can instead just connect the GitHub [MCP server](https://github.com/github/github-mcp-server) and get a pre-defined set of GitHub tools.

Yesterday I wrote some inference code that used an MCP server to discover and call tools. It was much more fiddly than I expected. There’s lots of support for adding MCP servers to your IDE, or standing up your own MCP server. But weirdly enough, there’s no straightforward guide to connecting an MCP server to your _code_.

I was expecting to be able to just use the OpenAI SDK with a `mcp:` field (or a tool with `type: mcp` in the tools list). But in fact you’ve got to do it yourself. If you’re writing your own agent or AI tool, what do you need to do to hook up MCP?

Fortunately, the work I did yesterday was in an [open-source repo](https://github.com/actions/ai-inference), so for once I can actually show it! I was connecting up the GitHub MCP server, but the core concepts should work for any server or language. Here’s the rough outline:

1.   Import the relevant MCP libraries
2.   On startup, handshake with the MCP server and fetch the list of tools
3.   Convert that tool format to whatever format your LLM inference provider expects
4.   Supply those tools to your LLM inference request in the API call
5.   In the response, check if the model wanted to call a tool. If so, pass that tool call request to the MCP server
6.   Include the tool call response in another LLM inference request and goto (4), so the model can decide its next move based on the tool output
7.   If the model doesn’t want to call any tools, treat the response as a normal response (show it to the user or feed it into the next part of the program, etc)

You can see the real implementation [here](https://github.com/actions/ai-inference/blob/main/src/inference.ts#L73) and [here](https://github.com/actions/ai-inference/blob/main/src/mcp.ts). Let’s walk through it in a bit more detail. The first [step](https://github.com/actions/ai-inference/blob/main/src/mcp.ts#L38) is to handshake to the server and fetch tools:

```
export async function connectToGitHubMCP(
  token: string
): Promise<GitHubMCPClient | null> {
  const githubMcpUrl = 'https://api.githubcopilot.com/mcp/'

  core.info('Connecting to GitHub MCP server...')

  const transport = new StreamableHTTPClientTransport(new URL(githubMcpUrl), {
    requestInit: {
      headers: {
        Authorization: `Bearer ${token}`,
        'X-MCP-Readonly': 'true'
      }
    }
  })

  const client = new Client({
    name: 'ai-inference-action',
    version: '1.0.0',
    transport
  })

  try {
    await client.connect(transport)
  } catch (mcpError) {
    core.warning(`Failed to connect to GitHub MCP server: ${mcpError}`)
    return null
  }

  core.info('Successfully connected to GitHub MCP server')

  const toolsResponse = await client.listTools()
  core.info(
    `Retrieved ${toolsResponse.tools?.length || 0} tools from GitHub MCP server`
  )

  // Map GitHub MCP tools → Azure AI Inference tool definitions
  const tools = (toolsResponse.tools || []).map((t) => ({
    type: 'function' as const,
    function: {
      name: t.name,
      description: t.description,
      parameters: t.inputSchema
    }
  }))

  core.info(`Mapped ${tools.length} GitHub MCP tools for Azure AI Inference`)

  return { client, tools }
}
```

Note that `StreamableHTTPClientTransport` is an MCP SDK client primitive - it’s the “talk to your server over HTTP” helper - and the `X-MCP-Readonly` means that we’re restricted to readonly tools (no pushing commits). Also note that we do a bit of format-munging on the list of tools (adding a `function` type to match the Azure [SDK](https://learn.microsoft.com/en-us/rest/api/aifoundry/model-inference/get-chat-completions/get-chat-completions?view=rest-aifoundry-model-inference-2024-05-01-preview&tabs=HTTP#chatcompletionstooldefinition) structure). But aside from that this should all be very straightforward: create an MCP client, `connect`, and fetch the list of tools.

It’s critical to note that this code is intended to execute inside a [GitHub Action](https://github.com/marketplace/actions/ai-inference), so the `token` is specific to the workflow and will be automatically user-scoped. If you’re building a web server, _do not use a single admin token_ for your MCP server. Remember that anyone who can control the input to the model can trigger MCP actions, so never give an MCP server a token that has more privileges than the user interacting with it. I write a lot more about this [here](https://www.seangoedecke.com/ai-security).

Here’s the actual inference code:

```
export async function mcpInference(
  request: InferenceRequest,
  githubMcpClient: GitHubMCPClient
): Promise<string | null> {
  core.info('Running GitHub MCP inference with tools')

  const client = ModelClient(
    request.endpoint,
    new AzureKeyCredential(request.token),
    {
      userAgentOptions: { userAgentPrefix: 'github-actions-ai-inference' }
    }
  )

  const messages = [
    {
      role: 'system',
      content: request.systemPrompt
    },
    { role: 'user', content: request.prompt }
  ]

  let iterationCount = 0
  const maxIterations = 5 // Prevent infinite loops

  while (iterationCount < maxIterations) {
    iterationCount++
    core.info(`MCP inference iteration ${iterationCount}`)

    const requestBody = {
      messages: messages,
      max_tokens: request.maxTokens,
      model: request.modelName,
      tools: githubMcpClient.tools
    }

    const response = await client.path('/chat/completions').post({
      body: requestBody
    })

    if (isUnexpected(response)) {
      handleUnexpectedResponse(response)
    }

    const assistantMessage = response.body.choices[0].message
    const modelResponse = assistantMessage.content
    const toolCalls = assistantMessage.tool_calls

    core.info(`Model response: ${modelResponse || 'No response content'}`)

    messages.push({
      role: 'assistant',
      content: modelResponse || '',
      ...(toolCalls && { tool_calls: toolCalls })
    })

    if (!toolCalls || toolCalls.length === 0) {
      core.info('No tool calls requested, ending GitHub MCP inference loop')
      return modelResponse
    }

    core.info(`Model requested ${toolCalls.length} tool calls`)

    // Execute all tool calls via GitHub MCP
    const toolResults = await executeToolCalls(
      githubMcpClient.client,
      toolCalls
    )

    // Add tool results to the conversation
    messages.push(...toolResults)

    core.info('Tool results added, continuing conversation...')
  }

  core.warning(
    `GitHub MCP inference loop exceeded maximum iterations (${maxIterations})`
  )

  // Return the last assistant message content
  const lastAssistantMessage = messages
    .slice()
    .reverse()
    .find((msg) => msg.role === 'assistant')

  return lastAssistantMessage?.content || null
}
```

Note that we’re doing this in a loop, because we’re now in agentic mode, and agentic just means “tools in a loop”. We run the first inference with the list of tools, and if the model response contains `tool_calls`, we call those tools (via `githubMcpClient.callTool()`, which is what `executeToolCalls` does [under the hood](https://github.com/actions/ai-inference/blob/main/src/mcp.ts#L92)), pack the result into a new message, and keep looping. This lets the model go through multiple steps: e.g. decide “I need to fetch the user’s recent PRs”, then look at them, then decide “OK, give me more detail about this PR”, then eventually return a response that’s informed by that detail.

This feels a little heavyweight for what is a pretty simple protocol. I can see why you can’t just have a `tools: mcp("https://api.githubcopilot.com/mcp/", token)` helper, since repeatedly fetching the list of tools per-inference request puts undue load on the server (especially if you have to do a handshake each time). But why can’t I do something like:

```
client = mcpClient("https://api.githubcopilot.com/mcp/", token)

while (true) {
    res = await inference(prompt, tools: client.toolsForAzureSDK)
    // ... all the stuff about calling tools and putting them in the loop
}
```

Or better yet:

```
client = mcpClient("https://api.githubcopilot.com/mcp/", token)
res = await agenticInference(prompt, tools: client.toolsForAzureSDK, maxLoops: 5)
```

Most people are still using MCP in their existing tools instead of writing their own code around it. The tooling in this space is still relatively immature. It took me way too long (like an hour) to figure out (a) that I had to wire most of this up myself, and (b) how it was supposed to work. Hopefully me writing it up saves someone else some of that time!

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

July 17, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/), [explainers](https://www.seangoedecke.com/tags/explainers/), [mcp](https://www.seangoedecke.com/tags/mcp/)

* * *
