class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ############ top-down / RECURSION + Cache
        # @cache
        # cache = {}
        # def f(s1, s2):
        #     if len(s1) == 0:
        #         return len(s2)
        #     if len(s2) == 0:
        #         return len(s1)
        #     if (s1, s2) in cache:
        #         return cache[(s1, s2)]

        #     if s1[0] == s2[0]:
        #         return f(s1[1:], s2[1:])
        #     else:
        #         insert = 1 + f(s1, s2[1:])
        #         delete = 1 + f(s1[1:], s2)
        #         replace = 1 + f(s1[1:], s2[1:])
        #         cache[(s1, s2)] = min(insert, delete, replace)
        #         return min(insert, delete, replace)
        # return f(word1, word2)

        ############# Bottom up - Tabulation
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        tracking = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                    tracking[i][j] = (i, j, 'insert ' + word2[j-1])
                elif j == 0:
                    dp[i][j] = i
                    tracking[i][j] = (i, j, 'delete ' + word1[i-1])
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    tracking[i][j] = (i-1,j-1, '')
                else:
                    delete = dp[i-1][j] +1
                    insert = dp[i][j-1] +1
                    replace = dp[i-1][j-1] +1
                    minN = min(delete, insert, replace)
                    if minN == delete:
                        tracking[i][j] = (i-1, j, 'delete ' + word1[i-1])
                    elif minN == insert:
                        tracking[i][j] = (i, j-1, 'insert' + word2[j-1])
                    else:
                        tracking[i][j] = (i-1, j-1, 'replace ' + word1[i-1] + ' with ' + word2[j-1] )
                    dp[i][j] = min(delete, insert, replace)
        steps = []
        ti, tj = m, n
        while ti and tj:
            ti, tj, interpret = tracking[ti][tj]
            steps.append(interpret)
        for s in reversed(steps):
            print(s)
        return dp[m][n]
word1, word2 = "horse", "ros" # 3
# word1, word2 = "intention", "execution" # 5
print(Solution().minDistance(word1, word2))