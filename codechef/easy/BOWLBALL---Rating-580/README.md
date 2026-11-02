# BOWLBALL - Rating 580

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Bowling Balls

Bowling balls come in $11$ total sizes, an integer weight between $6$ and $16$ (measured in pounds).

In a bowling event, Chef is given a total of $N$ bowling balls, with the $i$-th one being $A_i$ pounds. Some of the bowling balls may have the same weight as the others.

Chef can use a bowling ball which is at least $X$ pounds, and at most $Y$ pounds. Find the number of bowling balls Chef can use.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains $3$ integers - $N, X$ and $Y$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the number of bowling balls Chef can use.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $6 \le X \le Y \le 16$
- $6 \le A_i \le 16$
### Sample 1:
Input
Output

```
3
4 7 10
6 8 10 11
5 6 16
6 16 16 9 9
1 7 10
16

```

```
2
5
0

```

### Explanation:

 **Test Case 1**  : Chef can use the second and third bowling balls.

 **Test Case 2**  : Chef can use all the bowling balls.

 **Test Case 3**  : Chef can use none of the bowling balls.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T13:16:15.029Z  

```py
# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in a:
        if i>=x and i<=y:
            c+=1
    print(c)
```

---

[View on CodeChef](https://www.codechef.com/problems/BOWLBALL)