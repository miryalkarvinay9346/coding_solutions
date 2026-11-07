# Divide Array Into Equal Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:

- Each element belongs to exactly one pair.
- The elements present in a pair are equal.

Return `true`  *if nums can be divided into*  `n`  *pairs, otherwise return*  `false`.

 

 **Example 1:** 

```
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

```

 **Example 2:** 

```
Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

```

 

 **Constraints:** 

- nums.length == 2 * n
- 1 <= n <= 500
- 1 <= nums[i] <= 500

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 25.52%)  
**Submitted:** 2026-11-07T09:10:33.655Z  

```py

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq=[0]*501
        for num in nums:
            freq[num]+=1
        for count in freq:
            if count%2!=0:
                return False
        return True

```

---

[View on LeetCode](https://leetcode.com/problems/divide-array-into-equal-pairs/)