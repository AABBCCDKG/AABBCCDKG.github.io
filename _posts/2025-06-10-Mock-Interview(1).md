---
layout: post
title: Mock Interview(1), LeetCode
date: 2025-06-10 18:32:13
description: LeetCode problems discussed during a mock interview on 2025-06-10
tags: LeetCode
categories: LeetCode
tabs: true
---
A tree with `n` nodes must have exactly `n - 1` edges
 - More than `n - 1`: cycle
 - Less than `n - 1`: not all nodes are connected: isolated nodes or a forest (multiple disconnected subtrees)

 Union-Find, Find:
 ```python
 parent = [i for i in range(n)]
 def find(a):
    while parent[x] != x:
        # when parent[x] == x, then it is the true root
        parent[x] = parent[parent[x]] 
        # find the true father node of x
        # since the father node of x is parent[x], the father node of parent[x] is parent[parent[x]]
        # then the true father node of x is parent[parent[x]]
        # x is not the root, but parent[x] and parent[parent[x]] may be the root
        x = parent[x] 
        # update the x
    return x
 ```

 Union-Find, Union: 