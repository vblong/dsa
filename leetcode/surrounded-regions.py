from collections import deque


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        def bfs(x, y):
            region = [(x, y)]
            q = deque([(x, y)])
            isSurrounded = True
            while q:
                x, y = q.popleft()
                visited.add((x, y))
                if x == 0 or x == m-1 or y == 0 or y == n - 1:
                    isSurrounded = False
                for dx, dy in directions:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 'O' and (xx, yy) not in region:
                        q.append((xx, yy))
                        region.append((xx, yy))
            if isSurrounded:
                for xx, yy in region:
                    board[xx][yy] = 'X'

        def bfss(x, y):
            print('bfss at', x, y)
            q = deque([(x, y)])
            vit = set((x, y))
            while q:
                x, y = q.popleft()
                print('pop at', x, y)
                visited.add((x, y))
                vit.add((x, y))
                board[x][y] = 'A'
                for dx, dy in directions:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 'O' and (xx, yy) not in q and (xx, yy) not in visited and (xx, yy) not in vit:
                        q.append((xx, yy))
        print('ehem1')
        for i in range(m):
            if board[i][0] == 'O' and (i, 0) not in visited:
                bfss(i, 0)
            if board[i][n - 1] == 'O' and (i, n - 1) not in visited:
                bfss(i, n - 1)
        print('ehem2')
        for j in range(n):
            if board[0][j] == 'O':
                bfss(0, j)
            if board[m - 1][j] == 'O':
                bfss(m - 1, j)

        print('after all')
        for b in board:
            print(b)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                else:
                    pass
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O' and (i, j) not in visited:
        #             # print('start bfs at', i, j)
        #             bfs(i, j)
        #             # print('after that----')
        #             # for b in board:
        #             #     print(b)


board = [["O","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","X","O","X","O","O","O","O","X","O","O","X","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","X","O"],["O","X","X","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","O","O","X","X","O"],["O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","O","O","O","O","X","X","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","O","O","O","O","X","O","O","O","O","O","X"],["O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","X","O","X","O","O"],["O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","X","O","O","O","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]]
# for b in board:
#     print(b)
Solution().solve(board)