# BAKECAKE2 - Rating 612

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Bakes Cake 2

Chef is an expert baker. To make a cake, he needs $N$ different ingredients numbered $1, 2, \ldots, N$. He needs $A_i$ amount of the ingredient numbered $i$, and he currently has $B_i$ amount of that ingredient already.

Each ingredient costs him $1$ coin to buy. Find the total cost of buying the excess ingredients necessary to make $1$ cake.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains a single integer $N$ - the total number of ingredients. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$. The third line contains $N$ integers - $B_1, B_2, \ldots, B_N$.
### Output Format

For each test case, output on a new line the total cost of buying the necessary ingredients for $1$ cake.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i, B_i \le 100$
### Sample 1:
Input
Output

```
4
1
5
2
2
1 2
2 1
3
3 4 5
1 1 1
1
2
5

```

```
3
1
9
0
```

### Explanation:

 **Test Case 1**  : The cake has only one ingredient, of which you need $5$ to make $1$ cake. Since you already have $2$ of that ingredient, you need to buy $3$ more for a cost of $3$.

 **Test Case 2**  : The cake has $2$ ingredients. You don't need anymore quantity of the ingredient $1$, since you already have $2$ of those but need only $1$. However, you need $1$ more quantity of the ingredient $2$, since you have only $1$ but need $2$. Thus, you pay $1$ coin to buy ingredient $2$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T11:30:57.510Z  

```py
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cost = 0
    for i in range(n):
        if a[i] > b[i]:
            cost += a[i] - b[i]
    print(cost)

```

---

[View on CodeChef](https://www.codechef.com/problems/BAKECAKE2)