from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        parents = defaultdict(tuple)

        for x, y in stones:
            parents[(x, y)] = (x, y)

        def find(x, y):
            while (x, y) != parents[(x, y)]:
                x, y = parents[(x, y)]
            return (x, y)

        def union(x1, y1, x2, y2):
            root1 = find(x1, y1)
            root2 = find(x2, y2)
            parents[root1] = root2

        # print(parents)
        results = len(stones)
        for i in range(len(stones) - 1):
            x1, y1 = stones[i][0], stones[i][1]
            for j in range(i + 1, len(stones)):
                if i != j:
                    x2, y2 = stones[j][0], stones[j][1]
                    if (x1 == x2 or y1 == y2) and find(x1, y1) != find(x2, y2):
                        # print('unioning ', x1, y1, x2, y2)
                        union(x1, y1, x2, y2)
                        results -= 1
        # print('after')
        # for k, v in parents.items():
        #     print(k, v)
        return len(stones) - results

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] # 5
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]] # 3
stones = [[0,0]] # 0 
print(Solution().removeStones(stones))