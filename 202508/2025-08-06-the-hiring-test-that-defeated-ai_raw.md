Title: The hiring test that defeated AI

URL Source: https://www.bitecode.dev/p/the-hiring-test-that-defeated-ai

Published Time: 2025-08-05T15:18:18+00:00

Markdown Content:
_Filtering technical candidates fairly is a hard task: too easy and you don't exclude enough, too much friction and it's a turn off for everyone. At some point, the industry went all in on small tests you would do at home, but AI killed this strategy._

_However, there is still a small corner of the web the LLM crawlers are apparently not swallowing with abandon: specs._

_So here was the idea: take [PEP 750](https://peps.python.org/pep-0750/) and ask your future colleagues to make a demo for it._

_And for a tiny moment in time, it worked._

Sometimes I get a quick gig to help clients choose their future employees.

Filtering technical candidates is a delicate balance. On one hand, you might get hundreds of people reaching out, and you don't have the material resources to personally interview them all in person. On the other hand, imposing a heavy price for getting to a live call is disrespectful and inhuman.

While I don't think most of the time you should be hiring the elite (because, guess what, very few companies are actually working on an elite project, get off your high horse), that doesn't mean you should accept incompetence.

In 2010, we were already inundated with bullshit profiles, people attracted by the money but who [couldn't do a Fizz Buzz](https://blog.codinghorror.com/why-cant-programmers-program/), and this started the rise of take-at-home coding tests.

Of course, coding tests have the same balancing issue: you want something that can sort out impostors, but that won't make good devs flee because they have better to do with their lives than go through the hoops of every single prospective employer.

The solution I found is to make something trivial yet a little fun, but not too long, like level 3 or 4 of [AdventOfCode](https://adventofcode.com/). Then commit to spending as much time on reviewing the remaining good applications as they spent themselves applying, as a token of respect.

This doesn't work anymore thanks to LLM.

So I started a long quest of finding something that humans can perform with non-unfair amount of effort but not an AI.

At first, stuff like playing with cardinality (remember the strawberry thing?) or arithmetic sorta worked, but they fixed that.

So what now?

One day, I had a realization: LLM were good at things they were trained on, so the past. But have a harder time with things we might do in the future. What if we asked candidates a small exercise on a yet-to-be-implemented spec?

And so I went searching for something that was original enough to trip up machines, but interesting and not complicated in a way that keeps the humans we want in the loop.

Enter [PEP 750](https://peps.python.org/pep-0750/), the new t-string syntax that will be implemented in Python 3.14, coming out at the end of this year. The idea is to allow a syntax similar to f-strings interpolation, but with a `t` prefix:

`query = t"SELECT username from users where id='{user_id}'"`
The twist is, instead of `query` being a string, it results in a `Template` object that exposes separately the string part `SELECT username from users where id=` and the interpolated value part `user_id`.

The idea is to make it as convenient as string manipulation is for the developer, while allowing functions that are vulnerable to injections (bash commands, SQL queries, etc.) to easily process parameters that need escaping.

It's a great feature, and you can already test it because `uv` is awesome, and it supports beta Python versions as well:

```
uv self update
uv python install python3.14 
uvx python3.14
```

But even without this wonderful tool, the concept itself is not super complicated, and the spec is very clear. I expect any non-junior dev on my team to understand the PEP and be able to produce a PoC showcasing what it's supposed to do.

Hence, the following exercise was born:

> In Python 3.14 there will be a new feature called t-string.
> 
> 
> Here is the PEP: [https://peps.python.org/pep-0750/](https://peps.python.org/pep-0750/)
> 
> 
> It should help with things like avoiding injections. Create a run_command() function that demonstrates how it works. Make it simple, no need to be perfect. It should accept a t-string and execute it using subprocess. Then demonstrate how it helps with avoiding injections by comparing it to os.system() using a similar call with regular strings. Make it a self-contained script that I can run on python 3.14 beta.

To give you an idea, here is what I would come up with if I had to do so:

```
import os
import shlex
import subprocess
from string.templatelib import Template

def run_command(cmd: Template):
    result = []
    for item in cmd:
        if not isinstance(item, str):
            item = shlex.quote(item.value)
        result.append(item.strip())
    return subprocess.run(result)

if __name__ == "__main__":

    print('\nWithout injection:\n')
    dir_name = "."
    print('######## os.system')
    os.system(f"ls {dir_name}")
    print('######## run_command')
    run_command(t"ls {dir_name}")

    print('\nWith injection:\n')
    dir_name = ".; echo POWNED !!!!"
    print('######## os.system')
    os.system(f"ls {dir_name}")
    print('######## run_command')
    run_command(t"ls {dir_name}")
```

This will output something like this:

```
Without injection:

######## os.system
file1  file2
0
######## run_command
file1  file2
CompletedProcess(args=['ls', '.'], returncode=0)

With injection:

######## os.system
file1  file2
POWNED !!!!
0
######## run_command
ls: cannot access ''\''.; echo POWNED !!!!'\''': No such file or directory
CompletedProcess(args=['ls', "'.; echo POWNED !!!!'"], returncode=2)
```

I specifically state to make it simple, so a few lines just to show off the general idea are enough. Most of the time is spent reading the PEP, which is what I'm really testing the candidate against.

It is a tad longer to do than I wish it would be for a first filter. I was not completely happy with making all candidates go through that just for the privilege of being considered, but it was fairer than most tests I've seen around. So it had to do.

For several months, this worked beautifully. Neither Claude, Gemini, nor ChatGPT were able to solve it. They had never seen the syntax in any code, so they actually attempted to produce `f-string`, thinking I misspelled it.

Even today, ChatGPT and Gemini fail miserably at the task, both producing code that is conceptually wrong and not even syntactically correct.

Here is OpenAI's answer:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

import os
import subprocess

# ✅ SAFE: run a command using t-string and subprocess.run
def run_command(cmd: t-str):
"""Run a shell command safely using t-strings and subprocess.run."""
print(f"Running securely: {cmd}")
result=subprocess.run(cmd, capture_output=True, text=True)
print("Output:", result.stdout.strip())
if result.stderr:
print("Error:", result.stderr.strip())

# ❌ UNSAFE: vulnerable function using os.system
def vulnerable_command(user_input: str):
"""Run a shell command using os.system (vulnerable to injection)."""
cmd=f"echo Listing file: {user_input}"
print(f"Running insecurely: {cmd}")
os.system(cmd)

# === DEMO ===

# Simulated "safe" input
safe_input="safe_file.txt"

# Simulated "malicious" input that would cause injection in vulnerable code
malicious_input="safe_file.txt; echo 'Injected!' > /tmp/hacked"

print("\n--- SAFE COMMAND USING t-STRINGS ---")
run_command(t"echo Listing file: {safe_input}")

print("\n--- UNSAFE COMMAND USING os.system ---")
vulnerable_command(malicious_input)

# Show if /tmp/hacked was created (injected)
if os.path.exists("/tmp/hacked"):
print("\n⚠️ Injection succeeded! /tmp/hacked was created.")
with open("/tmp/hacked") as f:
print("Contents of /tmp/hacked:", f.read().strip())
else:
print("\n✅ Injection prevented. /tmp/hacked does not exist.")

You can see that not only does it contain an impossible type annotation, it also passes the template string object directly to `subprocess.run`, which only accepts strings.

Google doesn't do better:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

#!/usr/bin/env python3.14
# -*- coding: utf-8 -*-

"""
A demonstration of PEP 750's t-strings for safer command execution.

This script defines a `run_command` function that utilizes a custom
t-string tag to safely execute shell commands using the `subprocess` module.
It then contrasts this safe approach with a vulnerable command execution
using `os.system` and regular f-strings to highlight how t-strings
can prevent command injection attacks.

Note: This script must be run with a Python 3.14 interpreter that
supports t-strings (PEP 750).
"""

import shlex
import subprocess
import os
import sys
from typing import Any, List, Tuple

# --- T-String Implementation (as per PEP 750) ---

class ShellTag:
"""
A t-string tag processor for shell commands.

This class implements the `__process_string__` method, which is the
core of the t-string mechanism. It takes the literal parts of the
string and the interpolated values and processes them into a safe
list of command arguments.
"""
def __process_string__ (self, literals: Tuple[str, ...], values: Tuple[Any, ...]) ->List[str]:
"""
Processes the t-string into a list of shell arguments.

This method is called by the Python interpreter when it encounters
a string tagged with an instance of this class. It reconstructs
the string and then uses `shlex.split` to safely parse it into
a list of arguments, preventing malicious input from being
interpreted as part of the shell command itself.

Args:
literals: A tuple of the literal string parts.
values: A tuple of the interpolated values.

Returns:
A list of strings representing the command and its arguments.
"""
print(f"--- T-String Processor Invoked ---")
print(f"Literals: {literals}")
print(f"Values: {values}")

# Reconstruct the full string from its parts
full_string=""
for lit, val in zip(literals, values):
full_string+=lit
full_string+=str(val)
full_string+=literals[-1]

print(f"Reconstructed String: '{full_string}'")

# Use shlex.split to safely parse the command.
# This is crucial for preventing injection, as it correctly
# handles quotes and spaces.
args=shlex.split(full_string)
print(f"Parsed Arguments: {args}")
print(f"----------------------------------\n")
return args

# Create an instance of the tag processor.
# This 'sh' object will be used to tag our t-strings.
sh=ShellTag()

# --- Safe Function using T-Strings ---

def run_command(cmd_args: List[str]):
"""
Executes a command safely using subprocess.

This function expects a list of arguments, which is what our `sh`
t-string tag provides. It uses subprocess.run, which, when given a
list of arguments, does not invoke a shell. This is the safest way
to run external commands.

Args:
cmd_args: A list of strings, where the first element is the
command and the rest are its arguments.
"""
if not isinstance(cmd_args, list):
print(f"Error: run_command expects a list of arguments. "
f"Did you forget to use the 'sh' t-string tag?", file=sys.stderr)
return

print(f"✅ Running safe command with subprocess: {cmd_args}")
try:
result=subprocess.run(cmd_args, capture_output=True, text=True, check=True)
print("--- Command Output ---")
print(result.stdout)
print("----------------------")
except FileNotFoundError:
print(f"Error: Command not found: '{cmd_args[0]}'", file=sys.stderr)
except subprocess.CalledProcessError as e:
print(f"Error executing command: {e}", file=sys.stderr)
print(f"--- Stderr --- \n{e.stderr}", file=sys.stderr)

# --- Demonstration ---

def main():
"""
Main function to demonstrate safe vs. unsafe command execution.
"""
print("="*50)
print("Demonstrating Command Injection Prevention with T-Strings")
print("="*50+"\n")

# --- Scenario: Malicious Input ---
# An attacker provides a filename designed to inject a command.
# The injected command is `&& whoami`, which should not be executed.
malicious_filename="non_existent_file.txt && whoami"
print(f"😈 Malicious Input: '{malicious_filename}'\n")

# --- Vulnerable Example: os.system with f-string ---
print("1. VULNERABLE ATTEMPT with os.system and f-string")
print("-"*45)
# Here, the f-string directly embeds the malicious string.
# os.system passes this entire string to the system's shell (/bin/sh).
# The shell sees the '&&' and executes the `whoami` command as a
# separate, subsequent command.
unsafe_command=f"ls {malicious_filename}"
print(f"Executing unsafe command: os.system('{unsafe_command}')")
print("\n--- os.system Output ---")
os.system(unsafe_command)
print("------------------------")
print("😱 VULNERABILITY EXPOSED: The 'whoami' command was executed!\n\n")

# --- Secure Example: run_command with t-string ---
print("2. SECURE ATTEMPT with run_command and t-string")
print("-"*45)
# Now, we use our t-string. The `sh` tag triggers our ShellTag processor.
# `shlex.split` inside the processor correctly interprets
# "non_existent_file.txt && whoami" as a SINGLE argument.
# It does not see '&&' as a shell operator.
# The `run_command` function then receives a list: ['ls', 'non_existent_file.txt && whoami']
# The `ls` command is executed with this strange filename, and it will
# (correctly) fail to find the file. The `whoami` command is never run.
try:
# This is the new t-string syntax.
# The `sh` before the quote marks it as a typed string.
run_command(sh"ls {malicious_filename}")
except Exception as e:
print(f"An unexpected error occurred: {e}", file=sys.stderr)

print("✅ INJECTION PREVENTED: The malicious input was treated as a single, literal")
print(" filename argument, and the 'whoami' command was NOT executed.")

if __name__ =="__main__":
# Check for Python 3.14+
if sys.version_info< (3, 14):
print("This script requires Python 3.14 or newer to demonstrate t-strings.", file=sys.stderr)
sys.exit(1)
main()

It ignores the PEP link I gave and attempts to solve the problem with an old version of the spec (probably stored in the Google search cache).

And at first, Anthropic failed too.

This worked for a few months, but then something happened that changed the game: people started to write [tutorials on t-string](https://realpython.com/python-t-strings/). And one bot clearly trains on good dev blogs, because soon after a few publications, Claude started to make sense:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

#!/usr/bin/env python3.14
"""
Demonstration of Python 3.14's new t-string feature for secure command execution.
This script shows how t-strings help prevent command injection attacks.
"""

import subprocess
import os
import sys
from string.templatelib import Template, Interpolation

def run_command(template: Template) ->subprocess.CompletedProcess:
"""
Execute a command using a t-string template.

This function safely constructs a command list from a template,
preventing shell injection attacks by properly separating the
command and its arguments.
"""
# Build command list from template parts
cmd_parts= []

for item in template:
if isinstance(item, str):
# Static string parts are added as-is
if item.strip(): # Skip empty strings
cmd_parts.extend(item.split())
elif isinstance(item, Interpolation):
# Interpolated values are added as separate arguments
# This prevents them from being interpreted as shell metacharacters
value=str(item.value)
cmd_parts.append(value)

# Run the command with shell=False for safety
return subprocess.run(cmd_parts, capture_output=True, text=True, shell=False)

def demonstrate_injection_vulnerability():
"""Show how regular strings with os.system are vulnerable to injection."""
print("=== Demonstration: Command Injection Vulnerability ===\n")

# Simulated user input - normally this would come from untrusted source
user_input="test.txt; echo 'INJECTED COMMAND' > hacked.txt"

print(f"User input: {user_input}")
print("\n 1. Using os.system with string concatenation (VULNERABLE):")

# DON'T DO THIS - Vulnerable to injection!
command=f"echo 'Processing file: {user_input}'"
print(f" Command string: {command}")
print(" Executing with os.system()...")

# This would execute both commands if run
# os.system(command) # Commented out for safety
print(" [BLOCKED: Would execute injection if uncommented]\n")

print("2. Using subprocess with regular f-string (STILL VULNERABLE if misused):")
# Even with subprocess, using shell=True with f-strings is dangerous
command=f"echo 'Processing file: {user_input}'"
print(f" Command string: {command}")
# subprocess.run(command, shell=True) # Also vulnerable!
print(" [BLOCKED: Would execute injection with shell=True]\n")

def demonstrate_tstring_safety():
"""Show how t-strings provide safer command execution."""
print("=== Demonstration: T-String Safety ===\n")

# Same potentially malicious input
user_input="test.txt; echo 'INJECTED COMMAND' > hacked.txt"

print(f"User input: {user_input}")
print("\n 3. Using t-string with run_command (SAFE):")

# Create a t-string template
template=t"echo Processing file: {user_input}"

print(f" Template type: {type(template)}")
print(f" Static parts: {template.strings}")
print(f" Interpolations: [{', '.join(repr(i.value) for i in template.interpolations)}]")

# Execute safely
result=run_command(template)

print(f"\n Command executed safely!")
print(f" stdout: {result.stdout.strip()}")
print(f" stderr: {result.stderr.strip() if result.stderr else'(none)'}")
print(f" Return code: {result.returncode}")

def demonstrate_complex_example():
"""Show a more complex example with multiple interpolations."""
print("\n=== Demonstration: Complex T-String Example ===\n")

# Multiple user inputs
filename="data.csv"
search_term="'; DROP TABLE users; --"
output_file="results.txt"

print(f"Filename: {filename}")
print(f"Search term: {search_term}")
print(f"Output file: {output_file}\n")

# Using t-string for a grep-like command
template=t"grep {search_term} {filename}"

print("4. Complex command with t-string:")
print(f" Template strings: {template.strings}")
print(f" Number of interpolations: {len(template.interpolations)}")

# Show how each interpolation is handled
for i, interp in enumerate(template.interpolations):
print(f" Interpolation {i}: value={repr(interp.value)}, expr={repr(interp.expression)}")

# This would safely execute grep without risk of SQL injection
# result = run_command(template)
print("\n [Command would be executed safely, treating search_term as literal text]")

def demonstrate_format_spec():
"""Show how format specifications work in t-strings."""
print("\n=== Demonstration: Format Specifications ===\n")

count=42
precision=2

# T-string with format specification
template=t"Processing {count} items with {precision:.1f} precision"

print("5. T-string with format specifications:")
print(f" Template type: {type(template)}")

for i, interp in enumerate(template.interpolations):
print(f"\n Interpolation {i}:")
print(f" value: {interp.value}")
print(f" expression: {interp.expression}")
print(f" format_spec: {repr(interp.format_spec)}")
print(f" conversion: {interp.conversion}")

def main():
"""Run all demonstrations."""
print("Python 3.14 T-String Security Demonstration")
print("==========================================\n")

# Check Python version
if sys.version_info< (3, 14):
print(f"WARNING: This script requires Python 3.14 or later.")
print(f"You are running Python {sys.version}")
print("T-strings are not available in your Python version.\n")
return

# Run demonstrations
demonstrate_injection_vulnerability()
print("\n"+"="*60+"\n")

demonstrate_tstring_safety()
print("\n"+"="*60+"\n")

demonstrate_complex_example()
print("\n"+"="*60+"\n")

demonstrate_format_spec()

print("\n\n Key Takeaways:")
print("- T-strings provide access to both static and dynamic parts separately")
print("- This separation enables safe command construction without shell interpretation")
print("- User input is always treated as data, never as code")
print("- Format specifications and conversions are preserved for processing")

if __name__ =="__main__":
main()

The entire script is correct, runs on Python 3.14, and does, in fact, demonstrate a use of t-string.

Evidently, if a candidate were to send me this, I would flag the script right away:

*   It's full of redundant comments, and the docstring is futile.

*   The return value of `subprocess.CompletedProcess` is perfectionist to an extreme, which is the opposite of what you would expect from someone writing redundant comments and meaningless docstrings.

*   It's passing `shell=False` "for safety", but this is the default value of `subprocess.run`.

*   It's demonstrating SQL injections as well, something I never requested. Except it's not really doing that, if you look at the code, it just makes it up.

*   It's commenting out calls to `run_command` "for safety" despite the fact the values are hard-coded and it's a demo.

*   It's way too long and cleanly formatted, with way too many checks (like `sys.version`). Remember, I asked to keep it simple.

*   The injection demo is bogus and doesn’t execute the injected code.

*   It can't help itself and ends with "key takeaways".

But unless you are a total idiot, you can take the script, trim it down, and play pretend.

This test doesn't work anymore. It's solved, in the sense that somebody without the skills to pass it can do so with the help of tooling, and I could be fooled.

It goes without saying, but this particular instance of test only works if I intend to hire a moderately experienced backend Python dev. It won't work for a sysadmin, a data analyst, a junior, and so on.

And it's not going to fly anymore, anyway.

But the general idea stays valid. As long as the general public hasn't written about a concept, using RFC, specs, and even proposals still in discussion will converge on the hypothetical. That's in our favor.

Not because our future silicon overlords are not capable of it, it's just that their creators are not interested in solving those edge cases perfectly just yet. Until this blog post gets on their reading list, I guess.

Besides, it's an interesting exercise because it's closer to real work: it's not just about code, but about being a coder. And it makes for interesting discussions during the real interview, too. You can talk opinions, you can see curiosity, you can share points of view.

It's not just filtering bad devs, it's also making your first real contact with the good ones enjoyable. After all, we are planning to work together.