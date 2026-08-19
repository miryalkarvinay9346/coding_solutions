# ODDEVEN7

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Odd Even

An array $B$ is called good if the parity of the elements keep alternating, i.e. odd, even, odd,.... or even, odd, even,...

You are given an array $A$ containing $N$ integers, and you can do the following action:

- Choose some subset of elements of $A$, and then rearrange that subset to form a good array.

Find the maximum size of subset you can choose which can be rearranged to a good array.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the maximum size of a subset.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
2
5
1 3 7 4 5
4
1 1 2 4

```

```
3
4
```

### Explanation:

 **Test Case 1:**  We can choose the subset $\{1, 4, 5\}$. There is no need to reorder it, as it is already alternating.

 **Test Case 2:**  We can choose the subset $\{1, 1, 2, 4\}$ and reorder to get $[1, 2, 1, 4]$ which is alternating parity.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T15:45:35.953Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    oc=0
    ec=0
    for i in a:
        if i%2==0:
            ec=0
        else:
            ec=0
    if oc==ec:
        print(n)
    else:
        if oc%2!=0:
            print(oc+2)
        elif ev%2==0:
            print(ec+2)
```

---

[View on CodeChef](https://www.codechef.com/problems/ODDEVEN7)