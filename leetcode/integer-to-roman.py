num = 3749
num = 58
num = 1994

bases = []
lead = []
b = 1
while num:
    rem = num % 10
    lead.append(rem)
    bases.append(rem * b)
    b *= 10
    num = num // 10

result = ""
print(lead)
print(bases)

while bases:
    b = bases.pop()
    l = lead.pop()
    if b >= 1000:
        while b:
            b -= 1000
            result += "M"
    elif 100 <= b < 1000:
        while b:
            if l == 5:
                result += "D"
                b, l = 0, 0
            elif l == 4:
                result += "CD"
                b, l = 0, 0
            elif l == 9:
                result += "CM"
                b, l = 0, 0
            else: # 1 2 3 6 7 8
                if b < 500: # 100 200 300
                    result += "C"
                    b -= 100
                    l -= 1
                else: # 600 700 800
                    result += "D"
                    b -= 500
                    l -= 5
    elif 10 <= b < 100:
        while b:
            if l == 5: # 50
                result += "L"
                b, l = 0, 0
            elif l == 4: # 40
                result += "XL"
                b, l = 0, 0
            elif l == 9: # 90
                result += "XC"
                b, l = 0, 0
            else:
                if b < 40: #10 20 30
                    result += "X"
                    b -= 10
                    l -= 1
                else: # 60 70 80
                    result += "L"
                    b -= 50
                    l -= 5
    else:
        while b:
            if l == 5:
                result += "V"
                b, l = 0, 0
            elif l == 4:
                result += "IV"
                b,l = 0, 0
            elif l == 9:
                result += "IX"
                b, l = 0, 0
            else:
                if b < 5: # 1 2 3
                    result += "I"
                    b -= 1
                    l -= 1
                else:
                    result += "V"
                    b -= 5
                    l -= 5
print(result)
