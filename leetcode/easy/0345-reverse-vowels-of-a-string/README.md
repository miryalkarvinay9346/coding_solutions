# Reverse Vowels of a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

 **Example 1:** 

 **Input:**  s = "IceCreAm"

 **Output:**  "AceCreIm"

 **Explanation:** 

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

 **Example 2:** 

 **Input:**  s = "leetcode"

 **Output:**  "leotcede"

 

 **Constraints:** 

- 1 <= s.length <= 3 * 105
- s consist of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 17 ms (beats 23.55%)  
**Memory:** 23.8 MB (beats 5.06%)  
**Submitted:** 2026-08-13T17:57:07.252Z  

```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        """
        a = []
        indexs = []
        for i in range(len(s)):
            if s[i] in vowels:
                a.append(s[i])
                indexs.append(i)
        p = []
        k = len(a) - 1
        for j in range(len(s)):
            if j in indexs:
                p.append(a[k])
                k -= 1
            else:
                p.append(s[j])
        return "".join(p)
        """
        a = []
        indexs = set()
        for i in range(len(s)):
            if s[i] in vowels:
                a.append(s[i])
                indexs.add(i)
        p = []
        k = len(a) - 1
        for j in range(len(s)):
            if j in indexs:
                p.append(a[k])
                k -= 1
            else:
                p.append(s[j])
        return "".join(p)

```

---

[View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)