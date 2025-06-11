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

 ```python
 class Solution:
    def validTree(self, edges: List[List[int]]) -> bool:
        # [[1, 2]], [[1], [2]] all belongs to Lits[List[int]]
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * n
        # each node is own root
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            # if rootA = rootB, it means they already connected, there is a cycle
            if rootA == rootB:
                return False 
            
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA 
                # update the parent root
            else: 
                parent[rootA] = rootB
                rank[rootA] += 1
            return True
        for u, v in range(edges):
            if not union(u, v):
                return False
        return True
 ```