from bisect import bisect_right
import math
import sys
from typing import List
sys.stdin = open('input_full.txt', 'r') 
# sys.stdin = open('input.txt', 'r') 
# sys.stdin = open('input_1.txt', 'r') 
sys.stdout = open('output.txt', 'w')
t = int(input(), 10)

def sieve(n):
    isPrimes = [True] * (n+1)
    isPrimes[0] = isPrimes[1] = False
    p = 2
    while p * p <= n:
        if isPrimes[p]:
            for i in range(p*p, n+1, p):
                isPrimes[i] = False
        p += 1
    
    primes = [i for i in range(2, n + 1) if isPrimes[i]]
    return primes, isPrimes


def solve(n: int, primes: List[int], isPrimes: List[bool]):
    n_subtract = set()
    for i in range(len(primes)):
        if primes[i] > n: break
        if isPrimes[primes[i] - 2]:
            n_subtract.add(primes[i] - 2)
            n_subtract.add(primes[i]- (primes[i] - 2))
        # for j in range(0, i):
        #     if i != j and isPrimes[primes[i] - primes[j]]:
        #         print('found', primes[i], primes[j], 'diff=',primes[i] - primes[j])
        #         n_subtract.add(primes[i] - primes[j])
    # print('all is', n_subtract)
    return len(n_subtract)

primes, isPrimes = sieve(10**7)
for test in range(t):
    n = input()
    n = int(n)
    # primes, isPrimes = sieve(n)
    # print('primes are', primes)
    print(f'Case #{test+1}: ', solve(n, primes, isPrimes))