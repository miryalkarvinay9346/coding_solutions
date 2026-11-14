# MAXTRI - Rating 664

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Max Triangle

You have $N$ sticks of length $1, 2,..., N$ respectively.

Can you make a non-degenerate triangle$^{\dagger}$ with some $3$ sticks out of these $N$ sticks? Find the maximum possible perimeter$^{\ddagger}$ of a triangle you can make, or print $-1$ if not possible.

$^{\dagger}$ You can make a non-degenerate triangle with sticks of sizes $A$, $B$ and $C$ if and only if $2 \cdot \max(A, B, C) < A + B + C$.

$^{\ddagger}$ The perimeter of a triangle made with sticks of lengths $A$, $B$ and $C$ is $A + B + C$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of input contains $N$ - the number of sticks.
### Output Format

For each test case, output the maximum perimeter or $-1$ if not possible.

### Constraints
- $1 \le T \le 10^4$
- $3 \le N \le 10^8$
### Sample 1:
Input
Output

```
2
4
3

```

```
9
-1

```

### Explanation:

 **Test Case 1**  : You can make a triangle with the sticks of sies $4$, $3$ and $2$. This has the maximum perimeter possible of $4 + 3 + 2 = 9$.

 **Test Case 2**  : No triangle is possible.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T11:48:13.110Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n<=3:
        print(-1)
    else:
        print(3*(n-1))
```

---

[View on CodeChef](https://www.codechef.com/problems/MAXTRI)