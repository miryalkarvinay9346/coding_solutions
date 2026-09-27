# PBREV - Rating 643

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Problem Reviews

Om Khangat has come up with a problem that he thinks can be used in a CodeChef contest, and has submitted his proposal for review.

CodeChef's review panel has $N$ judges, each of whom will give Om's problem a point value between $1$ and $10$, denoting how good they think it is ($1$ being the lowest, and $10$ the highest).
A problem is considered  *good*  if and only if  **every judge**  gives it a score that's  *strictly greater than*  $4$.

You know the point values given by each judge to Om's problem. Can you tell whether his problem is  *good* ?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains one integer $N$ — the number of judges. The next line contains $N$ space-separated integers $S_1,S_{2},S_{3},\ldots,S_{N}$ — where $S_i$ denotes the score given to Om's problem by the $i$-th judge.
### Output Format

For each test case, print the answer on a new line: `YES` if Om's problem is  *good*, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `YES`, `yes`, `YeS`, and `yES` will all be treated as equivalent.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq S_i \leq 10$
- The sum of $N$ across all tests won't exceed $2000$.
### Sample 1:
Input
Output

```
3
4
3 5 6 9
3
8 7 8
4
10 9 10 4

```

```
NO
YES
NO

```

### Explanation:

 **Test case $1$:**  We have $S = [3, 5, 6, 9]$. The first judge gave a score of $3$, which isn't strictly greater than $4$. So, Om's problem is not  *good*.

 **Test case $2$:**  We have $S = [8, 7, 8]$. All the judges gave scores that are strictly greater than $4$, so Om's problem is  *good*.

 **Test case $3$:**  We have $S = [10, 9, 10, 4]$. The last judge gave a score of $4$, which isn't strictly greater than $4$. So, Om's problem is not  *good*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T08:53:34.290Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=map(int,input().split())
    count=0
    for i in s:
        if(i<=4):
            count+=1
    if(count==0):
        print("yes")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/PBREV)