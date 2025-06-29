Title: Prompting vs JSON Mode vs Function Calling vs Constrained Generation vs SAP

URL Source: https://www.boundaryml.com/blog/schema-aligned-parsing

Published Time: July 29, 2024

Markdown Content:
Pre-reading: What is structured generation?

Structured generation is the idea of coercing the LLM to generate some data that you can parse into a data model and then programatically use.

The most common way to extract structured data / do function calling out of an LLM is to somehow get the LLM to output JSON, and then call `JSON.parse`.

However, there is no reason to assume that JSON, the prevalant serialization for Web APIs, should be the ideal serialization for LLMs. Given the stochastic nature of LLMs, it might even be true that all strict serialization formats are suboptimal, since a single error can cause the entire serialization to be invalid.

In this article, we'll:

1.   Explain how every current technique of structured data extraction works
2.   Discuss the pros and cons of each technique
3.   Introduce a new technique, SAP (Schema-Aligned Parsing), that achieves state-of-the-art accuracy on the Berkeley Function Calling Leaderboard (Jump to [SAP](https://www.boundaryml.com/blog/schema-aligned-parsing#sap))

Problem Space
-------------

![Image 1: Problem Definition](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fproblem_definition.965ca75b.png&w=3840&q=75)

Given a QUERY, and a SCHEMA, the three things we can do to change the likelihood of generating an output are:

![Image 2: Prompt](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwrench-prompt.d2823bcc.png&w=256&q=75)Change how we construct the prompt and render the schema

![Image 3: Prompt](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwrench-model.e1a01b0f.png&w=128&q=75)Change how tokens are generated

![Image 4: Prompt](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwrench-parser.e674dca6.png&w=256&q=75)Change how we parse the output of the model into our desired structure

All 9 Techniques
----------------

| Category | Technique |
| --- | --- |
| Prompt | [Naive Approach](https://www.boundaryml.com/blog/schema-aligned-parsing#naive-approach) [Prompt Engineering](https://www.boundaryml.com/blog/schema-aligned-parsing#prompt-engineering) [Prompt Engineering + Parsing](https://www.boundaryml.com/blog/schema-aligned-parsing#prompt-engineering--parsing) |
| Model | [JSON Mode](https://www.boundaryml.com/blog/schema-aligned-parsing#json-mode) [Constrained Generation](https://www.boundaryml.com/blog/schema-aligned-parsing#constrained-generation) [Function Calling](https://www.boundaryml.com/blog/schema-aligned-parsing#function-calling) |
| Parser | [LLM Retries](https://www.boundaryml.com/blog/schema-aligned-parsing#llm-retries) [AST Parsing](https://www.boundaryml.com/blog/schema-aligned-parsing#ast-parsing) [SAP](https://www.boundaryml.com/blog/schema-aligned-parsing#sap) |

Technique Comparison
--------------------

We ran the most popular techniques on the [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) dataset. Here are the results:

| Model | Function Calling | Python AST Parser | SAP |
| --- | --- | --- | --- |
| gpt-3.5-turbo | 87.5% | 75.8% | 92% |
| gpt-4o | 87.4% | 82.1% | 93% |
| claude-3-haiku | 57.3% | 82.6% | 91.7% |
| gpt-4o-mini | 19.8% | 51.8% | 92.4% |
| claude-3-5-sonnet | 78.1% | 93.8% | 94.4% |
| llama-3.17b | - | 60.9% | 76.8% |

Dataset had n=1000 per model and comes from Berkeley Function Calling Leaderboard thanks to the Gorilla Team.

Technique Breakdown
-------------------

Technique 0:Naive Approach

Inject the question and the schema as JSON schema to the model, call `JSON.parse(..)` on the response

![Image 5: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F0_0.e8c170a0.png&w=1080&q=75)![Image 6: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F0_1.5ef29ca6.png&w=1080&q=75)![Image 7: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F0_2.f71ac994.png&w=1080&q=75)

**My Personal Rating:**

0

/ 5

Please don't do this. As of writing this, LLMs are just bad at producing JSON when left to their own devices.

Complete Propmt
```
Generate a resume in JSON format based on the SCHEMA defined below:

{
 type: "object",
 properties: {
    name: {
      type: "string",
      required: true,
    },
    contact: {
      type: "object",
      properties: {
        email: {
          type: "string",
          required: true,
        },
        phone: {
          type: "string",
          required: false,
        }
      },
      required: true,
    },
    education: {
      type: "array",
      items: {
        type: "object",
        properties: {
          institution: {
            type: "string",
            required: true,
          },
          degree: {
            type: "string",
            required: true,
          },
          year: {
            type: "string",
            required: true,
          }
        }
      },
      required: true,
    },
    experience: {
      type: "array",
      items: {
        type: "object",
        properties: {
          company: {
            type: "string",
            required: true,
          },
          role: {
            type: "string",
            required: true,
          },
          duration: {
            type: "string",
            required: true,
          }
        }
      },
      required: true,
    },
    skills: {
      type: "array",
      items: {
        type: "string"
      },
      required: true,
    }
 }
}
```

Prompt

Technique 1:Prompt Engineering

Try and better explain the desired format the model. **Example:** Ask it to not make common JSON mistakes

![Image 8: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F1_0.1b758999.png&w=1080&q=75)![Image 9: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F1_1.5ef29ca6.png&w=1080&q=75)![Image 10: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F1_2.f71ac994.png&w=1080&q=75)

**My Personal Rating:**

0

/ 5

Please don't do this either. Same reason as above.

Prompt

Technique 2:Prompt Engineering + Parsing

Add some programatic robustness. Only parse with `JSON.parse` conditionally.

![Image 11: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F2_0.a924ed77.png&w=1080&q=75)![Image 12: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F2_1.5ef29ca6.png&w=1080&q=75)![Image 13: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F2_2.2dd4644f.png&w=1080&q=75)

**My Personal Rating:**

0.5

/ 5

It is fast to write and though the LLM won't always listen to you verbaitum, at least you're trying. Points for effort.

Model

Technique 3:JSON Mode

Restrict the tokens the model is allowed to generate to only those that would be JSON parseable. Stop once the model completes the JSON object.

**Example:** After already generating `{ "key"`, the LLM must choose a token that starts with `:` to ensure valid JSON.

![Image 14: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F3_0.e8c170a0.png&w=1080&q=75)![Image 15: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F3_1.bb97954b.png&w=1080&q=75)![Image 16: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F3_2.f71ac994.png&w=1080&q=75)

**My Personal Rating:**

2.5

/ 5

JSON mode definitely works. It will at the very least always be parsable, but it loses points because JSON mode is both too strict and not strict enough at the same time.

1.   JSON is too rigid to use techniques which benefit from verbosity like Chain-of-Thought or Reasoning (See [CoT paper](https://arxiv.org/pdf/2201.11903) which had +40% in accuracy in some datasets)
2.   JSON is not sufficiently strict. `{ "foo": 1 }` is valid JSON, but if you wanted `{ "foo": int[] }`, it would be close, but still wrong.
3.   The error rate is often 10%+ when compared on larger datasets (see BFCL).
4.   And most importantly, not every model supports this

Model

Technique 4:Constrained Generation

The more general cousin of JSON mode. Instead of only allowing tokens which would produce valid JSON, only allow very specific tokens at any given step of token generation.

**Example:**

Take a grammar restriction: `[0-9]{1,2}\.[0-9]{0,2}` - a regular expression that matches numbers with one or two digits before the decimal point and zero to two digits after the decimal point.

We first only allow the LLM to pick tokens that match numbers.

After say, `83`, the LLM would be forced to pick tokens that started with `.`.

Tip

In this scenario, due to Constrained Generation, the LLM could never generate a number larger than 99.99, since the grammar would remove any 3+ digit numbers.

![Image 17: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F4_0.ba02d676.png&w=1080&q=75)![Image 18: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F4_1.2b0ceaa8.png&w=1080&q=75)![Image 19: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F4_2.4de9c628.png&w=1080&q=75)

**My Personal Rating:**

2

/ 5

While more generalizable than JSON mode, this only works for open-source models that give you an interface that accepts grammars. Grammars for simple systems are easy to write, but with a larger and more diverse team, **grammars can be virtually impossible to maintain long term**. The difficulty of writing a proper grammar can be that of writing a compiler.

// Example grammar for a "simple" calculator
?start: expression

?expression: term (("+" | "-") term)*

?term: factor (("*" | "/") factor)*

?factor: NUMBER

 | "-" factor

   | "(" expression ")"
%import common.NUMBER

Question

How would you modify the grammar to allow variables?

Answer I have no idea tbh...

Model

Technique 5:Tools / Function Calling

The idea here is to fine-tune the model to intelligently trigger when to use JSON mode.

**Example Generation:**

1.   Teach the model a new special token `USE_TOOL`.
2.   Whenever the model generates the `USE_TOOL` token, switch to JSON mode for all subsequent tokens.
3.   Once the JSON is complete (detect this programatically, not by the model), allow the model to pick from all tokens, including `USE_TOOL`.
4.   Loop until the model emits the `END_TOKEN` token.

![Image 20: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F5_0.04c3d34c.png&w=1080&q=75)![Image 21: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F5_1.a4ce9973.png&w=1080&q=75)![Image 22: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F5_2.5c40293d.png&w=1080&q=75)

**My Personal Rating:**

~~2 / 5~~
3.5

/ 5

This is one approach I've found where my opinion has changed over time. Since Function calling requiring training a model on the special `USE_TOOL` token, it was not previously supported by all providers. As it is more common, and the interface is becoming more standardized, I've warmed up to it. However, I still have a few reservations:

1.   Function calling suffers from the same schema inaccuracy JSON mode does. `{ "foo": 1 }` is valid JSON, but if you wanted `{ "foo": int[] }`, it would be close, but still wrong.
2.   Most APIs rely on a JSON schema, which is incredibly wasteful in the token space.
3.   A lot of models still don't support it
4.   Models that do support it often have degraded accuracy with function calling when compared to just prompting based techniques.

That said, it does overcome some of the key problems with JSON mode like supporting verbosity-based techniques. For example, you can do chain of thought prior to the trigger token.

Parser

Technique 6:LLM Retries

Retry the model until it produces something that is parseable or pass parsing errors to the model and hope that when it tries again, you can get good results. This is the technique libraries like Langchain, Instructor, and Marvin use to get structured data reliably.

![Image 23: LLM Hammer](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fllm-hammer.bfc3685e.png&w=2048&q=75)

**My Personal Rating:**

1

/ 5

This is the only technique on here that I think has a potential to be a game changer, but is currently not used in an interesting way.

Today, many libraries are treating an LLM like a hammer and throwing every problem its way. `JSON.parse` failed due to including a comment? a trailing comma? Ask the LLM to fix the error and try parsing again.

**This adds unbounded latency and costs to the system.** LLMs are already slow and expensive (albiet getting cheaper and faster, but still significantly slower than most software).

Where I see potential, however, is in more complex systems to fix logical inconsistencies. An LLM is likely the only approach for doing this at scale. For example, fixing a scenario where age was off by 3 years.

// Data model
class Person {
name string
job string
birth_year int
age int @assert(
  this == now().year - birth_year,
  "{this} doesn't match {birth_year} given {now().year}"
)
}

// To fix it, instead of giving the LLM everything (the entire data model), just give it the error and only the properties that are relevant to age.
{
"error": "age=30 doesn't match birth_year=1990 given now.year=2024",
"birth_year": 1990,
"age": 30
}

Current approaches, would likely just retry the entire model, but a more sophisticated approach would be to only give the LLM the error and the relevant properties, reducing costs and latencies. This would be a much more efficient approach, but would require a lot of engineering (and compilers) to get right.

Parser

Technique 7:Language-Specific AST parsers

Rely on the model's inherent ability to output code, and existing Abstract Syntax Tree Parsers for reading code, and then transform that into JSON. Example output: `[GetTriangleArea(base=5, height=10)]` (Note, that this is valid python syntax) After python_to_json: `{ "GetTriangleArea": {"base": 5, "base": 10} }`

![Image 24: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F6_0.8e8baac5.png&w=1080&q=75)![Image 25: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F6_1.dda7d1e8.png&w=1080&q=75)![Image 26: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F6_2.9f1921fd.png&w=1080&q=75)

**My Personal Rating:**

3.5

/ 5

Credit here goes to the Gorilla Team @ Berkley (see [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)).

This was one of the few ideas I've seen which step away from JSON, XML, and other similar formats and tries to reframe the problem in a way the LLM may better understand. **The issue with generating code, is that code, like JSON, is still a very strict grammar.** While code has very few superfluous tokens (like `:` or `"` in JSON), you still rely on a parser you often don't own (the syntax parser of the language). If the LLM, by accident, emits the wrong amount of whitespace, it can completely change what the python parser reads the output.

Parser

BAML's Technique (Ours):Schema Aligned Parsing (SAP)

Instead of relying on the model to strictly understand our desired format, write a parser that generously reads the output text and applies error correction techniques with knowledge of the original schema.

![Image 27: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F7_0.2ccf69fa.png&w=1080&q=75)![Image 28: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F7_1.dda7d1e8.png&w=1080&q=75)![Image 29: Technique](https://www.boundaryml.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F7_2.dc368696.png&w=1080&q=75)

**My Personal Rating:**

~~5~~
6

/ 5

I'm obviously a bit biased 😇, but at the same time, the numbers don't lie!

| Model | Function Calling | Python AST Parser | SAP |
| --- | --- | --- | --- |
| gpt-3.5-turbo | 87.5% | 75.8% | 92% |
| gpt-4o | 87.4% | 82.1% | 93% |
| claude-3-haiku | 57.3% | 82.6% | 91.7% |
| gpt-4o-mini | 19.8% | 51.8% | 92.4% |
| claude-3-5-sonnet | 78.1% | 93.8% | 94.4% |
| llama-3.17b | - | 60.9% | 76.8% |

Dataset had n=1000 per model and comes from Berkeley Function Calling Leaderboard thanks to the Gorilla Team.

Note

We don't use json_schema for SAP, instead we use baml_schema, which is a more compressed way to define schemas. This is because we don't need to be as strict as JSON during parsing so we can omit characters like quotes. You can read more here: [Your prompts are using 4x more tokens than they need.](https://www.boundaryml.com/blog/type-definition-prompting-baml)

What is SAP and why does it work so well?
-----------------------------------------

The key idea behind SAP is to assume that the model will make mistakes, and to build a parser that is robust enough to handle them. This would be virtually impossible for some tasks, but in the context of structured data extraction, we have a schema to guide us. A key inspiration to us was Postel's Law, coined by Jon Postel, the creator of TCP/IP:

> Be conservative in what you do, be liberal in what you accept from others.

We'll do a future post that outlines exactly how our SAP algorithm works. At a very high-level, you can think of the leetcode problem "Edit Distance" but instead of comparing two strings, we ask: "What is least cost edit I need to make to get from the model's output to something parseable by a schema?" The simplest cost function could be Levenshtein distance, but we use a custom cost function that takes into account the schema. (The code is open-source, so you can check it out [here](https://github.com/boundaryml/baml))

Meanwhile, here are three examples to show some of the error correction techniques we use:

Handling Invalid JSON sequence

Schema![Image 30: SAP](https://www.boundaryml.com/_next/static/media/llm-fix-1.c05d7979.svg)

LLM Response![Image 31: SAP](https://www.boundaryml.com/_next/static/media/llm-fix-2.e4de1157.svg)

Post-SAP![Image 32: SAP](https://www.boundaryml.com/_next/static/media/llm-fix-3.a8fa0539.svg)

Mistakes by the LLM fixed by SAP:

*   Included a comment
*   Used a fraction instead of a float
*   Forgot quotes around `stands_for`
*   Didn't escape the newline or `"` within the string
*   Included a trailing comma

Handling Invalid JSON sequence

Schema![Image 33: SAP](https://www.boundaryml.com/_next/static/media/schema-valid-1.21b75ac2.svg)

LLM Output![Image 34: SAP](https://www.boundaryml.com/_next/static/media/schema-valid-2.6c1bd060.svg)

Post-SAP![Image 35: SAP](https://www.boundaryml.com/_next/static/media/schema-valid-3.d75e176e.svg)

Mistakes by the LLM fixed by SAP:

*   `"Amazon"` was returned as a `string`, but `Founder.prior_jobs`should be a `string[]`

Handling Yapping

LLM Output![Image 36: SAP](https://www.boundaryml.com/_next/static/media/yapping-1.daf7e07b.svg)

Post-SAP![Image 37: SAP](https://www.boundaryml.com/_next/static/media/yapping-2.28e5c3ba.svg)

Mistakes by the LLM fixed by SAP:

*   Included a lot of prefix and suffix text that is not relevant to our desired output, but may be relevant to the LLM to generate the output

Some more error correction techniques we use in SAP include:

*   Unquoted strings
*   Unescaped quotes and new lines in strings
*   Missing commas
*   Missing colons
*   Missing brackets
*   Misnamed keys
*   Cast fractions to floats
*   Remove superfluous keys in objects
*   Strip yapping
*   Picking the best of many possible candidates in case LLM produces multiple outputs
*   Complete partial objects (due to streaming)
*   and more

Using SAP today
---------------

We wanted to offer SAP in all languages of your choice, so we've written it in Rust and provide a native interface for Python, Typescript, and Ruby. (We're working on more languages, but we're a small team!)

Since all interfaces use the same Rust code, you can expect the same performance and accuracy across all languages.

You can try it on our online playground: [https://promptfiddle.com](https://promptfiddle.com/) or add it to your code base already. ([Go to documentation](https://docs.boundaryml.com/docs/get-started/quickstart/python))

### Code Snippet

1.   Write a schema in BAML

```
// my_app/baml_src/my_schema.baml
class Resume {
  name string @description("first and last name")
  email string?
  experience Experience[]
}

class Experience {
  title string
  company string
}
```

1.   Write an LLM prompt in BAML

```
// my_app/baml_src/my_schema.baml
// ...

function ExtractResume(text: string) -> Resume {
  client "openai/gpt-4o"
  prompt #"
    Describe this resume.
    {{ ctx.output_format }}

    {{ _.role('user') }}
    {{ text }}
  "#
}
```

1.   Create bindings in your language of choice and use the BAML defined function as if it were a native function (with autocomplete and types!).

### Python

```
$ pip install baml-py
$ baml-cli generate --from /path/to/my_schema.baml --target "python/pydantic"
```

```
from baml_client import b

# resume will always be a Pydantic model of type Resume
resume = b.ExtractResume("""
  Vaibhav Gupta
  vbv@boundaryml.com
  - Founder @ BoundaryML
""")

# BAML will automatically validate the response via SAP and cast it to a Pydantic model
```

### Typescript

```
$ npm install @boundaryml/baml
$ ./node_modules/.bin/baml-cli generate --from /path/to/my_schema.baml --target "typescript"
```

```
import { b } from './baml_client'

// resume will always be a TypeScript interface of type Resume
const resume = await b.ExtractResume(`
  Vaibhav Gupta
  vbv@boundaryml.com
  - Founder @ BoundaryML
`);

// BAML will automatically validate the response via SAP and cast it to a TypeScript interface
```

### Ruby

```
$ gem install baml
$ baml-cli generate --from /path/to/my_schema.baml --target "ruby/sorbet"
```

```
require 'baml_client'

# resume will always be a Sorbet model of type Resume
resume = b.ExtractResume(<<~TEXT)
  Vaibhav Gupta
  vbv@boundaryml.com
  - Founder @ BoundaryML
TEXT

# BAML will automatically validate the response via SAP and cast it to a Sorbet model
```

Does this really matter since models will get better?
-----------------------------------------------------

I think one could make an arguement for no. If models get better, then JSON mode will be sufficient.

But I personally think performance always matters. If I had some technique that can get the same quality 50% faster or 50% cheaper, then I would obviously use it. Besides, as models get better, I would much rather they spend their training data on being better at understanding the world, rather than understanding my schema. The schema part we can solve with engineering.

Mandatory Blurb 🤝
------------------

Our mission at Boundary is to provide the best possible developer experience for shipping AI pipelines. We started with BAML, our new programming language for providing a _boundary_ between stochastic AI models, and deterministic, type-safe code.

What's next? Likely we'll be showing off demos of how to combine function calling and structured generation with SAP to get the best of both worlds. Stay tuned!

If you enjoyed this article, please consider giving us a star on [GitHub](https://github.com/boundaryml/baml).
