# PAINTCHRIS - Rating 567

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Painting Walls

Chef wants to decorate his house by painting the walls this Christmas.
Each wall has a dimension of $X$ `m` $\times Y$ `m`.

If the cost of paint is $2$ rupees per `m`$^2$, find the  **maximum**  number of walls Chef can paint  **completely**  with $Z$ rupees.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $X, Y,$ and $Z$ — where $X$ and $Y$ denote the dimensions of each wall in metres and $Z$ denotes the money Chef has.
### Output Format

For each test case, output on a new line, the  **maximum**  number of walls Chef can paint completely with $Z$ rupees.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 10$
- $1 \leq Z \leq 100$
### Sample 1:
Input
Output

```
4
3 4 40
4 2 52
9 9 100
1 7 22

```

```
1
3
0
1

```

### Explanation:

 **Test case $1$:**  The area of each wall is $3\cdot 4 = 12$ `m`$^2$. For a budget of $40$ rupees, Chef can paint $20$ `m`$^2$ of walls. Thus, Chef would only be able to paint $1$ wall completely.

 **Test case $2$:**  The area of each wall is $4\cdot 2 = 8$ `m`$^2$. For a budget of $52$ rupees, Chef can paint $26$ `m`$^2$ of walls. Thus, Chef would be able to paint $3$ walls completely.

 **Test case $3$:**  The area of each wall is $9\cdot 9 = 81$ `m`$^2$. For a budget of $100$ rupees, Chef can paint $50$ `m`$^2$ of walls. Thus, Chef would not be able to paint any wall completely.

 **Test case $4$:**  The area of each wall is $1\cdot 7 = 7$ `m`$^2$. For a budget of $22$ rupees, Chef can paint $11$ `m`$^2$ of walls. Thus, Chef would only be able to paint $1$ wall completely.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T17:12:56.963Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a=x*y*2
    print(z//a)
```

---

[View on CodeChef](https://www.codechef.com/problems/PAINTCHRIS)