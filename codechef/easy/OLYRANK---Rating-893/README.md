# OLYRANK - Rating 893

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Olympics Ranking

In Olympics, the countries are ranked by the  **total number of medals won**. You are given six integers $G_1$, $S_1$, $B_1$, and $G_2$, $S_2$, $B_2$, the number of gold, silver and bronze medals won by two different countries respectively. Determine which country is ranked better on the leaderboard. It is guaranteed that there will not be a tie between the two countries.

### Input Format
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains six space-separated integers $G_1$, $S_1$, $B_1$, and $G_2$, $S_2$, $B_2$.
### Output Format

For each test case, print `"1"` if the first country is ranked better or `"2"` otherwise. Output the answer without quotes.

### Constraints
- $1 \leq T \leq 1000$
- $0 \leq G_1, S_1, B_1, G_2, S_2, B_2 \leq 30$
### Subtasks

 **Subtask #1 (100 points):**  Original constraints

### Sample 1:
Input
Output

```
3
10 20 30 0 29 30
0 0 0 0 0 1
1 1 1 0 0 0

```

```
1
2
1
```

### Explanation:

 **Test case $1$:**  Total medals for the first country are $10 + 20 + 30 = 60$ and that for the second country are $0 + 29 + 30 = 59$. So the first country is ranked better than the second country.

 **Test case $2$:**  Total medals for the first country are $0 + 0 + 0 = 0$ and that for the second country are $0 + 0 + 1 = 1$. So the second country is ranked better than the first country.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T17:33:57.298Z  

```py
# cook your dish here
for _ in range(int(input())):
    g1,s1,b1,g2,s2,b2=map(int,input().split())
    print(1 if g1+s1+b1>g2+s2+b2 else 2)
```

---

[View on CodeChef](https://www.codechef.com/problems/OLYRANK)