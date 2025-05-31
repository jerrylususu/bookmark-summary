Title: TIL: timeout in Bash scripts | Heitor's log

URL Source: https://heitorpb.github.io/bla/timeout/

Markdown Content:
The other day at work we had a Bash script that would set up a web server and wait for it to be up before proceeding to the next things. The script worked fine and we had no issues, until we had an infinite loop.

[![Image 1: Airplane Tracks](https://live.staticflickr.com/1908/30622866477_d147a6f3fc_z.jpg)](https://www.flickr.com/photos/heitorpb/30622866477/ "Airplane Tracks")
We were using the Bash built-in `until` to check if the web server was up:

```
until curl --silent --fail-with-body 10.0.0.1:8080/health; do
	sleep 1
done
```

This works fine. Unless our web server crashes during startup and we `sleep 1` forever.

Here comes a handy utility: `timeout`. As the name suggests, this command adds a timeout to other commands. You specify the time limit you want to wait for a command and if that time passes, `timeout` sends a signal to terminate it and exits with non-zero. By default, `timeout` sends `SIGTERM`, but you can change it with the `--signal` flag, e.g. `timeout --signal=SIGKILL 1s foo`.

For example, `timeout 1s sleep 5` will send the `SIGTERM` signal to `sleep` after 1 second:

```
$ time timeout 1s sleep 4

real    0m1,004s
user    0m0,000s
sys     0m0,005s

$ echo $?
124
```

The natural thing to do then is to combine `timeout` and `until`:

```
timeout 1m until curl --silent --fail-with-body 10.0.0.1:8080/health; do
	sleep 1
done
```

The only issue is that this doesn’t work. `timeout` expects a killable command and `until` is a shell keyword: you can’t `SIGTERM``until`. We can’t use `timeout` with any shell built-in.

The way forward is to wrap that `until` in a Bash process:

```
timeout 1m bash -c "until curl --silent --fail-with-body 10.0.0.1:8080/health; do
	sleep 1
done"
```

Another approach is to move the `until` to a separate Bash script and `timeout` it:

```
timeout 1m ./until.sh
```

It’s a shame we can’t use `timeout` with `until` directly, that would be amazing. But wrapping it in a Bash process/script gets the job done.

Discussion on [HackerNews](https://news.ycombinator.com/item?id=44096395).
