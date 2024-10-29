Title: Why Perfect Clustering Algorithms Don't Exist

URL Source: https://blog.codingconfessions.com/p/the-cap-theorem-of-clustering

Published Time: 2024-10-29T09:00:44+00:00

Markdown Content:
As software engineers, we use clustering algorithms all the time. Whether it's grouping similar users, categorizing content, or detecting patterns in data, clustering seems deceptively simple: just group similar things together, right? You might have used k-means, DBSCAN, or agglomerative clustering, thinking you just need to pick the right algorithm for your use case.

But here's what most tutorials won't tell you: every clustering algorithm you choose is fundamentally flawed. Not because of poor implementation or wrong parameters, but because of the math itself. In 2002, [Jon Kleinberg](https://www.cs.cornell.edu/home/kleinber/) (in a [paper](https://www.cs.cornell.edu/home/kleinber/nips15.pdf) published at NIPS 2002) proved something that should make every developer pause: it's impossible for any clustering algorithm to have all three properties we'd naturally want it to have.

Think of it as the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) of clustering. Just as distributed systems force you to choose between consistency, availability, and partition tolerance, Kleinberg showed that clustering algorithms force you to pick between scale invariance, richness, and consistency. You can't have all three – ever, it’s a mathematical impossibility.

Before you deploy your next clustering solution in production, you need to understand what you're giving up. Let's dive into these three properties and see why you'll always have to choose what to sacrifice.

Before we talk about the theorem, we need a precise definition of clustering. The paper defines it in terms of the set of data points and the distance function as defined below:

We refer to the data being clustered as the set `S` of n points.

In order to perform the clustering, the clustering model needs to compute pairwise distance between each data point and for that it needs a distance function.

The distance function is a mathematical function which takes two data points `i` and `j` as parameters, and computes the distance between them. If the parameters `i` and `j` are the same data points then the distance between them as computed by this function should be 0.

Finally, the paper defines clustering as a function of the distance function `d`, and the set of data points `S` such that it partitions `S` into smaller subsets where each subset represent a cluster. Mathematically speaking:

> _In terms of the distance function d, the clustering function can be defined as a function ƒ that takes a distance function d on S and returns a partition Γ of S._

