# MOVUPSW

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Moving Up

You're given a grid with $2$ rows and $N$ columns. The cell at the intersection of the $i$-th row and $j$-th column is denoted $(i, j)$.

Each cell of the grid contains an integer between $1$ and $N$.
Further, it is guaranteed that each row of the grid contains all of the integers from $1$ to $N$, in some order.
That is, each row of the grid is a permutation of $\{1, 2, \ldots, N\}$.

Consider moving through the grid as follows:

- You initially stand at cell $(1, 1)$.
- Let your current cell be $(i, j)$, and the value in the current cell be $x$. You can then make the following movement: Choose an adjacent cell with value either $x$ or $x+1$, and move to that cell. Here, "an adjacent cell" refers to one among the four cells $(i-1, j), (i+1, j), (i, j-1), (i, j+1)$ - whichever of them are valid cells in the grid.

The grid is called  *good*  if it's possible to perform movements of this type several times, starting from $(1, 1)$, and eventually reach cell $(2, N)$.

You would like to make the grid  *good*. To that end, you can perform the following operation:

- Choose $i$ ($1 \le i \lt N$), and swap the values of the cells $(1, i)$ and $(1, i+1)$. That is, swap the values in the $i$-th and $(i+1)$-th columns of the first row.

Note that the second row remains constant throughout.

Compute the minimum number of adjacent swaps in the first row needed to make the given grid  *good*.
If it's impossible to make the grid  *good*  no matter what, output $-1$ instead.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input. The first line of each test case contains a single integer $N$. The second line contains $N$ space-separated integers $P_1, \ldots, P_N$, denoting the values in the first row of the grid. The third line contains $N$ space-separated integers $Q_1, \ldots, Q_N$, denoting the values in the second row of the grid.
### Output Format

For each test case,

- If it's impossible to make the grid good, output $-1$.
- Otherwise, output the minimum number of adjacent swaps in the first row needed to make the grid good.
### Constraints
- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2\cdot 10^5$
- $P$ and $Q$ are permutations of $[1, N]$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
### Sample 1:
Input
Output

```
4
3
1 3 2
1 2 3
5
2 1 3 5 4
2 1 3 4 5
7
1 3 6 7 5 2 4
6 4 1 2 5 3 7
8
4 8 5 7 3 6 2 1
2 3 1 4 6 8 5 7
```

```
0
1
9
-1
```

### Explanation:

 **Test case $1$:**  The grid is already  *good*, via the sequence of moves $(1, 1) \to (2, 1) \to (2, 2) \to (2, 3)$. No swaps are needed.

 **Test case $2$:**  Swap the first and second elements of the first row, turning it into $[1, 2, 3, 5, 4]$.
After this the grid is good via the sequence $(1, 1) \to (1, 2) \to (1, 3) \to (2, 3) \to (2, 4) \to (2, 5)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-22T16:02:32.286Z  

```py
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/MOVUPSW)