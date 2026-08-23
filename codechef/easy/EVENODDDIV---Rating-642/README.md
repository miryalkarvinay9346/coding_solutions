# EVENODDDIV - Rating 642

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Even vs Odd Divisors

Given an integer $N$, let

- $f(N)$ denote the number of even divisors of $N$
- $g(N)$ denote the number of odd divisors of $N$.

For example, the divisors of $6$ are $1, 2, 3$ and $6$. $f(N) = 2, g(N) = 2$ as there are $2$ even and $2$ odd numbers in this list;.

Find whether $f(N) > g(N)$ or $f(N) = g(N)$ or $f(N) < g(N)$.

Output

- $1$ if $f(N) > g(N)$
- $0$ if $f(N) = g(N)$
- $-1$ if $f(N) < g(N)$
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line consists of a single integer $N$.
### Output Format

For each test case, output on a new line :

- $1$ if $f(N) > g(N)$
- $0$ if $f(N) = g(N)$
- $-1$ if $f(N) < g(N)$
### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
### Sample 1:
Input
Output

```
6
1
2
3
4
5
6

```

```
-1
0
-1
1
-1
0
```

### Explanation:

 **Test Case 1**  : $1$ has only $1$ divisor, which is odd. Hence $f(1) = 0, g(1) = 1$, and we can see $f(1) < g(1)$.

 **Test Case 2**  : $2$ has $2$ factors - $1$ and $2$. Hence, $f(2) = 1$, $g(2) = 1$ and we see $f(2) = g(2)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-23T02:50:39.480Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    ed,od=0,0
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                ed+=1
            else:
                od+=1
    if ed==od:
        print(0)
    elif ed>od:
        print(1)
    else:
        print(-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/EVENODDDIV)