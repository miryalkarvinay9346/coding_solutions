# TWOROLL - Rating 653

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Two Rolls

Chef is playing a board game, and is currently at position $X$.
To win, he needs to reach position $50$.

Chef has a pair of $6$-sided dice, which will decide how he moves - he will roll the pair of dice, sum up the numbers on them, and then move exactly that many steps forward.
More precisely, if the dice show values of $d_1$ and $d_2$, Chef must move from $X$ to $(X+d_1+d_2)$.

However, Chef's dice are a bit weird: rather than starting from $1$, they start from $Y$.
That is, the values on a single die are $Y, Y+1, Y+2, Y+3, Y+4, Y+5$.

Is it possible for Chef to win the game by reaching position $50$, after  **exactly one turn** ?
Note that Chef must exactly land on position $50$ after his move - going beyond it does not count as a win.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line and only of each test case contains two space-separated integers $X$ and $Y$ — the current position of Chef and the starting value on the dice, respectively.
### Output Format

For each test case, output on a new line the answer: $\text{Yes}$ if Chef can reach position $50$ in exactly one turn, and $\text{No}$ otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings $\text{NO}, \text{No}, \text{nO},$ and $\text{no}$ will all be treated as equivalent.

### Constraints
- $1 \leq T \leq 2500$
- $1 \leq X \lt 50$
- $1 \leq Y \leq 50$
### Sample 1:
Input
Output

```
4
46 1
36 1
36 2
28 14

```

```
Yes
No
Yes
No
```

### Explanation:

 **Test case $1$:**  Chef is at $X = 46$ and needs to reach $50$. The dice have the values $1$ to $6$ on them.
This is possible: one way is if the dice roll values $(1, 3)$, for example.

 **Test case $2$:**  Chef is at $X = 36$ and needs to reach $50$. The dice have the values $1$ to $6$ on them.
This is impossible: no matter what the dice show, reaching $50$ is not possible.

 **Test case $3$:**  Chef is at $X = 36$ and needs to reach $50$. The dice have the values $2$ to $7$ on them.
This is possible if the dice roll values $(7, 7)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-07T09:01:44.974Z  

```py
# cook your dish here
x = int(input())
for _ in range(x):
    a, b = map(int, input().split())
    required = 50 - a
    min_sum = 2 * b
    max_sum = 2 * b + 10
    if min_sum <= required <= max_sum:
        print("yes")
    else:
        print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/TWOROLL)