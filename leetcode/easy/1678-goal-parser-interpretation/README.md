# Goal Parser Interpretation

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You own a  **Goal Parser**  that can interpret a string `command`. The `command` consists of an alphabet of `"G"`, `"()"` and/or `"(al)"` in some order. The Goal Parser will interpret `"G"` as the string `"G"`, `"()"` as the string `"o"`, and `"(al)"` as the string `"al"`. The interpreted strings are then concatenated in the original order.

Given the string `command`, return  *the  **Goal Parser** 's interpretation of* `command`.

 

 **Example 1:** 

```
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

```

 **Example 2:** 

```
Input: command = "G()()()()(al)"
Output: "Gooooal"

```

 **Example 3:** 

```
Input: command = "(al)G(al)()()G"
Output: "alGalooG"

```

 

 **Constraints:** 

- 1 <= command.length <= 100
- command consists of "G", "()", and/or "(al)" in some order.

## Solution

**Language:** Python  
**Runtime:** 49 ms (beats 25.99%)  
**Memory:** 19.2 MB (beats 43.94%)  
**Submitted:** 2026-09-10T17:59:04.570Z  

```py
class Solution:
    def interpret(self, command: str) -> str:
        s=""
        i=0
        while  i <(len(command)):
            if command[i]=="G":
                s+="G"
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                s+="o"
                i+=1
            elif  command[i]=="(" and command[i+1]=="a" and command[i+2]=="l" and command[i+3]==")":
                s+="al"
                i+=3
            else:
                i+=1
        return s
```

---

[View on LeetCode](https://leetcode.com/problems/goal-parser-interpretation/)