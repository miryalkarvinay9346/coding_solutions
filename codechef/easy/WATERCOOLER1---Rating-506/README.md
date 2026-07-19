# WATERCOOLER1 - Rating 506

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### The Cooler Dilemma 1

Summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

- Rent a cooler at the cost of $X$ coins per month.
- Purchase a cooler for $Y$ coins.

Given that the summer season will last for $M$ months in Chefland, help Chef in finding whether he should rent the cooler or not.

Chef rents the cooler only if the cost of renting the cooler is  **strictly less**  than the cost of purchasing it. Otherwise, he purchases the cooler.

Print $\texttt{YES}$ if Chef should  **rent the cooler**, otherwise print $\texttt{NO}$.

### Input Format
- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three integers $X$, $Y$ and $M$, as described in the problem statement.
### Output Format

For each test case, output $\texttt{YES}$ if Chef should rent the cooler, otherwise output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, M \leq 10^4$
- $1 \leq Y \leq 10^8$
### Sample 1:
Input
Output

```
3
5 10 1
5 10 2
5 10 3
```

```
YES
NO
NO
```

### Explanation:

 **Test case $1$** : Cost of renting the cooler $= 5$ coins. Cost of purchasing the cooler $= 10$ coins. So, Chef should rent the cooler as the cost of renting the cooler for $1$ month is strictly less than purchasing it.

 **Test case $2$** : Cost of renting the cooler $= 10$ coins. Cost of purchasing the cooler $= 10$ coins. So, Chef should not rent the cooler as the cost of renting the cooler for $2$ months is not strictly less than purchasing it.

 **Test case $3$** : Cost of renting the cooler $= 15$ coins. Cost of purchasing the cooler $= 10$ coins. So, Chef should not rent the cooler as the cost of renting the cooler for $3$ months is not strictly less than purchasing it.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-19T08:35:15.125Z  

```py
# cook your dish here
for _ in range(int(input())):
    x,y,m=map(int,input().split())
    print("YES" if x*m<y else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/WATERCOOLER1)