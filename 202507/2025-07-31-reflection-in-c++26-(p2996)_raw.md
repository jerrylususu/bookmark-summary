Title: Reflection in C++26 (P2996)

URL Source: https://learnmoderncpp.com/2025/07/31/reflection-in-c26-p2996/

Published Time: 2025-07-31T10:17:00+00:00

Markdown Content:
This article is intended to summarize the state of play in the upcoming C++26 Standard as regards reflection, which is where information (metadata) about the source code is made available for use at run-time, as opposed to only being available at compile-time. Proposal P2996 is the main (initial) paper for the implementation of reflection in C++, and has been voted into C++26 as of June 2025. An “experimental” branch of Clang (available on [Compiler Explorer](https://godbolt.org/)) currently implements a number of features from this paper (note that not all of the code in this article compiles at present, as syntax is in a state of flux).

The basics of the implementation center around two concepts, the new unary operator (`^^`) and the opaque `consteval` type `std::meta::info` defined within a new header `<meta>`. (The operator was previously reusing `^`, but this apparently conflicts with a non-standard Clang extension.) Applying this operator to any entity yields a `std::meta::info` object:

`#include <meta>`

`int``i;`

`consteval``std::meta::info i_info = ^^i;`

Keep in mind that while `auto` can optinally be used to deduce the type, either a `consteval` or `constexpr` qualifier **must be present**. The `std::meta::info` type produced is unique to the entity which provided it, in a similar fashion to machine addresses of lvalues being unique in C++. This program shows a more complete usage (note obligatory uses of `consteval` and `constexpr`):

`#include <meta>`

`#include <iostream>`

`struct``S {};`

`int``main() {`

```S s{};`

```consteval``std::meta::info outer_s = ^^s;`

```{`

```S s{};`

```consteval``std::meta::info inner_s = ^^s;`

```constexpr``auto``inner_s_copy = inner_s;`

```constexpr``bool``outer_not_inner = ( outer_s != inner_s );`

```constexpr``bool``inner_is_inner = ( inner_s == inner_s_copy );`

```std::cout << std::boolalpha`

```<< outer_not_inner <<``' '`

```<< inner_is_inner <<``'\n'``;`

```}`

`}`

The output from this program is `true true` showing that `std::meta::info` objects from the same type and the same name but within different scopes compare non-equal, while copies of `std::meta::info` objects compare equal.

_Introspection_ is the name given to querying reflected information, and a number of `consteval` functions exist to perform this (currently implemented as traits templates in the style of other parts of the standard library).

`#include <meta>`

`struct``Point {`

```int``x;`

```int``y;`

`};`

`static_assert``(std::meta::name_v<^^Point> ==``"Point"``);`

`static_assert``(std::meta::name_v<^^Point::x> ==``"x"``);`

(It is assumed that `std::meta::name_v` returns a object of type `constexpr std::string_view`.)

In addition to simple templates such as `std::meta::is_public_v<^^T>`, `std::meta::nonstatic_data_members_of<^^T>` yields an iterable `std::meta::info_range`:

`for``(``constexpr``std::meta::info member : std::meta::nonstatic_data_members_of<^^Point>) {`

```std::cout << std::meta::name_v<^^member> <<``'\n'``;`

`}`

Importantly, type information can be extracted and used to declare entities of the same type(s) with the _splicing_ syntax `[: ... :]`:

`constexpr``std::meta::info type_of_x = std::meta::type_v<^^Point::x>;`

`static_assert``(std::meta::name_v<type_of_x> ==``"int"``);`

`[:type_of_x:] new_variable;`

Splicing can also index into fields of composite types:

`Point p{ 24, 42 };`

`constexpr``std::meta::info member_y = std::meta::nonstatic_data_members_of<^^Point>[1];`

`std::cout << p.[:member_y:] <<``'\n'``;`

Custom extended annotations are supported extending the existing `[[...]]` syntax, allowing for features within classes to be switched on or off at compile time in conjunction with strongly-typed feature-describing `enum`s. In the code below the `Ultra::cache` member is not intended to be part of `Ultra`‘s value as regards hashing:

`enum``class``HashNotes { ignore };`

`struct``Ultra {`

```float``data[3];`

```[[=HashNotes::ignore]] Cache cache;`

```...`

`};`

A generic hash function can then be improved to check for these annotations and skip members that are marked to be ignored:

`if``(annotation_of_type<HashNotes>(data_member) != HashNotes::ignore) {`

`}`

For a more complex use-case of the implementation of extended annotations, see the clap (Command-Line Argument Parsing) project which is built with reflection. The user defines the command-line interface with a simple `struct`, using annotations to specify help messages, short names, and long names for each argument. The clap library handles all the parsing logic based on the `Args``struct`‘s definition, resulting in clean and intuitive user code:

`struct``Args : clap::Clap {`

```[[=Help(``"Name to greet"``)]]`

```[[=Short, =Long]]`

```std::string name;`

```[[=Help(``"Number of times to greet"``)]]`

```[[=Long(``"repeat"``)]]`

```int``count = 1;`

`};`

`int``main(``int``argc,``char``** argv) {`

```Args args;`

```args.parse(argc, argv);`

```for``(``int``i = 0; i < args.count; ++i) {`

```std::cout <<``"Hello "``<< args.name <<``"!\n"``;`

```}`

`}`

The library uses reflection to iterate through the members of the user-defined `struct`.

It queries the annotations for each member to configure the command-line options (e.g., setting up help text, short/long flags). This is made possible by features like `nonstatic_data_members_of`, `annotations_of`, and C++23’s “deducing this” to create a highly generic and reusable parser.

As interesting as paper P2996 is, it should only be seen as the initial step in a process of making the coding process cleaner. Upcoming is paper P3294 which facilitates _code injection_ (via token injection) to create on-demand C++ code. Exciting stuff.

That wraps things up for this article. It’s looking like Clang is ahead on implementing these features, but look out for them in other compilers after the C++26 standard is published (hopefully early next year).

Post navigation
---------------
