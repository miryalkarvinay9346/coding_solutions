# String Matching in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of string `words`, return all strings in `words` that are a substring of another word. You can return the answer in  **any order**.

 

Original
Python3
 **Example 1:** 

```
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

```

 **Example 2:** 

```
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

```

 **Example 3:** 

```
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

```

 

 **Constraints:** 

- 1 <= words.length <= 100
- 1 <= words[i].length <= 30
- words[i] contains only lowercase English letters.
- All the strings of words are unique.

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 9.93%)  
**Memory:** 19.3 MB (beats 48.53%)  
**Submitted:** 2026-11-14T11:57:12.741Z  

```py
class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        a=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        a.append(words[i])
                    elif words[j] in words[i]:
                        a.append(words[j])
        return list(set(a))
```

---

[View on LeetCode](https://leetcode.com/problems/string-matching-in-an-array/)