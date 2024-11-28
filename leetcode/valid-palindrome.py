class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s = s.replace(' ', '')
        # ss = ""
        # for i in range(len(s)):
        #     if 'z' >= s[i].lower() >= 'a' or '9' >= s[i].lower() >= '0':
        #         ss += s[i].lower()
        # print('ehem', ss)
        # s = ss

        def isAlNum(char):
            if (char >= '0' and char <= '9') or (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
            # if ('9' >= char >= '0') or ('z' >= char >= 'a') or ('Z' >= char >= 'A'):
                return True
            return False

        left = 0
        right = len(s) -1
        while left <= right:
            # print(0, left, right)
            while left < len(s) and not isAlNum(s[left]):
                # print(1)
                left += 1
            while right >= 0 and not isAlNum(s[right]):
                # print(2)
                right -= 1
            if left < len(s) and right >= 0 and s[left].lower() != s[right].lower():
                break
            # while s[left].lower() == s[right].lower():
            #     print(3)
            left += 1
            right -= 1
            # if s[left] == s[right]:
            #     left += 1
            #     right -= 1
            # else:
            #     break
        # print(left, right)
        return left >= right

input = "A man, a plan, a canal: Panama" # true
# input = " " # true
# input = "race a car" # false 
# race raca
print(Solution().isPalindrome(input))