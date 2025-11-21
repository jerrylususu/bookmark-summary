Title: Fizz Buzz with Cosines - Susam Pal

URL Source: https://susam.net/fizz-buzz-with-cosines.html

Markdown Content:
By **Susam Pal** on 20 Nov 2025

Fizz Buzz is a counting game that has become oddly popular in the world of computer programming as a simple test of basic programming skills. The rules of the game are straightforward. Players say the numbers aloud in order beginning with one. Whenever a number is divisible by 3, they say 'Fizz' instead. If it is divisible by 5, they say 'Buzz'. If it is divisible by both 3 and 5, the player says both 'Fizz' and 'Buzz'. Here is a typical Python program that prints this sequence:

```
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
```

Here is the output: [fizz-buzz.txt](https://susam.net/files/blog/fizz-buzz.txt). Can we make the program more complicated? Perhaps we can use trigonometric functions to encode all four cases in a single closed-form expression. That is what we are going to explore in this article. By the end, we will obtain a finite Fourier series that can take any integer n n  and select the text to be printed.

Contents[](https://susam.net/fizz-buzz-with-cosines.html#contents)
------------------------------------------------------------------

*   [Definitions](https://susam.net/fizz-buzz-with-cosines.html#definitions)
    *   [Symbol Functions](https://susam.net/fizz-buzz-with-cosines.html#symbol-functions)
    *   [Fizz Buzz Sequence](https://susam.net/fizz-buzz-with-cosines.html#fizz-buzz-sequence)

*   [Indicator Functions](https://susam.net/fizz-buzz-with-cosines.html#indicator-functions)
*   [Complex Exponentials](https://susam.net/fizz-buzz-with-cosines.html#complex-exponentials)
*   [Cosines](https://susam.net/fizz-buzz-with-cosines.html#cosines)
*   [Conclusion](https://susam.net/fizz-buzz-with-cosines.html#conclusion)

Definitions[](https://susam.net/fizz-buzz-with-cosines.html#definitions)
------------------------------------------------------------------------

Before going any further, we establish a precise mathematical definition for the Fizz Buzz sequence. We begin by introducing a few functions that will help us define the Fizz Buzz sequence later.

### Symbol Functions[](https://susam.net/fizz-buzz-with-cosines.html#symbol-functions)

We define a set of four functions {s 0,s 1,s 2,s 3} \{ s_0, s_1, s_2, s_3 \}  for integers n n  by: s 0(n)=n,s 1(n)=F i z z,s 2(n)=B u z z,s 3(n)=F i z z B u z z.\begin{align*} s_0(n) &= n, \\ s_1(n) &= \mathtt{Fizz}, \\ s_2(n) &= \mathtt{Buzz}, \\ s_3(n) &= \mathtt{FizzBuzz}. \end{align*} We call these the symbol functions because they produce every term that appears in the Fizz Buzz sequence. The symbol function s 0 s_0  returns n n  itself. The functions s 1, s_1, s 2 s_2  and s 3 s_3  are constant functions that always return the literal words F i z z, \mathtt{Fizz}, B u z z \mathtt{Buzz}  and F i z z B u z z \mathtt{FizzBuzz}  respectively, no matter what the value of n n  is.

### Fizz Buzz Sequence[](https://susam.net/fizz-buzz-with-cosines.html#fizz-buzz-sequence)

Now we can define the Fizz Buzz sequence as the sequence (s f(n)(n))n=1∞ (s_{f(n)}(n))_{n = 1}^{\infty}  where f(n)={1 if 3∣n and 5∤n,2 if 3∤n and 5∣n,3 if 3∣n and 5∣n,0 otherwise. f(n) = \begin{cases} 1 & \text{if } 3 \mid n \text{ and } 5 \nmid n, \\ 2 & \text{if } 3 \nmid n \text{ and } 5 \mid n, \\ 3 & \text{if } 3 \mid n \text{ and } 5 \mid n, \\ 0 & \text{otherwise}. \end{cases}  The notation m∣n m \mid n  means that the integer m m  divides the integer n, n,  i.e. n n  is a multiple of m. m.  Equivalently, there exists an integer c c  such that n=c m. n = cm .  Similarly, m∤n m \nmid n  means that m m  does not divide n, n,  i.e. n n  is not a multiple of m. m.  With the above definitions in place, we can expand the first few terms of the sequence explicitly as follows: (s f(n)(n))n=1∞=(s f(1)(1),s f(2)(2),s f(3)(3),s f(4)(4),s f(5)(5),s f(6)(6),s f(7)(7),…)=(s 0(1),s 0(2),s 1(3),s 0(4),s 2(5),s 1(6),s 0(7),…)=(1,2,F i z z,4,B u z z,F i z z,7,…).\begin{align*} (s_{f(n)}(n))_{n = 1}^{\infty} &= (s_{f(1)}(1), \; s_{f(2)}(2), \; s_{f(3)}(3), \; s_{f(4)}(4), \; s_{f(5)}(5), \; s_{f(6)}(6), \; s_{f(7)}(7), \; \dots) \\ &= (s_0(1), \; s_0(2), \; s_1(3), \; s_0(4), s_2(5), \; s_1(6), \; s_0(7), \; \dots) \\ &= (1, \; 2, \; \mathtt{Fizz}, \; 4, \; \mathtt{Buzz}, \; \mathtt{Fizz}, \; 7, \; \dots). \end{align*} Note how the function f(n) f(n)  produces an index i i  which we then use to select the symbol function s i(n) s_i(n)  to produce the n n th term of the sequence.

Indicator Functions[](https://susam.net/fizz-buzz-with-cosines.html#indicator-functions)
----------------------------------------------------------------------------------------

Here is the function f(n) f(n)  from the previous section with its cases and conditions rearranged to make it easier to spot interesting patterns: f(n)={0 if 5∤n and 3∤n,1 if 5∤n and 3∣n,2 if 5∣n and 3∤n,3 if 5∣n and 3∣n. f(n) = \begin{cases} 0 & \text{if } 5 \nmid n \text{ and } 3 \nmid n, \\ 1 & \text{if } 5 \nmid n \text{ and } 3 \mid n, \\ 2 & \text{if } 5 \mid n \text{ and } 3 \nmid n, \\ 3 & \text{if } 5 \mid n \text{ and } 3 \mid n. \end{cases}  This function helps us to select another function s f(n)(n) s_{f(n)}(n)  which in turn determines the n n th term of the Fizz Buzz sequence. Our goal now is to replace this piecewise formula with a single closed-form expression. To do so, we first define indicator functions I m(n) I_m(n)  as follows: I m(n)={1 if m∣n,0 if m∤n. I_m(n) = \begin{cases} 1 & \text{if } m \mid n, \\ 0 & \text{if } m \nmid n. \end{cases}  The formula for f(n) f(n)  can now be written as: f(n)={0 if I 5(n)=0 and I 3(n)=0,1 if I 5(n)=0 and I 3(n)=1,2 if I 5(n)=1 and I 3(n)=0,3 if I 5(n)=1 and I 3(n)=1. f(n) = \begin{cases} 0 & \text{if } I_5(n) = 0 \text{ and } I_3(n) = 0, \\ 1 & \text{if } I_5(n) = 0 \text{ and } I_3(n) = 1, \\ 2 & \text{if } I_5(n) = 1 \text{ and } I_3(n) = 0, \\ 3 & \text{if } I_5(n) = 1 \text{ and } I_3(n) = 1. \end{cases}  Do you see a pattern? Here is the same function written as a table:

| I 5(n) I_5(n) | I 3(n) I_3(n) | f(n) f(n) |
| --- | --- | --- |
| 0 0 | 0 0 | 0 0 |
| 0 0 | 1 1 | 1 1 |
| 1 1 | 0 0 | 2 2 |
| 1 1 | 1 1 | 3 3 |

Do you see it now? If we treat the values in the first two columns as binary digits and the values in the third column as decimal numbers, then in each row the first two columns give the binary representation of the number in the third column. For example, 3 10=11 2 3_{10} = 11_2  and indeed in the last row of the table, we see the bits 1 1  and 1 1  in the first two columns and the number 3 3  in the last column. In other words, writing the binary digits I 5(n) I_5(n)  and I 3(n) I_3(n)  side by side gives us the binary representation of f(n). f(n).  Therefore f(n)=2 I 5(n)+I 3(n). f(n) = 2 \, I_5(n) + I_3(n).  We can now write a small program to demonstrate this formula:

```
for n in range(1, 101):
    s = [n, 'Fizz', 'Buzz', 'FizzBuzz']
    i = (n % 3 == 0) + 2 * (n % 5 == 0)
    print(s[i])
```

We can make it even shorter at the cost of some clarity:

```
for n in range(1, 101):
    print([n, 'Fizz', 'Buzz', 'FizzBuzz'][(n % 3 == 0) + 2 * (n % 5 == 0)])
```

What we have obtained so far is pretty good. While there is no universal definition of a closed-form expression, I think most people would agree that the indicator functions as defined above are simple enough to be permitted in a closed-form expression.

Complex Exponentials[](https://susam.net/fizz-buzz-with-cosines.html#complex-exponentials)
------------------------------------------------------------------------------------------

In the previous section, we obtained the formula f(n)=I 3(n)+2 I 5(n) f(n) = I_3(n) + 2 \, I_5(n)  which we then used as an index to look up the text to be printed. We also argued that this is a pretty good closed-form expression already.

However, in the interest of making things more complicated, we must ask ourselves: What if we are not allowed to use the indicator functions? What if we must adhere to the commonly accepted meaning of a closed-form expression which allows only finite combinations of basic operations such as addition, subtraction, multiplication, division, integer exponents and roots with integer index as well as functions such as exponentials, logarithms and trigonometric functions. It turns out that the above formula can be rewritten using only addition, multiplication, division and the cosine function. Let us begin the translation. Consider the sum S m(n)=∑k=0 m−1 e 2 π i k n/m, S_m(n) = \sum_{k = 0}^{m - 1} e^{2 \pi i k n / m},  where i i  is the imaginary unit and n n  and m m  are integers. This is a geometric series in the complex plane with ratio r=e 2 π i n/m. r = e^{2 \pi i n / m}.  If n n  is a multiple of m, m ,  then n=c m n = cm  for some integer c c  and we get r=e 2 π i n/m=e 2 π i c=1. r = e^{2 \pi i n / m} = e^{2 \pi i c} = 1.  Therefore, when n n  is a multiple of m, m,  we get S m(n)=∑k=0 m−1 e 2 π i k n/m=∑k=0 m−1 1 k=m. S_m(n) = \sum_{k = 0}^{m - 1} e^{2 \pi i k n / m} = \sum_{k = 0}^{m - 1} 1^k = m.  If n n  is not a multiple of m, m,  then r≠1 r \ne 1  and the geometric series becomes S m(n)=r m−1 r−1=e 2 π i n−1 e 2 π i n/m−1=0. S_m(n) = \frac{r^m - 1}{r - 1} = \frac{e^{2 \pi i n} - 1}{e^{2 \pi i n / m} - 1} = 0.  Therefore, S m(n)={m if m∣n,0 if m∤n. S_m(n) = \begin{cases} m & \text{if } m \mid n, \\ 0 & \text{if } m \nmid n. \end{cases}  Dividing both sides by m, m,  we get S m(n)m={1 if m∣n,0 if m∤n. \frac{S_m(n)}{m} = \begin{cases} 1 & \text{if } m \mid n, \\ 0 & \text{if } m \nmid n. \end{cases}  But the right-hand side is I m(n). I_m(n).  Therefore I m(n)=S m(n)m=1 m∑k=0 m−1 e 2 π i k n/m. I_m(n) = \frac{S_m(n)}{m} = \frac{1}{m} \sum_{k = 0}^{m - 1} e^{2 \pi i k n / m}.

Cosines[](https://susam.net/fizz-buzz-with-cosines.html#cosines)
----------------------------------------------------------------

We begin with Euler's formula e i x=cos⁡x+i sin⁡x e^{i x} = \cos x + i \sin x  where x x  is a real number. From this formula, we get e i x+e−i x=2 cos⁡x. e^{i x} + e^{-i x} = 2 \cos x.  Therefore I 3(n)=1 3∑k=0 2 e 2 π i k n/3=1 3(1+e 2 π i n/3+e 4 π i n/3)=1 3(1+e 2 π i n/3+e−2 π i n/3)=1 3+2 3 cos⁡(2 π n 3).\begin{align*} I_3(n) &= \frac{1}{3} \sum_{k = 0}^2 e^{2 \pi i k n / 3} \\ &= \frac{1}{3} \left( 1 + e^{2 \pi i n / 3} + e^{4 \pi i n / 3} \right) \\ &= \frac{1}{3} \left( 1 + e^{2 \pi i n / 3} + e^{-2 \pi i n / 3} \right) \\ &= \frac{1}{3} + \frac{2}{3} \cos \left( \frac{2 \pi n}{3} \right). \end{align*} The third equality above follows from the fact that e 4 π i n/3=e 6 π i n/3 e−2 π i n/3=e 2 π i n e−2 π i n/3=e−2 π i n/3. e^{4 \pi i n / 3} = e^{6 \pi i n / 3} e^{-2 \pi i n / 3} = e^{2 \pi i n} e^{-2 \pi i n/3} = e^{-2 \pi i n / 3}.

The function above is defined for integer values of n n  but we can extend its formula to real x x  and plot it to observe its shape between integers. As expected, the function takes the value 1 1  whenever x x  is an integer multiple of 3 3  and 0 0  whenever x x  is an integer not divisible by 3. 3.

![Image 1: Graph](https://susam.net/files/blog/fizz-buzz-i3.png)

 Graph of 1 3+2 3 cos⁡(2 π x 3) \frac{1}{3} + \frac{2}{3} \cos \left( \frac{2 \pi x}{3} \right) 

Similarly, I 5(n)=1 5∑k=0 4 e 2 π i k n/5=1 5(1+e 2 π i n/5+e 4 π i n/5+e 6 π i n/5+e 8 π i n/5)=1 5(1+e 2 π i n/5+e 4 π i n/5+e−4 π i n/5+e−2 π i n/5)=1 5+2 5 cos⁡(2 π n 5)+2 5 cos⁡(4 π n 5).\begin{align*} I_5(n) &= \frac{1}{5} \sum_{k = 0}^4 e^{2 \pi i k n / 5} \\ &= \frac{1}{5} \left( 1 + e^{2 \pi i n / 5} + e^{4 \pi i n / 5} + e^{6 \pi i n / 5} + e^{8 \pi i n / 5} \right) \\ &= \frac{1}{5} \left( 1 + e^{2 \pi i n / 5} + e^{4 \pi i n / 5} + e^{-4 \pi i n / 5} + e^{-2 \pi i n / 5} \right) \\ &= \frac{1}{5} + \frac{2}{5} \cos \left( \frac{2 \pi n}{5} \right) + \frac{2}{5} \cos \left( \frac{4 \pi n}{5} \right). \end{align*} Extending this expression to real values of x x  allows us to plot its shape as well. Once again, the function takes the value 1 1  at integer multiples of 5 5  and 0 0  at integers not divisible by 5. 5.

![Image 2: Graph](https://susam.net/files/blog/fizz-buzz-i5.png)

 Graph of 1 5+2 5 cos⁡(2 π x 5)+2 5 cos⁡(4 π x 5) \frac{1}{5} + \frac{2}{5} \cos \left( \frac{2 \pi x}{5} \right) + \frac{2}{5} \cos \left( \frac{4 \pi x}{5} \right) 

Recall that we expressed f(n) f(n)  as f(n)=I 3(n)+2 I 5(n). f(n) = I_3(n) + 2 \, I_5(n).  Substituting these trigonometric expressions yields f(n)=1 3+2 3 cos⁡(2 π n 3)+2⋅(1 5+2 5 cos⁡(2 π n 5)+2 5 cos⁡(4 π n 5)). f(n) = \frac{1}{3} + \frac{2}{3} \cos \left( \frac{2 \pi n}{3} \right) + 2 \cdot \left( \frac{1}{5} + \frac{2}{5} \cos \left( \frac{2 \pi n}{5} \right) + \frac{2}{5} \cos \left( \frac{4 \pi n}{5} \right) \right).  A straightforward simplification gives f(n)=11 15+2 3 cos⁡(2 π n 3)+4 5 cos⁡(2 π n 5)+4 5 cos⁡(4 π n 5). f(n) = \frac{11}{15} + \frac{2}{3} \cos \left( \frac{2 \pi n}{3} \right) + \frac{4}{5} \cos \left( \frac{2 \pi n}{5} \right) + \frac{4}{5} \cos \left( \frac{4 \pi n}{5} \right).  We can extend this expression to real x x  and plot it as well. The resulting curve takes the values 0,1,2 0, 1, 2  and 3 3  at integer points, as desired.

![Image 3: Graph](https://susam.net/files/blog/fizz-buzz-f.png)

 Graph of 11 15+2 3 cos⁡(2 π x 3)+4 5 cos⁡(2 π x 5)+4 5 cos⁡(4 π x 5) \frac{11}{15} + \frac{2}{3} \cos \left( \frac{2 \pi x}{3} \right) + \frac{4}{5} \cos \left( \frac{2 \pi x}{5} \right) + \frac{4}{5} \cos \left( \frac{4 \pi x}{5} \right) 

Now we can write our Python program as follows:

```
from math import cos, pi
for n in range(1, 101):
    s = [n, 'Fizz', 'Buzz', 'FizzBuzz']
    i = round(11 / 15 + (2 / 3) * cos(2 * pi * n / 3)
                      + (4 / 5) * cos(2 * pi * n / 5)
                      + (4 / 5) * cos(4 * pi * n / 5))
    print(s[i])
```

Conclusion[](https://susam.net/fizz-buzz-with-cosines.html#conclusion)
----------------------------------------------------------------------

To summarise, we have defined the Fizz Buzz sequence as (s f(n)(n))n=1∞ (s_{f(n)}(n))_{n = 1}^{\infty}  where f(n)=11 15+2 3 cos⁡(2 π n 3)+4 5 cos⁡(2 π n 5)+4 5 cos⁡(4 π n 5)∈{0,1,2,3} f(n) = \frac{11}{15} + \frac{2}{3} \cos \left( \frac{2 \pi n}{3} \right) + \frac{4}{5} \cos \left( \frac{2 \pi n}{5} \right) + \frac{4}{5} \cos \left( \frac{4 \pi n}{5} \right) \in \{ 0, 1, 2, 3 \}  and s 0(n)=n, s_0(n) = n, s 1(n)=F i z z, s_1(n) = \mathtt{Fizz}, s 2(n)=B u z z s_2(n) = \mathtt{Buzz}  and s 3(n)=F i z z B u z z. s_3(n) = \mathtt{FizzBuzz}.  A Python program to print the Fizz Buzz sequence based on this definition was presented earlier. That program can be written more succinctly as follows:

```
from math import cos, pi
for n in range(1, 101):
    print([n, 'Fizz', 'Buzz', 'FizzBuzz'][round(11 / 15 + (2 / 3) * cos(2 * pi * n / 3) + (4 / 5) * (cos(2 * pi * n / 5) + cos(4 * pi * n / 5)))])
```

The keen-eyed might notice that the expression we have obtained for f(n) f(n)  is a finite Fourier series. This is not surprising, since the output of a Fizz Buzz program depends only on n m o d 15. n \bmod 15.  Any function on a finite cyclic group can be written exactly as a finite Fourier expansion.

We have taken a simple counting game and turned it into a trigonometric construction: a finite Fourier series with a constant term 11/15 11/15  and three cosine terms with coefficients 2/3, 2/3, 4/5 4/5  and 4/5. 4/5.  None of this makes Fizz Buzz any easier, of course, but it does show that every F i z z \mathtt{Fizz}  and B u z z \mathtt{Buzz}  now owes its existence to a particular set of Fourier coefficients. We began with the modest goal of making this simple problem more complicated. I think it is safe to say that we did not fall short.