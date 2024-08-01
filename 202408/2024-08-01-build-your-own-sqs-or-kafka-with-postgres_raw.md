Title: Build your own SQS or Kafka with Postgres

URL Source: https://blog.sequinstream.com/build-your-own-sqs-or-kafka-with-postgres/

Published Time: 2024-07-30T18:37:00.000Z

Markdown Content:
We're [Sequin](https://sequinstream.com/?ref=blog.sequinstream.com), an open source message stream built on Postgres. We think Sequin's cool, but you don't need to adopt the project to get started with streaming in Postgres. In fact, you can turn Postgres into a basic queue/stream pretty easily. Below, we share what we've learned so you can roll your own.

Build your own SQS
------------------

Simple Queue Service (or SQS) is a popular message queue from AWS. You can build your own SQS pretty quickly from scratch in Postgres.

The staple feature of SQS (and most queues) is **exactly once delivery within a visibility timeout**. It's called a visibility timeout because no other workers can pull (or "see") that message for some period after delivery. When the visibility timeout expires, the system will assume the worker has died, and will redeliver the message to another worker.

### Build the queue

You can create an SQS-inspired message queue table like so:

```
create table messages (
  seq serial primary key,
  data jsonb not null,
  not_visible_until timestamp,
  deliver_count integer not null default 0,
  last_delivered_at timestamp,
  inserted_at timestamp not null default now(),
  updated_at timestamp not null default now()
);
```

I like using the column name `seq` instead of `id` for the primary key, as it makes it clear it's the sequence number of the message.

Sending messages to the queue is easy – you just insert to this table. In a bit, you'll see how you can use `not_visible_until` to ensure exactly once delivery within a visibility period.

`deliver_count` is optional, but usually helpful for debugging. You can also set up rules where a message can only be delivered some max number of times.

`data` can be whatever you like. `jsonb` is a versatile option. But if you're never going to query the `data` column of `messages`, using a regular `text` column is a little more performant.

### Receiving messages

To select available messages, your query will look like this:

```
select seq
  from messages
  where not_visible_until is null
    or (not_visible_until <= now())
  order by inserted_at asc
  limit $1
```

When a message has never been delivered, `not_visible_until` is `null`. Otherwise, we respect the visibility timeout by not redelivering messages until `not_visible_until`.

The `limit $1` allows the consuming process to specify the batch size of messages it wants to receive.

Given this query will form the foundation of the receive message flow, add an index:

```
create index idx_messages_visibility on messages (not_visible_until, inserted_at asc);
```

Building on this, for receiving messages, you want to do two things inside a single query or transaction:

1.  "Claim" messages by modifying message rows.
2.  Retrieve the `data` payload.

You can do this with an `UPDATE` that uses a subquery:

```
with available_messages as (
  select seq
  from messages
  where not_visible_until is null
    or (not_visible_until <= now())
  order by inserted_at
  limit $1
  for update skip locked
)
update messages m
set 
  not_visible_until = $2,
  deliver_count = deliver_count + 1,
  last_delivered_at = now(),
  updated_at = now()
from available_messages am
where m.seq = am.seq
returning m.seq, m.data;
```

This query accepts two parameters. The first parameter (`$1`) is the batch size or count of messages to return. The second parameter (`$2`) is the visibility timeout.

