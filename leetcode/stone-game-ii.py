class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # preSum = [0] * (n + 1)
        # preSum[0] = 0
        # for i in range(n):
        #     preSum[i + 1] = preSum[i] + piles[i]
        # # 1 indexed
        # def getSum(left, right):
        #     print('get sum of', left, right, '=',preSum[right] - preSum[left - 1])
        #     return preSum[right] - preSum[left - 1]
        dp = {}
        def f(i, m, aliceTurn):
            if i == len(piles):
                return 0
            if (i, m, aliceTurn) in dp:
                return dp[(i, m, aliceTurn)]
            result = 0 if aliceTurn else 1e9
            total = 0
            for X in range(1, 2 * m + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if aliceTurn:
                    result = max(result, total + f(i + X, max(m, X), not aliceTurn))
                else:
                    result = min(result, f(i + X, max(m, X), not aliceTurn))
            dp[(i, m, aliceTurn)] = result
            return result
        
        return f(0, 1, True)
    
piles = [2,7,9,4,4] # 10
piles = [1,2,3,4,5,100] # 104
print(Solution().stoneGameII(piles))