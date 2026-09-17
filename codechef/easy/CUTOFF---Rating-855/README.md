# CUTOFF - Rating 855

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Passing Marks

In a class of $N$ students, a class test was held. The $i^{th}$ student scored $A_i$ marks. It is also known that the scores of all students were  **distinct**.

A student passes the test if their score is  **strictly greater**  than the passing mark. Given that exactly $X$ students pass in the test, find the  **maximum**  value of the passing mark of the test.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains two space-separated integers $N$ and $X$ — the number of students in the class and the number of students that passed in the test. The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$, where the $i^{th}$ integer denotes the marks of the $i^{th}$ student.
### Output Format

For each test case, output on a new line, the  **maximum**  value of the passing mark of the test.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq X \leq N$
- $1 \leq A_i \leq 100$
- All elements of array $A$ are distinct.
### Sample 1:
Input
Output

```
3
2 2
5 1
4 1
5 1 7 4
4 3
15 70 100 31

```

```
0
6
30

```

### Explanation:

 **Test case $1$:**  Since both students pass the test, both students scored greater than passing marks. The maximum value of passing marks can be $0$, as both students have marks greater than $0$.

 **Test case $2$:**  Only one student passes the test. Thus, the third student has passed the test by scoring $7$ marks. The passing marks of the test is $6$.

 **Test case $3$:**  Since three students pass the test, students $2, 3,$ and $4$ scored greater than passing marks. The maximum value of passing marks can be $30$, three students have marks greater than $30$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T13:35:58.021Z  

```py
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # your code goes here
    a.sort(reverse=True)
    k=min(a[:x])
    print(k-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/CUTOFF)