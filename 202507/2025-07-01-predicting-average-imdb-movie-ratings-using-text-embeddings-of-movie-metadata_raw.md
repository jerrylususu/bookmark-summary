Title: Predicting Average IMDb Movie Ratings Using Text Embeddings of Movie Metadata

URL Source: https://minimaxir.com/2025/06/movie-embeddings/

Published Time: 2025-06-30T10:00:00-07:00

Markdown Content:
Months ago, I saw a post titled “[Rejected from DS Role with no feedback](https://www.reddit.com/r/datascience/comments/1eykil7/rejected_from_ds_role_with_no_feedback/)” on Reddit’s [Data Science subreddit](https://www.reddit.com/r/datascience/), in which a prospective job candidate for a data science position provided a [Colab Notebook](https://colab.research.google.com/drive/1Ud2tXW2IAw_dXA5DONvNpPmmlL1foSwK) documenting their submission for a take-home assignment and asking for feedback as to why they were rejected. Per the Reddit user, the assignment was:

> Use the publicly available [IMDB Datasets](https://developer.imdb.com/non-commercial-datasets/) to build a model that predicts a movie’s average rating. Please document your approach and present your results in the notebook. Make sure your code is well-organized so that we can follow your modeling process.

[IMDb](https://www.imdb.com/), the Internet Movie Database owned by Amazon, allows users to rate movies on a scale from 1 to 10, wherein the average rating is then displayed prominently on the movie’s page:

![Image 1: The Shawshank Redemption is currently the highest-rated movie on IMDb with an average rating of 9.3 derived from 3.1 million user votes.](https://minimaxir.com/2025/06/movie-embeddings/shawshank.webp)

[The Shawshank Redemption](https://www.imdb.com/title/tt0111161/?ref_=sr_t_1) is currently the [highest-rated movie on IMDb](https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc) with an average rating of 9.3 derived from 3.1 million user votes.

In their notebook, the Redditor identifies a few intuitive features for such a model, including the year in which the movie was released, the genre(s) of the movies, and the actors/directors of the movie. However, the model they built is a [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/)-based neural network, with all the bells-and-whistles such as [batch normalization](https://en.wikipedia.org/wiki/Batch_normalization) and [dropout](https://en.wikipedia.org/wiki/Dilution_%28neural_networks%29). The immediate response by other data scientists on /r/datascience was, at its most polite, “why did you use a neural network when it’s a [black box](https://en.wikipedia.org/wiki/Black_box) that you can’t explain?”

Reading those replies made me nostalgic. Way back in 2017, before my first job as a data scientist, neural networks using frameworks such as TensorFlow and Keras were all the rage for their ability to “[solve any problem](https://en.wikipedia.org/wiki/Universal_approximation_theorem)” but were often seen as lazy and unskilled compared to traditional statistical modeling such as ordinary least squares linear regression or even gradient boosted trees. Although it’s funny to see that perception against neural networks in the data science community hasn’t changed since, nowadays the black box nature of neural networks can be an acceptable business tradeoff if the prediction results are higher quality and interpretability is not required.

Looking back at the assignment description, the objective is only “predict a movie’s average rating.” For data science interview take-homes, this is unusual: those assignments typically have an extra instruction along the lines of “explain your model and what decisions stakeholders should make as a result of it”, which is a strong hint that you need to use an explainable model like linear regression to obtain feature coefficients, or even a middle-ground like gradient boosted trees and its [variable importance](https://stats.stackexchange.com/questions/332960/what-is-variable-importance) to quantify relative feature contribution to the model. [1](https://minimaxir.com/2025/06/movie-embeddings/#fn:1) In absence of that particular constraint, it’s arguable that anything goes, including neural networks.

The quality of neural networks have improved significantly since 2017, even moreso due to the massive rise of LLMs. Why not try just feeding a LLM all raw metadata for a movie and encode it into a text embedding and build a statistical model based off of that? Would a neural network do better than a traditional statistical model in that instance? Let’s find out!

About IMDb Data
---------------

The [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/) are famous sets of data that have been around for nearly a decade [2](https://minimaxir.com/2025/06/movie-embeddings/#fn:2) but are still updated daily. Back in 2018 as a budding data scientist, I performed a [fun exporatory data analysis](https://minimaxir.com/2018/07/imdb-data-analysis/) using these datasets, although the results aren’t too surprising.

![Image 2: The average rating for a movie is around 6 and tends to skew higher: a common trend in internet rating systems.](https://minimaxir.com/2025/06/movie-embeddings/imdb-4.png)

The average rating for a movie is around 6 and tends to skew higher: a common trend in internet rating systems.

But in truth, these datasets are a terrible idea for companies to use for a take-home assignment. Although the datasets are released under a non-commercial license, IMDb doesn’t want to give too much information to their competitors, which results in a severely limited amount of features that could be used to build a good predictive model. Here are the common movie-performance-related features present in the `title.basics.tsv.gz` file:

*   **tconst**: unique identifier of the title
*   **titleType**: the type/format of the title (e.g. movie, tvmovie, short, tvseries, etc)
*   **primaryTitle**: the more popular title / the title used by the filmmakers on promotional materials at the point of release
*   **isAdult**: 0: non-adult title; 1: adult title
*   **startYear**: represents the release year of a title.
*   **runtimeMinutes**: primary runtime of the title, in minutes
*   **genres**: includes up to three genres associated with the title

This is a sensible schema for describing a movie, although it lacks some important information that would be very useful to determine movie quality such as production company, summary blurbs, granular genres/tags, and plot/setting — all of which are available on the IMDb movie page itself and presumably accessible through the [paid API](https://developer.imdb.com/documentation/api-documentation/?ref_=/documentation/_PAGE_BODY). Of note, since the assignment explicitly asks for a _movie_’s average rating, we need to filter the data to only `movie` and `tvMovie` entries, which the original assignment failed to do.

The ratings data in `title.ratings.tsv.gz` is what you’d expect:

*   **tconst**: unique identifier of the title (which can therefore be mapped to movie metadata using a JOIN)
*   **averageRating**: average of all the individual user ratings
*   **numVotes**: number of votes the title has received

In order to ensure that the average ratings for modeling are indeed stable and indicative of user sentiment, I will only analyze movies that have _atleast 30 user votes_: as of May 10th 2025, that’s about 242k movies total. Additionally, I will not use `numVotes` as a model feature, since that’s a metric based more on extrinsic movie popularity rather than the movie itself.

The last major dataset is `title.principals.tsv.gz`, which has very helpful information on metadata such as the roles people play in the production of a movie:

*   **tconst**: unique identifier of the title (which can be mapped to movie data using a JOIN)
*   **nconst**: unique identifier of the principal (this is mapped to `name.basics.tsv.gz` to get the principal’s `primaryName`, but nothing else useful)
*   **category**: the role the principal served in the title, such as `actor`, `actress`, `writer`, `producer`, etc.
*   **ordering**: the ordering of the principals within the title, which correlates to the order the principals appear on IMDb’s movie cast pages.

Additionally, because the datasets are so popular, it’s not the first time someone has built a IMDb ratings predictor and it’s easy to Google.

![Image 3](https://minimaxir.com/2025/06/movie-embeddings/google.webp)
Instead of using the official IMDb datasets, these analyses are based on the smaller [IMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset/data) hosted on Kaggle, which adds metadata such as movie rating, budget, and further actor metadata that make building a model much easier (albeit “number of likes on the lead actor’s Facebook page” is _very_ extrinsic to movie quality). Using the official datasets with much less metadata is building the models on hard mode and will likely have lower predictive performance.

Although IMDb data is very popular and very well documented, that doesn’t mean it’s easy to work with.

The Initial Assignment and “Feature Engineering”
------------------------------------------------

Data science take-home assignments are typically 1/2 [exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) for identifying impactful dataset features, and 1/2 building, iterating, and explaining the model. For real-world datasets, these are all very difficult problems with many difficult solutions, and the goal from the employer’s perspective is seeing more _how_ these problems are solved rather than the actual quantitative results.

The initial Reddit post decided to engineer some expected features using [pandas](https://pandas.pydata.org/), such as `is_sequel` by checking whether a non-`1` number is present at the end of a movie title and [one-hot encoding](https://en.wikipedia.org/wiki/One-hot) each distinct `genre` of a movie. These are fine for an initial approach, albeit sequel titles can be idiosyncratic and it suggests that a more [NLP](https://www.ibm.com/think/topics/natural-language-processing) approach to identifying sequels and other related media may be useful.

The main trick with this assignment is how to handle the principals. The common data science approach would be to use a sparse binary encoding of the actors/directors/writers, e.g. using a vector where actors present in the movie are `1` and every other actor is `0`, which leads to a large number of potential approaches to encode this data performantly, such as scikit-learn’s [MultiLabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html). The problem with this approach is that there are a _very_ large number of unique actors / [high cardinality](https://docs.honeycomb.io/get-started/basics/observability/concepts/high-cardinality/) — more unique actors than data points themselves — which leads to [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality) issues and workarounds such as encoding only the top _N_ actors will lead to the feature being uninformative since even a generous _N_ will fail to capture the majority of actors.

![Image 4: There are actually 624k unique actors in this dataset (Jupyter Notebook), the chart just becomes hard to read at that point.](https://minimaxir.com/2025/06/movie-embeddings/actor_cum_dist.png)

There are actually 624k unique actors in this dataset ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/actor_agg.ipynb)), the chart just becomes hard to read at that point.

Additionally, most statistical modeling approaches cannot account for the `ordering` of actors as they treat each feature as independent, and since the billing order of actors is generally correlated to their importance in the movie, that’s an omission of relevant information to the problem.

These constraints gave me an idea: why not use an LLM to encode _all_ movie data, and build a model using the downstream embedding representation? LLMs have [attention mechanisms](https://en.wikipedia.org/wiki/Attention_%28machine_learning%29), which will not only respect the relative ordering of actors (to give higher predictive priority to higher-billed actors, along with actor cooccurrences), but also identify patterns within movie name texts (to identify sequels and related media semantically).

I started by aggregating and denormalizing all the data locally ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/imdb_polars_etl_test.ipynb)). Each of the IMDb datasets are hundreds of megabytes and hundreds of thousands of rows at minimum: not quite [big data](https://en.wikipedia.org/wiki/Big_data), but enough to be more cognizant of tooling especially since computationally-intensive JOINs are required. Therefore, I used the [Polars](https://pola.rs/) library in Python, which not only loads data super fast, but is also one of the [fastest libraries at performing JOINs](https://duckdblabs.github.io/db-benchmark/) and other aggregation tasks. Polars’s syntax also allows for some cool tricks: for example, I want to spread out and aggregate the principals (4.1 million rows after prefiltering) for each movie into directors, writers, producers, actors, and all other principals into nested lists while simultaneously having them sorted by `ordering` as noted above. This is much easier to do in Polars than any other data processing library I’ve used, and on millions of rows, this takes _less than a second_:

```
df_principals_agg = (
    df_principals.sort(["tconst", "ordering"])
    .group_by("tconst")
    .agg(
        director_names=pl.col("primaryName").filter(pl.col("category") == "director"),
        writer_names=pl.col("primaryName").filter(pl.col("category") == "writer"),
        producer_names=pl.col("primaryName").filter(pl.col("category") == "producer"),
        actor_names=pl.col("primaryName").filter(
            pl.col("category").is_in(["actor", "actress"])
        ),
        principal_names=pl.col("primaryName").filter(
            ~pl.col("category").is_in(
                ["director", "writer", "producer", "actor", "actress"]
            )
        ),
        principal_roles=pl.col("category").filter(
            ~pl.col("category").is_in(
                ["director", "writer", "producer", "actor", "actress"]
            )
        ),
    )
)
```

After some cleanup and field renaming, here’s an example JSON document for [Star Wars: Episode IV - A New Hope](https://www.imdb.com/title/tt0076759/):

```
{
  "title": "Star Wars: Episode IV - A New Hope",
  "genres": [
    "Action",
    "Adventure",
    "Fantasy"
  ],
  "is_adult": false,
  "release_year": 1977,
  "runtime_minutes": 121,
  "directors": [
    "George Lucas"
  ],
  "writers": [
    "George Lucas"
  ],
  "producers": [
    "Gary Kurtz",
    "Rick McCallum"
  ],
  "actors": [
    "Mark Hamill",
    "Harrison Ford",
    "Carrie Fisher",
    "Alec Guinness",
    "Peter Cushing",
    "Anthony Daniels",
    "Kenny Baker",
    "Peter Mayhew",
    "David Prowse",
    "Phil Brown"
  ],
  "principals": [
    {
      "John Williams": "composer"
    },
    {
      "Gilbert Taylor": "cinematographer"
    },
    {
      "Richard Chew": "editor"
    },
    {
      "T.M. Christopher": "editor"
    },
    {
      "Paul Hirsch": "editor"
    },
    {
      "Marcia Lucas": "editor"
    },
    {
      "Dianne Crittenden": "casting_director"
    },
    {
      "Irene Lamb": "casting_director"
    },
    {
      "Vic Ramos": "casting_director"
    },
    {
      "John Barry": "production_designer"
    }
  ]
}
```

I was tempted to claim that I used zero feature engineering, but that wouldn’t be accurate. The selection and ordering of the JSON fields here is itself feature engineering: for example, `actors` and `principals` are intentionally last in this JSON encoding because they can have wildly varying lengths while the prior fields are more consistent, which should make downstream encodings more comparable and consistent.

Now, let’s discuss how to convert these JSON representations of movies into embeddings.

Creating And Visualizing the Movie Embeddings
---------------------------------------------

LLMs that are trained to output text embeddings are not much different from LLMs like [ChatGPT](https://chatgpt.com/) that just predict the next token in a loop. Models such as BERT and GPT can generate “embeddings” out-of-the-box by skipping the prediction heads of the models and instead taking an encoded value from the last hidden state of the model (e.g. for BERT, the first positional vector of the hidden state representing the `[CLS]` token). However, text embedding models are more optimized for distinctiveness of a given input text document using [contrastive learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/). These embeddings can be used for many things, from finding similar encoded inputs by identifying the similarity between embeddings, and of course, by building a statistical model on top of them.

Text embeddings that leverage LLMs are typically generated using a GPU in batches due to the increased amount of computation needed. Python libraries such as [Hugging Face](https://huggingface.co/)[transformers](https://huggingface.co/docs/transformers/en/index) and [sentence-transformers](https://sbert.net/) can load these embeddings models. For this experiment, I used the very new [Alibaba-NLP/gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) text embedding model that is finetuned from the [ModernBERT model](https://huggingface.co/answerdotai/ModernBERT-base) specifically for the embedding use case for two reasons: it uses the ModernBERT architecture which is [optimized for fast inference](https://huggingface.co/blog/modernbert), and the base ModernBERT model is trained to be more code-aware and should be able understand JSON-nested input strings more robustly — that’s also why I intentionally left in the indentation for nested JSON arrays as it’s semantically meaningful and [explicitly tokenized](https://huggingface.co/answerdotai/ModernBERT-base/blob/main/tokenizer_config.json). [3](https://minimaxir.com/2025/06/movie-embeddings/#fn:3)

The code ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/generate_imdb_embeddings.ipynb)) — with extra considerations to avoid running out of memory on either the CPU or GPU [4](https://minimaxir.com/2025/06/movie-embeddings/#fn:4) — looks something like this:

```
device = "cuda:0"
dataloader = torch.utils.data.DataLoader(docs, batch_size=32,
                                         shuffle=False,
                                         pin_memory=True,
                                         pin_memory_device=device)

dataset_embeddings = []
for batch in tqdm(dataloader, smoothing=0):
    tokenized_batch = tokenizer(
        batch, max_length=8192, padding=True, truncation=True, return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        outputs = model(**tokenized_batch)
        embeddings = outputs.last_hidden_state[:, 0].detach().cpu()
    dataset_embeddings.append(embeddings)

dataset_embeddings = torch.cat(dataset_embeddings)
dataset_embeddings = F.normalize(dataset_embeddings, p=2, dim=1)
```

![Image 5](https://minimaxir.com/2025/06/movie-embeddings/featured.webp)
I used a Spot [L4 GPU](https://cloud.google.com/blog/products/compute/introducing-g2-vms-with-nvidia-l4-gpus) on [Google Cloud Platform](https://cloud.google.com/) at a pricing of $0.28/hour, and it took 21 minutes to encode all 242k movie embeddings: about $0.10 total, which is surprisingly efficient.

Each of these embeddings is a set of 768 numbers (768D). If the embeddings are unit normalized (the `F.normalize()` step), then calculating the dot product between embeddings will return the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) of those movies, which can then be used to identify the most similar movies. But “similar” is open-ended, as there are many dimensions how a movie could be considered similar.

Let’s try a few movie similarity test cases where I calculate the cosine similarity between one query movie and _all_ movies, then sort by cosine similarity to find the most similar ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/movie_embeddings_similarity.ipynb)). How about Peter Jackson’s [Lord of the Rings: The Fellowship of the Ring](https://www.imdb.com/title/tt0120737/)? Ideally, not only would it surface the two other movies of the original trilogy, but also its prequel Hobbit trilogy.

| title | cossim |
| --- | --- |
| [The Lord of the Rings: The Fellowship of the Ring (2001)](https://www.imdb.com/title/tt0120737/) | 1.0 |
| [The Lord of the Rings: The Two Towers (2002)](https://www.imdb.com/title/tt0167261/) | 0.922 |
| [The Lord of the Rings: The Return of the King (2003)](https://www.imdb.com/title/tt0167260/) | 0.92 |
| [National Geographic: Beyond the Movie - The Lord of the Rings: The Fellowship of the Ring (2001)](https://www.imdb.com/title/tt10127200/) | 0.915 |
| [A Passage to Middle-earth: The Making of ‘Lord of the Rings’ (2001)](https://www.imdb.com/title/tt0301246/) | 0.915 |
| [Quest for the Ring (2001)](https://www.imdb.com/title/tt0299105/) | 0.906 |
| [The Lord of the Rings (1978)](https://www.imdb.com/title/tt0077869/) | 0.893 |
| [The Hobbit: The Battle of the Five Armies (2014)](https://www.imdb.com/title/tt2310332/) | 0.891 |
| [The Hobbit: The Desolation of Smaug (2013)](https://www.imdb.com/title/tt1170358/) | 0.883 |
| [The Hobbit: An Unexpected Journey (2012)](https://www.imdb.com/title/tt0903624/) | 0.883 |

Indeed, it worked and surfaced both trilogies! The other movies listed are about the original work, so having high similarity would be fair.

Compare these results to the “[More like this](https://help.imdb.com/article/imdb/discover-watch/what-is-the-more-like-this-section/GPE7SPGZREKKY7YN)” section on the IMDb page for the movie itself, which has the two sequels to the original Lord of the Rings and two other suggestions that I am not entirely sure are actually related.

![Image 6](https://minimaxir.com/2025/06/movie-embeddings/lotr_related.webp)
What about more elaborate franchises, such as the [Marvel Cinematic Universe](https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe)? If you asked for movies similar to [Avengers: Endgame](https://www.imdb.com/title/tt4154796/), would other MCU films be the most similar?

| title | cossim |
| --- | --- |
| [Avengers: Endgame (2019)](https://www.imdb.com/title/tt4154796/) | 1.0 |
| [Avengers: Infinity War (2018)](https://www.imdb.com/title/tt4154756/) | 0.909 |
| [The Avengers (2012)](https://www.imdb.com/title/tt0848228/) | 0.896 |
| [Endgame (2009)](https://www.imdb.com/title/tt1217616/) | 0.894 |
| [Captain Marvel (2019)](https://www.imdb.com/title/tt4154664/) | 0.89 |
| [Avengers: Age of Ultron (2015)](https://www.imdb.com/title/tt2395427/) | 0.882 |
| [Captain America: Civil War (2016)](https://www.imdb.com/title/tt3498820/) | 0.882 |
| [Endgame (2001)](https://www.imdb.com/title/tt0292502/) | 0.881 |
| [The Avengers (1998)](https://www.imdb.com/title/tt0118661/) | 0.877 |
| [Iron Man 2 (2010)](https://www.imdb.com/title/tt1228705/) | 0.876 |

The answer is yes, which isn’t a surprise since those movies share many principals. Although, there are instances of other movies named “Endgame” and “The Avengers” which are completely unrelated to Marvel and therefore implies that the similarities may be fixated on the names.

What about movies of a smaller franchise but a specific domain, such as Disney’s [Frozen](https://www.imdb.com/title/tt2294629/) that only has one sequel? Would it surface other 3D animated movies by [Walt Disney Animation Studios](https://en.wikipedia.org/wiki/Walt_Disney_Animation_Studios), or something else?

| title | cossim |
| --- | --- |
| [Frozen (2013)](https://www.imdb.com/title/tt2294629/) | 1.0 |
| [Frozen II (2019)](https://www.imdb.com/title/tt4520988/) | 0.93 |
| [Frozen (2010)](https://www.imdb.com/title/tt1323045/) | 0.92 |
| [Frozen (2010)](https://www.imdb.com/title/tt1611845/) [a different one] | 0.917 |
| [Frozen (1996)](https://www.imdb.com/title/tt0125279/) | 0.909 |
| [Frozen (2005)](https://www.imdb.com/title/tt0376606/) | 0.9 |
| [The Frozen (2012)](https://www.imdb.com/title/tt2363439/) | 0.898 |
| [The Story of Frozen: Making a Disney Animated Classic (2014)](https://www.imdb.com/title/tt4007494/) | 0.894 |
| [Frozen (2007)](https://www.imdb.com/title/tt1071798/) | 0.889 |
| [Frozen in Time (2014)](https://www.imdb.com/title/tt4150316/) | 0.888 |

…okay, it’s definitely fixating on the name. Let’s try a different approach to see if we can find more meaningful patterns in these embeddings.

In order to visualize the embeddings, we can project them to a lower dimensionality with a dimensionality reduction algorithm such as [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) or [UMAP](https://umap-learn.readthedocs.io/en/latest/): UMAP is preferred as it can simultaneously reorganize the data into more meaningful clusters. UMAP’s [construction of a neighborhood graph](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html), in theory, can allow the reduction to refine the similarities by leveraging many possible connections and hopefully avoid fixating on the movie name. However, with this amount of input data and the relatively high initial 768D vector size, the computation cost of UMAP is a concern as both factors each cause the UMAP training time to scale exponentially. Fortunately, NVIDIA’s [cuML library](https://github.com/rapidsai/cuml) recently [updated](https://github.com/rapidsai/cuml/releases/tag/v25.04.00) and now you can run UMAP with very high amounts of data on a GPU at a very high number of epochs to ensure the reduction fully converges, so I did just that ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/imdb_embeddings_umap_to_2D.ipynb)). What patterns can we find? Let’s try plotting the reduced points, colored by their user rating.

![Image 7](https://minimaxir.com/2025/06/movie-embeddings/imdb_umap_rating.webp)
So there’s a few things going on here. Indeed, most of the points are high-rating green as evident in the source data. But the points and ratings aren’t _random_ and there are trends. In the center giga cluster, there are soft subclusters of movies at high ratings and low ratings. Smaller discrete clusters did indeed form, but what is the deal with that extremely isolated cluster at the top? After investigation, that cluster only has movies released in 2008, which is another feature I should have considered when defining movie similarity.

As a sanity check, I faceted out the points by movie release year to better visualize where these clusters are forming:

![Image 8](https://minimaxir.com/2025/06/movie-embeddings/imdb_umap_rating_year.webp)
This shows that even the clusters movies have their values spread, but I unintentionally visualized how [embedding drift](https://arize.com/docs/ax/machine-learning/computer-vision/how-to-cv/embedding-drift) changes over time. 2024 is also a bizarrely-clustered year: I have no idea why those two years specifically are weird in movies.

The UMAP approach is more for fun, since it’s better for the downstream model building to use the raw 768D vector and have it learn the features from that. At the least, there’s _some_ semantic signal preserved in these embeddings, which makes me optimistic that these embeddings alone can be used to train a viable movie rating predictor.

So, we now have hundreds of thousands of 768D embeddings. How do we get them to predict movie ratings? What many don’t know is that all methods of traditional statistical modeling also work with embeddings — assumptions such as feature independence are invalid so the results aren’t explainable, but you can still get a valid predictive model.

First, we will shuffle and split the data set into a training set and a test set: for the test set, I chose 20,000 movies (roughly 10% of the data) which is more than enough for stable results. To decide the best model, we will be using the model that minimizes the [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) (MSE) of the test set, which is a standard approach to solving regression problems that predict a single numeric value.

Here are three approaches for using LLMs for solving non-next-token-prediction tasks.

### Method #1: Traditional Modeling (w/ GPU Acceleration!)

You can still fit a linear regression on top of the embeddings even if feature coefficients are completely useless and it serves as a decent baseline ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/cuml_grid_search.ipynb)). The absolute laziest “model” where we just use the mean of the training set for every prediction results in a test MSE of **1.637**, but performing a simple linear regression on top of the 768D instead results in a more reasonable test MSE of **1.187**. We should be able to beat that handily with a more advanced model.

Data scientists familiar with scikit-learn know there’s a rabbit hole of model options, but most of them are CPU-bound and single-threaded and would take considerable amount of time on a dataset of this size. That’s where cuML—the same library I used to create the UMAP projection—comes in, as cuML has [GPU-native implementations](https://docs.rapids.ai/api/cuml/stable/api/#regression-and-classification) of most popular scikit-learn models with a similar API. This notably includes [support vector machines](https://en.wikipedia.org/wiki/Support_vector_machine), which play especially nice with embeddings. And because we have the extra compute, we can also perform a brute force hyperparameter [grid search](https://www.dremio.com/wiki/grid-search/) to find the best parameters for fitting each model.

Here’s the results of MSE on the test dataset for a few of these new model types, with the hyperparameter combination for each model type that best minimizes MSE:

![Image 9](https://minimaxir.com/2025/06/movie-embeddings/model_comparison_base.png)
The winner is the Support Vector Machine, with a test MSE of **1.087**! This is a good start for a simple approach that handily beats the linear regression baseline, and it also beats the model training from the Redditor’s original notebook which had a test MSE of 1.096 [5](https://minimaxir.com/2025/06/movie-embeddings/#fn:5). In all cases, the train set MSE was close to the test set MSE, which means the models did not overfit either.

### Method #2: Neural Network on top of Embeddings

Since we’re already dealing with AI models and already have PyTorch installed to generate the embeddings, we might as well try the traditional approach of training a [multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron) (MLP) neural network on top of the embeddings ([Jupyter Notebook](https://github.com/minimaxir/imdb-embeddings/blob/main/pytorch_model_train_mlp.ipynb)). This workflow sounds much more complicated than just fitting a traditional model above, but PyTorch makes MLP construction straightforward, and Hugging Face’s [Trainer class](https://huggingface.co/docs/transformers/en/main_classes/trainer) incorporates best model training practices by default, although its `compute_loss` function has to be tweaked to minimize MSE specifically.

The PyTorch model, using a loop to set up the MLP blocks, looks something like this:

```
class RatingsModel(nn.Module):
    def __init__(self, linear_dims=256, num_layers=6):
        super().__init__()

        dims = [768] + [linear_dims] * num_layers
        self.mlp = nn.ModuleList([
            nn.Sequential(
                nn.Linear(dims[i], dims[i+1]),
                nn.GELU(),
                nn.BatchNorm1d(dims[i+1]),
                nn.Dropout(0.6)
            ) for i in range(len(dims)-1)
        ])

        self.output = nn.Linear(dims[-1], 1)

    def forward(self, x, targets=None):
        for layer in self.mlp:
            x = layer(x)

        return self.output(x).squeeze()  # return 1D output if batched inputs
```

This MLP is 529k parameters total: large for a MLP, but given the 222k row input dataset, it’s not egregiously so.

The real difficulty with this MLP approach is that it’s _too effective_: even with less than 1 million parameters, the model will extremely overfit and converge to 0.00 train MSE quickly, while the test set MSE explodes. That’s why `Dropout` is set to the atypically high probability of `0.6`.

Fortunately, MLPs are fast to train: training for 600 epochs (tota