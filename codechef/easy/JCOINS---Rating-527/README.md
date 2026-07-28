# JCOINS - Rating 527

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Janmansh and Coins

Janmansh received $X$ coins of $10$ rupees and $Y$ coins of $5$ rupees from Chingari. Since he is weak in math, can you find out how much total money does he have?

### Input Format
- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$, $Y$ - the number of $10$ and $5$ rupee coins respectively.
### Output Format

For each test case, output how much total money does Janmansh have.

### Constraints
- $1 \le T \le 100$
- $0 \le X, Y \le 100$
### Sample 1:
Input
Output

```
2
2 1
3 4

```

```
25
50

```

### Explanation:

 **Test case-1:**  He has $2$ coins of $10$ rupees and $1$ coin of $5$ rupees. Hence he has $2 \cdot 10+5 = 25$ rupees.

 **Test case-2:**  He has $3$ coins of $10$ rupees and $4$ coins of $5$ rupees. Hence he has $3 \cdot 10 + 4 \cdot 5 = 50$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T17:06:41.116Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print(x*10+y*5)
```

---

[View on CodeChef](https://www.codechef.com/problems/JCOINS)