# Maximum Difference Between Adjacent Elements in a Circular Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a  **circular**  array `nums`, find the  **maximum**  absolute difference between adjacent elements.

 **Note** : In a circular array, the first and last elements are adjacent.

 

 **Example 1:** 

 **Input:**  nums = [1,2,4]

 **Output:**  3

 **Explanation:** 

Because `nums` is circular, `nums[0]` and `nums[2]` are adjacent. They have the maximum absolute difference of `|4 - 1| = 3`.

 **Example 2:** 

 **Input:**  nums = [-5,-10,-5]

 **Output:**  5

 **Explanation:** 

The adjacent elements `nums[0]` and `nums[1]` have the maximum absolute difference of `|-5 - (-10)| = 5`.

 

 **Constraints:** 

- 2 <= nums.length <= 100
- -100 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 46.81%)  
**Memory:** 19.3 MB (beats 55.32%)  
**Submitted:** 2026-10-14T15:52:02.281Z  

```py
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            k=abs(nums[i-1]-nums[i])
            if k>c:
                c=k
        if abs(nums[0]-nums[-1])>c:
            return abs(nums[0]-nums[-1])
        return c
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/)