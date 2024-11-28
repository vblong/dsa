from collections import defaultdict
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        value_to_rows = defaultdict(set)
        for i, row in enumerate(grid):
            for val in row:
                value_to_rows[val].add(i)
        # print(value_to_rows)
        dp = defaultdict(int, {0: 0})
        # print(dp)
        for value in sorted(value_to_rows)[::-1]:
            for bitmask in list(dp):
                # print('bitmask', bitmask, dp[bitmask])
                score = dp[bitmask]
                for r in value_to_rows[value]:
                    if not (bitmask & (1 << r)):
                        dp[bitmask | (1 << r)] = max(dp[bitmask | (1 << r)], score + value)
        return max(dp.values())

        # for r in grid:
        #     print(r)        

        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     grid[i].sort()
        # for r in grid:
        #     print(r)      
        # results = 0
        # dp = {}
        # def f(r, previous, currentSum):
        #     nonlocal results, m, n
        #     # print(r, previous, currentSum)
        #     if r >= m:
        #         return currentSum
            
        #     if (r, ",".join(previous)) in dp:
        #         return dp[(r, ",".join(previous))]

        #     ans = currentSum
        #     # results = max(results, ans)
        #     for i in range(n):
        #         if previous and grid[r][i] < (int)(previous[-1]):
        #             continue
        #         case1 = 0
        #         if (str)(grid[r][i]) not in previous:
        #             case1 = max(ans, f(r + 1, previous + [(str)(grid[r][i])], currentSum + grid[r][i]))                    

        #         case2 = max(ans, f(r + 1, previous, currentSum))
        #         ans = max(case1, case2)
        #         results = max(results, ans)
            
        #     dp[(r, ",".join(previous))] = ans

        #     return ans
        # return f(0, [], 0)

    
grid = [[1,2,3],[4,3,2],[1,1,1]] # 8
# grid = [[8,7,6],[8,3,2]] # 15
# grid = [[5],[7],[19],[5]] # 31
# grid = [[5,5],[5,5],[11,5]] # 16
# grid = [[36,36,36,39,36,21],[36,36,36,36,7,6],[29,9,80,50,93,48],[36,93,36,80,9,80],[74,36,36,6,21,32],[36,70,39,2,17,30],[40,4,80,50,85,6],[17,93,6,66,6,39]]
# grid = [[92,11,45,88,38,13,65,85],[52,83,3,14,82,51,27,59],[65,69,99,27,7,70,39,43],[43,46,22,19,75,70,57,50],[54,36,91,80,74,43,62,61],[35,45,19,32,92,50,93,88],[60,15,93,10,89,32,51,11],[82,66,42,61,78,94,66,7],[75,56,49,78,81,61,79,50]]
print(Solution().maxScore(grid))