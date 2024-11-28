from collections import deque
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        def containsAll(chosen):
            for c in chosen:
                if c == 0:
                    return False
            return True
        merged = []
        k = len(nums)
        chosen = [0 for i in range(k)]
        for i, num in enumerate(nums):
            merged += [(i, n) for n in num]
        merged.sort(key=lambda x:x[1])
        minSize, minL, minR = 10**9, 0, 0
        print(merged)
        left = 0
        leftIdx, valLeft = merged[left]
        for right in range(len(merged)):
            rightIdx, valRight = merged[right]
            chosen[rightIdx] += 1
            while containsAll(chosen):
                # print(left)
                if valRight - valLeft < minSize:
                    minSize = valRight - valLeft
                    minL, minR = valLeft, valRight
                chosen[leftIdx] -= 1
                left += 1
                if left < len(merged):
                    leftIdx, valLeft = merged[left]
        return [minL, minR]

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]] # [20, 24]
nums = [[1,2,3],[1,2,3],[1,2,3]] # [1, 1]
nums = [[1]] # [1, 1]
print(Solution().smallestRange(nums))