# HARDBET - Rating 803

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Hardest Problem Bet

There are $3$ problems in a contest namely $A, B, C$ respectively. Alice bets Bob that problem $C$ is the hardest while Bob says that problem $B$ will be the hardest.

You are given three integers $S_A, S_B, S_C$ which denotes the number of successful submissions of the problems $A, B, C$ respectively. It is guaranteed that each problem has a different number of submissions. Determine who wins the bet.

- If Alice wins the bet (i.e. problem $C$ is the hardest), then output $Alice$.
- If Bob wins the bet (i.e. problem $B$ is the hardest), then output $Bob$.
- If no one wins the bet (i.e. problem $A$ is the hardest), then output $Draw$.

 **Note** : The hardest problem is the problem with the least number of successful submissions.

### Input Format
- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $S_A, S_B, S_C$, denoting the number of successful submissions of problems $A, B, C$ respectively.
### Output Format

For each test case, output the winner of the bet or print Draw in case no one wins the bet.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq S_A,S_B,S_C \leq 100$
- $S_A, S_B, S_C$ are all distinct.
### Sample 1:
Input
Output

```
3
1 4 2
16 8 10
14 15 9

```

```
Draw
Bob
Alice

```

### Explanation:

 **Test case $1$:**  Problem $A$ turns out to be the hardest so no one wins the bet.

 **Test case $2$:**  Problem $B$ turns out to be the hardest so Bob wins the bet.

 **Test case $3$:**  Problem $C$ turns out to be the hardest so Alice wins the bet.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T17:06:09.907Z  

```py
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if c<a and c<b:
        print("Alice")
    elif b<c and b<a:
        print("Bob")
    else:
        print("Draw")
```

---

[View on CodeChef](https://www.codechef.com/problems/HARDBET)