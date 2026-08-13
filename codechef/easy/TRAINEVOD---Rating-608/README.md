# TRAINEVOD - Rating 608

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Train Even or Odd

Chef will be going to the gym for some of the next $N$ days. On the $i$-th day, he is free to go to the gym for $A_i$ hours.

Chef does not want to go the gym every day, because he is lazy. But he also does not want to miss too many days without going to the gym once.

Thus, he decides that he will go  **every alternate day**. He may go on days $1, 3, 5, \ldots$ or days $2, 4, 6, \ldots$.

Find the maximum total hours he can invest in the gym.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains $N$ - the number of days. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$, the number of hours he is free for on the $i$-th day.
### Output Format

For each test case, output on a new line the maximum total hours he can invest.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
3
3
2 5 4
4
6 2 1 7
1
5

```

```
6
9
5
```

### Explanation:

 **Test Case 1**  : Chef can train on days $1, 3$ to spend a total of $6$ hours at the gym. On the other hand, day $2$ alone would only be $5$ hours.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T16:46:50.694Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(0,n,2):
        c1+=a[i]
    for j in range(1,n,2):
        c2+=a[j]
    print(max(c1,c2))
```

---

[View on CodeChef](https://www.codechef.com/problems/TRAINEVOD)