# WRAPGIFTS - Rating 574

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Christmas Gifts

Chef is wrapping Christmas gifts for his friends. He has a rectangular sheet of wrapping paper with a total area of $1000$ square centimeters. Each identical gift is a rectangular box with dimensions:

- Height $(H)$ centimeters
- Length $(L)$ centimeters
- Width $(W)$ centimeters

To wrap a gift, Chef needs enough paper to cover all six faces of the box, with no overlapping or gaps. Calculate the  **maximum**  number of complete gifts Chef can wrap using the available wrapping paper.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $H, L$ and $W$ — the dimensions of each gift box.
### Output Format

For each test case, output on a new line, the  **maximum**  number of complete gifts Chef can wrap using the available wrapping paper.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq H, L, W \leq 10$
### Sample 1:
Input
Output

```
3
1 1 2
4 2 6
10 2 4

```

```
100
11
7

```

### Explanation:

 **Test case $1$:**  With given dimensions, surface area of one gift is $2\cdot (1\cdot 1 + 1\cdot 2 + 1\cdot 2) = 10$ sq cm. Thus, Chef can wrap a total of $100$ gifts.

 **Test case $2$:**  With given dimensions, surface area of one gift is $2\cdot (4\cdot 2 + 2\cdot 6 + 6\cdot 4) = 88$ sq cm. Thus, Chef can wrap a total of $11$ gifts.

 **Test case $3$:**  With given dimensions, surface area of one gift is $2\cdot (10\cdot 2 + 2\cdot 4 + 10\cdot 4) = 136$ sq cm. Thus, Chef can wrap a total of $7$ gifts.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T15:47:13.368Z  

```py
# cook your dish here
for _ in range(int(input())):
    l,b,w=map(int,input().split())
    a=2*(l*b+b*w+w*l)
    print(1000//a)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/WRAPGIFTS)