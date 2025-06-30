Title: Use keyword-only arguments in Python dataclasses – ChipLog — Christian Hammond

URL Source: https://chipx86.blog/2025/06/29/tip-use-keyword-only-arguments-in-python-dataclasses/

Markdown Content:
Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) are a really nice feature for constructing classes that primarily hold or work with data. They can be a good alternative to using dictionaries, since they allow you to add methods, dynamic properties, and subclasses. They can also be a good alternative to building your own class by hand, since they don’t need a custom `__init__()` that reassigns attributes and provide methods like `__eq__()` out of the box.

One small tip to keeping dataclasses maintainable is to always construct them with `kw_only=True`, like so:

1

2

3

4

5

6

7

8`from``dataclasses``import``dataclass`

`@dataclass``(kw_only``=``True``)`

`class``MyDataClass:`

```x:``int`

```y:``str`

```z:``bool``=``True`

This will construct an `__init__()` that looks like this:

1

2

3

4

5

6

7

8

9

10

11`class``MyDataClass:`

```def``__init__(`

```self``,`

```*``,`

```x:``int``,`

```y:``str``,`

```z:``bool``=``True``,`

```)``-``>``None``:`

```self``.x``=``x`

```self``.y``=``y`

```self``.z``=``z`

Instead of:

1

2

3

4

5

6

7

8

9

10`class``MyDataClass:`

```def``__init__(`

```self``,`

```x:``int``,`

```y:``str``,`

```z:``bool``=``True``,`

```)``-``>``None``:`

```self``.x``=``x`

```self``.y``=``y`

```self``.z``=``z`

That `*` in the argument list means everything that follows must be passed as a keyword argument, instead of a positional argument.

There are two reasons you probably want to do this:

1.   It allows you to reorder the fields on the dataclass without breaking callers. Positional arguments means a caller can use `MyDataClass(1, 'foo', False)`, and if you remove/reorder any of these arguments, you’ll break those callers unexpectedly. By forcing callers to use `MyDataClass(x=1, y='foo', z=False)`, you remove this risk.
2.   It allows subclasses to add required fields. Normally, any field with a default value (like `z` above) will force any fields following it to also have a default. And that includes _all_ fields defined by subclasses. Using `kw_only=True` gives subclasses the flexibility to decide for themselves which fields must be provided by the caller and which have a default.

These reasons are more important for library authors than anything. We spend a lot of time trying to ensure backwards-compatibility and forwards-extensibility in [Review Board](https://www.reviewboard.org/), so this is an important topic for us. And if you’re developing something reusable with dataclasses, it might be for you, too.

**Update:** One important point I left out is Python compatibility. This flag was introduced in Python 3.10, so if you’re supporting older versions, you won’t be able to use this just yet. If you want to optimistically enable this just on 3.10+, one approach would be:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17`import``sys`

`from``dataclasses``import``dataclass`

`if``sys.version_info[:``2``] >``=``(``3``,``10``):`

```dataclass_kwargs``=``{`

```'kw_only'``:``True``,`

```}`

`else``:`

```dataclass_kwargs``=``{}`

`...`

`@dataclass``(``*``*``dataclass_kwargs)`

`class``MyDataClass:`

```...`

`...`

But this won’t solve the subclassing issue, so you’d still need to ensure any subclasses use default arguments if you want to support versions prior to 3.10.
