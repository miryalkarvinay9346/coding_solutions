# Find Lucky Integer in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `arr`, a  **lucky integer**  is an integer that has a frequency in the array equal to its value.

Return  *the largest  **lucky integer**  in the array*. If there is no  **lucky integer**  return `-1`.

 

 **Example 1:** 

```
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

```

 **Example 2:** 

```
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

```

 **Example 3:** 

```
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

```

 

 **Constraints:** 

- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500

## Solution

**Language:** Python  
**Runtime:** 179 ms (beats 5.56%)  
**Memory:** 19.3 MB (beats 29.61%)  
**Submitted:** 2026-07-25T12:35:39.524Z  

```py
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=-1
        for i in range(len(arr)):
            c=0
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    c+=1
            if c==arr[i]:
                l=max(l,arr[i])
        return l
```

---

[View on LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)