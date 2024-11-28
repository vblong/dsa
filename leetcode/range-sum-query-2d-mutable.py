from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.build(nums, 0, self.n-1, 0)

    def build(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, left, mid, 2*index+1)
        self.build(nums, mid + 1, right, 2*index+2)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

    def query(self, left, right, index, qLeft, qRight):
        if left > qRight or right < qLeft:
            return 0
        if left >= qLeft and right <= qRight:
            return self.tree[index]
        mid = (left + right) // 2
        return self.query(left, mid, 2*index+1, qLeft, qRight) + self.query(mid +1, right, 2*index+2, qLeft, qRight)

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
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]
        
    
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.segmentTrees = []
        self.m, self.n = len(matrix), len(matrix[0])
        for row in matrix:
            self.segmentTrees.append(SegmentTree(row))

    def update(self, row: int, col: int, val: int) -> None:
        self.segmentTrees[row].update(0, self.n-1, 0, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1):
            res += self.segmentTrees[row].query(0, self.n-1, 0, col1, col2)
        return res


# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))