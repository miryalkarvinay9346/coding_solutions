# CS2023_GYM - Rating 629

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Gymkhana Election IIIT-A

In the Gymkhana elections of IIIT-A, $N$ members are nominated for senator positions. The total number of voters in the college is $M$.

Om, one of the $N$ nominees, wants to secure a  *strict majority win*  in the election.

Assuming all voters cast their votes, find the  **minimum**  number of votes Om requires to ensure a  *strict majority win*.

Note that in a  *strict majority win*, all the nominees have strictly lesser votes than the winner.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $M$ — the number of nominated members and the number of voters respectively.
### Output Format

For each test case, output the  **minimum**  number of votes Om requires to ensure a strict majority win.

### Constraints
- $1 \leq T \leq 10^{5}$
- $2 \leq N \leq M \leq 10^{9}$
### Sample 1:
Input
Output

```
2
5 12 
4 5 
```

```
7
3
```

### Explanation:

 **Test case $1$:**  Om has to get a minimum of $7$ votes to ensure a strict majority win. If he gets $7$ votes, it is not possible for any other nominee to get at least $7$ votes.

 **Test case $2$:**  Om has to get a minimum of $3$ votes to ensure a strict majority win. If he gets $3$ votes, it is not possible for any other nominee to get at least $3$ votes.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T13:22:23.173Z  

```py
# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    print((m//2)+1)
```

---

[View on CodeChef](https://www.codechef.com/problems/CS2023_GYM)