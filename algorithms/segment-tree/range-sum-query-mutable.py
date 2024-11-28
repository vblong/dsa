from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
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
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

    def getSum(self, left, right, index, qLeft, qRight):
        if left > qRight or right < qLeft: return 0
        if left >= qLeft and right <= qRight: return self.tree[index]

        mid = (left + right) // 2
        sumLeft = self.getSum(left, mid, 2*index+1, qLeft, qRight)
        sumRight = self.getSum(mid + 1, right, 2*index+2, qLeft, qRight)
        return sumLeft + sumRight
    
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
class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)    

    def update(self, index: int, val: int) -> None:
        self.st.update(0, self.st.n - 1, 0, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.getSum(0, self.st.n-1, 0, left, right)


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2)) # 9
print(obj.update(1, 2))
print(obj.sumRange(0, 2)) # 8