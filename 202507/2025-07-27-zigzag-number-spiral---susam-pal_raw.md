Title: Zigzag Number Spiral - Susam Pal

URL Source: https://susam.net/zigzag-number-spiral.html

Markdown Content:
By **Susam Pal** on 27 Jul 2025

Consider the following infinite grid of numbers, where the numbers are arranged in a spiral-like manner, but the spiral reverses direction each time it reaches the edge of the grid: 1→2 9→10 25⋯↓↑↓↑4←3 8 11 24⋯↓↑↓↑5→6→7 12 23⋯↓↑16←15←14←13 22⋯↓↑17→18→19→20→21⋯⋮⋮⋮⋮⋮⋱\begin{array}{rcrcrcrcrl} 1 & \rt & 2 & \sp & 9 & \rt & 10 & \sp & 25 & \cd \\ \sp & \sp & \dn & \sp & \up & \sp & \dn & \sp & \up & \sp \\ 4 & \lf & 3 & \sp & 8 & \sp & 11 & \sp & 24 & \cd \\ \dn & \sp & \sp & \sp & \up & \sp & \dn & \sp & \up & \sp \\ 5 & \rt & 6 & \rt & 7 & \sp & 12 & \sp & 23 & \cd \\ \sp & \sp & \sp & \sp & \sp & \sp & \dn & \sp & \up & \sp \\ 16 & \lf & 15 & \lf & 14 & \lf & 13 & \sp & 22 & \cd \\ \dn & \sp & \sp & \sp & \sp & \sp & \sp & \sp & \up & \sp \\ 17 & \rt & 18 & \rt & 19 & \rt & 20 & \rt & 21 & \cd \\ \vd & \sp & \vd & \sp & \vd & \sp & \vd & \sp & \vd & \dd \end{array} Can we find a closed-form expression that tells us the number at the m m th row and n n th column?

