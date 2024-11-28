
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        ######## BRUTE FORCE
        # def isSpecial(num):
        #     count = [0] * 10
        #     while num:
        #         count[num % 10] += 1
        #         if count[num%10] > 1:
        #             return False
        #         num = num // 10
        #     return True
        # cnt = 0
        # for i in range(100, 200):
        #     if isSpecial(i):
        #         cnt += 1
        # return cnt
        
        ##############################
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        digits.reverse()
        
        print(digits)
        def dp(i, tight, chosenDigit):
            if i == len(digits):
                return 1
            ans = 0
            maxDigit = digits[i] if tight else 10
            for d in range(maxDigit + 1):
                # out of range
                if d >= 10:
                    continue
                # digit d has been chosen
                if chosenDigit & (1 << d):
                    continue
                # set chosen bit 
                newChosenDigit = 0 if (chosenDigit == 0 and d == 0) else (chosenDigit | (1 << d))
                ans += dp(i + 1, d == maxDigit, newChosenDigit)
            return ans
        return dp(0, True, 0) - 1
        

        ##########################
        # num = list(map(int, str(n)))

        # def dp(pos: int, tight: bool, chosen_digit: int) -> int:
        #     if pos == len(num): return 1
        #     res = 0
        #     bound = num[pos] if tight else 10
        #     for i in range(bound + 1):
        #         if i == 10: 
        #             continue
        #         if chosen_digit & (1 << i): 
        #             continue 
        #         new_tight = i == bound
        #         new_chosen_digit = 0 if chosen_digit == 0 and i == 0 \
        #                              else chosen_digit | (1 << i)
        #         res += dp(pos + 1, new_tight, new_chosen_digit)
        #     return res

        # return dp(0, True, 0) - 1


n = 20 # 19
# n = 5 # 5
# n = 135 # 110
# n = 365 # 279
print(Solution().countSpecialNumbers(n))