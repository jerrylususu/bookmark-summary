Title: Leader Election With S3 Conditional Writes

URL Source: https://www.morling.dev/blog/leader-election-with-s3-conditional-writes/

Published Time: 2024-08-26T09:15:00+01:00

Markdown Content:
In distributed systems, for instance when scaling out some workload to multiple compute nodes, it is a common requirement to select a _leader_ for performing a given task: only one of the nodes should process the records from a Kafka topic partition, write to a file system, call a remote API, etc. Otherwise, multiple workers may end up doing the same task twice, overwriting each other’s data, and worse.

One way to implement [leader election](https://aws.amazon.com/builders-library/leader-election-in-distributed-systems/) is distributed locking. All the nodes compete to obtain a specific lock, but only one of them can succeed, which will then be the selected leader for as long as it holds that lock. Systems like [Apache ZooKeeper](https://zookeeper.apache.org/doc/current/recipes.html#sc_recipes_Locks) or Postgres (via [Advisory Locks](https://jeremydmiller.com/2020/05/05/using-postgresql-advisory-locks-for-leader-election/)) provide the required building blocks for this.

Now, if your application solely is in the business of writing data to object storage such as Amazon S3, Google Cloud Storage, or Azure Blob Storage, running such a stateful service solely for the purposes for leader election can be an overhead which you’d like to avoid from an operational as well as financial perspective. While you could implement distributed locks on the latter two platforms for quite a while with their respective compare-and-swap (CAS) operations, this [notoriously was not the case for S3](https://materializedview.io/p/s3-is-showing-its-age). That is, until last week, when [AWS announced support](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/) for conditional writes on S3, which was received with great excitement by many folks in the data and distributed systems communities.

In a nutshell, the S3 `PutObject` operation now supports an optional [`If-None-Match` header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html#conditional-writes). When specified, the call will only succeed when no file with the same key exists in the target bucket yet; otherwise you’ll get a `412 Precondition Failed` response. Compared to what’s available on GCP and Azure, that’s rather limited, but it’s all you need for implementing a locking scheme for leader election.

The Algorithm
-------------

The basic idea is to have nodes compete on creating a lock file, with the winner being the leader. As S3 conditional writes don’t prevent lost updates to existing files, a new lock file will be created for each leader _epoch_, i.e. when leadership changes either after a node failure or when the leader releases the lock voluntarily. The lock file can be a simple JSON structure like this:

```
1
2
3
{
  "expired" : false
}
```

The `expired` attribute is used for releasing a lock after use (more on that below). The leader epoch, a strictly increasing numeric value, is part of the file name, e.g. _lock\_0000000001.json_. This allows you to determine the current epoch by listing all lock files and finding the one with the highest epoch value (all lock files but the latest one can be removed by a background process, thus keeping the cost for the listing call constant).

Here’s the overall leader election algorithm:

```
1. List all lock files
2. If there is no lock file, or the latest one has expired:
   3. Increment the epoch value by 1 and try to create a new lock file
   4. If the lock file could be created:
      5. The current node is the leader, start with the actual work
   6. Otherwise, go back to 1.
7. Otherwise, another process already is the leader, so do nothing.
   Go back to 1. periodically
```

Obtaining the Lock
------------------

To obtain the lock (step 3.), put a file for the next epoch. The key thing is to pass the `If-None-Match` header and handle the potential `412 Precondition failed` response. Using the AWS Java SDK, this could look like so:

```
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
17
18
19
20
21
22
23
24
int epoch = ...;

PutObjectRequest put = PutObjectRequest.builder()
  .bucket(BUCKET)
  .key("lock-%010d.json".formatted(epoch))
  .ifNoneMatch("*")
  .build();

try {
  s3.putObject(put, RequestBody.fromString("""
      {
        "expired": false
      }
      """));
}
catch(S3Exception e) {
  if (e.statusCode() == 412) {
    //handle elsewhere and start over
    throw new LockingFailedException();
  }
  else {
    throw e;
  }
}
```

If you receive a 412 response, this means another process created the lock file since between you’ve listed the existing locks and now. That way, it is guaranteed that only one process succeeds to create the lock for the current epoch and thus becomes the leader.

Expiring a Lock
---------------

At some point, the current leader may decide to step down from this role, for instance when gracefully shutting down. This is as simple as setting the `expired` attribute to `true` and update the current lock file:

```
1
2
3
{
  "expired" : true
}
```

When other nodes list the existing lock files subsequently, they’ll see that the lock has expired and thus a new leader needs to be elected. Note that only ever that process which created the lock file for a given epoch may expire it, otherwise chaos may ensue. Naturally, this brings up the question of what happens when a leader never expires its lock, such as when it crashes. In that case, no new leader could ever be elected without manual intervention, hampering the liveness of the system.

Lock Validity
-------------

To address this situation, you can add another attribute to the lock file format, defining for how long it should be valid:

```
1
2
3
4
{
  "validity_ms" : 60000,
  "expired" : false
}
```

In this example, the lock should be valid for 60 seconds. For each file, S3 provides the last modification timestamp, specifying when it has been created or updated. When performing its work, the current leader needs to check whether the lock is still valid (i.e. have less than 60 seconds passed since the lock was obtained), optionally touching the file in order to extend the lease. Similarly, current non-leader nodes can check whether the latest lock is still valid or not.

What about clock drift though? After all, you never should rely on clock accuracy of different nodes when building distributed systems. But the good news is, you don’t have to. Let’s discuss the different options. If the current leader’s clock is ahead, it will stop doing its work, despite the lock still being valid. Similarly, if the clock of a current non-leader is behind, it may not try to acquire leadership although the current lock already has expired. While this may impact throughput of the system, both cases are not a correctness problem.

Things look different if the current leader relies on a lock after it has expired (because its clock is behind) and another leader has been elected already, or if a non-leader determines prematurely that the current lock has expired (because its clock is ahead) and thus picks up leadership.

In both cases, there’s more than one node which assumes to be the leader, which is exactly what we want to avoid with leadership election. But as it turns out, this is just the nature of the beast: leader election [will only ever be eventually correct](https://ocheselandrei.github.io/2022/06/01/leader-election-vs-consensus.html). As Martin Kleppmann describes in [this excellent post](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html), checking lock validity and performing the leader’s actual work is not atomic, no matter how hard you try (for instance, think of unexpected GC pauses). So you’ll always need to be prepared to detect and fence off work done by a previous leader.

<table><tbody><tr><td><i title="Note"></i></td><td><p>Minimizing Clock Drift</p><p>While you never should rely on clock consistency across systems from a correctness point of view, it does make sense to keep clocks synchronous on a best-effort basis, thus reducing the aforementioned throughput impact. To do so, nodes could create a temporary file on S3 and compare its creation time on S3 with their local time. Alternatively, you could use the Amazon Time Sync Service, which <a href="https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-time-sync-service-microsecond-accurate-time/">offers micro-second time accuracy</a>.</p></td></tr></tbody></table>

Fencing Off Zombies
-------------------

As a solution, Kleppmann suggests using the leader epoch as a fencing token. The epoch value only ever increases, so it can be used to identify requests by a stale leader ("zombie"). When for instance invoking a remote API, the fencing token could be passed as a request header, allowing the API provider to recognize and discard zombie requests by keeping track of the highest epoch value it has seen. Of course this requires the remote API to support the notion of fencing tokens, which may or may not be the case.

As an example targeting S3 (which doesn’t have bespoke support for fencing tokens), [SlateDB](https://github.com/slatedb/slatedb) implements this by [uploading files following a serial order](https://github.com/slatedb/slatedb/blob/main/docs/0001-manifest.md) (similar to the lock file naming scheme above) and detecting conflicts between competing writers trying to create the same file. Thanks to the new support for conditional writes on S3, this task is trivial, not requiring any external stateful services any longer.
