class Solution:
    def minFlips(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])        

        def countFlips(row):
            left = 0
            right = len(row) - 1
            cnt = 0
            while left <= right:
                if row[left] != row[right]:
                    cnt += 1
                left += 1
                right -= 1
            return cnt        


        rowFlips = 0
        for i in range(m):
            rows = grid[i]
            rowFlips += countFlips(rows)

        colFlips = 0
        for col in range(n):
            cols = []
            for i in range(m):
                cols.append(grid[i][col])
            colFlips += countFlips(cols)

        return min(rowFlips, colFlips)

grid = [[1,0,0],[0,0,0],[0,0,1]] # 2
grid = [[0,1],[0,1],[0,0]] #
grid = [[1],[0]] # 0
grid = [[0,0]] # 0
print(Solution().minFlips(grid))