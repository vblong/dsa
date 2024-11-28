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
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # arr = [0 for i in range(max(nums) + 1)]
        # print('first arr', arr)
        # st = SegmentTree(arr)
        # print('initial state', st.tree)
        # for num in nums:
        #     maxLength, maxNum = st.query(0, st.n-1, 0, 0, num-1)
        #     print('at num=', num, maxLength, maxNum)
        #     if abs(num - maxNum) <= k or maxLength == 0:
        #         print('yes update')
        #         st.update(0, st.n-1, 0, num, maxLength + 1)
        #     else:
        #         st.update(0, st.n-1, 0, num, maxLength)
        #     print('new state', st.tree)
        # return st.query(0, st.n-1, 0, 0, max(nums) + 1)[0]

        arr = [0] * (max(nums) + 1)
        st = SegmentTree(arr)
        for num in nums:
            maxLength = st.query(0, st.n-1, 0, num - k if num - k >= 0 else 0, num-1)
            st.update(0, st.n-1, 0, num, maxLength + 1)
        return st.query(0, st.n-1, 0, 0, st.n-1)
        
nums, k = [4,2,1,4,3,4,5,8,15], 3 # 5
# nums, k = [7,4,5,1,8,12,4,7], 5 # 4
# nums, k = [1,5], 1 # 1
# nums, k = [1,5], 3 # 1
# nums, k = [1,3,3,4], 1 # 2
print(Solution().lengthOfLIS(nums, k))