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
def is_jaeum(i):
    return 0 <= i <= 13
def is_moeum(i):
    return 14 <= i <= 34
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
q = deque()
q.append((0, 0, 1, 1))
min_len = int(1e9)
visited = [[[int(1e9)] * 4 for _ in range(m)] for _ in range(n)]
if is_moeum(board[0][0]):
    print('BAD')
    exit(0) 
visited[0][0][1] = 1
min_len = int(1e9)
while q:
    x, y, last_type, length = q.popleft()
    if x == n-1 and y == m-1 and 2 <= last_type <= 3:
        min_len = min(min_len, length)
        continue
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if last_type == 1 and is_moeum(board[nx][ny]):
                if visited[nx][ny][2] >= length:
                    visited[nx][ny][2] = length
                    q.append((nx, ny, 2, length))
            elif last_type == 2 and is_jaeum(board[nx][ny]):
                if visited[nx][ny][1] >= length + 1:
                    visited[nx][ny][1] = length + 1
                    q.append((nx, ny, 1, length + 1))
                if visited[nx][ny][3] > length:
                    visited[nx][ny][3] = length
                    q.append((nx, ny, 3, length))
            elif last_type == 3 and is_jaeum(board[nx][ny]):
                if visited[nx][ny][1] >= length + 1:
                    visited[nx][ny][1] = length + 1
                    q.append((nx, ny, 1, length + 1))
print('BAD' if min_len == int(1e9) else min_len)
