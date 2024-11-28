class Solution:
    def minFlips(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])        
        single = 0 # 1 0
        double = 0 # 1 1

        res = 0
        for i in range(m // 2):
            for j in range(n // 2):
                ones = grid[i][j] +  grid[m-i-1][j] + grid[i][n-j-1] + grid[m-i-1][n-j-1]
                res += min(ones, 4 - ones)

            # middle col
            if n % 2 == 1:
                print('yeah')
                cnt = grid[i][n//2] + grid[m-i-1][n//2]
                single += (cnt == 1)
                double += (cnt == 2)

        # middle row
        if m % 2 == 1:
            print("hell ye")
            for i in range(n // 2):
                cnt = grid[m//2][i] + grid[m//2][n-i-1]
                print('cnt is', cnt)
                single += (cnt == 1)
                double += (cnt == 2)


        print(res, single, double)
        if m % 2 and n % 2:
            res += (grid[m//2][n//2] == 1)

        if double % 2 == 0 or single > 0:
            res += single
        else:
            if single > 0:
                res += single
            else:
                res += 2
        return res
        

grid = [[1,0,0],[0,1,0],[0,0,1]] # 3
grid = [[1],[1]] # 0
grid = [[1,1]] # 0
print(Solution().minFlips(grid))