import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 

w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]
c1, c2 = (-1, -1), (-1, -1)
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            if c1[0] == c1[1] == -1:
                c1 = (i, j)
            else:
                c2 = (i, j)
q = deque([(*c1, -1, -1)])
visited = [[int(1e9)] * w for _ in range(h)]
visited[c1[0]][c1[1]] = 0
directions = [(-1, 0, 0), (1, 0, 1), (0, 1, 2), (0, -1, 3)]
mirrors = int(1e9)
while q:
    x, y, arrow, cnt = q.popleft()
    if (x, y) == c2:
        mirrors = min(mirrors, cnt)
    for dx, dy, da in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            nc = cnt if arrow == da else cnt + 1
            if visited[nx][ny] >= nc:
                if board[nx][ny] == 'C' or board[nx][ny] == '.':
                    visited[nx][ny] = nc
                    q.append((nx, ny, da, nc))
print(mirrors)
