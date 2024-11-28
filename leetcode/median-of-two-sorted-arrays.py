
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find out which one has more elements
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        n = len(A) + len(B)
        half = n // 2
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2
            # bMid = half - (mid - left + 1)
            bMid = half - mid - 2
            
            aLeft = A[mid] if mid >= 0 else -1e9
            aRight = A[mid+1] if mid + 1 < len(A) else 1e9
            bLeft = B[bMid] if bMid >= 0 else -1e9
            bRight = B[bMid+1] if bMid + 1 < len(B) else 1e9

            if bRight >= aLeft and aRight >= bLeft:
                if (len(A) + len(B)) % 2:
                    return min(aRight, bRight)
                return (min(aRight, bRight) + max(aLeft, bLeft)) / 2
            elif aLeft > bRight:
                right = mid - 1
            else:
                left = mid + 1
            # elif aRight > bLeft: 
            #     left = mid + 1
            # else:
            #     right = mid - 1
            # if A[aMid] > B[mid]:
            #     right = mid - 1
            # elif A[aMid-1] > B[mid+1]:
            #     left = mid + 1
            # else:
            #     break
        
nums1, nums2 = [1, 3], [2] # 2
nums1, nums2 = [1,2], [3,4] # 2.5
print(Solution().findMedianSortedArrays(nums1, nums2))
























# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:

        # A, B = nums1, nums2
        # if len(nums2) < len(nums1):
        #     A, B = B, A
        # half = (len(nums1) + len(nums2)) // 2

        # l, r = 0, len(A) - 1
        # while True:
        #     i = (l + r) // 2
        #     j = half - i - 2

        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

        #     if Aleft <= Bright and Bleft <= Aright:
        #         if (len(nums1) + len(nums2)) % 2:
        #             return min(Aright, Bright)
        #         return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        #     elif Aleft > Bright:
        #         r = i - 1
        #     else:
        #         l = i + 1

# Solution().findMedianSortedArrays([1, 3], [2])
