Title: Immutable by Design: The Deep Tech Behind Tigris Bucket Forking | Tigris Object Storage

URL Source: https://www.tigrisdata.com/blog/bucket-forking-deep-dive/

Published Time: 2025-11-06T00:00:00.000Z

Markdown Content:
![Image 1: Pixel art of two copies of Ty from different timelines meeting up in the vast emptiness of space.](https://www.tigrisdata.com/blog/assets/images/absolutely-safe-capsule-4e7f2ca861aeeee58a8ae31aee70951d.webp)

_Pixel art of two copies of Ty from different timelines meeting up in the vast emptiness of space._
One of the coolest things about my job is picking apart how features were implemented so I can write these deep dives. A lot of Tigris features are implemented on koan-like primitives that lead to core lessons like:

*   Tigris implements snapshotting through representing time as a single 64 bit integer
*   Tigris implements bucket forking by making every object a write-ahead log and then doing recursive lookups in parent bucket snapshots
*   Tigris heavily abuses the fact that FoundationDB is inherently ordered by sorting times backwards

These lessons are small kernels of wisdom that take multiple thousands of words to fully unpack. Today, I’m going to break down everything involved with those three statements so that you can learn how Tigris exposes terabytes of data into new buckets in milliseconds.

Snapshots are time travel for state[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#snapshots-are-time-travel-for-state "Direct link to Snapshots are time travel for state")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Snapshots record the state of a bucket so that you can revisit that state in the future. One of the easiest ways to think about snapshots is via a list recording the changes to a TODO list:

History
-------

1.   11/4/2025, 4:05:59 PM 

Instead of just recording a value with all the TODOs in it, the snapshotting approach has you record the changes to that counter and set flags on events so you can get back to where the counter was at that point in time.

There’s a few ways to implement this, but for now let’s assume this is implemented as an write-ahead log: a data structure where the only event you’re allowed to take is appending new data on the end of it. This log typically includes the redo and undo information so that modifications can be undone or redone as administrative and replication needs demand.

### Write ahead logging is one of the core principles of distributed computing[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#write-ahead-logging-is-one-of-the-core-principles-of-distributed-computing "Direct link to Write ahead logging is one of the core principles of distributed computing")

As you can see, this effectively gives you the ability to travel in time to when changes were made so you can recover data, undo invalid data insertions, or make backups. This core idea is how [ZFS snapshots](https://docs.oracle.com/cd/E19253-01/819-5461/gbciq/index.html) work, and also [how git works](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).

ZFS internally represents its changelog as a list of changes made to an empty block storage device and use them to recreate what the contents of the disks at a point in time. Git is a list of patch files applied to an empty directory and uses those patches to recreate the state of your source code tree. If you need to read data at an earlier point in time (such as the state of a source code tree at a given git commit hash or tag), you can ask your git client to uncompute the changes needed to take you there.

This append-only model is super powerful, and you end up seeing it all over the computer science industry. It’s the backbone of how big-scale distributed systems like blockchains work. It’s the cornerstone of how paradigms like event sourcing and rollback netcode for multiplayer games serve millions of people daily.

One way to think about it is that the write-ahead log is the database, and anything else is just a cached view of that log to make queries more efficient.

However, this kind of point-in-time snapshotting is usually limited to database engines, block storage layers, filesystem layers, multiplayer game implementations, and message queues. There’s not really a good primitive like this in the object storage world. Most people see their object storage layer as their backup target, and as an industry we’ve accepted that you need to be very careful when modifying the contents of object storage because any change to mutable data could spell disaster.

We’re pretty sure that Tigris is the first S3-API compatible object storage service that allows you to make a snapshot of a bucket as it was at exactly one point in time and restore it.

-Wpedantic

Pedantically, [S3 has the concept of object versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), but it’s only at a per-object level. If you delete a versioned object without being very careful to delete only one version of that object, you lose all the data forever. And restoring to a point in time means checking and manipulating versions per object. Comparatively, Tigris snapshots and bucket forks mean that even if you “delete” data, you can still get it back by restoring the entire bucket to a prior state.

How Tigris implements snapshots for buckets[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#how-tigris-implements-snapshots-for-buckets "Direct link to How Tigris implements snapshots for buckets")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you [create a snapshot](https://www.tigrisdata.com/docs/sdks/tigris/snapshots-and-forks/#create-a-snapshot-from-the-bucket), Tigris computes a single numerical value:

Current Hex Time (Big‑Endian U64)
---------------------------------

Based on MAX_U64 - unix_nanos(UTC). Updates every second.

UTC now

2025-11-04T16:05:59.898Z

Hex value (16 hex chars / 8 bytes)

e78b26a026ca557f

Note: JavaScript dates are millisecond precision; nanoseconds are approximated by multiplying ms × 1,000,000.

That’s it. A snapshot is just a single 64 bit number. This number represents the number of nanoseconds since January 1, 1970 at midnight UTC. To understand how this lets you time travel in your buckets, let’s walk through how Tigris implemented changes to object metadata storage to support bucket forking. Once you see how it’s implemented for a single object, it’s pretty easy to understand how this extrapolates out to entire buckets with terabytes of data.

When you use a bucket with snapshotting and forking enabled, the keyspace (namespace for object keys) for objects in buckets looks something like this:

`bucket-name/object-name/version-id-timestamp`

Something important to keep in mind is that FoundationDB is an **ordered** key value store. That order is a crucially important part of this setup. As users manipulate objects, they could end up with potentially infinite numbers of versions. We [don’t ever want to sacrifice performance](https://www.tigrisdata.com/blog/benchmark-small-objects/), even if that sacrifice comes in the name of delivering features like snapshots and bucket forking. So, we use that inherent ordered property of FoundationDB to our advantage. Here’s how we calculate version IDs:

`func EncodeVersion(tm time.Time) []byte {    val := math.MaxUint64 - uint64(tm.UTC().UnixNano())    b := make([]byte, 8)    binary.BigEndian.PutUint64(b, val)    return b}`

This produces values like the following:

Hex Timestamps (Big‑Endian U64)
-------------------------------

Three static timestamps, each 3 days apart, shown out of order.

Out-of-order view: [T+6d, T, T+3d]

| Label | ISO (UTC) | Hex (u64, big‑endian) |
| --- | --- | --- |
| T+6d | 2025-11-10T16:05:59.899Z | e7894f24bee1133f |
| T | 2025-11-04T16:05:59.899Z | e78b26a026bb133f |
| T+3d | 2025-11-07T16:05:59.899Z | e78a3ae272ce133f |

Note: JavaScript dates are millisecond precision; nanoseconds are approximated by multiplying ms × 1,000,000.

The really cool part happens when you sort them. Each of these values is ordered such that as time increases, the value _decreases_. This backwards ordering means that the most recent timestamp will always be sorted to the top. So when the Tigris gateway goes in and asks for an object, it asks FoundationDB to return the value of the key that comes after `bucket-name/object-name`, and then whenever objects are created, updated, or deleted, Tigris creates a new version of the object metadata and inserts it on top of the existing object metadata. All the older versions of objects are neatly frozen in time.

This effectively turns each Tigris object into its own write-ahead log. Combine this with FoundationDB’s inherent ordering superpowers, and then you can read the snapshotted version of an object by querying for the newest timestamp that came before the snapshot.

![Image 2: Append-only log architecture showing immutable versions, snapshots as metadata pointers, and time-based reads](https://www.tigrisdata.com/blog/assets/images/append-only-log-502d7b7c2cc429eace9296c27c755412.svg)

So, yes, a snapshot really is just a single 64 bit integer representing the number of nanoseconds since January 1st, 1970 at midnight UTC. There’s some extra room in the database for things like human-readable descriptions, but that’s it. All you need is eight bytes representing time, then you can undelete objects.

Bucket forking backed by snapshots[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#bucket-forking-backed-by-snapshots "Direct link to Bucket forking backed by snapshots")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To be completely honest, we could have just called it a day and shipped the feature after implementing this per-object versioning and been fine. We would have already been ahead of the curve, but if we already have these point in time snapshots and inherent versioning on a per-object level, we can take things just that little step further and make this a revolutionary new feature instead of an evolution of features other providers have.

How can we take full advantage of these snapshots and put this to practical use? Well, you implement the ability to fork the timeline.

When we talk about time, our timespeak tends to assume that we're operating on a linear scale of time where events in the past happen "before" events in the present. Events then become fixed points on that line, for example:

![Image 3: A linear scale between January 1970 and January 2038, representing a linear scale of time. Several events are denoted: The release of Super Mario Brothers, the release of the Go programming language, and October 2025](https://www.tigrisdata.com/blog/assets/images/timeline-03039581a29dd786d11b1483f8118826.svg)

### Time in code[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#time-in-code "Direct link to Time in code")

However, when we talk about code, a lot of the time we end up explicitly modeling a system where this timeline can fork and diverge. Let’s consider Go’s infamous `if err != nil` problem:

`fout, err := os.Create("foo.txt")if err != nil {  panic(err)}if _, err := fout.Write([]byte("Hello, world!\n")); err != nil {  panic(err)}if err := fout.Close(); err != nil {  panic(err)}`

If you model this out in a timeline, it could look like this:

Every single thing that can fail creates a "fork" in the timeline for when it does fail. This basic idea is how we handle bucket forking. When you create a new bucket forked out of an existing snapshot, you basically create a new timeline for that bucket that diverges from the bucket’s old timeline:

![Image 4: Timeline of bucket forks diverging from source](https://www.tigrisdata.com/blog/assets/images/forking-timeline-a98bb25671b572893f3148bda7d8440a.svg)

So if every object in a forkable bucket is effectively a write-ahead log, then you can implement temporal divergence just by adding a layer of recursive indirection to object lookups.

When you modify data in a forked bucket, that new data is inserted into the child bucket just like any other object. When the service notices that the child bucket doesn’t have anything in it, it just checks for objects in the parent bucket snapshot. If that doesn’t have anything in it, it recurses until it finds something (even a tombstone marking that the object was deleted) or it returns a “not found” error when there’s nowhere else to check.

![Image 5: Diagram of a Source Bucket and Forked Bucket showing data prior to the fork is read from Source Bucket, and data after the fork is read from the Forked Bucket](https://www.tigrisdata.com/blog/assets/images/forked-bucket-fbb3fbf8d71848e9d05490bcdb6ae6a4.svg)

This is how Tigris is able to fork terabytes of data into a new bucket instantly. A 64 bit number is all you need.

Snapshots are free[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#snapshots-are-free "Direct link to Snapshots are free")
---------------------------------------------------------------------------------------------------------------------------------------

This all adds up to making snapshots essentially free at implementation on our end. Every bucket is copy-on-write. If data is deleted, a tombstone is left in its place. This also lets you delete data in child buckets all you want without affecting the source bucket in the slightest.

Consider this code:

`import { createBucket, createBucketSnapshot, put } from "@tigrisdata/storage";// Create a seed bucketconst seedBucketName = "agent-seed";await createBucket(seedBucketName, {  enableSnapshot: true,});// Put some data in itput("hello.txt", "Hello, world!", {  config: {    bucket: seedBucketName,  },});// Create snapshotconst snapshot = await createBucketSnapshot(seedBucketName, {  name: "agent-seed-v1",});const snapshotVersion = snapshot.data?.snapshotVersion;// Fork the bucket from the snapshot for a new agentconst agentBucketName = `${seedBucketName}-agent-${Date.now()}`;const forkResult = await createBucket(agentBucketName, {  sourceBucketName: seedBucketName,  sourceBucketSnapshot: snapshotVersion,});if (forkResult.data) {  // Start the agent using the forked bucket  await startAgent(agentBucketName);}`

This code puts 4 values into a bucket, takes a snapshot, and then forks a new bucket from that snapshot. From here, you can do whatever you want to the forked bucket without hurting the data in the parent bucket.

Consider this code:

`import { remove } from "@tigrisdata/storage";remove("hello.txt",  config: {    bucket: agentBucketName,  },)`

Now the forked bucket is empty. But, since the forked bucket comes from a snapshot of the source bucket, we can still view the data in the source bucket when sending a GET operation to the forked bucket:

`import { get } from "@tigrisdata/storage";const [data, err] = get("hello.txt", "string",  config: {    bucket: seedBucketName,  },);if (err !== undefined) {  throw err;}console.log(data)`

You can avoid entire categories of threats and collisions by handing out data via forks of your source buckets instead of the raw buckets themselves. Your AI agents, training workflow experiments, and other tools can work fearlessly, without the ability to mutate the source. Even if they go completely off the rails and delete everything, nothing is truly lost. The data is still accessible in the source bucket, and in any snapshots.

Object storage with deletion protection[​](https://www.tigrisdata.com/blog/bucket-forking-deep-dive/#object-storage-with-deletion-protection "Direct link to Object storage with deletion protection")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In conclusion, snapshots and forks give your data durable survivability even if you accidentally delete it. Though this level of durability represents a huge change in how Tigris works under the hood, we stand by the same guarantees about durability (99.999999999%), [availability](https://www.tigrisdata.com/blog/availability-metrics-public/) (99.99%), and [performance](https://www.tigrisdata.com/blog/benchmark-small-objects/) (forking fast!) for all buckets, including forks.

The following caveats apply at the time of writing:

*   Existing buckets cannot be snapshot-enabled yet. You must create a new snapshot-enabled bucket and migrate the data.
*   All snapshot-enabled buckets must be in the [Standard storage tier](https://www.tigrisdata.com/docs/objects/tiers/#standard-tier).
*   Snapshot-enabled buckets don’t support [storage tier lifecycle transitions](https://www.tigrisdata.com/docs/buckets/object-lifecycle-rules/) or [object time-to-live (auto-deletion)](https://www.tigrisdata.com/docs/buckets/settings/#ttl-configuration) yet.
*   Our model of time storage only really lasts until 2550 or thereabouts.

We’re pretty confident that future generations will be up to the task of transitioning us to 128 bit unix nanoseconds or whatever temporal reference format we’ll end up using. As for the rest, that’s where you come in. How are you using this? How do you like it? What features should we build next?

Keep following us on our socials and we’ll keep you posted for when we announce our next big thing!

Fork buckets like you fork code
-------------------------------

Ready to try immutable snapshots and forks?