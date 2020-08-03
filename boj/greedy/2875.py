import sys
import math
n, m, k = list(map(int, sys.stdin.readline().split()))
teams = 0
for _ in range(0, n + m):
    if n == 0 or n == 1 or m == 0:
        break
    n -= 2
    m -= 1
    teams += 1
if n + m >= k:
    print(teams)
    exit()
k -= n + m
print(teams - math.ceil((k)/3))