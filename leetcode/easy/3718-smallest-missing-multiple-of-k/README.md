# Smallest Missing Multiple of K

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` and an integer `k`, return the  **smallest positive multiple**  of `k` that is  **missing**  from `nums`.

A  **multiple**  of `k` is any positive integer divisible by `k`.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [8,2,3,4,6], k = 2

 **Output:**  10

 **Explanation:** 

The multiples of `k = 2` are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

 **Example 2:** 

 **Input:**  nums = [1,4,7,10,15], k = 5

 **Output:**  5

 **Explanation:** 

The multiples of `k = 5` are 5, 10, 15, 20... and the smallest multiple missing from `nums` is 5.

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 50.27%)  
**Submitted:** 2026-11-13T16:51:11.953Z  

```py
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            if i*k not in nums:
                return i*k
            i=i+1

```

---

[View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/)