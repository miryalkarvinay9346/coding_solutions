# Find the Sum of Encrypted Integers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` containing  **positive**  integers. We define a function `encrypt` such that `encrypt(x)` replaces  **every**  digit in `x` with the  **largest**  digit in `x`. For example, `encrypt(523) = 555` and `encrypt(213) = 333`.

Return  *the  **sum** of encrypted elements*.

 

 **Example 1:** 

 **Input:** nums = [1,2,3]

 **Output:** 6

 **Explanation:**  The encrypted elements are `[1,2,3]`. The sum of encrypted elements is `1 + 2 + 3 == 6`.

 **Example 2:** 

 **Input:** nums = [10,21,31]

 **Output:** 66

 **Explanation:**  The encrypted elements are `[11,22,33]`. The sum of encrypted elements is `11 + 22 + 33 == 66`.

 

 **Constraints:** 

- 1 <= nums.length <= 50
- 1 <= nums[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 65 ms (beats 24.00%)  
**Memory:** 19.2 MB (beats 74.25%)  
**Submitted:** 2026-11-02T14:42:26.595Z  

```py
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            k=0
            for j in str(i):
                k=max(k,int(j))
            s+=int(str(k)*len(str(i)))
        return s

```

---

[View on LeetCode](https://leetcode.com/problems/find-the-sum-of-encrypted-integers/)