# BANKGLITCH - Rating 649

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Bank Glitch

In Chefland, there are $2$ currencies in use, currency $1$ and currency $2$. Normally, one unit of currency $1$ is worth exactly $1$ unit of currency $2$.

Chef currently has $A$ units of currency $1$, and $B$ units of currency $2$.

However, he has found a glitch in the banking system, which allows him to trade $X$ units of currency $1$ for $Y$ units of currency $2$, where $X < Y$, so this is a positive trade for him to make
Chef may make this trade multiple times, however it has to be exactly $X$ units for $Y$ units and not just smaller parts in the same ratio - for example, if $X = 3$ and $Y = 6$ it is  *not*  allowed to exchange $2$ units of currency $1$ for $4$ units of currency $2$.

What is the maximum amount of money Chef can end up with? The amount of money being measured as the sum of currency $1$ and $2$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line contains $4$ integers - $A$, $B$, $X$ and $Y$.
### Output Format

For each test case, output on a new line the maximum amount of money Chef can end up with.

### Constraints
- $1 \le T \le 100$
- $1 \le A, B \le 100$
- $1 \le X \lt Y \le 100$
### Sample 1:
Input
Output

```
3
5 2 4 10
5 2 6 10
4 4 1 2

```

```
13
7
12
```

### Explanation:

 **Test Case 1**  : Chef can make the trade once, trading $6$ units of currency $1$ for $10$ units of currency $2$. He ends up with $1$ unit of currency $1$, and $12$ units of currency $2$ for a total of $13$.

 **Test Case 2**  : Chef is unable to make any trades.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T16:43:53.981Z  

```py
# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    """
    while a>=x:
        a-=x
        b+=y
    print(a+b)
    """
    trades = a // x# Calculate the maximum number of possible trades
    # Each trade increases the total money by (y - x)
    answer = a+ b + trades * (y-x)
    print(answer)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/BANKGLITCH)