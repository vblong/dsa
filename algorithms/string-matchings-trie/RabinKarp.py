

def bruteForce(s, t):
    m = len(s)
    n = len(t)
    if m < n:
        return -1
    
    for i in range(m - n):
        for j in range(n):
            if s[i + j] != t[j]:
                break
        if j >= n - 1:
            return i
    return -1

def rabinKarp(s, t):
    m = len(s)
    n = len(t)
    if m < n:
        return -1
    mod = 1e9 + 7
    sHash, tHash = 0, 0
    for i in range(n):
        tHash += ((1 << (n - i - 1)) * ord(t[i])) % mod
        sHash += ((1 << (n - i - 1)) * ord(s[i])) % mod
    
    if tHash == sHash:
        if s[:n] == t:
            return i - n + 1
    for i in range(n, m):
        sHash = (2 * (sHash - ord(s[i - n]) * ((1 << (n - 1)) % mod)) + ord(s[i])) % mod
        if sHash == tHash:
            if s[i-n+1:i+1] == t:
                return i - n + 1
        # print('final =======>', s[i], sHash, tHash, sHash == tHash)    
    return -1

# problem: find first occurence of target in source
source = "LeetCodeYeah" # 12
target = "eah" # 4

# print(bruteForce(source, target))
print(rabinKarp(source, target))
# print(ord('C'), ord('o'), ord('d'), ord('e'))
# print(ord('C') * (1 << 3), ord('o') * (1 << 2), ord('d') * (1 << 1), ord('e') * (1 << 0))
# print(ord('C') * (1 << 3) + ord('o') * (1 << 2) + ord('d') * (1 << 1) + ord('e') * (1 << 0))
# print(ord('L') * (1 << 3) + (ord('e') * (1 << 2) + ord('e') * (1 << 1) + ord('t') * (1 << 0)) * 2 - ord('L') * (1 << 3) + ord('C') )