class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        # brute force
        # count = [0] * 26
        # n = len(s)
        # results = 0
        # for i in range(n):
        #     count = [0] * 26
        #     maxCount = 0
        #     maxCharIdx = ""
        #     for j in range(i, n):
        #         count[ord(s[j]) - ord('A')] += 1
        #         if count[ord(s[j]) - ord('A')] > maxCount:
        #             maxCount = count[ord(s[j]) - ord('A')]
        #             maxCharIdx = ord(s[j]) - ord('A')
        #         strangeChars = 0
        #         for l in range(26):
        #             if l != maxCharIdx:
        #                 strangeChars += count[l]
        #         if strangeChars <= k:
        #             if j -i+1 > results:
        #                 results = j - i + 1
        #                 print('found at', i, j, results)
        #             # results = max(results, (j - i + 1))
        # return results

        # sliding window - slow & fast
        def valid(countArr, k):
            maxCount, maxIdx, strangeCount = 0, 0, 0
            for i in range(26):
                if countArr[i] > maxCount:
                    maxCount = countArr[i]
                    maxIdx = i
            for i in range(26):
                if i != maxIdx:
                    strangeCount += countArr[i]
            return strangeCount <= k
            
        slow = 0
        n = len(s)
        count = [0] * 26
        results = 0
        for fast in range(n):
            charIdx = ord(s[fast]) - ord('A')
            count[charIdx] += 1
            while not valid(count, k):
                count[ord(s[slow]) - ord('A')] -= 1
                slow += 1
            results = max(results, fast - slow + 1)
        return results

s, k = "EQQEJDOBDPDPFPEIAQLQGDNIRDDGEHJIORMJPKGPLCPDFMIGHJNIIRSDSBRNJNROBALNSHCRFBASTLRMENCCIBJLGAITBFCSMPRO", 2 # 5
s, k = "EQQEJDOBDPDPFPEI", 2 # 5
# 9 -> 13: PDPFP -> PPPPP
print(Solution().characterReplacement(s, k))