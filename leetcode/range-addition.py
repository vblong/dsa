from typing import List

class SegmentTree:
    def __init__(self, length) -> None:
        self.n = length
        self.tree = [0] * 4 * length
        self.lazy = [0] * 4 * length

    def processPending(self, left, right, index):
        if self.lazy[index] != 0:
            self.tree[index] += self.lazy[index] * (right - left + 1)
            if left != right:
                self.lazy[2*index+1] += self.lazy[index]
                self.lazy[2*index+2] += self.lazy[index]
            self.lazy[index] = 0

    def query(self, left, right, index, qLeft, qRight):
        self.processPending(left, right, index)
        if left > qRight or right < qLeft: return 0

        if left >= qLeft and right <= qRight:
            return self.tree[index]
        
        mid = (left + right) // 2
        left = self.query(left, mid, 2*index+1, qLeft, qRight)
        right = self.query(mid+1, right, 2*index+2, qLeft, qRight)
        return left + right
    
    def updateRange(self, left, right, index, qLeft, qRight, inc):
        self.processPending(left, right, index)
        if left > qRight or right < qLeft: return 0

        if qLeft <= left and right <= qRight:
            self.lazy[index] += inc
            self.processPending(left, right, index)
            return 

        mid = (left + right) // 2
        self.updateRange(left, mid, 2*index+ 1, qLeft, qRight, inc)    
        self.updateRange(mid+1, right, 2*index+ 2, qLeft, qRight, inc)    
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        st = SegmentTree(length)

        for start, end, inc in updates:
            st.updateRange(0, length -1, 0, start, end, inc)
        
        res = []
        for i in range(length):
            res.append(st.query(0, length-1, 0, i, i))
        return res


length, updates = 5, [[1,3,2],[2,4,3],[0,2,-2]] # [-2,0,3,5,3]
print(Solution().getModifiedArray(length, updates))