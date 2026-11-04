# Check if the Sentence Is Pangram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A  **pangram**  is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return `true` *if* `sentence` *is a  **pangram**, or* `false` *otherwise.* 

 

 **Example 1:** 

```
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

```

 **Example 2:** 

```
Input: sentence = "leetcode"
Output: false

```

 

 **Constraints:** 

- 1 <= sentence.length <= 1000
- sentence consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 11.77%)  
**Submitted:** 2026-11-04T03:49:34.138Z  

```py
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
```

---

[View on LeetCode](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)