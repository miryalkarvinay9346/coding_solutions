# Find the XOR of Numbers Which Appear Twice

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array `nums`, where each number in the array appears  **either**  once or twice.

Return the bitwise `XOR` of all the numbers that appear twice in the array, or 0 if no number appears twice.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [1,2,1,3]

 **Output:**  1

 **Explanation:** 

The only number that appears twice in `nums` is 1.

 **Example 2:** 

 **Input:**  nums = [1,2,3]

 **Output:**  0

 **Explanation:** 

No number appears twice in `nums`.

 **Example 3:** 

 **Input:**  nums = [1,2,2,1]

 **Output:**  3

 **Explanation:** 

Numbers 1 and 2 appeared twice. `1 XOR 2 == 3`.

 

 **Constraints:** 

- 1 <= nums.length <= 50
- 1 <= nums[i] <= 50
- Each number in nums appears either once or twice.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 32.16%)  
**Memory:** 18.9 MB (beats 96.71%)  
**Submitted:** 2026-11-19T15:32:14.980Z  

```py
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c=0
        for i in set(nums):
            if nums.count(i)==2:
                c=c^i
        return c
```

---

[View on LeetCode](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/)