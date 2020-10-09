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

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def remove(arr):
    new_arr = deepcopy(arr)
    flag = False
    s, c = 0, 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] != 0:
                c += 1
                s += arr[x][y] 
            for dx, dy in directions:
                nx, ny = x + dx, (y + dy) % len(arr[0])
                if 0 <= nx < len(arr):
                    if arr[x][y] == arr[nx][ny] != 0:
                        flag = True
                        new_arr[x][y] = new_arr[nx][ny] = 0
    arr = new_arr
    if c > 0 and not flag:
        avg = float(s) / c
        for x in range(len(arr)):
            for y in range(len(arr[0])):
                if arr[x][y] > 0:
                    if arr[x][y] < avg:
                        arr[x][y] += 1
                    elif arr[x][y] > avg:
                        arr[x][y] -= 1
    return arr

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, input().split())
    if d == 0: k = m - k
    for i in range(x, n+1, x):
        arr[i-1] = (arr[i-1] * 2)[k:k+m]
    arr = remove(arr)
s = 0
for i in range(n):
    s += sum(arr[i])
print(s)