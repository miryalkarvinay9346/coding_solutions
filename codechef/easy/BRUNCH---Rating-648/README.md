# BRUNCH - Rating 648

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sunday Brunch

On a sunny Sunday afternoon, Chef prepared a brunch for his $20$ neighbours.
Chef prepared a total of $X$ plates. However, the meal was so good that the neighbours started taking $Y$ plates each.

Find the  **maximum**  number of neighbours Chef can feed  **completely**.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the number of plates Chef prepared and the number of plates each person takes respectively.
### Output Format

For each test case, output on a new line, the  **maximum**  number of neighbours Chef can feed  **completely**.

### Constraints
- $1 \leq T \leq 405$
- $20 \leq X \leq 100$
- $1 \leq Y \leq 5$
### Sample 1:
Input
Output

```
4
20 1
20 2
100 4
74 5

```

```
20
10
20
14

```

### Explanation:

 **Test case $1$:**  Chef prepared $20$ plates and each neighbour eats $1$ plate. Thus, Chef can feed all $20$ neighbours.

 **Test case $2$:**  Chef prepared $20$ plates and each neighbour eats $2$ plates. Thus, Chef can feed only $10$ neighbours.

 **Test case $3$:**  Chef prepared $100$ plates and each neighbour eats $4$ plate. Thus, Chef can feed all $20$ neighbours and still have $20$ plates left.

 **Test case $4$:**  Chef prepared $74$ plates and each neighbour eats $5$ plate. Thus, Chef can feed only $14$ neighbours completely. Note that Chef would still have $74 - 5\cdot 14 = 4$ plates left.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T16:08:12.033Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print(min(20,x//y))
```

---

[View on CodeChef](https://www.codechef.com/problems/BRUNCH)