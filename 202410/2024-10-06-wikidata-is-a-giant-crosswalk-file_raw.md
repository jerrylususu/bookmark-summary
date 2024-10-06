Title: Wikidata is a Giant Crosswalk File

URL Source: https://www.dbreunig.com/2024/10/04/wikidata-is-a-giant-crosswalk-file.html

Published Time: 2024-10-04T08:43:00-07:00

Markdown Content:
![Image 1: The potential for many crosswalks](https://www.dbreunig.com/img/crosswalks.png)

### Building a Map Platform Join Table with DuckDB and Some Ruby

[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) is Wikipedia’s structuralist younger brother. It’s contents are seemingly exhaustive, but rather than readable articles, Wikidata expresses itself with _structured data_. Pick a subject and check out it’s page; it’s like reading the back of a baseball card for, well, anything.

And burried in those stats and metadata are _external IDs_: identifiers from other sites and systems, which we can use to grab more data and develop cross-platform applications. Wikidata has _thousands_ of ‘em.

Today we’re going to build a cross-walk table for _places_ (a topic [near and dear to my heart](https://www.dbreunig.com/2024/07/31/towards-standardizing-place.html)) that you can do with just DuckDB, a short Ruby script, and one hard-earned bash line.

If you want to follow along, [grab a recent JSON extract of the Wikidata corpus](https://www.wikidata.org/wiki/Wikidata:Database_download). But be aware: it’s just shy of 140 GB.

### Wrangling the Download

_Please_ do not extact the file you just downloaded. It’s big enough to potentially cause problems on your machine and will definately be unweildy. We need to break it down into chunks, so we can concurrently process it later.

Now Wikidata very helpfully [produces this file so each item is on it’s own line](https://doc.wikimedia.org/Wikibase/master/php/docs_topics_json.html).

_However_, for reasons unknown to me, they wrap these neatly separated rows with brackets (`[` and `]`) and add a comma to each line so it’s a valid, JSON array _containing 100+ million items_. So close, Wikidata. Please check out [JSON Lines](https://jsonlines.org/)…

We are not going to attempt to load a this massive array. Instead, we’re running this command:

```
zcat ../latest-all.json.gz | sed 's/,$//' | split -l 100000 - wd_items_cw --filter='gzip > $FILE.gz'
```

This hard-won line streams the uncompressed content into `sed`, which removes the trailing commas, then chunks the output into batches of 100,000 records which are finally gzipped into files.

Now we can use DuckDB!

```
SELECT count(*) FROM 'wd_items_*.jsonl.gz';
```

It takes a bit, but returns a count of ~107 million entities.

### Exploring the Wikidata Schema

Let’s look at a record to see what we’re dealing with:

```
COPY (select * from 'wd_items_*.jsonl.gz' limit 1) to 'sample_record.json';
```

This is the record for [Belgium](https://www.wikidata.org/wiki/Q31) and it’s a big one: 48,252 lines of formatted JSON. Let’s take a high-level tour of the entity structure:

*   There’s the basic, top-level values like `type`, `id`, and a timestamp noting when it was last modified.
*   The `labels` dictionary contains localized strings of the item’s name in many languages (Belgium has 323 labels). This dictionary uses a language code as a key (“en” for English, for example), which maps to a dictionary containing the localized value and a seemingly redundant langauge code. (I can’t figure out why the language code’s there twice! Let me know below, if you do.)
*   The `description` and `aliases` dictionary are similar in form to the `labels` dictionary, just with localized descriptions and aliases, respectively.
*   The `sitelinks` dictionary contains links to associated pages on other WikiMedia platforms. For example, [the English-langauge Wikiquote page for Belgium](https://en.wikiquote.org/wiki/Belgium).
*   But what we care about today is the `claims` dictionary…

Wikidata claims are a key-value system similar in nature to OpenStreetMaps’ [tag system](https://wiki.openstreetmap.org/wiki/Tags), and likley adopted for similar reasons. It’s a flexible, [folksonomic](https://en.wikipedia.org/wiki/Folksonomy) system that facillitates broad collaboration and diverse data elements. Wikidata claims can also join one element to another, and describe the relationship. For example, Belgium is `part of` the [European Union](https://www.wikidata.org/wiki/Q458). There can also be more than one claim of the same type: Belgiun is also `part of` the [Allies of the First World War](https://www.wikidata.org/wiki/Q215669), [Europe](https://www.wikidata.org/wiki/Q476033), and the [Low Countries](https://www.wikidata.org/wiki/Q8932)

The claims we’re after today are those describing an external IDs. Thankfully, they’re labeled clearly for us:

```
{
    "mainsnak": {
        "snaktype": "value",
        "property": "P7127",
        "datavalue": {
            "value": "belgium",
            "type": "string"
        },
        "datatype": "external-id"
    },
    "type": "statement",
    "qualifiers": null,
    "qualifiers-order": null,
    "id": "Q31$be99eedf-4d68-b90b-e95b-21438633aa8d",
    "rank": "normal",
    "references": null
}
```

This claim describes the [AllTrails](https://www.alltrails.com/) [ID](https://www.wikidata.org/wiki/Property:P7127) for [Belgium](https://www.alltrails.com/belgium). The `value` under `mainsnak` and `datavalue` is the AllTrails ID itself. The `property` under `mainsnak` is the claim identifier for AllTrails IDs. (And no, I don’t know why they’re named [snaks](https://www.mediawiki.org/wiki/Wikibase/DataModel#Snaks))

There are _214_ external ID claims for Belgium! Want the [Library of Congress](https://id.loc.gov/authorities/names/n80126041.html) number? Or how about the ID for the libraries of [Ireland](https://viaf.org/processed/N6Ivtls000316878), [Iceland](https://viaf.org/processed/UIY%7C000076881), or [Greece](https://koha.nlg.gr/cgi-bin/koha/opac-authoritiesdetail.pl?marc=1&authid=2020)? You can find stories about Belgium on [the BBC](https://www.bbc.com/news/topics/cz4pr2gdgrdt), [The Guardian](https://www.theguardian.com/world/belgium), or [C-SPAN](https://www.c-span.org/organization/belgium/19875/). Find all the videogames Belgium appears in on [Giant Bomb](https://www.giantbomb.com/wd/3035-254/) or find code tagged with `belgium` on [Github](https://github.com/topics/belgium).

Most interesting to me: geo identifiers like [OpenStreetMap](https://www.openstreetmap.org/node/1684793666), [Google Maps](https://www.google.com/maps/place/Belgium/@50.501038,4.4661,529159m/data=!3m2!1e3!4b1!4m6!3m5!1s0x47c17d64edf39797:0x47ebf2b439e60ff2!8m2!3d50.503887!4d4.469936!16zL20vMDE1NGo?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D), and [Who’s On First](https://spelunker.whosonfirst.org/id/85632997/) all have claims. And for many records, Apple Maps IDs are there too.

Today we’re going to build a giant crosswalk file for all the geographic entities on Wikidata.

Preparing the Entities
----------------------

Our folder full of gzipped JSONL files is good, but there’s a ton of metadata in there we don’t need and is in a more difficult format than necessary. We’ll use a small Ruby script to prep the data:
