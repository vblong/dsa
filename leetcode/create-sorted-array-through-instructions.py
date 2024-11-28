from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.lazy = [0] * 4 * self.n
        # self.build(nums, 0, self.n-1, 0)

    def build(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, left, mid, 2*index+1)
        self.build(nums, mid+1, right, 2*index+2)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

    # logN
    def query(self, left, right, index, qLeft, qRight):
        if left > qRight or right < qLeft: return 0
        if left >= qLeft and right <= qRight: return self.tree[index]
        mid = (left + right) // 2
        return self.query(left, mid, 2*index+1, qLeft, qRight) + self.query(mid+1, right, 2*index+2, qLeft, qRight)

    def lazyProcess(self, left, right, index):
        if self.lazy[index] != 0:
            self.tree[index] += self.lazy[index] * (right - left + 1)
            if left != right:
                self.lazy[2*index+1] += self.lazy[index]
                self.lazy[2*index+2] += self.lazy[index]
            self.lazy[index] = 0
    # logN
    def inc(self, left, right, index, pos):
        self.lazyProcess(left, right, index)
        
        if pos < left or pos > right: return
        if left == right:
            self.tree[index] += 1
            return
        mid = (left + right) // 2
        if pos <= mid:
            self.inc(left, mid, 2*index+1, pos)
        else:
            self.inc(mid+1, right, 2*index+2, pos)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # 6:16
        MOD = 1000000000+7
        count = [0] * (100001)
        st = SegmentTree(count)
        res = 0
        for i in instructions:
            res += (min(st.query(0, st.n-1, 0, 0, i - 1), st.query(0, st.n-1, 0, i+1, 100001)) % MOD)
            st.inc(0, st.n-1, 0, i)

        return res % MOD



instructions = [1,5,6,2] # 1
instructions = [1,2,3,6,5,4] # 3
print(Solution().createSortedArray(instructions))
