Title: Redka: Redis re-implemented with SQL

URL Source: https://antonz.org/redka/

Published Time: Tue, 15 Jul 2025 06:31:14 GMT

Markdown Content:
I'm a big fan of Redis. It's such an amazing idea to go beyond the get-set paradigm and provide a convenient API for more complex data structures: maps, sets, lists, streams, bloom filters, etc.

I'm also a big fan of relational databases and their universal language, SQL. They've really stood the test of time and have proven to solve a wide range of problems from the 1970s to today.

So, naturally, one day I decided to combine the two and reimplement Redis using a relational backend —first SQLite, then Postgres. That's how [Redka](https://github.com/nalgeon/redka) was born.

[About Redka](https://antonz.org/redka/#about-redka) • [Use cases](https://antonz.org/redka/#use-cases) • [Usage example](https://antonz.org/redka/#usage-example) • [Performance](https://antonz.org/redka/#performance) • [Final thoughts](https://antonz.org/redka/#final-thoughts)

About Redka
-----------

Redka is a software written in Go. It comes in two flavors:

*   Standalone Redis-compatible server.
*   Go module for in-process use.

```
┌────────────┐   ┌────────────┐
Any   → RESP → │ Redka      │ → │ Postgres   │
client         │ server     │ ← │ or SQLite  │
               └────────────┘   └────────────┘
               ┌────────────┐   ┌────────────┐
Go client    → │ Redka      │ → │ Postgres   │
               │ module     │ ← │ or SQLite  │
               └────────────┘   └────────────┘
```

Redka currently supports five core Redis data types:

*   [Strings](https://github.com/nalgeon/redka/blob/main/docs/commands/strings.md) are the most basic type, representing a sequence of bytes.
*   [Lists](https://github.com/nalgeon/redka/blob/main/docs/commands/lists.md) are sequences of strings sorted by insertion order.
*   [Sets](https://github.com/nalgeon/redka/blob/main/docs/commands/sets.md) are unordered collections of unique strings.
*   [Sorted sets](https://github.com/nalgeon/redka/blob/main/docs/commands/sorted-sets.md) (zsets) are collections of unique strings ordered by score.
*   [Hashes](https://github.com/nalgeon/redka/blob/main/docs/commands/hashes.md) are field-value maps.

```
┌─────────────────────────┐  ┌─────────────────────────┐
│          Go API         │  │       RESP server       │
└─────────────────────────┘  └─────────────────────────┘
┌─────────┐ ┌─────────┐ ┌────────┐ ┌───────────────────┐
│ Strings │ │ Lists   │ │ Sets   │ │ Transaction mngmt │
└─────────┘ └─────────┘ └────────┘ └───────────────────┘
┌─────────┐ ┌─────────┐ ┌────────┐ ┌───────────────────┐
│ Keys    │ │ Hashes  │ │ ZSets  │ │ Database adapter  │
└─────────┘ └─────────┘ └────────┘ └───────────────────┘
┌──────────────────────────────────────────────────────┐
│                  Relational database                 │
└──────────────────────────────────────────────────────┘
```

Redka can use either SQLite or PostgreSQL as its backend. It stores data in a database with a simple [schema](https://github.com/nalgeon/redka/blob/main/docs/persistence.md) and provides views for better introspection.

Use cases
---------

Here are some situations where Redka might be helpful:

_Embedded cache for Go applications_. If your Go app already uses SQLite or just needs a built-in key-value store, Redka is a natural fit. It gives you Redis-like features without the hassle of running a separate server. You're not limited to just get/set with expiration, of course — more advanced structures like lists, maps, and sets are also available.

_Lightweight testing environment_. Your app uses Redis in production, but setting up a Redis server for local development or integration tests can be a hassle. Redka with an in-memory database offers a fast alternative to test containers, providing full isolation for each test run.

_Postgres-first data structures_. If you prefer to use PostgreSQL for everything but need Redis-like data structures, Redka can use your existing database as the backend. This way, you can manage both relational data and specialized data structures with the same tools and transactional guarantees.

Usage example
-------------

You can run the Redka server the same way you run Redis:

```
./redka -h localhost -p 6379
```

Then use `redis-cli` or any Redis client for your programming language, like `redis-py`, `node-redis`, `go-redis`, and so on:

```
set name alice
setex age 3600 25
get name
get age
```

```
OK
OK
alice
25
```

You can also use Redka as a Go package without the server:

```
// Open the database.
db, err := redka.Open("file:/redka.db?vfs=memdb", nil)
if err != nil {
    log.Fatal(err)
}
defer db.Close()

// Set some values.
db.Str().Set("name", "alice")
db.Str().SetExpire("age", 25, time.Hour)

// Read them back.
name, err := db.Str().Get("name")
fmt.Printf("get name = %v, err = %v\n", name, err)
age, err := db.Str().Get("age")
fmt.Printf("get age = %v, err = %v\n", age, err)
```

```
set name, err = <nil>
set age, err = <nil>
get name = alice, err= <nil>
get age = 25, err= <nil>
```

All data is stored in the database, so you can access it using SQL views:

```
select * from vstring;
```

```
┌─────┬──────┬───────┬─────────────────────┬─────────────────────┐
│ kid │ key  │ value │        etime        │        mtime        │
├─────┼──────┼───────┼─────────────────────┼─────────────────────┤
│ 1   │ name │ alice │                     │ 2025-07-15 05:26:39 │
│ 2   │ age  │ 25    │ 2025-07-15 06:26:42 │ 2025-07-15 05:26:42 │
└─────┴──────┴───────┴─────────────────────┴─────────────────────┘
```

Performance
-----------

Redka is not about raw performance. You can't beat a specialized data store like Redis with a general-purpose relational backend like SQLite. However, Redka can still handle tens of thousands of operations per second, which should be more than enough for many apps.

Here are the [redis-benchmark](https://github.com/nalgeon/redka/blob/main/docs/performance.md) results for 1,000,000 GET/SET operations on 10,000 randomized keys.

Redis:

```
SET: 133262.25 requests per second, p50=0.055 msec
GET: 139217.59 requests per second, p50=0.055 msec
```

Redka (SQLite):

```
SET: 26773.76  requests per second, p50=0.215 msec
GET: 103092.78 requests per second, p50=0.063 msec
```

Redka (PostgreSQL):

```
SET: 11941.72 requests per second, p50=0.775 msec
GET: 25766.55 requests per second, p50=0.359 msec
```

Final thoughts
--------------

Redka for SQLite has been around for over a year, and I recently released a new version that also supports Postgres. If you like the idea of Redis with an SQL backend — feel free to try Redka in testing or (non-critical) production scenarios.

See the [nalgeon/redka](https://github.com/nalgeon/redka) repo for more details.

[★Subscribe](https://antonz.org/subscribe/) to keep up with new posts.
