from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.build(nums, 0, self.n - 1, 0)

    def build(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return
        
        mid = (left + right) // 2
        self.build(nums, left, mid, 2*index+1)
        self.build(nums, mid+1, right, 2*index+2)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index +2]

    def q(self, left, right):
        return self.query(0, self.n-1, 0, left, right)
    
    def query(self, left, right, index, qLeft, qRight):
        if right < qLeft or left > qRight: return 0
        if left >= qLeft and right <= qRight:
            return self.tree[index]
        mid = (left + right) // 2
        sumLeft = self.query(left, mid, 2*index +1, qLeft, qRight)
        sumRight = self.query(mid+1, right, 2*index +2, qLeft, qRight)
        return sumLeft + sumRight
        
    def update(self, left, right, index, pos):
        if pos < left or pos > right: return

        if left == right:
            self.tree[index] += 1
            return

        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2*index+1, pos)
        else:
            self.update(mid+1, right, 2*index+2, pos)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        minN, maxN = min(nums), max(nums)

        arr = [0] * (2 * 10000 + 1)
        st = SegmentTree(arr)
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            st.update(0, st.n-1, 0, nums[i] + minN)
            # print(st.tree)
            res[i] = st.q(0, nums[i]+minN-1)
        return res

nums = [5,2,6,1] #Output: [2,1,1,0] 
print(Solution().countSmaller(nums))