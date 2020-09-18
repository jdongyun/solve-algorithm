# https://www.acmicpc.net/problem/15991
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
dp = [0] * 100_001
dp[0] = 1
dp[1] = 1
dp[2] = 2 # 2
dp[3] = 2 # 3
for i in range(4, 100_001):
    dp[i] = dp[i - 2] % mod
    if i >= 4:
        dp[i] += dp[i - 4] % mod
    if i >= 6:
        dp[i] += dp[i - 6] % mod
    dp[i] = dp[i] % mod
for _ in range(int(input())):
    print(dp[int(input())])
