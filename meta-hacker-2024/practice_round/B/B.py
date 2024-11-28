import sys
sys.stdin = open("B_inp_small.txt")
sys.stdin = open("B_inp_large.txt")
sys.stdout = open("output.txt", "w")

def nRoot(num: int, n: int) -> float:
    return num**(1/n)

def solve(n: int, p: int) -> float:
    p = p / 100.0
        
    # Compute the new probability P'
    p_prime = 100 * (p ** ((n-1)/n))
        
    # Calculate the difference (increase in percentage)
    delta_P = p_prime - (p * 100)
    return delta_P

t = (int)(input())
for test in range(t):
    n, p = input().split(' ')
    n, p = (int)(n), (int)(p)
    res = solve(n, p)
    print(f'Case #{test+1}: ', res)