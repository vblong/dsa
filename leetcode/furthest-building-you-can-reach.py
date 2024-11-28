from heapq import heappop, heappush
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heappush(maxHeap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heappop(maxHeap)
        return i


heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
# 4
print(Solution().furthestBuilding(heights, bricks, ladders))