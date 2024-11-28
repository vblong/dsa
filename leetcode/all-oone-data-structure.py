class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None
        self.cnt = 1

class AllOne:

    def __init__(self):
        self.head = Node("")
        self.head.cnt = -1
        self.tail = Node("")
        self.tail.cnt = -1
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        if key not in self.map:
            node = Node(key)
            first = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = first
            first.prev = node
            self.map[key] = node
        else:
            node = self.map[key]
            node.cnt += 1

            while True:
                node = self.map[key]
                nextNode = node.next
                if node.cnt > nextNode.cnt and nextNode.cnt != -1:
                    self.swap(node, nextNode)
                else:
                    break
        print('increase', key)
        self.debug()

    def dec(self, key: str) -> None:
        if key not in self.map:
            return ""
        node = self.map[key]
        node.cnt -= 1
        if node.cnt == 0:
            nextNode, prevNode = node.next, node.prev
            nextNode.prev = prevNode
            prevNode.next = nextNode
            del self.map[key]
        else:
            while True:
                # node = self.map[key]
                prevNode = node.prev
                print(node.cnt, prevNode.cnt)
                if node.cnt < prevNode.cnt and prevNode.cnt != -1:
                    self.swap(prevNode, node)
                else:
                    break
        print('decrease', key)
        self.debug()

    def swap(self, node1, node2):
        prevN = node1.prev
        nextN = node2.next

        # connect node 2 and prevNode
        prevN.next = node2
        node2.prev = prevN

        # connect node 1 & nextNode
        node1.next = nextN
        nextN.prev = node1

        node1.prev = node2
        node2.next = node1

        
    def getMaxKey(self) -> str:
        print('getMax: ', self.tail.prev.val)
        return self.tail.prev.val

    def getMinKey(self) -> str:
        print('getMin: ', self.head.next.val)
        return self.head.next.val

    def debug(self):
        cur = self.head
        while cur:
            print(f'{cur.val} ({cur.cnt}) -> ', end = '')
            cur = cur.next
        print()
        


# Your AllOne object will be instantiated and called as such:
# ["dec","getMaxKey","dec","inc","getMaxKey","inc","inc","dec","dec","dec","dec","getMaxKey","inc","inc","inc","inc","inc","inc","getMaxKey","getMinKey"]
# [["leet"],[],["ds"],["hello"],[],["hello"],["hello"],["world"],["leet"],["code"],["ds"],[],["new"],["new"],["new"],["new"],["new"],["new"],[],[]]
obj = AllOne()
obj.inc("hello")
obj.inc("world")
obj.inc("leet")
obj.inc("code")
obj.inc("ds")
obj.inc("leet")
print(obj.getMaxKey()) # leet
obj.inc("ds")
obj.dec("leet")