Title: SQL/JSON is here! (kinda “Waiting for Pg 17”) – select * from depesz;

URL Source: https://www.depesz.com/2024/10/11/sql-json-is-here-kinda-waiting-for-pg-17/

Markdown Content:
Amazing. Awesome. Well, but what is it? We could store json data in Pg since [PostgreSQL 9.2](https://www.depesz.com/2012/02/12/waiting-for-9-2-json/) – so it's been there for over 12 years now. How is the new shiny thing different? What does it allow you to do?

Let's see if I can shed some light on it…

For starters: SQL/JSON is a standard. As in: written down by people not bound by “only for PostgreSQL" rules. This means that whatever is here will (eventually? hopefully?) work in other databases, once they will implement it.

We actually had parts of it in PostgreSQL for some time. JSON datatype, JSON PATH expressions. But now, we get _MORE_.

Up to this moment, we (generally speaking) had _json_ and _jsonb_ datatypes, some [functions and operators](https://www.postgresql.org/docs/16/functions-json.html) (including the ones that used JSONPATH datatype). This all doesn't go away. But we get more stuff. Some of it is kinda redundant to what we could have done previously, but it is there now, in this new way, because it is part of the standard. Some of it wasn't possible earlier or, at the very least, wasn't simple earlier.

To do any kind of work on json, we need to, well, have any json value. This means we need some constructors.

Of course, we could have done it previously, using things like:

\=$ SELECT '"test"'::json;

but SQL/JSON has a bunch of its own constructors. Let's see how to use them.

Constructors
------------

The simplest possible things. Takes something that kinda makes like a json, and returns json. Example usage:

\=$ SELECT JSON(123::text);
 json 
\------
 123
(1 ROW)
 
\=$ SELECT JSON( '"depesz"' );
   json   
\----------
 "depesz"
(1 ROW)

Basically simple _::json_ cast. Will work only if input is text, bytea, json, or jsonb datatype. Otherwise, you will get an error:

\=$ SELECT JSON( 123 );
ERROR:  cannot CAST TYPE INTEGER TO json
LINE 1: SELECT JSON( 123 );
                     ^

There is one bit of functionality. You can make the JSON() call validate that your object doesn't have duplicate keys.

Consider JSON value of _{“a": 123, “a": 256}_. Depending on how you'd cast it (to json, or jsonb) you get different things:

\=$ SELECT '{"a": 123, "a": 256}'::json;
         json         
\----------------------
 {"a": 123, "a": 256}
(1 ROW)
 
\=$ SELECT '{"a": 123, "a": 256}'::jsonb;
   jsonb    
\------------
 {"a": 256}
(1 ROW)

Plain JSON() call on this value will produce same output as cast to JSON:

\=$ SELECT JSON( '{"a": 123, "a": 256}' );
         json         
\----------------------
 {"a": 123, "a": 256}
(1 ROW)

but I can make it reject such (invalid?) objects, instead of silently modifying:

\=$ SELECT JSON( '{"a": 123, "a": 256}' WITH UNIQUE KEYS );
ERROR:  duplicate JSON object KEY VALUE

JSON\_SCALAR
------------

Function that generates properly quoted JSON scalar value. For some values – numbers, and boolean values, it will be something unquoted, but for everything else, you will get quotes:

\=$ SELECT
    JSON\_SCALAR(1),
    JSON\_SCALAR(\-12.34),
    JSON\_SCALAR(TRUE),
    JSON\_SCALAR('depesz'),
    JSON\_SCALAR(now()),
    JSON\_SCALAR(NULL)\\gx
\-\[ RECORD 1 \]\-----------------------------------
json\_scalar | 1
json\_scalar | \-12.34
json\_scalar | TRUE
json\_scalar | "depesz"
json\_scalar | "2024-10-11T14:11:44.636294+02:00"
json\_scalar | ␀

Please note that the last value is SQL null. So it's not JSON value of null

JSON\_SERIALIZE
---------------

This, to be honest, isn't really clear to me what it's for.

Docs say:

> Converts an SQL/JSON expression into a character or binary string. The expression can be of any JSON type, any character string type, or bytea in UTF8 encoding. The returned type used in RETURNING can be any character string type or bytea. The default is text.

While I kinda understand what it says, and I understand that I can use it, for some reason, to generate BYTEA, I don't really understand the functionality.

Just for completeness:

\=$ SELECT
    JSON\_SERIALIZE( JSON\_SCALAR( now() ) ),
    JSON\_SERIALIZE( JSON\_SCALAR( now() ) RETURNING BYTEA ) \\gx
\-\[ RECORD 1 \]\--+-----------------------------------------------------------------------
json\_serialize | "2024-10-11T14:18:24.670959+02:00"
json\_serialize | \\x22323032342d31302d31315431343a31383a32342e3637303935392b30323a303022

It might be worth noting that while JSON\_SCALAR (and other constructors) return JSON datatype, JSON\_SERIALIZE produces text (or bytea):

\=$ SELECT
    JSON\_SCALAR( now() ),
    JSON\_SERIALIZE( JSON\_SCALAR( now() ) ),
    JSON\_SERIALIZE( JSON\_SCALAR( now() ) RETURNING BYTEA ) \\gdesc
     COLUMN     | TYPE  
\----------------+-------
 json\_scalar    | json
 json\_serialize | text
 json\_serialize | bytea
(3 ROWS)

JSON\_ARRAY
-----------

This thing has two modes of operations. In first it gets list of values:

\=$ select json\_array( ‘depesz', true, now() );  
json\_array  
——————————————————  
\[“depesz", true, “2024-10-11T14:21:18.997901+02:00"\]  
(1 row)

In second, it takes a query:

\=$ SELECT json\_array( SELECT datname FROM pg\_database ORDER BY datname );
                                             json\_array                                             
\----------------------------------------------------------------------------------------------------
 \["coll", "depesz", "depesz\_explain", "pgdba", "postgres", "q", "template0", "template1", "x", "z"\]
(1 ROW)

In the mode where you give it list of values, you can specify what to do with null values:

\=$ SELECT json\_array( 'depesz', NULL, 'test' );
     json\_array     
\--------------------
 \["depesz", "test"\]
(1 ROW)
 
\=$ SELECT json\_array( 'depesz', NULL, 'test' ABSENT ON NULL );
     json\_array     
\--------------------
 \["depesz", "test"\]
(1 ROW)
 
\=$ SELECT json\_array( 'depesz', NULL, 'test' NULL ON NULL );
        json\_array        
\--------------------------
 \["depesz", NULL, "test"\]
(1 ROW)

In case of query based form, it always uses ‘ABSENT ON NULL', and it can't be changed.

Assitionally, you can set returning datatpoe, just like with JSON\_SERIALIZE(), and it works in both modes:

\=$ SELECT
    json\_array( 1, 2, 3 ),
    json\_array( 1, 2, 3 returning jsonb ),
    json\_array( SELECT datname FROM pg\_database ORDER BY datname ),
    json\_array( SELECT datname FROM pg\_database ORDER BY datname returning jsonb ) \\gdesc
   COLUMN   | TYPE  
\------------+-------
 json\_array | json
 json\_array | jsonb
 json\_array | json
 json\_array | jsonb
(4 ROWS)

JSON\_ARRAYAGG
--------------

Basically aggregate function that produces json values. Usage is pretty simple:

\=$ SELECT JSON\_ARRAYAGG( datname ORDER BY LENGTH(datname) DESC, datname ) FROM pg\_database;
                                           json\_arrayagg                                            
\----------------------------------------------------------------------------------------------------
 \["depesz\_explain", "template0", "template1", "postgres", "depesz", "pgdba", "coll", "q", "x", "z"\]
(1 ROW)

Just like [any aggregate](https://www.depesz.com/2010/01/06/waiting-for-8-5-ordered-aggregates/) you can add _ORDER BY_ clause, but because it's JSON thing you also get _NULL/ABSENT ON NULL_ and _RETURNING jsonb?_ modifiers:

\=$ WITH src AS ( SELECT unnest(array\['a', NULL, 'c' \]) AS f )
    SELECT
        json\_arrayagg(f),
        pg\_typeof( json\_arrayagg(f) ),
        json\_arrayagg(f NULL ON NULL),
        pg\_typeof( json\_arrayagg(f NULL ON NULL) ),
        json\_arrayagg(f NULL ON NULL returning jsonb),
        pg\_typeof( json\_arrayagg(f NULL ON NULL returning jsonb) )
        FROM src \\gx
\-\[ RECORD 1 \]\-+\-----------------
json\_arrayagg | \["a", "c"\]
pg\_typeof     | json
json\_arrayagg | \["a", NULL, "c"\]
pg\_typeof     | json
json\_arrayagg | \["a", NULL, "c"\]
pg\_typeof     | jsonb

JSON\_OBJECT
------------

This is going to be fun. We already had json\_object() functions, one operating on array of texts, and the other getting two arrays – for keys, and for values.

This new json\_object kinda looks like function call, but is a different thing. So, explaining differences on [IRC](irc://irc.libera.chat/postgresql)/[Slack](https://pgtreats.info/slack-invite)/[Discord](https://discord.gg/bW2hsax8We) will be fun /s.

Anyway. Basic usage looks like this:

\=$ SELECT json\_object(
    'a' VALUE 123,
    'b': TRUE,
    'c' VALUE now(),
    'd': json\_array( 1, 2, 'YEAH' )
);
                                       json\_object                                       
\-----------------------------------------------------------------------------------------
 {"a" : 123, "b" : TRUE, "c" : "2024-10-11T14:42:34.894498+02:00", "d" : \[1, 2, "YEAH"\]}
(1 ROW)

Depending on how you feel you can separate keys from values using keyword _value_, or by using colon _:_. Both work.

Just like in previous constructors, we can use _NULL ON NULL_ or _ABSENT ON NULL_ clauses (null matching works for values, not keys, NULL keys are invalid in any case).

Also, as usual, we have _RETURNING_ clause that allows us to return JSONB.

Just like with JSON(), we can use _WITH UNIQUE KEYS_ which will error out if any key is duplicated.

JSON\_OBJECTAGG
---------------

Similarly to JSON\_ARRAYAGG, it is basically an aggregate:

\=$ SELECT JSON\_OBJECTAGG( datname VALUE oid RETURNING JSONB ) FROM pg\_database;
                                                                                     json\_objectagg                                                                                     
\----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {"q": "530457", "x": "530456", "z": "530455", "coll": "529419", "pgdba": "530454", "depesz": "529711", "postgres": "5", "template0": "4", "template1": "1", "depesz\_explain": "16414"}
(1 ROW)

Of course we can use _NULL ON NULL_ or _ABSENT ON NULL_, and _WITH/WITHOUT UNIQUE KEYS_ specifiers.

Which is actually interesting – what will happen if I have the same key MANY times, but generate _with unique keys_ and use json/jsonb returning types?

\=$ WITH s(k,v) AS ( VALUES ('a', 1), ('a', 2), ('b', 3 ) )
SELECT
    JSON\_OBJECTAGG( k VALUE v returning json ),
    JSON\_OBJECTAGG( k VALUE v returning jsonb )
FROM s;
        json\_objectagg         |  json\_objectagg  
\-------------------------------+------------------
 { "a" : 1, "a" : 2, "b" : 3 } | {"a": 2, "b": 3}
(1 ROW)

Sweet. And now for…

Testing functions
-----------------

This is a family of expressions in format of:

_IS (NOT)? JSON \_TYPE\__

where _\_TYPE\__ is one of: _VALUE_, _SCALAR_, _ARRAY_, _OBJECT_.

And additionally, you can add _WITH/WITHOUT UNIQUE KEYS_ at the end.

In all of the cases we get boolean value that tells us if given thing is proper json thing.

Specifying _WITH UNIQUE KEYS_ will check the whole thing, not only the top-most level.

Couple of examples:

\=$ SELECT
    'depesz' IS JSON VALUE AS depesz,
    NULL IS JSON VALUE AS NULL,
    JSON\_SCALAR( now() ) IS JSON SCALAR AS null\_scalar,
    JSON\_SCALAR( now() ) IS JSON ARRAY AS null\_array,
    JSON\_SCALAR( now() ) IS JSON OBJECT AS null\_object,
    JSON\_ARRAY( 1,2,3 ) IS JSON ARRAY AS array\_array,
    JSON\_ARRAY( 1,2,3 ) IS JSON OBJECT AS array\_object,
    JSON\_OBJECT( 'k': 'v' ) IS JSON ARRAY AS object\_array,
    JSON\_OBJECT( 'k': 'v' ) IS JSON OBJECT AS object\_object,
    JSON\_ARRAY( 1, 2, json\_object( 'k': 1, 'k': 2 ) ) IS JSON ARRAY AS non\_unique\_array,
    JSON\_ARRAY( 1, 2, json\_object( 'k': 1, 'k': 2 ) ) IS JSON ARRAY WITH UNIQUE KEYS AS non\_unique\_array\_with\_unique
\\gx
\-\[ RECORD 1 \]\----------------+--
depesz                       | f
NULL                         | 
null\_scalar                  | t
null\_array                   | f
null\_object                  | f
array\_array                  | t
array\_object                 | f
object\_array                 | f
object\_object                | t
non\_unique\_array             | t
non\_unique\_array\_with\_unique | f

Query functions
---------------

These are so interesting/complicated that they got their own [section in manual](https://www.postgresql.org/docs/current/functions-json.html#SQLJSON-QUERY-FUNCTIONS). Let's see if I can explain them. A bit.

Before we can dig into them, one should know, and understand, at least to some extens, so called [SQL/JSON PATH EXPRESSIONS](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-PATH).

These were available for [quote some time now](https://www.depesz.com/2019/03/19/waiting-for-postgresql-12-partial-implementation-of-sql-json-path-language/), and could have been used in all functions named jsonb\_path\_SOMETHING that you can find in [the docs](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSON-PROCESSING-TABLE).

If you're not familiar with those – please read the _waiting_ blogpost linked above, and/or the docs, or just play a bit with it.

JSON\_EXISTS
------------

So this is basic testing if given path expression exists in JSON. Basically like _jsonb\_path\_exists()_ function.

So, let's see it:

\=$ SELECT
    JSON\_EXISTS( j, '$.k' ),
    JSON\_EXISTS( j, '$.f' ),
    JSON\_EXISTS( j, '$.a\[5\]' )
FROM
    ( VALUES ( json\_object( 'k': 'v', 'a': json\_array( 1, 2, 5 ) ) ) ) AS s (j);
 json\_exists | json\_exists | json\_exists 
\-------------+-------------+-------------
 t           | f           | f
(1 ROW)

Please note that in third example, I checked existence of 5th index of .a array. This worked because, by default, it's using “lax" processing. I could:

\=$ SELECT
    JSON\_EXISTS( j, 'strict $.a\[5\]' ERROR ON ERROR )
FROM
    ( VALUES ( json\_object( 'k': 'v', 'a': json\_array( 1, 2, 5 ) ) ) ) AS s (j);
ERROR:  jsonpath array subscript IS OUT OF bounds

This allows (strict processing) to set some other handlers for errors:

\=$ SELECT
    JSON\_EXISTS( j, 'strict $.a\[5\]' TRUE ON ERROR ),
    JSON\_EXISTS( j, 'strict $.a\[5\]' FALSE ON ERROR ),
    JSON\_EXISTS( j, 'strict $.a\[5\]' UNKNOWN ON ERROR ),
    JSON\_EXISTS( j, 'lax $.a\[5\]' TRUE ON ERROR ),
    JSON\_EXISTS( j, 'lax $.a\[5\]' FALSE ON ERROR ),
    JSON\_EXISTS( j, 'lax $.a\[5\]' UNKNOWN ON ERROR )
FROM
    ( VALUES ( json\_object( 'k': 'v', 'a': json\_array( 1, 2, 5 ) ) ) ) AS s (j);
 json\_exists | json\_exists | json\_exists | json\_exists | json\_exists | json\_exists 
\-------------+-------------+-------------+-------------+-------------+-------------
 t           | f           |             | f           | f           | f
(1 ROW)

Please note that in lax mode, the _\* ON ERROR_ clause doesn't do anything.

And of course, you can pass variables to path expressions, like this:

\=$ SELECT
    JSON\_EXISTS( j, '$.a\[\*\] ? ( @ \>\= $good )' PASSING 5 AS good ),
    JSON\_EXISTS( j, '$.a\[\*\] ? ( @ \>\= $good )' PASSING 10 AS good )
FROM
    ( VALUES ( json\_object( 'k': 'v', 'a': json\_array( 1, 2, 5 ) ) ) ) AS s (j);
 json\_exists | json\_exists 
\-------------+-------------
 t           | f
(1 ROW)

JSON\_QUERY
-----------

Now, we're entering more complicated features.

To give you some perspective, syntax definition for json\_query looks like:

JSON\_QUERY (
context\_item, path\_expression
\[ PASSING { VALUE AS varname } \[, ...\]\]
\[ RETURNING data\_type \[ FORMAT JSON \[ ENCODING UTF8 \] \] \]
\[ { WITHOUT | WITH { CONDITIONAL | \[UNCONDITIONAL\] } } \[ ARRAY \] WRAPPER \]
\[ { KEEP | OMIT } QUOTES \[ ON SCALAR STRING \] \]
\[ { ERROR | NULL | EMPTY { \[ ARRAY \] | OBJECT } | DEFAULT expression } ON EMPTY \]
\[ { ERROR | NULL | EMPTY { \[ ARRAY \] | OBJECT } | DEFAULT expression } ON ERROR \]) → jsonb

So. What it does. It takes jsonpath (second argument), and applies it on given data (first argument). And then it returns whatever the path returned.

Simple to explain, but there are some intersting details.

Let's start with something simple to see if I can show all the things I'd like to show.

Since getting all the data to each query will be rather tedious, let's make simple table with one column, and one row, that will contain test json:

\=$ CREATE TABLE t (j jsonb);
\=$ INSERT INTO t (j) VALUES ('{"k": "v", "a": \[ 1,2,5,15\], "n": { "s": "x", "b": \[ 5, 10, 15 \] } }' );
\=$ SELECT jsonb\_pretty(j) FROM t;
   jsonb\_pretty   
\------------------
 {               +
     "a": \[      +
         1,      +
         2,      +
         5,      +
         15      +
     \],          +
     "k": "v",   +
     "n": {      +
         "b": \[  +
             5,  +
             10, +
             15  +
         \],      +
         "s": "x"+
     }           +
 }
(1 ROW)

With this in place, we can try to get some json\_queries.

\=$ WITH d AS (
    SELECT json\_query( j, '$.k' ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof |  r  
\-----------+-----
 jsonb     | "v"
(1 ROW)

In here you can see that all I did was gettinf value of _k_ key from the object. Simple. I could also get it as normal text:

\=$ WITH d AS (
    SELECT json\_query( j, '$.k' returning text omit quotes ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof | r 
\-----------+---
 text      | v
(1 ROW)

Please note that I had to use _omit quotes_, as if I didn't:

\=$ WITH d AS (
    SELECT json\_query( j, '$.k' returning text ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof |  r  
\-----------+-----
 text      | "v"
(1 ROW)

I'd get still text, but instead of getting _v_ I got 3 characters: _“v"_. Which usually isn't what one would want.

Now. Let's assume you'd want to get elements from _.a_ but only the ones more than one. Trivial, should be:

\=$ WITH d AS (
    SELECT json\_query( j, '$.a\[\*\] ? ( @ \> 1 )' ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof | r 
\-----------+---
 jsonb     | 
(1 ROW)

Whoa. Why is r empty? The problem is that this expression returns multiple values, and this doesn't really work well. Json value can't have “1", and “2", and “3" – it can contain array of these things though. This is where wrappers come handy:

\=$ WITH d AS (
    SELECT json\_query( j, 'lax $.a\[\*\] ? ( @ \> 1 )' WITH array wrapper ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof |     r      
\-----------+------------
 jsonb     | \[2, 5, 15\]
(1 ROW)

There is also a way to specify default value to be returned, in case json\_query didn't match anything, or had an error.

In case of error, the clause is _X ON ERROR_, where _X_ can be one of:

*   ERROR – will raise exception
*   NULL
*   EMPTY ARRAY
*   EMPTY OBJECT
*   DEFAULT ‘whatever'

This works the same way I described above error handling in JSON\_EXISTS, so let's focus on handling empty return sets.

For example, what will happen if I'd like to get all values from .a that are above 50?

\=$ WITH d AS (
    SELECT json\_query( j, 'lax $.a\[\*\] ? ( @ \> 50 )' WITH array wrapper ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof | r 
\-----------+---
 jsonb     | 
(1 ROW)

It's null. But I can make it into something else using magical _X ON EMPTY_ clause:

\=$ WITH d AS (
    SELECT json\_query( j, 'lax $.a\[\*\] ? ( @ \> 50 )' WITH array wrapper DEFAULT '\["nothing", "found"\]' ON EMPTY) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof |          r           
\-----------+----------------------
 jsonb     | \["nothing", "found"\]
(1 ROW)

JSON\_VALUE
-----------

This is very much like JSON\_QUERY with one simple exception – you can't get multiple values from there. As such there is no _WITH … WRAPPER_ clause. Also, _KEEP/OMIT QUOTES_ is gone.

Generally this function makes sense if/when you are sure that you will be returning single scalar value. There is also one other _big_ difference. Default return datatype is TEXT:

\=$ WITH d AS (
    SELECT json\_value( j, '$.k' ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof | r 
\-----------+---
 text      | v
(1 ROW)

Of course you can use RETURNING clause to turn it to whatever you want 🙂

\=$ WITH d AS (
    SELECT json\_value( j, '$.a\[2\]' returning int8 ) AS r
    FROM t
)
SELECT pg\_typeof(r), r FROM d;
 pg\_typeof | r 
\-----------+---
 BIGINT    | 5
(1 ROW)

JSON\_TABLE
-----------

This is the **BIG** thing.

This one function has its own [section in docs](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-TABLE).

I checked, and it seems that everything that I wrote [previously](https://www.depesz.com/2022/04/06/waiting-for-postgresql-15-json_table/) still works/applies. So let's get the description from there (with small changes to reflect current state of my understanding):

Let's start with some simple example:

\=$ SELECT \* FROM json\_table(
    '\[{"a":10,"b":20},{"a":30,"b":40}\]'::jsonb,
    '$\[\*\]'
    COLUMNS (
        column\_a int4 path '$.a',
        column\_b int4 path '$.b'
    )
);
 column\_a | column\_b 
\----------+----------
       10 |       20
       30 |       40
(2 ROWS)

I assume the example is easy to understand.

Now, let's assume we want to add serial-like column, named id. Also, I'll show two more tricks:

\=$ SELECT \* FROM json\_table(
    '\[{"a":10,"b":20},{"a":30,"b":40}\]'::jsonb,
    '$\[\*\]'
    COLUMNS (
        id FOR ORDINALITY,
        column\_a int4 path '$.a',
        column\_b int4 path '$.b',
        a int4,
        b int4,
        c text
    )
);
 id | column\_a | column\_b | a  | b  | c 
\----+----------+----------+----+----+---
  1 |       10 |       20 | 10 | 20 | 
  2 |       30 |       40 | 30 | 40 | 
(2 ROWS)

Adding serial-like id worked. And please note that i also added columns _a_ and _b_ – without specifying their paths. In case path is simply ‘$.SOMETHING' and you want the column to be named _SOMETHING_ you don't need to explicitly state paths.

If there is no such field in the json, it will be returned as null.

Now, pretty commonly one has nested structures. For example, we could have json like this:

\=$ SELECT jsonb\_pretty(j) FROM sample;
              jsonb\_pretty               
\-----------------------------------------
 \[                                      +
     {                                  +
         "title": "first post",         +
         "author": "depesz",            +
         "comments": \[                  +
             {                          +
                 "body": "comment #1",  +
                 "author": "hubert"     +
             },                         +
             {                          +
                 "body": "comment #3",  +
                 "author": "lubaczewski"+
             },                         +
             {                          +
                 "body": "comment #5",  +
                 "author": "someone"    +
             }                          +
         \]                              +
     },                                 +
     {                                  +
         "title": "second post",        +
         "author": "depesz",            +
         "comments": \[                  +
             {                          +
                 "body": "comment #2",  +
                 "author": "depesz"     +
             },                         +
             {                          +
                 "body": "comment #6",  +
                 "author": "anyone"     +
             }                          +
         \]                              +
     },                                 +
     {                                  +
         "title": "third post",         +
         "author": "someone else",      +
         "comments": \[                  +
             {                          +
                 "body": "comment #4",  +
                 "author": "whoever"    +
             }                          +
         \]                              +
     }                                  +
 \]
(1 ROW)

Single row, nested structure.

With json\_table I can:

\=$ SELECT jt.\* FROM sample,
    lateral json\_table(
    j,
    '$\[\*\]'
    COLUMNS (
        id FOR ORDINALITY,
        author text,
        title text,
        NESTED PATH '$.comments\[\*\]'
        COLUMNS (
            comment\_author text PATH '$.author',
            comment\_body text PATH '$.body'
        )
    )
) AS jt;
 id |    author    |    title    | comment\_author | comment\_body 
\----+--------------+-------------+----------------+--------------
  1 | depesz       | FIRST post  | hubert         | comment #1
  1 | depesz       | FIRST post  | lubaczewski    | comment #3
  1 | depesz       | FIRST post  | someone        | comment #5
  2 | depesz       | SECOND post | depesz         | comment #2
  2 | depesz       | SECOND post | anyone         | comment #6
  3 | someone ELSE | third post  | whoever        | comment #4
(6 ROWS)

There are, as previously many additional options:

*   default clauses for fields
*   exists clauses that return boolean or int depending on jsonpath existing in given place
*   format specifier (json/jsonb) that allows extraction value from json, as json, even if datatype used is, for example, text
*   with/without wrapper – working just like in json\_query
*   keep/omit quotes
*   error handling, like _X ON ERROR_ in json\_query

And that kinda concludes the (long overdue) description. There are certainly aspects that I didn't cover with enough details, but if you plan on using any of these, I think that reading official documentation should be on your “todo" list anyway 🙂 And lots of experimentation.

Anyway – thanks a lot to all involved. There have been many patches over many years, authors of code, authors of docs, reviewers, testers. It's an amazing feature, and while I'm not really fan of using json blobs in databases, I can see that in some cases it makes sense, and having all these features is definitely great.
