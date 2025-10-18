Title: Use weird tests to capture tacit knowledge

URL Source: https://jmduke.com/posts/post/weird-tests-tacit-knowledge/

Markdown Content:
2024-03-04

Working on [Buttondown](https://buttondown.com/) — or any mature, complex codebase — effectively and quickly requires a lot of tacit knowledge that I've done a hitherto-poor job of documenting, a fact I am learning more and more quickly as I start to scale up the number of folks working on the codebase.

_Documentation_ in the literal sense is a good first step and final step, of course, but when a codebase is in the "process" of being documented writing down "this is how you do X" does often not actually _solve_ the problem of making sure everyone can do X safely and quickly.

One thing that I've found useful, in the spirit of shifting process to the left, is capturing steps in tests. Here's a simple (but real!) example: adding new Django modules to the codebase. Whenever you run `python manage.py startapp`, you _also_ need to add the new app to a bunch of different places:

*   `pytest.ini`, so tests are run;
*   `pyproject.toml`, so files are linted;
*   `modules.txt`, so metrics are exported.

The _perfect_ solution to this problem is creating a script that automatically adds a new app to all the relevant places and stuffing it into a Justfile, but that's a pretty big piece of work that requires thought and error handling and a whole slew of other stuff. Instead, it's comparatively easy to just capture these constraints in a test:

```
# This test suite ensures that, when we create or rename a module,
# we update all the relevant configurations so that we lint/test/etc. that module.
from django.conf import settings

RELEVANT_FILES = ["./pyproject.toml", "./pytest.ini", "./modules.txt"]

def pytest_generate_tests(metafunc):
    parameters = []
    for filename in RELEVANT_FILES:
        for module in settings.BUTTONDOWN_APPS:
            parameters.append((module, filename))
    metafunc.parametrize("module,filename", parameters)

def test_module_is_present_in_pytest(module: str, filename: str) -> None:
    assert module in open(filename).read()
```

This approach also works well when you're trying to enforce a norm or invariant for all _new_ code. (At Stripe, we called this approach "ratchet testing", though initial Googling seems to indicate that this metaphor has not exactly spread like wildfire.)

Another example: Buttondown uses Django-Ninja to generate an OpenAPI spec from the live API. OpenAPI is great, but it [sadly lacks an ergonomic ability to document each value of an enum](https://github.com/OAI/OpenAPI-Specification/issues/348), so we maintain a separate `enums.json` file that needs to be updated whenever a relevant enum has a new addition — even though some enum values are undocumented!

A similar approach works well here:

```
import json

ENUMS_FILENAME = "../shared/enums.json"
OPENAPI_SPEC_FILENAME = "assets/autogen/openapi.json"

RAW_ENUMS = json.load(open(ENUMS_FILENAME))
RAW_OPENAPI_SPEC = json.load(open(OPENAPI_SPEC_FILENAME))

def pytest_generate_tests(metafunc):
    parameters = []
    enums = RAW_ENUMS.keys()
    for enum_name in enums:
        extant_enum_values = RAW_OPENAPI_SPEC["components"]["schemas"][enum_name][
            "enum"
        ]
        for enum_value in extant_enum_values:
            parameters.append((enum_name, enum_value))
    metafunc.parametrize("enum_name,enum_value", parameters)

# Do not add more items to this ratchet unless you need to!
KNOWN_MISSING_PAIRS = [
    ("CreateSubscriberErrorCode", "metadata_invalid"),
    ("ExternalFeedAutomationCadence", "daily"),
    ("UpdateSubscriberErrorCode", "email_already_exists"),
    # ... and so on.
]

# This technically does not exercise Python code; it's testing that `shared/enums.json` is up to date.
def test_enum_is_exhaustively_documented(enum_name: str, enum_value: str) -> None:
    assert (
        enum_name in RAW_ENUMS
    ), f"Enum {enum_name} is not documented in {ENUMS_FILENAME}"
    if (enum_name, enum_value) in KNOWN_MISSING_PAIRS:
        return
    assert (
        enum_value in RAW_ENUMS[enum_name]
    ), f"Potential value {enum_value} of enum {enum_name} is not documented in {ENUMS_FILENAME}"
```

What I find _most_ lovely about this approach is that test-driven invariants are self-documenting. A task like "adding a new value to an existing enum" is not obviously a thing that should require searching an internal knowledge base, but a test that captures information about it can contain code pointers, technical explanation, _and_ a way to fix it.

In general, a good mental exercise whenever you're reviewing a PR is "could a test have caught this?", and then reminding yourself that a test should be defined less as "a thing that exercises business logic" and more as a "script that exercises your codebase".