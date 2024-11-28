from bisect import bisect_right
import math
import sys
from typing import List
# sys.stdin = open('input_full.txt', 'r') 
sys.stdin = open('input.txt', 'r') 
# sys.stdin = open('input_1.txt', 'r') 
# sys.stdout = open('output.txt', 'w')
t = int(input(), 10)

def expected_days(W, G, L):
    if L == 0:
        return W - G  # Directly return the difference

    # Let's compute the expected number of days with L > 0
    W_eff = W - G  # Effective weight difference
    L_eff = L

    # Using the derived formula based on previous results in the sequence:
    # E(W) = (W_eff + 1) * (W_eff + 2) / 2 + W_eff * L_eff
    # This is a generalization; adapt it based on testing with real calculations
    num_days = (W_eff + 1) * (W_eff + 2) / 2 + W_eff * L_eff

    return num_days


def modular_inverse(a, mod):
    return pow(a, mod - 2, mod)

def solve(w, g, l):
    if w == g: return 0
    mod = 998244353
    # expected = expected_days(w, g, l)
    # p, q = expected, 1  # p/q is expressed as an integer in lowest terms
    # inv_q = modular_inverse(q, mod)  # q is 1, so its inverse is also 1
    # result = (p * inv_q - 1) % mod
    
    # return result
    if l == 0: return (w - g) % mod

    wEffective = w - g
    lEffective = l
    p = (((wEffective + 1) * (wEffective + 2)) // 2) + (wEffective * lEffective)
    q = 1
    invq = modular_inverse(q, mod)

    return (p * invq) % mod

for test in range(t):
    line = input()
    w, g, l = line.split(' ')
    w, g, l = (int)(w), (int)(g), (int)(l)
    print(f'Case #{test+1}: ', solve(w, g, l))