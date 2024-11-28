from collections import defaultdict, deque


grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1

def bfs(k):
    rows, cols = len(grid), len(grid[0])

    state = (0, 0, k)
    q = deque([(0, state)])
    visited = set([state])

    while q:
        steps, (row, col, k) = q.popleft()

        if (row, col) == (rows - 1, cols -1): 
            return steps
        
        for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if (0 <= new_row < rows) and (0 <= new_col < cols):
                new_k = k - grid[new_row][new_col]
                new_state = (new_row, new_col, new_k)
                if new_k >= 0 and new_state not in visited:
                    q.append((steps + 1, new_state))
                    visited.add(new_state)
    return -1
print(bfs(k))