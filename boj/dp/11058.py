import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
d = [0] * 101
d[1] = 1
d[2] = 2
d[3] = 3
for i in range(4, n+1):
    d[i] = d[i-1] + 1
    for j in range(1, i-3):
        # d[j] 에서 i-j번 붙여넣기 한 값 계산
        d[i] = max(d[i], d[j] * (i-j-1))
print(d[n])
