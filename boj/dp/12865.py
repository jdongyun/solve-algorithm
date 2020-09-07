import sys
from collections import deque
from itertools import combinations, permutations
input = lambda: sys.stdin.readline().rstrip() 

n, k = map(int, input().split())
prod = [0] + [list(map(int, input().split())) for _ in range(n)]
d = [[0] * (k+1) for _ in range(n+1)]
if prod[1][0] <= k:
    d[1][prod[1][0]] = prod[1][1]

for i in range(2, n+1):
    weight, value = prod[i]

    for j in range(1, k+1):
        if d[i-1][j] > 0:
            d[i][j] = d[i-1][j]
    
    if weight <= k:
        d[i][weight] = max(d[i][weight], value)
    
    for w in range(1, k+1):
        if d[i-1][w] > 0 and weight + w <= k:
            d[i][weight + w] = max(d[i][weight + w], d[i-1][w] +value) 
print(max(d[n]))
