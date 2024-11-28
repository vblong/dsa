"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        p2 = None
        newHead = None
        nodeIndices = {}
        indicesNodes = {}
        index = 0
        while p:
            newNode = Node(p.val, None, None)
            if not newHead:
                newHead = newNode
                p2 = newNode
            else:
                p2.next = newNode
                p2 = p2.next
            nodeIndices[p] = index
            indicesNodes[index] = newNode
            index += 1
            p = p.next
        
        p = head
        p2 = newHead
        while p:
            originalRandomIndex = nodeIndices[p.random] if p.random else None
            if originalRandomIndex is not None:
                p2.random = indicesNodes[originalRandomIndex]
            else:
                p2.random = None
            p = p.next
            p2 = p2.next
        return newHead