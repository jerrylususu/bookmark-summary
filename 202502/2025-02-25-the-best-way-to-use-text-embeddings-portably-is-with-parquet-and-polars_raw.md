Title: The Best Way to Use Text Embeddings Portably is With Parquet and Polars

URL Source: https://minimaxir.com/2025/02/embeddings-parquet/

Published Time: 2025-02-24T10:15:00-08:00

Markdown Content:
[Text embeddings](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/), particularly modern embeddings generated from large language models, are one of the most useful applications coming from the generative AI boom. Embeddings are a list of numbers which represent an object: in the case of text embeddings, they can represent words, sentences, and full paragraphs and documents, and they do so with a surprising amount of distinctiveness.

Recently, I created text embeddings representing every distinct [Magic: the Gathering](https://magic.wizards.com/en) card released as of the February 2025 Aetherdrift expansion: 32,254 in total. With these embeddings, I can find the mathematical similarity between cards through the encoded representation of their card design, including all mechanical attributes such as the card name, card cost, card text, and even card rarity.

![Image 1: The iconic Magic card Wrath of God, along with its top four most similar cards identified using their respective embeddings. The similar cards are valid matches, with similar card text and card types.](https://minimaxir.com/2025/02/embeddings-parquet/wog.webp)

The iconic Magic card [Wrath of God](https://gatherer.wizards.com/pages/card/Details.aspx?multiverseid=129808), along with its top four most similar cards identified using their respective embeddings. The similar cards are valid matches, with similar card text and card types.

Additionally, I can create a fun 2D [UMAP](https://umap-learn.readthedocs.io/en/latest/) projection of all those cards, which also identifies interesting patterns:

![Image 2: The UMAP dimensionality reduction process also implicitly clusters the Magic cards to logical clusters, such as by card color(s) and card type.](https://minimaxir.com/2025/02/embeddings-parquet/mtg_umap.webp)

The UMAP dimensionality reduction process also implicitly clusters the Magic cards to logical clusters, such as by card color(s) and card type.

I generated these Magic card embeddings for _something special_ besides a pretty data visualization, but if you are curious how I generated them, they were made using the new-but-underrated [gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) embedding model and the process is detailed [in this GitHub repository](https://github.com/minimaxir/mtg-embeddings). The embeddings themselves (including the coordinate values to reproduce the 2D UMAP visualization) are available as a [Hugging Face dataset](https://huggingface.co/datasets/minimaxir/mtg-embeddings).

Most tutorials involving embedding generation omit the obvious question: what do you _do_ with the text embeddings after you generate them? The common solution is to use a [vector database](https://en.wikipedia.org/wiki/Vector_database), such as [faiss](https://github.com/facebookresearch/faiss) or [qdrant](https://qdrant.tech/), or even a cloud-hosted service such as [Pinecone](https://www.pinecone.io/). But those aren’t easy to use: faiss has [confusing configuration options](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index), qdrant requires [using a Docker container](https://github.com/qdrant/qdrant?tab=readme-ov-file#client-server) to host the storage server, and Pinecone can get [very expensive](https://www.pinecone.io/pricing/) very quickly, and its free Starter tier is limited.

What many don’t know about text embeddings is that you don’t _need_ a vector database to calculate nearest-neighbor similarity if your data isn’t too large. Using [numpy](https://numpy.org/doc/stable/index.html) and my Magic card embeddings, a 2D matrix of 32,254 `float32` embeddings at a dimensionality of 768D (common for “smaller” LLM embedding models) occupies **94.49 MB** of system memory, which is relatively low for modern personal computers and can fit within free usage tiers of cloud VMs. If both the query vector and the embeddings themselves are unit normalized (many embedding generators normalize by default), then the matrix dot product between the query and embeddings results in a cosine similarity between `[-1, 1]`, where the higher score is better/more similar. Since dot products are such a fundamental aspect of linear algebra, numpy’s implementation is extremely fast: with the help of additional numpy [sorting](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html) [shenanigans](https://numpy.org/doc/2.1/reference/generated/numpy.argsort.html), on my M3 Pro MacBook Pro it takes just **1.08 ms** on average to calculate all 32,254 dot products, find the top 3 most similar embeddings, and return their corresponding `idx` of the matrix and and cosine similarity `score`.

```
def fast_dot_product(query, matrix, k=3):
    dot_products = query @ matrix.T

    idx = np.argpartition(dot_products, -k)[-k:]
    idx = idx[np.argsort(dot_products[idx])[::-1]]

    score = dot_products[idx]

    return idx, score
```

In most implementations of vector databases, once you insert the embeddings, they’re stuck there in a proprietary serialization format and you are locked into that library and service. If you’re just building a personal pet project or sanity-checking embeddings to make sure the results are good, that’s a huge amount of friction. For example, when I want to experiment with embeddings, I generate them on a cloud server with a GPU since LLM-based embeddings models are often slow to generate without one, and then download them locally to my personal computer. What is the best way to handle embeddings portably such that they can easily be moved between machines and also in a non-proprietary format?

The answer, after much personal trial-and-error, is Parquet files, which still has a surprising amount of nuance. But before we talk about why Parquet files are good, let’s talk about how _not_ to store embeddings.

The Worst Ways to Store Embeddings
----------------------------------

The incorrect-but-unfortunately-common way to store embeddings is in a text format such as a CSV file. Text data is substantially larger than `float32` data: for example, a decimal number with full precision (e.g. `2.145829051733016968e-02`) as a `float32` is 32 bits/4 bytes, while as a text representation (in this case 24 ASCII `char`s) it’s 24 bytes, **6x larger**. When the CSV is saved and loaded, the data has to be serialized between a numpy and a string representation of the array, which adds significant overhead. Despite that, in [one of OpenAI’s official tutorials](https://github.com/openai/openai-cookbook/blob/a3e98ea4dcf866b5e7a3cb7d63dccaa68c7d63aa/examples/Embedding_Wikipedia_articles_for_search.ipynb) for their embeddings models, they save the embeddings as a CSV using [pandas](https://pandas.pydata.org/) with the admitted caveat of “Because this example only uses a few thousand strings, we’ll store them in a CSV file. (For larger datasets, use a vector database, which will be more performant.)”. In the case of the Magic card embeddings, pandas-to-CSV performs the _worst_ out of any encoding options: more on why later.

Numpy has native methods to [save](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html) and [load](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) embeddings as a `.txt` that’s straightforward:

```
np.savetxt("embeddings_txt.txt", embeddings)

embeddings_r = np.loadtxt("embeddings_txt.txt", dtype=np.float32, delimiter=" ")
```

The resulting file not only takes a few seconds to save and load, but it’s also massive: **631.5 MB**!

As an aside, HTTP APIs such as OpenAI’s [Embeddings API](https://platform.openai.com/docs/guides/embeddings) do transmit the embeddings over text which adds needless latency and bandwidth overhead. I wish more embedding providers offered [gRPC](https://grpc.io/) APIs which allow transfer of binary `float32` data instead to gain a performance increase: Pinecone’s [Python SDK](https://docs.pinecone.io/reference/python-sdk), for example, does just that.

The second incorrect method to save a matrix of embeddings to disk is to save it as a Python [pickle](https://docs.python.org/3/library/pickle.html) object, which stores its representation in memory on disk with a few lines of code from the native `pickle` library. Pickling is unfortunately common in the machine learning industry since many ML frameworks such as [scikit-learn](https://scikit-learn.org/stable/) don’t have easy ways to serialize encoders and models. But it comes with two major caveats: pickled files are a massive security risk as they can execute arbitrary code, and the pickled file may not be guaranteed to be able to be opened on other machines or Python versions. It’s 2025, just stop pickling if you can.

In the case of the Magic card embeddings, it does indeed work with instant save/loads, and the file size on disk is **94.49 MB**: the same as its memory consumption and about 1/6th of the text size as expected:

```
with open("embeddings_matrix.pkl", "wb") as f:
    pickle.dump(embeddings, f)

with open("embeddings_matrix.pkl", "rb") as f:
    embeddings_r = pickle.load(f)
```

But there are still better and easier approaches.

The Intended-But-Not-Great Way to Store Embeddings
--------------------------------------------------

Numpy itself has a canonical way to [save](https://numpy.org/doc/2.1/reference/generated/numpy.save.html) and [load](https://numpy.org/doc/2.1/reference/generated/numpy.load.html) matrixes — which annoyingly saves as a pickle by default for compatability reasons, but that can fortunately be disabled by setting `allow_pickle=False`:

```
np.save("embeddings_matrix.npy", embeddings, allow_pickle=False)

embeddings_r = np.load("embeddings_matrix.npy", allow_pickle=False)
```

File size and I/O speed are the same as with the `pickle` approach.

This works — and it’s something I had used for awhile — but in the process it exposes another problem: how do we map metadata (the Magic cards in this case) to embeddings? Currently, we use the `idx` of the most-similar matches to perform an efficient batched lookup to the source data. In this case, the number of rows matches the number of cards exactly, but what happens if the embeddings matrix needs to be changed, such as to add or remove cards and their embeddings? What happens if you want to add a dataset filter? It becomes a mess that inevitably causes technical debt.

The solution to this is to colocate metadata such as card names, card text, and attributes with their embeddings: that way, if they are later added, removed, or sorted, the results will remain the same. Modern vector databases such as qdrant and Pinecone do just that, with the ability to filter and sort on the metadata at the same time you query the most similar vectors. This is a bad idea to do in numpy itself, as it’s more optimized for numbers and not other data types such as strings, which have [limited operations available](https://numpy.org/devdocs/user/basics.strings.html).

The solution is to look at another file format that can store metadata and embeddings simultaneously, and the answer to that is Parquet files. But there’s a rabbit hole as to what’s the _best_ way to interact with them.

What are Parquet files?
-----------------------

Parquet, developed by the open-source [Apache Parquet](https://parquet.apache.org/) project, is a file format for handling columnar data, but despite being [first released in 2013](https://blog.x.com/engineering/en_us/a/2013/announcing-parquet-10-columnar-storage-for-hadoop) it hasn’t taken off in the data science community until very recently. [1](https://minimaxir.com/2025/02/embeddings-parquet/#fn:1) The most relevant feature of Parquet is that the resulting files are typed for each column, and that this typing includes nested lists, such as an embedding which is just a list of `float32` values. As a bonus, the columnar format allows downstream libraries to save/load them selectively and very quickly, far faster than CSVs and with rare parsing errors. The file format also allows for efficient compression and decompression, but that’s less effective with embeddings as there’s little redundant data.

For Parquet file I/O, the standard approach is to use the [Apache Arrow](https://arrow.apache.org/) protocol that is columnar in-memory, which complements the Parquet storage medium on disk. But how do you use Arrow?

How do you use Parquet files in Python for embeddings?
------------------------------------------------------

Ideally, we need a library that can handle nested data easily and can interoperate with numpy for serializing to a matrix and can run fast dot products.

The official Arrow library that [interacts with Parquet natively](https://arrow.apache.org/docs/python/index.html) in Python is [pyarrow](https://arrow.apache.org/docs/python/index.html). Here, I have an example Parquet file generated with \[SPOILERS\] that contains both the card metadata and an `embedding` column, with the embedding for each row corresponding to that card.

```
df = pa.parquet.read_table("mtg-embeddings.parquet")
```

![Image 3: Pyarrow’s table schema from the input Parquet file of Magic card embeddings. Note the embedding column at the bottom is a list of 768 floats.](https://minimaxir.com/2025/02/embeddings-parquet/parquet.png)

Pyarrow’s table schema from the input Parquet file of Magic card embeddings. Note the `embedding` column at the bottom is a list of 768 floats.

But pyarrow is not a DataFrame library, and despite the data being in a Table, it’s hard to slice and access: the documentation suggests that you export to pandas if you need more advanced manipulation.

Other more traditional data science libraries can leverage pyarrow directly. The most popular one is, of course, pandas itself which can [read/write Parquet](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html) doing just that. There are many, many resources for using pandas well, so it’s often the first choice among data science practioners.

```
df = pd.read_parquet("mtg-embeddings.parquet", columns=["name", "embedding"])
df
```

![Image 4: Pandas HTML table output of the Magic card DataFrame when printed in a Jupyter Notebook.](https://minimaxir.com/2025/02/embeddings-parquet/pandas_embed.png)

Pandas HTML table output of the Magic card DataFrame when printed in a Jupyter Notebook.

There’s one major weakness for the use case of embeddings: pandas is very bad at nested data. From the image above you’ll see that the `embedding` column _appears_ to be a list of numbers, but it’s actually a list of numpy `object`s, which is a very inefficent datatype and why I suspect writing it to a CSV is very slow. Simply converting it to numpy with `df["embedding"].to_numpy()` results in a 1D array, which is definitely wrong, and trying to cast it to `float32` doesn’t work. I found that the best way to extract the embeddings matrix from a pandas `embedding` column is to [np.vstack()](https://numpy.org/doc/2.1/reference/generated/numpy.vstack.html) the embeddings, e.g. `np.vstack(df["embedding"].to_numpy())`, which does result in a `(32254, 768)` `float32` matrix as expected. That adds a lot of compute and memory overhead in addition to unnecessary numpy array copies. Finally, after computing the dot products between a candidate query and the embedding matrix, row metadata with the most similar values can then be retrieved using `df.loc[idx]`. [2](https://minimaxir.com/2025/02/embeddings-parquet/#fn:2)

However, there is another, more recent tabular data library that not only is faster than pandas, it has proper support for nested data. That library is polars.

The Power of polars
-------------------

[Polars](https://pola.rs/) is a relatively new Python library which is primarily written in [Rust](https://www.rust-lang.org/) and [supports Arrow](https://docs.pola.rs/#key-features), which gives it a [massive performance increase](https://duckdblabs.github.io/db-benchmark/) over pandas and many other DataFrame libraries. In the case of Magic cards, 32k rows isn’t nearly “big data” and the gains of using a high-performance library are lesser, but there are some unexpected features that coincidentally work _perfectly_ for the embeddings use case.

As with pandas, you read a parquet file with a `read_parquet()`:

```
df = pl.read_parquet("mtg-embeddings.parquet", columns=["name", "embedding"])
df
```

![Image 5: Polars HTML table output of the Magic card DataFrame when printed in a Jupyter Notebook.](https://minimaxir.com/2025/02/embeddings-parquet/polars_embed.png)

Polars HTML table output of the Magic card DataFrame when printed in a Jupyter Notebook.

There’s a notable difference in the table output compared to `pandas`: it also reports the data type of its columns, and more importantly, it shows that the `embedding` column consists of arrays, all `float32`s, and all length 768. That’s a great start!

polars also has a to\_numpy() function. Unlike pandas, if you call `to_numpy()` on a column as a Series, e.g. `df['embedding'].to_numpy()`, the returned object is a numpy 2D matrix: no `np.vstack()` needed. If you look at the [documentation](https://docs.pola.rs/api/python/stable/reference/series/api/polars.Series.to_numpy.html) for the function, there’s a curious feature:

> This operation copies data only when necessary. The conversion is zero copy when all of the following hold: \[…\]

Zero copy! And in the case of columnar-stored embeddings, the conditions will always hold, but you can set `allow_copy=False` to throw an error just in case.

Inversely, if you want to add a 2D embeddings matrix to an existing DataFrame and colocate each embedding’s corresponding metadata, such as after you batch-generate thousands of embeddings and want to save and download the resulting Parquet, it’s just as easy as adding a column to the DataFrame.

```
df = pl.with_columns(embedding=embeddings)

df.write_parquet("mtg-embeddings.parquet")
```

Now, let’s put the speed to the test using all the Magic card metadata. What if we perform embedding similarity on a Magic card, but beforehand dynamically filter the dataset according to user parameters (therefore filtering the candidate embeddings at the same time since they are colocated) and perform the similarity calculations quickly as usual? Let’s try with [Lightning Helix](https://gatherer.wizards.com/pages/card/details.aspx?multiverseid=87908), a card whose effects are self-explanatory even to those who don’t play Magic.

![Image 6: The most similar cards to Lightning Helix do have similar effects, although “Lightning” cards dealing damage is a common trope in Magic. Warleader’s Helix is a direct reference to Lightning Helix.](https://minimaxir.com/2025/02/embeddings-parquet/helix_1.webp)

The most similar cards to Lightning Helix do have similar effects, although “Lightning” cards dealing damage is a common trope in Magic. [Warleader’s Helix](https://gatherer.wizards.com/pages/card/Details.aspx?multiverseid=456806) is a direct reference to Lightning Helix.

Now we can also find similar cards to Lightning Helix but with filters. In this case, let’s look for a Sorcery (which are analogous to Instants but tend to be stronger since they have play limitations) and has Black as one of its colors. This limits the candidates to ~3% of the original dataset. The resulting code would look like this, given a `query_embed`:

```
df_filter = df.filter(
    pl.col("type").str.contains("Sorcery"),
    pl.col("manaCost").str.contains("B"),
)

embeddings_filter = df_filter["embedding"].to_numpy(allow_copy=False)
idx, _ = fast_dot_product(query_embed, embeddings_filter, k=4)
related_cards = df_filter[idx]
```

As an aside, in polars you can call row subsets of a DataFrame with `df[idx]`, which makes it infinitely better than pandas and its `df.iloc[idx]`.

The resulting similar cards:

![Image 7: In this case, the similarity focuses on card text similarity, and these cards have near identical text. Smiting Helix is also a direct reference to Lightning Helix.](https://minimaxir.com/2025/02/embeddings-parquet/helix_2.webp)

In this case, the similarity focuses on card text similarity, and these cards have near identical text. [Smiting Helix](https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=464058) is also a direct reference to Lightning Helix.

Speed-wise, the code runs at about **1.48ms** on average, or about 37% slower than calculating all dot products, so the filtering does still have some overhead, which is not surprising as that the filtered dataframe does copy the embeddings. Overall, it’s still more than fast enough for a hobby project.

I’ve created an [interactive Colab Notebook](https://colab.research.google.com/drive/19C_9sBC0Py2PlXYihl2ed378oGyroONZ?usp=sharing) where you can generate similarities for any Magic card, and apply any filters you want!

Scaling to Vector Databases
---------------------------

Again, all of this assumes that you are using the embeddings for smaller/noncommercial projects. If you scale to hundreds of thousands of embeddings, the parquet and dot product approach for finding similarity should still be fine, but if it’s a business critical application, the marginal costs of querying a vector database are likely lower than the marginal revenue from a snappy similarity lookup. Deciding how to make these tradeoffs is the fun part of MLOps!

In the case that the amount of vectors is too large to fit into memory but you don’t want to go all-in on vector databases, another option that may be worth considering is using an old-fashioned database that can now support vector embeddings. Notably, [SQLite](https://www.sqlite.org/) databases are just a single portable file, however interacting with them has more technical overhead and considerations than the `read_parquet()` and `write_parquet()` of polars. One notable implementation of vector databases in SQLite is the [sqlite-vec extension](https://alexgarcia.xyz/sqlite-vec/), which also allows for simultaneous filtering and similarity calculations.

The next time you’re working with embeddings, consider whether you really need a vector database. For many applications, the combination of Parquet files and polars provides everything you need: efficient storage, fast similarity search, and easy metadata filtering. Sometimes the simplest solution is the best one.

_The code used to process the Magic card data, create the embeddings, and plot the UMAP 2D projection, is all available [in this GitHub repository](https://github.com/minimaxir/mtg-embeddings)._
