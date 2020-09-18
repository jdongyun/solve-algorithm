import sys
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
mod = 1_000_000_009
dp = [[0] * 1001 for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1
psum = [[0] * 1001 for _ in range(1001)]
for i in range(1, 4):
    for j in range(1, i + 1):
        psum[i][j] = psum[i][j-1] + dp[i][j]
for i in range(4, 1001):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i-1][j-1] % mod + dp[i-2][j-1] % mod + dp[i-3][j-1] % mod) % mod
        psum[i][j] = (psum[i][j-1] % mod + dp[i][j] % mod) % mod
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(psum[n][m])
