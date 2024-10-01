Title: Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More

URL Source: https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html

Published Time: 2024-09-27T15:11:00-07:00

Markdown Content:
![An NYC restaurant grade certificant being hung.](https://www.dbreunig.com/img/restaurant_grade.png)

### An Intro to Matching Place Data on Your Laptop

One of the trickiest problems in geospatial work is _conflation_, combining and integrating multiple data sources that describe the same real-world features.

It sounds simple enough, but datasets describe features inconsistently and are often riddled with errors. Conflation processes are complicated affairs with many stages, conditionals, and comparison methods. Even then, humans might be needed to review and solve the most stubborn joins.

Today we’re going to demonstrate a few different conflation methods, to illustrate the problem. The following is written for people with data processing or analysis experience, but little geospatial exposure. We’re currently experiencing a bit of a golden age in tooling and data for the geo-curious. It’s now possible to quickly assemble geo data and analyze it on your laptop, using freely available and easy-to-use tools. No complicated staging, no specialized databases, and (at least today) no map projection wrangling.

Further, the current boom in LLMs has delivered open _embedding models_ – which let us evaluate the contextual similarity of text, images, and more. ([Last year I used embeddings to search through thousands of bathroom fauces for our remodel](https://www.dbreunig.com/2023/09/26/faucet-finder.html).) Embeddings are a relatively new tool in our conflation toolkit, and (as we’ll see below) deliver promising results with relatively little effort.

We’re going to attempt to join [restaurant inspection data from Alameda County](https://data.acgov.org/datasets/e95ff2829e9d4ea0b3d8266aac37ff14_0/) with places data from [the Overture Maps Foundation](https://overturemaps.org/), enabling us to visualize and sort restaurants by their current inspection score.

And – inspired by the [Small Data conference](https://data.acgov.org/datasets/e95ff2829e9d4ea0b3d8266aac37ff14_0/) I attended last week – we’ll do this all on our local machine, using DuckDB, Ollama, and a bit of Python.

Sections
--------

*   [Staging the Data](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#staging-the-data)
*   [Generating H3 Tiles](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#generating-h3-tiles)
*   [Method 1: Exact Name Matching](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#method-1-exact-name-matching)
*   [Method 2: String Similarity](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#method-2-string-similarity)
*   [Method 3: Embeddings](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#method-3-embeddings)
*   [Bringing It Together](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#bringing-it-together)

### Staging the Data

First up, getting the data and staging it where we can work on it. Alameda County has its own data website where it [hosts restaurant inspection records](https://data.acgov.org/datasets/e95ff2829e9d4ea0b3d8266aac37ff14_0/). We can see when it was updated (September 23rd, last week) and download the CSV. Go ahead and do that.

We need to get this CSV into a form where we can interrogate it and compare it to other datasets. For that, we’re going to use DuckDB. Let’s set up our database and load our inspections into a table:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

import duckdb

\# Create the database we'll save our work to and load the extensions we'll need

con \= duckdb.connect("conflation\_demonstration.ddb")

con.sql("install spatial")

con.sql("install httpfs")

con.sql("load spatial")

con.sql("load httpfs")

\# Load the CSV downloaded from the Alameda County site

con.sql("CREATE TABLE inspections AS SELECT \* FROM read\_csv('inspections\_092324.csv', ignore\_errors=True)")

Because we’ll need it later, I’m going to present all these examples in Python. But you could do most of this without ever leaving DuckDB.

Now we need to get Overture’s Places data. We don’t want the _entire_ global dataset, so we’ll compute a bounding box in DuckDB that contains our inspection records to filter our request. We’ll take advantage of the confidence score to filter out some lower-quality data points. Finally, we’ll transform the data to closely match our inspection records:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

\# Download the Overture Places data. There's a lot going on here, but what we're doing is...

\# 1. Create a bounding box around all the Alameda County records

\# 2. Get all the places from Overture in that bounding box, with a confidence score \> 0.5

\# 3. Finally transform these results into a format that matches the Alameda County Data

con.sql("""

CREATE TABLE IF NOT EXISTS places AS

WITH bounding\_box AS (

SELECT max(Latitude) as max\_lat, min(Latitude) as min\_lat, max(Longitude) as max\_lon, min(Longitude) as min\_lon

FROM inspections

)

SELECT

id,

upper(names\['primary'\]) as Facility\_Name,

upper(addresses\[1\]\['freeform'\]) as Address,

upper(addresses\[1\]\['locality'\]) as City,

upper(addresses\[1\]\['region'\]) as State,

left(addresses\[1\]\['postcode'\], 5) as Zip,

geometry,

ST\_X(geometry) as Longitude,

ST\_Y(geometry) as Latitude,

categories

FROM (

SELECT \*

FROM read\_parquet('s3://overturemaps-us-west-2/release/2024-09-18.0/theme=places/type=place/\*', filename=true, hive\_partitioning=1),

bounding\_box

WHERE addresses\[1\] IS NOT NULL AND

bbox.xmin BETWEEN bounding\_box.min\_lon AND bounding\_box.max\_lon AND

bbox.ymin BETWEEN bounding\_box.min\_lat AND bounding\_box.max\_lat AND

confidence \> 0.5

);

""")

We now have 56,007 places from overture and inspection reports for 2,954 foodservice venues.

![All the restaurants and places in our database.](https://www.dbreunig.com/img/all_restaurants.png)

Looks good, but the blue points (the Overture data) go much further east than our inspection venues. Our bounding box is rectangular, but our county isn’t. If we were concerned with performance we could grab the county polygon from [Overture’s Divisions](https://docs.overturemaps.org/guides/divisions/) theme, but for our purposes this is fine.

### Generating H3 Tiles

In each conflation method, the first thing we’ll do is collect match candidates that are near our input record. We don’t need to compare an Alameda restaurant to a listing miles away in Hayward. We could use DuckDB’s [spatial](https://duckdb.org/docs/extensions/spatial/overview.html) extension to calculate distances and filter venues, but it’s much easier to use a tile-based index system to pre-group places by region. Tile indexes aren’t perfect – for example, a restaurant could sit on the edge of tile – but for most matches they’ll work great.

We’re going to use [H3](https://h3geo.org/) to tile our venues, because it’s fast and it has a DuckDB community extension so we don’t even have to bounce back up to Python. (Also, I ran into \[Isaac Brodsky\]\[issac\], H3’s creator, at the Small Data conference. So it’s on theme!)

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

con.sql("INSTALL h3 FROM community")

con.sql("LOAD h3")

\# Add H3 indexs to each table

con.sql("ALTER TABLE places ADD COLUMN IF NOT EXISTS h3 uint64")

con.sql("ALTER TABLE inspections ADD COLUMN IF NOT EXISTS h3 uint64")

con.sql("UPDATE places SET h3 = h3\_latlng\_to\_cell(Latitude, Longitude, 7)")

con.sql("UPDATE inspections SET h3 = h3\_latlng\_to\_cell(Latitude, Longitude, 7)")

We’re now ready to try some matching. To sum up:

1.  We have two tables: `inspections` and `places`.
2.  Each has a `Facility_Name`, `Address`, `City`, `Zip`, `Longitude`, `Latitude`, and `h3` column. These columns have been converted to uppercase to facilitate comparisons.
3.  The Overture `places` table also has a `categories` column with primary and alternate categories. It might come in handy.
4.  The `inspections` table has a `Grade` column for each inspection, containing one of three values: `G` for green, `Y` for yellow, and `R` for red. Meaning ‘all good’, ‘needs fixes’, and ‘_shut it down_’ – respectively.

Let’s step through several different matching methods to illustrate them and better understand our data.

### Method 1: Exact Name Matching

We’ll start simple. We’ll walk through all the facilities in the inspection data and find places within the same H3 tile with exactly matching names:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

exact\_name\_match\_df \= con.sql("""

SELECT

i.Facility\_ID as fid, p.id as gers, i.Facility\_Name as i\_name, p.Facility\_Name as p\_name, i.Address, p.Address

FROM (

SELECT DISTINCT Facility\_Name, Facility\_ID, Address, h3

FROM inspections

) i

JOIN places p

ON i.h3 = p.h3

AND i.Facility\_Name = p.Facility\_Name

""").df()

Inspecting the results, we matched 930 facilities to places. About ~31%, not bad!

We included the address columns so that when we scan these matches (and you always should, when building conflation routines), we can see if the addresses agree. Out of our 930 matched records, 248 have disagreeing addresses – or 26%. Taking a look, we see two genres of disagreement:

1.  The `places` table doesn’t capture the unit number in the address field. For example, `BOB'S DISCOUNT LIQUOR` is listed as having an address of `7000 JARVIS AVE`, but has an address of `7000 JARVIS AVE #A` in the `inspection` data.

This isn’t a problem, for our use case. We’re still confident these records refer to the same business, despite the address mismatch.

1.  Chain restaurants – or other companies with multiple, nearby outlets – will incorrectly match with another location close enough to occur in the same H3 tile. For example, a “SUBWAY” at `20848 MISSION BLVD` is matched with a _different_ `SUBWAY` in the Overture data at `791 A ST`.

_This_ is a problem. We used a resolution of 7 when generating our H3 tiles, [each of which has an average area of ~5 km](https://h3geo.org/docs/core-library/restable/). Sure, we could try using a smaller tile, but I can tell you from experience that’s not a perfect solution. There are a _shocking_ amount of Subways (over 20,000 in the US alone!), and plenty of other culprits will spoil your fun[1](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#fn:bp).

We’ll need to solve this problem another way, without throwing out all the correctly matched venues from point 1 above.

### Method 2: String Similarity

To find very similar addresses, we’ll use [string distance functions](https://en.wikipedia.org/wiki/String_metric), which quantify the similarity of two strings. There are plenty of different distance funcitons, but we’re going to use [Jaro-Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) because it weights matching at the beginning of strings more highly – which well suits our missing address unit situation. And hey, [it’s built into DuckDB](https://duckdb.org/docs/sql/functions/char#text-similarity-functions)!

String distance functions produce a score, from 0 to 1, so we’ll have to figure out a good cut-off value. Let’s plot the distribution of the scores to get an idea:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

import matplotlib.pyplot as plt

df \= con.sql("""

SELECT

i.Facility\_ID as fid, p.id as gers, i.Facility\_Name as i\_name, p.Facility\_Name as p\_name, i.Address, p.Address, jaro\_winkler\_similarity(i.Address, p.Address) as similarity

FROM (

SELECT DISTINCT Facility\_Name, Facility\_ID, Address, h3

FROM inspections

) i

JOIN places p

ON i.h3 = p.h3

AND i.Facility\_Name = p.Facility\_Name

""").df()

\# Visualize the distribution of Jaro-Winkler Similarity (jws) scores

plt.figure(figsize\=(10, 4))

plt.hist(df\['similarity'\], bins\=40, color\='blue', edgecolor\='black')

plt.title('Distribution of Jaro-Winkler Similarity Scores')

plt.xlabel('Jaro-Winkler Similarity of Addresses')

plt.ylabel('Frequency')

plt.show()

Which produces:

![The distribution of similarity scores for addresses among venues whose names match exactly](https://www.dbreunig.com/img/jws_addresses_name_match.png)

This looks super promising. Cracking open the data we can see the low scores are catching the nearby chain pairs: Subway, McDonald’s, Peet’s Coffee, etc. There are a couple false negatives, but we can solve those with another mechanism. Everything above a score of 0.75 is perfect. So our query looks like:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

exact\_name\_match\_df \= con.sql("""

SELECT

i.Facility\_ID as fid, p.id as gers, i.Facility\_Name as i\_name, p.Facility\_Name as p\_name, i.Address, p.Address

FROM (

SELECT DISTINCT Facility\_Name, Facility\_ID, Address, h3

FROM inspections

) i

JOIN places p

ON i.h3 = p.h3

AND i.Facility\_Name = p.Facility\_Name

AND jaro\_winkler\_similarity(i.Address, p.Address) \> 0.75

""").df()

Which produces 903 matches we trust.

But what if we use Jaro-Winkler (JW) string distance to find very similar venue names, not just exact matches? Looking at the scores for similar names (where the venues share the same H3 tile and have addresses with a score of 0.75) we see the algo spotting the same venues, with slightly different names. For example, the `inspections` dataset often adds a store number to chain restaurants, like, `CHIPTLE MEXICAN GRILL #2389`. JW matches this strongly with `CHIPOTLE MEXICAN GRILL`. Everything above a score of 0.89 is solid:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

jws\_matches\_df \= con.sql("""

WITH ranked\_matches AS (

SELECT

i.Facility\_ID as fid, p.id as gers,

i.Facility\_Name as i\_name, p.Facility\_Name as p\_name,

i.Address, p.Address,

jaro\_winkler\_similarity(i.Facility\_Name, p.Facility\_Name) as name\_similarity,

jaro\_winkler\_similarity(i.Address, p.Address) as address\_similarity,

ROW\_NUMBER() OVER (

PARTITION BY i.Facility\_ID

ORDER BY jaro\_winkler\_similarity(i.Facility\_Name, p.Facility\_Name) DESC

) as rank

FROM (

SELECT DISTINCT Facility\_Name, Facility\_ID, Address, h3

FROM inspections

) i

JOIN places p

ON i.h3 = p.h3

AND jaro\_winkler\_similarity(i.Facility\_Name, p.Facility\_Name) \> 0.89

AND jaro\_winkler\_similarity(i.Address, p.Address) \> 0.75

)

SELECT

fid, gers, i\_name, p\_name, Address, address\_similarity, name\_similarity

FROM ranked\_matches

WHERE rank = 1

""").df()

This produces 1,623 confident matches, or 55%.

But looking at our potential matches, there are very few false positives if we extend our JW score to a threshold of 0.8, which would get us a 70% match rate. The problem is those errors are very tricky ones. For example, look at match candidates below:

Inspection Name

Overture Name

Name JW Score

Inspection Address

Overture Address

Address JW Score

BERNAL ARCO

BERNAL DENTAL CARE

0.87

3121 BERNAL AVE

3283 BERNAL AVE

0.92

BERNAL ARCO

ARCO

0.39

3121 BERNAL AVE

3121 BERNAL AVE

1

Jaro-Winkler scoring is poorly suited to these two names, missing the correct match because of the `BERNAL` prefix. Meanwhile, the addresses match close enough – despite being obviously different – allowing the first record to outrank the correct pair in our query above.

How might we solve this? There are a few approaches:

1.  **Gradually Zoom Out:** Use escalating sizes of H3 tiles to try finding matches very close to the input venue, before broadening our area of evaluation. (Though this would fail for the above example – they’re ~150 meters apart.)
2.  **Pre-Filter Categories:** Use the venue categories present in the Overture data to filter out places not relevant to our data. We could add “convenience\_store” and others to an allow list, filtering out `BERNAL DENTAL CARE`. (But this tactic would remove plenty of unexpected or edge case places that serve food, like an arena, school, or liquor store.)
3.  **Add conditionals:** For example, if an address matches exactly it outweighs the highest name match.

For fun[2](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#fn:fun), we’ll write up the last method. It works pretty well, allowing us to lower our JW score threshold to 0.83 and delivers 2,035, for a ~68% match rate. But those extra 13% of matches come at the cost of some [very nasty SQL](https://gist.github.com/dbreunig/77d8c991f596ae17a8732884e585a02d)!

This is why most conflation is done with multistage pipelines. Breaking out our logic into cascading match conditions, of increasing complexity achieves the same result and is much more legible and maintable. Further, it allows us to only use our most expensive methods of matching for the most stubborn records. Bringing us to our next method…

### Method 3: Embeddings

Also at the Small Data conference was [Ollama](https://ollama.com/), a framework for easily running LLMs on your local machine. We’re going to use it today to generate _embeddings_ for our venues. To follow along, you’ll need to:

1.  [Download and install Ollama](https://ollama.com/)
2.  Run `ollama pull mxbai-embed-large` in your terminal to download the model we’ll be using
3.  Install the [Ollama python library](https://github.com/ollama/ollama-python) with: `pip install ollama`.
4.  Finally, run `ollama serve` in your terminal to start the server.

The Python code we’ll write will hit the running Ollama instance and get our results.

[Vicki Boykis wrote my favorite embedding explanation](https://vickiboykis.com/what_are_embeddings/), but it’s a bit long for the moment. What we need to know here is that \[embeddings measure how contextually similar things are to each other\]\[embededings\], based on all the input data used to create the model generating the embedding. We’re using the `mxbai-embed-large` model here to generate embedding _vectors_ for our places, which are large arrays of numbers that we can compare.

To embed our places we need to format each of them as single strings. We’ll concatenate their names and address information, then feed this “description” string into Ollama.

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

import ollama

def get\_embedding(text):

return ollama.embeddings(

model\='mxbai-embed-large',

prompt\=text

)\['embedding'\]

inspections\_df \= con.sql("""

SELECT Facility\_ID as fid, concat(Facility\_Name, ',', Address, ',', City, ',', Zip) as description FROM inspections GROUP BY description, fid

""").df()

places\_df \= con.sql("""

SELECT id as gers, concat(Facility\_Name, ',', Address, ',', City, ',', Zip) as description FROM places GROUP BY description, gers

""").df()

\# Compute the embeddings

inspection\_string\_df\['embedding'\] \= inspection\_string\_df\['description'\].apply(lambda x: get\_embedding(x))

places\_df\['embedding'\] \= places\_string\_df\['description'\].apply(lambda x: get\_embedding(x))

We could store the generated embeddings in our DuckDB database (DuckDB has a [vector similarity search](https://duckdb.org/docs/extensions/vss.html) extension, btw), but for this demo we’re going to stay in Python, using in-memory dataframes.

The code here is simple enough. We create our description strings as a column in DuckDB then generate embedding values using our `get_embedding` function, which calls out to Ollama.

But this code is _slow_. On my 64GB MacStudio, calculating embeddings for ~3,000 inspection strings takes over a minute. This performance remains consistent when we throw ~56,000 places strings at Ollama – taking just shy of 20 minutes. Our most complicated DuckDB query above took only _0.4 seconds_.

(An optimized conflation pipeline would only compute the Overture place strings _during_ comparison if they didn’t already exist – saving us some time. But 20 minutes isn’t unpalpable for this demo. You can always optimize later…)

Comparing embeddings is much faster, taking only a few minutes (and this could be faster in DuckDB, but we’ll skip that since a feature we’d need here is [not production-ready](https://duckdb.org/docs/extensions/vss#persistence)). Without using DuckDB VSS, we’ll need to load a few libraries. But that’s easy enough:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://www.dbreunig.com/2024/09/27/%7B%7BrevealButtonHref%7D%7D)

from sentence\_transformers.util import cos\_sim

import numpy as np

import pandas as pd

def generate\_search\_embedding(text):

return ollama.embeddings(

model\='mxbai-embed-large',

prompt\=text

)\['embedding'\]

results\_df \= pd.DataFrame(columns\=\['i\_description', 'p\_description', 'fid', 'gers', 'h3', 'similarity\_score'\])

for index, row in inspection\_string\_df.iterrows():

\# Generate the candidate embeddings

candidate\_places \= places\_string\_df\[places\_string\_df\['h3'\] \== row\['h3'\]\]

sims \= cos\_sim(row\['embedding'\], candidate\_places\['embedding'\].tolist())

\# Find the highest ranking score and the associated row

max\_sim\_index \= sims.argmax().item()

max\_sim\_score \= sims\[0\]\[max\_sim\_index\].item()

highest\_ranking\_row \= candidate\_places.iloc\[max\_sim\_index\]

\# Print the results

\# Add results to the new DataFrame

new\_row \= pd.DataFrame({

'i\_description': row\['description'\],

'p\_description': highest\_ranking\_row\['description'\],

'fid': row\['fid'\],

'gers': highest\_ranking\_row\['gers'\],

'h3': row\['h3'\],

'similarity\_score': max\_sim\_score

}, index\=\[index\])

results\_df \= pd.concat(\[results\_df, new\_row\], ignore\_index\=True)

results\_df

Scrolling through the results, its quite impressive. We can set our embedding distance score to anything greater than 0.87 and get matches with no errors for 71% of inspection venues. Compare that to the 68% we obtained with our gnarly SQL query. The big appeal of embeddings is the simplicity of the pipeline. It’s dramatically slower, but we achieve a similar match performance with a _single_ rule.

And it’s pulling out some impressive matches:

*   `RESTAURANT LOS ARCOS,3359 FOOTHILL BLVD,OAKLAND,94601` matched with `LOS ARCOS TAQUERIA,3359 FOOTHILL BLVD,OAKLAND,94601`
*   `SOI 4 RESTAURANT,5421 COLLEGE AVE,OAKLAND,94618` matched with `SOI 4 BANGKOK EATERY,5421 COLLEGE AVE,OAKLAND,94618`
*   `HARMANS KFC #189,17630 HESPERIAN BLVD,SAN LORENZO,94580` matched with `KFC,17630 HESPERIAN BLVD,SAN LORENZO,94580`

It correctly matched our `BERNAL ARCO` from above with a score of 0.96.

The only issue we caught with high-scoring results were with _sub-venues_, venues that exist within a larger property. Like a hot dog stand in a baseball stadium or a restaurant in a zoo. But for our use case, we’ll let these skate by.

### Bringing It Together

String distance matches were fast, but embedding matches were easier. But like I said before: conflation jobs are nearly _always_ multistep pipelines. We don’t have to choose.

Bringing it all together, our pipeline would be:

1.  **DuckDB string similarity scores and some conditional rules:** Matching 2,254 out of 2,954. Leaving 800 to match with…
2.  **Embedding generation and distance scores:** Matching 81 out of the remaining 800.

With these two steps, we confidently matched 80% of our input venues – with a pretty generic pipeline! Further, by running our string similarity as our first pass, we’ve greatly cut down on our time spent generating embeddings.

Which in many cases is good enough! If you’re more comfortable with false positives, tweak some of the thresholds above and get above 90%, easily. Or spend a day coming up with more conditional rules for specific edge cases. But many of these venues simply don’t have matches. This [small Chinese restaurant in Oakland](https://www.google.com/maps/place/Lucky+Chef+Chen/@37.7759671,-122.2223303,3a,75y,54.47h,93.72t/data=!3m6!1e1!3m4!1scE2VhxKmxWY5E47P-IvQFQ!2e0!7i16384!8i8192!4m15!1m8!3m7!1s0x808f86f52520aca5:0x337b9f4f8eb505cc!2s3542+International+Blvd,+Oakland,+CA+94601!3b1!8m2!3d37.7760422!4d-122.2222009!16s%2Fg%2F11ggr9kbbw!3m5!1s0x808f86f525242bd1:0x5977720977e10eda!8m2!3d37.7760422!4d-122.2222009!16s%2Fg%2F1tj57_x6?coh=205409&entry=ttu&g_ep=EgoyMDI0MDkyNS4wIKXMDSoASAFQAw%3D%3D), for example, doesn’t exist in the Overture Places data. No conflation method will fix that.

![Mostly green, thankfully](https://www.dbreunig.com/img/inspections.png)

Our matched Overture places, colored by their most recent inspection rating. Mostly green, thankfully!

I was pleasantly surprised by the ease of embedding matching. There’s a lot to like:

*   **It’s easy to stand up:** All you have to know about your data is what columns you’ll join to generate the input strings. No testing and checking to figure out SQL condition statements. For small, unfamiliar datasets, I’ll definitely be starting with embeddings. Especially if I just need a quick, rough join.
*   **It matched 10% of the records missed by our complex SQL:** Even when we spent the time to get to know the data and create a few conditionals, embedding distances caught a significant amount of our misses. I can see it always being a final step for the stubborn remainders.
*   **The hardest part is first-time set-up:** Most of our time spent generating and comparing embeddings (besides compute time) was getting Ollama set up and finding a model. But Ollama makes that pretty easy and it’s a one-time task.
*   **There’s certainly room for improvement with embeddings:** I didn’t put much thought into picking an embedding model; I just grabbed the largest model in Ollama’s directory with ‘embedding’ in the name. Perhaps a smaller model, like `[nomic-embed-text][nomic]` performs just as well as `mxbai-embed-large`, in a fraction of the time. And these are both general models! Fine-tuning a model to match place names and their addresses could reduce our error rate significantly. And hey: get DuckDB VSS up and running and comparisons could get even faster…

Best of all: I ran this all on a local machine. The staging, exploration, and conflation were done with DuckDB, Ollama, H3, [Rowboat](https://rowboat.xyz/)[3](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html#fn:rowboat), [Kepler](https://kepler.gl/) (for visualization), and some Python. Aside from H3 and generating our bounding box for downloading our Overture subset, we didn’t touch any geospatial functions, reducing our complexity significantly.
