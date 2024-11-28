from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()
        maxN = max(piles)
        left = 1
        right = maxN
        

        def getDays(k):
            days = 0
            for p in piles:
                if p <= k:
                    days += 1
                else:
                    if p % k == 0:
                        days += p // k
                    else:
                        days += (p // k) + 1
            return days
        
        results = right
        while left <= right:
            mid = (left + right) // 2
            days = getDays(mid)
            # print(left, right, 'k =', mid, '===> ', days, 'days')
            if days <= h:
                results = min(results, mid)
                right = mid - 1
            elif days > h:
                left = mid + 1
        return results
            

piles, h = [3,6,7,11], 8 # 4
piles, h = [30,11,23,4,20], 5 # 30
piles, h = [30,11,23,4,20], 6 # 23
piles, h = [312884470], 312884469 # 2
piles, h = [1_000_000_000], 2 # 500000000
print(Solution().minEatingSpeed(piles, h))