from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        degree = [0 for i in range(numCourses)]
        adj = defaultdict(list)

        for pre in prerequisites:
            if len(pre):
                ai, bi = pre[0], pre[1]
                degree[ai] += 1
                adj[bi].append(ai)

        q = deque([])
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        print(adj)
        print('degree', degree)
        while q:
            coursei = q.popleft()
            result.append(coursei)
            for neighbor in adj[coursei]:
                degree[neighbor] -= 1
                if degree[neighbor] <= 0:
                    q.append(neighbor)
        
        return result if len(result) == numCourses else []

numCourses, prerequisites = 2, [[1,0]] # [0, 1]
# numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]] # [0, 2, 1, 3]
numCourses, prerequisites = 1, [[]] # [0]
numCourses, prerequisites = 3, [[1,0],[1,2],[0,1]] # []
print(Solution().findOrder(numCourses, prerequisites))