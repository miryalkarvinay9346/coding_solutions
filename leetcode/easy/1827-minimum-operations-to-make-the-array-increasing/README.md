# Minimum Operations to Make the Array Increasing

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` (**0-indexed**). In one operation, you can choose an element of the array and increment it by `1`.

- For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].

Return  *the  **minimum**  number of operations needed to make*  `nums`  ***strictly**   **increasing**.*

An array `nums` is  **strictly increasing**  if `nums[i] < nums[i+1]` for all `0 <= i < nums.length - 1`. An array of length `1` is trivially strictly increasing.

 

 **Example 1:** 

```
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

```

 **Example 2:** 

```
Input: nums = [1,5,2,4,1]
Output: 14

```

 **Example 3:** 

```
Input: nums = [8]
Output: 0

```

 

 **Constraints:** 

- 1 <= nums.length <= 5000
- 1 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 108 ms (beats 51.62%)  
**Memory:** 19.6 MB (beats 98.59%)  
**Submitted:** 2026-10-21T05:16:33.096Z  

```py
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                n=nums[i-1]+1
                c+=n-nums[i]
                nums[i]=n
        return c

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/)