# CHOCDISTRIB - Rating 595

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chocolate Distribution

Christmas is the season of giving. As a part of celebrating the New Year, you decided to give away chocolates to the poor children in your neighbourhood.
Some of them even asked for $2$ chocolates and being the kind soul that you are, you always gave them if you could. They never asked for more than $2$ though because they are not greedy.

Now, you have forgotten exactly how many children you gave chocolates to. However, you remember that you started with $N$ chocolates and distributed all of them by the end.
Find the  **minimum**  and  **maximum**  number of possible children that you gave chocolates to.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one integer $N$, the number of chocolates you started with.
### Output Format

For each test case, output on a new line, two space-separated integers, the minimum possible number of children and the maximum possible number (in this order).

### Constraints
- $1 \le T \le 1000$
- $1 \le N \le 1000$
### Sample 1:
Input
Output

```
4
1
2
7
8

```

```
1 1
1 2
4 7
4 8

```

### Explanation:

 **Test case $1$:**  You had only $1$ chocolate, so that must have been given to only $1$ child.

 **Test case $2$:**  You had $2$ chocolates, so either you could have given both chocolates to $1$ child only, or $1$ chocolate each to $2$ children.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T12:51:45.758Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    print(-(-n//2),n)
```

---

[View on CodeChef](https://www.codechef.com/problems/CHOCDISTRIB)