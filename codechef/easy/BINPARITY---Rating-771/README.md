# BINPARITY - Rating 771

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Binary Parity

The  *binary parity*  of an integer $N$ is defined as follows:

- First, write $N$ in binary. For example, $N = 13$ is written as $\texttt{1101}$ in binary, and $N = 5$ is written as $\texttt{101}$.
- Compute $S_N$, the sum of the binary digits of $N$. For example, from the earlier examples, $S_{13} = 1+1+0+1 = 3$ and $S_{5} = 1+0+1 = 2$.
- The binary parity of $N$ is then the parity$^\dagger$ of $S_N$. $S_{13} = 3$ is odd, so $13$ is said to have odd binary parity; while $S_6 = 2$ is even, so $5$ has even binary parity.

Given an integer $N$, find its binary parity.

$^\dagger$ The parity of an integer is, quite simply, whether it's even or odd.
We say an integer has even parity if it is a multiple of $2$, and odd parity otherwise.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case will contain a single integer $N$.
### Output Format

For each test case, output on a new line the binary parity of $N$ — either `"EVEN"` or `"ODD"` (without quotes).

Each character of the output may be printed in either lowercase or uppercase, i.e, the strings `Odd`, `ODD`, `oDd`, and `ODd` will all be treated as equivalent.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
### Sample 1:
Input
Output

```
2
3
4
```

```
EVEN
ODD
```

### Explanation:

 **Test case $1$** : $N = 3$ is written as $\texttt{11}$ in binary.
This gives us $S_3 = 1+1 = 2$, which is even - so the binary parity of $3$ is even.

 **Test case $2$** : $N = 4$ is written as $\texttt{100}$ in binary.
This gives us $S_4 = 1+0+0 = 1$, which is odd - so the binary parity of $4$ is odd.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T09:18:41.169Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=str(bin(n))[2:]
    print("EVEN" if a.count("1")%2==0 else "ODD")
```

---

[View on CodeChef](https://www.codechef.com/problems/BINPARITY)