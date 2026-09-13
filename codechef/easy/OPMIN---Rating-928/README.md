# OPMIN - Rating 928

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T16:49:11.231Z  

```py
t = int(input())

while t > 0:
    n = int(input())
    a = list(set(list(map(int, input().split()))))
    t -= 1
    # Your code goes here
    a.sort(reverse=True)
    print(a[0]+a[1])
```

---

[View on CodeChef](https://www.codechef.com/problems/OPMIN)