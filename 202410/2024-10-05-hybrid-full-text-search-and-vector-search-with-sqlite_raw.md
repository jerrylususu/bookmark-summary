Title: Hybrid full-text search and vector search with SQLite

URL Source: https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html

Markdown Content:
* * *

The primary use-case for `sqlite-vec` and other vector search tools is to offer "semantic search" to text data. Full-text search (aka keyword search) alone doesn't always give great results — Queries like "climate change" won't return documents that say "global warming," or "reproductive rights" won't return documents about "abortion bans." Semantic search allows you to lookup results by "vibes," returning richer results with more meaning.

But using "semantic search" as your **only** search method can be harmful to your applications. Take this tweet as an example:

> _fun fact: on the "max" app, you have to scroll through 32 results to find "adventure time" despite typing it in exactly how its spelled. the first result is rick and morty_ [`@boygrrI` Aug 27, 2023](https://x.com/boygrrI/status/1696029804770771123)
> 
> ![Image 1](https://blog-static.alxg.xyz/F4mCHdpWsAAntlt.jpeg)

Why would searching "adventure time" on HBO Max not return the actual (and amazing) [Adventure Time](https://www.max.com/shows/adventure-time/fff09eaf-17c3-446b-be32-8a0d47e4ccf1) TV show as the first result, and instead return 30 other shows first?

Forgetting the actual "Adventure Time" TV Show, the query "'adventure time" could mean many different things. Rick and Morty has interdimensional adventures, Aqua Teen Hunger Force has ["surreal adventures"](https://en.wikipedia.org/wiki/Aqua_Teen_Hunger_Force#:~:text=is%20about%20the-,surreal%20adventures,-and%20antics%20of). Who's to say a user doesn't want to see recommendations like that in their general "adventure time" search?

Then again, when you search "adventure time", then the "Adventure Time" TV show should be the first result. This is the push and pull of vector search and keyword search: vector search gives you a more fuzzy recommendations-like search experience, while keyword search is the obvious answer much of the time. Both are important, so how do you juggle both?

SQLite has had keyword or "full text" search for over a decade, in the form of the [FTS5 extension](https://www.sqlite.org/fts5.html), which drives search applications [or billions](https://www.sqlite.org/mostdeployed.html) of devices every single day. We can combine this battle-tested SQLite keyword search with the new [`sqlite-vec`](https://github.com/asg017/sqlite-vec) vector search extension to offer easy-yet-configurable hybrid search, which can run on the command line, on mobile devices, Raspberry Pis, and even web browsers with WASM!

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#the-demo-nbc-news-headlines) The demo: NBC News Headlines
----------------------------------------------------------------------------------------------------------------------------------

We're gonna work with a dataset of news headlines, scraped from [the NBC News sitemaps](https://www.nbcnews.com/archive/articles/2024/march). This subset contains 14,500+ headlines from January 2024 to August 2024 totaling `4.3MB` of text data, a very small dataset.

Here's a sample of what's in the `articles` table:

```
┌────┬──────┬───────┬──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ id │ year │ month │ headline                                                                                             │
├────┼──────┼───────┼──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  1 │ 2024 │     1 │ Washington state faces first outbreak of a deadly fungal infection that's on the rise in the U.S.    │
│  2 │ 2024 │     1 │ Israel-Hamas war live updates: U.S. readies weeks of retaliatory strikes against Iran-linked targets │
│  3 │ 2024 │     1 │ House to vote on an expanded child tax credit bill                                                   │
│  4 │ 2024 │     1 │ Travel costs, staff and ads added up before Ron DeSantis dropped out                                 │
│  5 │ 2024 │     1 │ Victims of Hamas attack in Israel and their families blame Iran in new federal lawsuit               │
│  6 │ 2024 │     1 │ Trump meets with Teamsters as he targets Biden support                                               │
│  7 │ 2024 │     1 │ The bipartisan border deal would not allow 5,000 illegal crossings per day, despite what Trump says  │
│  8 │ 2024 │     1 │ Machu Picchu tourism suffering after week of protests against new ticketing system                   │
│  9 │ 2024 │     1 │ FCC moves to criminalize most AI-generated robocalls                                                 │
│ 10 │ 2024 │     1 │ Civil rights group says N.C. public schools are harming LGBTQ students, violating federal law        │
└────┴──────┴───────┴──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Now let's build a FTS5 index and vector index with the text inside `headline` column. We will do this with `fts5` and `vec0` virtual tables. The different "combination" methods described later use these two virtual tables, and just use different algorithms/approaches to join + order the data.

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#building-the-full-text-search-fts-5-table) Building the full-text search FTS5 table
------------------------------------------------------------------------------------------------------------------------------------------------------------

We can create, seed, and optimize a `fts_headlines` full-text search virtual table from the base `articles` table with a few SQL statements:

```
create virtual table fts_articles using fts5(
  headline,
  content='articles', content_rowid='id'
);

insert into fts_articles(rowid, headline)
  select rowid, headline
  from articles;

insert into fts_articles(fts_articles) values('optimize');
```

We define the `fts_headline` virtual table, declaring the `headline` column and defining the `content=` and `content_rowid=` options to configure an [external content table](https://www.sqlite.org/fts5.html#external_content_tables). This will save some space, signaling the `FTS5` extensions to not store the headline `TEXT` and only store the FTS index, since we can join back to the `articles` table to retrieve the `headline` contents.

After that's declared, we can `INSERT INTO` directly into the `fts_headline` table from the base `articles` table. The [`'optimize'`](https://www.sqlite.org/fts5.html#the_optimize_command) command won't help much for this small of a dataset, but is useful in larger projects.

Now to query this FTS5 table, all we need is a single `SELECT` statement:

```
select
  rowid,
  headline,
  rank
from fts_articles
where headline match 'planned parenthood'
limit 10;
```

```
┌───────┬──────────────────────────────────────────────────────────────┬───────────────────┐
│ rowid │                           headline                           │       rank        │
├───────┼──────────────────────────────────────────────────────────────┼───────────────────┤
│ 4666  │ Kamala Harris visits Planned Parenthood clinic               │ -18.9139950477264 │
├───────┼──────────────────────────────────────────────────────────────┼───────────────────┤
│ 6521  │ Former Marine sentenced to 9 years in prison for firebombing │ -14.8070227038387 │
│       │  Planned Parenthood clinic                                   │                   │
└───────┴──────────────────────────────────────────────────────────────┴───────────────────┘
```

The search `"planned parenthood"` return 2 results, both that specifically have the keywords "planned parenthood". The `rank` column is the [negative bm25 score](https://www.sqlite.org/fts5.html#:~:text=The%20%22%2D1%22%20term,numerically%20lower%20scores.) of the query and the headline.

Now these types of results are exactly what I want — what I search is what I get. But maybe I want to see more than just "planned parenthood", like articles about abortion, reproductive rights, women's healthcare, etc. This is what vector search offers us, and setting that up in SQLite looks very similar to FTS5 tables.

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#building-vector-search-with-sqlite-vec) Building vector search with `sqlite-vec`
---------------------------------------------------------------------------------------------------------------------------------------------------------

Now `sqlite-vec` offers vector storage and vector comparisions, but it does not generate embeddings for you. If you're running `sqlite-vec` from a Python/Node.js/some other script, you can always use a 3rd party service or a local embeddings inference API to generate embeddings. But for this example, I want to keep everything in SQL and keep things local, so I'll use the [`sqlite-lembed`](https://github.com/asg017/sqlite-lembed) extension with the [`Snowflake Artic Embed 1.5 model`](https://www.snowflake.com/engineering-blog/arctic-embed-m-v1-5-enterprise-retrieval/).

You can download a `.gguf` quantized version of this model with:

```
wget https://huggingface.co/asg017/sqlite-lembed-model-examples/resolve/main/snowflake-arctic-embed-m-v1.5/snowflake-arctic-embed-m-v1.5.d70deb40.f16.gguf
```

And we can configure `sqlite-lembed` to use this model like so:

```
.load ./lembed0
insert into lembed_models(name, model) values
  ('default', lembed_model_from_file('./snowflake-arctic-embed-m-v1.5.d70deb40.f16.gguf'));
```

Now we can embed our text with the `lembed()` SQL function! We will store these embeddings in a `vec0` virtual table like so:

```
.load ./vec0

create virtual table vec_articles using vec0(
  article_id integer primary key,
  headline_embedding float[768]
);

insert into vec_articles(article_id, headline_embedding)
  select
    rowid,
    lembed(headline)
  from articles;
```

And that's it! To perform a KNN query, we can do something like so:

```
select
  articles.headline,
  vec_articles.distance
from vec_articles
left join articles on articles.rowid = vec_articles.article_id
where headline_embedding match lembed("planned parenthood")
  and k = 10;
```

```
┌──────────────────────────────────────────────────────────────┬───────────────────┐
│                           headline                           │     distance      │
├──────────────────────────────────────────────────────────────┼───────────────────┤
│ Kamala Harris visits Planned Parenthood clinic               │ 0.492593914270401 │
├──────────────────────────────────────────────────────────────┼───────────────────┤
│ After Dobbs decision, more women are managing their own abor │ 0.578903257846832 │
│ tions                                                        │                   │
├──────────────────────────────────────────────────────────────┼───────────────────┤
│ Transforming Healthcare                                      │ 0.582241117954254 │
├──────────────────────────────────────────────────────────────┼───────────────────┤
│ A timeline of Trump's many, many positions on abortion       │ 0.610146284103394 │
├──────────────────────────────────────────────────────────────┼───────────────────┤
│ How a network of abortion pill providers works together in t │ 0.61968868970871  │
│ he wake of new threats                                       │                   │
├──────────────────────────────────────────────────────────────┼───────────────────┤
│                                  ...                                             │
└──────────────────────────────────────────────────────────────┴───────────────────┘
```

Now that we have `fts_articles` and `vec_articles` virtual tables set up, we can now explore different hybrid search methods. The core FTS5 and `vec0` queries will remain the same, they only really differ by using different `JOIN` or `ORDER BY` methods.

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#hybrid-approach-1-keyword-first) Hybrid approach #1: "Keyword-first"
---------------------------------------------------------------------------------------------------------------------------------------------

The first hybrid approach: return full-text search results first, then augment the rest with vector search.

We can perform this with a CTE, doing FTS5 and `sqlite-vec` searches in separate steps, combining them after with a `UNION ALL`:

```
.param set :query 'abortion bans'
.param set :k 10


--- FTS5 search results
with fts_matches as (
  select
    rowid as article_id,
    row_number() over (order by rank) as rank_number,
    rank as score
  from fts_articles
  where headline match :query
  limit :k
),
--- sqlite-vec KNN vector search results
vec_matches as (
  select
    article_id,
    row_number() over (order by distance) as rank_number,
    distance as score
  from vec_articles
  where
    headline_embedding match lembed(:query)
    and k = :k
  order by distance
),
-- combining FTS5 + vector search results, FTS comes first
combined as (
  select 'fts' as match_type, * from fts_matches
  union all
  select 'vec' as match_type, * from vec_matches
),
-- JOIN back the articles.headline contents
final as (
  select
    articles.id,
    articles.headline,
    combined.*
  from combined
  left join articles on articles.rowid = combined.article_id
)
select * from final;
```

The results:

```
┌───────┬──────────────────────────────────────────────────────────────┬────────────┬────────────┬─────────────┬───────────────────┐
│  id   │                           headline                           │ match_type │ article_id │ rank_number │       score       │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 10098 │ Kamala Harris says abortion bans are creating 'a health care │ fts        │ 10098      │ 1           │ -10.6788292709361 │
│       │  crisis'                                                     │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 9776  │ States with abortion bans saw birth control prescriptions fa │ fts        │ 9776       │ 2           │ -10.0163167259711 │
│       │ ll post-Dobbs, study finds                                   │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 2292  │ Ohio GOP Senate candidates pitch federal abortion bans even  │ fts        │ 2292       │ 3           │ -9.7149595994016  │
│       │ after voters protected reproductive rights                   │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 452   │ 64K women and girls became pregnant due to rape in states wi │ fts        │ 452        │ 4           │ -9.16355856942554 │
│       │ th abortion bans, study estimates                            │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 9187  │ Abortion bans drive away up to half of young talent, CNBC/Ge │ fts        │ 9187       │ 5           │ -9.16355856942554 │
│       │ neration Lab youth survey finds                              │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 6989  │ Trump says abortion restrictions should be left to states, d │ vec        │ 6989       │ 1           │ 0.493074983358383 │
│       │ odging a national ban                                        │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 13928 │ After Dobbs decision, more women are managing their own abor │ vec        │ 13928      │ 2           │ 0.512084662914276 │
│       │ tions                                                        │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 11822 │ Iowa now bans most abortions after about 6 weeks             │ vec        │ 11822      │ 3           │ 0.512569785118103 │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 7381  │ Where abortion rights could be on the ballot this fall: From │ vec        │ 7381       │ 4           │ 0.516829192638397 │
│       │  the Politics Desk                                           │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 14009 │ Trump signals openness to banning abortion pill              │ vec        │ 14009      │ 5           │ 0.528829395771027 │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 4426  │ Medication abortions rose in year after Dobbs decision, repo │ vec        │ 4426       │ 6           │ 0.530509769916534 │
│       │ rt finds                                                     │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 4328  │ Trump signals support for a national 15-week abortion ban    │ vec        │ 4328       │ 7           │ 0.532848060131073 │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 6979  │ A timeline of Trump's many, many positions on abortion       │ vec        │ 6979       │ 8           │ 0.533357560634613 │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 2092  │ For the first time in years, Sen. Graham hasn't introduced a │ vec        │ 2092       │ 9           │ 0.533683061599731 │
│       │  national abortion ban                                       │            │            │             │                   │
├───────┼──────────────────────────────────────────────────────────────┼────────────┼────────────┼─────────────┼───────────────────┤
│ 6794  │ Trump's conflicting abortion stances are coming back to haun │ vec        │ 6794       │ 10          │ 0.534709513187408 │
│       │ t him — and his party                                        │            │            │             │                   │
└───────┴──────────────────────────────────────────────────────────────┴────────────┴────────────┴─────────────┴───────────────────┘
```

This approach would technically fix the "Adventure Time + HBO Max" problem described above — what users expect will always come first. Then if those results aren't good enough, then hopefully the vector search results can satisfy them!

One note: this specific query doesn't do any de-duplication, so include that if needed.

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#hybrid-approach-2-reciprocal-rank-fusion-rrf) Hybrid approach #2: Reciprocal Rank Fusion (RRF)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another approach: [Reciprocal Rank Fusion (RRF)](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking), which ranks results that are both FTS5 and vector matches higher than others. Similar to the approach above, we can do this in a single `SELECT` query with CTEs, as described [in the Supabase docs](https://supabase.com/docs/guides/ai/hybrid-search):

```
.param set :query 'abortion ban'


.param set :k 10
.param set :rrf_k 60
.param set :weight_fts 1.0
.param set :weight_vec 1.0

-- the sqlite-vec KNN vector search results
with vec_matches as (
  select
    article_id,
    row_number() over (order by distance) as rank_number,
    distance
  from vec_articles
  where
    headline_embedding match lembed(:query)
    and k = :k
),
-- the FTS5 search results
fts_matches as (
  select
    rowid,
    row_number() over (order by rank) as rank_number,
    rank as score
  from fts_articles
  where headline match :query
  limit :k
),
-- combine FTS5 + vector search results with RRF
final as (
  select
    articles.id,
    articles.headline,
    vec_matches.rank_number as vec_rank,
    fts_matches.rank_number as fts_rank,
    -- RRF algorithm
    (
      coalesce(1.0 / (:rrf_k + fts_matches.rank_number), 0.0) * :weight_fts +
      coalesce(1.0 / (:rrf_k + vec_matches.rank_number), 0.0) * :weight_vec
    ) as combined_rank,
    vec_matches.distance as vec_distance,
    fts_matches.score as fts_score
  from fts_matches
  full outer join vec_matches on vec_matches.article_id = fts_matches.rowid
  join articles on articles.rowid = coalesce(fts_matches.rowid, vec_matches.article_id)
  order by combined_rank desc
)
select * from final;

```

And the results:

```
┌───────┬──────────────────────────────────────────────────────────────┬──────────┬──────────┬────────────────────┬───────────────────┬───────────────────┐
│  id   │                           headline                           │ vec_rank │ fts_rank │   combined_rank    │   vec_distance    │     fts_score     │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 4328  │ Trump signals support for a national 15-week abortion ban    │ 2        │ 3        │ 0.0320020481310804 │ 0.533420383930206 │ -9.84164516849395 │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 5769  │ Mitch McConnell shies away from supporting national abortion │ 8        │ 2        │ 0.0308349146110057 │ 0.550142526626587 │ -10.1901778756711 │
│       │  ban                                                         │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 9507  │ Arizona Senate passes repeal of 1864 abortion ban            │          │ 1        │ 0.0163934426229508 │                   │ -10.5643028316427 │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 6989  │ Trump says abortion restrictions should be left to states, d │ 1        │          │ 0.0163934426229508 │ 0.514239549636841 │                   │
│       │ odging a national ban                                        │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 10717 │ Supreme Court rejects bid to restrict access to abortion pil │ 3        │          │ 0.0158730158730159 │ 0.535124838352203 │                   │
│       │ l                                                            │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 5981  │ Arizona state House passes bill to repeal 1864 abortion ban  │          │ 4        │ 0.015625           │                   │ -9.84164516849395 │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 14009 │ Trump signals openness to banning abortion pill              │ 4        │          │ 0.015625           │ 0.536433517932892 │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 6375  │ Arizona Republicans again quash effort to repeal 1864 aborti │          │ 5        │ 0.0153846153846154 │                   │ -9.84164516849395 │
│       │ on ban                                                       │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 7381  │ Where abortion rights could be on the ballot this fall: From │ 5        │          │ 0.0153846153846154 │ 0.546237885951996 │                   │
│       │  the Politics Desk                                           │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 9443  │ Arizona Gov. Katie Hobbs signs repeal of 1864 abortion ban   │          │ 6        │ 0.0151515151515152 │                   │ -9.84164516849395 │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 13928 │ After Dobbs decision, more women are managing their own abor │ 6        │          │ 0.0151515151515152 │ 0.546703100204468 │                   │
│       │ tions                                                        │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 1821  │ Dominican women fight child marriage, teen pregancy amid tot │          │ 7        │ 0.0149253731343284 │                   │ -9.51616557526609 │
│       │ al abortion ban                                              │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 2092  │ For the first time in years, Sen. Graham hasn't introduced a │ 7        │          │ 0.0149253731343284 │ 0.547752380371094 │                   │
│       │  national abortion ban                                       │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 7150  │ Tennessee court weighs challenge to abortion ban’s narrow me │          │ 8        │ 0.0147058823529412 │                   │ -9.51616557526609 │
│       │ dical exception                                              │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 8690  │ Arizona Supreme Court pushes back enforcement date for 1864  │          │ 9        │ 0.0144927536231884 │                   │ -9.51616557526609 │
│       │ abortion ban                                                 │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 11822 │ Iowa now bans most abortions after about 6 weeks             │ 9        │          │ 0.0144927536231884 │ 0.555717051029205 │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 2646  │ Trump campaign scrambles over abortion ban report as Democra │          │ 10       │ 0.0142857142857143 │                   │ -9.21152510186621 │
│       │ ts seize the moment                                          │          │          │                    │                   │                   │
├───────┼──────────────────────────────────────────────────────────────┼──────────┼──────────┼────────────────────┼───────────────────┼───────────────────┤
│ 5538  │ Map: Where medication abortion is and isn’t legal            │ 10       │          │ 0.0142857142857143 │ 0.558846414089203 │                   │
└───────┴──────────────────────────────────────────────────────────────┴──────────┴──────────┴────────────────────┴───────────────────┴───────────────────┘
```

Note that the first result `"Trump signals support for a national 15-week abortion ban"` was ranked 2nd in the vector result and 3rd in FTS5 results. But since it's in both, it's ranked higher than the respective #1 results.

It's also configurable, you can change `:weight_fts` or `:weight_vec` to rank FTS5/vector results differently, which can be handy!

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#hybrid-approach-3-re-rank-by-semantics) Hybrid approach #3: Re-rank by semantics
---------------------------------------------------------------------------------------------------------------------------------------------------------

This approach is slightly different than the ones above: instead of querying the `vec0` table as all, we just perform a FTS5 search, but re-order the results based on their vector distance.

```
.param set :query 'abortion ban'
.param set :k 10


-- The FTS5 search results
with fts_matches as (
  select
    rowid,
    row_number() over (order by rank) as fts_rank_number,
    rank as score
  from fts_articles
  where headline match :query
  limit :k
),
-- re-ordered by "semantic meaning"
final as (
  select
    articles.id,
    articles.headline,
    fts_matches.*
  from fts_matches
  left join articles on articles.rowid = fts_matches.rowid
  order by vec_distance_cosine(lembed(:query), lembed(articles.headline))
)
select * from final;

```

And the results:

```
┌──────┬──────────────────────────────────────────────────────────────┬───────┬─────────────────┬───────────────────┐
│  id  │                           headline                           │ rowid │ fts_rank_number │       score       │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 4328 │ Trump signals support for a national 15-week abortion ban    │ 4328  │ 3               │ -9.84164516849395 │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 5769 │ Mitch McConnell shies away from supporting national abortion │ 5769  │ 2               │ -10.1901778756711 │
│      │  ban                                                         │       │                 │                   │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 2646 │ Trump campaign scrambles over abortion ban report as Democra │ 2646  │ 10              │ -9.21152510186621 │
│      │ ts seize the moment                                          │       │                 │                   │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 7150 │ Tennessee court weighs challenge to abortion ban’s narrow me │ 7150  │ 8               │ -9.51616557526609 │
│      │ dical exception                                              │       │                 │                   │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 1821 │ Dominican women fight child marriage, teen pregancy amid tot │ 1821  │ 7               │ -9.51616557526609 │
│      │ al abortion ban                                              │       │                 │                   │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 6375 │ Arizona Republicans again quash effort to repeal 1864 aborti │ 6375  │ 5               │ -9.84164516849395 │
│      │ on ban                                                       │       │                 │                   │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 9507 │ Arizona Senate passes repeal of 1864 abortion ban            │ 9507  │ 1               │ -10.5643028316427 │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 8690 │ Arizona Supreme Court pushes back enforcement date for 1864  │ 8690  │ 9               │ -9.51616557526609 │
│      │ abortion ban                                                 │       │                 │                   │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 5981 │ Arizona state House passes bill to repeal 1864 abortion ban  │ 5981  │ 4               │ -9.84164516849395 │
├──────┼──────────────────────────────────────────────────────────────┼───────┼─────────────────┼───────────────────┤
│ 9443 │ Arizona Gov. Katie Hobbs signs repeal of 1864 abortion ban   │ 9443  │ 6               │ -9.84164516849395 │
└──────┴──────────────────────────────────────────────────────────────┴───────┴─────────────────┴───────────────────┘
```

We still get only keyword match results, but better semantic matches will float towards the top. This can help workaround some of the disadvantages of BM25.

One note: this query here is inefficient — `lembed()` is called on each result, even though we pre-computed them in `vec_articles`. This could be replaced with a `SELECT headline_embedding FROM vec_articles WHERE rowid in (...)` query.

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#which-should-i-choose) Which should I choose?
----------------------------------------------------------------------------------------------------------------------

It depends on your application and use-case!

Are you building a search engine for email inbox? If so keyword-first may make the most sense, as "what you search is what you get" is pretty important in more inbox searches, at least in my experience.

Are you building RAG across some internal company documents? If so RRF may be a good option, as exact matches like internal company project names are important, while semantic matches can better shape a query. Plus, a LLM can usually parse out irrelevant responses.

Are you building a ["duplicate post"](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/marking-issues-or-pull-requests-as-a-duplicate) feature into your webapp? If some re-rank by semantics might work well, as finding exact matches would be contextually important, but the top few results would matter more.

So it really depends! What's nice about doing this in SQLite makes experimenting and prototyping easy. Your data is a single file, you can test multiple queries will single `SELECT` statements. It costs nothing, works in all programming languages, and can be easily done in a few lines of code.

[¶](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html#future-improvements) Future Improvements
-----------------------------------------------------------------------------------------------------------------

The union between FTS5 and `sqlite-vec` is great for small samples, but there's still some rough edges to smooth out!

For example: FTS5 query can "highlight" matches in a document like so:

```
select
  rowid,
  highlight(fts_articles, 0, '<b>', '</b>') as headline_highlighted
from fts_articles
where headline match 'planned parenthood'
limit 10;
```

```
┌───────┬──────────────────────────────────────────────────────────────┐
│ rowid │                     headline_highlighted                     │
├───────┼──────────────────────────────────────────────────────────────┤
│ 4666  │ Kamala Harris visits <b>Planned</b> <b>Parenthood</b> clinic │
├───────┼──────────────────────────────────────────────────────────────┤
│ 6521  │ Former Marine sentenced to 9 years in prison for firebombing │
│       │  <b>Planned</b> <b>Parenthood</b> clinic                     │
└───────┴──────────────────────────────────────────────────────────────┘
```

This adds HTML bold tags around the query matches in the document itself, so you can see easily see why a document is returned.

But `sqlite-vec` doesn't have this — a vector search only returns the L2/cosine distance between the query vector and document, not _why_ they are a match. There are models out there like [ColBERT](https://huggingface.co/vespa-engine/col-minilm) that provide ["scoring" on queries and passages](https://simonwillison.net/2024/Jan/28/colbert-query-passage-scoring-interpretability/), but `sqlite-vec` doesn't have tensor support yet.

Also, FTS5 queries have a ton of other features like [phrases](https://www.sqlite.org/fts5.html#fts5_phrases), [`NEAR` queries](https://www.sqlite.org/fts5.html#fts5_near_queries), and [boolean operators](https://www.sqlite.org/fts5.html#fts5_boolean_operators). Using these features will make vector searches awkward, since the query would be provided as-is.

Also, scaling hybrid search with FTS5 + `sqlite-vec` might be awkward. FTS5 tables perform a full search across the entire dataset everytime, there's no way of provided metadata filtering or indexing on a single FTS5 index. This isn't the case for `sqlite-vec` either, but support for [paritioning](https://github.com/asg017/sqlite-vec/issues/29) and [metadata filtering](https://github.com/asg017/sqlite-vec/issues/26) is coming soon!

* * *

So try out hybrid search with `sqlite-vec` in your projects! Feel free to drop any questions in the [`#sqlite-vec` channel in the Mozilla Discord](https://discord.gg/Ve7WeCJFXk).
