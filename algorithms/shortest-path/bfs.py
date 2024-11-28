from collections import deque


nodes = [1, 2, 3, 4, 5, 6, 7]
edges = {
    1: [5, 2],
    2: [4, 3],
    3: [],
    4: [],
    5: [7, 6],
    6: [],
    7: []
}

def bfs(source):
    q = deque([source])
    while q:
        node = q.popleft()

        for nei in edges[node]:
            q.append(nei)
        print(node)

bfs(1)
