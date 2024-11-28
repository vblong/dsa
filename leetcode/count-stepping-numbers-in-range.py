from functools import lru_cache
import string
from typing import List


class Solution:
    def countSteppingNumbers(self, start: str, end: str) -> int:
        a = (int)(end)
        print(a, type (a))
        # 1: a > b
        # 0: a == b
        # -1: a < b
        @lru_cache(None)
        def compare(a: List[int], b: List[int]):
            if len(a) > len(b):
                return 1
            if len(b) > len(a):
                return -1
            n = len(a)
            i = 0
            while i < n and a[i] == b[i]: i += 1
            if i >= n:
                return 0
            if a[i] > b[i]:
                return 1
            return -1

        # def f(pos, state, prev, n):    
        #     if pos == n:
        #         return 0
        #     # all 0s
        #     all0 = True
        #     for c in state:
        #         if c != '0':
        #             all0 = False
        #             break
        #     ans = 0
        #     if compare(state, start) != -1 and compare(state, end) != 1 and not all0:
        #         ans += 1

        #     for choice in [prev-1, prev+1]:
        #         if prev >= 0 and prev <= 9:
        #             ans += f(pos + 1, state + (str)(choice), choice, n)
        #     return ans
        @lru_cache(maxsize=None)
        def f(pos, state, prev, n):
            # print(pos, state, prev, n)
            # print(list(state) + [1])
            if pos == n:
                return 0
            
            all0 = True
            for c in list(state):
                if c != 0:
                    all0 = False
                    break
            ans = 0
            if compare(list(state), start) != -1 and compare(list(state), end) != 1 and not all0:
                ans += 1

            for choice in [prev-1, prev+1]:
                if 0 <= prev <= 9:
                    ans += f(pos + 1, tuple(list(state) + [choice]), choice, n)
            return ans

                            
        start = [(int)(c) for c in list(start)]
        end = [(int)(c) for c in list(end)]
        res = 0
        # for i in range(1, 10):
        #     res += f(0, (i,), i, len(end))
        return res
    
low, high = "1", "11" # 10
low, high = "90", "101" # 2
low, high = "1", "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999" 
print(Solution().countSteppingNumbers(low, high))