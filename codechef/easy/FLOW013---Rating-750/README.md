# FLOW013 - Rating 750

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Valid Triangles

Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then  **T**  lines follow, each line contains three angles  **A**,  **B**  and  **C**, of the triangle separated by space.

### Output Format

For each test case, display 'YES' if the triangle is valid, and 'NO', if it is not, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ A,B,C ≤ 180
### Sample 1:
Input
Output

```
3 
40 40 100
45 45 90
180 1 1

```

```
YES
YES
NO

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T16:54:24.153Z  

```py
# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print("YES" if a+b+c==180 else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW013)