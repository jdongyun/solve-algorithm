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
mod = 9901

n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2, n + 1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod
print(sum(dp[n]) % mod)