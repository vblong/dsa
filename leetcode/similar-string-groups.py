class Solution:
    def numSimilarGroups(self, strs) -> int:
        parents = {}
        count = len(strs)

        def union(str1, str2):
            root1, root2 = find(str1), find(str2)
            parents[root1] = root2

        def find(str):
            while str != parents[str]:
                str = parents[str]
            return str

        def isSimilar(str1, str2):
            diffs = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diffs += 1
            return diffs == 2 or diffs == 0

        for s in strs:
            parents[s] = s

        # print('start', parents)      
        n = len(strs)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    union(strs[i], strs[j])
                    count -= 1
        # print('after-', parents)
        # print()
        # print(set([find(k) for k in parents.keys()]))
        return len(set([find(k) for k in parents.keys()]))

        

strs = ["tars","rats","arts","star"] # 2
# strs = ["omv","ovm"] # 1
# strs = [
#     "qihcochwmglyiggvsqqfgjjxu","gcgqxiysqfqugmjgwclhjhovi","gjhoggxvcqlcsyifmqgqujwhi","wqoijxciuqlyghcvjhgsqfmgg","qshcoghwmglygqgviiqfjcjxu",
#     "jgcxqfqhuyimjglgihvcqsgow","qshcoghwmggylqgviiqfjcjxu","wcoijxqiuqlyghcvjhgsqgmgf","qshcoghwmglyiqgvigqfjcjxu","qgsjggjuiyihlqcxfovchqmwg",
#     "wcoijxjiuqlyghcvqhgsqgmgf","sijgumvhqwqioclcggxgyhfjq","lhogcgfqqihjuqsyicxgwmvgj","ijhoggxvcqlcsygfmqgqujwhi","qshcojhwmglyiqgvigqfgcjxu",
#     "wcoijxqiuqlyghcvjhgsqfmgg","qshcojhwmglyiggviqqfgcjxu","lhogcgqqfihjuqsyicxgwmvgj","xscjjyfiuglqigmgqwqghcvho","lhggcgfqqihjuqsyicxgwmvoj",
#     "lhgocgfqqihjuqsyicxgwmvgj","qihcojhwmglyiggvsqqfgcjxu","ojjycmqshgglwicfqguxvihgq","sijvumghqwqioclcggxgyhfjq","gglhhifwvqgqcoyumcgjjisqx"] # 11
print(Solution().numSimilarGroups(strs))