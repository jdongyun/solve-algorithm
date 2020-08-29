import sys
input = lambda: sys.stdin.readline().rstrip()
d = [[0] * 4 for _ in range(100_001)]
mod = 1_000_000_009
d[1][1] = 1 # d[i][j]는 총합이 i인 수가 j로 시작하는 경우의 수
d[2][2] = 1
d[3][1] = 1
d[3][2] = 1
d[3][3] = 1

for i in range(4, 100_001):
    d[i][1] = (d[i-1][2] % mod + d[i-1][3] % mod) % mod
    d[i][2] = (d[i-2][1] % mod  + d[i-2][3] % mod) % mod
    d[i][3] = (d[i-3][1] % mod  + d[i-3][2] % mod) % mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % mod)
