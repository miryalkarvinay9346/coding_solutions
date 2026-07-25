# MERGESORTED - Rating 1050

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Merge two sorted arrays

You are given two sorted arrays $A$ and $B$ of size $N$ and $M$ respectively. You need to merge these two arrays and keep the final array sorted.

### Input Format
- The first line contains two integers $N$ and $M$ — the size of array $A$ and $B$
- The second line contains all the elements of array $A$
- The third line contains all the elements of array $B$
### Output Format

Output the merged array elements on a single line.

### Constraints
- $1 \leq N, M \leq 10^5$
- $1 \leq A_i, B_i \leq 10^5$
### Sample 1:
Input
Output

```
5 4
1 4 8 9 10
2 3 5 6
```

```
1 2 3 4 5 6 8 9 10
```

### Sample 2:
Input
Output

```
1 2
10
1 2
```

```
1 2 10
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-25T06:16:24.837Z  

```py
# cook your dish here
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b :
    a.append(i)
a.sort()
for i in a:
    print(i,end=" ")
```

---

[View on CodeChef](https://www.codechef.com/problems/MERGESORTED)