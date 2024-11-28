from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, down = 0, len(matrix) - 1
        row = 0
        while top <= down:
            mid = (top + down) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                top = mid + 1
        
        nums = matrix[row]
        print('found matrix', nums)
        left, right = 0, n - 1
        print(left, right)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        print(mid)
        return nums[mid] == target
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#true
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
#false
# matrix = [[1,3]]
# target = 3
#true

print(Solution().searchMatrix(matrix, target))