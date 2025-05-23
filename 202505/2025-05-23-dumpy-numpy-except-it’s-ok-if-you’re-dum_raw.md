Title: DumPy: NumPy except it’s OK if you’re dum

URL Source: https://dynomight.net/dumpy/

Published Time: 2025-05-22T00:00:00+00:00

Markdown Content:
What I want from an array language is:

1.   Don’t make me think.
2.   Run fast on GPUs.
3.   Really, do not make me think.
4.   Do _not_.

I say NumPy misses on three of these. So I’d like to propose a “fix” that—I claim—eliminates 90% of unnecessary thinking, with no loss of power. It would also fix all the things based on NumPy, for example every machine learning library.

I know that sounds grandiose. Quite possibly you’re thinking that good-old dynomight has finally lost it. So I warn you now: My solution is utterly non-clever. If anything is clever here, it’s my single-minded rejection of cleverness.

To motivate the fix, let me give my story for how NumPy went wrong. It started as a nice little library for array operations and linear algebra. When everything has two or fewer dimensions, it’s great. But at some point, someone showed up with some higher-dimensional arrays. If loops were fast in Python, NumPy would have said, “Hello person with ≥3 dimensions, please call my ≤2 dimensional functions in a loop so I can stay nice and simple, xox, NumPy.”

But since loops are slow, NumPy instead took all the complexity that would _usually_ be addressed with loops and pushed it down into individual functions. I think this was a disaster, because _every time_ you see some function call like `np.func(A,B)`, you have to think:

1.   OK, what shapes do all those arrays have?
2.   And what does `np.func` do when it sees those shapes?

Different functions have different rules. Sometimes they’re bewildering. This means constantly thinking and moving dimensions around to appease the whims of particular functions. It’s the _functions_ that should be appeasing _your_ whims!

Even simple-looking things like `A*B` or `A[B,C]` do quite different things depending on the starting shapes. And those starting shapes are often themselves the output of _previous_ functions, so the complexity spirals.

Worst of all, if you write a new ≤2 dimensional function, then high-dimensional arrays are your problem. _You_ need to decide what rules to obey, and then _you_ need to re-write your function in a much more complex way to—

**Voice from the back**: Python sucks! If you used a real language, loops would be fast! This problem is stupid!

That was a strong argument, ten years ago. But now everything is GPU, and GPUs hate loops. Today, array packages are cheerful interfaces that _look_ like Python (or whatever) but are actually embedded languages that secretly compile everything into special GPU instructions that run on whole arrays in parallel. With big arrays, you need GPUs. So I think the speed of the host language doesn’t matter so much anymore.

Python’s slow loops may have paradoxically turned out to be an _advantage_, since they forced everything to be designed to work without loops even before GPUs took over.

