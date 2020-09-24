import sys
sys.setrecursionlimit(100000)
import heapq
from collections import deque
from itertools import combinations, permutations, combinations_with_replacement
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)
for t in range(3):
    dp = [[int(1e9)] * 3 for _ in range(n)]
    dp[0][t] = house[0][t]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]
    for i in range(3):
        if i == t: continue
        result = min(result, dp[n-1][i])
print(result)