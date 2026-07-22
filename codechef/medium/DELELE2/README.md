# DELELE2

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Deleting Elements (Easy)

 **This is the easy version. Here $N, \sum N \le 2000$.** 

An array $A$ is said to be  *deletable*  if it can be reduced to a size less than or equal to $2$ elements with the following operation used multiple times (possibly $0$):

- Choose an index $i$ ($1 < i < |A|$) such that $A_{i - 1} + A_{i + 1} \ge A_i$
- Add $X$ to $A_{i + 1}$ and $Y$ to $A_{i - 1}$ such that $0 \le X, Y$ and $X + Y = A_i$.
- Delete index $i$ and concatenate the parts of the array formed.

You are given an array $A$ of $N$ elements.

Count the number of subarrays of $A$ that are deletable. More formally, count the number of pairs $(L, R)$ such that:

- $1 \le L \le R \le N$
- The array $[A_L, A_{L + 1}, \ldots, A_R]$ is deletable.
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the number of deletable subarrays of $A$.

### Constraints
- $1 \le T \le 400$
- $3 \le N \le 2000$
- $1 \le A_i \le 10^9$
- The sum of $N$ over all test cases does not exceed $2000$.
### Sample 1:
Input
Output

```
3
3
2 4 1
4
2 3 2 3
7
5 1 3 1 10 2 1

```

```
5
10
21
```

### Explanation:

 **Test Case 1:**  There are $6$ subarrays, and all of them are deletable (due to being size $\le 2$ directly) except for $[2, 4, 1]$. Here, we cannot perform any operation.

 **Test Case 2:**  All subarrays are deletable. Here is an example of how we would operate on $[2, 3, 2, 3]$:

- First operation: Choose index $i = 2$, note that $A_2 \le A_1 + A_3$ Add $2$ to $A_1$ and $1$ to $A_3$. Delete $A_2$ Now, the array is $[4, 3, 3]$.
- Second operation: Choose index $i = 2$, note that $A_2 \le A_1 + A_3$ Add $3$ to $A_1$. Delete $A_2$ Now, the array is $[7, 3]$.
- After the second operation, the array is of size $\le 2$. Hence, we are done.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-22T16:00:38.922Z  

```py
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/DELELE2)