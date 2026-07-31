# PHONEYR - Rating 541

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Yearly Phone

Chef is interested by buying a new phone, and is in the process of researching what's available on the market.

His favorite brand, Kitchen Telecom, just released their latest model.
Kitchen Telecom releases a new phone every year, and so names its phones based upon the year of release: the name of the phone model launched in year $X$ is $\texttt{K}$ (the letter) followed by the last two digits of $X$.
For instance, the phone model launched in the year $2024$ is named $\texttt{K24}$.

The current year is $X$. What's the latest phone model launched by Kitchen Telecom?

### Input Format
- The first and only line of input contains a single integer $X$, the current year.
### Output Format

Print the name of Kitchen Telecom's phone launched in year $X$.

### Constraints
- $1973 \leq X \leq 2024$
### Sample 1:
Input
Output

```
2000

```

```
K00

```

### Sample 2:
Input
Output

```
2024
```

```
K24
```

### Explanation:

 **Sample $1$:**  The last two digits of $2000$ are $00$, so the answer is `K00`.
Note that any zeros are printed as-is, and are not ignored.

 **Sample $2$:**  The last two digits of $2024$ are $24$, so the answer is `K24`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T18:50:51.290Z  

```py
# cook your dish here
x=input()
print("k"+str(x)[-2]+str(x)[-1])
```

---

[View on CodeChef](https://www.codechef.com/problems/PHONEYR)