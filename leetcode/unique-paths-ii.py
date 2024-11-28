from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        directions = [(1, 0), (0, 1)]
        results = 0

        ######## RECUSION (TLE)
        # def f(x, y, visited):
        #     nonlocal results
        #     if x == m - 1 and y == n - 1 and obstacleGrid[x][y] == 0:
        #         results += 1
        #         return
        #     for dx, dy in directions:
        #         x2, y2 = x + dx, y + dy
        #         if 0 <= x2 < m and 0 <= y2 < n and obstacleGrid[x2][y2] != 1 and (x2, y2) not in visited:
        #             f(x2, y2, visited + [(x2, y2)])
        # if obstacleGrid[0][0] == 0:
        #     f(0, 0, [])

        # return results
    
        ####### RECURSION + MEMOIZ
        # memoiz = {}
        # def f(x, y, visited):
        #     nonlocal results
        #     if x == m - 1 and y == n - 1 and obstacleGrid[x][y] == 0:
        #         return 1
        #     if (x, y) in memoiz:
        #         return memoiz[(x, y)]
        #     ans = 0
        #     for dx, dy in directions:
        #         x2, y2 = x + dx, y + dy
        #         if 0 <= x2 < m and 0 <= y2 < n and obstacleGrid[x2][y2] != 1 and (x2, y2) not in visited:
        #             ans += f(x2, y2, visited + [(x2, y2)])
        #     memoiz[(x, y)] = ans
        #     return ans
        # if obstacleGrid[0][0] == 0:
        #     results = f(0, 0, [])

        # return results

        ####### DP BOTTOM UP
        # dp = [[0 for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             continue
        #         if i == 0 and j == 0:
        #             dp[i][j] = 1
        #         else:
        #             if i == 0:
        #                 dp[i][j] = dp[i][j-1]
        #             elif j == 0:
        #                 dp[i][j] = dp[i-1][j]
        #             else:
        #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # return dp[m - 1][n - 1]
    
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]] # 2
obstacleGrid = [[0,1],[0,0]] # 1
obstacleGrid = [[1]] # 0
obstacleGrid = [[1,0]] # 0
obstacleGrid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))