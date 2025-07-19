---
layout: post
title: Mock Interview(1), LeetCode
date: 2025-07-18 18:32:13
description: LeetCode problems discussed during a mock interview on 2025-07-18
tags: LeetCode
categories: LeetCode
tabs: true
---

[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)

Part 1: Count the Frequency of characters in `t`
```python
# Firts way
from collections import Counter
dict_t = Count(t) # C is capitalized

# Second way
dict_t = {}
for char in t:
    dict_t[char] = dict_t.get(char, 0) + 1 
    # dict_t.get(char): get the value of dict_t[char]
    # dict_t.get(char, 0): get the value of dict_t[char], if there is no char in dict_t, return 0
```

Part 2: Find a Window in `s` that contains those characters with required frequencies

```python
# general step:
left = 0 # window sliding is a double pointer problem
for right in range():
    # in what condition, we should shrink the window(move the left pointer to the right, most of time, it would be while loop)
```

Formed: Whenever the frequency of a character in the current window exactly macthes the required count in `t`, do addition

Required: the number of different type of character in `t`.

```python
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        min_length = float('inf')
        left = 0
        required = len(dict_t)
        window_count = {}
        formed = 0
        min_left =0
        min_right = 0
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            if char in dict_t and window_count[char] == dict_t[char]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_length:
                    min_length = min(min_length, right - left + 1)
                    min_left = left
                    min_right = right
                window_count[s[left]] -= 1
                if s[left] in dict_t and window_count[s[left]] < dict_t[s[left]]:
                    formed -= 1
                left += 1
        return "" if min_length == float('inf') else s[min_left: min_right + 1]
        # min_length == float('inf') means throughout the entire traversal, no valid window that satisfies the condition was ever found,
        #  so min_length was never updated: no need to do the check: if len(s) < len(t)
```



[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

Window means there are two pointers: `left` and `right`

`set()` is unordered, but it allows `O(1)` time complexity for checking the existence of an element. 

For sliding window problems, the typical patter is:
- At each step, expand the window by moving the right pointer, and then shrink the window from the left as needed to maintain the desired condition (window sliding is a double pointer problem)

The `set` object does not support `.append()` - use `.add()` to insert elements and `.remove()` to delete them

When shrinking the window, it's often not enough to remove a single element. You should use a `while` loop to continue shrinking the window from the left until the condition is satisfied again.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = float('-inf')
        left = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(right - left + 1, max_length)
        return max_length
```