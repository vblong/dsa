from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * 4 * self.n # sum tree
        self.build(nums, 0, self.n-1, 0)

    def build(self, nums, left, right, index):
        if left == right: 
            self.tree[index] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, left, mid, 2*index+1)
        self.build(nums, mid+1, right, 2*index+2)
        self.tree[index] = max(self.tree[2*index+1], self.tree[2*index+2])

    def query(self, left, right, index, qLeft, qRight):
        if left > qRight or right < qLeft: return 0

        if qLeft <= left and right <= qRight:
            return self.tree[index]
        mid = (left + right) // 2
        resLeft = self.query(left, mid, 2*index+1, qLeft, qRight)
        resRight = self.query(mid+1, right, 2*index+2, qLeft, qRight)
        return max(resLeft, resRight)

    def update(self, left, right, index, pos, val):
        if pos < left or pos > right: return
        if left == right:
            self.tree[index] = val
            return
        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2*index+1, pos, val)
        else:
            self.update(mid+1, right, 2*index+2, pos, val)
        self.tree[index] = max(self.tree[2*index+1], self.tree[2*index+2])


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [0] * (2 * 10000 + 1)
        # for n in nums: arr[n + 10000] += 1
        
        st = SegmentTree(arr)
        for num in nums:
            maxlength = st.query(0, st.n-1, 0, 0, num + 10000 - 1)
            print('maxL', maxlength)
            st.update(0, st.n-1, 0, num + 10000, maxlength + 1)
        print(max(st.tree))
        return st.query(0, st.n-1, 0, 0, max(nums) + 10000 + 1)


nums = [10,9,2,5,3,7,101,18] # 4
nums = [0,1,0,3,2,3] # 4
nums = [7,7,7,7,7,7,7] # 1
nums = [4,10,4,3,8,9] # 3
nums = [-10000] # 1
print(Solution().lengthOfLIS(nums))