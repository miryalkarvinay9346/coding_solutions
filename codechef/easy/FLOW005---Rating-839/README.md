# FLOW005 - Rating 839

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Smallest Numbers of Notes

Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
If the sum of Rs.  **N**  is input, write a program to compute smallest number of notes that will combine to give Rs.  **N**.

### Input

The first line contains an integer  **T**, total number of testcases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output

For each test case, display the smallest number of notes that will combine to give  **N**, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000
### Sample 1:
Input
Output

```
3 
1200
500
242
```

```
12
5
7
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T13:18:15.786Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    for x in [100,50,10,5,2,1]:
        y=n//x
        n-=y*x
        c+=y
    print(c)
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW005)