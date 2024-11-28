from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def f(i, numOpen, numClose, current):
            # print(i)
            nonlocal result
            if i == n * 2:
                result.append(current)
                return 
            if numOpen < n:
                f(i + 1, numOpen + 1, numClose, current + "(")
            if numOpen > numClose:
                f(i + 1, numOpen, numClose + 1, current + ")")

        f(0, 0, 0, "")
        return result
        
n = 3 # ["((()))","(()())","(())()","()(())","()()()"]
n = 1 # ["()"]
print(Solution().generateParenthesis(n))

