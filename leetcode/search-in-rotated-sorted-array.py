from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[right] < nums[left]:
                if target > nums[right]:
                    while mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                        mid += 1
                    right = mid
                else:
                    left = mid +1
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
nums, target = [4,5,6,7,0,1,2], 0 # 4
nums, target = [4,5,6,7,0,1,2], 3 # -1
nums, target = [1], 0 #-1
nums, target = [3,1], 2 # -1
nums, target = [3,1], 1 # 1
nums, target = [1], 1 # 0
nums, target = [1], 2 # -1
nums, target = [4,5,6,7,8,1,2,3], 8 # 4
nums, target = [5,1,3], 4
print(Solution().search(nums, target))