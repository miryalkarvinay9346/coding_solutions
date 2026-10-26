# NEARSQ - Rating 570

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Nearest Square

You have a positive integer $N$. Find the  **largest positive integer**  $A$ such that:

- $1 \le A \le N$
- $A$ is a square number, i.e. $A = B \cdot B$ for some integer $B$.
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer $N$.
### Output Format

For each test case, output on a new line the largest square integer $A$ smaller than or equal to $N$.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
### Sample 1:
Input
Output

```
3
1
10
48

```

```
1
9
36

```

### Explanation:

 **Test case 1** : $A = 1$ satisfies all the conditions. We cannot choose $A = 9$ because it does not satisfy $A \le N$ condition.

 **Test case 2** : $A = 1, 4, 9$ satisfies all the conditions. We print $9$ because we want the maximum.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T13:16:05.892Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())

    for i in range(1, n + 1):
        if i * i > n:
            print((i - 1) * (i - 1))
            break
    else:
        print(n * n)
    """ 
    for i in range(n,0,-1):
        if n>=i*i:
            print(i*i)
            break"""
```

---

[View on CodeChef](https://www.codechef.com/problems/NEARSQ)