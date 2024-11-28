from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #### RECURSION (problems's test cases seem to have changed. This approach without memoiz beats 98% O.O)
        # results = []
        # def f(substring, currentSplit):
        #     nonlocal results
        #     if len(substring) == 0:
        #         results.append(" ".join(currentSplit))
        #         return
        #     n = len(substring)
        #     for i in range(n):
        #         if substring[:i+1] in wordDict:
        #             f(substring[i+1:], currentSplit + [substring[:i+1]])

        # f(s, [])
        # return results
        
        ### DP BOTTOM UP
        n = len(s)
        dp = [[] for i in range(n + 1)]

        for i in range(n, -1,-1):
            valids = []
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    if j == n - 1:
                        valids.append(s[i:j+1])
                    else:
                        for substring in dp[j + 1]:
                            valids.append(s[i:j+1] + ' ' + substring)
            dp[i] += valids

        return dp[0]


s, wordDict = "catsanddog", ["cat","cats","and","sand","dog"] # ["cats and dog","cat sand dog"]
s, wordDict = "pineapplepenapple", ["apple","pen","applepen","pine","pineapple"] # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
s, wordDict = "catsandog", ["cats","dog","sand","and","cat"] # []
print(Solution().wordBreak(s, wordDict))