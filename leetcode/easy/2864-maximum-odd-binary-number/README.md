# Maximum Odd Binary Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **binary**  string `s` that contains at least one `'1'`.

You have to  **rearrange**  the bits in such a way that the resulting binary number is the  **maximum odd binary number**  that can be created from this combination.

Return  *a string representing the maximum odd binary number that can be created from the given combination.* 

 **Note** that the resulting string  **can**  have leading zeros.

 

Original
Python3
 **Example 1:** 

```
Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

```

 **Example 2:** 

```
Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists only of '0' and '1'.
- s contains at least one '1'.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 39.78%)  
**Memory:** 19.1 MB (beats 89.56%)  
**Submitted:** 2026-11-20T16:26:06.316Z  

```py
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count('1')
        zeros=len(s)-ones
        return '1'*(ones-1)+ '0'*zeros+ '1'
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-odd-binary-number/)