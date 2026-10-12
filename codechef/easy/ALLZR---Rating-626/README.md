# ALLZR - Rating 626

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### All Zero

There is a blackboard with three integers written on it: $A, B,$ and $C$.

You can modify these integers with the following two types of operations:

- Type $1$: Subtract $1$ from $A$ and subtract $2$ from $B$.
- Type $2$: Subtract $1$ from $B$ and subtract $3$ from $C$.

Each type of operation can be performed however many times you like.
The operations can be performed in any order.

Is it possible to perform the operations in such a way that all three of $A,B,$ and $C$ become $0$  **simultaneously** ?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing three space-separated integers $A, B, C$.
### Output Format

For each test case, output on a new line a string denoting the answer: `Yes` if all three integers can be made $0$, and `No` otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e. the strings `NO`, `No`, `nO`, and `no` will all be treated as equivalent.

### Constraints
- $1 \leq T \leq 8000$
- $1 \le A, B, C \le 20$
### Sample 1:
Input
Output

```
4
3 7 3
3 2 6
1 3 3
2 5 4

```

```
Yes
No
Yes
No
```

### Explanation:

 **Test case $1$:**  One sequence of operations is as follows:

- Initially, $(A, B, C) = (3, 7, 3)$.
- Perform a type $1$ operation. Now, $(A, B, C) = (2, 5, 3)$.
- Perform a type $1$ operation again. Now, $(A, B, C) = (1, 3, 3)$.
- Next, perform a type $2$ operation. Now, $(A, B, C) = (1, 2, 0)$.
- Finally, perform a type $1$ operation. Now, $(A, B, C) = (0, 0, 0)$ as we desired.

 **Test case $2$:**  It can be shown that no matter what we do, at least one of $A, B, C$ will be non-zero always.
For instance, if we perform an operation of type $1$ three times, $A$ will become $0$, but $B$ will become $2 - 3\cdot 2 = -4$; and since it's negative it can never become $0$ after that.

 **Test case $3$:**  We have $(A, B, C) = (1, 3, 3)$. Getting from here to $(0, 0, 0)$ is already covered in the explanation for sample test case $1$ (see the last two steps).

 **Test case $4$:**  It can be shown that no matter what we do, $C$ can never become $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T11:52:59.896Z  

```py
# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if c%3==0 and b==2*a+c//3:
        print("Yes")
    else:
        print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/ALLZR)