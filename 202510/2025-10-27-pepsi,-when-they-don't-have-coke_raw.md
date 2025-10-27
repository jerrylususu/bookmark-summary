Title: Pepsi, when they don't have coke

URL Source: https://www.bitecode.dev/p/pepsi-when-they-dont-have-coke

Published Time: 2025-10-26T12:17:43+00:00

Markdown Content:
_If you haven’t seen the underrated [The invention of lying](https://en.wikipedia.org/wiki/The\_Invention\_of\_Lying), the article’s title may not ring a bell, but my point is, I really like Cuelang, and the closest thing I can get is Starlark._

_You can write configuration in a decent sandboxed language, parse it with Python, and has very powerful filtering features for user capabilities._

_But it does require a lot of ceremony._

For small config files, times are glorious. [Toml](https://toml.io/en/) has [landed officially in Python 3.11](https://docs.python.org/3/library/tomllib.html), and we can read env vars and .env files in a thousand of ways. [Pydantic settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) lets you define a schema for the config, load it, and validate it. You get [argparse](https://docs.python.org/3/library/argparse.html) or [typer](https://typer.tiangolo.com/) to parse flags and options. And with AI, all this boilerplate doesn’t even have to be coded because, to be perfectly honest, not only is the LLM good at it, but it’s better at it than me.

However, when you get a big config file, with nested values, you need logic to generate stuff, require dividing it into several files, and so on.... The situation is quite terrible.

Toml is bad at nesting, and big .toml files are not great. It’s best used as a better .ini.

JSON doesn’t allow comments, import or trailing commas, has limited data type support, and makes you repeat yourself constantly. Alternatives like JSON5 barely make a dent at that, at the cost of being non-standard.

YAML is the worst of all, of course. I could write an entire article about it, but some people have already dedicated [a website](https://noyaml.com/) to just how awful it is.

None of those have imports, functions, or DRY facilities. Well, YAML kinda has some (ref, executable code), but they are dangerous, like everything in this devil spawn of a language.

To compensate for this, the industry decided to make it worse and use templating and ad hoc DSL for the most important (and hardest to debug) part of our stack: provisioning and CI.

So you use child-holed-ridden mitts to handle hot lava.

What an awesome idea.

Since I’m not the only one nor the first to lament about this state of affairs, nerds have been working hard at crafting tools to make the problem go away.

A myriad of configuration-oriented languages were born, and some are still more pain than gain like [HCL](https://developer.hashicorp.com/terraform/language/syntax/configuration), while others like [Dhall](https://dhall-lang.org/) or [Jsonnet](https://jsonnet.org/) are interesting if you give them a chance.

One that really stands out from the crowd for me is [CueLang](https://github.com/ClueLang/Clue), a nifty language that checks all the boxes:

*   Dedicated to configuration (declarative syntax, sandboxed, not Turing complete).

*   Great DRY facilities (functions, imports, sum types, loops, references).

*   A really nice, strong type system to make your input as clean as possible.

*   Embedded schema declaration for extra safety and reusability.

So it scales up, but more importantly, it scales down, because the language is well designed enough that simple things say simple. A basic .cue file might not be perfectly clear if you know nothing about the syntax, but you still get the gist of it:

```
package myapp

import “strings”

#DBType: {
    name:     string
    port:     int | *8080
    replicas: int & >=1 & <=10
    features: [...string]
    database: {
        host: string
        port: int | *5432
        ssl:  bool | *true
    }
}

DBConf: #DBType & {
    name:     “my-service”
    replicas: 3
    features: [”auth”, “logging”, “metrics”]
    database: {
        host: “db.example.com”
    }
}

output: {
    config
    url: “https://\(strings.ToLower(config.name)).example.com:\(config.port)”
}
```

And the beauty of Cue is that you can export it to JSON (or YAML) for compatibility, so you can do:

`cue export config.cue - -e output`
And get:

```
{
    “url”: “https://my-service.example.com:8080”,
    “name”: “my-service”,
    “port”: 8080,
    “replicas”: 3,
    “features”: [
        “auth”,
        “logging”,
        “metrics”
    ],
    “database”: {
        “host”: “db.example.com”,
        “port”: 5432,
        “ssl”: true
    }
}
```

Alas, the only Cue implementation is written in Go, and there are no bindings for Python, so I can’t directly load the result of the cue file in Python program. I would need to install the cue executable separately, call that with a subprocess, and load the resulting JSON.

This is not my idea of a good time. More importantly, this would not fly in the corporate world, and half of my clients are corporate. It’s hard enough to introduce an exotic language in those spheres, let alone if using it means you have to settle for a hack.

So I went back to using templated YAML, and for my projects, [Python as a configuration language.](https://www.bitecode.dev/p/python-as-a-configuration-language).. No sandboxing, and you can crash your config, so not ideal, but better than the alternatives.

Not great, not terrible.

I haven’t given a chance to Starlark, because:

*   It comes from the Java world, a community not exactly known for its flexible and lightweight infra.

*   It’s a child of [bazel](https://bazel.build/), and if you have ever used bazel, it’s an acquired taste.

*   It’s one of those numerous “it’s like Python, well if you really squint” type of languages. I don’t like when something tries to use Python similarity as a selling point, only to pull the rug under your feet as soon as you try to use the language for real.

*   The early Python bindings were super low quality.

But out of desperation, I gave it a chance, and I’m glad I did, because it can do things I hadn't realized.

It now has [Python bindings based on the Rust implementation](https://pypi.org/project/starlark-pyo3/), and as is often the case with Rust projects, the quality is much better than alternatives. It helps that said implementation is from Facebook, meaning it’s likely it will be maintained on the long run. And thanks to [Py03](https://pyo3.rs/) , there are robust wheels for major platforms, so it’s easy to install:

`pip install starlark-pyo3`
You get access to rich and familiar data types:

```
# None type
nullable_value = None

# Booleans
is_production = True

# Integers
port = 8080

# Floats
cpu_threshold = 0.85

# Strings
version = "2.1.0"
description = """
This is a multi-line description
of our microservice application
that handles user requests.
"""

# Lists  
allowed_origins = [
	"https://example.com",
	"https://app.example.com",
	"https://admin.example.com",
]

# Tuples 
coordinates = (40.7128, -74.0060)

# Dictionaries
database_config = {
	“host”: “db.example.com”,
	“ports”: [5432, 80],
	“ssl_enabled”: True,
	“pool_size”: 20,
	“timeout”: 30.0,
	“allowed_origins”: allowed_origins
}
```

You get DRY facilities like references, functions and imports:

```
load(”lib/utils.star”) # this doesn’t work like you think though

def generate_service_name(app, env):
    """Generate a standardized service name."""
    return “{}-{}”.format(app, env)
```

And there are [some built-ins](https://github.com/bazelbuild/starlark/blob/master/spec.md#built-in-constants-and-functions) for text and number manipulations. It supports UTF8, can sort stuff, provide lambdas, ** kwargs, and do comprehension lists. That’s it.

It is not AT ALL Python.

There is no `while`, `yield`, `import`, `class`, f-string, `Path`, `@decorator`, `async`/`await`, `global`, `with`, `assert`, set literals or comprehensions, advanced unpacking etc. It’s not like MicroPython, a limited subset of Python based on some compromises.

It’s a very restricted language (on purpose) which happens to implement its behavior with a Python flavor.

I think it’s very important to underline that. It is doing a disservice to this language to compare it to Python. You should see it as a completely different language that just happens to have similarities in syntax and naming.

The biggest difference is the import system, as it’s an opt-in system, and by default is deactivated, and uses a special `load` function.

Starlark programs are executed in a sandbox; they are isolated from the outside world. They don’t have, by default, access to the file system or the network.

Running one starlark file means creating an empty module, putting some values in there for the program to initialize with, execute the starlark code in the context of that module, then read the variables you are interested in back from the module.

It looks like this:

```
import starlark
# Assuming you code starlark code in config.star, read it:
with open(”config.star”, “r”) as f:
    starlark_code = f.read()

# Load the standard library to put at the disposal of starlark
stdlib = starlark.Globals.standard()
# Create some module in which starlark will execute in
module = starlark.Module()
# Put some data for starlark to read
module[”site”] = “www.bitecode.dev”
# Parse the starlark code (this can give you syntax errors here)
ast = starlark.parse(”config.star”, starlark_code)
# Run the code 
result = starlark.eval(module, ast, stdlib, None)
# Get our data bask
output_data = module[”variable_from_starlak”]
```

You could also expose callables from Python to Starlark if you want it to have more capabilities:

```
def calculate_tax(amount: float, rate: float = 0.1) -> float:
	“”“Python function with default arguments.”“”
	return amount * rate
	
module.add_callable(”calculate_tax”, calculate_tax)
```

This let you control how much of the file system and the network you want the sandbox to have access to.

By default, the config file can’t import anything. You have to provide a loader function, basically implement imports, and pass it to starlark. A basic implementation looks like this:

```
def load_function(filename):
    
    file_path = Path(filename)

    if not file_path.exists():
        raise FileNotFoundError(f”Cannot load {filename}: file not found”)
    
    with open(file_path, ‘r’) as f:
        source = f.read()

    module = starlark.Module()
    stdlib = starlark.Globals.standard()
    ast = starlark.parse(str(file_path), source)
    nested_loader = starlark.FileLoader(load_function)
    starlark.eval(module, ast, stdlib, nested_loader)
    return module.freeze()
```

And then, when you load the main Starlark file, you do this to tell it how to import stuff:

`result = starlark.eval(module, ast, stdlib, load_function)`
So that it can do `load(”submodule.star”)` in its own code.

This function is very simple and doesn’t even allow recursive imports (imports in imported files). But you can see the power in this: you can put any logic to filter imports based on anything you want, be it hashing, signature, allow-list of directories, content, naming…

So the library is more like “build your own configuration logic” than a turnkey solution like Cuelang. It is very interesting, though, because it gives you a decently powerful language you can expose to the end users, and decide very precisely what you allow them to do or not.

If I ever need to create a system that needs a DSL for 3rd parties I can’t trust, I would consider it.

However, as a configuration language for my own systems, this is too much work upfront. Not to mention that it is the same with all those dedicated DSL: tooling and debugability are subpar.

Plus, we are missing a critical part: schemas.

You can’t easily define what data should go in, nor whether the data that goes out is correct.

Sure, you can pair it with Pydantic. But then, if I just deal with trusted users and have to wire Pydantic myself, why not just write the config in Python itself? Pydantic can export it to JSON or YAML, and I don’t have to worry too much about side effects since I’m in control of the code.

Worked ok for Django, even without the schema.

It’s not perfect, once again, and the config still suck.

But I least I discovered a cool utility.