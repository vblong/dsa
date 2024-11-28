class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        track = [[(0, 0, "") for _ in range(n+1)] for _ in range(m+1)]
        si, sj = -1, -1
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    track[i][j] = (0, 0, "")
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if si == -1 and sj == -1:
                        si, sj = i-1, j-1
                    ti, tj, t = track[i-1][j-1]
                    track[i][j] = (i-1, j-1, t + s1[i-1])
                else:
                    if dp[i-1][j] > dp[i][j-1]:
                        track[i][j] = track[i-1][j]
                    else:
                        track[i][j] = track[i][j-1]
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        lcs = track[m][n][2]
        print(lcs)
        i, j = 0, 0
        res = ""
        for char in lcs:
            while s1[i] != char:
                res += s1[i]
                i += 1
            while s2[j] != char:
                res += s2[j]
                j += 1
            res += char
            i += 1
            j += 1
        while i < len(s1):
            res += s1[i]
            i += 1
        while j < len(s2):
            res += s2[i]
            j += 1

        print(res)
        # for r in track:
        #     print(r)
        # print('---', si, sj)
        # i, j, _ = track[m][n]
        # previ, prevj = m, n
        # trackStr = ""
        # scs = ""
        # while i and j:
            
        #     for ii in range(previ-1, i, -1):
        #         scs += s1[ii]
        #     for jj in range(prevj-1, j,-1):
        #         scs += s2[jj]
        #     scs += s1[i]
        #     previ, prevj = i, j
        #     trackStr += s1[i]
        #     i, j, _ = track[i][j]
        # print('gleich', scs, previ, prevj)
        # if previ-1 > 0:
        #     for ii in range(previ-1, -1, -1):
        #         scs += s1[ii]
        # if prevj-1 > 0:
        #     for jj in range(prevj-1, -1, -1):
        #         scs += s2[jj]
        # print("".join(reversed(trackStr)))
        # print('hey', "".join(reversed(scs)), previ, prevj)
        return dp[m][n]
s1, s2 = "abac", "cab" # => cabac
# s1, s2 = "bacdez", "facex" # => bfacdexz
# s1, s2 = "xayczew", "fagchei" # => xfaygczhewi
# s1, s2 = "bcacaaab", "bbabaccc" # => bbabcacccaaab

# s1, s2 = "adbc", "cab" # cadbc
print(Solution().longestCommonSubsequence(s1, s2))