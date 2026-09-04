# BRKSTICK - Rating 596

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Breaking Sticks

You have $N$ sticks, of integral lengths $A_1, A_2,..., A_N$.

You can take any stick of length $X$ and break it into $2$  **positive integer**  lengths $Y$ and $Z$ such that $Y + Z = X$, i.e. now instead of the stick of length $X$, you obtained one stick of length $Y$ and another of length $Z$.

One such action is called a  **break**. Find the maximum number of  **breaks**  you can perform.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of input contains $N$ - the number of sticks. The second line contains $N$ integers - $A_1, A_2,..., A_N$, the lengths of the sticks
### Output Format

For each test case, find the maximum number of  **breaks**  you can perform.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
2
2
1 1
1
3

```

```
0
2

```

### Explanation:

 **Test Case 1**  : There are no possible  **breaks**  to do because it is not possible to split $1$ into $2$ positive integer numbers.

 **Test Case 2**  : We can break the stick of length $3$ into sticks of lengths $2$ and $1$. Further, we then break the stick of length $2$ into sticks of lengths $1$ and $1$. Thus, we performed $2$  **breaks**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T08:11:02.237Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(sum(a)-n)
```

---

[View on CodeChef](https://www.codechef.com/problems/BRKSTICK)