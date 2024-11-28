from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # (sumM + x) / (m + n) = mean =>
        sumM = sum(rolls)
        m = len(rolls)
        x = (mean * (m + n)) - sumM
        print(sumM, m, n, x)
        if x / n > 6 or x /n < 1:
            return []
        
        if x % n == 0:
            return [x // n] * n
            
        div = x // n
        results = [div] * n
        rem = x % n
        k = 0
        
        while rem:
            if results[k] + rem > 6:
                rem -= (6-results[k])
                results[k] = 6
                k += 1
            else:
                results[k] += rem
                break
            if k > n-1:
                return []

        print(rem, div)
        return results
    
    
rolls, mean, n = [1,5,6], 3, 4 # [2,2,2,3]
# rolls, mean, n = [3,2,4,3], 4, 2 # [6,6]
# rolls, mean, n = [1,2,3,4], 6, 4 # []
# rolls, mean, n = [1], 3, 1 # [5]
# rolls, mean, n = [1, 2, 3, 4], 6, 4 # []
# rolls, mean, n = [4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40 # [4,4,4,4,4,4,5,5,4,4,4,5,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5]
print(Solution().missingRolls(rolls, mean, n))