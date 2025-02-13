Title: URL-addressable Pyodide Python environments

URL Source: https://simonwillison.net/2025/Feb/13/url-addressable-python/

Markdown Content:
13th February 2025

This evening I spotted [an obscure bug](https://github.com/simonw/datasette/issues/2466) in [Datasette](https://datasette.io/), using [Datasette Lite](https://github.com/simonw/datasette-lite). I figure it’s a good opportunity to highlight how useful it is to have a URL-addressable Python environment, powered by Pyodide and WebAssembly.

Here’s the page that helped me discover the bug:

`[https://lite.datasette.io/?install=datasette-visible-internal-db&ref=1.0a17#/_internal/catalog_columns?_facet=database_name](https://lite.datasette.io/?install=datasette-visible-internal-db&ref=1.0a17#/_internal/catalog_columns?_facet=database_name)`

To explain what’s going on here, let’s first review the individual components.

*   [Datasette Lite](https://simonwillison.net/2025/Feb/13/url-addressable-python/#datasette-lite)
*   [The Datasette 1.0 alphas](https://simonwillison.net/2025/Feb/13/url-addressable-python/#the-datasette-1-0-alphas)
*   [This works for plugins, too](https://simonwillison.net/2025/Feb/13/url-addressable-python/#this-works-for-plugins-too)
*   [datasette-visible-internal-db](https://simonwillison.net/2025/Feb/13/url-addressable-python/#datasette-visible-internal-db)
*   [Spotting the bug](https://simonwillison.net/2025/Feb/13/url-addressable-python/#spotting-the-bug)
*   [Fixing the bug](https://simonwillison.net/2025/Feb/13/url-addressable-python/#fixing-the-bug)
*   [URL-addressable Steps To Reproduce](https://simonwillison.net/2025/Feb/13/url-addressable-python/#url-addressable-steps-to-reproduce)

#### Datasette Lite

[Datasette Lite](https://lite.datasette.io/) is a version of [Datasette](https://datasette.io/) that runs entirely in your browser. It runs on [Pyodide](https://pyodide.org/), which I think is still the most underappreciated project in the Python ecosystem.

I built Datasette Lite [almost three years ago](https://simonwillison.net/2022/May/4/datasette-lite/) as a weekend hack project to try and see if I could get Datasette—a server-side Python web application—to run entirely in the browser.

I’ve added a bunch of features since then, [described in the README](https://github.com/simonw/datasette-lite/blob/main/README.md)—most significantly the ability to load SQLite databases, CSV files, JSON files or Parquet files by passing a URL to a query string parameter.

I built Datasette Lite almost as a joke, thinking nobody would want to wait for a full Python interpreter to download to their browser each time they wanted to explore some data. It turns out internet connections are fast these days and having a version of Datasette that needs a browser, GitHub Pages and _nothing else_ is actually extremely useful.

Just the other day [I saw Logan Williams](https://bsky.app/profile/obtusatum.bsky.social/post/3lhyeuqmpns22) of Bellingcat using it to share a better version of [this Excel sheet](https://www.commerce.senate.gov/2025/2/cruz-led-investigation-uncovers-2-billion-in-woke-dei-grants-at-nsf-releases-full-database):

> The NSF grants that Ted Cruz has singled out for advancing “neo-Marxist class warfare propaganda,” in Datasette-Lite: [lite.datasette.io?url=https://...](https://lite.datasette.io/?url=https://data-house-lake.nyc3.cdn.digitaloceanspaces.com/cruz_nhs.db#/cruz_nhs/grants)

Let’s look at that URL in full:

`https://lite.datasette.io/?url=https://data-house-lake.nyc3.cdn.digitaloceanspaces.com/cruz_nhs.db#/cruz_nhs/grants`

The `?url=` parameter there poins to a SQLite database file, hosted on DigitalOcean Spaces and served with the all-important `access-control-allow-origin: *` header which allows Datasette Lite to load it across domains.

The `#/cruz_nhs/grants` part of the URL tells Datasette Lite which page to load when you visit the link.

Anything after the `#` in Datasette Lite is a URL that gets passed on to the WebAssembly-hosted Datasette instance. Any query string items before that can be used to affect the initial state of the Datasette instance, to import data or even to install additional plugins.

#### The Datasette 1.0 alphas

I’ve shipped _a lot_ of Datasette alphas—the most recent is [Datasette 1.0a17](https://docs.datasette.io/en/latest/changelog.html#a17-2025-02-06). Those alphas get published to [PyPI](https://pypi.org/), which means they can be installed using `pip install datasette==1.0a17`.

A while back [I added the same ability](https://github.com/simonw/datasette-lite/issues/75) to Datasette Lite itself. You can now pass `&ref=1.0a17` to the Datasette Lite URL to load that specific version of Datasette.

This works thanks to the magic of Pyodide’s [micropip](https://micropip.pyodide.org/) mechanism. Every time you load Datasette Lite in your browser it’s actually using `micropip` to install the packages it needs directly from PyPI. The code looks something like this:

await pyodide.loadPackage('micropip', {messageCallback: log});
let datasetteToInstall \= 'datasette';
let pre \= 'False';
if (settings.ref) {
  if (settings.ref \== 'pre') {
    pre \= 'True';
  } else {
    datasetteToInstall \= \`datasette==${settings.ref}\`;
  }
}
await self.pyodide.runPythonAsync(\`
import micropip
await micropip.install("${datasetteToInstall}", pre=${pre})
\`);

[Full code here](https://github.com/simonw/datasette-lite/blob/main/webworker.js).

That `settings` object has been passed to the Web Worker that loads Datasette, incorporating various query string parameters.

This all means I can pass `?ref=1.0a17` to Datasette Lite to load a specific version, or `?ref=pre` to get the most recently released pre-release version.

#### This works for plugins, too

Since loading extra packages from PyPI via `micropip` is so easy, I went a step further and added plugin support.

The `?install=` parameter can be passed multiple times, each time specifying a Datasette plugin from PyPI that should be installed into the browser.

The README includes [a bunch of examples](https://github.com/simonw/datasette-lite?tab=readme-ov-file#installing-plugins) of this mechanism in action. Here’s a fun one [that loads datasette-mp3-audio](https://lite.datasette.io/?install=datasette-mp3-audio&csv=https://gist.githubusercontent.com/simonw/0a30d52feeb3ff60f7d8636b0bde296b/raw/c078a9e5a0151331e2e46c04c1ebe7edc9f45e8c/scotrail-announcements.csv#/data/scotrail-announcements) to provide inline MP3 playing widgets, originally created for my [ScotRail audio announcements](https://simonwillison.net/2022/Aug/21/scotrail/) project.

This only works for some plugins. They need to be pure Python wheels—getting plugins with compiled binary dependencies to work in Pyodide WebAssembly requires a whole set of steps that I haven’t quite figured out.

Frustratingly, it doesn’t work for plugins that run their own JavaScript yet! I may need to rearchitect significant chunks of both Datasette and Datasette Lite to make that work.

It’s also worth noting that this is a remote code execution security hole. I don’t think that’s a problem here, because `lite.datasette.io` is deliberately hosted on the subdomain of a domain that I _never_ intend to use cookies on. It’s possible to vandalize the visual display of `lite.datasette.io` but it shouldn’t be possible to steal any private data or do any lasting damage.

#### datasette-visible-internal-db

This evening’s debugging exercise used a plugin called [datasette-visible-internal-db](https://pypi.org/project/datasette-visible-internal-db/).

Datasette’s [internal database](https://docs.datasette.io/en/latest/internals.html#datasette-s-internal-database) is an invisible SQLite database that sits at the heart of Datasette, tracking things like loaded metadata and the schemas of the currently attached tables.

Being invisible means we can use it for features that shouldn’t be visible to users—plugins that record API secrets or permissions or track comments or data import progress, for example.

In Python code it’s accessed like this:

internal\_db \= datasette.get\_internal\_database()

As opposed to Datasette’s other databases which are accessed like so:

db \= datasette.get\_database("my-database")

Sometimes, when hacking on Datasette, it’s useful to be able to browse the internal database using the default Datasette UI.

That’s what `datasette-visible-internal-db` does. The plugin implementation is [just five lines of code](https://github.com/datasette/datasette-visible-internal-db/blob/759e7001f91d3076d9f42eddb03fbaf6d1c7b9bb/datasette_visible_internal_db.py):

import datasette

@datasette.hookimpl
def startup(datasette):
    db \= datasette.get\_internal\_database()
    datasette.add\_database(db, name\="\_internal", route\="\_internal")

On startup the plugin grabs a reference to that internal database and then registers it using Datasette’s [add\_database() method](https://docs.datasette.io/en/latest/internals.html#add-database-db-name-none-route-none). That’s all it takes to have it show up as a visible database on the `/_internal` path within Datasette.

#### Spotting the bug

I was poking around with this today out of pure curiosity—I hadn’t tried `?install=datasette-visible-internal-db` with Datasette Lite before and I wanted to see if it worked.

Here’s [that URL from earlier](https://lite.datasette.io/?install=datasette-visible-internal-db&ref=1.0a17#/_internal/catalog_columns?_facet=database_name), this time with commentary:

```
https://lite.datasette.io/ // Datasette Lite
  ?install=datasette-visible-internal-db // Install the visible internal DB plugin
  &ref=1.0a17 // Load the 1.0a17 alpha release
  #/_internal/catalog_columns // Navigate to the /_internal/catalog_columns table page
  &_facet=database_name // Facet by database_name for good measure
```

And this is what I saw:

![Image 3: Screenshot of Datasette Lite. catalog_columns table has 382 rows. database_name facet shows content 237, fixtures 97, _internal 48. A table shows columns for Link, database_name, table_name, cid and name - a red arrow points to a hyperlinked _internal in the database_name column.](https://static.simonwillison.net/static/2025/datasette-lite-bug.jpg)

This all looked good... until I clicked on that `_internal` link in the `database_name` column... and it took me to [this /\_internal/databases/\_internal 404 page](https://lite.datasette.io/?install=datasette-visible-internal-db&ref=1.0a17#/_internal/databases/_internal).

Why was that a 404? Datasette introspects the SQLite table schema to identify foreign key relationships, then turns those into hyperlinks. The SQL schema for that `catalog_columns` table (displayed at the bottom of the table page) looked like this:

CREATE TABLE catalog\_columns (
    database\_name TEXT,
    table\_name TEXT,
    cid INTEGER,
    name TEXT,
    type TEXT,
    "notnull" INTEGER,
    default\_value TEXT, \-- renamed from dflt\_value
    is\_pk INTEGER, \-- renamed from pk
    hidden INTEGER,
    PRIMARY KEY (database\_name, table\_name, name),
    FOREIGN KEY (database\_name) REFERENCES databases(database\_name),
    FOREIGN KEY (database\_name, table\_name) REFERENCES tables(database\_name, table\_name)
);

Those foreign key references are a bug! I renamed the internal tables from `databases` and `tables` to `catalog_databases` and `catalog_tables` quite a while ago, but apparently forgot to update the references—and SQLite let me get away with it.

#### Fixing the bug

I fixed the bug [in this commit](https://github.com/simonw/datasette/commit/e59fd0175708f2b14d4e3c08ea16631bda0aaed3). As is often the case the most interesting part of the fix is [the accompanying test](https://github.com/simonw/datasette/blob/e59fd0175708f2b14d4e3c08ea16631bda0aaed3/tests/test_internal_db.py#L65-L84). I decided to use the introspection helpers in [sqlite-utils](https://sqlite-utils.datasette.io/) to guard against every making another mistake like this again in the future:

@pytest.mark.asyncio
async def test\_internal\_foreign\_key\_references(ds\_client):
    internal\_db \= await ensure\_internal(ds\_client)
    def inner(conn):
        db \= sqlite\_utils.Database(conn)
        table\_names \= db.table\_names()
        for table in db.tables:
            for fk in table.foreign\_keys:
                other\_table \= fk.other\_table
                other\_column \= fk.other\_column
                message \= 'Column "{}.{}" references other column "{}.{}" which does not exist'.format(
                    table.name, fk.column, other\_table, other\_column
                )
                assert other\_table in table\_names, message + " (bad table)"
                assert other\_column in db\[other\_table\].columns\_dict, (
                    message + " (bad column)"
                )
    await internal\_db.execute\_fn(inner)

This uses Datasette’s [await db.execute\_fn()](https://docs.datasette.io/en/latest/internals.html#await-db-execute-fn-fn) method, which lets you run Python code that accesses SQLite in a thread. That code can then use the blocking `sqlite-utils` [introspection methods](https://sqlite-utils.datasette.io/en/stable/python-api.html#introspecting-tables-and-views)—here I’m looping through every table in that internal database, looping through each tables `.foreign_keys` and confirming that the `.other_table` and `.other_column` values reference a table and column that genuinely exist.

I ran this test, watched it fail, then applied the fix and it passed.

#### URL-addressable Steps To Reproduce

The idea I most wanted to highlight here is the enormous value provided by **URL-addressable Steps To Reproduce**.

Having good Steps To Reproduce is crucial for productively fixing bugs. Something you can _click on_ to see the bug is the most effective form of STR there is.

Ideally, these URLs will continue to work long into the future.

The great thing about a system like Datasette Lite is that everything is statically hosted files. The application itself is hosted on GitHub Pages, and it works by loading additional files from various different CDNs. The only dynamic aspect is cached lookups against the PyPI API, which I expect to stay stable for a long time to come.

As a stable component of the Web platform [for almost 8 years](https://caniuse.com/wasm) WebAssembly is clearly here to stay. I expect we’ll be able to execute today’s WASM code in browsers 20+ years from now.

I’m confident that the patterns I’ve been exploring in Datasette Lite over the past few years could be just as valuable for other projects. Imagine demonstrating bugs in a Django application using a static WebAssembly build, archived forever as part of an issue tracking system.

I think WebAssembly and Pyodide still have a great deal of untapped potential for the wider Python world.
