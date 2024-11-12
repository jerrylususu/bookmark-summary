Title: Binary vector embeddings are so cool

URL Source: https://emschwartz.me/binary-vector-embeddings-are-so-cool/

Markdown Content:
_Nov 11, 2024_

Vector embeddings by themselves are pretty neat. Binary quantized vector embeddings are extra impressive. In short, they can _retain 95+% retrieval accuracy with 32x compression and ~25x retrieval speedup_. Let's get into how this works and why it's so crazy.

What are embeddings?
--------------------

Embeddings let you turn an arbitrary piece of text into a series of numbers that manage to represent the meaning of the content. These embedding vectors can range in dimension from 512 on the shorter end all the way up to 8192 or more. Typically each of the weights in the vector is represented as a 32-bit floating point number.

LLMs use embeddings to represent input text, but embeddings can also be used on their own.

Embeddings enable you to easily search for pieces of content that have similar meanings by finding the similarity (commonly the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)) between the points represented by the vectors.

[HuggingFace](https://huggingface.co/blog/matryoshka) has some nice diagrams depicting this:

![Image 1: embeddings](https://bear-images.sfo2.cdn.digitaloceanspaces.com/emschwartz/embeddings.webp)

And this one shows how the first two texts are more similar than the second and third:

![Image 2: cosine-similarity](https://bear-images.sfo2.cdn.digitaloceanspaces.com/emschwartz/cosine-similarity.webp)

Embeddings are a powerful addition to use cases where you might otherwise use full-text search or a custom ML model to search for relevant items. It's especially nice that you can directly use one of the [many](https://huggingface.co/spaces/mteb/leaderboard) permissively-licensed embedding models without needing to train one yourself.

Binary quantization
-------------------

Binary quantization takes each of the 32-bit floating point weights in a vector embedding and converts them to a single bit. If the original weight was greater than 0, map it to a 1, otherwise map it to a 0.

Instead of using the cosine similarity, you use the [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) (simply counting how many bits are different) to search for similar content.

The mind-blowing fact about binary quantized vector embeddings is how much information they manage to retain.

The March 2024 blog post [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization) co-authored by [MixedBread.ai](https://www.mixedbread.ai/) and HuggingFace presents the following results for MixedBread's [`mxbai-embed-large-v1`](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) model:

| Quantization | Embedding size (bytes) | Percentage of default embedding size | MTEB Retrieval Score | Percentage of Default Performance |
| --- | --- | --- | --- | --- |
| float32 (default) | 4096 | 100% | 54.39 | 100% |
| int8 | 1024 | 25% | 52.79 | 97% |
| binary | 128 | **3.125% 👈** | 52.46 | **96.45% 🤯🤯🤯** |

Some other models also retain a high percentage of their default performance when using binary quantized embeddings:

*   [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) retains 93.79% of its performance
*   [`nomic-embed-text-v1.5`](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) retains 87.7%
*   [`cohere-embed-english-v3.0`](https://txt.cohere.com/introducing-embed-v3/) (a proprietary model) retains 94.6%

In a conversation, [Alex Kesling](https://www.linkedin.com/in/alexkesling/) commented that this technique is similar to why JPEG compression works. You can drop a huge percentage of the size while retaining enough signal to keep the image looking pretty good.

Comparison to Matryoshka embeddings
-----------------------------------

Another approach to shrinking embeddings is Matryoshka Representation Learning or [Matryoshka embeddings](https://huggingface.co/blog/matryoshka). This approach is named after the Russian nesting dolls.

Put simply, embedding models trained to support Matryoshka embeddings put the most important information at the front of the vector. This enables the embeddings to be sliced and retain a relatively high degree of performance.

This technique is widely used to shrink embeddings. For example, OpenAI's `text-embedding-3-large` produces embeddings with 3072 dimensions by default. It can support [reducing the dimensions to 1024 or even 256](https://openai.com/index/new-embedding-models-and-api-updates/#native-support-for-shortening-embeddings), though of course with slightly reduced accuracy (99% and 96%, respectively).

Let's take a look at how MixedBread's `mxbai-embed-large-v1` handles truncating the number of dimensions:

| Dimensions | Embedding size (bytes) | Percentage of default embedding size | MTEB Retrieval Score | Percentage of Default Performance |
| --- | --- | --- | --- | --- |
| 1024 (default) | 4096 | 100% | 54.39 | 100% |
| 512 | 2048 | 50% | 51.79 | 95.22% |
| 256 | 1024 | 25% | 46.78 | 86.01% |
| 128 | 512 | 12.5% | 36.63 | 67.34% |
| 64 | 256 | 6.25% | 18.63 | 34.35% |

You can see that there is a pretty steep drop-off on performance when slicing the vector to less than 50% or 25% of its original size. In contrast, binary quantization can retain high accuracy while shrinking the vector to only 3% of its original size.

Binary-quantized Matryoshka embeddings
--------------------------------------

Of course the good folks at MixedBread went ahead and [combined the two techniques](https://www.mixedbread.ai/blog/binary-mrl). What if you slice the vectors _and_ quantize each of the weights to a single bit?

| Dimensions | Embedding size (bytes) | Percentage of default embedding size | MTEB Retrieval Score | Percentage of Default Performance |
| --- | --- | --- | --- | --- |
| 1024 | 128 | 3.13% | 52.46 | 96.46% |
| 512 | 64 | **1.56% 👈** | 49.37 | **90.76% 👈** |
| 256 | 32 | 0.78% | 43.25 | 79.52% |
| 128 | 16 | 0.39% | 32.80 | 60.31% |
| 64 | 8 | Oh just stop it, right? | 17.61 | 32.38% |

As before, there is a pretty steep drop-off if you slice off too many dimensions. However, retaining 90.76% accuracy with an embedding that's only 1.56% the size of the original is pretty impressive!

Binary embeddings are smaller **and** faster
--------------------------------------------

Of course using binary embeddings would save you a decent amount on your storage bill. However, it's also worth noting that doing the distance calculations are also considerably faster.

Calculating the Hamming distance between binary vectors takes only a couple of CPU clock cycles for XORing and counting the number of 1's. In contrast, calculating the cosine distance between float32 vectors requires floating point multiplication, addition, square roots, and division, which are all more computationally expensive.

The HuggingFace [blog post](https://huggingface.co/blog/embedding-quantization#retrieval-speed) includes some benchmark results for retrieval using float32 and binary quantized vectors. The binary quantized vectors had a **15x-45x speedup with a mean of 25x**!

Conclusion
----------

I am using MixedBread's model to build a [personalized content feed](https://scour.emschwartz.me/). At one point, I noticed that my vector similarity lookups were getting a little slow. I'm not currently using a vector database (for reasons I'll explain in another post) so I considered switching to one or pre-computing distances between my vectors. Before making the decision, however, I found MixedBread's post about binary quantization and tried that out.

The speed up just from using the Hamming distance between binary vectors instead of cosine similarity between float32 vectors was enough that, at least for now, it solved my speed issue. No change of infra needed!

I think binary quantized vector embeddings are pretty mind-blowing. It seems somewhat counter-intuitive that you could reduce a 4-byte floating point number to a single bit and retain enough signal to implement vector similarity search with reasonably high accuracy. Of course, a 1024-dimension bit vector still has 2^1024 possible values, which is _a lot_. Nevertheless, a 32x compression with only a 3.5% drop in quality and a 25x boost in lookup speed is very impressive. I'll be keeping an eye on MixedBread's future work!

* * *

Discuss on [Lobsters](https://lobste.rs/s/f6hsm1/binary_vector_embeddings_are_so_cool), [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1gov1q4/binary_vector_embeddings_are_so_cool/), or [Hacker News](https://news.ycombinator.com/item?id=42107196).

* * *

[#ai](https://emschwartz.me/blog/?q=ai) [#appreciation](https://emschwartz.me/blog/?q=appreciation) [#best](https://emschwartz.me/blog/?q=best) [#embeddings](https://emschwartz.me/blog/?q=embeddings) [#scour](https://emschwartz.me/blog/?q=scour)
