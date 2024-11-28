from collections import defaultdict
import math
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        results = 0
        x, y = 0, 0
        directions = [
            (0, 1), # up
            (-1, 0), # left
            (0, -1), # down
            (1, 0) # right
        ]
        currDiractionIdx = 0
        obs = defaultdict(list)
        for ox, oy in obstacles:
            obs[ox].append(oy)
        # print(obs, 0+2 in obs and 0+4 in obs[0+2])
        for c in commands:
            if c == -2:                
                currDiractionIdx = (currDiractionIdx + 1) % 4
            elif c == -1:
                currDiractionIdx = (currDiractionIdx - 1) % 4
            else:
                k = c
                dx, dy = directions[currDiractionIdx]
                while k:
                    k -= 1
                    if x+dx in obs and y+dy in obs[x+dx]:
                        continue
                    x, y = x + dx, y + dy
                    results = max(results, (abs(x-0)**2 + abs(y-0)**2))
        return results
commands, obstacles = [4,-1,3], [] # 25
# commands, obstacles = [4,-1,4,-2,4], [[2,4]] # 65
commands, obstacles = [6,-1,-1,6], [] # 36
print(Solution().robotSim(commands, obstacles))