from collections import defaultdict, deque
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        matrix = [[0 for j in range(n)] for i in range(n)]        
        adj = defaultdict(list)
        for i, e in enumerate(edges):
            ai, bi = e[0], e[1]
            prob = succProb[i]
            matrix[ai][bi] = prob
            matrix[bi][ai] = prob
            adj[ai].append(bi)
            adj[bi].append(ai)

        # # debug
        # for m in matrix:
        #     print(m)
        distances = [0] * n
    
        def dijkstra(start):
            distances[start] = 1e9
            # print('start dist', distances)
            nonVisited = [i for i in range(n)]
            # print('nonvisited', nonVisited)
            while len(nonVisited):
                # choose node which has smallest distances
                minIdx, minDist = nonVisited[0], distances[0]
                chosenIdx = 0
                for i, nodeId in enumerate(nonVisited):
                    if distances[nodeId] > minDist:
                        minIdx, minDist = nodeId, distances[nodeId]
                        chosenIdx = i
                
                nonVisited = nonVisited[:chosenIdx] + nonVisited[chosenIdx+1:]
                for neighbor in adj[minIdx]:
                    if neighbor in nonVisited:
                        if distances[minIdx] == 1e9:
                            # print('-update', distances[neighbor], 'vs', matrix[minIdx][neighbor])
                            distances[neighbor] = max(distances[neighbor], matrix[minIdx][neighbor])
                        else:
                            # print('-update', distances[neighbor], 'vs', matrix[minIdx][neighbor] * distances[minIdx])
                            distances[neighbor] = max(distances[neighbor], distances[minIdx] * matrix[minIdx][neighbor])
        dijkstra(start_node)

        return distances[end_node]
    
n, edges, succProb, start, end = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2 # 0.25000
n, edges, succProb, start, end = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2 # 0.3
n, edges, succProb, start, end = 5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4 # 0.21390
print(Solution().maxProbability(n, edges, succProb, start, end))