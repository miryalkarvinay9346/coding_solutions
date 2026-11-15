# MAKETRIANGLE - Rating 714

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Make Triangle

You are given three integers $X$, $Y$, and $Z$.

In one move, you may increase exactly one of them by $1$. Formally, you may perform one of the following operations:

- $X := X + 1$
- $Y := Y + 1$
- $Z := Z + 1$

Find the minimum number of moves required so that $X$, $Y$, and $Z$ can be the side lengths of a non-degenerate triangle.

$X$, $Y$ and $Z$ can be the sides of a non-degenerate triangle if $X + Y > Z$, $Y + Z > X$ and $X + Z > Y$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $X$, $Y$ and $Z$ — the initial values of the three variables.
### Output Format

For each test case, output on a new line the minimum number of moves required to make $X$, $Y$, and $Z$ the side lengths of a non-degenerate triangle.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, Y, Z \leq 10$
### Sample 1:
Input
Output

```
5
1 2 3
4 3 2
1 10 1
5 5 5
8 1 2

```

```
1
0
9
0
6

```

### Explanation:

 **Test Case 1**  : In one operation, increase $X$ by $1$. Now $(2, 2, 3)$ are valid sides of a non-degenerate triangle.

 **Test Case 2**  : Already the sides are valid.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-15T02:26:27.419Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y>z and x+z>y and z+y>x:
        print("0")
    else:
        a=[x,y,z]
        a.sort()
        print(a[2]-(a[1]+a[0])+1)
```

---

[View on CodeChef](https://www.codechef.com/problems/MAKETRIANGLE)