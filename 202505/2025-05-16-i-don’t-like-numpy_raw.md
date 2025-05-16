Title: I don’t like NumPy

URL Source: https://dynomight.net/numpy/

Published Time: 2025-05-15T00:00:00+00:00

Markdown Content:
They say you can’t truly hate someone unless you loved them first. I don’t know if that’s true as a general principle, but it certainly describes my relationship with NumPy.

[NumPy](https://numpy.org/), by the way, is some software that does computations on arrays in Python. It’s insanely popular and has had a huge influence on all the popular machine learning libraries like PyTorch. These libraries share most of the same issues I discuss below, but I’ll stick to NumPy for concreteness.

NumPy makes easy things easy. Say `A` is a `5×5` matrix, `x` is a length-5 vector, and you want to find the vector _y_ such that `Ay=x`. In NumPy, that would be:

```
y = np.linalg.solve(A, x)
```

So elegant! So clear!

But say the situation is even a _little_ more complicated. Say `A` is a stack of 100 `5×5` matrices, given as a `100×5×5` array. And say `x` is a stack of 100 length-5 vectors, given as a `100×5` array. And say you want to solve `Aᵢyᵢ=xᵢ` for `1≤i≤100`.

If you could use loops, this would be easy:

```
y = np.empty_like(x)
for i in range(100):
    y[i,:] = np.linalg.solve(A[i,:,:], x[i,:])
```

But you can’t use loops. To some degree, this is a limitation of loops being slow in Python. But nowadays, everything is GPU and if you’ve got big arrays, you probably don’t want to use loops in any language. To get all those transistors firing, you need to call special GPU functions that will sort of split up the arrays into lots of little pieces and process them in parallel.

The good news is that NumPy knows about those special routines (at least if you use [JAX](https://github.com/jax-ml/jax) or [CuPy](https://cupy.dev/)), and if you call `np.linalg.solve` correctly, it will use them.

The bad news is that no one knows how do that.

Don’t believe me? OK, which of these is right?

```
y = linalg.solve(A,x)
y = linalg.solve(A,x,axis=0)
y = linalg.solve(A,x,axes=[[1,2],1])
y = linalg.solve(A.T, x.T)
y = linalg.solve(A.T, x).T
y = linalg.solve(A, x[None,:,:])
y = linalg.solve(A,x[:,:,None])
y = linalg.solve(A,x[:,:,None])[:,:,0]
y = linalg.solve(A[:,:,:,None],x[:,None,None,:])
y = linalg.solve(A.transpose([1,2,0]),x[:,:,None]).T
```

No one knows. And let me show you something else. Here’s the [documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html):

![Image 1: np.linalg.solve](https://dynomight.net/img/numpy/solve.png)

Read that. Meditate on it. Now, notice: You _still_ don’t know how to solve `Aᵢyᵢ=xᵢ` for all `i` at once. Is it even possible? Did I lie when I said it was?

As far as I can tell, what people actually do is try random variations until one seems to work.

Why NumPy bad
-------------

NumPy is all about applying operations to arrays. When the arrays have 2 or fewer dimensions, everything is fine. But if you’re doing something even mildly complicated, you inevitably find yourself with some operation you want to apply to some dimensions of array `A`, some other dimensions of array `B`, and some _other_ dimensions of array `C`. And NumPy has no theory for how to express that.

Let me show you what I mean. Suppose:

*   `A` is a `K×L×M` array
*   `B` is a `L×N` array
*   `C` is a `K×M` array

And say that for each `k` and `n`, you’d like to compute the mean over the `L` and `M` dimensions. That is, you want

`Dkn = 1/(LM) × ∑lm Aklm Bln Ckm.`

To do that, you’ve got two options. The first is to use grotesque dimension alignment tricks:

```
D = np.mean(
        np.mean(
            A[:,:,:,None] *
            B[None,:,None,:] *
            C[:,None,:,None],
        axis=1),
    axis=1)
```

The hell, you ask? Why is `None` everywhere? Well, when indexing an array in NumPy, you can write `None` to insert a new dimension. `A` is `K×L×M`, but `A[:,:,:,None]` is `K×L×M×`**`1`**. Similarly, `B[None,:,None,:]` is **`1`**`×L×`**`1`**`×N` and `C[:,None,:,None]` is `K×`**`1`**`×M×`**`1`**. When you multiply these together, NumPy “broadcasts” all the size-1 dimensions to give a `K×L×M×N` array. Then, the `np.mean` calls average over the `L` and `M` dimensions.

I think this is bad. I’ve been using NumPy for years and I still find it impossible to write code like that without _always_ making mistakes.

It’s also borderline-impossible to read. To prove this, I just flipped a coin and introduced a bug above if and only if the coin was tails. Is there a bug? Are you _sure_? No one knows.

Your second option is to desperately try to be clever. Life is short and precious, but if you spend a lot of yours reading the NumPy documentation, you might eventually realize that there’s a function called [`np.tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html), and that it’s possible to make it do much of the work:

```
D = (1/L) * np.mean(
                np.tensordot(A, B, axes=[1,0]) *
                C[:,:,None],
            axis=1)
```

That’s correct. (I promise.) But why does it work? What exactly is `np.tensordot` doing? If you saw that code in some other context, would you have the slightest idea what was happening?

Here’s how I’d do it, if only I could use loops:

```
D = np.zeros((K,N))  
for k in range(K):  
    for n in range(N):  
        a = A[k,:,:]  
        b = B[:,n]  
        c = C[k,:]  
        assert a.shape == (L,M)  
        assert b.shape == (L,)  
        assert c.shape == (M,)  
        D[k,n] = np.mean(a * b[:,None] * c[None,:])
```

People who’ve written too much NumPy may find that clunky. I suspect that’s a wee bit of Stockholm Syndrome. But surely we can agree that it’s _clear_.

In practice, things are often even worse. Say that `A` had shape `M×K×L` rather than `K×L×M`. With loops, no big deal. But NumPy requires you to write monstrosities like `A.transpose([1,2,0])`. Or should that be `A.transpose([2,0,1])`? What shapes do those produce? No one knows.

Loops were better.

OK I lied
---------

There is a third option:

```
D = 1/(L*M) * np.einsum('klm,ln,km->kn', A, B, C)
```

If you’ve never seen Einstein summation before, that might look terrifying. But remember, our goal is to find

D kn = 1/(LM) × ∑lm A klm B ln C km.

The string in the above code basically gives labels to the indices in each of the three inputs (`klm,ln,km`) and the target indices for the output (`->kn`). Then, [`np.einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) multiplies together the corresponding elements of the inputs and sums over all indices that aren’t in the output.

Personally, I think `np.einsum` is one of the rare parts of NumPy that’s actually good. The strings are a bit tedious, but they’re worth it, because the overall function is easy(ish) to understand, is completely explicit, and is quite general and powerful.

Except, how does `np.einsum` achieve all this? It uses indices. Or, more precisely, it introduces a tiny _domain-specific language_ based on indices. It doesn’t suffer from NumPy’s design flaws because it refuses to play by NumPy’s normal rules.

But `np.einsum` only does a few things. ([Einops](https://github.com/arogozhnikov/einops) does a few more.) What if you want to apply some other function over various dimensions of some arrays? There is no `np.linalg.einsolve`. And if you create your own function, there’s _certainly_ no “Einstein” version of _it_.

I think `np.einsum`’s goodness shows that NumPy went somewhere.

Intermission
------------

Here’s a [painting](https://www.nga.gov/artworks/45858-burning-old-south-church-bath-maine) which feels analogous to our subject.

![Image 2](https://dynomight.net/img/numpy/burning.jpg)

Where did NumPy go wrong?
-------------------------

Here’s what I want from an array language. I ain’t particular about syntax, but it would be nice if:

1.   When you want to do something, it’s “obvious” how to do it.
2.   When you read some code, it’s “obvious” what it does.

Wouldn’t that be nice? I think NumPy doesn’t achieve these because of its original sin: It took away indices and replaced them with broadcasting. And broadcasting cannot fill indices’ shoes.

I don’t love NumPy broadcasting
-------------------------------

NumPy’s core trick is broadcasting. Take this code:

```
A = np.array([[1,2],[3,4],[5,6]])
B = np.array([10,20])
C = A * B
print(C)
```

This outputs:

```
[[ 10  40]
 [ 30  80]
 [ 50 120]]
```

Here, `A` is a `3×2` array, and `B` is a length-`2` array. When you multiply them together, `B` is “broadcast” to the shape of `A`, meaning the first column of `A` is multiplied with `B[0]=10` and the second is multiplied with `B[1]=20`.

In simple cases, this seems good. But I don’t love it. One reason is that, as we saw above, you often have to do gross things to the dimensions to get them to line up.

Another reason is that it isn’t explicit or legible. Sometimes `A*B` multiplies element-by-element, and sometimes it does more complicated things. So every time you see `A*B`, you have to figure out which case in the [broadcasting conventions](https://numpy.org/doc/stable/user/basics.broadcasting.html) is getting triggered.

But the real problem with broadcasting is how it infects everything else. I’ll explain below.

I don’t like NumPy indexing
---------------------------

Here’s a riddle. Take this code:

```
A = np.ones((10,20,30,40))
i = np.array([1,2,3])
j = np.array([[0],[1]])
B = A[:,i,j,:]
```

What shape does `B` have?

It turns out the answer is `10×2×3×40`. That’s because the `i` and `j` indices get broadcast to a shape of `2×3` and then something something mumble mumble mumble. Try to convince yourself it makes sense.

Done? OK, now try these:

```
C = A[:,:,i,j]
D = A[:,i,:,j]
E = A[:,1:4,j,:]
```

What shapes do these have?

*   `C` is `10×20×2×3`. This seems logical, given what happened with `B` above.

*   What about `D`? It is `2×3×10×30`. Now, for some reason, the `2` and `3` go at the beginning?

*   And what about `E`? Well, “slices” in Python exclude the endpoint, so `1:4` is equivalent to `[1,2,3]` which is equivalent to `i`, and so `E` is the same as `B`. Hahaha, just kidding! `E` is `10×3×2×1×40`.

Yes, that is what happens. Try it if you don’t believe me! I understand why NumPy does this, because I’ve absorbed [this 5000 word document](https://numpy.org/doc/stable/user/basics.indexing.html) that explains how NumPy indexing works. But I want that time back.

 For fun, I tried asking a bunch of AI models to figure out what shapes those arrays have. Here were the results: 
I used this query:

> Take this python code
> 
> 
> A = np.ones((10,20,30,40))
> 
>  i = np.array([1,2,3])
> 
>  j = np.array([[0],[1]])
> 
>  B = A[:,i,j,:]
> 
>  C = A[:,:,i,j]
> 
>  D = A[:,i,:,j]
> 
>  E = A[:,1:4,j,:]
> 
> 
> what shapes do B, C, D, and E have?

Claude 3.7 used “extended thinking”. Here are all the incorrect outputs:

| AI | `B` | `C` | `D` | `E` |
| --- | --- | --- | --- | --- |
| GPT 4.1 |  |  | 10×2×3×30 |  |
| Grok 3 |  |  | 10×3×30×2 | 10×3×2×40 |
| Claude 3 Opus | 10×3×2×30 | 10×20×3×2 | 10×3×30×2 | 10×3×2×40 |
| Llama 4 Maverick |  |  | 10×3×30×2 | 10×3×2×40 |
| o3 |  |  | 10×2×3×30 |  |
| Claude 3.7 |  |  | 10×3×30×2 | 10×3×2×40 |

| AI | `B` | `C` | `D` | `E` |
| --- | --- | --- | --- | --- |
| GPT 4.1 | ✔️ | ✔️ | X | ✔️ |
| Grok 3 | ✔️ | ✔️ | X | X |
| Claude 3 Opus | X | X | X | X |
| Llama 4 Maverick | ✔️ | ✔️ | X | X |
| o3 | ✔️ | ✔️ | X | ✔️ |
| Claude 3.7 | ✔️ | ✔️ | X | X |
| Gemini 2.5 Pro | ✔️ | ✔️ | ✔️ | ✔️ |
| DeepSeek R1 | ✔️ | ✔️ | ✔️ | ✔️ |

(DeepSeek’s chain of thought used “wait” 76 times. It got everything right the first time, but when I tried it again, it somehow got `B`, `C`, and `D` all wrong, but `E` right.)

This is insane. Using basic features should not require solving crazy logic puzzles.

You might think, “OK, I’ll just limit myself to indexing in simple ways.” Sounds good, except sometimes you _need_ advanced indexing. And even if you’re doing something simple, you still need to be careful to avoid the crazy cases.

This again makes everything non-legible. Even if you’re just reading code that uses indexing in a simple way, how do you _know_ it’s simple? If you see `A[B,C]`, that could be doing almost anything. To understand it, you need to remember the shapes of `A`, `B`, and `C` and work through all the cases. And, of course, `A`, `B`, and `C` are often produced by _other_ code, which you _also_ need to think about…

I don’t like NumPy functions
----------------------------

Why did NumPy end up with a `np.linalg.solve(A,B)` function that’s so confusing? I imagine they first made it work when `A` is a 2D array and and `b` is a 1D or 2D array, just like the mathematical notation of `A⁻¹b` or `A⁻¹B`.

So far so good. But then someone probably came along with a 3D array. If you could use loops, the solution would be “use the old function with loops”. But you can’t use loops. So there were basically three options:

1.   They could add some extra `axes` argument, so the user can specify which dimensions to operate over. Maybe you could write `solve(A,B,axes=[[1,2],1])`.
2.   They could create different functions with different names for different situations. Maybe `solve_matrix_vector` would do one thing, `solve_tensor_matrix` would do another.
3.   They could add a Convention: Some arbitrary choice for how `solve` will internally try to line up the dimensions. Then it’s the user’s problem to figure out and conform to those Conventions.

All these options are bad, because none of them can really cope with the fact that there are a combinatorial number of different cases. NumPy chose: All of them. Some functions have `axes` arguments. Some have different versions with different names. Some have Conventions. Some have Conventions _and_`axes` arguments. And some don’t provide any vectorized version at all.

But the _biggest_ flaw of NumPy is this: Say you create a function that solves some problem with arrays of some given shape. Now, how do you apply it to particular dimensions of some larger arrays? The answer is: You re-write your function from scratch in a much more complex way. The basic principle of programming is abstraction—solving simple problems and then using the solutions as building blocks for more complex problems. NumPy doesn’t let you do that.

Attention please
----------------

One last example to show you what I’m talking about. Whenever I whine about NumPy, people always want to see an example with [self-attention](https://en.wikipedia.org/wiki/Attention_(machine_learning)), the core trick behind modern language models. So fine. Here’s an implementation, which I humbly suggest is better than all 227 versions I found when I searched for “self-attention numpy”:

```
# self attention by your friend dynomight

input_dim = 4  
seq_len = 4  
d_k = 5  
d_v = input_dim  
  
X = np.random.randn(seq_len, input_dim)  
W_q = np.random.randn(input_dim, d_k)  
W_k = np.random.randn(input_dim, d_k)  
W_v = np.random.randn(input_dim, d_v)  
  
def softmax(x, axis):  
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))  
    return e_x / np.sum(e_x, axis=axis, keepdims=True)  
  
def attention(X, W_q, W_k, W_v):  
    d_k = W_k.shape[1]  
    Q = X @ W_q  
    K = X @ W_k  
    V = X @ W_v  
    scores = Q @ K.T / np.sqrt(d_k)  
    attention_weights = softmax(scores, axis=-1)  
    return attention_weights @ V
```

This is fine. Some of the `axis` stuff is a little obscure, but whatever.

But what language models really need is _multi-head_ attention, where you sort of do attention several times in parallel and then merge the results. How do we do that?

First, let’s imagine we lived in a sane world where we were allowed to use abstractions. Then you could just call the previous function in a loop:

```
# multi-head self attention by your friend dynomight
# if only we could use loops

n_head = 2
  
X = np.random.randn(seq_len, input_dim)  
W_q = np.random.randn(n_head, input_dim, d_k)  
W_k = np.random.randn(n_head, input_dim, d_k)  
W_v = np.random.randn(n_head, input_dim, d_v)  
W_o = np.random.randn(n_head, d_v, input_dim // n_head)

def multi_head_attention(X, W_q, W_k, W_v, W_o):  
    projected = []  
    for n in range(n_head):  
        output = attention(X, W_q[n,:,:], W_k[n,:,:], W_v[n,:,:])  
        my_proj = output @ W_o[n,:,:]  
        projected.append(my_proj)  
    projected = np.array(projected)  
  
    output = []  
    for i in range(seq_len):  
        my_output = np.ravel(projected[:,i,:])  
        output.append(my_output)  
    return np.array(output)
```

Looks stupid, right? Yes—thank you! Cleverness is bad.

But we don’t live in a sane world. So instead you need to do this:

```
# multi-head self attention by your friend dynomight
# all vectorized and bewildering

def multi_head_attention(X, W_q, W_k, W_v, W_o):  
    d_k = W_k.shape[-1]  
    Q = np.einsum('si,hij->hsj', X, W_q)  
    K = np.einsum('si,hik->hsk', X, W_k)  
    V = np.einsum('si,hiv->hsv', X, W_v)  
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(d_k)  
    weights = softmax(scores, axis=-1)
    output = weights @ V  
    projected = np.einsum('hsv,hvd->hsd', output, W_o)  
    return projected.transpose(1, 0, 2).reshape(seq_len, input_dim)
```

Ha! Hahahahahaha!

So what then?
-------------

To be clear, I’m only suggesting that NumPy is “the worst array language other than all the other array languages”. What’s the point of complaining if I don’t have something better to suggest?

Well, actually I do have something better to suggest. I’ve made a prototype of a “better” NumPy that I think retains all the power while eliminating all the sharp edges. I thought this would just be a short motivational introduction, but after I started writing, the evil took hold of me and here we are 3000 words later.

Also, it’s probably wise to keep some distance between one’s raving polemics and one’s constructive array language API proposals. So I’ll cover my new thing next time.