`available_messages` is a common table expression [CTE](https://www.postgresql.org/docs/current/queries-with.html?ref=blog.sequinstream.com) (which I prefer over subqueries when possible). It selects available messages `for update skip locked`. This means:

*   I want to lock these rows because I'm about to update them.
*   Please only return rows that are not already locked by another process.

Without `for update skip locked`, there's a race condition. You can have two concurrent sessions evaluate the CTE/select at the same time. Then, they'd both run the `update`. One session would succeed first, and receive the messages. But then the second session – unknowingly – would perform its `update` as well and receive the same batch of messages.

You can also wrap this in a function like so:

```
create or replace function receive_messages(batch_size integer, not_visible_until timestamp)
returns table (id integer, data jsonb)
language sql
as $$
  -- query here
$$;
```

Or, you can query via your ORM. Doing so would likely require breaking this query up into four parts:

1.  Open a transaction
2.  `select [...] for update skip locked`
3.  `update [...] returning`
4.  Commit the transaction

Because they're more universal than showing queries in any one ORM, I'll use queries with CTEs throughout this post.

To ack messages, your worker can just delete the messages that it processed:

```
delete from messages where seq = ANY($1);
```

Or move them from the main `messages` table to an archive table like this:

```
with deleted_messages as (
  delete from messages
  where seq = ANY($1)
  returning *
)
insert into archived_messages (
  seq, data, deliver_count, last_delivered_at, inserted_at, updated_at
)
  select 
    seq, data, deliver_count, last_delivered_at, inserted_at, updated_at
    from deleted_messages
    returning seq;
```

With that, you have about 80% of the most important features that SQS offers!

### Adding FIFO

In SQS, a queue can be configured as **FIFO** (first in, first out). This is useful when you need to make sure that you process related messages in order.

For example, imagine you're processing a stream of updates from an API. It's important that you process records in order. If a record is updated then deleted, you want your workers to handle the update then the delete – not the other way around.

When an SQS queue is configured as FIFO, you publish messages you want to process in sequential order with the same `key`. Then, SQS ensures they are delivered in the order they were received. If two messages have the same `key`, the first message must be acked in order for the second message to be made available for delivery.

You can achieve a basic version of this behavior fairly easily in Postgres. First, add a `key` to your `messages` table:

```
alter table messages add column key text not null;

-- add an index as well, as this will be queried often
create index idx_messages_key on messages (key);
-- and one that combines key with inserted_at
create index idx_messages_inserted_at_key on messages (key, inserted_at asc);
```

Then, you need to tweak the logic for receiving messages. To do so requires adding an additional step to the receive query.

First, you want to select the first (earliest) instance of a message for a given `key`, where that message is not currently processing:

```
with processing_keys as (
  select key
  from messages
  where not_visible_until >= now()
),
next_message_seqs as (
  select distinct on (key) seq
  from messages
  where key not in (select key from processing_keys)
  order by key, inserted_at
  limit $1 -- batch_size
),
-- ...
```

Then, you can lock those messages like so:

```
-- ...
next_messages as (
  select m.*
  from messages m
  join next_message_seqs nmi on m.seq = nmi.seq
  where m.not_visible_until is null or m.not_visible_until <= now()
  for update skip locked
)
-- ...
```

You have to perform this operation in two separate steps, as `for update skip locked` does not work with `distinct` (or `group by` for that matter).

There is a little race here: it's possible the query will select keys in the `next_message_ids` CTE but by the time it tries to lock the messages with those keys they'll have been claimed by another process. This race is why I recommend filtering with `where` again in `next_messages`, just in case.

Still, when this race occurs it will result in this receive messages query returning fewer messages than the requested `batch_size`. This could be a deal-breaker in high throughput systems. So, I detail resolutions in "[Advanced FIFO](https://blog.sequinstream.com/build-your-own-sqs-or-kafka-with-postgres/#advanced-fifo)".

Finally, with `next_messages` locked, you can update them:

```
-- ...
update messages m
set 
  not_visible_until = $2,
  deliver_count = m.deliver_count + 1,
  last_delivered_at = now(),
  updated_at = now()
from next_messages nm
where m.seq = nm.seq
returning m.seq, m.data, m.key;
```

Now, messages can't be made available to consumers until any prior messages with the same `key` have been acked.

### Advanced FIFO

The basic FIFO approach has a race condition when receiving messages. There are some decent mitigations for this, such as:

*   Request `batch_size * 10` (or some other multiple) in the first query. Then, use `batch_size` in the second query. This will give you a greater number of message IDs to select from in the subsequent query. You'll basically be able to have X process pull simultaneously, where X is the multiple.
*   Use an advisory lock to ensure only one process can pull messages at a time. This will lower throughput but ensure `batch_size` is always filled.
*   Use a procedure to loop until the `batch_size` is filled.

Alternatively, with a little more overhead/bookkeeping on inserting into `messages`and ack'ing them, you can eliminate that race condition.

The trick is that you need to keep track of what the lowest `seq` is for a given `key`. As you'll see, this is not trivial! But you can still build something that handles FIFO performantly.

You can create a new table, `message_key_seqs`. This table will indicate the lowest `seq` for any given `key`. Because you'll need to update the table transactionally on all writes to `messages`, there will be some locking between writes. If two processes are simultaneously committing messages with the same `key`, they will be serialized during the `update message_key_seqs` call. This should only be an issue if messages with the same key are repeatedly being written in quick succession.

```
create table message_key_seqs (
  key text not null,
  seq bigint not null,
  primary key (key, seq)
);
```

Then, you should update this table after any inserts into `messages`, inside the same transaction:

```
begin;

insert into messages
  (...);

insert into message_key_seqs (key, seq)
  values (unnest($1::text[]), unnest($2::bigint[]))
  on conflict (key) do update
  set seq = least(message_key_seqs.seq, excluded.seq);
```

The `update` takes batches of keys (`$1`) and seqs (`$2`) and upserts them into `message_key_seqs`. The query sets `seq` to the incoming value if it's lower than the current value.

This means you can use `message_key_seqs` to drive receiving messages:

```
with next_messages as (
  select m.*
  from messages m
  join message_key_seqs mks on m.key = mks.key
  where m.seq = mks.seq
    and (m.not_visible_until is null or m.not_visible_until <= now())
  order by m.inserted_at
  limit $1  -- batch_size
  for update skip locked
)
update messages m
set 
  not_visible_until = now() + $2,  -- visibility timeout
  deliver_count = m.deliver_count + 1,
  last_delivered_at = now(),
  updated_at = now()
from next_messages nm
where m.seq = nm.seq
returning m.seq, m.data, m.key, m.seq;

commit;
```

The most complicated part is in ack'ing. When you ack, you need to set the next lowest `seq` for the newly deleted messages.

One way is to first select all the `key, min(seq)` pairs from `messages` matching the keys you're ack'ing (`$1`):

```
begin;

-- $1 here is the list of seqs you're ack'ing
delete from messages where seq = any($1);

-- perform in a follow-up query. $1 here is the list of keys
select key, min(seq) as min_seq
  from messages
  where key = any($1)
  group by key;
```

Then, your application can use those key/seq pairs to determine which `message_key_seqs` to delete. It will be the set of keys that was in the first set (keys to ack) but not in the second set (the `key, min(seq)` pairs):

```
-- Delete entries from message_key_seqs where there are no more messages
delete from message_key_seqs mks
  where key = any($1);
```

Finally, update the remaining entries in `message_key_seqs` and commit:

```
update message_key_seqs
  set seq = new_seq.seq
  from (
    select unnest($1::text[]) as key, unnest($2::bigint[]) as seq
  ) as new_seq
where message_key_seqs.key = new_seq.key
```

This query takes a list of the keys (`$1`) alongside their seqs (`$2`). Batch updates like this often look a lot less complicated in ORMs.

Whew! Postgres' powerful concurrency paradigm (multi version concurrency control or MVCC) usually works in your favor, but means to get FIFO behavior you need a little elbow grease.

### Dead letter queue

In this system, what happens if a message keeps being delivered but workers always fail to process it? There may be something wrong with the message, or it might exploit a bug in your code.

To make dealing with this issue easier and avoid wasting too many cycles in your queue, you can introduce a **dead letter queue**. A dead letter queue is a place you can store messages to get them out of your main queue. The simplest strategy here is to simply move problematic messages from your main queue to the dead letter queue for future, manual diagnosis.

Your dead letter queue could look like this:

```
create table dead_messages (
  id serial primary key,
  message_seq integer not null,
  message_data jsonb not null,
  message_key text,
  message_deliver_count integer not null,
  message_last_delivered_at timestamp,
  inserted_at timestamp not null
);
```

You could have a background job move messages to `dead_messages`. Or, to keep things simple, you can "piggyback" on one of your lifecycle functions.

For example, your "move to dead letter queue" query can look like this:

```
  with messages_to_move as (
    select seq
    from messages
      where (
          not_visible_until is null
          or (not_visible_until <= now())
      )
      and deliver_count >= $1
    order by inserted_at
    limit $2
    for update skip locked
  ),
  deleted_messages as (
    delete from messages m
    using messages_to_move mtm
    where m.seq = mtm.seq
    returning m.seq, m.data, m.key, m.deliver_count, m.last_delivered_at
  )
  insert into dead_messages (message_seq, message_data, message_key, message_deliver_count, message_last_delivered_at)
  select seq, data, key, deliver_count, last_delivered_at
  from deleted_messages;
```

The first CTE selects messages that need to move to `dead_messages`. It ensures that the messages are (1) available for delivery but (2) exceed some max deliver count (`$1`). It also does so in batches (`$2`), which is usually wise to ensure no one instance of this query runs too long.

The second CTE (`deleted_messages as (...)`) deletes the messages from `messages`. Then the primary query inserts the dead messages into `dead_messages`.

You could also piggyback on message ack'ing. The only downside with this approach is that the `messages` table could grow unbounded if all your workers are failing to ack.

### How does this compare to SQS?

Postgres is a great fit for taking on SQS workloads.

If a non-FIFO SQS queue is sufficient, the biggest advantage SQS has is that it has [unlimited throughput](https://aws.amazon.com/sqs/features/?ref=blog.sequinstream.com) (according to AWS). So if your throughput is very high and ordering doesn't matter, SQS might be hard to beat with Postgres.

But if you need FIFO or your throughput is in the ~thousands per second, Postgres is a great option. FIFO SQS can support up to 3,000 messages per second. A basic machine running Postgres can achieve that easily as well.

Build your own Kafka
--------------------

SQS and Kafka are both messaging systems that help power async workloads. But their approaches are quite different.

A Kafka cluster can contain many topics. A topic shares some features with an SQS FIFO queue: messages are persisted until they're processed. And messages with the same key must be processed in order.

The primary difference is that in Kafka, **messages are not deleted after they're read**. Instead, each topic defines its own retention policy (e.g. "keep messages around for 60 days" or "keep messages around indefinitely".)

Building on this, Kafka has the concept of a consumer group. A topic can have many **consumer groups**. Each consumer group will only process each message once. In SQS, exactly once processing is achieved by simply deleting the message after it's processed. In Kafka, exactly once processing is guaranteed _per consumer group_. And it's achieved by the consumer group having a cursor or _offset_ which indicates where in the stream the consumer group is.

When a consumer group acks a message, it doesn't delete the message, it just increments its offset. This leaves the message in place for other consumer groups to process.

This is what makes Kafka a **stream** whereas SQS is a queue.

Streams are essentially a superset of queues and add some nice functionality. You can easily fan out one message to multiple different services. You can add new services/workers to your system at any time, and they can "play through" the history of messages. You can rewind and replay messages. And the history of messages can be useful for debugging.

Storing messages for a long time is naturally something that Postgres excels at. You can evolve the SQS design into a stream by:

1.  Decoupling messages from the state around their consumption
2.  Storing consumer state in another table

In Kafka, a consumer group is essentially an instance of offset state. When you create a new service that should process messages in a topic, you create a new consumer group for that service. Then you can have one or more **workers** consume messages from the topic via that consumer group.

To build Kafka in Postgres, you can create a `messages` table and a `consumer_group_offsets` table.

Because each message has a `seq` which is the sequence number, you can use `seq`as the offset. `messages` will contain just the `key` and `data`. `consumer_group_offsets` might look like this:

```
create table consumer_group_offsets (
  consumer_name text primary key,
  seq bigint default 0 not null
);
```

Each consumer group in your system will have a corresponding entry in `consumer_group_offsets`. So, if you have two services that should consume from the stream independently, you'll have two rows in `consumer_group_offsets`, one for `service1` and the other for `service2`.

The problem with this design currently is that messages can only be processed in serial, one-at-a-time, by a single worker for each consumer group.

So, like Kafka, you really need the concept of **partitions**. Partitions are what allow multiple workers to process messages concurrently. Worker A can grab a batch of messages to process from partition 1 while Worker B can grab a batch of messages to process from partition 2. They can both finish in their own time, and ack their batch, moving the offset for each partition forward.

Therefore, `consumer_group_offsets` should look like this:

```
create table consumer_group_offsets (
  consumer_name text primary key,
  partition int not null,
  seq bigint not null,
  updated_at timestamp default now() not null,
  inserted_at timestamp default now() not null
);
```

i.e. each `partition` + `consumer_name` should have its own `seq`. The `seq` will be the last processed `messages.seq` for a given `partition` + `consumer_name`.

You can create a `messages` table with a deterministic `partition` like so:

```
create sequence messages_seq;

create table messages (
  seq bigint not null default nextval('messages_seq'),
  key text not null,
  data text not null,
  inserted_at timestamp not null default now(),
  partition int generated always as (abs(hashtext(key) % 10)) stored,
  primary key (seq, partition)
);

create index idx_messages_seq on messages (seq);
```

The `messages` table no longer contains state about consumption, just the messages.

The most interesting bit is `partition`. It's a generated column, computed based on the `key` on insert. The goal is to produce a deterministic number between 0 and 9 for a given string `key`. `hashtext` computes a hash of the `key`, an `int`. The `% 10` takes the modulus to get a number from 0 to 9. `abs` ensures the result is non-negative (`hashtext` can return negative values).

This gives you 10 "partitions" to consume from.

To make things simple, I'm treating a Postgres table like Kafka treats a Kafka topic. i.e. all messages will flow into this table and consumers will play through every message in this table. If you wanted multiple "topics" in your system, you could have a table for each "bucket" of messages: one for `orders`, another for `subscriptions`, etc. (You could also store multiple "topics" on a single table, but that complicates things a fair bit.)

With this data model, here's the workflow I propose:

*   A worker runs a query to receive a batch of messages for a consumer group.
*   The query checks to see if any `consumer_group_offsets` are available.
*   If an offset is available, the query locks the offset. It then delivers the batch of messages.
*   When the worker is done processing the batch, it acks them by incrementing the offset on `consumer_group_offsets`.

Following that, a worker can first run a query to try to lock an offset like this:

```
-- open a transaction, needed for `for update skip locked`
begin;
select * from consumer_group_offsets
    where consumer_name = $1
    for update skip locked
    limit 1;
```

If it gets an offset, it can proceed with querying the `messages` table:

```
select * from messages
  where partition = $1 and seq > $2
  limit $3
  order by seq asc
```

Where `$1` and `$2` are the partition and offset from the first query, respectively.

It makes enough sense to just perform two back-to-back queries from your application, but you can also combine them into a single query like so:

```
begin;
with locked_offset as (
    select consumer_name, seq, partition
    from consumer_group_offsets
    where consumer_name = $1
    for update skip locked
    limit 1
    order by updated_at asc
)
select 
    lo.consumer_name,
    lo.seq as current_seq,
    lo.partition,
    m.seq,
    m.key,
    m.data,
    m.inserted_at
from locked_offset lo
left join messages m on m.partition = lo.partition and m.seq > lo.seq
where lo.consumer_name is not null  -- Ensures we only return rows if we got a lock
order by m.seq asc
limit $2;
-- ... process the messages
-- ... ack the messages
commit;
```

Here, I'm proposing you do this all in one big transaction (hence the `begin/commit`). This locks the offset record in `consumer_group_offsets`. With that lock in place, a worker can safely process messages for a partition. (If you'd prefer not to hold open a long-running transaction, a reasonable alternative is to set a `locked_until` field on `consumer_group_offsets` and enforce exclusivity that way.)

Then, to acknowledge a batch of messages, you just need to set the offset to the max `seq` of the batch at the end of your transaction:

```
begin;
-- ... process the messages
update consumer_group_offsets
  set seq = $1, updated_at = now()
  where consumer_name = $2 and partition = $3;
```

Note that in the receive query, you should sort the offsets by `updated_at asc`. Then in the ack query, you set `updated_at = now()`. This ensures that your workers "round robin" offsets.

To prevent an unresponsive worker from "hogging" a `consumer_group_offset` for too long, be sure to set a timeout limit on your workers. You can do this application side, but it may also make sense to set one for the transaction, so you know for sure how long offsets can be locked for:

```
begin;
set local statement_timeout = '30s';
-- ... run the select query
```

With this simple design, you get a lot of Kafka's functionality right in Postgres:

*   The `messages` table acts like a Kafka topic, storing all messages
*   Messages are stored indefinitely
*   Messages are delivered exactly once within a visibility timeout
*   Work fans out to multiple workers
*   Workers in a consumer group can process messages concurrently
*   Messages with the same `key` are processed in order
*   Trivial to rewind offsets in order to replay messages

The neat part is that you don't need the complexity of a Kafka broker/Zookeeper. Postgres takes care of coordination through the `consumer_group_offsets` table, so workers can be safely assigned a partition each time they request a batch.

There's one big flaw and a notable drawback, though:

### Flaw: Overcoming the sequence issue

[Postgres can commit sequences out-of-order](https://blog.sequinstream.com/postgres-sequences-can-commit-out-of-order/). This means there are race conditions with the current design. It's possible a `seq` for a given partition will be incremented in such a way as to skip a message that was recently inserted.

Postgres' MVCC paradigm makes paginating Postgres challenging. There are, unfortunately, no easy shortcuts here.

If you import the two functions from that post, `register_sequence_transaction` and `max_safe_seq`, you can use them to protect against this issue like so:

```
-- for inserts
begin;
perform register_sequence_transaction('messages_seq');
-- do the insert
insert into messages
  (...);
commit;
```

Then in reads, change this line:

```
left join messages m on m.partition = lo.partition and m.seq > lo.seq and m.seq < max_safe_seq('messages_seq')
```

This should remove the possibility of skipping messages.

### Drawback: Altering the partition count

It's worth noting that changing the partition count is not trivial. If you were to change the partitions from `10` to `11`, all messages would need to be shuffled around. It would also render your consumer group offsets meaningless.

The partition count determines your max concurrency. So couldn't you just set it to some arbitrarily high value, like `100` or `1000`? Not quite: if you only have a handful of workers pulling messages, it will take them a long time to round-robin through all the partitions.

So, in this design, you want your worker count to roughly match your partition count.

### Taking partitions further

Postgres comes with table partitioning. For a high-throughput system, you can expand on the design by actually partitioning your data into many tables.

Partitioning should speed up writes, especially for single message inserts, as the writes will be distributed across many tables. Reads should also be faster, as each query will run against a single partition table, which is a slice of all messages.

Here's what that looks like:

```
create sequence messages_seq;

create table messages (
  seq bigint not null default nextval('messages_seq'),
  key text not null,
  data text not null,
  inserted_at timestamp not null default now(),
  primary key (seq)
) partition by hash (key);

-- Create 10 partitions
-- Little verbose!
create table messages_0 partition of messages for values with (modulus 10, remainder 0);
create table messages_1 partition of messages for values with (modulus 10, remainder 1);
create table messages_2 partition of messages for values with (modulus 10, remainder 2);
create table messages_3 partition of messages for values with (modulus 10, remainder 3);
create table messages_4 partition of messages for values with (modulus 10, remainder 4);
create table messages_5 partition of messages for values with (modulus 10, remainder 5);
create table messages_6 partition of messages for values with (modulus 10, remainder 6);
create table messages_7 partition of messages for values with (modulus 10, remainder 7);
create table messages_8 partition of messages for values with (modulus 10, remainder 8);
create table messages_9 partition of messages for values with (modulus 10, remainder 9);

create index idx_messages_inserted_at on messages (inserted_at);
```

The neat part is, none of your queries have to change! You'll continue to run queries against the `messages` table. Postgres will route queries to the appropriate partition table.

### Deleting old messages from the table

You can add a "retention policy" to the table by deleting old messages from it.

A simple approach is to write a Postgres function that loops until stale messages have been deleted:

```
create or replace function batch_delete_old_messages(
    batch_size integer default 10000,
    max_deletions integer default 1000000
)
returns integer as $$
declare
    total_deleted integer := 0;
    batch_deleted integer;
begin
    loop
        with deleted_rows as (
            delete from messages
            where ctid in (
                select ctid
                from messages
                where inserted_at < now() - interval '60 days'
                limit batch_size
            )
            returning 1
        )
        select count(*) into batch_deleted from deleted_rows;

        total_deleted := total_deleted + batch_deleted;
        
        -- when batch_deleted < batch_size, we've deleted the last "page" of messages
        exit when batch_deleted < batch_size or total_deleted >= max_deletions;
        
        perform pg_sleep(0.1);  -- short pause between batches
    end loop;

    return total_deleted;
end;
$$ language plpgsql;
```

You can then schedule this function to run with a tool like `pg_cron`:

```
create extension pg_cron;

-- scheduling with pg_cron (assuming it's installed)
select cron.schedule('0 1 * * *', $$select batch_delete_old_messages()$$);
```

Alternatively, you could use a tool like [pg\_partman](https://github.com/pgpartman/pg_partman/?ref=blog.sequinstream.com).

### How does this compare to Kafka?

The reason Kafka has the runtime that it does (with topics and partitions) is so that it can offer its guarantees at massive scale. Each topic partition can live on its own machine, meaning you can keep adding machines to a Kafka cluster to get it to scale horizontally.

We were able to replicate this design pattern in Postgres, but it's running on a single machine.

The horizontal scalability of Kafka gives it a big throughput advantage over Postgres. Postgres doesn't partition in the same way across machines, at least not out-of-the-box.

So, it's a matter of your requirements. If you need massive scale and throughput (> 100k messages/sec), Kafka will be hard to beat. But if you're not operating at that scale, _Postgres_ is hard to beat. You can use one system in your stack (Postgres) instead of two (Postgres and Kafka), and Postgres is far more observable than Kafka (everything is just a table).

A Kafka stream with SQS consumption
-----------------------------------

Replicating Kafka's consumer group and offset strategy into Postgres yields a great design. The two tables, `messages` and `consumer_group_offsets` are simple. The queries to pull batches of messages are fairly concise. Really, the most un-ergonomic part is dealing with `seq`, which you can abstract away into functions as I do above.

Still, some might find Kafka's partition/offset strategy too limiting. The primary downside is the constraints around partitions. The partition counts are hard to change. And a single bad message can stop a partition from progressing––you can't progress an offset until all messages have been processed.

You can create something multi-paradigm: keep the `messages` table, but use message queue functionality to pull from it. So you get the benefits of a stream-based solution, like Kafka. But ergonomics that resemble SQS. This makes the concurrency dynamics of consumption much more dynamic.

In this approach, you don't need a `partition` key on `messages` anymore:

```
create sequence messages_seq;

create table messages (
  seq bigint not null default nextval('messages_seq'),
  key text not null,
  data text not null,
  inserted_at timestamp not null default now(),
  primary key (seq)
);
```

Then, instead of `consumer_group_offsets`, you need another table to represent the messages outbox. That table will be `consumer_messages`.

`consumer_messages` is best thought of as an outbox. It has all the messages – available and delivered/processing – for a given `consumer_name`. As you'll see, that means whenever you insert a message into `messages`, you should insert a corresponding `consumer_message` for each consumer into `consumer_messages`.

`consumer_messages` looks a lot like `messages` from the SQS implementation:

```
create table consumer_messages (
  id serial primary key,
  consumer_name text not null,
  message_seq text not null,
  not_visible_until timestamp,
  deliver_count integer not null default 0,
  last_delivered_at timestamp,
  inserted_at timestamp not null default now(),
  updated_at timestamp not null default now()
);

create index idx_consumer_messages_state_visibility on consumer_messages (consumer_name, not_visible_until, inserted_at);

create index idx_consumer_messages_seq on consumers_messages (message_seq);

create unique index uidx_consumer_name_seq on consumer_messages (consumer_name, message_seq);
```

`consumer_messages` does not contain any of the messages, it references the stream table `messages`.

Note I avoid a foreign key constraint to `messages` here. That can get very expensive as `messages` grow, affecting throughput. Instead, I'd suggest that if you delete messages, you should just manually clear them out from `consumer_messages` as well.

With this design, your inserts get a little heavier. Each insert into `messages` results in corresponding inserts into `consumer_messages`, one for each consumer:

```
-- single message insert version
with new_message as (
  insert into messages (key, data)
  values ($1, $2)
  returning seq
)
insert into consumer_messages (consumer_name, message_seq)
select unnest($3::text[]), new_message.seq
from new_message;
```

During upserts, your application passes in the list of consumer names it wants to fan out to (e.g. `['service1', 'service2']`) as `$3`. Now, consumers can process messages independent of one another.

The batch message version is a little more complicated:

```
-- batch message insert version
with new_messages as (
  insert into messages (key, data)
  select key, data
  from unnest($1::text[], $2::text[]) as t(key, data)
  returning seq, key
),
consumer_names as (
  select distinct unnest($3::text[]) as name
)
insert into consumer_messages (consumer_name, message_seq)
select 
  cn.name,
  nm.seq
from new_messages nm
cross join consumer_names cn;
```

This allows you to pass in a list of keys as `$1` and their corresponding datas as `$2`.

Receiving messages for a consumer is much like receiving messages in the SQS implementation. You just need to join against `messages` to get the message's `data`:

```
with available_messages as (
  select distinct on (m.key) cm.id, m.seq, m.key, m.data
  from consumer_messages cm
  join messages m on cm.message_seq = m.seq
  where cm.consumer_name = $1
    and (
      cm.not_visible_until is null or
      cm.not_visible_until <= now())
    )
  order by m.key, m.seq desc
  limit $2
  for update skip locked
)
update consumer_messages cm
set 
  not_visible_until = $3,
  deliver_count = deliver_count + 1,
  last_delivered_at = now(),
  updated_at = now()
from available_messages am
where cm.id = am.id
returning am.seq, am.key, am.data;
```

This design is missing a critical piece, though: how do you _add_ a new consumer to the system? You need to backfill `consumer_messages` with all `messages` for that consumer. The workflow:

1.  Ensure your system starts upserting messages for the new `consumer_name`.
2.  Run a process that upserts into `consumer_messages` up until some max `seq`. You'll want this process to overlap with inserts performed by #1, so on conflict `(consumer_messages, seq)` do `nothing`.

You can, of course, choose exactly what history the new consumer should process. It's trivial to have it only process the last 60 days of messages, for example.

With this simple design, you get a great, concurrent, and efficient blend of a Kafka stream and a FIFO SQS queue.

While the data model of this design is straightforward, you'll need to mitigate these downsides:

1.  You need a workflow to backfill `consumer_messages` every time you add a consumer to the system.
2.  There is no back pressure on `consumer_messages`. If a consumer is dormant (not processing messages), the queue of work for it to do will grow unbounded.

You can mitigate both these downsides independently. But you may be tempted to insert into `consumer_messages` just-in-time to avoid these downsides entirely. Let me convince you why this may not be a good idea.

### Deadend: Insert `consumer_messages` JIT

Can't you just insert into `consumer_messages` when the system _delivers_ a message and now needs to track its state?

A `consumer_message` will need to be inserted for every consumer + message combination _at some point_, so this method doesn't save you on write volume. However, it does save on storage volume. It keeps `consumer_messages` lean. And you don't need to backfill the table when you initialize a new consumer.

This seems simple enough, but actually turns out to be difficult to do.

This strategy requires a blend of an offset cursor (for pulling new messages from `messages`) and the `consumer_messages` table. Add a new table, `consumer_offsets`:

```
create table consumer_offsets (
  consumer_name text not null,
  seq bigint not null
);
```

Then, to receive a new batch of messages, consumers need to (1) grab available messages in `consumer_messages` i.e. delivered messages that are visible again because they were not acked. Then (2), if they have any more room in their requested `batch_size`, pull messages from `messages` into `consumer_messages`to round out their batch.

This is totally doable in a SQL query or function. However, `(2)` presents a bottleneck: **only one worker will be able to pull messages from `consumer_messages` at a time**. `consumer_offsets.seq` is a bottleneck. When one worker uses it to perform a pull from `consumer_messages`, it must lock it until its pull is complete. This means pretty much all consumers need to run in serial!

Furthermore, if you want to support FIFO delivery by `key`, things get even more complicated. You can't easily pull a message from `messages` into `consumer_messages` if a message with the same `key` is currently processing. You need to "halt" the offset progression and wait for the message with that `key` to be processed.

Sequin
------

[Sequin](https://sequinstream.com/?ref=blog.sequinstream.com)'s design takes after this last implementation: the benefits of a stream like Kafka, but with ergonomics closer to SQS.

After we built the initial version of what would become Sequin, we realized we wanted to take things even further. So we just kept building, and added abilities like:

*   You can create consumers that only process a subset of all messages in a stream.
*   You can easily rewind a consumer or replay messages into a consumer.
*   You can stream changes from any Postgres table into a stream.
*   You can use a CLI for managing streams, consumers, and for debugging.

[You can find all this on GitHub](https://github.com/sequinstream/sequin?ref=blog.sequinstream.com). The project is early, but the core feature set is coming together quickly. Let us know if there's anything else you'd like to see!

### Addendum: When to use functions vs big queries?

You'll note in this post I use big queries with CTEs instead of functions. I do this for two reasons:

Foremost, the really great part about using queries is that you don't need to worry about migrating them. With functions, you have to constantly run migrations to do `create or replace function...` on deploys. And this means older versions of your application that might still be running are immediately swapped over to the newer function, which may be undesirable.

With queries, you don't need to worry about migrations. And many great ORMs/Postgres clients will save queries as prepared statements on the server, so you don't need to worry about the overhead of sending the same query to the server over and over again.

Second, I think queries are a little easier to read than functions in a post like this.

You can always start out with queries, and then as your approach hardens move things over to functions if desired.
