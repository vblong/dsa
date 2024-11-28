from collections import defaultdict
from heapq import heappop, heappush
from data import nodes, edges

def dijkstra(nodes, edges, source, target) -> float:
    distances = defaultdict(float)
    for n in nodes:
        distances[n] = 1e9 * 1.0
    distances[source] = 0.0
    q = [(0.0, source, ())]
    visited = set()
    while q:
        cost, u, path = heappop(q)
        print(cost, u, path)        
        if u not in visited:
            print(1)
            visited.add(u)
            path += (u,)
            if u == target:
                print(11)
                return (cost, path)
            print(2, edges[u])
            for v, costUV in edges[u]:
                # print(v, cost + costUV, distances[cost])
                if v in visited:
                    continue
                if cost + costUV < distances[v]:
                    distances[v] = cost + costUV
                    heappush(q, (distances[v], v, path))
            print(3, q)
    print(distances)
    # return distances[target]
    return (-1, ())


# print(dists)
print(dijkstra(nodes, edges, 'b', 'c'))