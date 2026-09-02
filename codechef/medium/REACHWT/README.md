# REACHWT

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Reach Weight

You need to buy some weights that total to exactly $N$ kg.

You can buy either $1$ kg weights for $20$ rupees, or $2$ kg weights for $30$ rupees.

Find the minimum cost to buy such a set of weights that sum to $N$ kg.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line contains a single integer $N$.
### Output Format

For each test case, output on a new line the minimum total cost of buying a set of weights that total to exactly $N$ kg.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
### Sample 1:
Input
Output

```
3
1
2
3

```

```
20
30
50

```

### Explanation:

 **Test Case 1:**  You buy $1$ one-kg weight for a cost of $20$.

 **Test Case 2:**  You buy $1$ two-kg weight for a cost of $30$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T14:37:26.634Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%2!=0:
        k=n//2
        print(k*30+20)
    else:
        k=n//2
        print(k*30)
```

---

[View on CodeChef](https://www.codechef.com/problems/REACHWT)