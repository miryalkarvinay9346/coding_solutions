# NCOPIES - Rating 838

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T16:53:52.166Z  

```py
class Solution:
    def count_non_minimum(self, nums):
        # write your code here
        m=min(nums)
        cm=nums.count(m)
        return len(nums)-cm
```

---

[View on CodeChef](https://www.codechef.com/problems/NCOPIES)