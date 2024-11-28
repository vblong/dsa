class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:        
        def count(nums, diff):
            left = 0
            count = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > diff:
                    left += 1
                count += (right - left)
            return count

        nums.sort()
        left = 0
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            cnt = count(nums, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return right
    
nums, k = [1,3,1], 1 # 0, sorted = 1 1 3, diff = [0, 2, 2]
print(Solution().smallestDistancePair(nums, k))