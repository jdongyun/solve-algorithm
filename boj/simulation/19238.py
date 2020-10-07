from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys

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

n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
now_x, now_y = [x-1 for x in list(map(int, input().split()))]


start_board = [[-1] * n for _ in range(n)]
start, end = [], []
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    start.append((x1-1, y1-1))
    end.append((x2-1, y2-1))
    start_board[x1-1][y1-1] = i

distances = [int(1e9)] * m
for ith_passenger in range(m):
    start_x, start_y = start[ith_passenger]
    end_x, end_y = end[ith_passenger]
    visited = [[False] * n for _ in range(n)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    while q:
        x, y, d = q.popleft()
        if (x, y) == (end_x, end_y):
            distances[ith_passenger] = d
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and \
                    not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))

finished = [False] * m

def next_near_loc(now_x, now_y):
    visited = [[False] * n for _ in range(n)]
    q = deque([(now_x, now_y, 0)])
    visited[now_x][now_y] = True
    min_dist = int(1e9)
    min_x, min_y = n, n
    while q:
        x, y, d = q.popleft()
        if d > min_dist:
            continue
        if start_board[x][y] != -1:
            if not finished[start_board[x][y]]:
                min_dist = d
                min_x, min_y = min((min_x, min_y), (x, y))
                continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and \
                    not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))
    if min_dist == int(1e9):
        return None
    finished[start_board[min_x][min_y]] = True
    return min_x, min_y, min_dist

for _ in range(m):
    next_near = next_near_loc(now_x, now_y)
    if next_near == None:
        print(-1)
        exit(0)
    nx, ny, dist_to_start = next_near
    
    ith = start_board[nx][ny]
    dist_to_end = distances[ith]
    if fuel < dist_to_start + dist_to_end:
        print(-1)
        exit(0)
    fuel = fuel - dist_to_start + dist_to_end

    now_x, now_y = end[ith]
print(fuel)