from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = defaultdict(int)
        adj = defaultdict(list)
        nodes = []
        used = [False] * len(edges)
        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)
        nodes = list(adj.keys())
        for n in nodes:
            parents[n] = n
        counts = len(nodes)

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parents[rootX] = rootY

        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x

        for i in range(len(edges)):
            # print('------ edge:', edges[i])
            ai, bi = edges[i][0], edges[i][1]
            # print('checking ', ai, ': ', find(ai), ', and', bi, ': ', find(bi))
            if find(ai) != find(bi):
                union(ai, bi)
                counts -=1
                used[i] = True
                # print('use edge', edges[i], ', parents', parents)
                if counts == 1:
                    break
        # print('nodes', nodes)
        
        # print('used edges', used)
        for i in range(len(edges)):
            if not used[i]:
                return edges[i]
        
edges = [[1,2],[1,3],[2,3]] # [2, 3]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]] # [1, 4]
edges = [[1,3],[3,4],[1,5],[3,5],[2,3]] # [3,5]
print(Solution().findRedundantConnection(edges))
