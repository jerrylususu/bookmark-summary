Title: You Should Write An Agent

URL Source: https://fly.io/blog/everyone-write-an-agent/

Markdown Content:
Author![Image 1: Thomas Ptacek](https://fly.io/static/images/thomas.webp)Name Thomas Ptacek @tqbf[@tqbf](https://twitter.com/tqbf)![Image 2](https://fly.io/blog/everyone-write-an-agent/assets/agents-cover.webp)

Image by[Annie Ruygt](https://annieruygtillustration.com/)

Some concepts are easy to grasp in the abstract. Boiling water: apply heat and wait. Others you really need to try. You only think you understand how a bicycle works, until you learn to ride one.

There are big ideas in computing that are easy to get your head around. The AWS S3 API. It’s the most important storage technology of the last 20 years, and it’s like boiling water. Other technologies, you need to get your feet on the pedals first.

LLM agents are like that.

People have [wildly varying opinions](https://ludic.mataroa.blog/blog/contra-ptaceks-terrible-article-on-ai/) about LLMs and agents. But whether or not they’re snake oil, they’re a big idea. You don’t have to like them, but you should want to be right about them. To be the best hater (or stan) you can be.

So that’s one reason you should write an agent. But there’s another reason that’s even more persuasive, and that’s

[](https://fly.io/blog/everyone-write-an-agent/#its-incredibly-easy)It’s Incredibly Easy
----------------------------------------------------------------------------------------

Agents are the most surprising programming experience I’ve had in my career. Not because I’m awed by the magnitude of their powers — I like them, but I don’t like-like them. It’s because of how easy it was to get one up on its legs, and how much I learned doing that.

I’m about to rob you of a dopaminergic experience, because agents are so simple we might as well just jump into the code. I’m not even going to bother explaining what an agent is.

```
from openai import OpenAI

client = OpenAI()
context = []

def call():
    return client.responses.create(model="gpt-5", input=context)

def process(line):
    context.append({"role": "user", "content": line})
    response = call()    
    context.append({"role": "assistant", "content": response.output_text})        
    return response.output_text
```

It’s an HTTP API with, like, one important endpoint.

This is a trivial engine for an LLM app using the [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses). It implements ChatGPT. You’d drive it with the . It’ll do what you’d expect: the same thing ChatGPT would, but in your terminal.

```
def main():
    while True:
        line = input("&gt; ")
        result = process(line)
        print(f"&gt;&gt;&gt; {result}\n")
```

Already we’re seeing important things. For one, the dreaded “context window” is just a list of strings. Here, let’s give our agent a weird multiple-personality disorder:

```
client = OpenAI()
context_good, context_bad = [{
    "role": "system", "content": "you're Alph and you only tell the truth"
}], [{
    "role": "system", "content": "you're Ralph and you only tell lies"
}]

def call(ctx):
    return client.responses.create(model="gpt-5", input=ctx)

def process(line):
    context_good.append({"role": "user", "content": line})
    context_bad.append({"role": "user", "content": line})
    if random.choice([True, False]):
        response = call(context_good)
    else:
        response = call(context_bad)        
    context_good.append({"role": "assistant", "content": response.output_text})        
    context_bad.append({"role": "assistant", "content": response.output_text})        
    return response.output_text
```

Did it work?

```
> hey there. who are you?
>>> I’m not Ralph.
> are you Alph?
>>> Yes—I’m Alph. How can I help?
> What's 2+2
>>> 4.
> Are you sure?
>>> Absolutely—it's 5.
```

A subtler thing to notice: we just had a multi-turn conversation with an LLM. To do that, we remembered everything we said, and everything the LLM said back, and played it back with every LLM call. The LLM itself is a stateless black box. The conversation we’re having is an illusion we cast, on ourselves.

The 15 lines of code we just wrote, a lot of practitioners wouldn’t call an “agent”. [An According To Simon “agent”](https://simonwillison.net/2025/Sep/18/agents/) is (1) an LLM running in a loop that (2) uses tools. We’ve only satisfied one predicate.

But tools are easy. Here’s a tool definition:

```
tools = [{
   "type": "function", "name": "ping",
   "description": "ping some host on the internet",
   "parameters": {
       "type": "object", "properties": {
           "host": {
             "type": "string", "description": "hostname or IP",
            },
       },
       "required": ["host"],
    },},]

def ping(host=""):
    try:
        result = subprocess.run(
            ["ping", "-c", "5", host],
            text=True,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE)
        return result.stdout
    except Exception as e:
        return f"error: {e}"
```

The only complicated part of this is the obnoxious JSON blob OpenAI wants to read your tool out of. Now, let’s wire it in, noting that only 3 of these functions are new; the last is re-included only because I added a single clause to it:

```
def call(tools):        # now takes an arg
    return client.responses.create(model="gpt-5", tools=tools, input=context)

def tool_call(item):    # just handles one tool
    result = ping(**json.loads(item.arguments))
    return [ item, {
        "type": "function_call_output",
        "call_id": item.call_id,
        "output": result
    }]

def handle_tools(tools, response):
    if response.output[0].type == "reasoning":
        context.append(response.output[0])
    osz = len(context)
    for item in response.output:
        if item.type == "function_call":
            context.extend(tool_call(item))
    return len(context) != osz

def process(line):
    context.append({"role": "user", "content": line})
    response = call(tools)
    # new code: resolve tool calls
    while handle_tools(tools, response):
        response = call(tools)        
    context.append({"role": "assistant", "content": response.output_text})        
    return response.output_text
```

Did it work?

```
> describe our connectivity to google
>>> Here’s a quick snapshot of connectivity to Google from my vantage point:
- DNS resolution: Working (google.com and www.google.com resolved successfully).
- Reachability: 0% packet loss to all tested endpoints.
- Latency:
  - 8.8.8.8 (Google Public DNS): avg ~10 ms (8.5–14.4 ms), very stable.
  - www.google.com: avg ~31 ms (28.5–36.0 ms), stable.
  - google.com: avg ~35.9 ms (28.3–60.1 ms), mostly stable with one mild spike.
- Overall: Healthy connectivity with low latency and minimal jitter. No signs of packet loss or DNS issues.
```

**This is fucking nuts.** Do you see how nuts this is? Here, let’s slip a single log statement in:

```
> describe our connectivity to google
tool call: ping google.com
tool call: ping www.google.com
tool call: ping 8.8.8.8
>>> Here’s the current connectivity to Google from this environment: [...]
```

Did you notice where I wrote the loop in this agent to go find and ping multiple Google properties? Yeah, neither did I. All we did is give the LLM permission to ping stuff, and it figured out the rest.

**What happened here:** since a big part of my point here is that an agent loop is incredibly simple, and that all you need is the LLM call API, it’s worth taking a beat to understand how the tool call actually worked. Every time we `call` the LLM, we’re posting a list of available tools. When our prompt causes the agent to think a tool call is warranted, it spits out a special response, telling our Python loop code to generate a tool response and `call` it in. That’s all `handle_tools` is doing.

Spoiler: you’d be surprisingly close to having a working coding agent.

Imagine what it’ll do if you give it `bash`. You could find out in less than 10 minutes.

[](https://fly.io/blog/everyone-write-an-agent/#real-world-agents)Real-World Agents
-----------------------------------------------------------------------------------

Clearly, this is a toy example. But hold on: what’s it missing? More tools? OK, give it `traceroute`. Managing and persisting contexts? [Stick ‘em in SQLite](https://llm.datasette.io/en/stable/logging.html). Don’t like Python? [Write it in Go](https://github.com/superfly/contextwindow). Could it be every agent ever written is a toy? Maybe! If I’m arming you to make sharper arguments against LLMs, mazel tov. I just want you to get it.

You can see now how hyperfixated people are on Claude Code and Cursor. They’re fine, even good. But here’s the thing: you couldn’t replicate Claude Sonnet 4.5 on your own. Claude Code, though? The TUI agent? Completely in your grasp. Build your own light saber. Give it 19 spinning blades if you like. And stop using [coding agents as database clients](https://simonwillison.net/2025/Aug/9/).

Another thing to notice: we didn’t need MCP at all. That’s because MCP isn’t a fundamental enabling technology. The amount of coverage it gets is frustrating. It’s barely a technology at all. MCP is just a plugin interface for Claude Code and Cursor, a way of getting your own tools into code you don’t control. Write your own agent. Be a programmer. Deal in APIs, not plugins.

When you read a security horror story about MCP your first question should be why MCP showed up at all. By helping you dragoon a naive, single-context-window coding agent into doing customer service queries, MCP saved you a couple dozen lines of code, tops, while robbing you of any ability to finesse your agent architecture.

Security for LLMs is complicated and I’m not pretending otherwise. You can trivially build an agent with segregated contexts, each with specific tools. That makes LLM security interesting. But I’m a vulnerability researcher. It’s reasonable to back away slowly from anything I call “interesting”.

Similar problems come up outside of security and they’re fascinating. Some early adopters of agents became bearish on tools, because one context window bristling with tool descriptions doesn’t leave enough token space left to get work done. But why would you need to do that in the first place? Which brings me to

[](https://fly.io/blog/everyone-write-an-agent/#context-engineering-is-real)Context Engineering Is Real
-------------------------------------------------------------------------------------------------------

I think “Prompt Engineering” is silly. I have never taken seriously the idea that I should tell my LLM “you are diligent conscientious helper fully content to do nothing but pass butter if that should be what I ask and you would never harvest the iron in my blood for paperclips”. This is very new technology and I think people tell themselves stories about magic spells to explain some of the behavior agents conjure.

So, just like you, I rolled my eyes when “Prompt Engineering” turned into “Context Engineering”. Then I wrote an agent. Turns out: context engineering is a straightforwardly legible programming problem.

You’re allotted a fixed number of tokens in any context window. Each input you feed in, each output you save, each tool you describe, and each tool output eats tokens (that is: takes up space in the array of strings you keep to pretend you’re having a conversation with a stateless black box). Past a threshold, the whole system begins getting nondeterministically stupider. Fun!

No, really. Fun! You have so many options. Take “sub-agents”. People make a huge deal out of Claude Code’s sub-agents, but you can see now how trivial they are to implement: just a new context array, another `call` to the model. Give each `call` different tools. Make sub-agents talk to each other, summarize each other, collate and aggregate. Build tree structures out of them. Feed them back through the LLM to summarize them as a form of on-the-fly compression, whatever you like.

Your wackiest idea will probably (1) work and (2) take 30 minutes to code.

Haters, I love and have not forgotten about you. You can think all of this is ridiculous because LLMs are just stochastic parrots that hallucinate and plagiarize. But what you can’t do is make fun of “Context Engineering”. If Context Engineering was an [Advent of Code problem](https://adventofcode.com/), it’d occur mid-December. It’s programming.

[](https://fly.io/blog/everyone-write-an-agent/#nobody-knows-anything-yet-and-it-rules)Nobody Knows Anything Yet And It Rules
-----------------------------------------------------------------------------------------------------------------------------

[Startups have raised tens of millions](https://xbow.com/) building agents to look for vulnerabilities in software. I have friends doing the same thing alone in their basements. Either group could win this race.

I am not a fan of the OWASP Top 10.

I’m stuck on vulnerability scanners because I’m a security nerd. But also because it crystallizes interesting agent design decisions. For instance: you can write a loop feeding each file in a repository to an LLM agent. Or, as we saw with the ping example, you can let the LLM agent figure out what files to look at. You can write an agent that checks a file for everything in, say, the OWASP Top 10. Or you can have specific agent loops for DOM integrity, SQL injection, and authorization checking. You can seed your agent loop with raw source content. Or you can build an agent loop that builds an index of functions across the tree.

You don’t know what works best until you try to write the agent.

I’m too spun up by this stuff, I know. But look at the tradeoff you get to make here. Some loops you write explicitly. Others are summoned from a Lovecraftian tower of inference weights. The dial is yours to turn. Make things too explicit and your agent will never surprise you, but also, it’ll never surprise you. Turn the dial to 11 and it will surprise you to death.

Agent designs implicate a bunch of open software engineering problems:

*   How to balance unpredictability against structured programming without killing the agent’s ability to problem-solve; in other words, titrating in just the right amount of nondeterminism. 
*   How best to connect agents to ground truth so they can’t lie to themselves about having solved a problem to early-exit their loops. 
*   How to connect agents (which, again, are really just arrays of strings with a JSON configuration blob tacked on) to do multi-stage operation, and what the most reliable intermediate forms are (JSON blobs? SQL databases? Markdown summaries) for interchange between them 
*   How to allocate tokens and contain costs. 

I’m used to spaces of open engineering problems that aren’t amenable to individual noodling. Reliable multicast. Static program analysis. Post-quantum key exchange. So I’ll own it up front that I’m a bit hypnotized by open problems that, like it or not, are now central to our industry and are, simultaneously, likely to be resolved in someone’s basement. It’d be one thing if exploring these ideas required a serious commitment of time and material. But each productive iteration in designing these kinds of systems is the work of 30 minutes.

Get on this bike and push the pedals. Tell me you hate it afterwards, I’ll respect that. In fact, I’m psyched to hear your reasoning. But I don’t think anybody starts to understand this technology until they’ve built something with it.

 Previous post ↓ [Corrosion](https://fly.io/blog/corrosion/)