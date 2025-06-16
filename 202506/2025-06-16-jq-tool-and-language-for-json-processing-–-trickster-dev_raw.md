Title: tool and language for JSON processing – Trickster Dev

URL Source: https://www.trickster.dev/post/jq-tool-and-language-for-json-processing/

Published Time: Sat, 14 Jun 2025 16:27:45 GMT

Markdown Content:
JSON is the dominant data representation format for most of the modern RESTful APIs and certain automation/devops tools (Terraform, AWS CLI, kubectl, etc.) optionally output data in JSON format to make it machine readable. Some datasets (e.g. service price lists from health insurance companies) are available primarily as JSON files. For these reasons parsing, generation, modification and analysis of JSON documents is nothing new for many explorers of cyberspace. Indeed, there are libraries and tools to wrangle JSONified data in pretty much all popular general purpose programming languages. But what about shell scripts? When one is programming in Bash or Zsh it might be necessary to run some curl(1) snippet and extract parts of API response, but your standard Unix text processing tools - awk(1), sed(1), grep(1) and others largely predate JSON popularity and are not designed with nested data trees in mind. [jq](https://jqlang.github.io/jq/) is CLI tool that was designed to fill the gap here and addresses the need of making JSON wrangling easier within the Unix/Linux environment. But it is not merely a CLI tool. Like AWK, it is also a Turing-complete domain specific language that lets you implement arbitrarily complex (within limits of computability) JSON document processing scripts.

One can install jq via the usual package managers:

*   `brew install jq` on macOS with Homebrew.
*   `apt-get install jq` on Debian and many Debian-based distributions.
*   `pacman -S jq` on Arch Linux.
*   `pkg install jq` on FreeBSD.

Furthermore, jq project ships ready-to-use binary files as part of their [release deliverables](https://github.com/jqlang/jq/releases). To get the official Docker image with jq one can run `docker pull ghcr.io/jqlang/jq:latest`.

There is also [jqplay.org](https://jqplay.org/) - a web playground for playing with jq language without installing anything (but not for processing large JSON documents).

The syntax of jq has similarities with JSON syntax. The very simplest thing one can do in jq is pretty printing the input for readability (this can be turned off with `--compact-output` or `-c`):

```
$ echo '{"x": 1, "y": 2}' | jq '.'
{
  "x": 1,
  "y": 2
}
```

By default jq makes output colored for easier reading. We used jq identity statement as the first argument.

We may want to create JSON object or list in jq language. Syntax to do so is very similar to JSON notation:

```
$ jq --null-input '{a: 1, b: 2}'
{
  "a": 1,
  "b": 2
}
$ jq --null-input '[1,3,5,7,11]'
[
  1,
  3,
  5,
  7,
  11
]
```

To extract a single field from JSON object we can use object identifier-index syntax - dot character with field name:

```
$ echo '{"x": 1, "y": 2}' | jq '.x'
1
```

This can be done across multiple levels:

```
$ echo '{"coord": {"x": 1, "y": 2}}' | jq '.coord.y'
2
```

Like other programming languages, JSON arrays can be indexed:

```
$ echo '{"coords": [{"x": 1.1, "y": 2.5}]}' | jq '.coords[0].y'
2.5
```

Like in Python, arrays can be sliced by index range:

```
$ echo '[1,2,3,4,5]' | jq '.[1:3]'
[
  2,
  3
]
```

If used without indices, `[]` is iterator - it returns all values within the input list or object:

```
$ echo '[1,2,3,4,5]' | jq '.[]'   
1
2
3
4
5
$ echo '{"a": 1, "b": 2}' | jq '.[]'
1
2
```

Note that first index in the range is inclusive, but not the second one - second index tells jq to extract values _up to_ that index.

JSON data types have the same syntax in jq language as in JSON notation:

```
$ jq --monochrome-output --null-input 'null'   
null
$ jq --null-input '1.2'   
1.2
$ jq --null-input '"str"' 
"str"
$ jq --null-input 'false'
false
$ jq --null-input '{"latitude": 1.1, "longitude": 2.2}' 
{
  "latitude": 1.1,
  "longitude": 2.2
}
$ jq --null-input '["a", "b", "c"]' 
[
  "a",
  "b",
  "c"
]
```

Like in Unix environment, pipe character can be used to build pipelines of operations:

```
$ jq --null-input '{"latitude": 1.1, "longitude": 2.2} | .latitude'
1.1
```

Comma character can be used to concatenate outputs from two or more operations into single stream:

```
$ jq --null-input '{"latitude": 1.1, "longitude": 2.2} | .latitude, .longitude'  
1.1
2.2
```

Furthermore, jq language allows using question mark character as optional operator. Like in Swift programming language, this allows for parts of input (e.g. a subtree in JSON document) to be missing without crashing the program. If something is not missing, further operations will be executed. If it is missing, the entire chain of operations will return null value:

```
$ echo '{"coords": [{"x": 1.1, "y": 2.5}]}' | jq '.coords?[0].y'
2.5
$ echo '{"coords": [{"x": 1.1, "y": 2.5}]}' | jq '.coordinates?[0].y'
null
```

Like all the proper programming languages, jq has operators for basic math operations:

```
$ jq --null-input '1 + 1'
2
$ jq --null-input '1 - 1'
0
$ jq --null-input '1 * 2'
2
$ jq --null-input '1 / 2'
0.5
$ jq --null-input '5 % 2' 
1
```

Multiplication operator can also be used to make repeated string:

```
$ jq --null-input '"cyber" * 3'
"cybercybercyber"
```

Furthermore, jq has some built-in functions for common computations and data processing operations. For example, `length` is equivalent to Python’s `len()` function:

```
$ echo '"abc"' | jq 'length'   
3
$ echo '[1, 2, 3, 4]' | jq 'length'
4
```

The jq language does not have for or while loops. Instead, we are supposed to use two brackets (`[]`) - iteration operator and/or `range` function:

```
$ jq --null-input 'range(100)'
0
1
2
3
4
...
96
97
98
99
100
$ jq --null-input '[range(100)]' | jq '.[] | . + 1000' | head
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
```

In jq language `map` is equivalent to `map()` in Python and `select` is equivalent to `filter()`.

This allows us to implement data processing in FP-like manner:

```
$ echo "[1000, 2000, 3000, 5000, 9001, 10240]" | jq '.[] | select(. > 9000)'
9001
10240
$ echo '["corpothieves", "must", "die"]' | jq 'map(length)'
[
  12,
  4,
  3
]
```

If we don’t want to use `select` we can use regular if-then-else control flow feature of jq:

```
$ echo "9001" | jq 'if . > 9000 then "over nine thousand" else "below 9000" end'
"over nine thousand"
```

I asked Google Gemini 2.5 to write Fizzbuzz code in jq language. Take a look:

```
range(1; 101) |
  if . % 15 == 0 then
    "FizzBuzz"
  elif . % 3 == 0 then
    "Fizz"
  elif . % 5 == 0 then
    "Buzz"
  else
    .
  end
```

It can be launched with following command:

```
$ jq -n -r -f fizzbuzz_standard.jq
```

There is also IEEE754 double precision floating point number support so you can do trigonometry and stuff. See the [documentation](https://jqlang.github.io/jq/manual/#builtin-operators-and-functions) for a list of built-in functions available.

Many programming languages provide a way to develop reusable pieces of code that can be accessed via API. We already tried some jq functions that are shipped with standard installation. To define jq module we must create file with `.jq` extension and write one more jq functions in there like it is done in [src/builtin.jq](https://github.com/jqlang/jq/blob/master/src/builtin.jq) file.

Now it’s time for a real-worldish example of using jq for data extraction. But first, let me show you a trick. Pretty much all Shopify stores that don’t use custom frontend expose some APIs with product data. First, `/products.json` endpoint provides a product list. It acts as paginated Product List Page (PLP) API with parameters `page` for page number (starting with 1) and `limit` for page size (can be up to 250). See the following examples:

*   [https://hypebeastbaltics.com/products.json](https://hypebeastbaltics.com/products.json)
*   [https://hypebeastbaltics.com/products.json?limit=10&page=1](https://hypebeastbaltics.com/products.json?limit=10&page=1)
*   [https://hypebeastbaltics.com/products.json?limit=10&page=2](https://hypebeastbaltics.com/products.json?limit=10&page=2)

It should be noted that sometimes primary store domain cannot be used and should be replaced with .myshopify subdomain that can be found in page source. For our example store that would be online-hypebeastbaltics.myshopify.com.

[Screenshot 1](https://www.trickster.dev/2025-04-26_15.57.30.png)

If you want individual product data from the store that can be retrieved by appending `.js` or `.json` to PDP URL path. This will give you slightly different versions of the data and, depending on the target, fields regarding inventory or product availability might be present in one form, but not in another. For example the following URLs can be used for API scraping:

*   [https://hypebeastbaltics.com/products/nike-air-force-1-low-supreme-white.js](https://hypebeastbaltics.com/products/nike-air-force-1-low-supreme-white.js)
*   [https://hypebeastbaltics.com/products/nike-air-force-1-low-supreme-white.json](https://hypebeastbaltics.com/products/nike-air-force-1-low-supreme-white.json)

It is also possible to retrieve products from collection, e.g.:

*   [https://hypebeastbaltics.com/collections/clothing-1/products.json](https://hypebeastbaltics.com/collections/clothing-1/products.json)
*   [https://hypebeastbaltics.com/collections/clothing-1/products.json?limit=5&page=2](https://hypebeastbaltics.com/collections/clothing-1/products.json?limit=5&page=2)

This can be used to gather data programmatically at PLP and PDP levels from Shopify store with little to no need for HTML page scraping. Since the response data format is JSON, we can use jq to extract the interesting parts. We will still need something else to implement the remaining parts of API scraping code. In this case we will use Bash scripting language.

```
#!/bin/bash

set -x

URL="https://hypebeastbaltics.com/products.json"
PER_PAGE=250
PAGE=1

echo "id,title,body_html,vendor,product_type,price,handle" > hbb.csv

while true ; do
    JSON_STR=$(curl "$URL?page=$PAGE&limit=$PER_PAGE")
    echo "$JSON_STR" | jq -r '.products[] | [.id, .title, .body_html, .vendor, .product_type, .variants[0].price, .handle] | @csv' >> hbb.csv
    N_PRODUCTS=$(echo "$JSON_STR" | jq -r '.products | length')
    if [[ "$N_PRODUCTS" -lt "$PER_PAGE" ]]; then
        break
    fi
    PAGE=$((PAGE+1))
done
```

The jq codebase is in C, but the underlying “backend” of the language can be used as a shared library - libjq. This would enable using it as DSL outside shell scripts. But the thing is, unless what you do is in the realm of systems programming you probably do not want to use [libjq C API](https://github.com/jqlang/jq/wiki/C-API:-jv) in your own code. For our convenience there are wrappers in higher level languages:

*   [`jq` for Python](https://pypi.org/project/jq/) - available from PIP.
*   [`jq-rs` for Rust](https://crates.io/crates/jq-rs)
*   [`node-jq` for Node.js](https://www.npmjs.com/package/node-jq)
*   [JSON::JQ for Perl](https://metacpan.org/pod/JSON::JQ)

For example, the Python module makes API scraping code less tedious:

```
>>> import requests
>>> import jq
>>> from pprint import pprint
>>> resp = requests.get("https://hypebeastbaltics.com/products.json")
>>> titles = jq.compile(".products[].title").input(text=resp.text).all()
>>> pprint(titles)
['Denver Broncos fitted hat brown corduroy 7 3/4',
 'Denver Broncos fitted hat Black 8',
 'Dallas Cowboys Superbowl fitted hat navy 7 1/8',
 'Minnesota Vikings fitted hat pink 7 1/4',
 'San Diego Padres fitted hat white green 7 1/2',
 'San Francisco 49ers fitted hat  7 3/8',
 'Los Angeles Rams fitted hat white 7 3/8',
 'San Antonio Spurs fitted hat Grey 7 3/8',
 'New York Yankees fitted hat Navy 6 3/8',
 'CDG Polka Dot With Upside Down Heart T-Shirt White',
 'Used adidas Yeezy Boost 350 V2 Cream',
 'Used Adidas Ultra Boost 4.0 Bape Camo',
 'Used Adidas Yeezy Boost 350 V2 Earth',
 'Used Yeezy 500 Utility Black',
 'Used adidas Yeezy Boost 350 V2 MX Oat',
 'Used Yeezy 700 V3 Clay Brown',
 'Used Yves Saint Laurent Leather high trainers',
 'Used Louis Vuitton Boxing High Top Triple Black',
 'Pop Mart Labubu The Monsters Lazy Yoga Series Figures Blind Box',
 'Pop Mart The Monsters Labubu Zimomo Angel in Clouds Figure (No Tote)',
 'Nike x Jacquemus Le Polo Off-White',
 'Nike x NOCTA NRG Knit Long Sleeve Top Cobalt Bliss/Dark Obsidian',
 'COMING 6TH JUNE Pop Mart Labubu The Monsters Have a Seat Vinyl Plush Sealed '
 'Case (6 Blind Boxes)',
 'COMING 6TH JUNE Pop Mart Labubu The Monsters Tasty Macarons Vinyl Plush '
 'Pendant Single Blind Box',
 'Corteiz Olympic Shuku Nigeria Jacket Green/White',
 'Nike x NOCTA NRG Short Cobalt Bliss/White',
 'Pop Mart Labubu The Monsters Big into Energy Series Vinyl Plush Pendant '
 'Sealed Case (6 Blind Boxes)',
 'COMING 6TH JUNE Pop Mart Labubu The Monsters Exciting Macarons Vinyl Face '
 'Blind Box Whole Set',
 'Used Supreme Bandana Tarp Side Bag',
 'Used Carolina Panthers Fitted Cap']
```

[Gojq project](https://github.com/itchyny/gojq) reimplements the language in pure Go and does not rely on the C codebase. It can be used as CLI tool and integrated into other software as library.

Some interesting codebases using jq language:

*   [jnv](https://github.com/ynqa/jnv) - interactive tool to browse JSON data and prototype jq one-liners in a terminal.
*   [jqview](https://github.com/fiatjaf/jqview) - Qt-based GUI app based on Gojq.
*   [tq](https://github.com/jdolitsky/tq) - tool to manipulate Terraform objects with jq language.

Trickster Dev
-------------

Code level discussion of web scraping, gray hat automation, growth hacking and bounty hunting

* * *

By rl1987, 2025-06-14
