# Minimum String Length After Removing Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `s` consisting only of  **uppercase**  English letters.

You can apply some operations to this string where, in one operation, you can remove  **any**  occurrence of one of the substrings `"AB"` or `"CD"` from `s`.

Return  *the  **minimum**  possible length of the resulting string that you can obtain*.

 **Note**  that the string concatenates after removing the substring and could produce new `"AB"` or `"CD"` substrings.

 

Original
Python3
 **Example 1:** 

```
Input:s = "ABFCACDB"Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
```

 **Example 2:** 

```
Input:s = "ACBBD"Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists only of uppercase English letters.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 45.68%)  
**Memory:** 19 MB (beats 86.42%)  
**Submitted:** 2026-11-24T14:20:09.885Z  

```py
class Solution:
    def minLength(self, s: str) -> int:
        """
        a=[]
        for i in s:
            if a:
                if (a[-1]=="A" and i=="B"):
                    a.pop()
                elif (a[-1]=='C' and i=='D'):
                    a.pop()
                else:
                    a.append(i)
            else:
                a.append(i)
        return len(a)
        """
        while "AB" in s or "CD" in s:
            s=s.replace("AB","").replace("CD","")
        return len(s)
        
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/)