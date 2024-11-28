from collections import deque


class Solution:
    def minDays(self, grid) -> int:
        def isMoreIsland(grid, totalIslandCells):
            # print('check is more island')
            m = len(grid)
            n = len(grid[0])
            row, col = -1, -1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        row, col = i, j
                        break
                if row != -1 and col != -1:
                    break

            marked = [ [0 for j in range(n)] for i in range(m)]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([(row, col)])
            islandCells = 0
            while queue:
                # print('quqeue is', queue)
                row, col = queue[0][0], queue[0][1]
                queue.popleft()
                islandCells += 1
                marked[row][col] = 1
                # print('marking cell', row, col)
                # for ii in range(m):
                #     print(marked[ii]) 
                for d in directions:
                    newRow = row + d[0]
                    newCol = col + d[1]
                    if 0 <= newRow < m and 0 <= newCol < n:
                        if grid[newRow][newCol] == 1 and marked[newRow][newCol] == 0 and (newRow, newCol) not in queue:
                            queue.append((newRow, newCol))
            print('total found cells', islandCells, 'total', totalIslandCells)
            return islandCells < totalIslandCells

        def oneBridge(grid, totalIslandCells):
            # print('check has bridge')
            m = len(grid)
            n = len(grid[0])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        newGrid = []
                        for ii in range(m):
                            r = []
                            for jj in range(n):
                                if ii == i and jj == j:
                                    r.append(0)
                                else:
                                    r.append(grid[ii][jj])
                            newGrid.append(r)

                        # print('check one bridge with this')
                        # for ii in range(m):
                        #     print(newGrid[ii])
                        if totalIslandCells - 1 == 0:
                            return True
                        if isMoreIsland(newGrid, totalIslandCells - 1):
                            return True
            return False
        
        print('initla')
        for i in range(len(grid)):
            print(grid[i])
        print('initla')

        totalIslandCells = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    totalIslandCells += 1

        # all waters
        if totalIslandCells == 0:
            # print('ehem -1')
            return 0
        
        # there is more than 1 island
        more = isMoreIsland(grid, totalIslandCells)
        if more == True:
            # print('ehem 0')
            return 0
        
        if oneBridge(grid, totalIslandCells):
            return 1
        return 2

grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]] # 2
grid = [[1,1]] # 2
grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]] # 2
grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]] # 1
grid = [[0,0,0],[0,1,0],[0,0,0]] # 1
print(Solution().minDays(grid))