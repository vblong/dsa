class RandomizedSet:
    # Idea: 
    # - xây dựng hashTable với kích thước cố định (vd 100)
    # - hash value của mỗi giá trị mới được tính bằng cách chia modulo cho kích thước của hashTable
    # - Tạo thêm 1 set `keys` dùng lưu trữ những keys đang có trong class
    # - Mỗi lần hàm insert() được gọi thì key (hoặc hash value) sẽ được đưa vào set `keys`
    # - Tương tự mỗi lần hàm remove() được gọi thì key cũng sẽ được bỏ ra khỏi set `keys` nếu giá trị tại key đó trong hashtable là rỗng
    # - Khi hàm getRandom() được gọi thì sử dụng hàm random.choice để lựa chọn ngẫu nhiên 1 key, sau đó lại dùng
    # hàm random.choice() để lấy ngẫu nhiên 1 value của key trong hashtable này
    # Time: O(1)
    # Space: O(N). N = capacity
    def __init__(self):
        self.capacity = 100
        self.hashTable = [[] for i in range(self.capacity)]
        self.keys = set()

    def insert(self, val: int) -> bool:
        keyIndex = val % self.capacity
        present = False
        for i in range(len(self.hashTable[keyIndex])):
            if self.hashTable[keyIndex][i] == val:
                present = True
                break
        if present: 
            return False

        self.keys.add(keyIndex)
        self.hashTable[keyIndex].append(val)
        return True

    def remove(self, val: int) -> bool:
        keyIndex = val % self.capacity
        for i in range(len(self.hashTable[keyIndex])):
            if self.hashTable[keyIndex][i] == val:
                del self.hashTable[keyIndex][i]
                if len(self.hashTable[keyIndex]) == 0:
                    if keyIndex in self.keys:
                        self.keys.remove(keyIndex)
                return True
        return False

    def getRandom(self) -> int:
        keyIndex = random.choice(list(self.keys))
        return random.choice(self.hashTable[keyIndex])



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()