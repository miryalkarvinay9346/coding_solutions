# Count Integers With Even Digit Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer `num`, return  *the number of positive integers  **less than or equal to***  `num`  *whose digit sums are  **even***.

The  **digit sum**  of a positive integer is the sum of all its digits.

 

 **Example 1:** 

```
Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    

```

 **Example 2:** 

```
Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

```

 

 **Constraints:** 

- 1 <= num <= 1000

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 84.04%)  
**Memory:** 19.2 MB (beats 89.36%)  
**Submitted:** 2026-10-05T16:29:03.656Z  

```py
class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            s=0
            while i>0:
                s+=i%10
                i=i//10
            if s%2==0:
                c+=1
        return c
```

---

[View on LeetCode](https://leetcode.com/problems/count-integers-with-even-digit-sum/)