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

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
identity = [[0] * n for _ in range(n)]
for i in range(n):
    identity[i][i] = 1

def mul(a, b):
    ret = [[0] * n for _ in range(n)]
    z = list(zip(*b))
    for i in range(n):
        for j in range(n):
            ret[i][j] = sum([x*y for x, y in list(zip(a[i], z[j]))])
            ret[i][j] = ret[i][j] % 1000
    return ret

def pow(arr, cnt):
    if cnt == 0:
        return identity
    if cnt % 2 == 1:
        return mul(pow(arr, cnt - 1), arr)
    half = pow(arr, cnt // 2)
    return mul(half, half)
ret = pow(arr, b)
for i in range(n):
    print(*ret[i])