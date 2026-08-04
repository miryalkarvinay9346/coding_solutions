# TEA - Rating 591

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Drinks Tea

Chef has planned that he will drink exactly $X$ liters of tea daily. He has an  **empty**  jar having a capacity of $Y$ liters.

Chef can visit the tea shop to refill the jar. In each refill, the jar is completely filled to the brim and Chef is charged $Z$ rupees.

Chef wonders what is the  **minimum**  amount of money he has to pay for drinking exactly $X$ liters of tea daily.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three space-separated integers $X$, $Y$, and $Z$ denoting the amount of tea Chef has to drink daily, the capacity of his jar and the cost of refilling his jar.
### Output Format

For each test case, output in a single line, the minimum amount Chef has to pay.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq X, Y, Z \leq 100$
### Sample 1:
Input
Output

```
4
3 3 3
6 3 3
5 7 2
9 4 5

```

```
3
6
2
15

```

### Explanation:

 **Test case $1$:**  Chef can get his jar refilled once and drink $3$ liters of tea, which will cost him $3$ rupees in total.

 **Test case $2$:**  Chef needs to refill his jar twice to get $3\cdot 2 = 6$ liters of tea, which will cost him $3\cdot 2 = 6$ rupees in total.

 **Test case $3$:**  Chef can refill his jar once and drink exactly $5$ liters out of the $7$ liters. This will cost him $2$ rupees.

 **Test case $4$:**  Chef can refill his jar twice and drink $4\cdot 2 = 8$ liters of tea. He needs to have one more refill, but this time he would drink only $1$ liter tea from the jar. Thus the total tea he drinks is $4+4+1 = 9$ liters. He made $3$ refills in total costing him $5\cdot 3 = 15$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T17:18:09.508Z  

```py
# cook your dish here
import math
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if  x<=y:
        print(z)
    else:
        k=math.ceil(x/y)
        print(k*z)
```

---

[View on CodeChef](https://www.codechef.com/problems/TEA)