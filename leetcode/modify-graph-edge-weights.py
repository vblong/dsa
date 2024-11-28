from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        result = []
        graph = [[]for i in range(n)]

        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        def dijkstra(graph, start, end) -> float:
            dists = [1e9 for i in range(n)]
            dists[start] = 0
            minHeap = [(0, start)]
            while minHeap:
                du, u = heappop(minHeap)
                if du > dists[u]:
                    continue
                for v, dv in graph[u]:
                    if du + dv < dists[v]:
                        dists[v] = du + dv
                        heappush(minHeap, (dists[v], v))
            return dists[end]

        case1 = dijkstra(graph, source, destination)
        print('case1', case1)
        if case1 < target:
            return []
        
        # case 2
        if case1 == target:
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = 2*1e9
            return edges
        
        # case 3
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            newDists = dijkstra(graph, source, destination)
            if newDists <= target:
                edges[i][2] += target - newDists

                for j in range(len(edges)):
                    if i != j and edges[j][2] == -1:
                        edges[j][2] = 1e9
                return edges

        return result
n, edges, source, destination, target = 5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5 # [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
# n, edges, source, destination, target = 3, [[0,1,-1],[0,2,5]], 0, 2, 6 # []
# n, edges, source, destination, target = 4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6 # [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
# n, edges, source, destination, target = 5, [[1,3,10],[4,2,-1],[0,3,7],[4,0,7],[3,2,-1],[1,4,5],[2,0,8],[1,0,3],[1,2,5]], 3, 4, 11 # [[1,3,10],[4,2,1],[0,3,7],[4,0,7],[3,2,10],[1,4,5],[2,0,8],[1,0,3],[1,2,5]]
# n, edges, source, destination, target = 4, [[2,1,5],[0,1,3],[0,3,-1],[2,3,9]], 0, 2, 9 # [[1,3,10],[4,2,1],[0,3,7],[4,0,7],[3,2,10],[1,4,5],[2,0,8],[1,0,3],[1,2,5]]
# n, edges, source, destination, target = 4, [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]], 2, 3, 8 # [[1,3,10],[4,2,1],[0,3,7],[4,0,7],[3,2,10],[1,4,5],[2,0,8],[1,0,3],[1,2,5]]
n, edges, source, destination, target = 4, [[0,1,5],[1,2,7],[2,3,7],[3,1,9],[3,0,-1],[0,2,-1]], 2, 3, 7 # [[0,1,5],[1,2,7],[2,3,7],[3,1,9],[3,0,1000000005],[0,2,6]]
print(Solution().modifiedGraphEdges(n, edges, source, destination, target))


