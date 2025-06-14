---
layout: post
title: Stack and Queue, LeetCode
date: 2025-06-14 15:32:13
description: LeetCode problems related to Stack and Queue
tags: LeetCode
categories: LeetCode
tabs: true
---
[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/)

Double stack (input stack and output stack)
Transfer the element in input stack when output stack is empty
```python
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int):
        self.stack1.append(x)
    
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self):
        return not self.stack1 and not self.stack2
```

[225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)

`Queue`:
- initialization: `q = deque()`
- `q.append()`, `q.popleft()`

`List`:
- initialization: `l = []`
- `l.append()`, `l.pop()`
```python
from collections import deque
class MyStack:
    def __init__(self):
        self.queue = deque()
    

    def push(self, x: int):
        # there is no pop in the queue
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
            # [1, 2, 3]
            # [2, 3, 1]
            # [3, 1, 2]
            # not reverse, just move the last element to the begining

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue    
```

[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
            else:
                if not stack or char != stack.pop(): # stack should not be empty in advance
                    return False
        return not stack # stack should be empty exactly when iterate all char in s
```