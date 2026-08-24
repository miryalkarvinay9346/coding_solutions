# SCORING - Rating 569

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Scoring

Alice and Bob were playing a game with points to score. Each player's score is some non-negative integer number of points.

In the end, Alice won the game by scoring $X$ more points than Bob. Further, it is known that the total number of points scored by both of them was $Y$.

With this information, your task is to find how many points Alice scored, and how many points Bob scored. It is guaranteed that the input is generated such that there exists a valid solution.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $2$ integers - $X$ and $Y$.
### Output Format

For each test case, output on a new line Alice and Bob's scored points.

### Constraints
- $1 \le T \le 100$
- $1 \le X, Y \le 100$
- There exists a valid solution to each input test.
### Sample 1:
Input
Output

```
3
1 1
2 8
6 8

```

```
1 0
5 3
7 1

```

### Explanation:

 **Test Case 1**  : It is given that Alice scored $1$ more point than Bob, and the total scored points was $1$. In this case, the only possible solution is Alice scored $1$ point and Bob scored $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-24T10:22:13.759Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    """
    alice=bob+x
    alice+bob=y
    -----------
    2*bob+x=y
    bob=(y-x)/2
    -------------
    alice=((y-x)/2)+x
    -----------------
    """
    print(((y-x)//2)+x,(y-x)//2)
```

---

[View on CodeChef](https://www.codechef.com/problems/SCORING)