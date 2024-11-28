from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.lazy = [0] * 4 * self.n
        self.build_tree(nums, 0, self.n-1, 0) # range sum

    def build_tree(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return
        
        mid = (left + right) // 2
        self.build_tree(nums, left, mid, 2 * index + 1)
        self.build_tree(nums, mid+1, right, 2 * index + 2)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def querySum(self, left, right, index, qLeft, qRight):
        if qRight < left or qLeft > right:
            return 0
        
        if left >= qLeft and right <= qRight:
            return self.tree[index]
        
        mid = (left + right) // 2
        resLeft = self.querySum(left, mid, 2 * index + 1, qLeft, qRight)
        resRight = self.querySum(mid + 1, right, 2 * index + 2, qLeft, qRight)
        return resLeft + resRight

    def update(self, left, right, index, pos, val):
        if pos < left or pos > right:
            return
        
        if left == right:
            self.tree[index] = val
            return
        
        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2 * index + 1, pos, val)
        else:
            self.update(mid + 1, right, 2 * index + 2, pos, val)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def process_pending_node(self, left, right, index):
        if self.lazy[index] != 0:
            self.tree[index] += self.lazy[index] * (right - left + 1)
            if left != right:
                self.lazy[2*index + 1] += self.lazy[index]
                self.lazy[2*index + 2] += self.lazy[index]
            self.lazy[index] = 0
    
    def updateRange(self, left, right, index, qLeft, qRight, inc):
        self.process_pending_node(left, right, index)

        if qRight < left or qLeft > right: return 0

        if qLeft <= left and right <= qRight:
            self.lazy[index] += inc
            self.process_pending_node(left, right, index)
            return
        
        mid = (left + right) // 2
        self.updateRange(left, mid, 2*index + 1, qLeft, qRight, inc)
        self.updateRange(mid+1, right, 2*index + 2, qLeft, qRight, inc)
        self.tree[index] = self.tree[2*index + 1] + self.tree[2*index + 2]

data = [-6, 1, 3, 11, 0, 15, -1, 5, 9, 8]
st = SegmentTree(data)
print(st.tree)
print(st.querySum(0, len(data)-1, 0, 3, 4)) # 11
print(st.querySum(0, len(data)-1, 0, 3, 5)) # 26
st.update(0, len(data) - 1, 0, 4, 9)
print(st.querySum(0, len(data)-1, 0, 3, 4)) # 20