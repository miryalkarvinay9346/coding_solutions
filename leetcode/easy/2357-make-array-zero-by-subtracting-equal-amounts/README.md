# Make Array Zero by Subtracting Equal Amounts

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a non-negative integer array `nums`. In one operation, you must:

- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.

Return  *the  **minimum**  number of operations to make every element in* `nums` *equal to* `0`.

 

 **Example 1:** 

```
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

```

 **Example 2:** 

```
Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.

```

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 55.93%)  
**Submitted:** 2026-10-23T07:17:21.725Z  

```py
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        a=[]
        for i in  nums:
            if i!=0 and i not in a:
                a.append(i)
        return len(a)
        """
        return len(set(nums) - {0})
        """
        
```

---

[View on LeetCode](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/)