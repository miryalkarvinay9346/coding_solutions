# PERFECTTRIO - Rating 455

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Perfect Trio

Chef defines a group of three friends as a  *perfect*  group if the age of one person is equal to the  **sum**  of the age of remaining two people.

Given that, the ages of three people in a group are $A, B,$ and $C$ respectively, find whether the group is  *perfect*.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $A, B,$ and $C$ — the age of the three members of group.
### Output Format

For each test case, output on a new line, `YES`, if the group is perfect, and `NO` otherwise.

You may print each character in uppercase or lowercase. For example, the strings `YES`, `yes`, `Yes`, and `yES` are considered identical.

### Constraints
- $1 \leq T \leq 200$
- $1 \leq A, B, C \leq 100$
### Sample 1:
Input
Output

```
4
10 20 30
23 51 17
44 21 23
30 30 30

```

```
YES
NO
YES
NO

```

### Explanation:

 **Test case $1$:**  The sum of age of first and second person is equal to that of the third person. Thus, the group is  *perfect*.

 **Test case $2$:**  There exists no member in the group such that the age of one person is equal to the sum of the age of remaining two people. Thus, the group is not  *perfect*.

 **Test case $3$:**  The sum of age of second and third person is equal to that of the first person. Thus, the group is  *perfect*.

 **Test case $4$:**  There exists no member in the group such that the age of one person is equal to the sum of the age of remaining two people. Thus, the group is not  *perfect*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-18T04:28:42.712Z  

```py
# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b==c or b+c==a or c+a==b:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/PERFECTTRIO)