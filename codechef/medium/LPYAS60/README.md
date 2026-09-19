# LPYAS60

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to print the grade of a student based on the marks he/she has obtained.

 **Grading Rules** 

- Grade A → Marks > 90
- Grade B → Marks > 70
- Grade C → Marks ≥ 40
- Grade F → Marks < 40

 **Input Format** 

- A single integer, representing the student’s marks (0–100).

 **Output Format** 

- A single character (A, B, C, or F), representing the student’s grade.
### Sample 1:
Input
Output

```
95
```

```
A   
```

### Sample 2:
Input
Output

```
40
```

```
C
```

### Sample 3:
Input
Output

```
20
```

```
F
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T16:53:25.316Z  

```py
# cook your dish here
n=int(input())
if n>90:
    print("A")
elif n>70:
    print("B")
elif n>=40:
    print("C")
elif n<40:
    print("F")
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS60)