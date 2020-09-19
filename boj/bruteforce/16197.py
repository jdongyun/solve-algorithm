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

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())

board = []
board.append(['x'] * (m + 2))
for _ in range(n):
    board.append(['x'] + list(input()) + ['x'])
board.append(['x'] * (m + 2))
coin = []
for i in range(n + 2):
    for j in range(m + 2):
        if board[i][j] == 'o':
            coin.append((i, j))
            board[i][j] = '.'

visited = [[[[False] * (m + 2) for _ in range(n + 2)] for _ in range(m + 2) ] for _ in range(n + 2)]

q = deque()
q.append((*coin[0], *coin[1], 0))
ret = -1
while q:
    x1, y1, x2, y2, cnt = q.popleft()
    if cnt > 10: continue
    if board[x1][y1] == board[x2][y2] == 'x':
        continue
    if (board[x1][y1] == '.' and board[x2][y2] == 'x') or \
        (board[x1][y1] == 'x' and board[x2][y2] == '.'):
        ret = cnt
        break
    for dx, dy in directions:
        nx1, ny1, nx2, ny2 = x1, y1, x2, y2
        if board[nx1 + dx][ny1 + dy] != '#':
            nx1, ny1 = nx1 + dx, ny1 + dy
        if board[nx2 + dx][ny2 + dy] != '#':
            nx2, ny2 = nx2 + dx, ny2 + dy
        if not visited[nx1][ny1][nx2][ny2]:
            visited[nx1][ny1][nx2][ny2] = True
        q.append((nx1, ny1, nx2, ny2, cnt + 1))
print(ret)
