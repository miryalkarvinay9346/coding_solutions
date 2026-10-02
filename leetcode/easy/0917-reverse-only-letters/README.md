# Reverse Only Letters

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse the string according to the following rules:

- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.

Return `s` *after reversing it*.

 

 **Example 1:** 

```
Input: s = "ab-cd"
Output: "dc-ba"

```

 **Example 2:** 

```
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

```

 **Example 3:** 

```
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range [33, 122].
- s does not contain '\"' or '\\'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 36.67%)  
**Submitted:** 2026-10-02T10:46:21.035Z  

```py
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=[]
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                a.append(s[i])
        res=[]
        i=0
        for ch in s:
            if ch.isalpha():
                res.append(a[i])
                i += 1
            else:
                res.append(ch)
        return ''.join(res)
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-only-letters/)