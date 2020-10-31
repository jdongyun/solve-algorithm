import bisect
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
dp_max = [[0] * 3 for _ in range(2)]
dp_min = [[0] * 3 for _ in range(2)]
for _ in range(n):
    arr = list(map(int, input().split()))
    dp_max[1][0] = max(dp_max[0][0], dp_max[0][1]) + arr[0]
    dp_max[1][1] = max(dp_max[0]) + arr[1]
    dp_max[1][2] = max(dp_max[0][1], dp_max[0][2]) + arr[2]
    dp_max[0][0] = dp_max[1][0]
    dp_max[0][1] = dp_max[1][1]
    dp_max[0][2] = dp_max[1][2]
    dp_max[1][0] = dp_max[1][1] = dp_max[1][2] = 0

    dp_min[1][0] = min(dp_min[0][0], dp_min[0][1]) + arr[0]
    dp_min[1][1] = min(dp_min[0]) + arr[1]
    dp_min[1][2] = min(dp_min[0][1], dp_min[0][2]) + arr[2]
    dp_min[0][0] = dp_min[1][0]
    dp_min[0][1] = dp_min[1][1]
    dp_min[0][2] = dp_min[1][2]
    dp_min[1][0] = dp_min[1][1] = dp_min[1][2] = 0

    del arr

print(max(dp_max[0]), min(dp_min[0]))