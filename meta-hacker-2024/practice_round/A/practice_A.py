import sys
from typing import List
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')
t = int(input(), 10)

def solve(s: List[int], n: int, k: int) -> bool:
    s.sort()
    if len(s) == 1:
        return s[0] <= k
    totalTime = 0
    for i in range(len(s) - 1, 0, -1):
        totalTime += s[0]
        if i > 1:
            totalTime += s[0]
        # if totalTime > k:
        #     return False
    # print("total time", totalTime)
    return totalTime <= k

for test in range(t):
    n, k = input().split(' ')
    n, k = int(n), (int)(k)
    s = []
    for i in range(n):
        s.append(int(input(), 10))
    res = solve(s, n, k)
    print(f'Case #{test+1}: ', "YES" if res else "NO")
    # print(n, k, s)