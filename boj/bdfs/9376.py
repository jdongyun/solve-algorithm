# https://naivep.tistory.com/58 를 참고하였음.

import sys
import heapq
from collections import deque
from itertools import combinations, permutations
input = lambda: sys.stdin.readline().rstrip() 

test = False
if test:
    sys.stdin = open('input.txt', 'r')
    print('sys.stdin = input.txt')

for tc in range(int(input())):
    h, w = map(int, input().split())
    b = [list(input()) for _ in range(h)]
    board = [['.'] * (w + 2) for _ in range(h + 2)]
    prisoners = []
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            board[i][j] = b[i-1][j-1]
            if board[i][j] == '$':
                prisoners.append((i, j))
    def bfs(i, j):
        q = deque()
        visited = [[False] * (w + 2) for _ in range(h + 2)]
        dist = [[0] * (w + 2) for _ in range(h + 2)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited[i][j] = True
        dist[i][j] = 0
        q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                    if not visited[nx][ny]:
                        if board[nx][ny] == '.' or board[nx][ny] == '$':
                            visited[nx][ny] = True
                            dist[nx][ny] = dist[x][y]
                            q.appendleft((nx, ny))
                        if board[nx][ny] == '#':
                            visited[nx][ny] = True
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
        return dist

    v = [[int(1e9)] * (w + 2) for _ in range(h + 2)]
    b = [bfs(0, 0), bfs(*prisoners[0]), bfs(*prisoners[1])]

    min_v = int(1e9)
    for i in range(h+2):
        for j in range(w+2):
            if board[i][j] == '*':
                continue
            v[i][j] = b[0][i][j] + b[1][i][j] + b[2][i][j]
            if board[i][j] == '#':
                v[i][j] -= 2
            min_v = min(min_v, v[i][j])
    print(min_v)
