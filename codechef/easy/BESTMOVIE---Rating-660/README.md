# BESTMOVIE - Rating 660

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Best Movie

You want to rent a movie. There are $N$ movies and the $i$-th movie has an IMDB score of $A_i$ and costs $B_i$ to rent. Note that IMDB scores can only be  **integers**  in the range $1$ to $10$ for the sake of this problem.

You will only watch movies with an IMDB score of at least $7$. Find the minimum cost of a movie that you are willing to watch.

There may be no movies available with an IMDB score of at least $7$. Print $-1$ then.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains $N$ - the number of movies. The $i$-th of the next $N$ lines contain $2$ integers each - $A_i$ and $B_i$.
### Output Format

For each test case, output the minimum cost of a movie with a IMDB rating of at least $7$, or $-1$ if no such movie.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le 10$
- $100 \le B_i \le 1000$
### Sample 1:
Input
Output

```
3
3
8 400
7 350
6 100
2
5 100
4 200
4
9 150
7 200
7 180
5 180

```

```
350
-1
150

```

### Explanation:

 **Test Case 1**  : You can buy the $2^{nd}$ movie which has an IMDB rating of $7$ and a cost of $350$. The $1^{st}$ movie has a larger IMDB rating, but is also more costly. the $3^{rd}$ movie has lower than $7$ IMDB rating.

 **Test Case 2**  : There are no movies available with IMDB rating of at least $7$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T03:51:58.144Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        k,m=map(int,input().split())
        a.append(k)
        b.append(m)
    c=float('inf')
    v=0
    vc=False
    for i in range(n):
        if a[i]>=7:
            c=min(c,b[i])
        else:
            v=v+1
            if v==n:
                vc=True
                break
    if vc==True:
        print(-1)
    else:
        print(c)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/BESTMOVIE)