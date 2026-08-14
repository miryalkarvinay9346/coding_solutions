# MIXINGLIQ - Rating 553

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Mixing Liquids

Chef is now making orange juice! He has $A$ units of orange syrup, and $B$ units of water.

To make orange juice, Chef must mix the orange syrup and the water in exactly a $1 : 2$ ratio, otherwise the recipe is spoilt. Further, Chef can  **only use integer**  amounts of liquids, because his measuring cylinder cannot accurately measure fractional quantities.

Chef wants to make as much orange juice as possible. How much will he be able to make? The total quantity of orange juice is the sum of units of orange syrup and water.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains $2$ integers - $A$ and $B$.
### Output Format

For each test case, output on a new line the maximum quantity of orange juice Chef can make.

### Constraints
- $1 \le T \le 100$
- $1 \le A, B \le 100$
### Sample 1:
Input
Output

```
3
1 5
5 5
10 1

```

```
3
6
0
```

### Explanation:

 **Test Case 1**  : Chef can mix $1$ unit of orange syrup and $2$ units of water to get $3$ units of orange juice.

 **Test Case 2**  : Chef mixes $2$ units of orange syrup and $4$ units of water.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T07:35:07.976Z  

```py
# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(min(a,b//2)*3)
```

---

[View on CodeChef](https://www.codechef.com/problems/MIXINGLIQ)