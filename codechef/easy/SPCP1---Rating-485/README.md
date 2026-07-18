# SPCP1 - Rating 485

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Water Park

Chef decides to go to the water park to play. To enter the water slide, a person must have a weight of  **at most**  $W$ Kg and a height of  **at least**  $H$ cm.

Chef weighs $60$ Kg and his height is $130$ cm.

Is Chef allowed to enter the water slide?

### Input Format
- The first and only line of input will contain two space-separated integers $W$ and $H$.
### Output Format
- Output YES if Chef can enter the waterslide and NO if he cannot.
- You may print each character of the string in either uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
### Constraints

$1 \leq W, H \leq 1000$

### Sample 1:
Input
Output

```
75 110

```

```
YES
```

### Explanation:

Chef is allowed on the water slide, because:

- His height is $130$ cm, which is $\geq 110$.
- His weight is $60$ kg, which is $\leq 75$.
### Sample 2:
Input
Output

```
55 115

```

```
NO
```

### Explanation:

Chef's height is $\geq 115$ cm, but his weight is greater than $55$ kg.
So, Chef is  **NOT**  allowed on the water slide.

### Sample 3:
Input
Output

```
60 130
```

```
YES
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-18T04:47:55.013Z  

```py
# cook your dish here
w,h=map(int,input().split())
print("YEs" if 60<=w and 130>=h else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/SPCP1)