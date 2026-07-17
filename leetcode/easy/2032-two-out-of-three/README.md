# Two Out of Three

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given three integer arrays `nums1`, `nums2`, and `nums3`, return  *a  **distinct**  array containing all the values that are present in  **at least two**  out of the three arrays. You may return the values in  **any**  order*.

 

 **Example 1:** 

```
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

```

 **Example 2:** 

```
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

```

 **Example 3:** 

```
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.

```

 

 **Constraints:** 

- 1 <= nums1.length, nums2.length, nums3.length <= 100
- 1 <= nums1[i], nums2[j], nums3[k] <= 100

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 57.98%)  
**Memory:** 12.4 MB (beats 58.51%)  
**Submitted:** 2026-07-17T18:34:21.270Z  

```py
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        a=[]
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        for  i in  nums1.union(nums2).union(nums3):
            c=0
            if i in nums1:
                c+=1
            if i in nums2:
                c+=1
            if i in nums3:
                c+=1    
            if c>=2:
                a.append(i)
        return a    

```

---

[View on LeetCode](https://leetcode.com/problems/two-out-of-three/)