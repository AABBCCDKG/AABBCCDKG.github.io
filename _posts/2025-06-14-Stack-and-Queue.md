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