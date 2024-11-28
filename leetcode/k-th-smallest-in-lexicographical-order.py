from collections import deque


class TrieNode:
    def __init__(self, digit, val):
        self.digit = digit
        self.val = val
        self.children = {}
        self.isNum = False

    def __str__(self):
        if self.digit and self.val:
            return f'Digit: {self.digit}, val: {self.val}'
        return ''

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # sort (memory limit due to save string array)
        # res = [(str)(i) for i in range(1, n +1)]
        # res.sort()
        # print(res)
        # return (int)(res[k-1])

        ######### TRIE
        root = {}
        q = deque([])
        for i in range(1, 10):
            if i <= n:
                newNode = TrieNode(i, i)
                root[i] = newNode
                q.append(newNode)
        while q:
            node = q.popleft()
            val = node.val
            # print('----- at', val, 'adding ', end='')
            for i in range(10):
                if val * 10 + i <= n:
                    newNode = TrieNode(i, val * 10 + i)
                    # print(newNode.val, end=', ')
                    node.children[i] = newNode
                    q.append(newNode)
            # print()
        
        q2 = deque(root.values())
        cnt = 0
        while q2:
            node = q2.popleft()
            # print('blem blem', node)
            cnt += 1
            if cnt == k: return node.val
            st = []
            for child in node.children.values():
                # print('getting', child.digit, child.val)
                st.append(child)
            for rChild in reversed(st):
                q2.appendleft(rChild)
        return 0
n, k = 13, 2 # 10
n, k = 100, 10 # 17
n, k = 4289384, 1922239 
print(Solution().findKthNumber(n, k))