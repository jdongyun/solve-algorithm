from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys
import math

sys.setrecursionlimit(100_000)
input = lambda: sys.stdin.readline().rstrip() 
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

n = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3
for i in range(4, 31):
    if (i * 3) % 2 == 0:
        dp[i] = dp[i-2] * 3
        for j in range(i-4, -1, -2):
            # 왼쪽부분(dp[j]개) * 오른쪽부분(뒤집어서 총 2개)
            dp[i] += dp[j] * 2
print(dp[n])