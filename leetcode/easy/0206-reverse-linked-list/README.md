# Reverse Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a singly linked list, reverse the list, and return  *the reversed list*.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```

 **Example 2:** 

```
Input: head = [1,2]
Output: [2,1]

```

 **Example 3:** 

```
Input: head = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

 

 **Follow up:**  A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 20.4 MB (beats 63.38%)  
**Submitted:** 2026-10-24T06:02:30.400Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None  # Previous node starts as None
        curr=head  # Current node starts at the head
        # Traverse the list
        while curr is not None:
            next_node=curr.next  # Save the next node
            curr.next=prev  # Reverse the link
            # Move pointers forward
            prev=curr  # Move prev to the current node
            curr=next_node  # Move curr to the next node
        # prev is now the new head of the reversed list
        return prev
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-linked-list/)