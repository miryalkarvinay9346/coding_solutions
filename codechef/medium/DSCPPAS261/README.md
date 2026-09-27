# DSCPPAS261

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Intersecting arrays

Given two integer arrays $nums1$ and $nums2$, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and return the result in  **sorted order**.

Intersection is defined as the common element in both arrays. For example -

$nums1$ - [1, 2] and $nums2$ - [2, 1, 3]

Therefore, only 1 and 2 are common in both arrays. On sorting the resultant array would be [1, 2].

### Input Format
- The first line contains two integers $n$, $m$— the size of $nums1$ and $nums2$.
- The second line contains n integers $a1,a2,…,an$ — the number of $nums1$.
- The third line contains m integers $b1,b2,…,bm$ — the number of $nums2$.
### Output Format

Print all the elements that are appearing in both the arrays in sorted order.

### Constraints
- $1 \leq n,m \leq 100$
- $0 \leq ai \leq 100$
- $0 \leq bi \leq 100$
### Sample 1:
Input
Output

```
2 3
1 2
2 1 3
```

```
1 2
```

### Explanation:

The common elements in both arrays are 1,2. so their intersection is 1,2.

### Sample 2:
Input
Output

```
3 3
1 2 3
3 4 6
```

```
3
```

### Explanation:

Only 3 is present as the common element in both arrays.

### Sample 3:
Input
Output

```
3 3
1 1 2
1 3 1
```

```
1 1
```

### Explanation:

There are 2 1's present in both of the arrays so the answer is `1 1`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T09:47:27.181Z  

```py
class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        result=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return result

```

---

[View on CodeChef](https://www.codechef.com/problems/DSCPPAS261)