# SBMD

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Window Medians

You are given an array $A$ of length $N$ and an integer $K$.

Your task is to compute the median of every contiguous subarray of length $K$.

A  **contiguous subarray**  (or simply, a  **subarray**) is a sequence of consecutive elements of the array. For example, if the array is `[2, 4, 3, 5, 8]`, then `[4, 3, 5]` and `[3]` are subarrays, whereas `[2, 3, 8]` is not.

The median of a subarray is the middle element after sorting it. If the subarray has an even number of elements, the median is defined as the  **smaller**  of the two middle elements.

### Input Format
- The first line contains two integers $N$ and $K$ — the length of the array and the size of the subarray.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
### Output Format
- Print $N-K+1$ integers, where the $i^{\text{th}}$ integer is the median of the $i^{\text{th}}$ contiguous subarray of length $K$.
### Constraints
- $1 \le K \le N \le 2 \times 10^5$
- $1 \le A_i \le 10^9$
### Sample 1:
Input
Output

```
7 4
6 2 9 1 5 8 3
```

```
2 2 5 3
```

### Explanation:

The medians of the contiguous subarrays of length $4$ are $2$, $2$, $5$, and $3$, respectively.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T13:48:51.780Z  

```py
# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))

```

---

[View on CodeChef](https://www.codechef.com/problems/SBMD)