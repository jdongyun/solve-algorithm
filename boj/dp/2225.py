import sys
input = lambda: sys.stdin.readline().rstrip() 
mod = 1_000_000_000
n, k = map(int, input().split())
d = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, k+1):
    d[1][i] = i
for i in range(1, n+1):
    d[i][1] = 1
for i in range(2, n+1):
    for j in range(2, k+1):
        d[i][j] = (d[i-1][j] % mod + d[i][j-1] % mod) % mod
print(d[n][k] % mod)
