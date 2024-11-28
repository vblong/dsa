class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        results = n
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                dp[i+1][i] = True
                results += 1
        # abcdedbdca

        for diff in range(2, n):
            for j in range(n-diff):
                if s[j] == s[j+diff]:
                    if dp[j+1][j+diff-1] == True:
                        dp[j][j + diff] = True
                        results += 1

        for r in dp:
            print(r)
        return results
        
s = "abc" # 3
# s = "aaa" # 6
print(Solution().countSubstrings(s))