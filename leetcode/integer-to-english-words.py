class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        n2w = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five', 
            6: 'Six', 
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }

        def toLeadWords(value):            
            words = ""
            # 1 -> 99
            if value < 100:
                if value in n2w:
                    return n2w[value]
                unit = value % 10
                dozen = (value // 10) * 10
                if dozen > 0:
                    words += n2w[dozen]
                    if unit > 0:
                        words += " "
                if unit > 0:
                    words += n2w[unit]
            else:
                # 100 -> 999
                words = ""
                unit = value % 10
                dozen = ((value // 10) % 10)
                h = ((value // 10) // 10) * 100
                hundredLead = h // 100
                words += n2w[hundredLead] + " " + n2w[100]
                if dozen * 10 + unit > 0:
                    if dozen * 10 + unit < 10:
                        words += " " + toLeadWords(dozen * 10 + unit)
                    else:
                        words += " " + toLeadWords(dozen * 10 + unit)
            return words
        
        result = ""
        unit, dozen, hundred, thousand, million, billion = 0,0,0,0,0,0
        nums = []
        bases = 1
        while num:
            nums.append((num % 10) * bases)
            num = num // 10
            bases *= 10
        
        for n in nums:
            if n < 10:
                unit += n
            elif 10 <= n < 100:
                dozen += n
            elif 100 <= n < 1_000:
                hundred += n
            elif 1_000 <= n < 1_000_000:
                thousand += n
            elif 1_000_000 <= n < 1000_000_000:
                million += n
            else:
                billion += n
        print(unit, dozen, hundred, thousand, million, billion)

        if billion:
            if len(result):
                result += " "
            result += toLeadWords(billion // 1000_000_000) + " Billion"
        if million // 1000_000:
            if len(result):
                result += " "
            result += toLeadWords(million // 1000_000) + " Million"            
        if thousand // 1000:
            if len(result):
                result += " "
            result += toLeadWords(thousand // 1000) + " Thousand"
        if unit + dozen + hundred:
            if len(result):
                result += " "
            result += toLeadWords(unit + dozen + hundred)
                
        # return toLeadWords(567)
        return result
    
a = Solution().numberToWords(101)
print(a)
