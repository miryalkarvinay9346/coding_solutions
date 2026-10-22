# HOWMANY - Rating 520

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### HOW MANY DIGITS DO I HAVE

Write a program to obtain a number $(N)$ from the user and display whether the number is a one digit number, 2 digit number, 3 digit number or more than 3 digit number

### Input Format

First line will contain the number $N$,

### Output Format

Print "1" if N is a 1 digit number.

Print "2" if N is a 2 digit number.

Print "3" if N is a 3 digit number.

Print "More than 3 digits" if N has more than 3 digits.

### Constraints
- $0 \leq N \leq 1000000$
### Sample 1:
Input
Output

```
9
```

```
1
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T05:31:07.651Z  

```py
# cook your dish here
n=input()
print(len(n) if len(n)<=3 else "More than 3 digits")
```

---

[View on CodeChef](https://www.codechef.com/problems/HOWMANY)