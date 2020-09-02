import sys
sys.setrecursionlimit(100000)
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 
n, k = map(int, input().split())
d = [int(1e9)] * 100_001
q = deque([(n, 0)])
parent = [0] * 100_001
d[n] = 0
while q:
    i, t = q.popleft()
    for ni in [i-1, i+1, 2*i]:
        nt = t + 1
        if 0 <= ni <= 100_000 and d[ni] > nt:
            d[ni] = nt
            q.append((ni, nt))
            parent[ni] = i
print(d[k])
def prints(i):
    if i == n:
        print(i, end=' ')
        return
    prints(parent[i])
    print(i, end=' ')
prints(k)
