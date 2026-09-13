# LAZYCHF - Rating 801

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Lazy Chef

Chef is a very lazy person. Whatever work is supposed to be finished in $x$ units of time, he finishes it in $m * x$ units of time. But there is always a limit to laziness, so he delays the work by at max $d$ units of time. Given $x, m, d$, find the maximum time taken by Chef to complete the work.

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains a single line of input, three integers $x, m, d$.
### Output Format

For each testcase, output in a single line answer to the problem.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq x, m \leq 10$
- $0 \leq d \lt 100$
### Sample 1:
Input
Output

```
3
1 1 0
1 3 1
2 2 3
```

```
1
2
4
```

### Explanation:

 **TestCase $1$:**  Chef takes $1 * 1 = 1$ unit of time which is equal to the upper bound($1 + 0 = 1$ unit) to do the work.

 **TestCase $2$:**  Chef takes $min(1 * 3, 1 + 1) = min(3, 2) = 2$ units of time to do the work.

 **TestCase $3$:**  Chef takes $2 * 2 = 4$ units of time which is less than the upper bound($2 + 3 = 5$ units) to do the work.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T16:11:42.826Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,m,d=map(int,input().split())
    print(min(x*m,x+d))
```

---

[View on CodeChef](https://www.codechef.com/problems/LAZYCHF)