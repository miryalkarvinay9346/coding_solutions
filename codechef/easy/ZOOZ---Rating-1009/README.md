# ZOOZ - Rating 1009

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Zero Ones Equal One Zeros

Kulyash believes in equality.
Given an integer $N$, output a binary string of length $N$ such that:

- The count of $01$ subsequences in the string is equal to the count of $10$ subsequences;
- The string has at least one occurrence of $0$ as well as $1$.

If multiple such strings exist, print any. Also, it is guaranteed that corresponding to the given input, an answer always exists.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, an integer $N$ - the length of the binary string.
### Output Format

For each test case, output any binary string of length $N$ satisfying the given conditions.

### Constraints
- $1 \leq T \leq 100$
- $3 \leq N \leq 1000$
### Subtasks
### Sample 1:
Input
Output

```
2
4
3

```

```
1001
010

```

### Explanation:

 **Test case $1$:**  A binary string satisfying both the conditions is $1001$. The count of $01$ as well as $10$ subsequences in the string is $2$.

 **Test case $2$:**  A binary string satisfying both the conditions is $010$. The count of $01$ as well as $10$ subsequences in the string is $1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T13:11:17.609Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    #print(bin(n)[2:].zfill(n))
    print('1'+((n-2)*'0')+'1')

```

---

[View on CodeChef](https://www.codechef.com/problems/ZOOZ)