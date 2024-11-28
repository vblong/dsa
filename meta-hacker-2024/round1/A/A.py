import sys
from typing import List
sys.stdin = open('input_full.txt', 'r') 
sys.stdout = open('output.txt', 'w')
t = int(input(), 10)

def solve(stations: List[List[int]]):
    allMinSpeed = 0
    stationMinMax = []
    for i, [a, b] in enumerate(stations):        
        maxSpeed = (i + 1) / a if a > 0 else float("inf")
        minSpeed = (i + 1) / b if b > 0 else 0
        stationMinMax.append((minSpeed, maxSpeed))
        if minSpeed != 0:
            allMinSpeed = max(allMinSpeed, minSpeed)

    for va, vb in stationMinMax:
        if allMinSpeed < va or allMinSpeed > vb: 
            return -1
    return allMinSpeed

for test in range(t):
    n = input()
    n = int(n)
    stations = []
    for i in range(n):
        a, b = input().split(' ')
        a, b = (int)(a), (int)(b)        
        stations.append([a, b])
    res = solve(stations)
    print(f'Case #{test+1}: ', res)
    # print(n, k, s)