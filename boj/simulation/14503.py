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
n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, -1, 0), (1, 0, 1), (2, 1, 0), (3, 0, -1)] * 2

while True:
    if board[x][y] == 0:
        board[x][y] = 2
    flag = False
    for di, dx, dy in directions[d:d+4][::-1]:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == 0:
            flag = True
            d = di
            x, y = nx, ny
            break
    if flag: continue
    di, dx, dy = directions[d]
    nx, ny = x - dx, y - dy
    if board[nx][ny] == 1:
        break
    else:
        x, y = nx, ny

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            cnt += 1
print(cnt)
