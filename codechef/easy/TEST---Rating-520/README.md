# TEST - Rating 520

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Life, the Universe, and Everything

 **For help on this problem, please check out our tutorial**  Input and Output (I/O)

Your program is to use the brute-force approach in order to  *find the Answer to Life, the Universe, and Everything.*  More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number $42$. All numbers at input are integers of one or two digits.

### Sample 1:
Input
Output

```
1
2
88
42
99
```

```
1
2
88
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T05:27:37.318Z  

```py
# cook your dish here
while True:
    n=int(input())
    if n==42:
        break
    print(n)
```

---

[View on CodeChef](https://www.codechef.com/problems/TEST)