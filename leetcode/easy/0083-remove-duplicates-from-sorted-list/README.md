# Remove Duplicates from Sorted List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a sorted linked list,  *delete all duplicates such that each element appears only once*. Return  *the linked list  **sorted**  as well*.

 

 **Example 1:** 

```
Input: head = [1,1,2]
Output: [1,2]

```

 **Example 2:** 

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 34.33%)  
**Memory:** 19.1 MB (beats 92.55%)  
**Submitted:** 2026-10-19T03:42:39.298Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```

---

[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)