# Count Pairs Of Similar Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **0-indexed**  string array `words`.

Two strings are  **similar**  if they consist of the same characters.

- For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
- However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.

Return  *the number of pairs* `(i, j)` *such that* `0 <= i < j <= word.length - 1` *and the two strings* `words[i]` *and* `words[j]` *are similar*.

 

Original
Python3
 **Example 1:** 

```
Input:words = ["aba", "aabb", "abcd", "bac", "aabc"]Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 

```

 **Example 2:** 

```
Input:words = ["aabb", "ab", "ba"]Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.

```

 **Example 3:** 

```
Input:words = ["nba", "cba", "dba"]Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.
```

 

 **Constraints:** 

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consist of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 227 ms (beats 18.70%)  
**Memory:** 19.2 MB (beats 88.03%)  
**Submitted:** 2026-11-12T16:40:18.627Z  

```py
class Solution:
    def similarPairs(self, words: list[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    c+=1
        return c

```

---

[View on LeetCode](https://leetcode.com/problems/count-pairs-of-similar-strings/)