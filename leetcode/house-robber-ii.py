from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = {}
        # def f(i, visited):
        #     if i >= n:
        #         return 0
            
        #     if i == n - 1 and 0 in visited:
        #         return 0
        #     if (i, tuple(visited)) in memo:
        #         return memo[(i, tuple(visited))]
        #     ans = max(nums[i] + f(i + 2, visited + [i]), f(i + 1, visited))
        #     memo[(i, tuple(visited))] = ans
        #     return ans
        
        # return f(0, [])

        def solve(slicedNums):
            n = len(slicedNums)
            dp = [0] * n
            for i in range(n -1, -1, -1):
                if i == n - 1:
                    dp[i] = slicedNums[i]
                elif i == n - 2:
                    dp[i] = max(slicedNums[i], slicedNums[i + 1])
                else:
                    dp[i] = max(dp[i + 1], slicedNums[i] + dp[i + 2])
            return dp[0]
        
        return max(solve(nums[1:]), solve(nums[:-1]))

nums = [2,3,2] # 3
# nums = [1,2,3,1] # 4
# nums = [1,2,3] # 3
nums = [94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]
print(Solution().rob(nums))
