import string
from typing import List


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Solution:    
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        
        def insert(word: string):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWord = True
        
        def startsWith(word: string):
            cur = root
            for c in word:
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return True
        
        def search(word: string):
            cur = root
            for c in word:
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.isWord
        
        def dp(word: string):
            # print('dp', word)
            ans = 1e9
            for w in dictionary:
                findIdx = word.find(w)                
                if findIdx > -1:
                    rem = word[:findIdx] + word[findIdx + len(w):]
                    # print('found', w, 'gonna dp', rem)
                    ans = min(ans, dp(rem))
            if ans == 1e9:
                ans = len(word)
            return ans

        return dp(s)
        
        # for w in dictionary:
        #     insert(w)
            
        # w = ""
        # res = 0
        # i = 0
        # while i < len(s):
        #     w += s[i]
        #     if not startsWith(w):
        #         print(i, 'word', w, 'not found')
        #         pre = w[:-1]
        #         if not search(pre):
        #             res += len(pre)
        #             print('-->', pre, 'not found, res to', res)
        #         else:
        #             print('-->>', pre, 'found')
                    
        #         if not startsWith(s[i]):
        #             w = ""
        #             res += 1
        #             print('----', s[i], 'also not found, set w to "", res=',res)
        #         else:                    
        #             w = s[i]
        #             print('-->>>', w, 'found (startsWith), set word to', w, ', res =', res)
        #     i += 1
        # if not search(w):
        #     res += len(w)
        #     print('--->>>> final word', w, 'not found, res to', res)
        # return res
    
s, d = "leetscode", ["leet","code","leetcode"] # 1
s, d = "sayhelloworld", ["hello","world"] # 3
s, d = "dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"] # 7
s, d = "kngmktvcxrwubjzk", ["ktvc","pajp","x","emye","hde","haol","ubjz","tc","rb","kng","li","fph","d","rgrg"] # 4
s, d = "tpqojlnhenbzmqkqnxohmzakm", ["enbzm","yy","xqnjw","cxwgv","q","ras","ezc","nt","eq","j","chfw","v","ebh","tvwk","we","xhk","bumlw","czgy",
                                     "njrml","pl","cxg","ztg","mnvi","k","hslr","fwhrj","h","yqro","vpxyf","bps","nhuv","w","m","ln","nxoh","skiun",
                                     "qnqc","wtrwp","hl","ydbv","cv","a","tpqoj","umrj","nq","xadnx","emwv","dmuuw"] # 1
print(Solution().minExtraChar(s, d))