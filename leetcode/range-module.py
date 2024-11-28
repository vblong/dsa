class STNode:
    def __init__(self, l, r, value) -> None:
        self.start, self.end = l, r
        self.val = value
        self.left = None
        self.right = None

class RangeModule:

    def __init__(self):
        # self.root = STNode(0, 1e9+1, False)
        self.root = STNode(0, 10**9+1, False)

    def update(self, node: STNode, left: int, right: int, value: bool):        
        # if node.start >= right or node.end <= left: 
        #     return node.val
        # if node.start >= left and node.end <= right:
        #     node.val = value
        #     return value
        # mid = (node.start + node.end) // 2
        # if not node.left:
        #     node.left = STNode(node.start, mid, node.val)
        #     node.right = STNode(mid + 1, node.end, node.val)

        # left = self.update(node.left, left, right, value)
        # right = self.update(node.right, left, right, value)
        # node.val = left and right
        # return node.val
        if node.start >= left and node.end <= right:
            node.val = value
            node.left = node.right = None
            return value
        if left >= node.end or right <= node.start:
            return node.val
        mid = node.start + (node.end - node.start) // 2 #(node.start + node.end) // 2
        if not node.left:
            node.left = STNode(node.start, mid, node.val)
            node.right = STNode(mid, node.end, node.val)
        leftVal = self.update(node.left, left, right, value)
        rightVal = self.update(node.right, left, right, value)
        node.val = leftVal and rightVal
        return node.val
        
        
    # def updateOne(self, node: STNode, pos: int, val: bool):
    #     if pos < node.start or pos > node.end: return
    #     if node.start == node.end:
    #         node.val = val
    #         return
        
    #     mid = (node.start + node.end) // 2
    #     if not node.left:
    #         node.left = STNode(node.start, mid, node.val)
    #         node.right = STNode(mid+1, node.end, node.val)

    #     self.updateOne(node.left, pos, val)
    #     self.updateOne(node.right, pos, val)
    #     node.val = node.left.val and node.right.val

    def addRange(self, left: int, right: int) -> None:
        self.update(self.root, left, right, True)
        # for i in range(left, right):
        #     self.updateOne(self.root, i, True)
        # self.debug()

    def removeRange(self, left: int, right: int) -> None:
        self.update(self.root, left, right, False)
        # for i in range(left, right):
        #     self.updateOne(self.root, i, False)
        # self.debug()
    
    def query(self, node: STNode, left: int, right: int):
        if (node.start >= left and node.end <= right) or not node.left:
            return node.val
        mid = (node.start + node.end) // 2
        if right <= mid:
            return self.query(node.left, left, right)
        elif left >= mid:
            return self.query(node.right, left, right)
        else:
            return self.query(node.left, left, right) and self.query(node.right, left, right)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(self.root, left, right)

    def debug(self):
        node = self.root
        def dfs(node):
            if not node:
                return
            print(f'[{node.start}..{node.end}]: {node.val}')
            dfs(node.left)
            dfs(node.right)
        dfs(node)
    


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
# obj.addRange(10, 20)
# obj.removeRange(14, 16)
# print(obj.queryRange(10, 14)) # True
# print(obj.queryRange(13, 15)) # False
# print(obj.queryRange(16, 17)) # True


#########
# obj.addRange(10, 180)
# obj.addRange(150, 200)
# obj.addRange(250, 500)
# print(obj.queryRange(50, 100))
# print(obj.queryRange(180, 300))
# print(obj.queryRange(600, 1000))
# obj.removeRange(50, 150)
# print(obj.queryRange(10, 49))



#######
print(obj.queryRange(2, 7)) # F
print(obj.queryRange(4, 5)) # F
obj.removeRange(6, 7)
obj.addRange(2, 9)
print(obj.queryRange(1, 5)) # F
obj.removeRange(6, 10)
obj.addRange(6, 8)
obj.removeRange(9, 10)
obj.addRange(2, 7)
