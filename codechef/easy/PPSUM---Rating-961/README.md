# PPSUM - Rating 961

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Puppy and Sum

Yesterday, puppy Tuzik learned a magically efficient method to find the sum of the integers from  **1**  to  **N**. He denotes it as  **sum(N)**. But today, as a true explorer, he defined his own new function:  **sum(D, N)**, which means the operation  **sum**  applied  **D**  times: the first time to  **N**, and each subsequent time to the result of the previous operation.

For example, if  **D = 2**  and  **N = 3**, then  **sum(2, 3)**  equals to  **sum(sum(3)) = sum(1 + 2 + 3) = sum(6) = 21**.

Tuzik wants to calculate some values of the  **sum(D, N)**  function. Will you help him with that?

### Input

The first line contains a single integer  **T**, the number of test cases. Each test case is described by a single line containing two integers  **D**  and  **N**.

### Output

For each testcase, output one integer on a separate line.

### Constraints
- 1 ≤ T ≤ 16
- 1 ≤ D, N ≤ 4
### Sample 1:
Input
Output

```
2
1 4
2 3
```

```
10
21
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-01T17:01:33.792Z  

```py
# cook your dish here
for _ in range(int(input())):
    d,n=map(int,input().split())
    s=1
    for i in range(d):
        s=(n*(n+1)//2)
        n=s
    print(s)
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSUM)