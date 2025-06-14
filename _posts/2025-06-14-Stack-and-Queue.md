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

[1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)

The index of `0` of stack: the first element: `''.join(stack)` equals to `''.join(list)` 

The index of `-1` of stack: the last element(top)

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append()
        return ''.join(stack)
```
[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

`if token in '+-*/'`: Check whether token is not one of the characters `+`, `-`, `*`, or `/`.

`a // b`: floor division (only when there is no negative integer between `a` and `b`)
`int(a/b)`: truncate toward zero

```python
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: # the order of iteration is from index 0 to index len(tokens) - 1
            if token not in '+-*/':
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left/right))
        return stack[0]
```