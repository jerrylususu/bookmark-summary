Title: What to do about SQLITE_BUSY errors despite setting a timeout - Bert Hubert's writings

URL Source: https://berthub.eu/articles/posts/a-brief-post-on-sqlite3-database-locked-despite-timeout/

Published Time: 2025-02-16T21:00:00+01:00

Markdown Content:
So I’m a huge SQLite fanboy and I use it for almost everything these days. Recently, the project added [sqlite3\_rsync](https://www.sqlite.org/rsync.html) which allows you to swiftly replicate your database to other servers (or to the same server if you want), and this really was the cherry on top for me.

Last week however, I ran into one of my projects unexpectedly getting [SQLITE\_BUSY](https://www.sqlite.org/rescode.html#busy) errors. And then someone urged me to run ‘a real database’ (PostgreSQL), and that hurt.

> The tl;dr on this, to prevent SQLITE\_BUSY errors even when setting a timeout, don’t ever upgrade transactions to read-write. If you know you are going to write in a transaction, use ‘BEGIN IMMEDIATE’, or start off with the write. But do read on for why this is so, and how other databases struggle with this problem as well.  
> Thanks are due to PostgreSQL developer & backdoor-slayer [Andres Freund for sharing his wisdom on Mastodon](https://mastodon.social/@AndresFreundTec/114009633982257113), which found its way into this post. Mistakes remain mine though!

Before we start, do know I love both PostgreSQL and SQLite, these are two very impressive projects, and we are extremely lucky that we get to benefit from all this excellence.

The problem
-----------

When running in [WAL mode](https://www.sqlite.org/wal.html) (which you should), SQLite makes some explicit and detailed concurrency promises: “Readers do not block writers and a writer does not block readers. Reading and writing can proceed concurrently”. The devil is in those details however.

Now, we can easily deal with _waiting_ for the database to do something. Often there aren’t that many writes, and if occasionally two writes have to wait for each other, this is not a problem, especially since SQLite is extremely fast anyhow. SQLite’s single writer mode will often in practice be faster than other server’s multiple writer models, if only because it has no interprocess/network latency penalty. Meanwhile, SQLite offers various timeout settings and functions to deal with waiting for write access.

What is harder to deal with however is when queries or inserts don’t wait but immediately dump a SQLITE\_BUSY error on you, despite setting a timeout. It can be hard to recover from that.

So why does this happen?

SQLite transactions
-------------------

SQLite allows you to [BEGIN a transaction](https://www.sqlite.org/lang_transaction.html) without telling it what kind of transaction this will be: read-only or a read-write transaction. SQLite actually determines this based on the first statement you execute within the transaction. If that is an UPDATE or a DELETE or anything else that changes things, you get a write capable transaction. Otherwise you get a read-only transaction. You can also force this decision with BEGIN IMMEDIATE, which always starts a write transaction.

To demonstrate this, we’ll first setup a database:

```
pragma journal_mode="wal"; -- only have to do this once
create table t (v INT) strict;
.timeout 10000 -- 10 seconds
```

Next up, let’s open two parallel connections:

```
begin immediate;           |
insert into t values (1);  | begin immediate; -- blocks 
commit;                    | -- we are unblocked 
                           | insert into t values(2);
                           | commit;
```

This is all good. It may be disappointing that SQLite only allows one simultaneous writer, but at least this is clear, and by waiting for a bit, our writes do happen (sequentially). If we leave the transaction on the left open for too long, the right side will get a SQLITE\_BUSY error:

```
Runtime error: database is locked (5)
```

Figuring out the right timeout is not easy. But, if you get a timeout, you can reconsider, and perhaps decide to wait even longer.

Getting into trouble
--------------------

As noted, if you BEGIN a transaction in SQLite without specifying ‘immediate’, SQLite actually only begins a transaction after you submit the first statement, and it will pick the _kind_ of transaction based on that first statement (read-only or read-write).

If you later in a read-only transaction try to write to the database somehow, SQLite will attempt to _upgrade_ your transaction to a write transaction. And this is where we can run into problems:

```
                           | begin;
begin;                     | insert into t values(2); 
select count(1) from t;    | -- we are in a WRITE transaction
insert into t values(3);   | 
Runtime error: database is locked (5) -- immediately 
```

The right side opens a write transaction based on the initial ‘insert’ statement. The left side opens a read-only transaction, while the right side has a write transaction open. SQLite supports this just fine.

Then however the left site tries to do an insert, which leads to an attempt to upgrade the transaction to read-write. And this fails immediately. No matter how high you set your .timeout, this scenario always delivers an instant SQLITE\_BUSY error. And this is frustrating.

Why does this have to happen?
-----------------------------

At this point, you might have preferred to have the insert on the left just wait it out until the transaction on the right is done. But no can do.

SQLite implements a [transaction isolation mode called “serializable”](https://www.sqlite.org/isolation.html). The technical definition from [some kind of SQL standard informal draft review](https://en.wikipedia.org/wiki/Isolation_(database_systems)#Serializable) (?): “A serializable execution is defined to be an execution of the operations of concurrently executing SQL-transactions that produces the same effect as _some_ serial execution of those same SQL-transactions”.

When the transaction on the left wanted to upgrade itself to a read-write transaction, SQLite could not allow this since the transaction on the right might already have made changes that the transaction on the left had not yet seen.

This in turn means that if left and right transactions would commit sequentially, the result would not necessarily be what would have happened if all statements had been executed sequentially within the same transaction. So no go.

Now, this is not a SQLite problem, all quality databases mostly do the same thing when in SERIALIZABLE mode.

Let’s try it in PostgreSQL:

```
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL serializable;
```

Then we run two transactions:

```
                              | begin;
begin;                        | select count(1) from t;
select count(1) from t;       | insert into t values (2);
insert into t values (1);     | commit;
commit;                       |
ERROR:  could not serialize access due to read/write dependencies among transactions
DETAIL:  Reason code: Canceled on identification as a pivot, during commit attempt.
HINT:  The transaction might succeed if retried.
```

It may be good to know that in many common cases, PostgreSQL can prove there are no serialization issues, and will in fact be able to commit both transactions without issue. But not always.

Another key difference is that PostgreSQL, being an extremely impressive project, allows for multiple transaction isolation levels, some of which do not get you these errors (but also not this consistency). SQLite just has one mode (also due to its straightforward design which lacks row-level locks).

It turns out that there is a fundamental issue with concurrent read-write access to all databases - you can have slow operations that never fail nor get errors, or you can run in faster modes where you could get inconsistent results, or you can pick a mode where you will have to learn how to recover from writes that failed and need to be reissued somehow. If someone smugly tells you their “real database” supports multiple writers, know that they probably aren’t aware of [these trade-offs](https://www.postgresql.org/docs/current/transaction-iso.html).

By default, PostgreSQL runs in Read Committed isolation mode, which leads to the following behaviour that may be surprising for people coming from SQLite or MySQL:

```
BEGIN;                      | BEGIN;
select count(1) from t;     | insert into t values (3);
     4                      | COMMIT;
select count(1) from t;     |
     5                      |
COMMIT;                     |
```

In SQLite and [MySQL](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html), the left transaction would not have seen the insert that happened on the right. As long as the left transaction is open, no changes are observed. But in PostgreSQL’s default mode, you do see them. Note that MySQL defaults not to serializable but to ‘[repeatable read](https://en.wikipedia.org/wiki/Isolation_(database_systems)#Repeatable_reads)’.

Again, [this is all a matter of choice](https://mastodon.social/@AndresFreundTec/114009633982257113), and there are [lots of reasons to prefer one transaction isolation mode over another](https://www.postgresql.org/docs/current/transaction-iso.html). Just know and understand which one you are using!

Ok, but now what
----------------

The excellent [PostgreSQL documentation notes that serializable mode can lead to failing transactions that need to be repeated](https://www.postgresql.org/docs/current/transaction-iso.html#XACT-SERIALIZABLE). And they also offer us advice for how to ameliorate that, and this advice is very useful for SQLite as well:

*   Declare transactions (or connections in SQLite) as READ ONLY when possible.
*   Control the number of active connections, using a connection pool if needed. This is always an important performance consideration, but it can be particularly important in a busy system using Serializable transactions.
*   Don’t put more into a single transaction than needed for integrity purposes.
*   Don’t leave connections dangling “idle in transaction” longer than necessary

This is all mitigation. To absolutely prevent SQLITE\_BUSY errors, you have a few options (when running in WAL mode):

*   If you know you are going to write in a transaction, start it with a write, or use BEGIN IMMEDIATE
*   Just don’t use transactions, or effectively, use single-statement transactions

You might read here and there to just always use BEGIN IMMEDIATE but that will easily cause timeouts, since you can only have a single write transaction open at a time.

It is better to have a good think on how you do writes, and completely avoid transactions that have to be upgraded. Because that is where the immediate SQLITE\_BUSY errors come from once you’ve made a database connection.

SQLITE\_BUSY\_RECOVERY
----------------------

If your program starts by opening multiple SQLite connections at the same time, you might get a SQLITE\_BUSY error at that stage. This has to do with [the rolling the WAL journal when recovering from an unclean shutdown](https://www.sqlite.org/rescode.html#busy_recovery). If you open multiple SQLite connections at the beginning of your program, I recommend doing so sequentially. This admittedly is somewhat of a wart.

Some further reading
--------------------

*   [Wikipedia page Isolation (database systems)](https://en.wikipedia.org/wiki/Isolation_(database_systems))
*   [SQLite Transactions page](https://www.sqlite.org/lang_transaction.html)
*   [SQLITE\_BUSY](https://www.sqlite.org/rescode.html#busy)
*   [How SELECT FOR UPDATE Works (in PostgreSQL)](https://haril.dev/en/blog/2024/04/20/select-for-update-in-PostgreSQL)
