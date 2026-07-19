# CPRIVAL - Rating 501

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Rivalry

Dominater and Everule are very competitive, and keep trying to show that they are better at competitive programming than the other. What better measure is there than their rating?

Both of them participated in a contest. Before the contest, Dominater's rating was $R_1$ and Everule's rating was $R_2$. Dominater's rating changed by $D_1$ in the contest, and Everule's rating changed by $D_2$.

Who has the higher final rating after the contest?
Print "Dominater" if his rating is higher, and "Everule" if his rating is higher (without the quotes).
It is guaranteed they do not have equal ratings at the end of the contest.

### Input Format
- The first line of input will contain two space-separated integers $R_1$ and $R_2$, denoting the initial ratings of Dominater and Everule.
- The second line of input will contain two space-separated integers $D_1$ and $D_2$, denoting the rating changes of Dominater and Everule.
### Output Format

Output `Dominater` or `Everule`, depending on who has a higher rating at the end.

Each character of the output may be printed in either uppercase or lowercase, i.e, `Everule`, `EVERULE`, and `evERuLe` will all be treated as equivalent.

### Constraints
- $1 \leq R_1, R_2 \leq 3000$
- $-200 \leq D_1, D_2 \leq 200$
- It is guaranteed Dominater and Everule have different final ratings.
### Sample 1:
Input
Output

```
1 100
-5 -150

```

```
Dominater

```

### Explanation:

Dominater's final rating after the contest is $1 - 5 = -4$. Everule's final rating is $-50$. Hence, Dominater has a greater final rating.

### Sample 2:
Input
Output

```
2636 2536
-116 -11

```

```
Everule

```

### Explanation:

Dominater's final rating is $2520$. Everule's final rating is $2525$. Hence, Everule has a higher final rating.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-19T18:21:53.999Z  

```py
# cook your dish here
r1,r2=map(int,input().split())
d1,d2=map(int,input().split())
print("Dominator" if r1+d1>r2+d2 else "Everule")
```

---

[View on CodeChef](https://www.codechef.com/problems/CPRIVAL)