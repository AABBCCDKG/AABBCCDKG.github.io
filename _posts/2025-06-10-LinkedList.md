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
        def __init__(self, val: int, prev = None, next = None):
            self.val = val
            self.next = next
            self.prev = prev
    
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

        def addAtHead(self, val: int) -> None:
            self.addAtIndex(0, val) # no need for updating self.size
        
        def addAtTail(self, val: int) -> None:
            self.addAtIndex(self.size, val) # no need for updating self.size
        
        def addAtIndex(self, index: int, val: int) -> None:
            if index < 0 or index > self.size:
                return
            
            curr = self.head
            for i in range(index + 1):
                curr = curr.next

            pred = curr.prev
            suc = curr # move afterward, so suc is curr instead of curr.next
            curr = ListNode(val)
            pred.next = curr
            curr.prev = pred
            curr.next = suc
            suc.prev = curr
            self.size += 1
    
        def deleteAtIndex(self, index: int) -> None:
            if index < 0 or index > self.size - 1:
                return
            
            curr = self.head
            for i in range(index + 1):
                curr = curr.next
            
            pred = curr.prev
            suc = curr.next
            pred.next = suc
            suc.prev = pred
            self.size -= 1
```
[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

The entire operation consists of rerouting the single pointer among `curr`, `pred`, and `suc`: replacing `curr.next = suc` with `curr.next = pred`. So there is no pointer exsiting between `curr` and `pred`, otherwise there will be a cycle. - why initialize `pred` as `None` instead of `dummy_head (dummy_head.next = head)`

```python
from typing import List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reverseList(self, head: Optional[LitsNode]):
        pred = None
        curr = head
        while curr: # check
            suc = curr.next # adjust
            curr.next = pred
            pred = curr # move
            cur = succ 
        return pred
```

[24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

```python
from typing import Optional
class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        pred = dummy_head
        #        [0,   1,   2,    3]
        # pred, curr, suc
        while pred.next and pred.next.next:
        # the length must be even
            curr = pred.next
            suc = pred.next.next

            curr.next = suc.next
            pred.next = suc
            suc.next = curr

            pred = curr
        return dummy_head.next
```

[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

Steps:
- These are number of loop iterations (for/while)
- To reach the n-th node in the linked list, you need `n - 1` steps (`n - 1` loop iterations)

Elements:
- This is the count of items in a range
- For index `left` and `right`, `right - left` calculates the length (the number of elements) of interval `[left, right)`

```python
from typing import Optional
class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, n: int, head: Optional[ListNode]):
        dummy_head = ListNode(0)
        dummy_head.next = head
        fast, slow = dummy_head
        # move fast n + 1 steps to make sure there are only n nodes between fast and slow

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
```
[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)

In the cycle, `fast` pointer is chasing `slow` pointer, and the relative velocity between `fast` and `slow` pointers are `2 - 1 = 1`, so they will meet for sure

```python
from typing import Optional
class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast = slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
```