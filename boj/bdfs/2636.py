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

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1 ,0), (1, 0), (0, 1), (0, -1)]
def get_count():
    ret = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                ret += 1
    return ret

recent = 0
for t in range(1000):
    temp_count = get_count()
    if temp_count == 0:
        print(t)
        print(recent)
        exit(0)
    recent = temp_count

    outers = []
    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        outers.append((nx, ny))
                        visited[nx][ny] = True
                    elif board[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    for x, y in outers:
        board[x][y] = 0
    