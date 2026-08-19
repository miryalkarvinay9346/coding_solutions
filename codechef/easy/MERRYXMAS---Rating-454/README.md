# MERRYXMAS - Rating 454

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Merry Christmas!

Chef is planning Christmas festivities and has three activities to choose from:

- Decorating a Christmas tree, which takes $1$ hour.
- Baking cookies, which takes $2$ hours.
- Making a gingerbread house, which takes $4$ hours.

Given that Chef has $X$ hours available, determine the maximum number of activities he can complete.

Note that no two activities can overlap in time.

### Input Format
- The first and only line of input will contain a single integer $X$, denoting the number of hours Chef has.
### Output Format

Output on a new line, the maximum number of activities he can complete.

### Constraints
- $1 \leq X \leq 10$
### Sample 1:
Input
Output

```
2
```

```
1
```

### Explanation:

Since Chef has $2$ hours, he can only complete one activity. It can be either decorating the tree or baking cookies.

### Sample 2:
Input
Output

```
6
```

```
2
```

### Explanation:

In $6$ hours Chef can complete any $2$ activities out of three.

### Sample 3:
Input
Output

```
10
```

```
3
```

### Explanation:

Chef can complete all three activities in $4+2+1 = 7$ hours.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T14:11:41.411Z  

```py
# cook your dish here
x=int(input())
if x>=7:
    print(3)
elif x >= 3:
    print(2)
else:
    print(1)
        
```

---

[View on CodeChef](https://www.codechef.com/problems/MERRYXMAS)