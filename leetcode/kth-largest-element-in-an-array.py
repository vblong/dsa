from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # TC O(NlogN)
        # SC: O(N)
        # nums.sort()
        # return nums[len(nums) - k]
        minHeap = []
        for n in nums:
            heappush(minHeap, n)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]


nums = [3,2,1,5,6,4]
k = 2
# 5
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# 4
print(Solution().findKthLargest(nums, k))

heapify(nums)
print('ater', nums)