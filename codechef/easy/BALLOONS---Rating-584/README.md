# BALLOONS - Rating 584

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Coloured Balloons

There are $N$ different colours of balloons, numbered $1$ to $N$. The $i$-th colour balloon costs exactly $i$ rupees. That is, a balloon of colour $1$ costs $1$ rupee, balloon of colour $2$ costs $2$ rupees and so on.

You bought $A_i$ balloons of the $i$-th colour, what is the total cost of all the balloons you bought?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains a single integer $N$ - the number of colours. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the total cost of the balloons.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
2
1
5
3
1 1 1

```

```
5
6

```

### Explanation:

 **Test Case 1**  : You have $5$ balloons of colour $1$, so a total cost of $5 \cdot 1$.

 **Test Case 2**  : $1$ balloon each of colours $1$, $2$, and $3$, thus a cost of $1 + 2 + 3 = 6$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T11:58:27.035Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(n):
        s+=a[i]*(i+1)
    print(s)
```

---

[View on CodeChef](https://www.codechef.com/problems/BALLOONS)