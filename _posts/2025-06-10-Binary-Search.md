---
layout: post
title: Binary Search
date: 2025-06-10 00:32:13
description: LeetCode problems related to Binary Search
tags: LeetCode
categories: LeetCode
tabs: true
---

To calculate the middle index: use `(left + right) // 2`, where `//` denotes floor division. When the number of elements is even, the fomular returns the left-middle index.

Optimization: `left + (right - left) // 2` - Avoid integer overflow caused by a too large `right + left` through interval offset

Why O(log(n))?
- Each iteration eliminates half of elements
- Search Space shrinks exponentially
    - 1st iteration: n elements
    - 2st iteration: n/2 elements
- At most log(n) comparisons are needed
    - 2^k = n, log(n) = k
- Stop in advance (`nums[middle] == target`) before checking all search space (`left == right`)

```python
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left)//2
            if target < nums[middle]: 
                # target is smaller, search the left half and update the right boundary
                right = middle - 1
            elif target > nums[middle]: 
                # target is bigger, search the right half and update the left boundary
                left = middle + 1
            else:
                return middle
        return -1
```