For instance, the k-means algorithm takes the number of clusters k, a distance function (such as the [Euclidean distance function](https://en.wikipedia.org/wiki/Euclidean_distance)), and the set of data points as input, and results in k clusters as its output. These k clusters are essentially a partition of the original dataset `S`.

We want our clustering algorithm to exhibit three desirable properties, which are termed as scale-invariance, richness, and consistency. Let’s understand what these properties mean.

Scale invariance is a property that sounds almost too obvious: if you take your data points and scale all distances between them by the same factor, your clusters shouldn't change.

For instance, if for any two points i,j in the dataset the distance between them is d(i,j). Then, if we scale this distance by a factor 𝛼 such that it becomes 𝛼.d(i,j) then the clustering result should remain unchanged. This means that the clustering algorithm is invariant to the scale.

In the real world, this matters more than you might think. Have you ever:

*   Changed your measurement units (like feet to meters)
    
*   Normalized your data differently
    
*   Applied a different scaling to your features only to find your clustering results completely changed? That's what happens when your algorithm isn't scale invariant.
    

Richness is about possibilities — a clustering algorithm should be capable of producing any grouping that might make sense for your data.

Imagine you're sorting your wardrobe. Sometimes you might want to group clothes by color (creating many clusters), other times by season (four clusters), or simply into 'wear now' and 'store away' (two clusters). A truly rich clustering algorithm should be able to handle all these possibilities, not force you into a predetermined number of groups.

But many popular algorithms fail this requirement. Take k-means, for instance. The moment you specify k=3, you've already ruled out any possibility of finding two clusters or four clusters, even if that's what your data naturally suggests. It's like forcing your wardrobe into exactly three groups, even if that doesn't make sense for your clothes.

Mathematically speaking: if `f` is our clustering function and `S` is our dataset, richness means that `f` should be able to produce any possible partitioning of `S`. In other words, `range(f)` should equal the set of all possible ways to partition `S`.

While this flexibility sounds great in theory, you can probably see why many practical algorithms sacrifice it. When you're analyzing real data, you often want to control the number of clusters to make the results interpretable

The third property, consistency, means that if your existing clusters are good, making similar points more similar and different points more different shouldn't change these clusters.

Let's break this down with a simple example. Imagine you've clustered movies into genres based on their characteristics. Now:

*   Two action movies add even more explosive scenes, making them more similar to each other
    
*   Meanwhile, a romance movie adds more romantic scenes, making it even more different from the action movies
    

Consistency means that if these changes only reinforce the existing grouping, your clustering algorithm shouldn't suddenly decide to reorganize the groups.

Mathematically speaking: if `Γ` is a clustering of points using distance function `d`, and we create a new distance function `d'` where:

*   For any two points `i`,`j` in the same cluster: `d'(i,j) < d(i,j)` (similar things become more similar)
    
*   For any two points `i`,`j` in different clusters: `d'(i,j) > d(i,j)` (different things become more different)
    

Then a consistent clustering algorithm should produce the same clustering `Γ` with `d'` as it did with `d`. This new distance function `d'` is called a `Γ` transformation of `d`.

**There is no clustering function which satisfies all three properties:** _**scale-invariance**_**,** _**richness**_ **and** _**consistency**_**.**

While Kleinberg proved this mathematically (check out his paper for the full proof), let's see how this 'pick two out of three' limitation shows up in algorithms you might be using today.

Single linkage is a form of hierarchical clustering. It starts simple: every point is its own cluster, and we gradually merge the closest clusters. The interesting part is deciding how to stop the algorithm. One of the three common criterion are used to stop the algorithm and each one has its trade off rooted in the impossibility theorem.

*   What we do: Stop clustering after we have k clusters
    
*   What we sacrifice: Richness
    
*   Why? We've locked ourselves into exactly k groups. Our algorithm will never discover any other groupings of size smaller or larger than k.
    

*   What we do: We keep merging clusters as long as their distance <\= some distance r. When all clusters are at a distance larger than r, the algorithm automatically stops.
    
*   What we sacrifice: Scale-invariance
    
*   Why? If we scale up our data by 2x (or some other factor), then clusters which were previously mergeable are suddenly too far apart and will not be merged. This changes the clustering output.
    

*   What we do: We calculate the maximum pairwise distance `ρ` within our dataset using some distance function `d1`. After that we only merge two clusters if their distance is <\= `αρ`, where `α` < 1.
    
*   What we sacrifice: Consistency
    
*   Why? Let’s say we change our distance function from `d1` to `d2`, such that d2 makes similar points more similar, and dissimilar points more dissimilar. More formally, `d2` is a `Γ` transformation of `d1`. Then by definition, the maximum pairwise distance obtained using `d2` will be larger than `ρ`, and as a result the clustering output obtained using `d2` will also be very different than the original clustering.
    

Centroid based clustering refers to the commonly used _k-means_ and _k-median_ algorithms. Where we start with a predefined _k_ number of clusters by selecting _k_ points in the data as centroids and then assigning each point to their nearest cluster. The algorithm iteratively optimizes the centroids of the k clusters by computing the mean (or the median) of each cluster, and then redistributing the points based on their nearest cluster centroid. The algorithm normally stops when the clusters become stable.

These algorithms suffer with the problem of not satisfying the _richness_ property because as soon as we fix the number of clusters k, automatically it eliminates the possibility of achieving all the possible clusterings as the output.

The paper proves that these algorithms don't satisfy the _consistency_ property as well. For instance, for k=2, k-means may come up with clusters X and Y. However, if we decrease the distance between the points within X, and Y, while increasing the distance between the points in X and Y, then the algorithm might come up with two completely different clusters as its output. The paper has a formal proof for this specific example which generalizes to k \> 2 as well.

Now you know why clustering algorithms force you to make sacrifices. It's not a flaw in implementation or a limitation we'll eventually overcome – it's mathematically impossible to have it all. Every clustering algorithm must give up either scale-invariance, richness, or consistency. There's no escape from this fundamental trade-off.

But once you understand what you're giving up, you can make this limitation work for you. Just like engineers choose between consistency and availability in distributed systems, you can strategically choose which clustering property to sacrifice:

*   Need your algorithm to handle data regardless of scale? You might have to give up richness.
    
*   Want the flexibility to discover any possible grouping? Be prepared to lose scale-invariance.
    
*   Need results to stay stable when cluster patterns become more pronounced? You'll probably sacrifice richness.
    

Instead of fighting these limitations, use them as a guide. Ask yourself:

*   What property matters most for your specific use case?
    
*   Which trade-off can your application tolerate?
    
*   How can you design your system knowing these inherent limitations?
    

Understanding Kleinberg's theorem doesn't just make you a better theorist – it makes you a more effective engineer. Because in the real world, success isn't about finding the perfect clustering algorithm (it doesn't exist). It's about choosing the right sacrifices for your specific needs.

If you find my work interesting and valuable, you can support me by opting for a paid subscription (it’s $6 monthly/$60 annual). As a bonus you get access to monthly live sessions, and all the past recordings.

Many people report failed payments, or don’t want a recurring subscription. For that I also have a [buymeacoffee page](https://buymeacoffee.com/codeconfessions). Where you can buy me coffees or become a member. I will upgrade you to a paid subscription for the equivalent duration here.

[Buy me a coffee](https://buymeacoffee.com/codeconfessions)

I also have a GitHub Sponsor page. You will get a sponsorship badge, and also a complementary paid subscription here.

[Sponsor me on GitHub](https://github.com/sponsors/abhinav-upadhyay)
