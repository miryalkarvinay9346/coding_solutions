# Permutation Difference between Two Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given two strings `s` and `t` such that every character occurs at most once in `s` and `t` is a permutation of `s`.

The  **permutation difference**  between `s` and `t` is defined as the  **sum**  of the absolute difference between the index of the occurrence of each character in `s` and the index of the occurrence of the same character in `t`.

Return the  **permutation difference**  between `s` and `t`.

 

 **Example 1:** 

 **Input:**  s = "abc", t = "bac"

 **Output:**  2

 **Explanation:** 

For `s = "abc"` and `t = "bac"`, the permutation difference of `s` and `t` is equal to the sum of:

- The absolute difference between the index of the occurrence of "a" in s and the index of the occurrence of "a" in t.
- The absolute difference between the index of the occurrence of "b" in s and the index of the occurrence of "b" in t.
- The absolute difference between the index of the occurrence of "c" in s and the index of the occurrence of "c" in t.

That is, the permutation difference between `s` and `t` is equal to `|0 - 1| + |1 - 0| + |2 - 2| = 2`.

 **Example 2:** 

 **Input:**  s = "abcde", t = "edbac"

 **Output:**  12

 **Explanation:**  The permutation difference between `s` and `t` is equal to `|0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12`.

 

 **Constraints:** 

- 1 <= s.length <= 26
- Each character occurs at most once in s.
- t is a permutation of s.
- s consists only of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 40.51%)  
**Memory:** 19.3 MB (beats 54.41%)  
**Submitted:** 2026-08-20T17:23:56.298Z  

```py
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    a+=abs(i - j)
        return a
```

---

[View on LeetCode](https://leetcode.com/problems/permutation-difference-between-two-strings/)