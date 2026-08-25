# Backspace String Compare

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true`  *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

 **Example 1:** 

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

```

 **Example 2:** 

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

```

 **Example 3:** 

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

```

 

 **Constraints:** 

- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

 

 **Follow up:**  Can you solve it in `O(n)` time and `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 64.76%)  
**Submitted:** 2026-08-25T18:00:33.754Z  

```py
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            a=[]
            for ch in s:
                if ch == '#':
                    if a:
                        a.pop()
                else:
                    a.append(ch)
            return ''.join(a)
        return build(s) == build(t)

```

---

[View on LeetCode](https://leetcode.com/problems/backspace-string-compare/)