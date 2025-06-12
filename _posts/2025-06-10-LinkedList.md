---
layout: post
title: Linked List, LeetCode
date: 2025-06-10 15:32:13
description: LeetCode problems related to Linked List
tags: LeetCode
categories: LeetCode
tabs: true
---

```python
# Definition for singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        # '=' assigns value
        # ':' type annotation
        # val: int = 0
        self.val = 0
        self.next = next
```
```python
# Definition for doubly-linked list
class ListNode:
    def __init__(self, val: int = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
```
Since ListNode may be `None`, so the type annotation should be Optional[ListNode]
```python
from typing import Optional
def method(head: Optional[ListNode]):
```

Check `curr.next` for deletion of Linked List, so use `while curr.next` instead of `while curr`

```python
from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        curr = dummy_head
        while curr.next: 
            if curr.next.val == val:
                curr.next = curr.next.next
                # curr.next is updated, check it 
                # again without moving curr forward 
                # otherwise, might skip consecutive target nodes.
            else:
                curr = curr.next
        return dummy_head.next
```
[707. Design Linked List](https://leetcode.com/problems/design-linked-list/description/)

`return None` equals to `return` (end the function in advance)

```python
from typing import Optional
class Solution:
    class ListNode:
        def __init__(self, val: int, pre = None, next = None):
            self.val = val
            self.next = next
            self.pre = pre
    
    class MyLinkedList:
        def __init__(self):
            self.head = ListNode(0)
            self.tail = ListNode(0)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0

        def get(self, index: int) -> int:
            if index < 0 or index > self.size - 1:
                return -1
            
            curr = self.head 
            # use self.head: iterate index + 1 times, i could be index
            # use self.head.next: iterate index times, 
            for i in range(index + 1):
                curr = curr.next
                # during this block, curr is the node at position i
            return curr.val

        def
```