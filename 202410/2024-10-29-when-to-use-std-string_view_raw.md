Title: When to use std::string_view

URL Source: https://learnmoderncpp.com/2024/10/29/when-to-use-stdstring_view/

Published Time: 2024-10-29T09:27:18+00:00

Markdown Content:
C++17 brought us the class `std::string_view` in the standard library, which was touted as a lightweight, non-owning string-_like_ entity which could be passed cheaply as a function parameter. In this article we’re going to examine its best-practice use cases as well as where it’s neither necessary nor beneficial to use it.

At the most basic level, a `std::string_view` can be created from a C-style literal string, a `std::string` (this is an implicit conversion), another `std::string_view` or a pair of iterators:

void f(std::string\_view s) {
    // ...
}

f("C-String");
std::string str{ "String" };
f(str);
std::string\_view str\_vw{ "String View" };
f(str\_vw);
std::string str2{ "A very long string." };
std::string\_view str\_vw2(str2.begin() + 2, str2.begin() + 11);
f(str\_vw2);

A `std::string_view` object is typically implemented as a pointer and a length, so on 64-bit machines is 16 bytes in size and is **best passed by value**. The string data can be accessed through member function `data()` and the length through either `size()` or `length()`.

For a `std::string_view`, `data()` returns a `const char*` pointer which is not guaranteed to end with a null byte. It is important to note that there is no `c_str()` member function (unlike for `std::string`), although `std::string_view`s created from literals (with suffix `sv`), or whole `std::string`s can usually be assumed to end with a null byte:

auto str\_vw3 = "String view literal"sv;  // will have null byte

When passing string-like objects as arguments to functions, the following table outlines the implicit conversions between types (from column heading to row heading):

<table><tbody><tr><td data-align="center">To \ From</td><td data-align="center">std::string_view</td><td data-align="center">std::string</td><td data-align="center">“C-string literal”</td><td data-align="center">“String literal”s</td></tr><tr><td data-align="center">std::string_view</td><td data-align="center">✔</td><td data-align="center">✔</td><td data-align="center">✔</td><td data-align="center">✔</td></tr><tr><td data-align="center">const std::string&amp;</td><td data-align="center">✗</td><td data-align="center">✔</td><td data-align="center">✔ +</td><td data-align="center">✔</td></tr><tr><td data-align="center">const char*</td><td data-align="center"><code>data()</code> *</td><td data-align="center"><code>c_str()</code></td><td data-align="center">✔</td><td data-align="center"><code>c_str()</code></td></tr><tr><td data-align="center">std::string&amp;&amp;</td><td data-align="center">✗</td><td data-align="center"><code>std::move()</code></td><td data-align="center">✔ +</td><td data-align="center">✔</td></tr></tbody></table>

\* Must ensure ends with null byte + Involves construction of `std::string` object

The key takeaway is that `std::string` converts to `std::string_view`, but not vice-versa. Also construction of a `const std::string&` or `std::string&&` from C-string literal is not necessarily cheap.

If the arguments can be any type(s) in addition to `std::string`, using `std::string_view` as the parameter type may be beneficial to performance. If the arguments are always `std::string` l-values (ie. variables of type `std::string`) then `std::string_view` gives no performance benefit, and `const std::string&` should be used in preference. In addition when passing values through multiple function calls, keeping `const std::string&` may improve performance.

Other features of `std::string_view` include member functions such as `begins_with()` and `ends_with()` (as for `std::string`) as well as `substr()`, `compare()`, `contains()` and the `find()` family. It also contains member functions `remove_prefix()` and `remove_suffix()` which `std::string` does not have, shrinking the object from the beginning or end. It is unlikely that lack of functionality is a reason to not use `std::string_view` instead of `std::string`.

In this article we have looked at `std::string_view`‘s chief claim to fame, which is that it can be cheaply passed by value to functions accepting a variety of standard string-like types. However it is not always preferable to using parameter type of `const std::string&` in the case when the parameter is (almost) always a `std::string` l-value.

Post navigation
---------------
