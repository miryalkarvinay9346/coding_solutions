# Height Checker

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in  **non-decreasing order**  by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the  **current order**  that the students are standing in. Each `heights[i]` is the height of the `ith` student in line (**0-indexed**).

Return  *the  **number of indices**  where* `heights[i] != expected[i]`.

 

 **Example 1:** 

```
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

```

 **Example 2:** 

```
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

```

 **Example 3:** 

```
Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

```

 

 **Constraints:** 

- 1 <= heights.length <= 100
- 1 <= heights[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 6.16%)  
**Memory:** 19.3 MB (beats 53.70%)  
**Submitted:** 2026-09-14T10:06:16.609Z  

```py
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=[0]*len(heights)
        for i in range(len(heights)):
            a[i] = heights[i]
        for i in range(len(heights)):
            j=i
            while(j>0 and a[j-1] >a[j]):
                temp=a[j-1]
                a[j-1]= a[j]
                a[j] = temp
                j-=1
        c=0
        for i in range(len(a)):
            if(a[i] != heights[i]):
                c+=1
        return c
```

---

[View on LeetCode](https://leetcode.com/problems/height-checker/)