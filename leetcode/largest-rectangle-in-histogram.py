from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = []
        right = deque([])
        stack = []
        for i, h in enumerate(heights):
            # print(i, h, left)
            if len(stack) == 0 or (stack and stack[-1][0] <= h):
                stack.append((h, i))
            
            left.append(stack[-1])
            # if len(left) == 0 or (left and left[-1][0] <= h):
            #     left.append((h, i))            
            # else:
            #     while left and left[-1][0] > h:
            #         left.pop()
            #     left.append((h, i))

        # for i in range(n - 1, - 1, -1):            
        #     h = heights[i]
        #     # print(i, h, right)
        #     if len(right) == 0 or (right and right[0][0] < h):
        #         right.append((h, i))
        #     else:
        #         j = 0
        #         while j < len(right) - 1 and right[j][0] > h:
        #             j += 1
        #         right.append(right[j])

        print(left)
        print(right)
        result = 0

        # for i in range(n):
        #     result = max(result, abs((right[i][1] - left[i][1] + 1)) * heights[i])

        return result

heights = [2,1,5,6,2,3]
heights = [2,1,5,6,3,2]
print(Solution().largestRectangleArea(heights))