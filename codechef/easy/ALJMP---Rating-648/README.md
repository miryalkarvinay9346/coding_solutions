# ALJMP - Rating 648

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Alternate Jumps

There are $N$ lily pads, arranged in a line. They are numbered $1$ to $N$ from left to right.

A frog is initially standing on lily pad $N$. The frog loves to jump, so it will perform a sequence of $(N-1)$ jumps with alternating directions as follows:

- First, jump to the lily pad $N-1$ positions to the left of its current position.
- Next, jump to the lily pad $N-2$ positions to the right of its current position.
- Next, jump to the lily pad $N-3$ positions to the left of its current position. $\vdots$

More formally, in the $i$-th jump $(1 \le i \le N-1$),

- If $i$ is odd, the frog will jump to the lily pad $N-i$ positions to the left of its current position. That is, if its current position is $X$, its new position will be $X - (N-i)$.
- If $i$ is even, the frog will jump to the lily pad $N-i$ positions to the right of its current position. That is, if its current position is $X$, its new position will be $X + (N-i)$.

It can be proved that all of the frog's jumps are valid - that is, it will always be on one of the lily pads $1$ to $N$.

You're given $N$. Can you find the number of the final lily pad the frog will end up at?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing a single integer $N$.
### Output Format

For each test case, output on a new line the answer: the final position of the frog.

### Constraints
- $1 \leq T \leq 100$
- $2 \leq N \leq 100$
### Sample 1:
Input
Output

```
4
2
3
5
6

```

```
1
2
3
3

```

### Explanation:

 **Test case $1$:**  There are two lily pads, numbered $1$ and $2$. The frog is on lily pad $2$.
There will be $N-1 = 1$ move made, in which the frog will jump $1$ step left and hence end up on lily pad $1$.

 **Test case $2$:**  There are three lily pads, numbered $1,2,$ and $3$. The frog is on lily pad $3$.
There will be $N-1 = 2$ jumps made, as follows:

- First jump: jump $2$ positions left. The frog is now on lily pad $3-2=1$.
- Second jump: jump $1$ position right. The frog is now on lily pad $1+1=2$.

So, in the end, the frog is on lily pad $2$.

 **Test case $3$:**  The frog is on lily pad $N = 5$. Four jumps will be made, as follows:

- First jump: $4$ positions left. The frog is now on lily pad $5-4=1$.
- Second jump: $3$ positions right. The frog is now on lily pad $1+3=4$.
- Third jump: $2$ positions left. The frog is now on lily pad $4-2=2$.
- Fourth jump: $1$ positions right. The frog is now on lily pad $2+1=3$.

So, the final answer is $3$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T15:30:44.094Z  

```py
# cook your dish here
for i in range(int(input())):
    n = int(input())
    pos = n
    for j in range(1, n):
        if j % 2 == 1:
            pos -= n - j
        else:
            pos += n - j
    print(pos)
```

---

[View on CodeChef](https://www.codechef.com/problems/ALJMP)