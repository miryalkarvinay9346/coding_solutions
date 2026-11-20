# FARFROMO - Rating 750

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Far from origin

Alex, Bob, and, Chef are standing on the coordinate plane. Chef is standing at the origin (coordinates $(0, 0)$) while the location of Alex and Bob are $(X_1, Y_1)$ and $(X_2, Y_2)$ respectively.

Amongst Alex and Bob, find out who is at a farther distance from Chef or determine if both are at the same distance from Chef.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers $X_1, Y_1, X_2,$ and $Y_2$ — the coordinates of Alex and Bob.
### Output Format

For each test case, output on a new line:

- ALEX, if Alex is at a farther distance from Chef.
- BOB, if Bob is at a farther distance from Chef.
- EQUAL, if both are standing at the same distance from Chef.

You may print each character in uppercase or lowercase. For example, `Bob`, `BOB`, `bob`, and `bOB`, are all considered identical.

### Constraints
- $1 \leq T \leq 2000$
- $-1000 \leq X_1, Y_1, X_2, Y_2 \leq 1000$
### Sample 1:
Input
Output

```
3
-1 0 3 4
3 4 -4 -3
8 -6 0 5

```

```
BOB
EQUAL
ALEX
```

### Explanation:

 **Test case $1$:**  Alex is at a distance $1$ from Chef while Bob is at distance $5$ from Chef. Thus, Bob is at a farther distance.

 **Test case $2$:**  Alex is at a distance $5$ from Chef and Bob is also at distance $5$ from Chef. Thus, both are at the same distance.

 **Test case $3$:**  Alex is at a distance $10$ from Chef while Bob is at distance $5$ from Chef. Thus, Alex is at a farther distance.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T16:08:02.705Z  

```py
# cook your dish here
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    a=(x1**2)+(y1**2)
    b=(x2**2)+(y2**2)
    if a==b:
        print("EQUAL")
    elif a>b:
        print("ALEX")
    else:
        print("BOB")
```

---

[View on CodeChef](https://www.codechef.com/problems/FARFROMO)