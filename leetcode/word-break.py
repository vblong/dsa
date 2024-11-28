class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
     
        def dp(i):
            if i < 0:
                return True
            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            return False

        return dp(len(s) - 1)
    

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"] # false
# s = "leetcode" 
# wordDict = ["leet","code"] # true
# s = "applepenapple" 
# wordDict = ["apple","pen"] # true
# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"] # true
# s = "cars"
# wordDict = ["car","ca","rs"] # true
print(Solution().wordBreak(s, wordDict))