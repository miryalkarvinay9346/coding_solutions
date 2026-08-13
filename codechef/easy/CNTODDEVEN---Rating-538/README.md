# CNTODDEVEN - Rating 538

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Count Odd Even Divisors

You have an integer $N$, and you want to calculate the number of odd divisors of $N$, and the number of even divisors of $N$.

For example, $2$ has $1$ odd divisor (which is $1$), and $1$ even divisor (which is $2$). $8$ has $1$ odd divisor (which is $1$) and $3$ even divisors (which are $2, 4, 8$).

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of input contains a single integer $N$.
### Output Format

For each test case, output on a new line $2$ integers - first, the number of odd divisors of $N$, and second, the number of even divisors of $N$.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
### Sample 1:
Input
Output

```
5
1
2
3
4
8

```

```
1 0
1 1
2 0
1 2
1 3
```

### Explanation:

 **Test Case 1**  : $1$ has only $1$ divisor, which is odd.

 **Test Case 2**  : Explained in statement.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T16:38:25.243Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    o=0
    e=0
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                e+=1
            else:
                o+=1
    print(o,e)
```

---

[View on CodeChef](https://www.codechef.com/problems/CNTODDEVEN)