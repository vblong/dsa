from collections import deque
import math
class Solution:
    def nthUglyNumber(self, num: int) -> int:
        # def valid(n):
        #     if n == 1:
        #         return True
        
        #     while n % 2 == 0:
        #         n = n // 2
                
        #     for i in range(3,int(math.sqrt(n))+1,2):
        #         # while i divides n , print i and divide n
        #         while n % i== 0:
        #             if i not in [2, 3, 5]:
        #                 return False
        #             n = n / i
                    
        #     # Condition if n is a prime
        #     # number greater than 2
        #     if n > 2 and n not in [ 2, 3, 5]:
        #         return False
            
        #     return True

        # k = 0
        # val = 1
        # while k < num:
        #     if valid(val):
        #         k += 1
        #     if k == num:
        #         break
        #     val += 1
        # return val
        uglyNums = [1]
        q = deque([1])
        l = 1
        while True:
            seed = q.popleft()
            for factor in [2, 3, 5]:
                newNum = seed * factor
                if newNum not in uglyNums:
                    uglyNums.append(seed * factor)
                    q.append(seed * factor)
            if len(uglyNums) >= num:
                break
        uglyNums.sort()
        print(uglyNums)
        return uglyNums[num - 1]
    
n = 10 # 12
# n = 1 # 1
print(Solution().nthUglyNumber(n))