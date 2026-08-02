# LITRATE - Rating 512

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Literacy Rate

You are given two positive integers $P$ and $L$ denoting the total population of Chefland and the total number of literate people in Chefland.

Find whether the literacy rate of Chefland is  **greater than or equal to**  $75 \%$.

Note that the literacy rate is calculated as $\frac {L}{P} \times 100 \%$

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $P$ and $L$ — the total population and the total number of literate people in Chefland respectively.
### Output Format

For each test case, output on a new line, `YES`, if the literacy rate of Chefland is  **greater than or equal to**  $75 \%$. Otherwise, output `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 6000$
- $1 \leq L \leq P \leq 100$
### Sample 1:
Input
Output

```
4
100 75
20 5
53 51
50 10

```

```
YES
NO
YES
NO

```

### Explanation:

 **Test case $1$:**  The literacy rate is exactly $75 \%$ which is greater than equal to $75 \%$.

 **Test case $2$:**  The literacy rate is $25 \%$ which is less than $75 \%$.

 **Test case $3$:**  The literacy rate is greater than $75 \%$.

 **Test case $4$:**  The literacy rate is $20 \%$ which is less than $75 \%$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-02T03:06:14.002Z  

```py
# cook your dish here
for _ in range(int(input())):
    p,l=map(int,input().split())
    print("YES" if (l/p)*100>=75 else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/LITRATE)