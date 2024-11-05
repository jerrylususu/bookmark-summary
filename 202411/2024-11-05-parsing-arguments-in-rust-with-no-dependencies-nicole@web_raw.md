Title: Parsing arguments in Rust with no dependencies

URL Source: https://ntietz.com/blog/parsing-arguments-rust-no-deps/

Markdown Content:
When pairing with my friend Emily, we had a choice of what to implement in her project: start a new feature, or add a command line argument parser? We opted for the latter, because it had to happen eventually and it was more well bounded. It ended up having a lot of depth!

We wrote it from scratch to learn more, rather than pulling in a library[1](https://ntietz.com/blog/parsing-arguments-rust-no-deps/#cplusplus). What we found was a nice level of depth in a well-bounded project. I came away wanting to repeat the exercise in Rust.

Opportunity arrives on a yak
----------------------------

As with many of my best procrastination projects, the chance to do this again in Rust came in the form of a yak shave. I've started writing a little poetry, and to get practice, I wanted to write a small utility to generate prompts[2](https://ntietz.com/blog/parsing-arguments-rust-no-deps/#hahano). Naturally, this has to be _configurable_ because my little utility will _sweep the world_ (spoiler alert: no it won't). That means we need command-line arguments!

I could pull in [clap](https://docs.rs/clap/latest/clap/index.html), which I think is the best fully-featured choice available today. That would add 23 dependencies to my little project, if you count transitive dependencies. This can go up higher if you turn on a few features: `derive`, `env`, `unicode`, and `wrap_help` bring you up to 38 dependencies!

Instead, I thought it would be fun to implement it myself again, and do it in the same mode as our C++ adventure: parse command-line arguments with _no_ external dependencies! This will have the side benefit of keeping my project's dependencies much lighter, which should (I think) keep compile times lower and make the entire system easier to understand front-to-back. If I do this, I may as well publish it and make it usable for everyone!

The basic design
----------------

The design of this parser is pretty straightforward. We have two types of arguments: positional or named.

We'll handle positional arguments as little more than a list of the leftover strings that we don't need for named options. These don't get any special handling, and there's not a lot of parsing to do (unless you do fancy things like path and variable expansion).

Named options (and their respective arguments) are where we have more work to do. We want this to feel familiar, like most unix/linux/etc. command-line interfaces we've used. So we'll want the usual short and long options. For example, specifying a port might be able to use the short option `-p` or the long option `--port-number`. And we'll also want to be able to specify some help text, and whether or not the argument is required or optional.

Where things might be a little bit unfamiliar is with the action. We have to have a way of specifying whether something is a flag, a single value, or a list of values. Libraries like clap have more comprehensive options for actions, but this should be sufficient for us here.

And then to do our parsing, we can think of it like a state machine. You iterate through the provided arguments until you find one that could be the start of option (starts with a hyphen). Then you find the matching option and switch into a state based on what you expect to come next. After handling its argument (if there is one), you go back to the default state and look for the next option.

So now we just have to build that.

Implementing it
---------------

The data structures we use here match what was described previously in perhaps the most straightforward way. We have a struct to represent each of our options (here using `Opt` since `Option` is a highly useful existing struct in the standard library; we can never escape names being hard and ambiguous). For ergonomics, we'll also define methods to set each of these easily and return self; I have one example here, but the rest are the same idea. We also use a `name` method as the constructor, since all named arguments must have names.

```
#[derive(Clone, Debug, PartialEq)]
pub struct Opt {
    pub name: String,
    pub short: Option<char>,
    pub long: Option<String>,
    pub help: Option<String>,
    pub default: Option<String>,
    pub action: Action,
    pub required: bool,
}

impl Opt {


    pub fn short(mut self, short: char) -> Opt {
        self.short = Some(short);
        self
    }

    // same idea for the other fields
}
```

And we have a couple of enums for some values we need[3](https://ntietz.com/blog/parsing-arguments-rust-no-deps/#values). The first enum is for our actions. These tell the parser what to do when it encounters an option while parsing. `Set` and `Append` will slurp up the next argument as the value and store it or insert it. `SetTrue` and `SetFalse` will each set the boolean for their respective values. Note that each of the set flags implies that the _opposite_ is the default value (and we'll implement it that way).

```
#[derive(Clone, Debug, PartialEq)]
pub enum Action {
    Set,
    Append,
    SetTrue,
    SetFalse,
}
```

Then we have a what we end up storing for the values we've parsed. I opted to keep this simple and not introduce any extra types here. I think this is a reasonable tradeoff, since it keeps the code simple and it remains flexible, but the cost is that this means checking if an incorrect value is passed in (say, "fiddlesticks" for something that expects an integer) is pushed off as the user's responsibility, making the library harder to use.

Anyway, we have three choices: a single value, a list of values, or a true/false value.

```
#[derive(Clone, Debug, PartialEq)]
pub enum Value {
    Single(String),
    Multi(Vec<String>),
    Flag(bool),
}
```

And we have one struct to put it all together and define our parsing method on. This one is truly spartan.

```
#[derive(Debug, PartialEq)]
pub struct Opts {
    opts: Vec<Opt>,
}
```

And we have our resulting matches, after we've parsed things. Here we'll store one thing we haven't talked about yet, the name of the executable (the first argument passed in), and then the positional and named arguments.

```
#[derive(Debug, PartialEq)]
pub struct Matches {
    exec_name: String,
    positional: Vec<String>,
    named: HashMap<String, Value>,
}
```

Now that we have the data structures, we can implement the parsing itself.

We'll start by making a `parse` method on `Opts`. This will take in our arguments (from something like `std::env::args`) and return our matches, or an error.

```
pub fn parse(&self, args: Vec<String>) -> Result<Matches, ParseError> {
    todo!()
}
```

We can simplify our lives a bit by setting all the default values at the beginning, letting them get overwritten later if another value is provided. This is not the most efficient approach! But it is going to be a rounding error for most programs, and we could improve the implementation later to run it _last_ and only fill the arguments which aren't provided (or to fill them when we _request_ them). Let's just do this for now, though.

```
fn populate_defaults(&self, named: &mut HashMap<String, Value>) {
    for opt in self.opts.iter() {
        if let Some(default) = &opt.default {
            named.insert(opt.name.clone(), Value::Single(default.to_owned()));
        } else {
            match opt.action {
                Action::Append => {
                    named.insert(opt.name.clone(), Value::Multi(vec![]));
                }
                Action::SetTrue => {
                    named.insert(opt.name.clone(), Value::Flag(false));
                }
                Action::SetFalse => {
                    named.insert(opt.name.clone(), Value::Flag(false));
                }
                _ => {}
            }
        }
    }
}
```

And then we can make a helper function to find the named option which matches a given option, if any, and returns an error if an unexpected option is provided.

```
fn find_opt(&self, arg: &str) -> Result<&Opt, ParseError> {
    let opt = if arg.starts_with("--") {
        let long = arg.strip_prefix("--").unwrap();
        self.opts.iter().find(|o| o.long.as_deref() == Some(long))
    } else if arg.starts_with("-") {
        if arg.chars().count() != 2 {
            return Err(ParseError::MalformedOption(arg.to_string()));
        }
        let short = arg.chars().nth(1);
        self.opts.iter().find(|o| o.short == short)
    } else {
        return Err(ParseError::UnexpectedOption(arg.to_string()));
    };

    if let Some(opt) = opt {
        Ok(opt)
    } else {
        Err(ParseError::UnexpectedOption(arg.to_string()))
    }
}
```

And now we can come back and define our parse function. It starts out with converting the args into an iterator (so we don't have to clone each string, we take ownership of them all). If there isn't a first one, we know the whole thing has gone wrong, so we abort there.

```
// pub fn parse(&self, args: Vec<String>) -> Result<Matches, ParseError> {

    let mut args_iter = args.into_iter();
    let exec_name = match args_iter.next() {
        Some(s) => s,
        None => return Err(ParseError::MissingProgramName),
    };
```

Next we setup our storage and populate the defaults with our helper function.

```
// pub fn parse(&self, args: Vec<String>) -> Result<Matches, ParseError> {

    let mut positional = vec![];
    let mut named = HashMap::new();

    self.populate_defaults(&mut named);
```

And then we do our main loop. Inside the main parse loop, we check if any start with a dash (`-`): if so, we handle it as a named named option, otherwise we handle it as positional (just push it into a vec). For each named option we have to find the right Opt, then we do the action: set the value, append it into a list, or set a flag. There's a little error handling which makes it all somewhat longer, but overall the logic is simple.

```
// pub fn parse(&self, args: Vec<String>) -> Result<Matches, ParseError> {

    while let Some(arg) = args_iter.next() {
        if arg.starts_with("-") {
            let opt = self.find_opt(&arg)?;

            match opt.action {
                Action::Set => {
                    if let Some(value) = args_iter.next() {
                        named.insert(opt.name.clone(), Value::Single(value));
                    } else {
                        return Err(ParseError::MissingValue(opt.name.clone()));
                    }
                }
                Action::Append => {
                    match (args_iter.next(), named.get_mut(&opt.name)) {
                        (None, _) => return Err(ParseError::MissingValue(opt.name.clone())),
                        (Some(val), Some(Value::Multi(vals))) => {
                            vals.push(val);
                        }
                        (Some(val), None) => {
                            named.insert(opt.name.clone(), Value::Multi(vec![val]));
                        }
                        _ => return Err(ParseError::BadInternalState), // unexpected case
                    };
                }
                Action::SetTrue => {
                    named.insert(opt.name.clone(), Value::Flag(true));
                }
                Action::SetFalse => {
                    named.insert(opt.name.clone(), Value::Flag(false));
                }
            };
        } else {
            positional.push(arg);
        }
    }

    Ok(Matches::new(exec_name, positional, named))
}
```

And there we have it, a command-line options parser with _no_ external dependencies!

There are a few things left that aren't done:

*   No help or versions print
*   There's not a lot of help for validation
*   Things aren't exported in the root module, so using it is clunky

I'll fix these as I use it, but if anyone actually uses this and wants to contribute or maintain it, let me know. For now, the code is [in a git repo](https://git.sr.ht/~ntietz/ltl-args) and licensed under MIT and Apache licenses. This is a deviation from my usual use of the [Gay Agenda License](https://gal.gay/) because this is a project that I suspect could have some small real utility. Anyway, be gay do crime.

This "no-dependencies" thing
----------------------------

Okay, but why am I yammering on about no dependencies so much? Because there are some fundamentally nice things about _not_ adding more dependencies to your project, and sometimes we should reinvent things.

One hypothesis is that with no dependencies, the compile times will be faster. This isn't _broadly_ true (splitting a crate into subcrates can improve compile times, and this is a common practice), but I think _here_ it will improve compile times because this keeps it smaller and leaner.

More concretely, by having no external dependencies you reduce your bug surface area. Sure, you _own_ all the bugs now—but you won't get leftpad-ed, and you won't get dependabot alerts for third-removed transitive dependencies that now you've gotta patch.

On the other hand, you miss out on nice things. Here in particular, I'll be missing partial unicode support! You could put whatever you want in the strings, but once I implement help text, I'll probably have some form of text wrapping. And if you do that, you have to know how _wide_ characters are when displayed. Not all of them are the same as one monospace Latin alphabet character (such as emoji and some languages), and it depends on your font as well I think? We can do a best-effort job here of splitting based on some assumptions (and allow manual line splitting). But the best idea would probably be to optionally add a dependency as a Cargo feature so that you only get the dependency if you need it.

I think more things should be built from scratch and, ideally, without dependencies. You get to know the problem space better, and most things don't _need_ the big sophisticated solution—but you pay for the _whole_ dependency you pull in. It's also nice because if you have no dependencies, that means folks can depend on _you_ without adding any _transitive_ dependencies, and this is really a big deal. I'd love to have a set of dependencies to use that all have either no dependencies, or themselves have only 0-dep dependencies, so your number of transitive dependencies is capped. Then you could add in a lot of "fit for purpose" simple 0-dep things, and pick up the complex ones for where you _really_ need it while still keeping your `Cargo.lock` slimmer than today.

* * *

If this post was enjoyable or useful for you, **please share it!** If you have comments, questions, or feedback, you can email [my personal email](mailto:me@ntietz.com). To get new posts and support my work, subscribe to the [newsletter](https://ntietz.com/newsletter/). There is also an [RSS feed](https://ntietz.com/atom.xml).
