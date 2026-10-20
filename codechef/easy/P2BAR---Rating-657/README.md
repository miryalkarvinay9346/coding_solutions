# P2BAR - Rating 657

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Signal

A secret binary transmission is represented by a string $S$ of length $N$.

In this signal:

- 0 represents a silence period.
- 1 represents a pulse period.

Your task is to determine how many pulses occurred after at least one silence had already appeared in the transmission.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines: The first line contains an integer $N$ — the length of the binary string. The second line contains the binary string $S$.
### Output Format

For each test case, output on a new line the number of pulses occurred after at least one silence had already appeared in the transmission.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10$
- The sum of $N$ over all test cases won't exceed $2\cdot10^4$.
### Sample 1:
Input
Output

```
4
3
011
3
101
3
110
4
1101

```

```
2
1
0
1
```

### Explanation:
- For the first test case, period $1$ is a silence period. Periods $2$ and $3$ are pulse periods which occurred after at least one silence had already appeared in the transmission. Hence answer is $2$.
- For the second test case, period $2$ is a silence period. Period $3$ is a pulse period which occurred after at least one silence had already appeared in the transmission. Hence answer is $1$.
- For the third test case, period $3$ is a silence period. No pulse period passed after that. Hence answer is $0$.
- For the fourth test case, period $3$ is a silence period. Period $4$ is a pulse period which occurred after at least one silence had already appeared in the transmission. Hence answer is $1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T06:01:34.207Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    sil=0
    pu=0
    for i in s:
        if i=="0":
            sil=1
        elif i=="1"and sil==1:
            pu+=1
    print(pu)
```

---

[View on CodeChef](https://www.codechef.com/problems/P2BAR)