Contents[](https://susam.net/zigzag-number-spiral.html#contents)
----------------------------------------------------------------

*   [Introduction](https://susam.net/zigzag-number-spiral.html#introduction)
*   [Patterns on the Edges](https://susam.net/zigzag-number-spiral.html#patterns-on-the-edges)
    *   [Computing Edge Numbers](https://susam.net/zigzag-number-spiral.html#computing-edge-numbers)
    *   [Computing All Grid Numbers](https://susam.net/zigzag-number-spiral.html#computing-all-grid-numbers-1)
    *   [Closed Form Expression](https://susam.net/zigzag-number-spiral.html#closed-form-expression-1)

*   [Patterns on the Diagonal](https://susam.net/zigzag-number-spiral.html#patterns-on-the-diagonal)
    *   [Computing Diagonal Numbers](https://susam.net/zigzag-number-spiral.html#computing-diagonal-numbers)
    *   [Computing All Grid Numbers](https://susam.net/zigzag-number-spiral.html#computing-all-grid-numbers-2)
    *   [Closed Form Expression](https://susam.net/zigzag-number-spiral.html#closed-form-expression-2)

*   [References](https://susam.net/zigzag-number-spiral.html#references)

Introduction[](https://susam.net/zigzag-number-spiral.html#introduction)
------------------------------------------------------------------------

Before we explore this problem further, let us rewrite the zigzag number spiral grid in a cleaner form, omitting the arrows: 1 2 9 10 25⋯4 3 8 11 24⋯5 6 7 12 23⋯16 15 14 13 22⋯17 18 19 20 21⋯⋮⋮⋮⋮⋮⋱\begin{array}{rrrrrl} 1 & 2 & 9 & 10 & 25 & \cd \\ 4 & 3 & 8 & 11 & 24 & \cd \\ 5 & 6 & 7 & 12 & 23 & \cd \\ 16 & 15 & 14 & 13 & 22 & \cd \\ 17 & 18 & 19 & 20 & 21 & \cd \\ \vd & \vd & \vd & \vd & \vd & \dd \end{array} Let f(m,n) f(m, n)  denote the number at the m m th row and n n th column. For example, f(1,1)=1 f(1, 1) = 1  and f(2,5)=24. f(2, 5) = 24.  We want to find a closed-form expression for f(m,n). f(m, n).

Let us first clarify what we mean by a _closed-form expression_. There is no universal definition for a closed-form expression, but typically a closed-form expression is a mathematical expression involving variables and constants, constructed using a finite number of operations such as addition, subtraction, multiplication, division, integer exponents, roots with integer index, and standard functions such as exponentials, logarithms and trigonometric functions.

In this article, however, we need only addition, subtraction, division, squares and square roots. This may be a bit of a spoiler, but I must mention that the max⁡ \max  function appears in the closed-form expressions we are about to see. If you are concerned about whether functions like max⁡ \max  and min⁡ \min  are permitted in such expressions, note that max⁡(m,n)=m+n+(m−n)2 2,min⁡(m,n)=m+n−(m−n)2 2.\begin{align*} \max(m, n) & = \frac{m + n + \sqrt{(m - n)^2}}{2}, \\ \min(m, n) & = \frac{m + n - \sqrt{(m - n)^2}}{2}. \end{align*} So max⁡ \max  and min⁡ \min  are simply shorthand for expressions involving addition, subtraction, division, squares and square roots. In the discussion that follows, we will use only the max⁡ \max  function.

Patterns on the Edges[](https://susam.net/zigzag-number-spiral.html#patterns-on-the-edges)
------------------------------------------------------------------------------------------

Let us begin by analysing the edge numbers. Number the rows as 1,2,3… 1, 2, 3 \dots  and the columns likewise. Observe where the spiral touches the left edge and changes direction. This happens only on even-numbered rows. Similarly, each time the spiral touches the top edge and changes direction, it does so on odd-numbered columns. In the following subsections, we take a closer look at this behaviour of the spiral.

Before we proceed, I should mention that this section takes a rather long path to arrive at the closed-form solution. Personally, I enjoy such extended tours. If you prefer a more direct approach, feel free to skip ahead to [Patterns on the Diagonal](https://susam.net/zigzag-number-spiral.html#patterns-on-the-diagonal) for a shorter discussion that reaches the same result.

### Computing Edge Numbers[](https://susam.net/zigzag-number-spiral.html#computing-edge-numbers)

Each time the spiral reaches the left edge of the grid, it does so at some m m th row where m m  is even. The m×m m \times m  subgrid formed by the first m m  rows and the first m m  columns contains m 2 m^2  consecutive numbers. Since the numbers strictly increase as the spiral grows, the largest of these m 2 m^2  numbers must appear at the position where the spiral touches the left edge. This is illustrated in the figure below.

1 2 9 10 25⋯4 3 8 11 24⋯5 6 7 12 23⋯▶16 15 14 13 22⋯17 18 19 20 21⋯⋮⋮⋮⋮⋮⋱\begin{array}{rrrr:rl} 1 & 2 & 9 & 10 & 25 & \cd \\ 4 & 3 & 8 & 11 & 24 & \cd \\ 5 & 6 & 7 & 12 & 23 & \cd \\ \hl 16 & 15 & 14 & 13 & 22 & \cd \\ \hdashline 17 & 18 & 19 & 20 & 21 & \cd \\ \vd & \vd & \vd & \vd & \vd & \dd \end{array}

 The spiral touches the left edge on the 4 4 th row where the number is 4 2 4^2 

Whenever the spiral touches the left edge at the m m th row (where m m  is even), the number in the first column of that row is m 2. m^2.  Hence, we conclude that f(m,1)=m 2 f(m, 1) = m^2  when m m  is even. Immediately after touching the left edge, the spiral turns downwards into the first column of the next row. Thus, in the next row, i.e., in the (m+1) (m + 1) th row, we have f(m+1,1)=m 2+1, f(m + 1, 1) = m^2 + 1,  where m+1 m + 1  is odd. This can be restated as f(m,1)=(m−1)2+1 f(m, 1) = (m - 1)^2 + 1  when m m  is odd. Since f(1,1)=1, f(1, 1) = 1,  we can summarise the two formulas we have found here as: f(m,1)={m 2 if m≡0(m o d 2),(m−1)2+1 if m≡1(m o d 2). f(m, 1) = \begin{cases} m^2 & \text{if } m \equiv 0 \pmod{2}, \\ (m - 1)^2 + 1 & \text{if } m \equiv 1 \pmod{2}. \end{cases}

We can perform a similar analysis for the numbers at the top edge and note that whenever the spiral touches the top edge at the n n th column (where n n  is odd), the number in the first row of that column is n 2. n^2.  This is illustrated below.

1 2▶9 10 25⋯4 3 8 11 24⋯5 6 7 12 23⋯16 15 14 13 22⋯17 18 19 20 21⋯⋮⋮⋮⋮⋮⋱\begin{array}{rrr:rrl} 1 & 2 & \hl 9 & 10 & 25 & \cd \\ 4 & 3 & 8 & 11 & 24 & \cd \\ 5 & 6 & 7 & 12 & 23 & \cd \\ \hdashline 16 & 15 & 14 & 13 & 22 & \cd \\ 17 & 18 & 19 & 20 & 21 & \cd \\ \vd & \vd & \vd & \vd & \vd & \dd \end{array}

 The spiral touches the top edge on the 3 3 rd column where the number is 3 2 3^2 

Immediately after touching the top edge, the spiral turns right into the next column. These observations give us the following formula for the numbers at the top edge: f(1,n)={n 2 if n≡1(m o d 2),(n−1)2+1 if n≡0(m o d 2). f(1, n) = \begin{cases} n^2 & \text{if } n \equiv 1 \pmod{2}, \\ (n - 1)^2 + 1 & \text{if } n \equiv 0 \pmod{2}. \end{cases}  Next we will find a formula for any arbitrary number anywhere in the grid.

### Computing All Grid Numbers[](https://susam.net/zigzag-number-spiral.html#computing-all-grid-numbers-1)

Since the spiral touches the left edge on even-numbered rows, then turns downwards into the next (odd-numbered) row, and then starts moving right until the diagonal (where it changes direction again), the following two rules hold:

*    On every odd-numbered row, as we go from left to right, the numbers increase until we reach the diagonal. 
*    On every even-numbered row, as we go from left to right, the numbers decrease until we reach the diagonal. 

Note that all the numbers we considered in the above two points lie on or below the diagonal (or equivalently, on or to the left of the diagonal). Therefore, on an odd-numbered row, we can find the numbers on or below the diagonal using the formula f(m,n)=f(m,1)+(n−1), f(m, n) = f(m, 1) + (n - 1),  where m m  is odd. Similarly, on even-numbered rows, we can find the numbers on or below the diagonal using the formula f(m,n)=f(m,1)−(n−1), f(m, n) = f(m, 1) - (n - 1),  where m m  is even.

By a similar analysis, the following rules hold when we consider the numbers in a column:

*    On every even-numbered column, as we go from top to bottom, the numbers increase until we reach the diagonal. 
*    On every odd-numbered column, as we go from top to bottom, the numbers decrease until we reach the diagonal. 

Now the numbers on or above the diagonal can be found using the formula f(m,n)=f(1,n)−(m−1) f(m, n) = f(1, n) - (m - 1)  when n n  is odd, and f(m,n)=f(1,n)+(m−1), f(m, n) = f(1, n) + (m - 1),  when n n  is even.

Can we determine from the values of m m  and n n  if the number f(m,n) f(m, n)  is above the diagonal or below it? Yes, if m≤n, m \le n,  then f(m,n) f(m, n)  lies on or above the diagonal. However, if m≥n, m \ge n,  then f(m,n) f(m, n)  lies on or below the diagonal.

We now have everything we need to write a general formula for finding the numbers anywhere in the grid. Using the four formulas and the two inequalities obtained in this section, we get f(m,n)={f(1,n)+(m−1)if m≤n and n≡0(m o d 2),f(1,n)−(m−1)if m≤n and n≡1(m o d 2),f(m,1)−(n−1)if m≥n and m≡0(m o d 2),f(m,1)+(n−1)if m≥n and m≡1(m o d 2). f(m, n) = \begin{cases} f(1, n) + (m - 1) & \text{if } m \le n \text{ and } n \equiv 0 \pmod{2}, \\ f(1, n) - (m - 1) & \text{if } m \le n \text{ and } n \equiv 1 \pmod{2}, \\ f(m, 1) - (n - 1) & \text{if } m \ge n \text{ and } m \equiv 0 \pmod{2}, \\ f(m, 1) + (n - 1) & \text{if } m \ge n \text{ and } m \equiv 1 \pmod{2}. \\ \end{cases}  Using the equations for f(1,n) f(1, n)  and f(m,1) f(m, 1)  from the previous section, the above formulas can be rewritten as f(m,n)={(n−1)2+1+(m−1)if m≤n and n≡0(m o d 2),n 2−(m−1)if m≤n and n≡1(m o d 2),m 2−(n−1)if m≥n and m≡0(m o d 2),(m−1)2+1+(n−1)if m≥n and m≡1(m o d 2). f(m, n) = \begin{cases} (n - 1)^2 + 1 + (m - 1) & \text{if } m \le n \text{ and } n \equiv 0 \pmod{2}, \\ n^2 - (m - 1) & \text{if } m \le n \text{ and } n \equiv 1 \pmod{2}, \\ m^2 - (n - 1) & \text{if } m \ge n \text{ and } m \equiv 0 \pmod{2}, \\ (m - 1)^2 + 1 + (n - 1) & \text{if } m \ge n \text{ and } m \equiv 1 \pmod{2}. \\ \end{cases}  Simplifying the expressions on the right-hand side, we get f(m,n)={(n−1)2+m if m≤n and n≡0(m o d 2),n 2−m+1 if m≤n and n≡1(m o d 2),m 2−n+1 if m≥n and m≡0(m o d 2),(m−1)2+n if m≥n and m≡1(m o d 2). f(m, n) = \begin{cases} (n - 1)^2 + m & \text{if } m \le n \text{ and } n \equiv 0 \pmod{2}, \\ n^2 - m + 1 & \text{if } m \le n \text{ and } n \equiv 1 \pmod{2}, \\ m^2 - n + 1 & \text{if } m \ge n \text{ and } m \equiv 0 \pmod{2}, \\ (m - 1)^2 + n & \text{if } m \ge n \text{ and } m \equiv 1 \pmod{2}. \\ \end{cases}  This is pretty good. We now have a piecewise formula that works for any position in the grid. Let us now explore whether we can express it as a single closed-form expression.

### Closed Form Expression[](https://susam.net/zigzag-number-spiral.html#closed-form-expression-1)

First, we will rewrite the piecewise formula from the previous section in the following form: f(m,n)={(n 2−n+1)+(m−n)if m≤n and n≡0(m o d 2),(n 2−n+1)−(m−n)if m≤n and n≡1(m o d 2),(m 2−m+1)+(m−n)if m≥n and m≡0(m o d 2),(m 2−m+1)−(m−n)if m≥n and m≡1(m o d 2). f(m, n) = \begin{cases} (n^2 - n + 1) + (m - n) & \text{if } m \le n \text{ and } n \equiv 0 \pmod{2}, \\ (n^2 - n + 1) - (m - n) & \text{if } m \le n \text{ and } n \equiv 1 \pmod{2}, \\ (m^2 - m + 1) + (m - n) & \text{if } m \ge n \text{ and } m \equiv 0 \pmod{2}, \\ (m^2 - m + 1) - (m - n) & \text{if } m \ge n \text{ and } m \equiv 1 \pmod{2}. \\ \end{cases}  This is the same formula, rewritten to reveal common patterns between the four expressions on the right-hand side. In each expression, one variable plays the dominant role, occurring several times, while the other appears only once. For example, in the first two expressions n n  plays the dominant role whereas m m  occurs only once. If we look closely, we realise that it is the variable that is greater than or equal to the other that plays the dominant role. Therefore the first and third expressions may be written as ((max⁡(m,n))2−max⁡(m,n)+1)+(m−n). \left( (\max(m, n))^2 - \max(m, n) + 1 \right) + (m - n).  Similarly, the second and fourth expressions may be written as ((max⁡(m,n))2−max⁡(m,n)+1)−(m−n). \left( (\max(m, n))^2 - \max(m, n) + 1 \right) - (m - n).  We have made some progress towards a closed-form expression. We have collapsed the four expressions in the piecewise formula to just two. The only difference between them lies in the sign of the second term: it is positive when the dominant variable is even, and negative when it is odd. This observation allows us to unify both cases into a single expression: f(m,n)=(max⁡(m,n))2−max⁡(m,n)+1+(−1)max⁡(m,n)(m−n). f(m, n) = (\max(m, n))^2 - \max(m, n) + 1 + (-1)^{\max(m, n)} (m - n).  Now we have a closed-form expression for f(m,n) f(m, n)  that gives the number at any position in the grid.

Patterns on the Diagonal[](https://susam.net/zigzag-number-spiral.html#patterns-on-the-diagonal)
------------------------------------------------------------------------------------------------

As mentioned earlier, there is a shorter route to the same closed-form expression. This alternative approach is based on analysing the numbers along the diagonal of the grid. We still need to examine the edge numbers, but not all of them as we did in the previous section. Some of the reasoning about edge values will be repeated here to ensure this section is self-contained.

### Computing Diagonal Numbers[](https://susam.net/zigzag-number-spiral.html#computing-diagonal-numbers)

A number on the diagonal has the same row number and column number. In other words, a diagonal number has the value f(n,n) f(n, n)  for some positive integer n. n.  Consider the case when n n  is even. In this case, the diagonal number is on a segment of the spiral that is moving to the left. The n×n n \times n  subgrid formed by the first n n  rows and the first n n  columns contains exactly n 2 n^2  consecutive numbers. Since the diagonal number is on the last row of this subgrid and the numbers in this row increase as we move from right to left, the largest number in the subgrid must be on the left edge of this row. Therefore the number at the left edge is f(n,1)=n 2, f(n, 1) = n^2,  where n n  is even. This is illustrated below.

1 2 9 10 25⋯4 3 8 11 24⋯5 6 7 12 23⋯▶16 15 14▶13 22⋯17 18 19 20 21⋯⋮⋮⋮⋮⋮⋱\begin{array}{rrrr:rl} 1 & 2 & 9 & 10 & 25 & \cd \\ 4 & 3 & 8 & 11 & 24 & \cd \\ 5 & 6 & 7 & 12 & 23 & \cd \\ \hl 16 & 15 & 14 & \hl 13 & 22 & \cd \\ \hdashline 17 & 18 & 19 & 20 & 21 & \cd \\ \vd & \vd & \vd & \vd & \vd & \dd \end{array}

 The spiral touches the left edge on the 4 4 th row where the number is 4 2 4^2 

From the diagonal to the edge of the subgrid, there are n n  consecutive numbers. In a sequence of n n  consecutive numbers, the difference between the maximum number and the minimum number is n−1. n - 1.  Therefore, n 2−f(n,n)=n−1. n^2 - f(n, n) = n - 1.  This gives us f(n,n)=n 2−n+1 if n≡0(m o d 2). f(n, n) = n^2 - n + 1 \quad \text{if } n \equiv 0 \pmod{2}.

Now consider the case when n n  is odd.

1 2▶9 10 25⋯4 3 8 11 24⋯5 6▶7 12 23⋯16 15 14 13 22⋯17 18 19 20 21⋯⋮⋮⋮⋮⋮⋱\begin{array}{rrr:rrl} 1 & 2 & \hl 9 & 10 & 25 & \cd \\ 4 & 3 & 8 & 11 & 24 & \cd \\ 5 & 6 & \hl 7 & 12 & 23 & \cd \\ \hdashline 16 & 15 & 14 & 13 & 22 & \cd \\ 17 & 18 & 19 & 20 & 21 & \cd \\ \vd & \vd & \vd & \vd & \vd & \dd \end{array}

 The spiral touches the top edge on the 3 3 rd column where the number is 3 2 3^2 

By a similar reasoning, for odd n, n,  the n n th column has numbers that increase as we move up from the diagonal number towards the top edge. Therefore f(1,n)=n 2, f(1, n) = n^2,  and since n 2−f(n,n)=n−1, n^2 - f(n, n) = n - 1,  we again obtain f(n,n)=n 2−n+1 if n≡1(m o d 2). f(n, n) = n^2 - n + 1 \quad \text{if } n \equiv 1 \pmod{2}.  Since f(n,n) f(n, n)  takes the same form for both odd and even n, n ,  we can write f(n,n)=n 2−n+1 f(n, n) = n^2 - n + 1  for all positive integers n. n.

### Computing All Grid Numbers[](https://susam.net/zigzag-number-spiral.html#computing-all-grid-numbers-2)

If m≤n, m \le n,  then the number f(m,n) f(m, n)  lies on or above the diagonal number f(n,n). f(n, n).  If n n  is even, then the numbers decrease as we go from the diagonal up to the top edge. Therefore f(m,n)≤f(n,n) f(m, n) \le f(n, n)  and f(m,n)=f(n,n)−(n−m). f(m, n) = f(n, n) - (n - m).  If n n  is odd, then the numbers increase as we go from the diagonal up to the top edge, and therefore f(m,n)≥f(n,n) f(m, n) \ge f(n, n)  and f(m,n)=f(n,n)+(n−m). f(m, n) = f(n, n) + (n - m).

If m≥n, m \ge n,  then the number f(m,n) f(m, n)  lies on or below the diagonal number f(m,m). f(m, m).  By a similar analysis, we find that f(m,n)=f(m,m)+(m−n) f(m, n) = f(m, m) + (m - n)  if n n  is even, and f(m,n)=f(m,m)−(m−n) f(m, n) = f(m, m) - (m - n)  if n n  is odd. We summarise these results as follows: f(m,n)={f(n,n)−(n−m)if m≤n and n≡0(m o d 2),f(n,n)+(n−m)if m≤n and n≡1(m o d 2),f(m,m)+(m−n)if m≥n and m≡0(m o d 2),f(m,m)−(m−n)if m≥n and m≡1(m o d 2). f(m, n) = \begin{cases} f(n, n) - (n - m) & \text{if } m \le n \text{ and } n \equiv 0 \pmod{2}, \\ f(n, n) + (n - m) & \text{if } m \le n \text{ and } n \equiv 1 \pmod{2}, \\ f(m, m) + (m - n) & \text{if } m \ge n \text{ and } m \equiv 0 \pmod{2}, \\ f(m, m) - (m - n) & \text{if } m \ge n \text{ and } m \equiv 1 \pmod{2}. \\ \end{cases}  Note that the above formula can be rewritten as f(m,n)={f(n,n)+(m−n)if m≤n and n≡0(m o d 2),f(n,n)−(m−n)if m≤n and n≡1(m o d 2),f(m,m)+(m−n)if m≥n and m≡0(m o d 2),f(m,m)−(m−n)if m≥n and m≡1(m o d 2). f(m, n) = \begin{cases} f(n, n) + (m - n) & \text{if } m \le n \text{ and } n \equiv 0 \pmod{2}, \\ f(n, n) - (m - n) & \text{if } m \le n \text{ and } n \equiv 1 \pmod{2}, \\ f(m, m) + (m - n) & \text{if } m \ge n \text{ and } m \equiv 0 \pmod{2}, \\ f(m, m) - (m - n) & \text{if } m \ge n \text{ and } m \equiv 1 \pmod{2}. \\ \end{cases}

### Closed Form Expression[](https://susam.net/zigzag-number-spiral.html#closed-form-expression-2)

If we take a close look at the last formula in the previous section, we find that in each expression, one variable plays a dominant role, i.e., it occurs more frequently in the expression than the other. In the first two expressions n n  plays the dominant role whereas in the last two expressions m m  plays the dominant role. In fact, in each expression, the dominant variable is the one that is greater than or equal to the other. With this in mind, we can rewrite the above formula as f(m,n)={f(max⁡(m,n),max⁡(m,n))+(m−n)if max⁡(m,n)≡0(m o d 2),f(max⁡(m,n),max⁡(m,n))−(m−n)if max⁡(m,n)≡1(m o d 2). f(m, n) = \begin{cases} f(\max(m, n), \max(m, n)) + (m - n) & \text{if } \max(m, n) \equiv 0 \pmod{2}, \\ f(\max(m, n), \max(m, n)) - (m - n) & \text{if } \max(m, n) \equiv 1 \pmod{2}. \\ \end{cases}  The only difference between the expressions is the sign of the second term: it is positive when max⁡(m,n) \max(m, n)  is even and negative when max⁡(m,n) \max(m, n)  is odd. As a result, we can rewrite the above formula as a single expression like this: f(m,n)=f(max⁡(m,n),max⁡(m,n))+(−1)max⁡(m,n)(m−n). f(m, n) = f(\max(m, n), \max(m, n)) + (-1)^{\max(m, n)} (m - n).  Using the formula f(n,n)=n 2−n+1 f(n, n) = n^2 - n + 1  from the previous section, we get f(m,n)=(max⁡(m,n))2−max⁡(m,n)+1+(−1)max⁡(m,n)(m−n). f(m, n) = (\max(m, n))^2 - \max(m, n) + 1 + (-1)^{\max(m, n)} (m - n).  We arrive again at the same closed-form expression, this time by focusing on the diagonal of the grid.

References[](https://susam.net/zigzag-number-spiral.html#references)
--------------------------------------------------------------------

*   [Number Spiral](https://cses.fi/problemset/task/1071) from the CSES Problem Set 
*   [Closed-Form Solution](https://mathworld.wolfram.com/Closed-FormSolution.html) by Christopher Stover and Eric W. Weisstein 
*   [Piecewise Function](https://mathworld.wolfram.com/PiecewiseFunction.html) by Eric W. Weisstein