Still, thinking is bad, and NumPy makes me think, so [I don’t like NumPy](https://dynomight.net/numpy/).

So what’s the fix?
------------------

Here’s my extremely non-clever idea: Let’s just admit that loops were better. In high dimensions, no one has yet come up with a notation that beats loops and indices. So, let’s do this:

1.   Bring back the syntax of loops and indices.
2.   But don’t actually _execute_ the loops. Just take the syntax and secretly compile it into vectorized operations.
3.   Also, let’s get rid of all the insanity that’s been added to NumPy because loops were slow.

That’s basically the whole idea. If you take those three bullet-points, you could probably re-derive everything I do below. I told you this wasn’t clever.

What does it look like?
-----------------------

Suppose that `X` and `Y` are 2D arrays, and `A` is a 4D array. And suppose you want to find a 2D array `Z` such that `Zij = (Yj)T (Aij)-1 Xi`. If you could write loops, this would be easy:

```
import numpy as np
Z = np.empty((X.shape[0], Y.shape[0]))
for i in range(X.shape[0]):
    for j in range(Y.shape[0]):
        Z[i,j] = Y[j] @ np.linalg.solve(A[i,j], X[i])
```

That’s not pretty. It’s not short or fast. But it _is_ easy!

So how do you do this efficiently in NumPy? Like this:

```
import numpy as np
AiX = np.linalg.solve(A.transpose(1,0,2,3),
                      X[None,...,None])[...,0]
Z = np.sum(AiX * Y[:,None], axis=-1).T
```

If you’re not a NumPy otaku, that may look like outsider art. Rest assured, it looks like that to me too, and I just wrote it. Why is it so confusing? At a high level, it’s because `np.linalg.solve` and `np.sum` and multiplication (`*`) have complicated rules, and weren’t designed to work together to solve this particular problem nicely. That would be impossible, because there are an infinite number of problems. So you need to mash the arrays around a lot to make those functions happy.

Without further ado, here’s how you solve this problem with **DumPy** (ostensibly **D**ynomight N**umPy**):

```
import dumpy as dp
A = dp.Array(A)
X = dp.Array(X)
Y = dp.Array(Y)
Z = dp.Slot()
Z['i','j'] = Y['j',:] @ dp.linalg.solve(A['i','j',:,:], X['i',:])
```

Yes! If you prefer, you can also use this equivalent syntax:

```
Z = dp.Slot()
with dp.Range(X.shape[0]) as i:
    with dp.Range(Y.shape[0]) as j:
        Z[i,j] = Y[j,:] @ dp.linalg.solve(A[i,j,:,:], X[i,:])
```

Those are both fully vectorized. No loops are executed behind the scenes. They’ll run on a GPU if you have one.

But how?
--------

While it looks magical, but the way this actually works is fairly simple:

1.   If you index a DumPy array with a string or a `dp.Range` object, it creates a special “mapped” array that pretends to have fewer dimensions.

2.   When a DumPy function is called (e.g. `dp.linalg.solve` or `dp.matmul` (called with `@`)), it checks if any of the arguments have mapped dimensions. If so, it automatically vectorizes the computation, matching up mapped dimensions that share label.

3.   When you assign an array with “mapped” dimensions to a `dp.Slot`, it “unmaps” them into the positions you specify.

No evil meta-programming abstract syntax tree macro bytecode interception is needed. When you run this code:

```
Z = dp.Slot()
Z['i','j'] = Y['j',:] @ dp.linalg.solve(A['i','j',:,:], X['i',:])
```

This is what happens behind the scenes.

```
a = A.map_axes([0, 1], ['i', 'j'])
x = X.map_axes([0], ['i'])
y = Y.map_axes([0], ['j'])
z = y @ dp.linalg.solve(a, x)
Z = z.unmap('i','j')
```

 (Click here for a version with a million asserts and comments.) 

```
# first map A
a = A.map_axes([0, 1], ['i', 'j'])
assert A.ndim == 4
assert a.ndim == 2             # pretends to have fewer dims
assert a.data.shape == A.shape          # secret mapped data
assert a.axes == ('i', 'j', None, None) # secret mapped axes
assert a.shape == (a.data.shape[2], a.data.shape[3])
                # shape determined by non-mapped (None) axes

# now map X
x = X.map_axes([0], ['i'])
assert X.ndim == 2
assert x.ndim == 1
assert x.data.shape == X.shape
assert x.axes == ('i', None)
assert x.shape == (x.data.shape[1], )

# now map Y
y = Y.map_axes([0], ['j'])
assert Y.ndim == 2
assert y.ndim == 1
assert y.shape == (Y.shape[1],)
assert y.axes == ('j', None)
assert y.data.shape == Y.shape
assert y.shape == (y.data.shape[1],)

# Actually do the computation. It happens that the 'j'
# dimension is stored first because its found first (in y).
# But you never need to think about that!
z = y @ dp.linalg.solve(a, x)
assert z.ndim == 0
assert z.shape == ()
assert z.axes == ('j','i')
assert z.data.shape == (Y.shape[0], X.shape[0])

# unmap the mapped axes
Z = z.unmap('i','j')
assert Z.ndim == 2
assert Z.shape == (X.shape[0], Y.shape[0])
```

Wait, but _how_?
----------------

It might seem like I’ve skipped the hard part. How does `dp.linalg.solve` know how to vectorize over any combination of input dimensions? Don’t I need to do that for every single function that DumPy includes? Isn’t that hard?

It _is_ hard, but [`jax.vmap`](https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html) did it already. This takes a function defined using ([JAX](https://github.com/jax-ml/jax)’s version of) NumPy and vectorizes it over _any_ set of input dimensions. DumPy relies on this to do all the actual vectorization. (If you prefer your `vmap` janky and broken, I heartily recommend PyTorch’s [`torch.vmap`](https://docs.pytorch.org/docs/stable/generated/torch.vmap.html).)

But hold on. If `vmap` already exists, then why do we need DumPy? Here’s why:

```
import jax
from jax import numpy as jnp
Z = jax.vmap(
        jax.vmap(
            lambda x, y, a: y @ jnp.linalg.solve(a, x),
            in_axes=[None, 0, 0]
        ),
        in_axes=[0, None, 0]
    )(X, Y, A)
```

That’s how you solve the same problem with `vmap`. (It’s also basically what DumPy does behind the scenes.)

I think `vmap` is one of the best parts of the NumPy ecosystem. I think the above code is genuinely better than the base NumPy version. But it still involves a lot of thinking! Why put `in_axes=[None, 0, 0]` in the inner `vmap` and `in_axes=[0, None, 0]` in the outer one? Why are all the axes `0` even though you need to vectorize over the second dimension of `A`? There are answers, but they require thinking. Loop and index notation is better.

A tiny bit of cleverness
------------------------

OK, I did do one thing that’s a _little_ clever. Say you want to create a [Hilbert Matrix](https://en.wikipedia.org/wiki/Hilbert_matrix) with `Hij = 1/(1+i+j)`. In base NumPy you’d have to do this:

```
X = 1 / (np.arange(5)[:,None] + np.arange(5)[None,:] + 1) # hurr?
```

In DumPy, you can just write:

```
X = dp.Slot()
with dp.Range(5) as i:
    with dp.Range(5) as j:
        X[i,j] = 1 / (i + j + 1)
```

Yes! That works! It works because a `dp.Range` acts _both_ like a string and like an array mapped along that string. So the above code is roughly equivalent to:

```
I = dp.Array([0,1,2,3,4])
J = dp.Array([0,1,2,3,4])
X['i','j'] = 1 / (1 + I['i'] + J['j'])
```

See? Still no magic.
In reality, the `dp.Range` choose random strings. (The class maintains a stack of active ranges to prevent collisions.) So in more detail, the above code becomes something like this:

```
I = dp.Array([0,1,2,3,4])
J = dp.Array([0,1,2,3,4])
i = I.map_axes([0],'range_EZaW')
j = J.map_axes([0],'range_ailw')
x = 1 / (1 + i + j) # vectorized
X = x.unmap('range_EZaW','range_ailw')
```

OK but is it actually better?
-----------------------------

To test if DumPy is actually better in practice, I took six problems of increasing complexity and implemented each of them using loops, Numpy, JAX (with `vmap`), and DumPy.

Note that in these examples, I always assume the input arrays are in the class of the system being used. If you try running them, you’ll need to add some conversions with `np.array` / `jnp.array` / `dp.Array`.

```
# loops
H = np.empty((N, N))
for i in range(N):
    for j in range(N):
        H[i, j] = 1 / (i + j + 1)

# NumPy
i = np.arange(N)
j = np.arange(N)
H = 1 / (i[:, None] + j[None, :] + 1)

# JAX
indices = jnp.arange(N)
H = jax.vmap(
        jax.vmap(
            lambda i, j: 1 / (i + j + 1),
            [0, None]),
        [None, 0]
    )(indices, indices)

# DumPy
H = dp.Slot()
with dp.Range(N) as i:
    with dp.Range(N) as j:
        H[i, j] = 1 / (i + j + 1) # Yes! This works!
```

```
# Loops
C = np.zeros((X.shape[0],X.shape[1],X.shape[1]))
for n in range(X.shape[0]):
    C[n] = np.cov(X[n])

# NumPy
mu = np.mean(X, axis=2)[:, :, None]    # hurr?
C = np.sum((X - mu)[:, None, :, :] *
           (X - mu)[:, :, None, :],
           axis=3) / (X.shape[2] - 1)  # hurrr??

# JAX
C = jax.vmap(jnp.cov)(X)

# DumPy
C_dumpy = dp.Slot()
with dp.Range(X.shape[0]) as n:
    C_dumpy[n, :, :] = dp.cov(X[n, :, :])

# DumPy (alternate)
C = dp.Slot()
C['n',:,:] = dp.cov(X['n',:,:])
```

(Pretending [`numpy.lib.stride_tricks`](https://numpy.org/devdocs/reference/generated/numpy.lib.stride_tricks.html) doesn’t exist.)

```
# Loops
B = np.empty(N - window + 1)
for i in range(N - window + 1):
    B[i] = np.mean(A[i:i + window])

# NumPy
i = np.arange(N - window + 1)[:, None]
j = np.arange(window)[None, :] 
B = np.mean(A[i+j], axis=-1)

# JAX
idx = jnp.arange(window)
B = jax.vmap(
        lambda i: jnp.mean(A[i+idx]),
    )(jnp.arange(N - window + 1))

# DumPy
windowed = dp.Slot()
B = dp.Slot()
with dp.Range(N - window + 1) as i:
    with dp.Range(window) as j:
        windowed[i, j] = A[i + j]
    B[i] = dp.mean(windowed[i, :])
    # Note: B[i] = dp.mean(A[i:i+window])
    # would not work because dp.Range can't be used in slice
```

The goal is to create `E` with

`E[i1, i2, :, i3] = A[B[i1], C[i1, i2], ::2, D[i2, i3]]`.

```
# Setup
K = 4
L = 5
M = 6
N = 7

A = np.random.randn(K, L, M, N)
B = np.random.randint(0, K, size=(9,))
C = np.random.randint(0, L, size=(9, 10))
D = np.random.randint(0, N, size=(10, 11))

# Loops
E = np.empty((9, 10, M // 2, 11))
for i1 in range(9):
    for i2 in range(10):
        for i3 in range(11):
            E[i1,i2,:,i3] = A[B[i1],C[i1, i2],::2,D[i2, i3]]

# NumPy
E = A[B[:, None, None],
      C[:, :, None],
      ::2,
      D[None, :, :]
    ].transpose((0, 1, 3, 2))

# JAX
E = jax.vmap(
        jax.vmap(
            jax.vmap(
                lambda b, c, d: A[b, c, ::2, d],
                in_axes=[None,None,0]),
            in_axes=[None,0,0]),
        in_axes=[0,0,None]
    )(B,C,D).transpose(0,1,3,2)

# DumPy
E = dp.Slot()
with dp.Range(9) as i1:
    with dp.Range(10) as i2:
        with dp.Range(11) as i3:
            E[i1,i2,:,i3] = A[B[i1],C[i1, i2],::2,D[i2, i3]]

# DumPy (alternative)
E = dp.Slot()
E['i1','i2',:,'i3'] = A[B['i1'], C['i1','i2'], ::2, D['i2','i3']]
```

The goal of this problem is, given a list of vectors and a list of [Gaussians](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) parameters, and arrays mapping each vector to a list of parameters, evaluate each corresponding vector/parameter combination. Formally, given 2D `X`, `B`, `C`, and `means` and 3D `covs`, the goal is to create `A` with

`Aij = log N( Xi | meansBij, covsCij)`.

```
# Setup
ndims = 3
ndata = 10
neval = 5
ndist = 7

X = np.random.randn(ndata, ndims)
B = np.random.randint(0, ndist, size=(ndata, neval))
C = np.random.randint(0, ndist, size=(ndata, neval))
means = np.random.randn(ndist, ndims)
scales = np.array(np.random.randn(ndist, ndims, ndims))
covs = np.array([scale @ scale.T for scale in scales])
```

```
# Loops
def log_prob(x, mean, cov):
    diff = x - mean
    y = np.linalg.solve(cov, diff)
    quad = diff @ y
    logdet = np.linalg.slogdet(2 * np.pi * cov)[1]
    return -0.5 * (quad + logdet)

A = np.empty((ndata, neval))
for i in range(ndata):
    for j in range(neval):
        A[i, j] = log_prob(X[i, :],
                           means[B[i, j], :],
                           covs[C[i, j], :, :])

# NumPy
diff = X[:, None, :] - means[B]
y = np.linalg.solve(covs[C], diff[..., None])
quad = np.sum(diff * y[..., 0], axis=-1)
logdet = np.linalg.slogdet(2 * np.pi * covs[C])[1]
A = -0.5 * (quad + logdet)

# JAX
A = jax.vmap(
        jax.vmap(
            log_prob_gauss,
            in_axes=[None, 0, 0]
        ),
    )(X, means[B], covs[C])

# DumPy
def log_prob(x, mean, cov):
    diff = x - mean
    quad = diff @ dp.linalg.solve(cov, diff)
    logdet = dp.linalg.slogdet(2 * jnp.pi * cov)[1]

A = dp.Slot()
with dp.Range(ndata) as i:
    with dp.Range(neval) as j:
        A[i, j] = log_prob(X[i,:],
                           means[B[i,j],:],
                           covs[C[i,j],:,:])

# DumPy (alternate)
A = dp.Slot()
with dp.Range(ndata) as i:
    with dp.Range(neval) as j:
        mean = means[B[i,j],:]
        cov = covs[C[i,j],:,:]
        diff = X[i,:] - mean
        quad = diff @ dp.linalg.solve(cov, diff)
        logdet = dp.linalg.slogdet(2 * jnp.pi * cov)[1]
        A[i,j] = -0.5 * (quad + logdet)
```

See also the discussion in the [previous post](https://dynomight.net/numpy/#attention-please).

```
# Setup
input_dim = 4
seq_len = 4
d_k = 5
d_v = input_dim
n_head = 2
X = np.random.randn(seq_len, input_dim)
W_q = np.random.randn(n_head, input_dim, d_k)
W_k = np.random.randn(n_head, input_dim, d_k)
W_v = np.random.randn(n_head, input_dim, d_v)
W_o = np.random.randn(n_head, d_v, input_dim // n_head)

# Loops
def softmax_numpy(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def attention(X, W_q, W_k, W_v):
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    scores = Q @ K.T / np.sqrt(d_k)
    attention_weights = softmax_numpy(scores, axis=-1)
    output = attention_weights @ V
    return output

def multi_head_attention_loops(X, W_q, W_k, W_v, W_o):
    projected = []
    for n in range(n_head):
        my_output = attention(X,
                                W_q[n, :, :],
                                W_k[n, :, :],
                                W_v[n, :, :])
        my_proj = my_output @ W_o[n, :, :]
        projected.append(my_proj)
    projected = np.array(projected)

    final = []
    for i in range(seq_len):
        my_final = np.ravel(projected[:, i, :])
        final.append(my_final)
    return np.array(final)

# NumPy
def softmax_numpy(x, axis=-1): # repeat
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention_numpy(X, W_q, W_k, W_v, W_o):
    Q = np.einsum('si,hij->hsj', X, W_q)
    K = np.einsum('si,hik->hsk', X, W_k)
    V = np.einsum('si,hiv->hsv', X, W_v)
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(d_k)
    weights = softmax_numpy(scores, axis=-1)
    output = weights @ V
    projected = np.einsum('hsv,hvd->hsd', output, W_o)
    return projected.transpose(1, 0, 2).reshape(
        seq_len, input_dim)

# JAX
def softmax_jax(x, axis=-1):
    e_x = jnp.exp(x - jnp.max(x, axis=axis, keepdims=True))
    return e_x / jnp.sum(e_x, axis=axis, keepdims=True)

def attention_jax(X, W_q, W_k, W_v):
    d_k = W_k.shape[-1]
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    scores = Q @ K.T / jnp.sqrt(d_k)
    attention_weights = softmax_jax(scores, axis=-1)
    output = attention_weights @ V
    return output

def multi_head_attention_jax(X, W_q, W_k, W_v, W_o):
    def myfun(X, w_q, w_k, w_v, w_o):
        return attention_jax(X, w_q, w_k, w_v) @ w_o

    projected = jax.vmap(myfun,
                            in_axes=[None, 0, 0, 0, 0]
                )(X, W_q, W_k, W_v, W_o)

    return jax.vmap(jnp.ravel, in_axes=1)(projected)

# DumPy
def softmax_dumpy(x):
    assert x.ndim == 1 # no need to think about dimensions!
    e_x = dp.exp(x - dp.max(x))
    return e_x / dp.sum(e_x)

@dp.wrap # needed to make functions with Slots auto-vectorizing
def attention_dumpy(X, W_q, W_k, W_v):
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    scores = Q @ K.T / np.sqrt(d_k)
    attention_weights = dp.Slot()
    with dp.Range(seq_len) as i:
        attention_weights[i, :] = softmax_dumpy(scores[i, :])
    output = attention_weights @ V
    return output

def multi_head_attention_dumpy(X, W_q, W_k, W_v, W_o):
    output = dp.Slot()
    projected = dp.Slot()
    final = dp.Slot()
    with dp.Range(n_head) as n:
        output[n, :, :] = attention_dumpy(X,
                                          W_q[n, :, :],
                                          W_k[n, :, :],
                                          W_v[n, :, :])
        projected[n, :, :] = output[n, :, :] @ W_o[n, :, :]
    with dp.Range(seq_len) as i:
        final[i, :] = dp.ravel(projected[:, i, :])
    return final

# DumPy (alternate)
def multi_head_attention(X, W_q, W_k, W_v, W_o):
    attn_weights = dp.Slot()
    projected = dp.Slot()
    final = dp.Slot()
    with dp.Range(n_head) as n:
        Q = X @ W_q[n, :, :]
        K = X @ W_k[n, :, :]
        V = X @ W_v[n, :, :]
        scores = Q @ K.T / np.sqrt(d_k)
        with dp.Range(seq_len) as i:
            attn_weights[n, i, :] = softmax_dumpy(scores[i, :])
        projected[n, :, :] = attn_weights[n, :, :] @ V @ W_o[n, :, :]
    with dp.Range(seq_len) as i:
        final[i, :] = dp.ravel(projected[:, i, :])
    return final
```

I gave each implementation a subjective “goodness” score on a 1-10 scale. I always gave the best implementation for each problem 10 points, and then took off points from the others based on how much thinking they required.

| Problem | Loops | Numpy | JAX (vmap) | DumPy |
| --- | --- | --- | --- | --- |
| Hilbert matrices | 10 | 7 | 7 | 10 |
| Covariance | 9 | 4 | 10 | 9 |
| Moving Ave. | 10 | 6 | 6 | 8 |
| Indexing | 10 | 5 | 4 | 10 |
| Gaussians | 10 | 3 | 6 | 10 |
| Attention | 10 | 1 | 8 | 10 |
| **Mean** | **9.8** | **4.3** | **6.8** | **9.5** |

According to this dubious methodology and these made-up numbers, DumPy is 96.93877% as good as loops! Knowledge is power! But seriously, while subjective, I don’t think my scores should be _too_ controversial. The most debatable one is probably JAX’s attention score.

What to remove?
---------------

The only thing DumPy adds to NumPy is some nice notation for indices. That’s it.

What I think makes DumPy good is it also _removes_ a lot of stuff. Roughly speaking, I’ve tried to remove anything that is confusing and exists because NumPy doesn’t have loops. I’m not sure that I’ve drawn the line in exactly the right place, but I do feel confident that I’m on the right track.

### 1. Goodbye broadcasting

In NumPy, `A * B` works if `A` and `B` are both scalar. Or if `A` is `5×1×6` and `B` is `5×1×6×1`. But not if `A` is `1×5×6` and `B` is `1×5×6×1`. Huh?

In truth, the [broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html) aren’t _that_ complicated for scalar operations like multiplication. But still, I don’t like it, because _every time_ you see `A * B`, you have to worry about what shapes those have and what the computation might be doing.

So, I removed it. In DumPy you can only do `A * B` if one of `A` or `B` is scalar or `A` and `B` have exactly the same shape. That’s it, anything else raises an error. Instead, use indices, so it’s clear what you’re doing. Instead of this:

```
C = A[...,None] * B[None]
```

write this:

```
C['i','j','k'] = A['i','j'] * B['j','k']
```

### 2. Goodbye fancy indexing

Indexing in NumPy is [absurdly complicated](https://dynomight.net/numpy/#i-dont-like-numpy-indexing). When you write `A[B,C,D]` that could do _many_ different things depending on what all the shapes are. I considered going cold-turkey and only allowing scalar indices in DumPy. That wouldn’t have been _so_ bad, since you can still do advanced stuff using loops. But it’s quite annoying to not be able to write `A[B]` when `A` and `B` are just simple 1D arrays.

So I’ve tentatively decided to be more pragmatic. In DumPy, you can index with integers, or slices, or (possibly mapped) `Array`s. **But only one `Array` index can be non-scalar**. I settled on this because it’s the most general syntax that doesn’t require thinking.

Let me show you what I mean. If you see this:

```
A[1, 1:6, C, 2:10] # legal in both numpy and dumpy
```

It’s “obvious” what the output shape will be. (First the shape of `1:6`, then the shape of `C`, then the shape of `2:10`). Simple enough. But as soon as you have _two_ multidimensional array inputs like this:

```
A[B, 1:6, C, 2:10] # legal in numpy, verboten in dumpy
```

Suddenly all hell breaks loose. You need to think about broadcasting between `A` and `B`, orthogonal vs. pointwise indices, slices behaving differently than arrays, and quirks for where the output dimensions go. So DumPy forbids this. Instead, you need to write one of these:

```
D['i',:,:]     = A[B['i'],     1:6, C['i'],     2:10] # (1)
D[:,:,'i']     = A[B['i'],     1:6, C['i'],     2:10] # (2)
D['i','j',:,:] = A[B['i'],     1:6, C['j'],     2:10] # (3)
D['i','j',:,:] = A[B['i','j'], 1:6, C['i'],     2:10] # (4)
D['i','j',:,:] = A[B['i','j'], 1:6, C['i','j'], 2:10] # (5)
```

Those all do exactly what they look like they do.

Oh, and one more thing! In DumPy, you **must index all dimensions**. In NumPy, if `A` has three dimensions, then `A[2]` is equivalent to `A[2,:,:]`. This is sometimes nice, but it means that _every time_ you see `A[2]`, you have to worry about how many dimensions `A` has.

In DumPy, every index statement checks that all indices have been included. The same is true when assigning to a `dp.Slot`. So when you see option (4) above, you _know_ that:

*   `A` has 4 dimensions
*   `B` has 2 dimensions
*   `C` has 1 dimension
*   `D` has 4 dimensions

Always, always, _always_. Thinking bad.

### 3. Goodbye complicated functions

Again, many NumPy functions have complex conventions for vectorization. [`np.linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html) sort of says, “If the inputs have ≤2 dimensions, do the obvious thing. Otherwise, do some extremely confusing broadcasting thing.” DumPy removes all the confusing broadcasting things. When you see `dp.linalg.solve(A,B)`, you know that `A` and `B` have no more than two dimensions.

Similarly, in NumPy, `A @ B` is equivalent to [`np.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)`(A,B)`. When both inputs have ≤2 or fewer dimensions, this does the “obvious thing”. (Either and inner-product or some kind of matrix-vector multiplication.) Otherwise, it broadcasts or vectorizes or something? I can never remember. In DumPy you don’t have that problem, because it restricts `A @ B` to arrays with one or two dimensions only.

### Why remove?

It might seem annoying to remove features, but I’m telling you: _Just try it_. If you program this way, a wonderful feeling of calmness comes over you, as class after class of possible errors disappear.

Put another way, why remove all the fancy stuff, instead of leaving it optional? Because optional implies thinking! I want to program in a simple way. I don’t want to worry that I’m accidentally triggering some confusing functionality, because that would be a mistake. I want the computer to help me catch mistakes, not silently do something weird that I didn’t intend.

In principle, it would be OK if there was a `evil_batch_solve` method that preserves all the confusing batching stuff. If you _really_ want that, you can make it yourself with `dp.MappedFunction(jnp.linalg.solve)`.

Discussion
----------

Think about math: In two or fewer dimensions, coordinate-free linear algebra notation is wonderful. But for higher dimensional [tensors](https://en.wikipedia.org/wiki/Tensor), there are just too many cases, so most physicists just use coordinates.

So this solution seems pretty obvious to me. Honestly, I’m a little confused why it isn’t already standard. Am I missing something?

### What about APL?

When I complain about NumPy, many people often suggest looking into [APL](https://en.wikipedia.org/wiki/APL_(programming_language))-type languages, like A, J, K, or Q. (All single-letter languages are APL-descended except C, D, F, R, T, X, and several others. Convenient, right?) The obvious disadvantages of these are that:

1.   They’re unfamiliar.
2.   The code looks like gibberish.
3.   They don’t usually provide autodiff or GPU execution.

None of those bother me. If the languages are better, we should learn to use them and make them do autodiff on GPUs. But I’m not convinced they _are_ better. When you actually learn these languages, what you figure out is that the symbol gibberish basically amounts to doing the same kind of dimension mashing that we saw earlier in NumPy:

```
AiX = np.linalg.solve(A.transpose(1,0,2,3),
                      X[None,...,None])[...,0]
Z = np.sum(AiX * Y[:,None], axis=-1).T
```

The reason is that, just like NumPy and `vmap`, these languages choose align dimensions by _positions_, rather than by names. If I _have_ to mash dimensions, I want to use the best tool. But I’d prefer not to mash dimensions at all.

### What about named dimensions?

People also often suggest “NumPy with named dimensions” as in [xarray](https://docs.xarray.dev/en/stable/index.html). (PyTorch also has a [half-hearted implementation](https://docs.pytorch.org/docs/stable/named_tensor.html).) Of course, DumPy also uses named dimensions, but there’s a critical difference. In xarray, they’re part of the arrays themselves, while in DumPy, they live outside the arrays.

In some cases, permanent named dimensions are very nice. But for linear algebra, they’re confusing. For example, suppose `A` is 2-D with named dimensions `"cat"` and `"dog"`. Now, what dimensions should `ATA` have? (`"dog"` twice?) Or say you take a singular value decomposition like `U, S, Vh = svd(A)`. What name should the inner dimensions have? Does the user have to specify it?

I haven’t seen a nice solution. xarray doesn’t focus on linear algebra, so it’s not much of an issue there. A theoretical “DumPy with permanent names” _might_ be very nice, but I’m not how it should work. This is worth thinking about more.

### What about Julia or [other language]

I like [Julia](https://julialang.org/)! Loops are fast in Julia! But again, I don’t think fast loops matter that much, because I want to move all the loops to the GPU. So even if I was using Julia, I think I’d want to use a DumPy-type solution.

I think Julia might well be a better host language than Python, but it wouldn’t be because of fast loops, but because it offers much more powerful meta-programming capabilities. I built DumPy on top of JAX just because JAX is very mature and good at calling the GPU, but I’d love to see the same idea used in Julia (“Dulia”?) or other languages.

Prototype
---------

OK, I promised a link to my prototype, so here it is: [`dumpy.py`](https://dynomight.net/img/dumpy/dumpy.py)

It’s just a single file with around 700 lines. I’m leaving it as a single file because I want to stress that **this is just something I hacked together in the service of this rant**. I wanted to show that I’m not totally out of my mind, and that doing all this is actually pretty easy.

I stress that I don’t really intend to update or improve this. (Unless someone gives me a lot of money?) So please do not attempt to use it for “real work”, and do not make fun of my code.

_P.S_. DumPy works out of the box with both [`jax.jit`](https://docs.jax.dev/en/latest/_autosummary/jax.jit.html) and [`jax.grad`](https://docs.jax.dev/en/latest/_autosummary/jax.grad.html). For gradients, you need to either cast the output to a JAX scalar or use the `dp.grad` wrapper.
