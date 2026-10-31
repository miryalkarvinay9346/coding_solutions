# PROFIT - Rating 607

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Profits

Chef is running a lemonade stand, and each lemonade costs him Rs. $X$ to make.

Chef will have $N$ total customers coming to his lemonade stand today, with the $i$-th customer willing to spend Rs. $i$ on a lemonade.
So, the first customer is willing to spend Rs. $1$, the second Rs. $2$, the third Rs. $3$ and so on.

For each customer, Chef can choose whether to accept and provide him with lemonade (at the amount he is willing to pay), or reject him. Find the maximum profit Chef can make. Ignore any other costs.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $2$ integers - $N$ and $X$.
### Output Format

For each test case, output on a new line the maximum profit Chef can make.

### Constraints
- $1 \le T \le 100$
- $1 \le N, X \le 100$
### Sample 1:
Input
Output

```
3
5 2
5 4
5 6

```

```
6
1
0
```

### Explanation:

 **Test case $1$** : Chef chooses to accept the second, third, fourth and fifth customers. His total cost of making the lemonade would be $2 \cdot 4 = 8$, and he gets $2 + 3 + 4 + 5 = 14$ for a profit of $14-8=6$.

 **Test case $2$** : Chef only accepts the fifth customer.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T06:36:15.572Z  

```py
# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    p=0
    for i in range(1,n+1):
        if i>x:
            p+=i-x
    print(p)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/PROFIT)