# Reverse Words in a String III

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

 **Example 1:** 

```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

```

 **Example 2:** 

```
Input: s = "Mr Ding"
Output: "rM gniD"

```

 

 **Constraints:** 

- 1 <= s.length <= 5 * 104
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space.

## Solution

**Language:** Python  
**Runtime:** 8 ms (beats 26.65%)  
**Memory:** 19.8 MB (beats 54.16%)  
**Submitted:** 2026-08-22T08:19:10.114Z  

```py
class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        k=""
        for i in a:
            k=k+i[::-1]+" "
        return k[:len(k)-1]
        
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/)