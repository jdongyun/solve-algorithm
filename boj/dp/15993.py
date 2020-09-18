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
dp = [[0] * 2 for _ in range(100_001)]
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 2
dp[3][1] = 2

for i in range(4, 100_001):
    dp[i][0] = (dp[i-1][1] % mod + dp[i-2][1] % mod + dp[i-3][1] % mod) % mod
    dp[i][1] = (dp[i-1][0] % mod + dp[i-2][0] % mod + dp[i-3][0] % mod) % mod

for _ in range(int(input())):
    n = int(input())
    print(dp[n][1], dp[n][0])
