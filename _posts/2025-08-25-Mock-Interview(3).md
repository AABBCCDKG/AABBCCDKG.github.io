---
layout: post
title: Mock Interview(3), LeetCode
date: 2025-08-25 18:32:13
description: LeetCode problems discussed during a mock interview on 2025-08-25
tags: LeetCode
categories: LeetCode
tabs: true
---
[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

变量的类型，是用冒号`:`，而不是`=`：
- `prerequisites: List[Tuple[int, int]]`

对于`Tuple`, 从`typing`引入，和`List`一样.

对于`Tuple`, 用
- `for pair in prerequisites: a, b = pair`是可以的
- `for a, b in prerequisites也是可以的`

从`collections`里引入`deque`, `queue = deque()`来初始化

参数中的变量，用逗号隔开


```python
from collections import deque
from typing import List, Tuple

def find_course_order(num_courses: int, pre: List[Tuple[int, int]]) -> List[int]:
    graph: List[int] = [[] for _ in range(num_courses)]
    indegree: List[int] = [0] * num_courses
    
    for pair in pre:
        a, b = pair
        graph[b].append(a)
        indegree[a] += 1
    
    queue: deque[int] = deque()
    for course_id in range(num_courses):
        if indegree[course_id] == 0:
            queue.append(course_id)
    order: List[int] = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for next_course in graph[current]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    if len(order) == num_courses:
        return order
    else:
        return []

def main():
    numCourses = 2
    pre = [[1, 0]]
    print(find_course_order(numCourses, pre))

if __name__ == '__main__':
    main()
```


[739.Daily Temperature](https://leetcode.com/problems/daily-temperatures/description/)

```python
from collections import List

class Solution:
    def dailyTemperature(self, temperatures: List[int]):
        n = len(temperatures)
        answer: List[int] = [0] * n

        stack_indeces: List[int] = []

        for i in range(n):
            current_temp = temeratures[i]

            while stack_indeces and current_temp > temperatures[stack_indeces[-1]]:
                j = stack_indices.pop()
                answer[j] = i - j
        stack_indices.append(i)
    return answer

def main():
    solver = Solution()
    case1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solver.dailyTemperatures(case1))

if __name__ == '__main__':
    main()
```

