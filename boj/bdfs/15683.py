# https://www.acmicpc.net/problem/15683
import sys
import heapq
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

directions = \
[
    [],
    [
        [(-1, 0)],
        [(1, 0)],
        [(0, 1)],
        [(0, -1)]
    ],
    [
        [(-1, 0), (1, 0)],
        [(0, 1), (0, -1)]
    ],
    [
        [(-1, 0), (0, 1)],
        [(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(0, -1), (-1, 0)]
    ],
    [
        [(0, -1), (-1, 0), (0, 1)],
        [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)],
        [(1, 0), (0, -1), (-1, 0)]
    ],
    [
        [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ]
]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 6:
            board[i][j] = -5
        elif 1 <= board[i][j] <= 5:
            cctvs.append((i, j))
def set(ds, x, y, i):
    for dx, dy in ds:
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == -5: break
            if board[nx][ny] < 1 or board[nx][ny] > 5: 
                board[nx][ny] += i
            nx, ny = nx + dx, ny + dy

def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt

min_size = int(1e9)

def dfs(i):
    global min_size
    if i == len(cctvs):
        min_size = min(min_size, check())
        return
    cx, cy = cctvs[i]
    ct = board[cx][cy]
    for direction in directions[ct]:
        set(direction, cx, cy, 10)
        dfs(i+1)
        set(direction, cx, cy, -10)
dfs(0)
print(min_size)
