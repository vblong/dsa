class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def getMirror(num, oddNumber):
            res = num
            if oddNumber:
                num = num // 10
            while num:
                res = res * 10 + num % 10
                num = num // 10
            return res
        poss = []
        midPoint = len(n) // 2 - 1 if len(n) % 2 == 0 else len(n) // 2
        half = (int)(n[:midPoint + 1])

        poss.append(getMirror(half, len(n) % 2))
        poss.append(getMirror(half + 1, len(n) % 2))
        poss.append(getMirror(half - 1, len(n) % 2))
        poss.append(10 ** (len(n) - 1) - 1)
        poss.append(10 ** len(n) + 1)
        # print(poss)
        minDiff = 1e9   
        minPoss = 0
        for p in poss:
            if p == (int)(n):
                continue
            if abs(p - (int)(n)) < minDiff:
                minDiff = abs(p - (int)(n))
                minPoss = p
            elif abs(p - (int)(n)) == minDiff:
                minPoss = min(minPoss, p)
        return (str)(minPoss)
        # half = (len(n) // 2)
        # print(half)

        # case1 = (int)(getMirror(n, 0))
        # diff1 = abs(case1 - (int)(n))
        # case2 = (int)(getMirror(n, 1))
        # diff2 = abs(case2 - (int)(n))
        # case3 = (int)(getMirror(n, -1))
        # diff3 = abs(case2 - (int)(n))
        # case4 = (int)("9" * len(n))
        # diff4 = abs(case2 - (int)(n))
        # case5 = (int)("1" + "0" * (len(n) - 2) + "1")
        # diff5 = abs(case2 - (int)(n))
        # minDiff = 1e9
        # minCase = ""
        # for case, diff in [(case1, diff1), (case2, diff2), (case3, diff3), (case4, diff4), (case5, diff5)]:
        #     if diff < minDiff:
        #         minCase, minDiff = case, diff
        #     elif diff == minDiff:
        #         if case < minCase:
        #             minCase = case
        # print('n = ', n)
        # print('case1', case1)
        # print('case2', case2)
        # print('case3', case3)
        # print('case4', case4)
        # print('case5', case5)
        # # print(case1, case2, case3, case4, case5)
        # return minCase

# n = "1234"
n = "123" # 121
n = "1" # 0
# # n = "1213"
n = "10" # 9
n = "11" # 9
n = "100" # -> 101 or 99
print(Solution().nearestPalindromic(n))