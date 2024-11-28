import sys
from typing import List
sys.stdin = open('input_full.txt', 'r') 
# sys.stdin = open('input.txt', 'r') 
# sys.stdin = open('input_1.txt', 'r') 
sys.stdout = open('output.txt', 'w')
t = int(input(), 10)

def genPeaks():
    peaks = set()
    
    for k in range(0, 9):  
        for start in range(1, 10 - k):  
            half = [str(start)]
            
            for _ in range(1, k + 1):
                half.append(str(int(half[-1]) + 1))
                
            peak_str = ''.join(half) + ''.join(reversed(half[:-1]))  
            peaks.add(int(peak_str))
    
    return sorted(peaks)

def solve(peaks, A, B, M):
    count = 0
    for peak in peaks:
        if A <= peak <= B and peak % M == 0:
            count += 1
    return count


peaks = genPeaks()
# print(peaks)
for test in range(t):
    a, b, m = input().split(' ')
    a, b, m = int(a), int(b), int(m)
    res = solve(peaks, a, b, m)
    print(f'Case #{test+1}: ', res)