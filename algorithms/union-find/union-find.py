class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def query(self, x, y):
        return self.find(x) == self.find(y)
    

obj = UnionFind(10)
obj.union(1, 2)
print(obj.query(1, 2))
print(obj.query(3, 2))
obj.union(2, 3)
print(obj.query(3, 2))
print(obj.find(2))
