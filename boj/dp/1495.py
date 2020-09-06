import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 
n, s, m = map(int, input().split())
vols = [0] + list(map(int, input().split()))
d = [[False for _ in range(1001)] for _ in range(101)]
d[0][s] = True
for i in range(1, n+1):
    v = vols[i]
    for j in range(m+1):
        if d[i-1][j] and 0 <= j-v <= m:
            d[i][j-v] = True
        if d[i-1][j] and 0 <= j+v <= m:
            d[i][j+v] = True
for i in range(m, -1, -1):
    if d[n][i]:
        print(i)
        exit(0)
print(-1)
