import sys
from typing import List
sys.stdin = open('input_full.txt', 'r') 
# sys.stdin = open('input.txt', 'r') 
# sys.stdin = open('input_1.txt', 'r') 
sys.stdout = open('output.txt', 'w')
t = int(input(), 10)

def genMountains():
    
    # def f(i, n):
    #     # print(i, n, current)
    #     if i == n:
    #         s = [str(digit) for digit in current]
    #         mountains.add(int("".join(s)))
    #         return
        
    #     mid = n // 2
    #     maxN = max(current) if len(current) else 1
    #     if i == mid:
    #         for num in range(maxN+1, 10):
    #             current.append(num)
    #             f(i + 1, n)
    #             current.pop()
    #     elif i < mid:
    #         for num in range(maxN, 10):
    #             current.append(num)
    #             f(i + 1, n)
    #             current.pop()
    #     else:
    #         prev = current[-1]
    #         if i == mid + 1:
    #             prev -= 1
    #         for num in range(prev, 0, -1):
    #             current.append(num)
    #             f(i + 1, n)
    #             current.pop()

    def gen(length):
        prevLength = length - 2
        prevLengthNums = mountains[prevLength]
        # print('prev length', prevLength)
        # print('prev length nums', prevLengthNums)
        for num in prevLengthNums:
            asString = [digit for digit in str(num)]
            # print(asString)
            if length == 3:
                nextPrefix = nextSuffix = (int)(asString[0]) - 1
            else:
                nextPrefix = int(asString[0])
                nextSuffix = int(asString[-1])
            newNum = ['0'] + asString + ['0']
            for prefix in range(nextPrefix, 0, -1):
                for suffix in range(nextSuffix, 0, -1):
                    newNum[0] = str(prefix)
                    newNum[-1] = str(suffix)
                    if '0' in newNum: continue
                    mountains[length].add(int("".join(newNum)))
    mountains = {
        1: set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
        3: set([]),
        5: set([]),
        7: set([]),
        9: set([]),
        11: set([]),
        13: set([]),
        15: set([]),
        17: set([]),
        19: set([]), # not used
    }
    for length in range(3, 18, 2): # length is odd from 1 -> 19
        if length % 2 == 0: continue
        # print('at length', length)
        gen(length)
        
    return mountains

def solve(mountains, A, B, M):
    count = 0
    for k, v in mountains.items():
        nA, nB = len(str(A)), len(str(B))
        if nA <= k <= nB:
            for mountain in v:
                if A <= mountain <= B and mountain % M == 0:
                    count += 1
    return count

mountains = genMountains()
# print(mountains)
for test in range(t):
    a, b, m = input().split(' ')
    a, b, m = int(a), int(b), int(m)
    res = solve(mountains, a, b, m)
    print(f'Case #{test+1}: ', res)