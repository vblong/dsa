from typing import List

class SegTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(nums, 0, self.n-1, 0)
        
    def build(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return 
        mid = (left + right) // 2
        self.build(nums, left, mid, 2*index+1)
        self.build(nums, mid+1, right, 2*index+2)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

    def updateRange(self, left, right, index, qLeft, qRight):
        self.process(left, right, index)
        if left > qRight or right < qLeft: return
        if left >= qLeft and right <= qRight:
            self.tree[index] = (right - left + 1) - self.tree[index]
            if left != right:
                self.lazy[2*index+1] ^= 1
                self.lazy[2*index+2] ^= 1
            return
        mid = (left + right) // 2
        self.updateRange(left, mid, 2*index+1, qLeft, qRight)
        self.updateRange(mid+1, right, 2*index+2, qLeft, qRight)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

    def process(self, left, right, index):
        if self.lazy[index] != 0:
            self.tree[index] = (right - left + 1) - self.tree[index]
            if left != right:
                self.lazy[2*index+1] ^= 1
                self.lazy[2*index+2] ^= 1
            self.lazy[index] = 0

    def query(self, left, right, index, qLeft, qRight):
        if left > qRight or right < qLeft: return 0
        if left >= qLeft and right <= qRight:
            return self.tree[index]
        mid = (left + right) // 2
        return self.query(left, mid, 2*index+1, qLeft, qRight) + self.query(mid+1, right, 2*index+2, qLeft, qRight)

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        st = SegTree(nums1)
        sum2 = sum(nums2)
        res = []

        for q, l, r in queries:
            if q == 1:
                print("update", q, l ,r)
                st.updateRange(0, st.n-1, 0, l, r)
            elif q == 2:
                sum2 += (st.query(0, st.n-1, 0, 0, st.n-1) * l)
            else:
                res.append(sum2)

        return res
    
nums1, nums2, queries = [1,0,1], [0,0,0], [[1,1,1],[2,1,0],[3,0,0]] # [3]
nums1, nums2, queries = [1], [5], [[2,0,0],[3,0,0]] # [5]
nums1, nums2, queries = [1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0], [7,17,2,13,35,23,47,45,40,23,13,37,0,9,21,50,45,21,2,10,37], [[2,13,0],[3,0,0],[1,9,10],[2,24,0],[1,1,10],[1,16,16],[2,13,0],[2,10,0],[2,4,0],[1,17,20]] # [5]
print(Solution().handleQuery(nums1, nums2, queries))