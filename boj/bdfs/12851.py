import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 

n, k = map(int, input().split())
d = [int(1e9)] * 100_001
q = deque([(n, 0)])
d[n] = 0
cnt = [0] * 100_001
cnt[n] = 1
while q:
    i, t = q.popleft()
    if i == k:
        continue
    for ni in [i-1, i+1, 2*i]:
        nt = t + 1
        if 0 <= ni <= 100_000 and d[ni] >= nt:
            d[ni] = nt
            cnt[ni] += 1
            q.append((ni, nt))
print(d[k])
print(cnt[k])
