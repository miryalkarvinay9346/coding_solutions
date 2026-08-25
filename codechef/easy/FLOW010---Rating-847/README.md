# FLOW010 - Rating 847

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Id and Ship

Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

Class ID	Ship Class
B or b	BattleShip
C or c	Cruiser
D or d	Destroyer
F or f	Frigate
### Input Format

The first line contains an integer  **T**, the total number of testcases. Then  **T**  lines follow, each line contains a character.

### Output Format

For each test case, display the Ship Class depending on ID, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
### Sample 1:
Input
Output

```
3 
B
c
D

```

```
BattleShip
Cruiser
Destroyer

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T16:57:23.998Z  

```py
# cook your dish here
for _ in range(int(input())):
    a=input().lower()
    if a=="b":
        print("BattleShip")
    elif a=="c":
        print("Cruiser")
    elif a=="d":
        print("Destroyer")
    else:
        print("Frigate")
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW010)