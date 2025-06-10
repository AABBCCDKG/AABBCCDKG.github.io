---
layout: post
title: Binary Search
date: 2025-06-10 00:32:13
description: LeetCode problems related to Binary Search
tags: LeetCode
categories: LeetCode
tabs: true
---

To calculate the middle index: use `(left + right)//2`, where `//` denotes floor division. When the number of elements is even, the fomular returns the left-middle index.

Optimization: `left + (right - left) // 2` - Avoid integer overflow caused by a too large `right + left` through interval offset
