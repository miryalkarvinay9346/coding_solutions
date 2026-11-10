# Check Balanced String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `num` consisting of only digits. A string of digits is called  **balanced** if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return `true` if `num` is  **balanced**, otherwise return `false`.

 

 **Example 1:** 

 **Input:**  num = "1234"

 **Output:**  false

 **Explanation:** 

- The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
- Since 4 is not equal to 6, num is not balanced.

 **Example 2:** 

 **Input:**  num = "24123"

 **Output:**  true

 **Explanation:** 

- The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
- Since both are equal the num is balanced.

 

 **Constraints:** 

- 2 <= num.length <= 100
- num consists of digits only

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.1 MB (beats 92.75%)  
**Submitted:** 2026-11-10T09:03:55.762Z  

```py
class Solution:
    def isBalanced(self, num: str) -> bool:
        es,os=0,0
        for i in range(len(num)):
            if i%2==0:
                es+=int(num[i])
            else:
                os+=int(num[i])
        return es==os

```

---

[View on LeetCode](https://leetcode.com/problems/check-balanced-string/)