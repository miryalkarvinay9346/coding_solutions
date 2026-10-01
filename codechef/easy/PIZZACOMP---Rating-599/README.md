# PIZZACOMP - Rating 599

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Pizza Comparision

Chef makes $2$ types of (square) pizzas:

- A small pizza, with length $10$ inches, costing $A$ rupees.
- A large pizza, with length $15$ inches, costing $B$ rupees.

His customers are wondering which pizza is more optimal to buy if they want to maximize the amount of pizza received per rupee spent. For comparing, we will assume the amount of pizza to be it's area.

Output $\text{'Small'}$ if the small pizza has more amount per rupee spent, $\text{'Large'}$ if the large pizza has more, and $\text{'Equal'}$ otherwise (without the quotes).

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $2$ integers - $A$ and $B$.
### Output Format

For each test case, output on a new line $\text{Small}$, $\text{Large}$ or $\text{Equal}$ as specified.

### Constraints
- $1 \le T \le 100$
- $100 \le A \lt B \le 400$
### Sample 1:
Input
Output

```
7
100 400
200 201
100 225
101 225
177 400
178 400
176 396

```

```
Small
Large
Equal
Large
Small
Large
Equal

```

### Explanation:

 **Test Case 1**  : The small pizza has an area of $100$, and costs $100$, thus a cost of $1$ rupee per unit area, while the large pizza costs $\frac{400}{225}$ per unit area. Hence, the small pizza is more optimal.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T13:02:34.827Z  

```py
for _ in range(int(input())):
    A, B = map(int, input().split())
    # Compare 100/A and 225/B using cross-multiplication
    small_value = 100 * B
    large_value = 225 * A
    
    if small_value > large_value:
        print("Small")
    elif small_value < large_value:
        print("Large")
    else:
        print("Equal")
```

---

[View on CodeChef](https://www.codechef.com/problems/PIZZACOMP)