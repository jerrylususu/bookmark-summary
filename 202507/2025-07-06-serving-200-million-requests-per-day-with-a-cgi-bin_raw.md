Title: Serving 200 million requests per day with a cgi-bin

URL Source: https://jacob.gold/posts/serving-200-million-requests-with-cgi-bin/

Published Time: 2025-07-03T20:14:46-07:00

Markdown Content:
In the early 2000s, we used to write a lot of [CGI](https://en.wikipedia.org/wiki/Common_Gateway_Interface) programs.

This was the primary way to make websites dynamic at the time. These CGI programs were usually written in Perl, but sometimes in C to increase performance.

The CGI mechanism is conceptually simple but powerful. When the web server receives an incoming request handled by a CGI script (e.g. `GET /~jakegold/cgi-bin/guestbook.cgi`), it:

1.   Sets up environment variables containing request metadata (HTTP headers, query parameters, request method, etc.)
2.   Spawns a new process to execute the CGI program
3.   Passes the request body (if any) to the program via stdin
4.   Captures the program’s stdout as the HTTP response
5.   Sends any error output from stderr to the error log

The CGI program reads the environment variables to understand the request, processes it, and writes an HTTP response to stdout, starting with headers.

One of the nice features of this is that the CGI program exits after handling a single request, so all of its file descriptors and memory are automatically freed by the operating system. This made the terrible code of the time run quite reliably.

The developer experience was excellent as well. Deploying a new version of your CGI program was just a matter of copying it to the `cgi-bin/` directory on your web server.

Hug of death
------------

Typical web servers of this time had 1-2 CPUs and 1-4 GB of memory.

Most web servers ran Apache, which would fork an `httpd` process for every connection, each of which took a significant amount of memory. This would limit the maximum concurrency to fewer than 100 connections in most cases.

This made it incredibly easy to [Slashdot](https://en.wikipedia.org/wiki/Slashdot_effect) a website just by linking to it from a popular site.

Modern servers
--------------

These days, we have servers with 384 CPU threads. Even a small VM can have 16 CPUs. The CPUs and memory are much faster as well.

Most importantly, CGI programs, because they run as separate processes, are excellent at taking advantage of many CPUs!

This got me curious about how fast CGI programs might run on relatively modern hardware. I ran these benchmarks on an older 16-thread AMD 3700X in my server closet.

I might try running them on something really large later.

Benchmarking results
--------------------

To run a benchmark of CGI on a modern system, I created a little CGI program and ran it under Apache and (just for fun) a custom Go `net/http` server. I used `plow` to make concurrent HTTP requests and measure the results.

I haven’t analyzed the results in much detail (I need to go to sleep), but the basic takeaway is that CGI is impressively fast on modern servers.

**Using CGI on modest hardware, it’s possible to serve 2400+ requests per second or 200M+ requests per day.**

It’s almost never going to be the best choice these days, but it’s definitely viable.

### `guestbook.cgi`

I quickly wrote a little [guestbook](https://en.wikipedia.org/wiki/Guestbook) program that could be used to allow visitors to leave comments at the bottom of a website.

It uses Go with SQLite and is about as simple as it can be while remaining realistic.

### The code

I pushed the code and Dockerfiles to GitHub, in case they’re helpful or interesting to anyone else.

[[https://github.com/Jacob2161/cgi-bin](https://github.com/Jacob2161/cgi-bin)](https://github.com/Jacob2161/cgi-bin)

```
package main

import (
    "database/sql"
    "fmt"
    "html/template"
    "log/slog"
    "net/http"
    "net/http/cgi"
    "os"

    _ "github.com/mattn/go-sqlite3"
)

const guestbookHTML = `<!DOCTYPE html><html><head><meta charset="utf-8"><title>Guestbook</title>
<style>body{font-family:sans-serif}form{margin-bottom:2em}textarea{width:100%;height:6em}</style>
</head><body><h2>Guestbook</h2>
<form method="post" action="{{.ScriptURL}}">
<label>Name:<br><input name="name" required></label><br>
<label>Message:<br><textarea name="message" required></textarea></label><br>
<button type="submit">Sign</button></form>
{{range .Entries}}<div><strong>{{.Name}}</strong> <em>{{.Created}}</em><p>{{.Message}}</p></div><hr>{{end}}
</body></html>`

type entry struct {
    Name    string
    Message string
    Created string
}

type page struct {
    ScriptURL string
    Entries   []entry
}

const (
    databaseFile = "/tmp/guestbook.db"
)

var (
    db        *sql.DB
    templates = template.Must(template.New("page").Parse(guestbookHTML))
)

func main() {
    _, err := os.Stat(databaseFile)
    createTable := os.IsNotExist(err)

    dsn := fmt.Sprintf("file:%s?_journal_mode=WAL&_synchronous=NORMAL&_busy_timeout=5000&_cache_size=10000", databaseFile)
    db, err = sql.Open("sqlite3", dsn)
    if err != nil {
        slog.Error("open database failed", "error", err)
        os.Exit(1)
    }
    db.SetMaxOpenConns(1)

    if createTable {
        if _, err = db.Exec(`
            CREATE TABLE guestbook(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                created DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX index_guestbook_created ON guestbook(created);
            CREATE INDEX index_guestbook_name ON guestbook(name);
            CREATE INDEX index_guestbook_message ON guestbook(message);
        `); err != nil {
            slog.Error("create table failed", "error", err)
            os.Exit(1)
        }
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        if r.Method == "POST" {
            signHandler(w, r)
        } else {
            listHandler(w, r)
        }
    })
    cgi.Serve(http.DefaultServeMux)
}

func listHandler(w http.ResponseWriter, r *http.Request) {
    rows, err := db.Query(`
        SELECT 
            name, message, created
        FROM
            guestbook
        ORDER BY
            created DESC
        LIMIT
            100
    `)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer rows.Close()

    var entries []entry
    for rows.Next() {
        var e entry
        if err = rows.Scan(&e.Name, &e.Message, &e.Created); err != nil {
            slog.Error("scan row failed", "error", err)
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        entries = append(entries, e)
    }
    if err = rows.Err(); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    scriptURL := r.URL.RequestURI()
    if scriptURL == "" {
        scriptURL = os.Getenv("SCRIPT_NAME")
    }

    data := page{
        ScriptURL: scriptURL,
        Entries:   entries,
    }

    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    if err := templates.Execute(w, data); err != nil {
        slog.Error("execute template failed", "error", err)
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
}

func signHandler(w http.ResponseWriter, r *http.Request) {
    if err := r.ParseForm(); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    name, msg := r.Form.Get("name"), r.Form.Get("message")
    if name == "" || msg == "" {
        http.Redirect(w, r, "/", http.StatusSeeOther)
        return
    }
    if _, err := db.Exec(`
        INSERT INTO
            guestbook (name, message)
        VALUES
            (?, ?)
    `, name, msg); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    redirectURL := r.URL.RequestURI()
    if redirectURL == "" {
        redirectURL = os.Getenv("SCRIPT_NAME")
    }
    http.Redirect(w, r, redirectURL, http.StatusSeeOther)
}
```

Benchmarking writes using Apache
--------------------------------

[![Image 1: cgi-bin writes Apache benchmark](https://jacob.gold/images/cgi-bin-performance-benchmark-apache-writes.png)](https://jacob.gold/images/cgi-bin-performance-benchmark-apache-writes.png)

```
jake@lab1:~$ plow \
  --method POST \
  --body "name=John+Carmack&message=Hello+from+id+software%21" \
  --content "application/x-www-form-urlencoded" \
  --concurrency 16 \
  --requests 100000 \
    http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi
Benchmarking http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi with 100000 request(s) using 16 connection(s).
@ Real-time charts is listening on http://[::]:18888

Summary:
  Elapsed      40.5s
  Count       100000
    3xx       100000
  RPS       2468.836
  Reads    0.509MB/s
  Writes   0.494MB/s

Statistics    Min     Mean    StdDev      Max   
  Latency   3.815ms  6.473ms  2.391ms  135.391ms
  RPS       1852.4   2468.33  133.46    2555.7  

Latency Percentile:
  P50        P75      P90      P95      P99      P99.9     P99.99 
  5.974ms  6.757ms  8.123ms  9.285ms  14.436ms  38.758ms  84.111ms

Latency Histogram:
  6.117ms   85451  85.45%
  7.311ms   10800  10.80%
  9.719ms    2951   2.95%
  16.576ms    636   0.64%
  32.873ms    121   0.12%
  49.686ms     26   0.03%
  64.236ms     11   0.01%
  98.211ms      4   0.00%
```

Benchmarking reads using Apache
-------------------------------

[![Image 2: cgi-bin reads Apache benchmark](https://jacob.gold/images/cgi-bin-performance-benchmark-apache-reads.png)](https://jacob.gold/images/cgi-bin-performance-benchmark-apache-reads.png)

```
jake@lab1:~$ plow \
  --method GET \
  --concurrency 16 \
  --requests 100000 \
    http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi
Benchmarking http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi with 100000 request(s) using 16 connection(s).
@ Real-time charts is listening on http://[::]:18888

Summary:
  Elapsed         51s
  Count        100000
    2xx        100000
  RPS        1959.026
  Reads    20.631MB/s
  Writes    0.166MB/s

Statistics    Min     Mean    StdDev     Max   
  Latency   4.733ms  8.16ms   1.981ms  31.142ms
  RPS       1400.67  1958.64  135.64   2164.44 

Latency Percentile:
  P50        P75      P90      P95       P99      P99.9     P99.99 
  7.659ms  8.535ms  9.789ms  13.716ms  15.605ms  17.946ms  22.223ms

Latency Histogram:
  7.164ms   52606  52.61%
  8.352ms   33022  33.02%
  10.08ms   10155  10.16%
  14.053ms   3046   3.05%
  15.03ms     704   0.70%
  15.899ms    365   0.37%
  17.223ms     89   0.09%
  20.196ms     13   0.01%
```

Benchmarking writes using Go net/http
-------------------------------------

[![Image 3: cgi-bin writes gohttpd benchmark](https://jacob.gold/images/cgi-bin-performance-benchmark-gohttpd-writes.png)](https://jacob.gold/images/cgi-bin-performance-benchmark-gohttpd-writes.png)

```
jake@lab1:~$ plow \
  --method POST \
  --body "name=John+Carmack&message=Hello+from+id+software%21" \
  --content "application/x-www-form-urlencoded" \
  --concurrency 16 \
  --requests 100000 \
    http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi
Benchmarking http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi with 100000 request(s) using 16 connection(s).
@ Real-time charts is listening on http://[::]:18888

Summary:
  Elapsed      36.4s
  Count       100000
    3xx       100000
  RPS       2742.432
  Reads    0.437MB/s
  Writes   0.549MB/s

Statistics    Min     Mean    StdDev      Max   
  Latency   2.981ms  5.825ms  3.882ms  113.286ms
  RPS       2263.09  2741.02   99.4     2819.35 

Latency Percentile:
  P50        P75      P90      P95      P99      P99.9     P99.99  
  5.012ms  6.091ms  7.879ms  9.707ms  22.914ms  58.042ms  108.861ms

Latency Histogram:
  5.456ms    94833  94.83%
  9.474ms     4330   4.33%
  21.782ms     627   0.63%
  38.597ms     152   0.15%
  66.833ms      38   0.04%
  97.435ms      13   0.01%
  109.886ms      6   0.01%
  112.707ms      1   0.00%
```

Benchmarking reads using Go net/http
------------------------------------

[![Image 4: cgi-bin reads gohttpd benchmark](https://jacob.gold/images/cgi-bin-performance-benchmark-gohttpd-reads.png)](https://jacob.gold/images/cgi-bin-performance-benchmark-gohttpd-reads.png)

```
jake@lab1:~$ plow \
  --method GET \
  --concurrency 16 \
  --requests 100000 \
    http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi
Benchmarking http://localhost:1111/~jakegold/cgi-bin/guestbook.cgi with 100000 request(s) using 16 connection(s).
@ Real-time charts is listening on http://[::]:18888

Summary:
  Elapsed       40.4s
  Count        100000
    2xx        100000
  RPS        2469.613
  Reads    25.921MB/s
  Writes    0.210MB/s

Statistics    Min     Mean    StdDev     Max   
  Latency   3.969ms  6.471ms  1.269ms  27.326ms
  RPS       2308.31  2469.49   41.47   2519.05 

Latency Percentile:
  P50        P75      P90     P95      P99      P99.9     P99.99 
  6.249ms  7.079ms  8.061ms  8.77ms  10.599ms  14.446ms  20.813ms

Latency Histogram:
  6.035ms   71273  71.27%
  7.346ms   25248  25.25%
  8.528ms    2674   2.67%
  10.116ms    655   0.66%
  12.33ms     114   0.11%
  17.163ms     31   0.03%
  22.546ms      4   0.00%
  27.326ms      1   0.00%
```

[Discuss on Hacker News](https://news.ycombinator.com/item?id=44464272)
