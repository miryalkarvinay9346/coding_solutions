# PASSINGGR - Rating 629

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Passing Grade

Chef is in a class in his university with a total of $N$ students (including him). Chef's professor likes Chef but hates the entire class.

Chef's professor has just finished grading their exam papers, and it is known that the $i$-th student has scored $A_i$ marks. Chef is student number $1$, and the other students are numbered from $2$ to $N$.

Chef's professor cannot change the marks the students received, but he can decide the cutoff marks. He wants to ensure Chef passes, but at the same time, fail as many other students as possible. Formally, he will choose some cutoff marks $X (0 \le X \le 100)$ and then fail all students with marks strictly less than $X$, and pass those with $\ge X$.

Find the number of students that passes that class, when Chef's professor chooses in the cutoff in the optimal way (minimizing the number of students that pass, but ensuring Chef passes).

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$, the marks each student got.
### Output Format

For each test case, output on a new line the minimum number of students that pass the class.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $0 \le A_i \le 100$
### Sample 1:
Input
Output

```
3
3
100 59 98
4
0 100 0 100
7
54 23 67 85 34 54 53

```

```
1
4
4

```

### Explanation:

 **Test Case 1**  : Chef's professor can set the cutoff marks to $99$, and then only Chef passes.

 **Test Case 2**  : Chef's professor must set the cutoff marks to $0$ to ensure Chef passes, and then everybody else will also pass.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T18:46:24.911Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p=a[0]
    c=0
    for i in a:
        if i>=p:
            c+=1
    print(c)
```

---

[View on CodeChef](https://www.codechef.com/problems/PASSINGGR)