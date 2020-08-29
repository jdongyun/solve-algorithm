n = int(input())
d = [0] * 1_000_001
mod = 1_000_000_009
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 1_000_001):
    d[i] = (d[i-1] % mod + d[i-2] % mod + d[i-3] % mod) % mod
for _ in range(n):
    k = int(input())
    print(d[k] % mod)
