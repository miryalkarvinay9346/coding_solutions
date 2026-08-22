# DSAPROB20

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com

You are given two arrays of positive integers, $arr1$ and $arr2$, of sizes $n$ and $m$ respectively. Your task is to find the largest common element that appears in both arrays. If no common element exists, return $-1$.

### Constraints
- $1 \leq n, m \leq 10^5$
- $0 \leq arr1[i], arr2[i] \leq 10^9$
### Sample 1:
Input
Output

```
5 6
1 3 4 6 7
2 3 5 6 7 8
```

```
7
```

### Explanation:

In the given arrays, the common elements are 3, 6, and 7. The largest common element is 7.

### Sample 2:
Input
Output

```
4 3
1 2 3 4
5 6 7
```

```
-1
```

### Explanation:

In the given arrays, there are no common elements. Therefore, the output is -1.

### Sample 3:
Input
Output

```
4 4
9 2 1 10
3 11 9 2
```

```
9
```

### Explanation:

The common elements are 2,9. The largest one is 9.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T13:14:25.905Z  

```py
def largestCommonElement(arr1, arr2):
    # Write your code here
    arr1.sort(reverse=True)
    #arr2.sort(reverse=True)
    #n,m=len(arr1),len(arr2)
    #k=min(n,m)
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            return (arr1[i])
    return -1       
```

---

[View on CodeChef](https://www.codechef.com/problems/DSAPROB20)