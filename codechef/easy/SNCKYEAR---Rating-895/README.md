# SNCKYEAR - Rating 895

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and SnackDown

Chef is interested in the history of SnackDown contests. He needs a program to verify if SnackDown was hosted in a given year.

SnackDown was hosted by CodeChef in the following years: 2010, 2015, 2016, 2017 and 2019.

### Input Format

The first line contain the number of test-cases $T$.

The first line of each test-case contains a single integer $N$.

### Output Format

For each test case print a single line containing the string `"HOSTED"` if SnackDown was hosted in year $N$ or `"NOT HOSTED"` otherwise (without quotes).

### Constraints
- $1 \le T \le 10$
- $2010 \le N \le 2019$
### Sample 1:
Input
Output

```
2
2019
2018
```

```
HOSTED
NOT HOSTED
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T08:23:47.196Z  

```py
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n==2010 or n==2015 or n==2016 or n==2017 or n==2019:
        print("HOSTED")
    else:
        print("NOT HOSTED")
```

---

[View on CodeChef](https://www.codechef.com/problems/SNCKYEAR)