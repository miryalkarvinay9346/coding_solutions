# MERGEPAR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Merging Parity

You are given an array $A$ consisting of $N$ positive integers.

You can perform the following action on the array multiple times (possibly $0$):

- Choose an index $i$ such that $1 \le i < N$, and $A_i$ and $A_{i + 1}$ have the same parity.
- Set $A_i \leftarrow A_i + A_{i + 1}$ (i.e. add $A_{i + 1}$ to $A_i$)
- Delete $A_{i + 1}$ from the array (concatenating the parts formed).

Count the number of possible arrays you can reach by the following operations. Since the answer may be large, find it modulo $998244353$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, \ldots, A_N$.
### Output Format

For each test case, output on a new line the number of possible arrays modulo $998244353$.

### Constraints
- $1 \le T \le 10^4$
- $2 \le N \le 2 \cdot 10^5$
- $1 \le A_i \le 10^9$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
### Sample 1:
Input
Output

```
4
3
1 1 2
3
2 4 6
4
1 2 3 4
8
5 3 2 6 8 5 5 101

```

```
3
4
1
48
```

### Explanation:

 **Test Case 1:**  The $3$ possible arrays are $[1, 1, 2]$, $[2, 2]$ and $[4]$. You can perform one operation on $[1, 1, 2]$ with $i = 1$ to get $[2, 2]$; and then another operation with $i = 1$ to get $[4]$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-22T16:01:37.112Z  

```py
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/MERGEPAR)