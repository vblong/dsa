class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        result = 0
        arr = [[0 for _ in range(n * 3)] for _ in range(n * 3)]
       
        for i in range(len(grid)):
            startRow = i * 3
            for j in range(len(grid[i])):
                startCol = j * 3
                if grid[i][j] == '/':
                    arr[startRow][startCol + 2] = 1
                    arr[startRow + 1][startCol + 1] = 1
                    arr[startRow + 2][startCol] = 1
                elif grid[i][j] == '\\':
                    arr[startRow][startCol] = 1
                    arr[startRow + 1][startCol + 1] = 1
                    arr[startRow + 2][startCol + 2] = 1
                else:
                    continue

        def dfs(arr, i, j, limit):
            arr[i][j] = 1
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for d in directions:
                newI = i + d[0]
                newJ = j + d[1]
                if 0 <= newI < limit and 0 <= newJ < limit and arr[newI][newJ] != 1:
                    dfs(arr, newI, newJ, limit)


        for i in range(n * 3):
            for j in range(n * 3):
                if arr[i][j] == 0:
                    dfs(arr, i, j, n * 3)
                    result += 1
        return result
    

grid = [" /","/ "] # 2
# grid = [" /","  "] # 1
# grid = ["/\\","\\/"] # 5
print(Solution().regionsBySlashes(grid))