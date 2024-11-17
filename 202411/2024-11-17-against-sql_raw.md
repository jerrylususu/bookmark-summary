Title: Against SQL

URL Source: https://www.scattered-thoughts.net/writing/against-sql/

Markdown Content:
TLDR
----

The relational model is great:

*   A shared universal data model allows cooperation between programs written in many different languages, running on different machines and with different lifespans.
*   Normalization allows updating data without worrying about forgetting to update derived data.
*   Physical data independence allows changing data-structures and query plans without having to change all of your queries.
*   Declarative constraints clearly communicate application invariants and are automatically enforced.
*   Unlike imperative languages, relational query languages don't have false data dependencies created by loop counters and aliasable pointers. This makes relational languages:
    *   A good match for modern machines. Data can be rearranged for more compact layouts, even automatic compression. Operations can be reordered for high cache locality, pipeline-friendly hot loops, simd etc.
    *   Amenable to automatic parallelization.
    *   Amenable to incremental maintenance.

But SQL is the only widely-used implementation of the relational model, and it is:

*   [Inexpressive](https://www.scattered-thoughts.net/writing/against-sql/#inexpressive)
*   [Incompressible](https://www.scattered-thoughts.net/writing/against-sql/#incompressible)
*   [Non-porous](https://www.scattered-thoughts.net/writing/against-sql/#non-porous)

This isn't just a matter of some constant programmer overhead, like SQL queries taking 20% longer to write. The fact that these issues exist in our dominant model for accessing data has dramatic downstream effects for the entire industry:

*   [Complexity is a massive drag on quality and innovation in runtime and tooling](https://www.scattered-thoughts.net/writing/against-sql/#complexity-drag)
*   [The need for an application layer with hand-written coordination between database and client renders useless most of the best features of relational databases](https://www.scattered-thoughts.net/writing/against-sql/#the-application-layer)

The core message that I want people to take away is that there is potentially a huge amount of value to be unlocked by [replacing SQL](https://www.scattered-thoughts.net/writing/against-sql/#after-sql), and more generally in rethinking where and how we draw the lines between databases, query languages and programming languages.

Inexpressive
------------

Talking about expressiveness is usually difficult, since it's a very subjective measure. But SQL is a particularly inexpressive language. Many simple types and computations can't be expressed at all. Others require far more typing than they need to. And often the structure is fragile - small changes to the computation can require large changes to the code.

### Can't be expressed

Let's start with the easiest examples - things that can't be expressed in SQL at all.

For example, SQL:2016 added support for json values. In most languages json support is provided by a library. Why did SQL have to add it to the language spec?

First, while SQL allows user-defined types, it doesn't have any concept of a sum type. So there is no way for a user to define the type of an arbitrary json value:

```
enum Json {
    Null,
    Bool(bool),
    Number(Number),
    String(String),
    Array(Vec<Value>),
    Object(Map<String, Value>),
}
```

The usual response to complaints about the lack of sum types in sql is that you should use an id column that joins against multiple tables, one for each possible type.

```
create table json_value(id integer);
create table json_bool(id integer, value bool)
create table json_number(id integer, value double);
create table json_string(id integer, value text);
create table json_array(id integer);
create table json_array_elements(id integer, position integer, value json_value, foreign key (value) references json_value(id));
create table json_object(id integer);
create table json_object_properties(id integer, key text, value json_value, foreign key (value) references json_value(id));
```

This works for data modelling (although it's still clunky because you must try joins against each of the tables at every use site rather than just ask the value which table it refers to). But this solution is clearly inappropriate for modelling a value like json that can be created inside scalar expressions, where inserts into some global table are not allowed.

Second, parsing json requires iteration. SQLs `with recursive` is limited to linear recursion and has a bizarre choice of semantics - each step can access only the results from the previous step, but the result of the whole thing is the union of all the steps. This makes parsing, and especially backtracking, difficult. Most SQL databases also have a procedural sublanguage that has explicit iteration, but there are few commonalities between the languages in different databases. So there is no pure-SQL json parser that works across different databases.

Third, most databases have some kind of extension system that allows adding new types and functions using a regular programming language (usually c). Indeed, this is how json support first appeared in many databases. But again these extension systems are not at all standardized so it's not feasible to write a library that works across many databases.

So instead the best we can do is add json to the SQL spec and hope that all the databases implement it in a compatible way (they don't).

The same goes for xml, regular expressions, windows, multi-dimensional arrays, periods etc.

Compare [how flink exposes windowing](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/datastream/operators/windows/#windows):

*   The interface is made out of objects and function calls, both of which are first-class values and can be stored in variables and passed as function arguments.
*   The style of windowing is defined by a [WindowAssigner](https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/streaming/api/windowing/assigners/WindowAssigner.html#assignWindows-T-long-org.apache.flink.streaming.api.windowing.assigners.WindowAssigner.WindowAssignerContext-) which simply takes a row and returns a set of window ids.
*   Several common styles of windows are provided as library code.

Vs SQL:

*   The interface adds a [substantial amount of new syntax](https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS) to the language.
*   The windowing style is purely syntactic - it is not a value that can be assigned to a variable or passed to a function. This means that we can't compress common windowing patterns.
*   Only a few styles of windowing are provided and they are hard-coded into the language.

Why is the SQL interface defined this way?

Much of this is simply cultural - this is just how new SQL features are designed.

But even if we wanted to mimic the flink interface we couldn't do it in SQL.

*   Functions are not values that can be passed around, and they can't take tables or other functions as arguments. So complex operations such as windowing can't be added as stdlib functions.
*   Without sum types we can't even express the hardcoded windowing styles as a value. So we're forced to add new syntax whenever we want to parameterize some operation with several options.

### Verbose to express

Joins are at the heart of the relational model. SQL's syntax is not unreasonable in the most general case, but there are many repeated join patterns that deserve more concise expression.

By far the most common case for joins is following foreign keys. SQL has no special syntax for this:

```
select foo.id, quux.value 
from foo, bar, quux 
where foo.bar_id = bar.id and bar.quux_id = quux.id
```

Compare to eg [alloy](http://alloytools.org/tutorials/online/sidenote-relational-join.html), which has a dedicated syntax for this case:

```
foo.bar.quux
```

Or libraries like pandas or flink, where it's trivial to write a function that encapsulates this logic:

```
fk_join(foo, 'bar_id', bar, 'quux_id', quux)
```

Can we write such a function in sql? Most databases don't allow functions to take tables as arguments, and also require the column names and types of the input and output tables to be fixed when the function is defined. SQL:2016 introduced [polymorphic table functions](https://www.slideshare.net/ChrisSaxon1/polymorphic-table-functions-in-sql), which might allow writing something like `fk_join` but so far only oracle has implemented them (and they didn't follow the spec!).

Verbose syntax for such core operations has chilling effects downstream, such as developers avoiding [6NF](https://en.wikipedia.org/wiki/Sixth_normal_form) even in situations where it's useful, because all their queries would balloon in size.

### Fragile structure

There are many cases where a small change to a computation requires totally changing the structure of the query, but subqueries are my favourite because they're the most obvious way to express many queries and yet also provide so many cliffs to fall off.

```
-- for each manager, find their employee with the highest salary
> select
>   manager.name,
>   (select employee.name
>    from employee
>    where employee.manager = manager.name
>    order by employee.salary desc
>    limit 1)
> from manager;
 name  | name
-------+------
 alice | bob
(1 row)

-- what if we want to return the salary too?
> select
>   manager.name,
>   (select employee.name, employee.salary
>    from employee
>    where employee.manager = manager.name
>    order by employee.salary desc
>    limit 1)
> from manager;
ERROR:  subquery must return only one column
LINE 3:   (select employee.name, employee.salary
          ^

-- the only solution is to change half of the lines in the query
> select manager.name, employee.name, employee.salary
> from manager
> join lateral (
>   select employee.name, employee.salary
>   from employee
>   where employee.manager = manager.name
>   order by employee.salary desc
>   limit 1
> ) as employee
> on true;
 name  | name | salary
-------+------+--------
 alice | bob  |    100
(1 row)
```

This isn't terrible in such a simple example, but in analytics it's not uncommon to have to write queries that are hundreds of lines long and have many levels of nesting, at which point this kind of restructuring is laborious and error-prone.

Incompressible
--------------

Code can be [compressed](https://caseymuratori.com/blog_0015) by extracting similar structures from two or more sections. For example, if a calculation was used in several places we could assign it to a variable and then use the variable in those places. Or if the calculation depended on different inputs in each place, we could create a function and pass the different inputs as arguments.

This is programming 101 - variables, functions and expression substitution. How does SQL fare on this front?

### Variables

Scalar values can be assigned to variables, but only as a column inside a relation. You can't name a thing without including it in the result! Which means that if you want a temporary scalar variable you must introduce a new `select` to get rid off it. And also name all your other values.

```
-- repeated structure
select a+((z*2)-1), b+((z*2)-1) from foo;

-- compressed?
select a2, b2 from (select a+tmp as a2, b+tmp as b2, (z*2)-1 as tmp from foo);
```

You can use `as` to name scalar values anywhere they appear. Except in a `group by`.

```
-- can't name this value
> select x2 from foo group by x+1 as x2;
ERROR:  syntax error at or near "as"
LINE 1: select x2 from foo group by x+1 as x2;

-- sprinkle some more select on it
> select x2 from (select x+1 as x2 from foo) group by x2;
 ?column?
----------
(0 rows)
```

Rather than fix this bizarre oversight, the SQL spec allows a novel form of variable naming - you can refer to a column by using an expression which produces the same parse tree as the one that produced the column.

```
-- this magically works, even though x is not in scope in the select
> select (x + 1)*2 from foo group by x+1;
 ?column?
----------
(0 rows)

-- but this doesn't, because it isn't the same parse tree
> select (x + +1)*2 from foo group by x+1;
ERROR:  column "foo.x" must appear in the GROUP BY clause or be used in an aggregate function
LINE 1: select (x + +1)*2 from foo group by x+1;
                ^
```

Of course, you can't use this feature across any kind of syntactic boundary. If you wanted to, say, assign this table to a variable or pass it to a function, then you need to both repeat the expression and explicitly name it;

```
> with foo_plus as (select x+1 from foo group by x+1)
> select (x+1)*2 from foo_plus;
ERROR:  column "x" does not exist
LINE 2: select (x+1)*2 from foo_plus;
                ^
               
> with foo_plus as (select x+1 as x_plus from foo group by x+1)
> select x_plus*2 from foo_plus;
 ?column?
----------
(0 rows)
```

SQL was first used in the early 70s, but if your repeated value was a table then you were out of luck until CTEs were added in SQL:99.

```
-- repeated structure
select * 
from 
  (select x, x+1 as x2 from foo) as foo1 
left join 
  (select x, x+1 as x2 from foo) as foo2 
on 
  foo1.x2 = foo2.x;
  
-- compressed?
with foo_plus as 
  (select x, x+1 as x2 from foo)
select * 
from 
  foo_plus as foo1 
left join 
  foo_plus as foo2 
on 
  foo1.x2 = foo2.x;
```

### Functions

Similarly, if your repeated calculations have different inputs then you were out of luck until scalar functions were added in SQL:99.

```
-- repeated structure
select a+((x*2)-1), b+((y*2)-1) from foo;

-- compressed?
create function bar(integer, integer) returns integer
    as 'select $1+(($2*2)-1);'
    language sql;
select bar(a,x), bar(b,y) from foo;
```

Functions that return tables weren't added until SQL:2003.

```
-- repeated structure
(select x from foo)
union
(select x+1 from foo)
union
(select x+2 from foo)
union
(select x from bar)
union
(select x+1 from bar)
union
(select x+2 from bar);

-- compressed?
create function increments(integer) returns setof integer 
    as $$
        (select $1) 
        union 
        (select $1+1) 
        union 
        (select $1+2);
    $$
    language sql;
(select increments(x) from foo)
union
(select increments(x) from bar);
```

What if you want to compress a repeated calculation that produces more than one table as a result? Tough!

What if you want to compress a repeated calculation where one of the inputs is a table? The spec doesn't explicitly disallow this, but it isn't widely supported. SQL server can do it with this lovely syntax:

```
-- compressed?

create type foo_like as table (x int);

create function increments(@foo foo_like readonly) returns table
    as return
        (select x from @foo) 
        union 
        (select x+1 from @foo) 
        union 
        (select x+2 from @foo);
        
declare @foo as foo_like;
insert into @foo select * from foo;

declare @bar as foo_like;
insert into @bar select * from bar;

increments(@foo) union increments(@bar);
```

Aside from the weird insistence that we can't just pass a table directly to our function, this example points to a more general problem: column names are part of types. If in our example `bar` happened to have a different column name then we would have had to write:

```
increments(@foo) union increments(select y as x from @bar)
```

Since columns names aren't themselves first-class this makes it hard to compress repeated structure that happens to involve different names:

```
-- repeated structure
select a,b,c,x,y,z from foo order by a,b,c,x,y,z;

-- fantasy land
with ps as (columns 'a,b,c,x,y,z')
select $ps from foo order by $ps
```

The same is true of windows, collations, string encodings, the part argument to `extract` ... pretty much anything that involves one of the several hundred SQL keywords.

Functions and types are also not first-class, so repeated structures involving different functions or types can't be compressed.

### Expression substitution

To be able to compress repeated structure we must be able to replace the verbose version with the compressed version. In many languages, there is a principle that it's always possible to replace any expression with another expression that has the same value. SQL breaks this principle in (at least) two ways.

Firstly, it's only possible to substitute one expression for another when they are both the same type of expression. SQL has statements (DDL), table expressions and scalar expressions.

Using a scalar expression inside a table expression requires first wrapping the entire thing with a new `select`.

Using a table expression inside a scalar expression is generally not possible, unless the table expression returns only 1 column and either a) the table expression is guaranteed to return at most 1 row or b) your usage fits into one of the hard-coded patterns such as `exists`. Otherwise, as we saw in the most-highly-paid-employee example earlier, it must be rewritten as a lateral join against the nearest enclosing table expression.

Secondly, table expressions aren't all made equal. Some table expressions depend not only on the value of an inner expression, but the syntax. For example:

```
-- this is fine - the spec allows `order by` to see inside the `(select ...)`
-- and make use of a column `y` that doesn't exist in the returned value
> (select x from foo) order by y;
 x
---
 3
(1 row)

-- same value in the inner expression
-- but the spec doesn't have a syntactic exception for this case
> (select x from (select x from foo) as foo2) order by y;
ERROR:  column "y" does not exist
LINE 1: (select x from (select x from foo) as foo2) order by y;
```

In such cases it's not possible to compress repeated structure without first rewriting the query to explicitly select and then drop the magic column:

```
select x from ((select x,y from foo) order by y);
```

Non-porous
----------

I took the term 'porous' from [Some Were Meant For C](https://www.cl.cam.ac.uk/%7Esrk31/research/papers/kell17some-preprint.pdf), where Stephen Kell argues that the endurance of c is down to it's extreme openness to interaction with other systems via foreign memory, FFI, dynamic linking etc. He contrasts this with managed languages which don't allow touching anything in the entire memory space without first notifying the GC, have their own internal notions of namespaces and linking which they don't expose to the outside world, have closed build systems which are hard to interface with other languages' build systems etc.

For non-porous languages to succeed they have to eat the whole world - gaining enough users that the entire programming ecosystem can be duplicated within their walled garden. But porous languages can easily interact with existing systems and make use of existing libraries and tools.

Whether or not you like this argument as applied to c, the notion of porousness itself is a useful lens for system design. When we apply it to SQL databases, we see that individual databases are often porous in many aspects of their design but the mechanisms are almost always not portable. So while individual databases can be extended in many ways, the extensions can't be shared between databases easily and the SQL spec is still left trying to eat the whole world.

### Language level

Most SQL databases have language-level escape hatches for defining new types and functions via a mature programming language (usually c). The syntax for declaring these in SQL is defined in the spec but the c interface and calling convention is not, so these are not portable across different databases.

```
-- sql side

CREATE FUNCTION add_one(integer) RETURNS integer
     AS 'DIRECTORY/funcs', 'add_one'
     LANGUAGE C STRICT;
```

```
// c side

#include "postgres.h"
#include <string.h>
#include "fmgr.h"
#include "utils/geo_decls.h"

PG_MODULE_MAGIC;

PG_FUNCTION_INFO_V1(add_one);

Datum
add_one(PG_FUNCTION_ARGS)
{
    int32   arg = PG_GETARG_INT32(0);

    PG_RETURN_INT32(arg + 1);
}
```

### Runtime level

Many SQL databases also have runtime-level extension mechanisms for creating new index types and storage methods (eg [postgis](https://www.postgis.net/)) and also for supplying hints to the optimizer. Again, these extensions are not portable across different implementations. At this level it's hard to see how they could be, as they can be deeply entangled with design decisions in the database runtime, but it's worth noting that if they were portable then much of the SQL spec would not need to exist.

The SQL spec also has an extension [SQL/MED](https://en.wikipedia.org/wiki/SQL/MED) which defines how to query data that isn't owned by the database, but it isn't widely or portably implemented.

### Interface level

At the interface level, the status quo is much worse. Each database has a completely different interface protocol.

The protocols I'm familiar with are all ordered, synchronous and allow returning only one relation at a time. Many don't even support pipelining. For a long time SQL also lacked any way to return nested structures and even now (with json support) it's incredibly verbose.

This meant that if you wanted to return, say, a list of user profiles and their followers, you would have to make multiple round-trips to the database. Latency considerations make this unfeasible over longer distances. This practically mandates the existence of an application layer whose main purpose is to coalesce multiple database queries and reassemble their nested structure using hand-written joins over the output relations - duplicating work that the database is supposed to be good at.

Protocols also typically return metadata as text in an unspecified format with no parser supplied (even if there is a binary protocol for SQL values, metadata is still typically returned as a 1-row 1-column table containing a string). This makes it harder than necessary to build any kind of tooling outside of the database. Eg if we wanted to parse plans and verify that they don't contain any table scans or nested loops.

Similarly, SQL is submitted to the database as a text format identical to what the programmer would type. Since the syntax is so complicated, it's difficult for other languages to embed, validate and escape SQL queries and to figure out what types they return. (Query parameters are not a panacea for escaping - often you need to vary query structure depending on user input, not just values).

SQL databases are also typically monolithic. You can't, for example, just send a query plan directly to postgres. Or call the planner as a library to help make operational forecasts based on projected future workloads. Looking at the value unlocked by eg [pg\_query](https://pganalyze.com/blog/pg-query-2-0-postgres-query-parser) gives the sense that there could be a lot to gain by exposing more of the innards of SQL systems.

Complexity drag
---------------

In modern programming languages, the language itself consists of a small number of carefully chosen primitives. Programmers combine these to build up the rest of the functionality, which can be shared in the form of libraries. This lowers the burden on the language designers to foresee every possible need and allows new implementations to reuse existing functionality. Eg if you implement a new javascript interpreter, you get the whole javascript ecosystem for free.

Because SQL is so inexpressive, incompressible and non-porous it was never able to develop a library ecosystem. Instead, any new functionality that is regularly needed is added to the spec, often with it's own custom syntax. So if you develop a new SQL implementation you must also implement the entire ecosystem from scratch too because **users can't implement it themselves**.

This results in an enormous language.

The core SQL language is defined in part 2 (of 9) of the [SQL 2016 spec](https://blog.ansi.org/2018/10/sql-standard-iso-iec-9075-2016-ansi-x3-135/). Part 2 alone is 1732 pages. By way of comparison, the [javascript 2021 spec](https://www.ecma-international.org/wp-content/uploads/ECMA-262_12th_edition_june_2021.pdf) is 879 pages and the [c++ 2020 spec](https://www.iso.org/standard/79358.html) is 1853 pages.

But the SQL spec is [not even complete!](https://databasearchitects.blogspot.com/2015/02/type-inference-in-sql.html)

> A quick grep of the SQL standard indicates 411 occurrences of implementation-defined behavior. And not in some obscure corner cases, this includes basic language features. For a programming language that would be ridiculous. But for some reason people accept the fact that SQL is incredibly under-specified, and that it is impossible to write even relatively simple analytical queries in a way that is portable across database systems.

Notably, the spec does not define type inference at all, which means that the results of basic arithmetic are implementation-defined. Here is an example from the sqlite test suite in various databases:

```
sqlite> SELECT DISTINCT - + 34 + + - 26 + - 34 + - 34 + + COALESCE ( 93, COUNT ( * ) + + 44 - 16, - AVG ( + 86 ) + 12 ) / 86 * + 55 * + 46;
2402

postgres> SELECT DISTINCT - + 34 + + - 26 + - 34 + - 34 + + COALESCE ( 93, COUNT ( * ) + + 44 - 16, - AVG ( + 86 ) + 12 ) / 86 * + 55 * + 46;
       ?column?
-----------------------
 2607.9302325581395290
(1 row)

mariadb> SELECT DISTINCT - + 34 + + - 26 + - 34 + - 34 + + COALESCE ( 93, COUNT ( * ) + + 44 - 16, - AVG ( + 86 ) + 12 ) / 86 * + 55 * + 46;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '* ) + + 44 - 16, - AVG ( + 86 ) + 12 ) / 86 * + 55 * + 46' at line 1
```

The spec also declares that certain operations should produce errors when evaluated, but since it doesn't define an evaluation order the decision is left down to the optimizer. A query that runs fine in your database today might return an error tomorrow on the same data if the optimizer produces a different plan.

```
sqlite> select count(foo.bar/0) from (select 1 as bar) as foo where foo.bar = 0;
0

postgres> select count(foo.bar/0) from (select 1 as bar) as foo where foo.bar = 0;
ERROR:  division by zero

mariadb> select count(foo.bar/0) from (select 1 as bar) as foo where foo.bar = 0;
+------------------+
| count(foo.bar/0) |
+------------------+
|                0 |
+------------------+
1 row in set (0.001 sec)
```

And despite being enormous and not even definining the whole language, the spec still manages to define a language so anemic that every database ends up with a raft of [non-standard](https://www.postgresql.org/docs/9.4/plpgsql.html) [extensions](https://en.wikipedia.org/wiki/Transact-SQL) to compensate.

Even if all the flaws I listed in the previous sections were to be fixed in the future, SQL already ate a monstrous amount of complexity in workarounds for those flaws and that complexity will never be removed from the spec. This complexity has a huge impact on the effort required to implement a new SQL engine.

To take an example close to my heart: [Differential dataflow](https://github.com/TimelyDataflow/differential-dataflow/) is a dataflow engine that includes support for automatic parallel execution, horizontal scaling and incrementally maintained views. It totals [~16kloc](https://gist.github.com/jamii/55830e5660d0feb9bb2088435e5cac61) and was mostly written by a single person. [Materialize](https://github.com/MaterializeInc/materialize/) adds support for SQL and various data sources. To date, that has taken [~128kloc](https://gist.github.com/jamii/c775e371521b516402bfc2ad44c72668) (not including dependencies) and I estimate ~15-20 engineer-years. Just converting SQL to the logical plan takes [~27kloc](https://gist.github.com/jamii/64e86e63d0e6440d4be010d84b7748bd), more than than the entirety of differential dataflow.

Similarly, [sqlite](https://www.sqlite.org/index.html) looks to have [~212kloc](https://gist.github.com/jamii/c5bb19156b92966990dfa9ca85cc1c7e) and [duckdb](https://github.com/duckdb/duckdb) [~141kloc](https://gist.github.com/jamii/e36c8b6d0cb4a9606137fddd6d9d17d6). The count for duckdb doesn't even include the parser that they (sensibly) borrowed from postgres, which at [~47kloc](https://gist.github.com/jamii/fb97183731cf0b3a0ac019db9b1ec3af) is much larger than the entire [~30kloc](https://gist.github.com/jamii/9dfcecce9fb6dd0aae5f45739421c6b9) codebase for lua.

Materialize passes [more than 7 million tests](https://gist.github.com/jamii/b362cbf9823f76e59090a06b5520b194), including the entire sqlite logic test suite and much of the cockroachdb logic test suite. And yet they are [still discovering (my) bugs](https://web.archive.org/web/20240822170747/https://github.com/MaterializeInc/materialize/issues/6875) in such core components as name resolution, which in any sane language would be trivial.

The entire database industry is hauling a massive SQL-shaped parachute behind them. This complexity creates a drag on everything downstream.

### Quality of implementation suffers

There is so much ground to cover that it's not possible to do a good job of all of it. Subqueries, for example, add some much-needed expressiveness to SQL but their use is usually not recommended because [most databases optimize them poorly or not at all](https://www.scattered-thoughts.net/writing/materialize-decorrelation#existing-approaches).

This affects UX too. Every SQL database I've used has terrible syntax errors.

```
sqlite> with q17_part as (
   ...>   select p_partkey from part where
   ...>   p_brand = 'Brand#23'
   ...>   and p_container = 'MED BOX'
   ...> ),
   ...> q17_avg as (
   ...>   select l_partkey as t_partkey, 0.2 * avg(l_quantity) as t_avg_quantity
   ...>   from lineitem
   ...>   where l_partkey IN (select p_partkey from q17_part)
   ...>   group by l_partkey
   ...> ),
   ...> q17_price as (
   ...>   select
   ...>   l_quantity,
   ...>   l_partkey,
   ...>   l_extendedprice
   ...>   from
   ...>   lineitem
   ...>   where
   ...>   l_partkey IN (select p_partkeyfrom q17_part)
   ...> ),
   ...> select cast(sum(l_extendedprice) / 7.0 as decimal(32,2)) as avg_yearly
   ...> from q17_avg, q17_price
   ...> where
   ...> t_partkey = l_partkey and l_quantity < t_avg_quantity;   
Error: near "select": syntax error
```

But it's hard to produce good errors when your grammar contains 1732 non-terminals. And several hundred keywords. And allows using (some) keywords as identifiers. And contains many many ambiguities which mean that typos are often valid but nonsensical SQL.

### Innovation at the implementation level is gated

[Incremental maintenance](https://dl.acm.org/doi/pdf/10.1145/2983551), [parallel execution](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1090.7126&rep=rep1&type=pdf), [provenance](https://homepages.inf.ed.ac.uk/jcheney/publications/provdbsurvey.pdf), [equivalence checking](https://cidrdb.org/cidr2017/papers/p51-chu-cidr17.pdf), [query synthesis](https://dl.acm.org/doi/pdf/10.1145/3035918.3058738) etc. These show up in academic papers, produce demos for simplified subsets of SQL, and then disappear.

In the programming language world we have a smooth pipeline that takes basic research and applies it to increasingly realistic languages, eventually producing widely-used industrial-quality tools. But in the database world there is a missing step between demos on toy relational algebras and handling the enormity of SQL, down which most compelling research quietly plummets. Bringing anything novel to a usable level requires a substantial investment of time and money that most researchers simply don't have.

### Portability is a myth

The spec is too large and too incomplete, and the incentives to follow the spec too weak. For example, the latest postgres docs [note](https://www.postgresql.org/docs/current/features.html) that "at the time of writing, no current version of any database management system claims full conformance to Core SQL:2016". It also lists a few dozen [departures from the spec](https://wiki.postgresql.org/wiki/PostgreSQL_vs_SQL_Standard).

This is exacerbated by the fact that every database also has to invent myriad non-standard extensions to cover the weaknesses of standard SQL.

Where the average javascript program can be expected to work in any interpreter, and the average c program might need to macro-fy some compiler builtins, the average body of SQL queries will need serious editing to run on a different database and even then can't be expected to produce the same answers.

One of the big selling points for supporting SQL in a new database is that existing tools that emit SQL will be able to run unmodified. But in practice, such tools almost always end up maintaining [separate backends](https://github.com/sqlalchemy/sqlalchemy/tree/master/lib/sqlalchemy/dialects) for every dialect, so unless you match an existing database bug-for-bug you'll still have to add a new backend to every tool.

Similarly, users will be able to carry across some SQL knowledge, but will be regularly surprised by inconsistencies in syntax, semantics and the set of available types and functions. And unlike the programming language world they won't be able to carry across any existing code or libraries.

This means that the network effects of SQL are much weaker than they are for programming languages, which makes it all the more surprising that we have a bounty of programming languages but only one relational database language.

The application layer
---------------------

The original idea of relational databases was that they would be queried directly from the client. With the rise of the web this idea died - SQL is too complex to be easily secured against adversarial input, cache invalidation for SQL queries is too hard, and there is no way to easily spawn background tasks (eg resizing images) or to communicate with the rest of the world (eg sending email). And the SQL language itself was not an appealing target for adding these capabilities.

So instead we added the 'application layer' - a process written in a reasonable programming language that would live between the database and the client and manage their communication. And we invented [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) to patch over the weaknesses of SQL, especially the lack of compressibility.

This move was necessary, but costly.

ORMs are prone to [n+1 query bugs](https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/) and [feral concurrency](https://hashingit.com/elements/research-resources/2015-06-03-feral-concurrency.pdf). To rephrase, they are bad at efficiently querying data and bad at making use of transactions - two of the core features of relational databases.

As for the application layer: Converting queries into rest endpoints by hand is a lot of error-prone boilerplate work. Managing cache invalidation by hand leads to a steady supply of bugs. If endpoints are too fine-grained then clients have to make multiple roundtrip calls, but if they're too coarse then clients waste bandwidth on data they didn't need. And there is no hope of automatically notifying clients when the result of their query has changed.

The success of [GraphQL](https://graphql.org/) shows that these pains are real and that people really do want to issue rich queries directly from the client. Compared to SQL, GraphQL is substantially easier to implement, easier to cache, has a much smaller attack surface, has various mechanisms for compressing common patterns, makes it easy to follow foreign keys and return nested results, has first-class mechanisms for interacting with foreign code and with the outside world, has a rich type system (with union types!), and is easy to embed in other languages.

Similarly for [firebase](https://web.archive.org/web/20140625064551/https://www.firebase.com/) (before it was acqui-smothered by google). It dropped the entire application layer and offered streaming updates to client-side queries, built-in access control, client-side caching etc. Despite offering very little in the way of runtime innovation compared to existing databases, it was able to succesfully compete by recognizing that the current division of database + sql + orm + application-layer is a historical accident and can be dramatically simplified.

The overall vibe of the NoSQL years was "relations bad, objects good". I fear that what many researchers and developers are taking away from the success of GraphQL and co is but a minor update - "relations bad, ~objects~ graphs good".

This is a mistake. GraphQL is still more or less a relational model, as evidenced by the fact that it's typically backed by wrappers like [hasura](https://hasura.io/) that allow taking advantage of the mature runtimes of relational databases. The key to the success of GraphQL was not doing away with relations, but recognizing and fixing the real flaws in SQL that were hobbling relational databases, as well as unbundling the query language from a single monolithic storage and execution engine.

After SQL?
----------

To summarize:

*   Design flaws in the SQL language resulted in a language with no library ecosystem and a burdensome spec which limits innovation.
*   Additional design flaws in SQL database interfaces resulted in moving as much logic as possible to the application layer and limiting the use of the most valuable features of the database.
*   It's probably too late to fix either of these.

But the idea of modelling data with a declarative [disorderly](https://www.youtube.com/watch?v=R2Aa4PivG0g) language is still valuable. Maybe more so than ever, given the trends in hardware. What should a new language learn from SQL's successes and mistakes?

We can get pretty far by just negating every mistake listed in this post, while ensuring we retain the ability to produce and optimize query plans:

*   Start with the structure that all modern languages have converged towards.
    *   Everything is an expression.
    *   Variables and functions have compact syntax.
    *   Few keywords - most things are stdlib functions rather than builtin syntax.
    *   Have an explicit type system rather than totally disjoint syntax for scalar expressions vs table expressions.
    *   Ensure that it's always possible to replace a given expression with another expression that has the same type and value.
    *   Define a (non-implementation specific) system for distributing and loading (and unloading!) libraries.
*   Keep the spec simple and complete.
    *   Simple denotational semantics for the core language.
    *   Completely specify type inference, error semantics etc.
    *   Should be possible for an experienced engineer to throw together a slow but correct interpreter in a week or two.
    *   Encode semantics in a model checker or theorem prover to eg test optimizations. Ship this with the spec.
    *   Lean on wasm as an extension language - avoids having to spec arithemetic, strings etc if they can be defined as a library over some bits type.
*   Make it compressible.
    *   Allow functions to take relations and other functions are arguments (can be erased by specialization before planning, ala rust or julia).
    *   Allow functions to operate on relations polymorphically (ie without having to fix the columns and types when writing the function).
    *   Make column names, orderings, collations, window specifications etc first-class values rather than just syntax (can use staging ala [zig's comptime](https://kristoff.it/blog/what-is-zig-comptime/) if these need to be constant at planning time).
    *   Compact syntax for simple joins (eg snowflake schemas, graph traversal).
    *   True recursion / fixpoints (allows expressing iterative algorithms like parsing).
*   Make it porous.
    *   Allow defining new types, functions, indexes, plan operators etc via wasm plugins (with the calling convention etc in the spec).
    *   Expose plans, hints etc via api (not via strings).
    *   Spec both a human-friendly encoding and a tooling-friendly encoding (probably text vs binary [like wasm](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format)). Ship an embedabble library that does parsing and type inference.
    *   Make returning nested structures (eg json) ergonomic, or at least allow returning multiple relations.
    *   Create a subset of the language that can be easily verified to run in reasonable time (eg no table scans, no nested loops).
    *   Allow exposing subset to clients via [graphql-like authorization rules](https://graphql.org/learn/authorization/).
*   Better layering.
    *   Separate as much as possible out into embeddable libraries (ala pg\_query).
    *   Expose storage, transaction, execution as apis. The database server just receives and executes wasm against these apis.
    *   Distribute query parser/planner/compiler as a library so clients can choose to use modified versions to produce wasm for the server.

Strategies for actually getting people to use the thing are much harder.

Tackling the entire stack at once seems challenging. [Rethinkdb died](https://www.defmacro.org/2017/01/18/why-rethinkdb-failed.html). [Datomic](https://www.datomic.com/) is alive but the company was [acquihired](https://www.cognitect.com/blog/2020/07/23/Cognitect-Joins-Nubank). [Neo4j](https://neo4j.com/), on the other hand, seems to be [catnip for investors](https://neo4j.com/press-releases/neo4j-announces-seriesf-funding/), so who knows.

A safer approach is to first piggy-back on existing databases runtime. [EdgeDB](https://www.edgedb.com/) uses the postgres runtime. [Logica](https://github.com/EvgSkv/logica) compiles to SQL. GraphQL has compilers for many different query languages.

Another option is to find an untapped niche and work outward from there. I haven't seen this done yet, but there are a lot of relational-ish query niches. [Pandas](https://pandas.pydata.org/) targets data cleaning/analysis. [Datascript](https://github.com/tonsky/datascript) is a front-end database. [Bloom](http://bloom-lang.net/) targets distributed systems algorithms. [Semmle](https://semmle.com/) targets code analysis. Other potential niches include embedded databases in applications (ala [fossils use of sqlite](https://www.fossil-scm.org/home/doc/trunk/www/theory1.wiki)), [incremental functions from state to UI](https://www.scattered-thoughts.net/writing/relational-ui/), [querying as an interface to the state of complex programs](https://petevilter.me/post/datalog-typechecking/) etc.

In a niche with less competition you could first grow the language and then try to expand the runtime outwards to cover more potential usecases, similar to how sqlite started as a [tcl extension](https://en.wikipedia.org/wiki/SQLite#History) and ended up becoming the defacto standard for application-embedded databases, a common choice for data publishing format, and a backend for a variety of data-processing tools.

FAQ
---

**Why do you want json in your database?** I'm personally not that interested in storing json in tables (although I hear that it's useful for modelling sparse data). But many usecases require returning disparate data that does not fit into a single relation (eg a monitoring dashboard or the logged-in landing page of many websites). If you can't return all this data from a single query, you need an entire extra process co-located with the database whose job it is to coalesce multiple synchronous queries and then join the results together into some structured form to send to the client. This results in duplication of work in the database, hides some of the query structure from the query planner, opens up the potential for n+1 bugs, adds the possibility of partial failure etc. It's a lot of extra complexity that can be avoided if your database can just return all the data in one query (eg see [how Hasura translates GraphQL to SQL](https://hasura.io/blog/building-a-graphql-to-sql-compiler-on-postgres-ms-sql-and-mysql/)). This is why people are excited about databases providing GraphQL support.

**That code belongs in the application layer. Use the right tool for the job!** If your database query language is not the right tool for querying data, that seems like a problem.

**SQL is the only relational language that has even been successful. It's just the natural way of expressing relational queries.** [LINQ](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/basic-linq-query-operations), [spark](https://spark.apache.org/), [flink](https://flink.apache.org/), [kafka streams](https://kafka.apache.org/documentation/streams/), [pandas](https://pandas.pydata.org/docs/), [dataframes](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/data.frame) are all widely used examples of an expression-based language-embedded approach to relational queries. [Logica](https://opensource.googleblog.com/2021/04/logica-organizing-your-data-queries.html), [logiql](https://developer.logicblox.com/technology/), [differential datalog](https://github.com/vmware/differential-datalog), [semmle](https://semmle.com/case-studies/semmle-nasa-landing-curiosity-safely-mars), [datomic](https://www.datomic.com/) are all examples of commercially-deployed datalog-based relational query languages.

**But SQL enables transactions, logical data independence, plan optimization etc.** The relational data model enables those things. None of them require the language to be SQL. Eg logicblox and datomic manage to have transactions, transparent indexes, query planners etc while still having much simpler and more orthogonal query languages than SQL.

**Javascript is crazy too!** Javascript has improved dramatically over the last decade or two, to the point that compatibility between different vendors is almost complete. But imagine a javascript without libraries, without polyfills, where functions couldn't take collections as arguments and where `for` loops had a different syntax in each engine. I would, for the record, totally endorse a SQL STRICT MODE which discarded all the silly edge cases and produced a simpler, more orthogonal language. But the database vendors have no incentive to do this - SQL is their moat.

**SQL has been around for more than 50 years.** So has COBOL. Thousands of engineer-years have been invested in the COBOL ecosystem. But it sure seems that noticing COBOL's flaws and designing better successors paid off in the long run. It turns out that we learned a lot about language design in the last 50 years.

**Complaining is easy. Where's your solution?** Perhaps the first step in trying to replace something would be to carefully analyze and discuss the strengths and weaknesses of that thing. Those who don't [study history](https://dsf.berkeley.edu/cs286/papers/goesaround-redbook2005.pdf)...

**You just need to learn how SQL works.** [Bruh.](https://github.com/MaterializeInc/materialize/graphs/contributors)

I'd like to finish with this [quote](http://www.redbook.io/ch2-importantdbms.html) from [Michael Stonebraker](https://en.wikipedia.org/wiki/Michael_Stonebraker), one of the most prominent figures in the history of relational databases:

> My biggest complaint about System R is that the team never stopped to clean up SQL... All the annoying features of the language have endured to this day. SQL will be the COBOL of 2020...
