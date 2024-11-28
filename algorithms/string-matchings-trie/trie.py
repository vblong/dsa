from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int = 0) -> None:
        current = self.root
        for character in key:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.isWord = True
        current.value = val

    def sum(self, prefix: str) -> int:
        totalSum = 0
        
        current = self.root
        for character in prefix:
            if character not in current.children:
                return 0
            current = current.children[character]
        totalSum += current.value
        # print('okay here it is', totalSum)
        # print('next is', current.children['p'].value)
        queue = deque()
        for key, node in current.children.items():
            queue.append(node)
        while queue:
            current = queue.popleft()
            # print('current childs are ', current.children, current.children.keys())
            totalSum += current.value
            for k in current.children.keys():
                queue.append(current.children[k])

        return totalSum


    def search(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current and current.isWord

    def startsWith(self, prefix):
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# trie = MapSum()
# trie.insert("apple")
# print(trie.search("apple"))   # return True
# print(trie.search("app"))     # return False
# print(trie.startsWith("app")) # return True
# trie.insert("app")
# print(trie.search("app")) # return True

mapSum = MapSum()
mapSum.insert("apple", 3); 
print(mapSum.startsWith("ap"))
print(mapSum.sum("ap"))  # return 3 (apple = 3)
mapSum.insert("app", 2)
print(mapSum.sum("ap"))  # return 5 (apple + app = 3 + 2 = 5)