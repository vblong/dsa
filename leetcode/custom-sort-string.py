class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        od = {}
        for i in range(len(order)):
            od[i] = order[i]
        
        freeChars = ""
        count = {} 
        for char in s:
            if char not in order:
                freeChars += char
            else:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] += 1
        
        for i in range(len(od)):
            if od[i] in count:    
                result += od[i] * (count[od[i]])
        return result + freeChars

order, s = "cba", "abcd" # "cbad"
# order, s = "bcafg", "abcd" # "bcad"
print(Solution().customSortString(order, s))