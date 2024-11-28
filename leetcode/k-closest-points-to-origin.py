import math
class Solution:
    def kClosest(self, points, k: int):
        def dist(x1, y1, x2, y2):
            return math.sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2))

        distances = []
        for p in points:
            distances.append((p, dist(0, 0, p[0], p[1])))
        # ######### BRUTE FORCE 
        # Idea: Tính tất cả khoảng cách của các điểm, sau đó sort tăng dần và lấy k điểm gần nhất.
        # Time: O(n + k)
        # Space: O(n)        
        # distances.sort(key=lambda x:x[1])        

        # ######### QUICK SELECT
        # Idea:
        # Time:
        # Space:
        def partition(nums, left, right):
            print('partitioning', nums, left, right)    
            pivot = nums[right]
            i = left - 1
            for j in range(left, right):
                if nums[j][1] < pivot[1]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
                    
            nums[i + 1], nums[right] = nums[right], nums[i + 1]
            return i+1

        def quickSelect(dists, left, right, k):
            print('quickSelect', left, right, k)
            if left < right:
                partitionIndex = partition(dists, left, right)
                if (partitionIndex - left == k - 1): 
                    return
        
                if (partitionIndex - left > k - 1): 
                    quickSelect(dists, left, partitionIndex - 1, k) 
                else:
                    quickSelect(dists, partitionIndex + 1, right, k - partitionIndex + left - 1) 

        quickSelect(distances, 0, len(distances) - 1, k)

        # Chuyển thành kết quả
        result = []
        for i in range(k):
            result.append(distances[i][0])
        return result
    
points, k = [[1,3],[-2,2]], 1
points, k = [[3,3],[5,-1],[-2,4]], 2
print(Solution().kClosest(points, k))