# DIGARR - Rating 949

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Rearranging digits to get a multiple of 5

Given a positive integer $N$, MoEngage wants you to determine if it is possible to rearrange the digits of $N$ (in decimal representation) and obtain a multiple of $5$.

For example, when $N = 108$, we can rearrange its digits to construct $180 = 36 \cdot 5$ which is a multiple of $5$.

### Input Format
- The first line contains an integer $T$, the number of test cases. The description of the $T$ test cases follow.
- Each test case consists of two lines
- The first line contains a single integer $D$, the number of digits in $N$.
- The second line consists of a string of length $D$, the number $N$ (in decimal representation). It is guaranteed that the string does not contain leading zeroes and consists only of the characters $0, 1, \dots 9$.
### Output Format
- For each test case, print $\texttt{Yes}$ if it is possible to rearrange the digits of $N$ so that it becomes a multiple $5$. Otherwise, print $\texttt{No}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq D \leq 1000$
- $1 \leq N \lt 10^{1000}$
- Sum of $D$ over all test cases $\leq 1000$.
### Sample 1:
Input
Output

```
3
3
115
3
103
3
119
```

```
Yes
Yes
No
```

### Explanation:

 **Test Case $1$:**  The given number is already divisible by $5$, therefore the answer is $\texttt{Yes}$.

 **Test Case 2:**  We can obtain $310 = 62 \cdot 5$ by rearranging the digits of $103$, so the answer is $\texttt{Yes}$.

 **Test Case 3:**  The only numbers that can be obtained by rearranging the digits of $119$ are $\{119, 191, 911\}$. None of these numbers are multiples of $5$, so the answer is $\texttt{No}$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-25T13:15:35.272Z  

```py
# cook your dish here
for  _ in range(int(input())):
    d=map(int,input().split())
    n=input()
    print("yes" if ('0' in n) or('5' in n) else "no" )
    
```

---

[View on CodeChef](https://www.codechef.com/problems/DIGARR)