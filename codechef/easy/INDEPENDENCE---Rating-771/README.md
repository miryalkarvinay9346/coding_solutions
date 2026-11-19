# INDEPENDENCE - Rating 771

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Independence Day 101

On the occasion of Independence Day, Chef wants to design a new flag for the country of Chefland.

He has some equal-sized strips in three different colors and needs to arrange them in a line so that no two adjacent strips share the same color.

Given that Chef has $A$ orange strips, $B$ white strips, and $C$ green strips, determine if it is possible to design such a flag using all the strips.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $A, B,$ and $C$ — the number of strips of orange, white, and green color respectively.
### Output Format

For each test case, output on a new line, `YES`, if it is possible to design a flag using all the strips such that no two adjacent strips share the same color. Otherwise, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq A, B, C \leq 10$
### Sample 1:
Input
Output

```
3
1 1 1
2 3 10
2 3 4

```

```
YES
NO
YES

```

### Explanation:

Let $O, W,$ and $G$ denote one orange, white, and green strip respectively.

 **Test case $1$:**  Consider the flag $OWG$ where all strips are used and no two adjacent strips have the same color.

 **Test case $2$:**  It can be shown that Chef cannot design a flag with all the strips.

 **Test case $3$:**  Consider the flag $GWGOWGOWG$ where all strips are used and no two adjacent strips have the same color.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-19T01:26:14.711Z  

```py
# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().strip().split())
    max_value=max(a,b,c)
    other=a+b+c-max_value
    if max_value <= (other+1):
        print("Yes")
    else:
        print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/INDEPENDENCE)